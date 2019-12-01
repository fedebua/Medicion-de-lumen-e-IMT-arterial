import cv2
from time import sleep
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QImage, QPixmap ,QMouseEvent
import numpy as np
from scipy import signal 
import csv
global point1_resized , point2_resized , point1_line_inf , point1_line_sup ,point2_line_inf,point2_line_sup, vector_diametro_interno, vector_intmed_sup, vector_intmed_inf
global borde_frameant,valores_y_intmedInf,vector_intmed_sup
global h2 
global Medida_pixels,Medida_cm,Medida_pixels_ajustada,LUMEN_MEDIDO,IMT_MEDIDO
LUMEN_MEDIDO = 0
IMT_MEDIDO_SUPERIOR = 0
IMT_MEDIDO_INFERIOR = 0
Medida_pixels_ajustada=0
Medida_pixels=0
Medida_cm=0
h2=1
valores_y_intmedInf = []
borde_frameant = []
point2_resized = []

point1_resized = []
point1_line_sup =[]
point2_line_sup =[]
point1_line_inf =[]
point2_line_inf =[]
vector_diametro_interno = []
vector_intmed_sup = []
vector_intmed_inf = []
class Thread(QThread):
	changePixmapOriginal = pyqtSignal(QPixmap)
	changePixmapEditado = pyqtSignal(QPixmap)
	terminoVideo = pyqtSignal(bool)
	editandoVideo = True
	#sigDatosDiamatro = pyqtSignal(np.ndarray)
	#sigDatosIntInf = pyqtSignal(np.ndarray)
	#sigDatosIntSup = pyqtSignal(np.ndarray)
	sigDatosDiamatro = pyqtSignal(list)
	sigDatosIntInf = pyqtSignal(list)
	sigDatosIntSup = pyqtSignal(list)

	sigClearGraficos = pyqtSignal()
	clicked = pyqtSignal()
	sigLabelEscala = pyqtSignal(str)
	
	## Señales de conexion con los labels que muestran los espesores medidos en el primer frame 
	sigLabelIMT=pyqtSignal(str)	
	sigLabelLumen=pyqtSignal(str)	

	def __init__(self, parent=None):
		QThread.__init__(self, parent=parent)
		 
		
		self.isRunning = True
		self.flag_ROI = True ## modificado de false a true
		self.flag_Line_Int_Med_Inf = False ## variable al pedo
		self.flag_Line_Int_Med_Sup = False ##  variable al pedo
		self.point1 = [] 
		self.point2 = []
		self.points = []

		self.count = 0

		self.drawing = False
		self.resize = False
		self.medir=False
		self.flag_1st_frame = True
		self.frame_cpy = []
		self.frame = []
		self.frame_crop =[]
		self.frame_crop_IMT =[]
		self.ret = False
		self.cap = []
		self.contraste=0
		self.brillo = 0 #Diámetro arterial

		self.brillo_IMT =0 #Íntima media
		self.contraste_IMT=0


		self.resolucion=10
		self.flag_vid_original = False
		self.flagCalibracion = False
		## variables donde guardo las confiuraciones del primer cuadro
		self.rect = [] 
		self.ymin = 0
		self.ymax =0
		
		self.flag_resized = False
		self.flag_procesar = False
												
		self.Reiniciado = False
		self.flag_mostrar_editado = False
		self.primerGrafico = False
		self.cant_frames = 0
		self.borde_cercano_actual=[]
		self.volverACalcular = False
		self.valores_y_intmedInf = []  

		self.canvas_heigth=0
		self.canvas_width=0
		
		self.signalPause=False
		self.w2 = 0
		self.hl=126.75222081783 ## medicion patron en pixels (5mm)
		self.dl1= 1.25984 ## mm patron escala
		self.scale_px=0

#==========AL LLAMAR AL MÉTODO START EJECUTA LA FUNCIÓN RUN================
	def run(self):  
		self.cap = cv2.VideoCapture("VAS_CAR_001.AVI")
		if(self.flagCalibracion==True):
			self.ret, self.frame = self.cap.read()
			cv2.destroyAllWindows() #destruye en caso de que haya ventanas abiertas por el ROI	
			while self.isRunning:			
				self.Calibrar()

			
		else:
			#self.resize=False	
			while self.isRunning :


					if(self.signalPause == False):
						self.ret, self.frame = self.cap.read()
					
					if(self.ret!=False):
						self.frame=cv2.resize(self.frame ,(self.canvas_width, self.canvas_heigth) )

					if (self.ret!=False):   #Si obtengo un cuadro válido

						if self.editandoVideo == True:
							self.procesar()
							
							self.editandoVideo = False   
						else:

							self.flag_resized = False
							self.frame_cpy = self.frame.copy()
							self.procesamiento()
							if self.flag_vid_original == True:
								mi_frame = self.frame
								self.flag_mostrar_editado = False
							else :
								mi_frame = cv2.convertScaleAbs(self.frame_crop, alpha=self.contraste, beta=self.brillo)
								mi_frame_IMT=cv2.convertScaleAbs(self.frame_crop_IMT, alpha=self.contraste, beta=self.brillo)
								self.cant_frames = self.cant_frames + 1

							self.mostrarVideo(mi_frame)
							self.flag_vid_original=True
							self.mostrarVideo(mi_frame_IMT)
							self.flag_vid_original=False
							
					else:
						if (self.primerGrafico==False):
							self.primerGrafico = True
							self.graficar()         
						#En caso de que termine de reproducir el video, mata al proceso y emite la señal para habilitar el botón

			self.stop()
		
	
	def mouse_drawing(self,event, x, y,flags,param):
		
		if event == cv2.EVENT_LBUTTONDOWN:
			
			if self.drawing is False:
				self.drawing = True
				self.point1 = (x, y)
				self.medir=False
				self.resize = False 
			else:
				self.medir=True
				self.resize = True
				self.drawing = False
			   
		
		elif event == cv2.EVENT_LBUTTONUP:
			
			if self.drawing is True:
				self.drawing = False
				self.point2 = (x, y)
				self.medir =True
				self.resize = True

	def Calibrar(self):
		global Medida_pixels,Medida_cm
		self.frame = cv2.resize(self.frame ,(self.canvas_width , self.canvas_heigth) )
		
		cv2.imshow("frame-calib",self.frame) ## muestro el video original 
		cv2.namedWindow("frame-calib")
		cv2.setMouseCallback("frame-calib", self.mouse_drawing)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			return      
		altoFrameCalibracion = self.frame.shape[0]
		
		if self.medir == True:
			
			Medida_pixels = np.abs(self.point2[1]-self.point1[1])
			
			Medida_pixels = Medida_pixels *10*self.canvas_heigth/altoFrameCalibracion
			self.medir = False
			
			self.sigLabelEscala.emit(str(int(Medida_pixels)) + ' pixels/mm')
			self.point1=[]
			self.point2=[]
			self.flagCalibracion = False
			self.cap.release()  
			cv2.destroyAllWindows() 	

			self.stop()


	def procesamiento (self):
	
		global point1_resized , point2_resized , point1_line_inf , point1_line_sup ,point2_line_inf,point2_line_sup, vector_diametro_interno, vector_intmed_sup, vector_intmed_inf,vector_intmed_sup
		global borde_frameant,valores_y_intmedInf,h2,Medida_pixels,Medida_pixels_ajustada, LUMEN_MEDIDO,IMT_MEDIDO_INFERIOR,IMT_MEDIDO_SUPERIOR
		####### DIMENSIONES DEL self.frame_crop, TENIENDO EN CUENTA QUE EL (0,0) ESTA EN LA ESQUINA SUPERIOR IZQUIERDA ####
		
		
		dimensions_original = self.frame.shape
		max_values = []
		min_values = []
						
		##### PRCESAMIENTO DEL PRIMER CUADRO 
		
		if self.flag_mostrar_editado == False:
			if self.point1 and self.point2 and (self.point1!=self.point2):
				

				if self.flag_ROI == True:
					self.borde_frameant = []
					#el area seleccionada queda guardada para el resto del video
					self.rect = cv2.rectangle(self.frame_cpy, self.point1, self.point2, (0, 255, 255))
					if self.resize == True :    
						self.flag_resized = True

						h2=np.abs(self.point2[1]-self.point1[1]) 
						
						if(self.point1[1]<self.point2[1] and self.point1[0]<self.point2[0] ):
							self.frame_cpy = self.frame[ self.point1[1]:self.point2[1],self.point1[0]:self.point2[0] ].copy()
						if(self.point1[1]>self.point2[1] and self.point1[0]>self.point2[0]):
							self.frame_cpy = self.frame[ self.point2[1]:self.point1[1],self.point2[0]:self.point1[0] ].copy()
						if(self.point1[1]>self.point2[1] and self.point1[0]<self.point2[0]):
							self.frame_cpy = self.frame[ self.point2[1]:self.point1[1],self.point1[0]:self.point2[0] ].copy()
						if(self.point1[1]<self.point2[1] and self.point1[0]>self.point2[0]):
							self.frame_cpy = self.frame[ self.point1[1]:self.point2[1],self.point2[0]:self.point1[0] ].copy()
						


						
						
						
						try:
							if self.frame_cpy != [] :

								Medida_pixels_ajustada = Medida_pixels * self.canvas_heigth/ np.abs(self.point1[1]-self.point2[1])
								self.sigLabelEscala.emit(str(int(Medida_pixels_ajustada)) + ' pixels/mm')
								self.frame_cpy = cv2.resize(self.frame_cpy ,(self.canvas_width , self.canvas_heigth) )
								#self.frame_cpy = cv2.resize(self.frame_cpy ,(dimensions_original[1] , dimensions_original[0]) )
						except: pass
						point1_resized = self.point1                        
						point2_resized = self.point2

						self.point1 = []
						self.point2 = []
						
						self.flag_procesar = True

			
		else:

			self.frame_cpy = self.frame[ point1_resized[1]:point2_resized[1],point1_resized[0]:point2_resized[0] ].copy()

			if self.frame_cpy != [] :
				self.frame_cpy = cv2.resize(self.frame_cpy ,(self.canvas_width , self.canvas_heigth) )
				##self.frame_cpy = cv2.resize(self.frame_cpy ,(dimensions_original[1] , dimensions_original[0]) )
			

		self.frame_crop = self.frame_cpy
		self.frame_crop_IMT = self.frame_cpy
		dimensions = self.frame_crop.shape
		height = self.frame_crop.shape[0]
		width = self.frame_crop.shape[1]
		channels = self.frame_crop.shape[2]

		########  PROCESA LUEGO DE MARCAR LA LINEA Y LOS CUADRADOS#####
		if self.flag_procesar == True or self.flag_mostrar_editado == True or self.volverACalcular==True:
			self.volverACalcular = False
			self.flag_procesar = False
			#if self.volverACalcular == True:
			self.frame_crop_IMT=cv2.convertScaleAbs(self.frame_crop_IMT, alpha=self.contraste_IMT, beta=self.brillo_IMT)
			self.frame_crop=cv2.convertScaleAbs(self.frame_crop, alpha=self.contraste, beta=self.brillo)

			#   self.volverACalcular = False
			### DELIMITO LOS BORDES DE LA IMAGEN PARA QUE LA DETECCION DE BORDES SEA MAS PRECISA ##
			cv2.line(self.frame_crop,(0,0),(0,height), (0,255,0),10)
			cv2.line(self.frame_crop,(width,0),(width,height), (0,255,0),10)
			
				   
						
			
			#####################################
			####### DIAMETRO INTERNO ############
			#####################################
			
			imgray = cv2.cvtColor(self.frame_crop, cv2.COLOR_BGR2GRAY)## es redundante porque la imagen ya esta en blanco y negro
			imgray = cv2.bitwise_not(imgray) ##invierto os colores
			imgray = cv2.bilateralFilter(imgray,5,400,400) ## aplico un filtrado para eliminar las lineas horizontales 
			ret, thresh = cv2.threshold(imgray,210,255,cv2.THRESH_BINARY)### aplico un treshold para quedarme con las partes mas oscuras de la imagen original
			
			contours, _ = cv2.findContours(thresh, cv2.RETR_TREE   , cv2.CHAIN_APPROX_NONE )## encuentro todos los contornos

			
			area =[] #### filtro el contorno de mayor area
			dy1=[]
			dx1=[]
			max_mean=0
			min_mean=0
			if(contours!=[]):
				for c in contours: 
					area.append(cv2.contourArea(c))

				con_area_max = np.argmax(area)


				cv2.drawContours(self.frame_crop, contours,con_area_max , (0,255,0), 1)

				dx1=contours[con_area_max ][:,0][:,0] ## del vector 0 tomo todas las filas de la columna 0 (valores de X)
			  
				dy1= contours[con_area_max ][:,0][:,1]
			  

				######### MEDICION ########
				max_values = []
				min_values = []
				tolerancia = 30
				for i in dy1:
					if i > dy1[np.argmax(dy1)]-tolerancia:
						max_values.append(i) ### almaceno valores maximos 
					if i< dy1[np.argmin(dy1)]+tolerancia:
						min_values.append(i) ## almaceno valores minimos   
				
				## Utilizando la media
				max_mean = np.mean(max_values)
				min_mean = np.mean(min_values)
				pts1=(int(width/2),int(max_mean))
				pts2=(int(width/2),int(min_mean))
				cv2.line(self.frame_crop,pts1,pts2, (255,0,0),10)
				
				dx1_max = dx1[np.argmax(dy1)]
				dx1_min = dx1[np.argmin(dy1)]
				
				
				diff_media = max_mean - min_mean
				
				std_dev_maxValues = np.std(max_values)
				std_dev_minValues = np.std(min_values)
				
				if self.flag_mostrar_editado == True:
					vector_diametro_interno.append(diff_media)
					## mido el lumen en mm y lo muestro en la aplicacion
					LUMEN_MEDIDO = diff_media/Medida_pixels 
					
			###################################################
			######## DETECCION DE ESPESOR INTIMA-MEDIA ########
			###################################################

			
			#img =  cv2.cvtColor(self.frame_crop,cv2.COLOR_BGR2GRAY)
			
			if max_values!= [] and min_values!=[]:
				self.ymax = max_values[np.argmax(max_values)]
				self.ymin = min_values[np.argmin(min_values)]
			else: 
				self.ymax=0
				self.ymin=0

			
			
			imgray = cv2.cvtColor(self.frame_crop_IMT, cv2.COLOR_BGR2GRAY)## es redundante porque la imagen ya esta en blanco y negro
			imgray = cv2.bilateralFilter(imgray,5,400,400) ## aplico un filtrado para eliminar las lineas horizontales 
			ret, thresh = cv2.threshold(imgray,210,255,cv2.THRESH_BINARY)### aplico un treshold para quedarme con las partes mas oscuras de la imagen original
			
			contours, ret = cv2.findContours(thresh, cv2.RETR_EXTERNAL   , cv2.CHAIN_APPROX_NONE )


			for c in contours :
				#=========================================ÍNTIMA MEDIA INFERIOR================================================================
				if cv2.contourArea(c) > self.resolucion and c[:,0][:,1][np.argmin(c[:,0][:,1])] > max_mean:  #Contornos grandes por debajo del límite del diámero arterial
					dx1_int_med_inf = c[:,0][:,0] ## del vector 0 tomo todas las filas de la columna 0 (valores de X)
					dy1_int_med_inf = c[:,0][:,1]

					cv2.drawContours(self.frame_crop_IMT, [c], -1 , (0,0,255), 1)



					######### MEDICION ########
					if self.flag_mostrar_editado == True:
						min_values_int_med_inf = []
						indices_valores_minimos_int_med_inf = []
						tolerancia = np.mean(dy1_int_med_inf)


						for index, i in  enumerate(dy1_int_med_inf):
							if i <tolerancia: #Todos los valores entre la tolerancia y el punto más cercano al diámetro
								min_values_int_med_inf.append(i) ## almaceno valores minimos
								indices_valores_minimos_int_med_inf.append(index)   
						

						## Utilizando la media
						min_mean_int_med_inf = np.mean(min_values_int_med_inf)
						vector_intmed_inf.append(min_mean_int_med_inf - max_mean) 
						
						IMT_MEDIDO_INFERIOR = (min_mean_int_med_inf - max_mean)/Medida_pixels
						
						pts1=(int(width/4),int(min_mean_int_med_inf))
						pts2=(int(width/4),int(max_mean))
						cv2.line(self.frame_crop_IMT,pts1,pts2, (255,255,0),5)





				#=========================================ÍNTIMA MEDIA SUPERIOR================================================================
				if cv2.contourArea(c) > self.resolucion and c[:,0][:,1][np.argmax(c[:,0][:,1])] <  min_mean: #Contorno grande y cuyo punto superior esté por encima de el diámetro
					cv2.drawContours(self.frame_crop_IMT, [c], -1 , (0,0,255), 1)
					dx1_int_med_sup = c[:,0][:,0] ## del vector 0 tomo todas las filas de la columna 0 (valores de X)
				  
					dy1_int_med_sup = c[:,0][:,1]

					######### MEDICION ########
					if self.flag_mostrar_editado == True:

						max_values_int_med_sup = []
						indices_valores_minimos_int_med_sup = []
						tolerancia = np.mean(dy1_int_med_sup)
						for index, i in enumerate(dy1_int_med_sup):
							if i > tolerancia:	#Todos los valores entre la tolerancia y el valor más cerca al diámetro arterial 
								max_values_int_med_sup.append(i) ## almaceno valores minimos  
								indices_valores_minimos_int_med_sup.append(index)
						

						## Utilizando la media
						max_mean_int_med_sup = np.mean(max_values_int_med_sup)
						vector_intmed_sup.append( min_mean - max_mean_int_med_sup ) 

						IMT_MEDIDO_SUPERIOR =  (min_mean - max_mean_int_med_sup)/Medida_pixels
						pts1=(int(width*0.75),int(min_mean))
						pts2=(int(width*0.75),int(max_mean_int_med_sup))
						cv2.line(self.frame_crop_IMT,pts1,pts2, (255,255,0),2)

			if self.flag_mostrar_editado == True:
				print("Lumen "+str(diff_media) )
				print("IMT inf"+str(IMT_MEDIDO_INFERIOR*Medida_pixels))
				
				LUMEN_MEDIDO=diff_media/Medida_pixels
				self.sigLabelLumen.emit("Lumen: "+str(np.around(LUMEN_MEDIDO,decimals=3) ) + ' mm') 
				
				self.sigLabelIMT.emit("Inferior: "+str(np.around(IMT_MEDIDO_INFERIOR,decimals=3) ) +" mm Superior: "+str(np.around(IMT_MEDIDO_SUPERIOR,decimals=3))+" mm")	
				

				#==========================================MOSTRAR================================================================================
			if self.flag_mostrar_editado == False:
				
				cv2.namedWindow("frame_crop")
				cv2.setMouseCallback("frame_crop", self.mouse_drawing)

				cv2.imshow("frame_crop",self.frame_crop)
				cv2.imshow("frame_crop_IMT",self.frame_crop_IMT)


		
		 
	def procesar(self):
		
		self.flag_resized =False
		self.frame_cpy = self.frame.copy()
		
		while( self.editandoVideo == True ):

			if self.Reiniciado == True:
				self.Reiniciado = False
				break

			self.procesamiento()
			cv2.imshow("frame",self.frame) ## muestro el video original 
			cv2.namedWindow("frame")
			cv2.setMouseCallback("frame", self.mouse_drawing)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				return      
	
		self.cap.release()  
		cv2.destroyAllWindows() 
		

	def mostrarVideo(self, frame_orig):

		size = frame_orig.shape
		step = frame_orig.size / size[0]
		qformat = QImage.Format_RGB888  #RGB solamente
		img = QImage(frame_orig, size[1], size[0], step, qformat)
		img = img.rgbSwapped()
		p=QPixmap.fromImage(img)
		
		if self.flag_vid_original == True:
			self.changePixmapOriginal.emit(p)   
		else:   
			self.changePixmapEditado.emit(p)



			
	def graficar(self):
		global vector_diametro_interno
		global vector_intmed_inf,valores_y_intmedInf
		print("Cantidad de frames del video : " +str(self.cant_frames))
		print("Cantidad de frames procesados para diametro interno : "+str(len(vector_diametro_interno)))
		print("Cantidad de frames procesados para int med inf : "+str(len(vector_intmed_inf)))

		######## PROCESAMIENTO SOBRE EL VECTOR DE DATOS #####
		vector_diametro_interno_pro = []
		vector_intmed_inf_pro = []
		vector_intmed_sup_pro = []
		
		
		### GUARDO LOS DATOS PARA PROCESAMIENTO EXTERNO
		
		Diam = np.asarray(vector_diametro_interno)
		IntSup_txt = np.asarray(vector_intmed_sup)
		IntInf_txt = np.asarray(vector_intmed_inf)
		try:
			
			np.savetxt("Diam.csv", Diam, delimiter=",")
			np.savetxt("IntSup.csv", IntSup_txt, delimiter=",")
			np.savetxt("IntInf.csv", IntInf_txt, delimiter=",")
		except:pass
		
	
		
		#####

		self.sigClearGraficos.emit()
		self.sigDatosDiamatro.emit(vector_diametro_interno)
		self.sigDatosIntSup.emit(vector_intmed_sup)
		self.sigDatosIntInf.emit(vector_intmed_inf)
		# vector_intmed_sup=[]
		# vector_diametro_interno=[]
		# vector_intmed_inf=[]
		#self.sigClearGraficos.emit()
		
	def stop(self):
		self.isRunning = False
		self.quit()
		
		


			
	




