from interfazpy import *
from classThread import *

import pyqtgraph as pg
import numpy as np


from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtMultimediaWidgets import QVideoWidget
#Podría poner todo en el mismo código pero mejor separar la lógica de la UI (clase MainWindow definida en ui_ejemplo1.py) y acá se la instancia.

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):	#Ui_MainWindow hace referencia al ui_ejemplo1.py

	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		super().__init__()
		self.setupUi(self)	#generará la interfaz, pero pasándolo self que representa el propio objeto de la ventana
		#=======================================================================================================
		#======================== A partir de acá va la lógica propia ==========================================
		#=======================================================================================================
		self.SliderBrilloDiam.valueChanged.connect(self.cambioSliders)# cambiado
		self.sliderContrasteDiam.valueChanged.connect(self.cambioSliders)# cambiado
		self.SliderResolucion.valueChanged.connect(self.cambioSliders)# cambiado
		self.sliderContrasteIMT.valueChanged.connect(self.cambioSliders)# cambiado
		self.SliderBrilloIMT.valueChanged.connect(self.cambioSliders)# cambiado


		##self.botonReproducir.clicked.connect(self.mostrarImagen)
		self.botonProcesar.clicked.connect(self.editarImagen)# cambiado
		self.botonROI.clicked.connect(self.mostrarPrimerCuadro)# cambiado
		self.botonPlay.clicked.connect(self.PlayPause)
		self.botonCalibrar.clicked.connect(self.Calibracion)
		
		self.botonReiniciar.clicked.connect(self.Reiniciar)

		self.threadVidEditado = Thread (self)
		self.threadVidOriginal = Thread(self)
		self.threadCalibracion = Thread(self)
		## guardo dimensiones del layout para ajustar tamaño de imagenes
		self.threadVidOriginal.canvas_width = self.visualizadorIMT.frameGeometry().width()
		self.threadVidOriginal.canvas_heigth = self.visualizadorIMT.frameGeometry().height()
		
		self.botonPlay.setEnabled(False)
		self.botonProcesar.setEnabled(False)
		self.botonROI.setEnabled(False)
		self.reiniciar = False

	#=======================================================================================================
	#==================================== Espacio para funciones ===========================================
	#=======================================================================================================
	def Calibracion(self):

		msg = QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Information)
		msg.setText("Dibuje una linea vertical sobre la regla indicando 1cm")
		#msg.setInformativeText("This is additional information")
		msg.setWindowTitle("Calibración")
		#msg.setDetailedText("The details are as follows:")
		msg.setStandardButtons(QtGui.QMessageBox.Ok)
		#msg.buttonClicked.connect(self.InitCal)
		retval = msg.exec_()


		self.threadCalibracion = Thread(self)
		self.threadCalibracion.canvas_width = self.visualizadorIMT.frameGeometry().width()
		self.threadCalibracion.canvas_heigth = self.visualizadorIMT.frameGeometry().height()
		self.threadCalibracion.flagCalibracion=True
		self.threadCalibracion.sigLabelEscala.connect(self.labelEscala.setText)
		self.threadCalibracion.start()
		self.botonProcesar.setEnabled(True)
		self.comboBoxEscala.setEnabled(True)
		self.botonROI.setEnabled(True)
	def InitCal():
		pass
	def PlayPause(self):
		icon_play = QtGui.QIcon()
		icon_play.addPixmap(QtGui.QPixmap("./recursos_rc/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		icon_pause = QtGui.QIcon()
		icon_pause.addPixmap(QtGui.QPixmap("./recursos_rc/pause.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	   
		print(self.threadVidEditado.signalPause)
		if(self.threadVidEditado.signalPause==False):
				
			self.threadVidEditado.signalPause=True
			self.botonPlay.setText("Reanudar")
			self.botonPlay.setIcon(icon_play)
		else:
			self.botonPlay.setText("Pausa")
			self.botonPlay.setIcon(icon_pause)
			self.threadVidEditado.signalPause=False

	def mostrarImagen(self):
		
		self.botonProcesar.setEnabled(False) #Inhabilito el botón para que no reproduzcan más de un video a la vez
		self.botonReproducir.setEnabled(False) #Deshabilito botón
		self.botonROI.setEnabled(False) #Deshabilito botón
		self.comboBoxEscala.setEnabled(False)
		self.threadVidOriginal = Thread(self)
		self.threadVidOriginal.changePixmapOriginal.connect(self.visualizadorIMT.setPixmap)		
		self.threadVidOriginal.changePixmapEditado.connect(self.visualizadorLumen.setPixmap)
		
		self.threadVidOriginal.sigLabelIMT.connect(self.labelValorIMT.setText)
		self.threadVidOriginal.sigLabelLumen.connect(self.labelValorLumen.setText)

		self.threadVidOriginal.terminoVideo.connect(self.botonProcesar.setEnabled)		#Señal que vuelve a habilitar el botón
		self.threadVidOriginal.terminoVideo.connect(self.botonROI.setEnabled)		#Señal que vuelve a habilitar el botón
		##self.threadVidOriginal.terminoVideo.connect(self.botonReproducir.setEnabled)
		self.threadVidOriginal.editandoVideo = False
		self.threadVidOriginal.flag_vid_original = True
		self.threadVidOriginal.start()

	def editarImagen(self):
		
		self.botonPlay.setEnabled(True)
		self.botonProcesar.setEnabled(False)
		self.botonROI.setEnabled(False)
		self.botonCalibrar.setEnabled(False)
		self.comboBoxEscala.setEnabled(False)
		self.botonPlay.setText("Pausa")
		self.botonProcesar.setEnabled(False) 
		#Inhabilito el botón para que no reproduzcan más de un video a la vez
		##self.botonReproducir.setEnabled(False) #Deshabilito botón
		self.botonROI.setEnabled(False) #Deshabilito botón
		
		self.threadVidOriginal = Thread(self)
		self.threadVidOriginal.sigLabelIMT.connect(self.labelValorIMT.setText)
		self.threadVidOriginal.sigLabelLumen.connect(self.labelValorLumen.setText)
		self.threadVidEditado.sigLabelIMT.connect(self.labelValorIMT.setText)
		self.threadVidEditado.sigLabelLumen.connect(self.labelValorLumen.setText)

		self.threadVidOriginal.canvas_width = self.visualizadorIMT.frameGeometry().width()
		self.threadVidOriginal.canvas_heigth = self.visualizadorIMT.frameGeometry().height()
		
		self.threadVidEditado.changePixmapOriginal.connect(self.visualizadorIMT.setPixmap)		
		self.threadVidEditado.changePixmapEditado.connect(self.visualizadorLumen.setPixmap)
		self.threadVidOriginal.changePixmapOriginal.connect(self.visualizadorIMT.setPixmap)		
		self.threadVidOriginal.changePixmapEditado.connect(self.visualizadorLumen.setPixmap)
		self.threadVidEditado.terminoVideo.connect(self.botonProcesar.setEnabled)		#Señal que vuelve a habilitar el botón
		self.threadVidEditado.terminoVideo.connect(self.botonROI.setEnabled)		#Señal que vuelve a habilitar el botón
		##self.threadVidEditado.terminoVideo.connect(self.botonReproducir.setEnabled)		#Señal que vuelve a habilitar el botón
		
		self.threadVidEditado.Reiniciado = True
		self.threadVidOriginal.Reiniciado = True
		self.threadVidEditado.flag_vid_original = False
		self.threadVidOriginal.flag_vid_original = False
		self.threadVidOriginal.editandoVideo = False
		self.threadVidOriginal.flag_mostrar_editado = True
		self.threadVidOriginal.primerGrafico = False


		self.threadVidOriginal.volverACalcular = False
		self.threadVidEditado.volverACalcular = False
		self.threadVidEditado.brillo=self.SliderBrilloDiam.value()
		self.threadVidEditado.contraste=self.sliderContrasteDiam.value() /10
		self.threadVidEditado.resolucion=self.SliderResolucion.value()
		self.threadVidEditado.brillo_IMT=self.SliderBrilloIMT.value()
		self.threadVidEditado.contraste_IMT=self.sliderContrasteIMT.value()/10
		self.threadVidOriginal.brillo=self.SliderBrilloDiam.value()
		self.threadVidOriginal.resolucion=self.SliderResolucion.value()
		self.threadVidOriginal.contraste=self.sliderContrasteDiam.value() /10
		self.threadVidOriginal.brillo_IMT=self.SliderBrilloIMT.value()
		self.threadVidOriginal.contraste_IMT=self.sliderContrasteIMT.value()/10
		

		self.threadVidOriginal.start()
		

		
	def mostrarPrimerCuadro(self):

		##self.botonReproducir.setEnabled(False) #Deshabilito botón
		self.botonROI.setEnabled(False) #Deshabilito botón

		self.threadVidEditado.flag_1st_frame = False
		self.threadVidEditado.editandoVideo = True
		self.threadVidOriginal.canvas_width = int(self.visualizadorLumen.frameGeometry().width())
		self.threadVidOriginal.canvas_heigth = int(self.visualizadorLumen.frameGeometry().height())
		self.threadVidEditado.canvas_width = int(self.visualizadorLumen.frameGeometry().width())
		self.threadVidEditado.canvas_heigth = int(self.visualizadorLumen.frameGeometry().height())
		
		self.threadVidEditado.brillo = self.SliderBrilloDiam.value()
		self.threadVidEditado.contraste = self.sliderContrasteDiam.value()/10
		self.threadVidEditado.resolucion=self.SliderResolucion.value()
		self.threadVidEditado.brillo_IMT=self.SliderBrilloIMT.value()
		self.threadVidEditado.contraste_IMT=self.sliderContrasteIMT.value()/10
		self.threadVidEditado.Reiniciado = False
		self.threadVidEditado.isRunning = True

		self.threadVidEditado.sigLabelEscala.connect(self.labelEscala.setText)
		
		self.threadVidEditado.start()
		

	def Reiniciar(self):
		
		#Habilito todos los botones

		self.threadVidEditado.flag_vid_original=True
		self.threadVidEditado.Reiniciado = True
		self.threadVidOriginal.Reiniciado = True
		self.threadCalibracion.isRunning = False
		self.threadVidOriginal.isRunning = False
		self.threadVidEditado.isRunning=False
		
		##sleep(2)
		##self.botonReproducir.setEnabled(True) 
	
		self.botonProcesar.setEnabled(True)	
		self.botonROI.setEnabled(True)
		self.botonPlay.setEnabled(False)
		self.botonCalibrar.setEnabled(True)
		self.comboBoxEscala.setEnabled(True)	
		sleep(1)
		self.visualizadorIMT.clear()
		self.visualizadorLumen.clear()	
		
		
		
		self.visualizadorIMT.clear()
		self.visualizadorLumen.clear()
		

	
		
	def cambioSliders(self):
		self.threadVidEditado.brillo=self.SliderBrilloDiam.value()
		self.threadVidEditado.contraste=self.sliderContrasteDiam.value() /10
		self.threadVidEditado.resolucion=self.SliderResolucion.value()
		self.threadVidEditado.brillo_IMT=self.SliderBrilloIMT.value()
		self.threadVidEditado.contraste_IMT=self.sliderContrasteIMT.value()/10
		self.threadVidEditado.volverACalcular = True




if __name__ == "__main__": #el contenido del if sólo se ejecutará al llamar el propio script en la terminal para evitar ejecuciones duplicadas en caso de que importemos el fichero ventana.py en otro script
	app = QtWidgets.QApplication([])	#Creamos una aplicación con lista vacía (ACÁ VAN LOS ARGUMENTOS DE LÍNEA DE COMANDO)
	window = MainWindow()

	#window.setGeometry(500, 300, 300, 400)
	window.showMaximized()			#mostrar instancia de MainWindow

	app.exec_()				#Poner el programa en bucle
