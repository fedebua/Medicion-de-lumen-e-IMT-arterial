# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz12-11.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1015, 814)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelContrasteDiam = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.labelContrasteDiam.setFont(font)
        self.labelContrasteDiam.setAlignment(QtCore.Qt.AlignCenter)
        self.labelContrasteDiam.setObjectName("labelContrasteDiam")
        self.verticalLayout_2.addWidget(self.labelContrasteDiam)
        self.sliderContrasteDiam = QtWidgets.QSlider(self.centralwidget)
        self.sliderContrasteDiam.setMinimum(10)
        self.sliderContrasteDiam.setMaximum(30)
        self.sliderContrasteDiam.setSingleStep(1)
        self.sliderContrasteDiam.setProperty("value", 10)
        self.sliderContrasteDiam.setOrientation(QtCore.Qt.Horizontal)
        self.sliderContrasteDiam.setObjectName("sliderContrasteDiam")
        self.verticalLayout_2.addWidget(self.sliderContrasteDiam)
        self.labelBrilloDiam = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.labelBrilloDiam.setFont(font)
        self.labelBrilloDiam.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBrilloDiam.setObjectName("labelBrilloDiam")
        self.verticalLayout_2.addWidget(self.labelBrilloDiam)
        self.SliderBrilloDiam = QtWidgets.QSlider(self.centralwidget)
        self.SliderBrilloDiam.setMinimum(-200)
        self.SliderBrilloDiam.setMaximum(200)
        self.SliderBrilloDiam.setProperty("value", -100)
        self.SliderBrilloDiam.setOrientation(QtCore.Qt.Horizontal)
        self.SliderBrilloDiam.setObjectName("SliderBrilloDiam")
        self.verticalLayout_2.addWidget(self.SliderBrilloDiam)
        self.labelResolucion = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.labelResolucion.setFont(font)
        self.labelResolucion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResolucion.setObjectName("labelResolucion")
        self.verticalLayout_2.addWidget(self.labelResolucion)
        self.SliderResolucion = QtWidgets.QSlider(self.centralwidget)
        self.SliderResolucion.setMinimum(10)
        self.SliderResolucion.setMaximum(1000)
        self.SliderResolucion.setProperty("value", 800)
        self.SliderResolucion.setOrientation(QtCore.Qt.Horizontal)
        self.SliderResolucion.setObjectName("SliderResolucion")
        self.verticalLayout_2.addWidget(self.SliderResolucion)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.labelBrilloIMT = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.labelBrilloIMT.setFont(font)
        self.labelBrilloIMT.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBrilloIMT.setObjectName("labelBrilloIMT")
        self.verticalLayout_2.addWidget(self.labelBrilloIMT)
        self.SliderBrilloIMT = QtWidgets.QSlider(self.centralwidget)
        self.SliderBrilloIMT.setMinimum(-200)
        self.SliderBrilloIMT.setMaximum(200)
        self.SliderBrilloIMT.setProperty("value", -100)
        self.SliderBrilloIMT.setOrientation(QtCore.Qt.Horizontal)
        self.SliderBrilloIMT.setObjectName("SliderBrilloIMT")
        self.verticalLayout_2.addWidget(self.SliderBrilloIMT)
        self.labelContrasteIMT = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.labelContrasteIMT.setFont(font)
        self.labelContrasteIMT.setAlignment(QtCore.Qt.AlignCenter)
        self.labelContrasteIMT.setObjectName("labelContrasteIMT")
        self.verticalLayout_2.addWidget(self.labelContrasteIMT)
        self.sliderContrasteIMT = QtWidgets.QSlider(self.centralwidget)
        self.sliderContrasteIMT.setMinimum(10)
        self.sliderContrasteIMT.setMaximum(30)
        self.sliderContrasteIMT.setSingleStep(1)
        self.sliderContrasteIMT.setProperty("value", 30)
        self.sliderContrasteIMT.setOrientation(QtCore.Qt.Horizontal)
        self.sliderContrasteIMT.setObjectName("sliderContrasteIMT")
        self.verticalLayout_2.addWidget(self.sliderContrasteIMT)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.botonCalibrar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.botonCalibrar.setFont(font)
        self.botonCalibrar.setObjectName("botonCalibrar")
        self.horizontalLayout_4.addWidget(self.botonCalibrar)
        self.comboBoxEscala = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.comboBoxEscala.setFont(font)
        self.comboBoxEscala.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBoxEscala.setCurrentText("Marcar 1 cm")
        self.comboBoxEscala.setObjectName("comboBoxEscala")
        self.comboBoxEscala.addItem("")
        self.comboBoxEscala.addItem("")
        self.comboBoxEscala.addItem("")
        self.comboBoxEscala.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBoxEscala)
        self.labelEscala = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelEscala.setFont(font)
        self.labelEscala.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelEscala.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEscala.setObjectName("labelEscala")
        self.horizontalLayout_4.addWidget(self.labelEscala)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.botonROI = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.botonROI.setFont(font)
        self.botonROI.setObjectName("botonROI")
        self.verticalLayout_2.addWidget(self.botonROI)
        self.botonProcesar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.botonProcesar.setFont(font)
        self.botonProcesar.setObjectName("botonProcesar")
        self.verticalLayout_2.addWidget(self.botonProcesar)
        self.botonPlay = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.botonPlay.setFont(font)
        self.botonPlay.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botonPlay.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("recursos_rc/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonPlay.setIcon(icon)
        self.botonPlay.setObjectName("botonPlay")
        self.verticalLayout_2.addWidget(self.botonPlay)
        self.botonReiniciar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.botonReiniciar.setFont(font)
        self.botonReiniciar.setObjectName("botonReiniciar")
        self.verticalLayout_2.addWidget(self.botonReiniciar)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.imgGIBIO = QtWidgets.QLabel(self.centralwidget)
        self.imgGIBIO.setMaximumSize(QtCore.QSize(463, 200))
        self.imgGIBIO.setText("")
        self.imgGIBIO.setPixmap(QtGui.QPixmap("recursos_rc/GIBIO.png"))
        self.imgGIBIO.setScaledContents(True)
        self.imgGIBIO.setObjectName("imgGIBIO")
        self.verticalLayout_2.addWidget(self.imgGIBIO)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelIMT = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.labelIMT.setFont(font)
        self.labelIMT.setAlignment(QtCore.Qt.AlignCenter)
        self.labelIMT.setObjectName("labelIMT")
        self.verticalLayout_3.addWidget(self.labelIMT)
        self.visualizadorIMT = QtWidgets.QLabel(self.centralwidget)
        self.visualizadorIMT.setMinimumSize(QtCore.QSize(0, 300))
        self.visualizadorIMT.setText("")
        self.visualizadorIMT.setAlignment(QtCore.Qt.AlignCenter)
        self.visualizadorIMT.setObjectName("visualizadorIMT")
        self.verticalLayout_3.addWidget(self.visualizadorIMT)
        self.labelLumen = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.labelLumen.setFont(font)
        self.labelLumen.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLumen.setObjectName("labelLumen")
        self.verticalLayout_3.addWidget(self.labelLumen)
        self.visualizadorLumen = QtWidgets.QLabel(self.centralwidget)
        self.visualizadorLumen.setMinimumSize(QtCore.QSize(0, 300))
        self.visualizadorLumen.setText("")
        self.visualizadorLumen.setAlignment(QtCore.Qt.AlignCenter)
        self.visualizadorLumen.setObjectName("visualizadorLumen")
        self.verticalLayout_3.addWidget(self.visualizadorLumen)
        self.labelValorIMT = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelValorIMT.sizePolicy().hasHeightForWidth())
        self.labelValorIMT.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.labelValorIMT.setFont(font)
        self.labelValorIMT.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.labelValorIMT.setObjectName("labelValorIMT")
        self.verticalLayout_3.addWidget(self.labelValorIMT)
        self.labelValorLumen = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelValorLumen.sizePolicy().hasHeightForWidth())
        self.labelValorLumen.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.labelValorLumen.setFont(font)
        self.labelValorLumen.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.labelValorLumen.setObjectName("labelValorLumen")
        self.verticalLayout_3.addWidget(self.labelValorLumen)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1015, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelContrasteDiam.setText(_translate("MainWindow", "Contraste Lumen"))
        self.labelBrilloDiam.setText(_translate("MainWindow", "Brillo Lumen"))
        self.labelResolucion.setText(_translate("MainWindow", "Resolución"))
        self.labelBrilloIMT.setText(_translate("MainWindow", "Brillo IMT"))
        self.labelContrasteIMT.setText(_translate("MainWindow", "Contraste IMT"))
        self.botonCalibrar.setText(_translate("MainWindow", "Calibrar escala"))
        self.comboBoxEscala.setItemText(0, _translate("MainWindow", "Marcar 1 cm"))
        self.comboBoxEscala.setItemText(1, _translate("MainWindow", "Marcar 5 cm"))
        self.comboBoxEscala.setItemText(2, _translate("MainWindow", "Marcar 1 mm"))
        self.comboBoxEscala.setItemText(3, _translate("MainWindow", "Marcar 5 mm"))
        self.labelEscala.setText(_translate("MainWindow", "NO DEFINIDO pixels/mm"))
        self.botonROI.setText(_translate("MainWindow", "Región de Interés (ROI)"))
        self.botonProcesar.setText(_translate("MainWindow", "Procesar"))
        self.botonReiniciar.setText(_translate("MainWindow", "Reiniciar"))
        self.labelIMT.setText(_translate("MainWindow", "IMT"))
        self.labelLumen.setText(_translate("MainWindow", "Lumen"))
        self.labelValorIMT.setText(_translate("MainWindow", "Medición IMT [mm]: "))
        self.labelValorLumen.setText(_translate("MainWindow", "Medición lumen [mm]:"))

import recursos_rc