# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon May 26 00:12:10 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 544)
        MainWindow.setMaximumSize(QtCore.QSize(800, 554))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.SliderMem = QtGui.QSlider(self.centralwidget)
        self.SliderMem.setGeometry(QtCore.QRect(425, 410, 371, 29))
        self.SliderMem.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.SliderMem.setSingleStep(2)
        self.SliderMem.setOrientation(QtCore.Qt.Horizontal)
        self.SliderMem.setObjectName(_fromUtf8("SliderMem"))
        self.Memoire = QtGui.QLabel(self.centralwidget)
        self.Memoire.setGeometry(QtCore.QRect(430, 350, 131, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Serif"))
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.Memoire.setFont(font)
        self.Memoire.setObjectName(_fromUtf8("Memoire"))
        self.SliderShader = QtGui.QSlider(self.centralwidget)
        self.SliderShader.setEnabled(True)
        self.SliderShader.setGeometry(QtCore.QRect(425, 304, 371, 29))
        self.SliderShader.setAutoFillBackground(False)
        self.SliderShader.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.SliderShader.setSingleStep(2)
        self.SliderShader.setSliderPosition(0)
        self.SliderShader.setOrientation(QtCore.Qt.Horizontal)
        self.SliderShader.setTickInterval(2)
        self.SliderShader.setObjectName(_fromUtf8("SliderShader"))
        self.SliderGpu = QtGui.QSlider(self.centralwidget)
        self.SliderGpu.setGeometry(QtCore.QRect(425, 200, 371, 29))
        self.SliderGpu.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.SliderGpu.setSingleStep(2)
        self.SliderGpu.setOrientation(QtCore.Qt.Horizontal)
        self.SliderGpu.setObjectName(_fromUtf8("SliderGpu"))
        self.lcdMem = QtGui.QLCDNumber(self.centralwidget)
        self.lcdMem.setGeometry(QtCore.QRect(660, 360, 82, 32))
        self.lcdMem.setDigitCount(6)
        self.lcdMem.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdMem.setObjectName(_fromUtf8("lcdMem"))
        self.lcdShader = QtGui.QLCDNumber(self.centralwidget)
        self.lcdShader.setGeometry(QtCore.QRect(660, 250, 82, 32))
        self.lcdShader.setDigitCount(6)
        self.lcdShader.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdShader.setProperty("intValue", 0)
        self.lcdShader.setObjectName(_fromUtf8("lcdShader"))
        self.VitesseShader = QtGui.QLabel(self.centralwidget)
        self.VitesseShader.setGeometry(QtCore.QRect(430, 250, 131, 42))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Serif"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VitesseShader.setFont(font)
        self.VitesseShader.setObjectName(_fromUtf8("VitesseShader"))
        self.lcdGPU = QtGui.QLCDNumber(self.centralwidget)
        self.lcdGPU.setGeometry(QtCore.QRect(660, 160, 82, 32))
        self.lcdGPU.setDigitCount(6)
        self.lcdGPU.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdGPU.setObjectName(_fromUtf8("lcdGPU"))
        self.VitesseGpu = QtGui.QLabel(self.centralwidget)
        self.VitesseGpu.setGeometry(QtCore.QRect(430, 150, 131, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Serif"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VitesseGpu.setFont(font)
        self.VitesseGpu.setObjectName(_fromUtf8("VitesseGpu"))
        self.Title = QtGui.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(10, 10, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName(_fromUtf8("Title"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 140, 801, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.ButtonReset = QtGui.QPushButton(self.centralwidget)
        self.ButtonReset.setGeometry(QtCore.QRect(450, 460, 150, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonReset.setFont(font)
        self.ButtonReset.setAutoDefault(False)
        self.ButtonReset.setDefault(False)
        self.ButtonReset.setFlat(False)
        self.ButtonReset.setObjectName(_fromUtf8("ButtonReset"))
        self.ButtonApply = QtGui.QPushButton(self.centralwidget)
        self.ButtonApply.setGeometry(QtCore.QRect(620, 459, 150, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonApply.setFont(font)
        self.ButtonApply.setStyleSheet(_fromUtf8(""))
        self.ButtonApply.setDefault(False)
        self.ButtonApply.setObjectName(_fromUtf8("ButtonApply"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(410, 150, 20, 391))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.Information = QtGui.QLabel(self.centralwidget)
        self.Information.setGeometry(QtCore.QRect(10, 110, 191, 31))
        self.Information.setAlignment(QtCore.Qt.AlignCenter)
        self.Information.setObjectName(_fromUtf8("Information"))
        self.NomGpu = QtGui.QLabel(self.centralwidget)
        self.NomGpu.setGeometry(QtCore.QRect(0, 160, 401, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.NomGpu.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.NomGpu.setFont(font)
        self.NomGpu.setAlignment(QtCore.Qt.AlignCenter)
        self.NomGpu.setObjectName(_fromUtf8("NomGpu"))
        self.Message = QtGui.QLabel(self.centralwidget)
        self.Message.setGeometry(QtCore.QRect(0, 460, 421, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.Message.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Message.setFont(font)
        self.Message.setText(_fromUtf8(""))
        self.Message.setAlignment(QtCore.Qt.AlignCenter)
        self.Message.setObjectName(_fromUtf8("Message"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(750, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(750, 250, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(750, 360, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.checkBoxOptimus = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxOptimus.setEnabled(False)
        self.checkBoxOptimus.setGeometry(QtCore.QRect(330, 120, 97, 22))
        self.checkBoxOptimus.setCheckable(True)
        self.checkBoxOptimus.setChecked(False)
        self.checkBoxOptimus.setObjectName(_fromUtf8("checkBoxOptimus"))
        self.checkBoxSli = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxSli.setEnabled(False)
        self.checkBoxSli.setGeometry(QtCore.QRect(430, 120, 51, 22))
        self.checkBoxSli.setCheckable(True)
        self.checkBoxSli.setObjectName(_fromUtf8("checkBoxSli"))
        self.checkBoxVaapi = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxVaapi.setEnabled(False)
        self.checkBoxVaapi.setGeometry(QtCore.QRect(260, 120, 71, 22))
        self.checkBoxVaapi.setCheckable(True)
        self.checkBoxVaapi.setObjectName(_fromUtf8("checkBoxVaapi"))
        self.listWidgetGpu = QtGui.QListWidget(self.centralwidget)
        self.listWidgetGpu.setGeometry(QtCore.QRect(220, 10, 301, 101))
        self.listWidgetGpu.setStyleSheet(_fromUtf8("background-color: rgb(207, 255, 233);"))
        self.listWidgetGpu.setObjectName(_fromUtf8("listWidgetGpu"))
        self.PiloteVersion = QtGui.QLabel(self.centralwidget)
        self.PiloteVersion.setGeometry(QtCore.QRect(5, 200, 200, 65))
        self.PiloteVersion.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);"))
        self.PiloteVersion.setAlignment(QtCore.Qt.AlignCenter)
        self.PiloteVersion.setMargin(2)
        self.PiloteVersion.setObjectName(_fromUtf8("PiloteVersion"))
        self.OpenGlSupport = QtGui.QLabel(self.centralwidget)
        self.OpenGlSupport.setGeometry(QtCore.QRect(210, 200, 200, 65))
        self.OpenGlSupport.setAlignment(QtCore.Qt.AlignCenter)
        self.OpenGlSupport.setMargin(2)
        self.OpenGlSupport.setObjectName(_fromUtf8("OpenGlSupport"))
        self.MemGpu = QtGui.QLabel(self.centralwidget)
        self.MemGpu.setGeometry(QtCore.QRect(5, 270, 200, 65))
        self.MemGpu.setAlignment(QtCore.Qt.AlignCenter)
        self.MemGpu.setMargin(2)
        self.MemGpu.setObjectName(_fromUtf8("MemGpu"))
        self.CudaCore = QtGui.QLabel(self.centralwidget)
        self.CudaCore.setGeometry(QtCore.QRect(210, 270, 200, 65))
        self.CudaCore.setAlignment(QtCore.Qt.AlignCenter)
        self.CudaCore.setMargin(2)
        self.CudaCore.setObjectName(_fromUtf8("CudaCore"))
        self.UGPU = QtGui.QLabel(self.centralwidget)
        self.UGPU.setGeometry(QtCore.QRect(210, 400, 200, 65))
        self.UGPU.setAlignment(QtCore.Qt.AlignCenter)
        self.UGPU.setMargin(2)
        self.UGPU.setObjectName(_fromUtf8("UGPU"))
        self.UMem = QtGui.QLabel(self.centralwidget)
        self.UMem.setGeometry(QtCore.QRect(210, 340, 200, 65))
        self.UMem.setAlignment(QtCore.Qt.AlignCenter)
        self.UMem.setMargin(2)
        self.UMem.setObjectName(_fromUtf8("UMem"))
        self.UPCIE = QtGui.QLabel(self.centralwidget)
        self.UPCIE.setGeometry(QtCore.QRect(5, 400, 200, 65))
        self.UPCIE.setAlignment(QtCore.Qt.AlignCenter)
        self.UPCIE.setMargin(2)
        self.UPCIE.setObjectName(_fromUtf8("UPCIE"))
        self.Temp = QtGui.QLabel(self.centralwidget)
        self.Temp.setGeometry(QtCore.QRect(5, 340, 200, 65))
        self.Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.Temp.setMargin(2)
        self.Temp.setObjectName(_fromUtf8("Temp"))
        self.label_Img = QtGui.QLabel(self.centralwidget)
        self.label_Img.setGeometry(QtCore.QRect(554, 5, 241, 140))
        self.label_Img.setObjectName(_fromUtf8("label_Img"))
        self.label_Dfreq_Gpu = QtGui.QLabel(self.centralwidget)
        self.label_Dfreq_Gpu.setGeometry(QtCore.QRect(570, 160, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Dfreq_Gpu.setFont(font)
        self.label_Dfreq_Gpu.setObjectName(_fromUtf8("label_Dfreq_Gpu"))
        self.label_Dfreq_Shader = QtGui.QLabel(self.centralwidget)
        self.label_Dfreq_Shader.setGeometry(QtCore.QRect(570, 250, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Dfreq_Shader.setFont(font)
        self.label_Dfreq_Shader.setObjectName(_fromUtf8("label_Dfreq_Shader"))
        self.label_Dfreq_Mem = QtGui.QLabel(self.centralwidget)
        self.label_Dfreq_Mem.setGeometry(QtCore.QRect(570, 360, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Dfreq_Mem.setFont(font)
        self.label_Dfreq_Mem.setObjectName(_fromUtf8("label_Dfreq_Mem"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        self.menuAide = QtGui.QMenu(self.menubar)
        self.menuAide.setObjectName(_fromUtf8("menuAide"))
        MainWindow.setMenuBar(self.menubar)
        self.actionQuitter = QtGui.QAction(MainWindow)
        self.actionQuitter.setObjectName(_fromUtf8("actionQuitter"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFichier.addAction(self.actionQuitter)
        self.menuAide.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Nvidiux", None))
        self.Memoire.setText(_translate("MainWindow", "<html><head/><body><p>Memoire</p></body></html>", None))
        self.VitesseShader.setText(_translate("MainWindow", "<html><head/><body><p>Shader</p></body></html>", None))
        self.VitesseGpu.setText(_translate("MainWindow", "Gpu", None))
        self.Title.setText(_translate("MainWindow", "Nvidiux", None))
        self.ButtonReset.setText(_translate("MainWindow", "Reset", None))
        self.ButtonApply.setText(_translate("MainWindow", "Appliquer", None))
        self.Information.setText(_translate("MainWindow", "Version beta 2", None))
        self.NomGpu.setText(_translate("MainWindow", "Nom gpu", None))
        self.label.setText(_translate("MainWindow", "Mhz", None))
        self.label_2.setText(_translate("MainWindow", "Mhz", None))
        self.label_3.setText(_translate("MainWindow", "Mhz", None))
        self.checkBoxOptimus.setText(_translate("MainWindow", "Optimus", None))
        self.checkBoxSli.setText(_translate("MainWindow", "Sli", None))
        self.checkBoxVaapi.setText(_translate("MainWindow", "Vaapi", None))
        self.PiloteVersion.setText(_translate("MainWindow", "Version pilote", None))
        self.OpenGlSupport.setText(_translate("MainWindow", "OpenGl Support", None))
        self.MemGpu.setText(_translate("MainWindow", "Mem Gpu", None))
        self.CudaCore.setText(_translate("MainWindow", "Cudacore", None))
        self.UGPU.setText(_translate("MainWindow", "Gpu utilisation", None))
        self.UMem.setText(_translate("MainWindow", "Mem utilisation", None))
        self.UPCIE.setText(_translate("MainWindow", "Pcie utili", None))
        self.Temp.setText(_translate("MainWindow", "Temp", None))
        self.label_Img.setText(_translate("MainWindow", "Img", None))
        self.label_Dfreq_Gpu.setText(_translate("MainWindow", "TextLabel", None))
        self.label_Dfreq_Shader.setText(_translate("MainWindow", "TextLabel", None))
        self.label_Dfreq_Mem.setText(_translate("MainWindow", "TextLabel", None))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        self.menuAide.setTitle(_translate("MainWindow", "Aide", None))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
