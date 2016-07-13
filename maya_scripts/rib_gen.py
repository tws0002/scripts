# -*- coding: utf-8 -*-
#
#Pixar Renderman RIB Tool


from PySide import QtCore, QtGui
import pymel.core as pm
import maya.cmds as cmds
import os
import subprocess
import zipfile
import json
import getpass

cmds.loadPlugin('RenderMan_for_Maya.mll')

'''ribGenDict = {'currentFrameCheck':'1','startFrameCheck':'0','currentFrameValue':'1.0','startFrameValue':'1.0',
              'endFrameValue':'10.0','motionBlurCheck':'0','cameraBlurCheck':'0','shutterAngleValue':'80.0',
              'shutterOpeningOn':'0.0','shutterOpeningOff':'1.0','shutterTiming':'frameOpen','motionBlurType':'frame',
              'motionSamples':'2.0','rayTracedMotionBlurCheck':'0','subdivschemeCheck':'0','assignLamertShader':'0',
              'delayedReadArchiveCheck':'1','ReadArchiveCheck':'0',
              'noteText':'type information before push "Generate Rib Archive"'}
exportDict = {'projectName':'fullProjectPathAndName','ribIndexNumber':'00000','referenceAsset':'referenceAssetName',
              'referenceAssetPosition':'referenceAssetFullPathName','ribArchiveName':'ribName','gpuCachePosition':'gpufullPathName',
              'ribCachePosition':'ribfullPathName','ribArchiveDuration':'1.0','creator':'creatorName','buildTime':'yyyymmdd',
              'ribScreenShot':'screenShotImagePosition','version':'xxxx','exportNoteText':'none'}
'''
              

global ui
global newCurentFrame
global newStartFrame
global newEndFrame
global newShutterAngle
global newOpeningA
global newOpeningB
global newShutterTimingType
global newMotionBlurType
global newMotionSample

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(432, 921)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 431, 901))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 290, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_B04 = QtGui.QLineEdit(self.tab)
        self.lineEdit_B04.setEnabled(True)
        self.lineEdit_B04.setGeometry(QtCore.QRect(110, 380, 70, 20))
        self.lineEdit_B04.setObjectName("lineEdit_B04")
        self.line_4 = QtGui.QFrame(self.tab)
        self.line_4.setGeometry(QtCore.QRect(10, 630, 351, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_2 = QtGui.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(10, 220, 351, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(10, 350, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.checkBox_B03 = QtGui.QCheckBox(self.tab)
        self.checkBox_B03.setGeometry(QtCore.QRect(110, 410, 221, 16))
        self.checkBox_B03.setObjectName("checkBox_B03")
        self.checkBox_B01 = QtGui.QCheckBox(self.tab)
        self.checkBox_B01.setGeometry(QtCore.QRect(30, 240, 111, 16))
        self.checkBox_B01.setObjectName("checkBox_B01")
        self.horizontalSlider_2 = QtGui.QSlider(self.tab)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(190, 380, 161, 22))
        self.horizontalSlider_2.setMinimum(2)
        self.horizontalSlider_2.setMaximum(10)
        self.horizontalSlider_2.setProperty("value", 2)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.line_3 = QtGui.QFrame(self.tab)
        self.line_3.setGeometry(QtCore.QRect(10, 430, 351, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lineEdit_A03 = QtGui.QLineEdit(self.tab)
        self.lineEdit_A03.setEnabled(True)
        self.lineEdit_A03.setGeometry(QtCore.QRect(230, 190, 91, 20))
        self.lineEdit_A03.setObjectName("lineEdit_A03")
        self.lineEdit_A02 = QtGui.QLineEdit(self.tab)
        self.lineEdit_A02.setEnabled(True)
        self.lineEdit_A02.setGeometry(QtCore.QRect(130, 190, 91, 20))
        self.lineEdit_A02.setObjectName("lineEdit_A02")
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 320, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(50, 190, 71, 16))
        self.label_2.setObjectName("label_2")
        self.horizontalSlider = QtGui.QSlider(self.tab)
        self.horizontalSlider.setGeometry(QtCore.QRect(190, 260, 161, 22))
        self.horizontalSlider.setMaximum(360)
        self.horizontalSlider.setProperty("value", 80)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.lineEdit_B02 = QtGui.QLineEdit(self.tab)
        self.lineEdit_B02.setEnabled(True)
        self.lineEdit_B02.setGeometry(QtCore.QRect(110, 290, 70, 20))
        self.lineEdit_B02.setObjectName("lineEdit_B02")
        self.checkBox_C01 = QtGui.QCheckBox(self.tab)
        self.checkBox_C01.setGeometry(QtCore.QRect(10, 650, 141, 21))
        self.checkBox_C01.setAutoExclusive(False)
        self.checkBox_C01.setObjectName("checkBox_C01")
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(10, 620, 131, 16))
        self.label_11.setObjectName("label_11")
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(10, 380, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(110, 320, 131, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 260, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtGui.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 350, 131, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_01 = QtGui.QPushButton(self.tab)
        self.pushButton_01.setGeometry(QtCore.QRect(10, 450, 161, 31))
        self.pushButton_01.setObjectName("pushButton_01")
        self.lineEdit_B03 = QtGui.QLineEdit(self.tab)
        self.lineEdit_B03.setEnabled(True)
        self.lineEdit_B03.setGeometry(QtCore.QRect(200, 290, 70, 20))
        self.lineEdit_B03.setObjectName("lineEdit_B03")
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(9, 490, 131, 16))
        self.label_10.setObjectName("label_10")
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 100, 111, 41))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 110, 231, 52))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_A01 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_A01.setAutoExclusive(True)
        self.checkBox_A01.setObjectName("checkBox_A01")
        self.verticalLayout.addWidget(self.checkBox_A01)
        self.checkBox_A02 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_A02.setAutoExclusive(True)
        self.checkBox_A02.setObjectName("checkBox_A02")
        self.verticalLayout.addWidget(self.checkBox_A02)
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(10, 210, 131, 16))
        self.label_8.setObjectName("label_8")
        self.checkBox_B02 = QtGui.QCheckBox(self.tab)
        self.checkBox_B02.setGeometry(QtCore.QRect(140, 240, 111, 16))
        self.checkBox_B02.setObjectName("checkBox_B02")
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label_9.setObjectName("label_9")
        self.line = QtGui.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(10, 100, 351, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit_B01 = QtGui.QLineEdit(self.tab)
        self.lineEdit_B01.setEnabled(True)
        self.lineEdit_B01.setGeometry(QtCore.QRect(110, 260, 70, 20))
        self.lineEdit_B01.setObjectName("lineEdit_B01")
        self.checkBox_C02 = QtGui.QCheckBox(self.tab)
        self.checkBox_C02.setGeometry(QtCore.QRect(140, 650, 211, 21))
        self.checkBox_C02.setAutoExclusive(False)
        self.checkBox_C02.setObjectName("checkBox_C02")
        self.lineEdit_c01 = QtGui.QLineEdit(self.tab)
        self.lineEdit_c01.setGeometry(QtCore.QRect(9, 510, 361, 101))
        self.lineEdit_c01.setObjectName("lineEdit_c01")
        self.label_23 = QtGui.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(30, 160, 91, 16))
        self.label_23.setObjectName("label_23")
        self.lineEdit_A01 = QtGui.QLineEdit(self.tab)
        self.lineEdit_A01.setEnabled(True)
        self.lineEdit_A01.setGeometry(QtCore.QRect(130, 160, 91, 20))
        self.lineEdit_A01.setObjectName("lineEdit_A01")
        self.horizontalLayoutWidget = QtGui.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 690, 361, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_D01 = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_D01.setAutoExclusive(True)
        self.checkBox_D01.setObjectName("checkBox_D01")
        self.horizontalLayout.addWidget(self.checkBox_D01)
        self.checkBox_D02 = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_D02.setAutoExclusive(True)
        self.checkBox_D02.setObjectName("checkBox_D02")
        self.horizontalLayout.addWidget(self.checkBox_D02)
        self.toolButton_01 = QtGui.QToolButton(self.tab)
        self.toolButton_01.setGeometry(QtCore.QRect(340, 490, 31, 20))
        self.toolButton_01.setObjectName("toolButton_01")
        self.pushButton_02 = QtGui.QPushButton(self.tab)
        self.pushButton_02.setGeometry(QtCore.QRect(210, 450, 161, 31))
        self.pushButton_02.setObjectName("pushButton_02")
        self.pushButton_03 = QtGui.QPushButton(self.tab)
        self.pushButton_03.setGeometry(QtCore.QRect(220, 820, 161, 31))
        self.pushButton_03.setObjectName("pushButton_03")
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(350, 0, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtGui.QPlainTextEdit(self.tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 30, 341, 71))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(10, 790, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(10, 730, 131, 16))
        self.label_13.setObjectName("label_13")
        self.line_6 = QtGui.QFrame(self.tab)
        self.line_6.setGeometry(QtCore.QRect(10, 740, 351, 20))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.checkBox_E01 = QtGui.QCheckBox(self.tab)
        self.checkBox_E01.setGeometry(QtCore.QRect(10, 760, 181, 16))
        self.checkBox_E01.setObjectName("checkBox_E01")
        self.lineEdit_D01 = QtGui.QLineEdit(self.tab)
        self.lineEdit_D01.setEnabled(True)
        self.lineEdit_D01.setGeometry(QtCore.QRect(80, 790, 41, 20))
        self.lineEdit_D01.setAccessibleName("")
        self.lineEdit_D01.setObjectName("lineEdit_D01")
        self.horizontalSlider_3 = QtGui.QSlider(self.tab)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(140, 790, 231, 22))
        self.horizontalSlider_3.setMinimum(1)
        self.horizontalSlider_3.setMaximum(100)
        self.horizontalSlider_3.setProperty("value", 50)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "RIB Generator", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Shutter Opening", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_B04.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Motion Blur Type", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_B03.setText(QtGui.QApplication.translate("MainWindow", "Ray traced Motion Blur", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_B01.setText(QtGui.QApplication.translate("MainWindow", "Motion Blur", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Shutter Timing", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Start/End", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_C01.setText(QtGui.QApplication.translate("MainWindow", "Subdivscheme", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "RIB Archive Option", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Motion Samples", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Frame Open", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Frame Center", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Frame Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Shutter Angle", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0, QtGui.QApplication.translate("MainWindow", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(1, QtGui.QApplication.translate("MainWindow", "Subframe", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_01.setText(QtGui.QApplication.translate("MainWindow", "Generate RIBArchive", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Note:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Cache time range", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_A01.setText(QtGui.QApplication.translate("MainWindow", "Current Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_A02.setText(QtGui.QApplication.translate("MainWindow", "Start/End Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "with Motion Blur", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_B02.setText(QtGui.QApplication.translate("MainWindow", "Camera Blur", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Current Project:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_C02.setText(QtGui.QApplication.translate("MainWindow", "assign Lambert Shader / reyes", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_c01.setText(QtGui.QApplication.translate("MainWindow", "type information before push \"Generate Rib Archive\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("MainWindow", "Curent Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_D01.setText(QtGui.QApplication.translate("MainWindow", "Delayed Read Archive", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_D02.setText(QtGui.QApplication.translate("MainWindow", "Read Archive", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_01.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_02.setText(QtGui.QApplication.translate("MainWindow", "Get ShaveRIBArchive", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_03.setText(QtGui.QApplication.translate("MainWindow", "Publish RIB Archive", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Percentage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "GPU Cache Option", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_E01.setText(QtGui.QApplication.translate("MainWindow", "reduce GPU cache Mesh Count", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_D01.setText(QtGui.QApplication.translate("MainWindow", "50", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "RIB Generate", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "RIB Check", None, QtGui.QApplication.UnicodeUTF8))




        self.currentProj = pm.workspace(q=True, rd=True)
        self.currentFrame = cmds.currentTime( query=True )
        self.plainTextEdit.setPlainText(self.currentProj)
        self.currentStartFrame = float(pm.getAttr('defaultRenderGlobals.startFrame'))
        self.currentEndFrame = float(pm.getAttr('defaultRenderGlobals.endFrame'))
        
        self.lineEdit_A01.setText("%s"%self.currentFrame)
        self.lineEdit_A02.setText("%s"%self.currentStartFrame)
        self.lineEdit_A03.setText("%s"%self.currentEndFrame)
        
        self.lineEdit_B01.setText('%s'%self.horizontalSlider.value())
        self.lineEdit_B02.setText('0.000')
        self.lineEdit_B03.setText('1.000')

        #self.checkBox_B01.setChecked(True)
        pm.setAttr('renderManRISGlobals.rman__torattr___motionBlur',0)
        self.ribGenDict['motionBlurCheck'] = '0'
        self.checkBox_B01.setChecked(False)
        self.setMotionOptionInit

        self.checkBox_A01.setChecked(True)
        self.checkBox_B02.setEnabled(False)
        self.checkBox_B02.setChecked(False)
        self.checkBox_B03.setChecked(False) 
        self.checkBox_B03.setEnabled(False)
        
        self.lineEdit_B01.setEnabled(False) 
        self.lineEdit_B02.setEnabled(False)
        self.lineEdit_B03.setEnabled(False)
        self.lineEdit_B04.setEnabled(False)

        self.comboBox.setEnabled(False)
        self.comboBox_2.setEnabled(False)
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider_2.setEnabled(False)
        
#---------------------------GPU Cache Option-------------------------------------        
        self.checkBox_E01.setChecked(False)
        self.lineEdit_D01.setEnabled(False) 
        self.horizontalSlider_3.setEnabled(False)

#        self.checkBox_C02.setChecked(False)
    
        self.checkBox_D01.setChecked(True)
        self.checkBox_D02.setChecked(False)
        self.comboxDisc ={'frameOpen':0,'frameCenter':1,'frameClose':2}
        self.comboBox.setCurrentIndex(self.comboxDisc[pm.getAttr('renderManRISGlobals.rman__toropt___shutterTiming')])
        self.combox_2Disc={'frame':0,'subframe':1}
        self.comboBox_2.setCurrentIndex(self.combox_2Disc[pm.getAttr('renderManRISGlobals.rman__toropt___motionBlurType')])

        



class mod_MainWindow(QtGui.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtGui.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)

#---------------------------Data Sheet------------------初始值 Start----------------------------------------------------------------------------------        
#        self.ribGenDict ={}
#        self.exportDict ={}
        self.ribGenDict = {'currentFrameCheck':'1','startEndFrameCheck':'0','currentFrameValue':'1.0','startFrameValue':'1.0',
              'endFrameValue':'10.0','motionBlurCheck':'0','cameraBlurCheck':'0','shutterAngleValue':'80.0',
              'shutterOpeningOn':'0.0','shutterOpeningOff':'1.0','shutterTiming':'frameOpen','motionBlurType':'frame',
              'motionSamples':'2.0','rayTracedMotionBlurCheck':'0','subdivschemeCheck':'0','assignLamertShader':'0',
              'delayedReadArchiveCheck':'1','ReadArchiveCheck':'0',
              'noteText':'type information before push "Generate Rib Archive"',
              'exportCmd':'\"rmanExportRIBCompression=0;rmanExportFullPaths=0;rmanExportGlobalLights=0;rmanExportLocalLights=0;rmanExportCoordinateSystems=0;rmanExportShaders=1;rmanExportAttributeBlock=0;',
              'finalRibExportCmd':'none',
              'finalGpuExportCmd':'none',
              'cacheForder':'none',
              'ribArchiveFileName':'none',
              'gpuCacheFileName':'none'}
        self.exportDict = {'projectName':'fullProjectPathAndName','ribIndexNumber':'00000','referenceAsset':'referenceAssetName',
              'referenceAssetPosition':'referenceAssetFullPathName','ribArchiveName':'ribName','gpuCachePosition':'gpufullPathName',
              'shadeMode':'beauty','subD':'enable',
              'ribCachePosition':'ribfullPathName','ribArchiveDuration':'1.0','creator':'creatorName','buildTime':'yyyymmdd',
              'ribScreenShot':'screenShotImagePosition','version':'xxxx','exportNoteText':'none'}
    #---------------------------Data Sheet------------------變更為現在資料--------------------------------------------------------------------------------- 
        self.ribGenDict['currentFrameCheck'] = "1"
        self.ribGenDict['startEndFrameCheck'] = "0"
        
        self.ribGenDict['currentFrameValue']=str(cmds.currentTime( query=True ))
        self.ribGenDict['startFrameValue']=str(pm.getAttr('defaultRenderGlobals.startFrame'))
        self.ribGenDict['endFrameValue']=str(pm.getAttr('defaultRenderGlobals.endFrame'))
        
        #self.ribGenDict['motionBlurCheck'] = str(pm.getAttr('renderManRISGlobals.rman__torattr___motionBlur'))
        self.ribGenDict['cameraBlurCheck'] = str(pm.getAttr('renderManRISGlobals.rman__torattr___cameraBlur'))
        
        self.ribGenDict['shutterAngleValue']=str(pm.getAttr('renderManRISGlobals.rman__toropt___shutterAngle'))
        self.ribGenDict['shutterOpeningOn']=str(pm.getAttr('renderManRISGlobals.rman__riopt__Camera_shutteropening0'))
        self.ribGenDict['shutterOpeningOff']=str(pm.getAttr('renderManRISGlobals.rman__riopt__Camera_shutteropening1'))
        self.ribGenDict['shutterTiming'] = pm.getAttr("renderManRISGlobals.rman__toropt___shutterTiming")
        self.ribGenDict['motionBlurType'] = pm.getAttr("renderManRISGlobals.rman__toropt___motionBlurType")
        self.ribGenDict['motionSamples']=str(pm.getAttr('renderManRISGlobals.rman__torattr___motionSamples'))
        self.ribGenDict['rayTracedMotionBlurCheck'] = "0"
        self.ribGenDict['subdivschemeCheck'] = "0"
        self.ribGenDict['assignLamertShader'] = "0"
        self.ribGenDict['delayedReadArchiveCheck'] = "1"
        self.ribGenDict['ReadArchiveCheck'] = "0"
        self.meshReduceValue = 50


        #self.selectedGeo=[]


    
        

        
#---------------------------Data Sheet-------------------初始值 END--------------------------------------------------------------------------------------         


#-----------------------------------------signalbegin-------------------------------------------------------------------
        # self.setWindowFlags(QtCore.Qt.Tool)
        self.setupUi(self)
        
        #reset button signal      
        self.pushButton.clicked.connect(self.modpushButton)
        
        #Cache time range mode ,checkbox modify and returen value to dictionary checkBox_A01 ,checkBox_A02
        self.checkBox_A01.stateChanged.connect(self.modcheckBox_A01)
        self.checkBox_A01.stateChanged.connect(self.modcheckBox_A02)
        
        #store value from current frame, start/end frame
        self.lineEdit_A01.textChanged.connect(self.modlineEdit_A01)
        self.lineEdit_A02.textChanged.connect(self.modlineEdit_A02)
        self.lineEdit_A03.textChanged.connect(self.modlineEdit_A03)
        
        #MotionBlurCheckBox,CameraBlurCheckBok modify and store value to dictionary checkBox_B01 ,checkBox_B02
        self.checkBox_B01.stateChanged.connect(self.modcheckBox_B01)
        self.checkBox_B02.stateChanged.connect(self.modcheckBox_B02)
        self.checkBox_B03.stateChanged.connect(self.modcheckBox_B03)

        
        
        #ShutterComboBox ,MotionBlurTypeComboBox select modify signal
        self.comboBox.currentIndexChanged.connect(self.modcomboBox)
        self.comboBox_2.currentIndexChanged.connect(self.modcomboBox_2)
        
        #store value from current frame, shutter angle , shutter opening
        self.horizontalSlider.valueChanged.connect(self.modlineEdit_B01)
        self.lineEdit_B01.textChanged.connect(self.modhorizontalSlider)
        self.lineEdit_B02.textChanged.connect(self.modlineEdit_B02)
        self.lineEdit_B03.textChanged.connect(self.modlineEdit_B03)


        
        self.horizontalSlider_2.valueChanged.connect(self.modlineEdit_B04)
        self.lineEdit_B04.textChanged.connect(self.modhorizontalSlider_2)
        
        
        self.horizontalSlider_3.valueChanged.connect(self.modlineEdit_D01)
        self.lineEdit_D01.textChanged.connect(self.modhorizontalSlider_3)
        
        
        self.pushButton_01.clicked.connect(self.modpushButton_01)

        #SubdivschemeCheckBox, assignLambertShaderCheckBok modify and store value to dictionary checkBox_C01 ,checkBox_C02
        self.checkBox_C01.stateChanged.connect(self.modcheckBox_C01)
        self.checkBox_C02.stateChanged.connect(self.modcheckBox_C02)
        
        
        #DelayedReadArchiveCheckBox, ReadArchiveCheckBok modify and store value to dictionary checkBox_D01 ,checkBox_D02
        self.checkBox_D01.stateChanged.connect(self.modcheckBox_D01)
        self.checkBox_D02.stateChanged.connect(self.modcheckBox_D02)
        
        
        self.pushButton_02.clicked.connect(self.modpushButton_02)
        self.pushButton_03.clicked.connect(self.modpushButton_03)
        
        
        self.toolButton_01.clicked.connect(self.modtoolButton_01)
        
        
        self.checkBox_E01.stateChanged.connect(self.modcheckBox_E01)
        
        
#-----------------------------------------signal End-------------------------------------------------------------------        
        
#    def projectInfo(self):
#        self.plainTextEditA.setPlainText("ssss")

    def modcheckBox_A01(self):
        if self.checkBox_A01.isChecked() == True:
            self.ribGenDict['currentFrameCheck'] = '1'
            self.ribGenDict['startEndFrameCheck'] ='0'

    def modcheckBox_A02(self):
        if self.checkBox_A02.isChecked() == True:
            self.ribGenDict['currentFrameCheck'] = '0'
            self.ribGenDict['startEndFrameCheck'] ='1'

    def modlineEdit_A01(self):
        newCurentFrame = float(self.lineEdit_A01.text())
        cmds.currentTime( newCurentFrame )
       # print cmds.currentTime( newCurentFrame )
        self.ribGenDict['currentFrameValue'] = str(cmds.currentTime( newCurentFrame ))

    def modlineEdit_A02(self):
        newStartFrame = float(self.lineEdit_A02.text())
        pm.setAttr('defaultRenderGlobals.startFrame',newStartFrame)
        self.ribGenDict['startFrameValue'] = self.lineEdit_A02.text()

        
    def modlineEdit_A03(self):
        newEndFrame = float(self.lineEdit_A03.text())
        pm.setAttr('defaultRenderGlobals.endFrame',newEndFrame)   
        self.ribGenDict['endFrameValue'] = self.lineEdit_A03.text()
#----------------------------------------------------------------------------------------------------------

    def setMotionOptionInit(self):

        
        
        if pm.getAttr('renderManRISGlobals.rman__torattr___motionBlur') == 0:
            print "motion blur not Enable"
            self.ribGenDict['motionBlurCheck'] = '0'
            self.ribGenDict['cameraBlurCheck'] ='0'
            self.checkBox_B01.setChecked(False)

            self.checkBox_B02.setChecked(False)
            self.checkBox_B02.setEnabled(False)
            self.checkBox_B03.setEnabled(False)
            self.lineEdit_B01.setEnabled(False)
            self.lineEdit_B02.setEnabled(False)
            self.lineEdit_B03.setEnabled(False)
            self.lineEdit_B04.setEnabled(False)
            self.comboBox.setEnabled(False)
            self.comboBox_2.setEnabled(False)
            self.horizontalSlider.setEnabled(False)
            self.horizontalSlider_2.setEnabled(False)
            
        else:
            pm.getAttr('renderManRISGlobals.rman__torattr___motionBlur') == 1 
            print "motion blur Enable"
            self.ribGenDict['motionBlurCheck'] = '1'
            self.ribGenDict['cameraBlurCheck'] ='0'
            self.checkBox_B01.setChecked(True)
            self.checkBox_B02.setEnabled(True)
            self.checkBox_B03.setEnabled(True)
            self.lineEdit_B01.setEnabled(True)
            self.lineEdit_B02.setEnabled(True)
            self.lineEdit_B03.setEnabled(True)
            self.lineEdit_B04.setEnabled(True)
            self.comboBox.setEnabled(True)
            self.comboBox_2.setEnabled(True)
            self.horizontalSlider.setEnabled(True)
            self.horizontalSlider_2.setEnabled(True)
            
            self.ribGenDict['shutterAngleValue'] =str('%1.f'%pm.getAttr('renderManRISGlobals.rman__toropt___shutterAngle'))
            
            self.lineEdit_B01.setText(self.ribGenDict['shutterAngleValue'])
   #         self.ribGenDict['shutterAngleValue'] =str(newShutterAngle)
   #         pm.setAttr('renderManRISGlobals.rman__toropt___shutterAngle',float(self.ribGenDict['shutterAngleValue']))
            
            self.ribGenDict['shutterOpeningOn'] =str('%.3f'%pm.getAttr('renderManRISGlobals.rman__riopt__Camera_shutteropening0'))
            self.ribGenDict['shutterOpeningOff'] =str('%.3f'%pm.getAttr('renderManRISGlobals.rman__riopt__Camera_shutteropening1'))

            self.lineEdit_B02.setText(self.ribGenDict['shutterOpeningOn']) 
            self.lineEdit_B03.setText(self.ribGenDict['shutterOpeningOff']) 
            
            self.lineEdit_B04.setText(self.ribGenDict['motionSamples'])
            
            self.ribGenDict['rayTracedMotionBlurCheck'] =str(pm.getAttr('renderManRISGlobals.rman__riattr__trace_samplemotion'))
            self.checkBox_B03.setChecked(int(self.ribGenDict['rayTracedMotionBlurCheck']))



#----------------------------check motion blur option start----------------------------

    def modcheckBox_B01(self):
        if self.checkBox_B01.isChecked() == True:                     #motion blur check on and get info from renderman Globals
            self.ribGenDict['motionBlurCheck'] = '1'
            self.ribGenDict['cameraBlurCheck'] ='0'
            self.checkBox_B02.setEnabled(True)
            self.checkBox_B03.setEnabled(True)
            self.lineEdit_B01.setEnabled(True)
            self.lineEdit_B02.setEnabled(True)
            self.lineEdit_B03.setEnabled(True)
            self.lineEdit_B04.setEnabled(True)
            self.comboBox.setEnabled(True)
            self.comboBox_2.setEnabled(True)
            self.horizontalSlider.setEnabled(True)
            self.horizontalSlider_2.setEnabled(True)
            
            self.ribGenDict['shutterAngleValue'] =str('%1.f'%pm.getAttr('renderManRISGlobals.rman__toropt___shutterAngle'))
            
            self.lineEdit_B01.setText(self.ribGenDict['shutterAngleValue'])
   #         self.ribGenDict['shutterAngleValue'] =str(newShutterAngle)
   #         pm.setAttr('renderManRISGlobals.rman__toropt___shutterAngle',float(self.ribGenDict['shutterAngleValue']))
            
            self.ribGenDict['shutterOpeningOn'] =str('%.3f'%pm.getAttr('renderManRISGlobals.rman__riopt__Camera_shutteropening0'))
            self.ribGenDict['shutterOpeningOff'] =str('%.3f'%pm.getAttr('renderManRISGlobals.rman__riopt__Camera_shutteropening1'))

            self.lineEdit_B02.setText(self.ribGenDict['shutterOpeningOn']) 
            self.lineEdit_B03.setText(self.ribGenDict['shutterOpeningOff']) 
            
            self.lineEdit_B04.setText(self.ribGenDict['motionSamples'])
            
            self.ribGenDict['rayTracedMotionBlurCheck'] =str(pm.getAttr('renderManRISGlobals.rman__riattr__trace_samplemotion'))
            self.checkBox_B03.setChecked(int(self.ribGenDict['rayTracedMotionBlurCheck']))
            
            pm.setAttr('renderManRISGlobals.rman__torattr___motionBlur',1)
            if self.checkBox_B02.isChecked() == False:
                pm.setAttr('renderManRISGlobals.rman__torattr___cameraBlur',0)
                
        elif self.checkBox_B01.isChecked() == False:
            self.ribGenDict['motionBlurCheck'] = '0'
            self.ribGenDict['cameraBlurCheck'] ='0'
            self.checkBox_B02.setChecked(False)
            self.checkBox_B02.setEnabled(False)
            self.checkBox_B03.setEnabled(False)
            self.lineEdit_B01.setEnabled(False)
            self.lineEdit_B02.setEnabled(False)
            self.lineEdit_B03.setEnabled(False)
            self.lineEdit_B04.setEnabled(False)
            self.comboBox.setEnabled(False)
            self.comboBox_2.setEnabled(False)
            self.horizontalSlider.setEnabled(False)
            self.horizontalSlider_2.setEnabled(False)
            pm.setAttr('renderManRISGlobals.rman__torattr___motionBlur',0)
            
    def modcheckBox_B02(self):
        if self.checkBox_B01.isChecked() == True:           
            if self.checkBox_B02.isChecked() == True:
                self.ribGenDict['motionBlurCheck'] = '1'
                self.ribGenDict['cameraBlurCheck'] ='1'
                pm.setAttr('renderManRISGlobals.rman__torattr___cameraBlur',1)
            else:
                self.ribGenDict['motionBlurCheck'] = '1'
                self.ribGenDict['cameraBlurCheck'] ='0'
                pm.setAttr('renderManRISGlobals.rman__torattr___cameraBlur',0)
        elif self.checkBox_B01.isChecked() == False :
            self.ribGenDict['motionBlurCheck'] = '0'
            self.ribGenDict['cameraBlurCheck'] ='0'
            self.checkBox_B02.setEnabled(False)
            self.lineEdit_B01.setEnabled(False)
            



    def modlineEdit_B01(self):
        self.lineEdit_B01.setText('%s'%self.horizontalSlider.value())
        

    def modlineEdit_B02(self):
        newOpeningAStr = str(self.lineEdit_B02.text())
 #       newOpeningA = float(newOpeningAStr)
        self.ribGenDict['shutterOpeningOn']=newOpeningAStr
        pm.setAttr('renderManRISGlobals.rman__riopt__Camera_shutteropening0',float(newOpeningAStr))
 
        
    def modlineEdit_B03(self):
        newOpeningBStr = str(self.lineEdit_B03.text())
#        newOpeningB = float(newOpeningBStr)
        self.ribGenDict['shutterOpeningOff']=newOpeningBStr
        pm.setAttr('renderManRISGlobals.rman__riopt__Camera_shutteropening1',float(newOpeningBStr))

        
    def modhorizontalSlider(self):        
        self.horizontalSlider.setValue(int(self.lineEdit_B01.text()))
        newShutterAngle = self.horizontalSlider.value()
        self.ribGenDict['shutterAngleValue'] =str(newShutterAngle)
        pm.setAttr('renderManRISGlobals.rman__toropt___shutterAngle',float(self.ribGenDict['shutterAngleValue']))


    def modcomboBox(self):
        print self.comboBox.currentIndex()
        if self.comboBox.currentIndex() == 0:
            self.ribGenDict['shutterTiming'] = 'frameOpen'
            pm.setAttr('renderManRISGlobals.rman__toropt___shutterTiming','frameOpen')
            
        elif self.comboBox.currentIndex() == 1:
            self.ribGenDict['shutterTiming'] = 'frameCenter'
            pm.setAttr('renderManRISGlobals.rman__toropt___shutterTiming','frameCenter')

        elif self.comboBox.currentIndex() == 2:
            self.ribGenDict['shutterTiming'] = 'frameClose'
            pm.setAttr('renderManRISGlobals.rman__toropt___shutterTiming','frameClose')
            

    def modcomboBox_2(self):
        if self.comboBox_2.currentIndex() == 0:
            self.ribGenDict['motionBlurType'] = 'frame'
            pm.setAttr("renderManRISGlobals.rman__toropt___motionBlurType",'frame')
                       
        elif self.comboBox_2.currentIndex() == 1:
            self.ribGenDict['motionBlurType'] = 'subframe'
            pm.setAttr("renderManRISGlobals.rman__toropt___motionBlurType",'subframe')


     


    def modcheckBox_B03(self):
        if self.checkBox_B03.isChecked() == True:
            self.ribGenDict['rayTracedMotionBlurCheck'] ='1'
        elif self.checkBox_B03.isChecked() == False:
            self.ribGenDict['rayTracedMotionBlurCheck'] ='0'
            
            

        
    def modlineEdit_B04(self):
        self.lineEdit_B04.setText('%s'%self.horizontalSlider_2.value())
        
    def modhorizontalSlider_2(self):        
        self.horizontalSlider_2.setValue(int(self.lineEdit_B04.text()))
        newMotionSample = self.horizontalSlider_2.value()
        self.ribGenDict['motionSamples'] =str(newMotionSample)



    def modcheckBox_E01(self):
        
        if self.checkBox_E01.isChecked() == 1:
            self.lineEdit_D01.setEnabled(True) 
            self.horizontalSlider_3.setEnabled(True)
        else:
            self.lineEdit_D01.setEnabled(False) 
            self.horizontalSlider_3.setEnabled(False)
            
        self.meshReduceValue = self.horizontalSlider_3.value()
       # print self.meshReduceValue

    def modlineEdit_D01(self):
        self.lineEdit_D01.setText('%s'%self.horizontalSlider_3.value())
        self.meshReduceValue = self.horizontalSlider_3.value()
      #  print self.meshReduceValue

        
    def modhorizontalSlider_3(self):        
        self.horizontalSlider_3.setValue(int(self.lineEdit_D01.text()))
        newMotionSample = self.horizontalSlider_3.value()
        self.meshReduceValue = self.horizontalSlider_3.value()
       # print self.meshReduceValue





#----------------------------check motion blur option End---------------------------    
            
    def modcheckBox_C01(self):
        if self.checkBox_C01.isChecked() == True:
            self.ribGenDict['subdivschemeCheck'] ='1'
        elif self.checkBox_C01.isChecked() == False:
            self.ribGenDict['subdivschemeCheck'] ='0'
            
    def modcheckBox_C02(self):
        if self.checkBox_C02.isChecked() == True:
            self.ribGenDict['assignLamertShader'] ='1'
        elif self.checkBox_C02.isChecked() == False:
            self.ribGenDict['assignLamertShader'] ='0'
                        
            
    def modcheckBox_D01(self):
        if self.checkBox_D01.isChecked() == True:
            self.ribGenDict['delayedReadArchiveCheck'] = '1'
            self.ribGenDict['ReadArchiveCheck'] ='0'
            self.checkBox_D02.setChecked(False)
        else:
            self.ribGenDict['delayedReadArchiveCheck'] = '0'
            self.ribGenDict['ReadArchiveCheck'] ='1'
            self.checkBox_D02.setChecked(True)            
            
    def modcheckBox_D02(self):
        if self.checkBox_D02.isChecked() == True:
            self.ribGenDict['delayedReadArchiveCheck'] = '0'
            self.ribGenDict['ReadArchiveCheck'] ='1'
            self.checkBox_D01.setChecked(False)
        else:
            self.ribGenDict['delayedReadArchiveCheck'] = '1'
            self.ribGenDict['ReadArchiveCheck'] ='0'
            self.checkBox_D02.setChecked(False)           





    def modpushButton(self):
        self.ribGenDict = {'currentFrameCheck':'1','startEndFrameCheck':'0','currentFrameValue':'1.0','startFrameValue':'1.0',
        'endFrameValue':'10.0','motionBlurCheck':'0','cameraBlurCheck':'0','shutterAngleValue':'80.0',
        'shutterOpeningOn':'0.0','shutterOpeningOff':'1.0','shutterTiming':'frameOpen','motionBlurType':'frame',
        'motionSamples':'2.0','rayTracedMotionBlurCheck':'0','subdivschemeCheck':'0','assignLamertShader':'0',
        'delayedReadArchiveCheck':'1','ReadArchiveCheck':'0',
        'noteText':'type information before push "Generate Rib Archive"',
                      'exportCmd':'\"rmanExportRIBCompression=0;rmanExportFullPaths=0;rmanExportGlobalLights=0;rmanExportLocalLights=0;rmanExportCoordinateSystems=0;rmanExportShaders=1;rmanExportAttributeBlock=0;',
              'finalRibExportCmd':'none',
              'finalGpuExportCmd':'none',
              'cacheForder':'none',              
              'ribArchiveFileName':'none',
              'gpuCacheFileName':'none'}                      

        self.checkBox_A01.setChecked(True)
        self.checkBox_B01.setChecked(False)
        self.checkBox_B03.setChecked(False)
        self.checkBox_C01.setChecked(False)
        self.checkBox_C02.setChecked(False)
        self.checkBox_D01.setChecked(True)
        

#----------------------------------------------所選取的Group Start------------------------------------------------------------


    def selectGrpList(self,singleGrp):
        self.selectedTGrpList= pm.ls( sl=True)


#----------------------------------------------所選取的Group End------------------------------------------------------------









#---------------------------------------------------選擇物件shape定義 Start---由所選的group中選出 shape------------------------------------------------------       

 
    def selectedShape(self,singleGrp):
        grpName = self.singleGrp
        self.selectedGeoShape = pm.ls(grpName, type='geometryShape',dag=True,ap=True,lf=True)
      #  pm.ls(sl=True, type='geometryShape',dag=True,ap=True,lf=True)
        #pm.nodeType(pm.ls(sl=True))
       # pm.ls(sl=True,dag=1)
#---------------------------------------------------選擇物件shape定義 end-----------------------------------------------------------







#-----------------------------------------define create folder Begin------------------------------------------------

    def createSelectFolder(self,singleGrp):   # singleGrp 是一個可以用來回傳單一選定的group transforme
        print "run createSelectFolder Function"
        cacheFolderCreate = self.currentProj + 'data/cache/' + self.singleGrp

        pm.sysFile( cacheFolderCreate, makeDir=True )  # create folder
        
        self.ribGenDict['cacheForder'] = cacheFolderCreate
        print "run createSelectFolder Function Completed"
#-----------------------------------------define create folder End------------------------------------------------
        
   
   

   

#--------------------------------------------Define RIB Archive and GPUCache File Name Begin------------------------------------------------------------        
    def cacheFileName(self,singleGrp):
        print "run CacheFileName Function"
        self.ribGenDict['ribArchiveFileName'] =''
        self.ribGenDict['gpuCacheFileName'] =''
        ribArchiveFileName = self.singleGrp         
        fileOptionDisc ={'subdivscheme':'',
                         'assignLamertShader':'',
                         'motionBlur':'',
                         'currentFrame':''}
        
        if self.ribGenDict['subdivschemeCheck'] == "1":            
            fileOptionDisc['subdivscheme'] = 'SubD'
        else:
            fileOptionDisc['subdivscheme'] = ''  
             
        if self.ribGenDict['assignLamertShader'] == "1":
            fileOptionDisc['assignLamertShader'] = 'Reyes'
        else:
            fileOptionDisc['assignLamertShader'] = ''
            
        if self.ribGenDict['motionBlurCheck'] == "1":
            fileOptionDisc['motionBlur']= 'Mblur'
        else:    
            fileOptionDisc['motionBlur']= ''
            
        if self.ribGenDict['currentFrameCheck'] == '0':
            fileOptionDisc['currentFrame']= str(self.ribGenDict['currentFrameValue'])
        else:
            fileOptionDisc['currentFrame']= ''
            
       # self.ribGenDict['ribArchiveFileName'] = ribArchiveFileName+fileOptionDisc['subdivscheme']+fileOptionDisc['assignLamertShader']+fileOptionDisc['motionBlur']+fileOptionDisc['currentFrame']+".rib"
       # self.ribGenDict['gpuCacheFileName'] = ribArchiveFileName+fileOptionDisc['subdivscheme']+fileOptionDisc['assignLamertShader']+fileOptionDisc['motionBlur']+fileOptionDisc['currentFrame']
        self.ribGenDict['ribArchiveFileName'] = ribArchiveFileName+fileOptionDisc['subdivscheme']+fileOptionDisc['assignLamertShader']+fileOptionDisc['motionBlur']+".rib"
        self.ribGenDict['gpuCacheFileName'] = ribArchiveFileName+fileOptionDisc['subdivscheme']+fileOptionDisc['assignLamertShader']+fileOptionDisc['motionBlur']
       
       # print self.ribGenDict['ribArchiveFileName']
       # print self.ribGenDict['gpuCacheFileName']
        self.exportRibName = self.ribGenDict['ribArchiveFileName']
        self.gpuCacheFileName = self.ribGenDict['gpuCacheFileName']
        print "run CacheFileName Function Completed"
 
#--------------------------------------------Define RIB Archive and GPUCache File Name END------------------------------------------------------------        
 
 
 
 
 
 
     
 

#---------------------------------------------------export Cmd Start--------------------------------------------------------------------
    def getRibExportCmd(self,exportCmd): 
        print "run getRibExportCmd Function"

        #定義輸出資料夾與檔案名稱  
        self.cacheFileName(self)  
        
        exportRibNamePath = self.ribGenDict['cacheForder']+'/' + self.exportRibName
    
        ribFileDir = self.ribGenDict['cacheForder']
        startFrameReal= str(float(self.ribGenDict['startFrameValue']))
        endFrameReal = str(float(self.ribGenDict['endFrameValue']))
        gpuCacheFileNameSingle = self.gpuCacheFileName
       # if str(int(self.ribGenDict['currentFrameCheck'])) == '1':
        if self.ribGenDict['currentFrameCheck'] == '1':

            cmd02 ='rmanExportMultipleFrames=0;'
            cmd03='rmanExportStartFrame=%s;'%self.ribGenDict['currentFrameValue']
            cmd04='rmanExportEndFrame=%s;' %self.ribGenDict['currentFrameValue']
            cmd05='rmanExportByFrame=1\"'
            ribExportSingalOption=self.ribGenDict['exportCmd']+cmd02+ cmd03+ cmd04 + cmd05
            # 輸出最終指令
            self.ribGenDict['finalRibExportCmd']="file -force -op"+" "+str(ribExportSingalOption)+" "+"-typ"+" "+"\"RIB_Archive\""+" "+"-pr"+" "+"-es"+" "+"\"%s"%exportRibNamePath+"\""
            self.ribGenDict['finalGpuExportCmd'] = str("gpuCache -startTime "+"%s"%self.ribGenDict['currentFrameValue']+" -endTime "+"%s"%self.ribGenDict['currentFrameValue']+" -optimize -optimizationThreshold 200000 -writeMaterials -dataFormat ogawa "+ "-directory "+"\"%s"%ribFileDir+"\"" + " -fileName " + "\" %s"%gpuCacheFileNameSingle+"\"")
                                                       #gpuCache    開始時間                   變數 --------------------------結束時間-----------變數--------------------------------------------------------------------------------------------------------

    #        pm.mel.eval('%s'%exportCmd)
    #        pm.mel.eval('%s'%exportGpuCacheCmd)
    #        print ribExportSingalOption
        else: 
            cmd02 ='rmanExportMultipleFrames=1;'
            #cmd03='rmanExportStartFrame=%s;'%self.ribGenDict['startFrameValue']
           # cmd04='rmanExportEndFrame=%s;'%self.ribGenDict['endFrameValue']
            cmd03='rmanExportStartFrame=%s;'%startFrameReal #輸出的指令必須是真正的格數 -1
            cmd04='rmanExportEndFrame=%s;'%endFrameReal #輸出的指令必須是真正的格數 -1
            cmd05='rmanExportByFrame=1\"'
            ribExportMultiOptions = self.ribGenDict['exportCmd']+cmd02+ cmd03+ cmd04 + cmd05
           # if 
            self.ribGenDict['finalRibExportCmd'] = "file -force -op"+" "+str(ribExportMultiOptions)+" "+"-typ"+" "+"\"RIB_Archive\""+" "+"-pr"+" "+"-es"+" "+"\"%s"%exportRibNamePath+"\""
            self.ribGenDict['finalGpuExportCmd'] = str("gpuCache -startTime "+"%s"%self.ribGenDict['startFrameValue']+" -endTime "+"%s"%self.ribGenDict['endFrameValue']+" -optimize -optimizationThreshold 200000 -writeMaterials -dataFormat ogawa "+ "-directory "+"\"%s"%ribFileDir+"\"" + " -fileName " + "\" %s"%gpuCacheFileNameSingle+"\"")

        print "run getRibExportCmd Function Completed"

#------------------------------------------------export Cmd End-------------------------------------------------------





#---------------------------------------------------shaveRibExport Start--------------------------------------------------------------------


    def shaveRibExport(self,singleGrp):

        print "run shaveRibExport Function start"
        #定義輸出資料夾與檔案名稱  
        ribArchiveFileName = str(self.singleGrp)
        if self.ribGenDict['currentFrameCheck'] == '0':

            
            exportRibNamePath = self.ribGenDict['cacheForder']+'/' + ribArchiveFileName

            shaveStartFrame = int(float(self.ribGenDict['startFrameValue']))
            shaveEndFrame = int(float(self.ribGenDict['endFrameValue']))

            
            while (shaveStartFrame <= shaveEndFrame):
                exportFrame = str('%04d'%shaveStartFrame)
                print exportFrame
                shaveEcportCmd = "shaveWriteRib -opa -rtc -b -gz -f"+" "+"%s"%exportFrame +" "+"\""+ exportRibNamePath+".%s"%exportFrame+".rib"+"\""
                shaveStartFrame = shaveStartFrame + 1
                print shaveEcportCmd
                pm.mel.eval(shaveEcportCmd)   #create shave and Haircur Rib Archive 
                
            print shaveStartFrame
            print shaveEndFrame
           # print endFrameReal
                   
            pm.mel.eval('%s'%self.ribGenDict['finalGpuExportCmd'])  #create Gpu Cache


        if self.ribGenDict['currentFrameCheck'] == '1':

            
            exportRibNamePath = self.ribGenDict['cacheForder']+'/' + ribArchiveFileName
            
            currentShaveFrame = int(float(self.ribGenDict['currentFrameValue']))
            
            exportFrame = str('%04d'%currentShaveFrame)


            shaveEcportCmd = "shaveWriteRib -opa -rtc -b -gz -f"+" "+"%s"%exportFrame +" "+"\""+ exportRibNamePath +".rib"+"\""
            print shaveEcportCmd

            pm.mel.eval(shaveEcportCmd)   #create shave and Haircur Rib Archive 


                   
            pm.mel.eval('%s'%self.ribGenDict['finalGpuExportCmd'])  #create Gpu Cache


      #  self.connectGpuRib(self)
      #  if self.ribGenDict['shutterTiming'] == "frameCenter":
      #      self.batchRename(self)

       # self.batchRename(self)

        self.bBoxFind(self)

        self.zipRibFiles(self)

        

        print "run shaveRibExport Function Completed"




#---------------------------------------------------shaveRibExport End--------------------------------------------------------------------

#---------------------------------------------------賦予 SubD Start-----------------------------------------------------------
    def addSubD(self,singleShape):

        print "run addSubD Function"

        geoShape = self.singleShape         

        addSubDAttrCmdA = "rmanAddAttr "+"%s "%geoShape + "rman__torattr___subdivScheme "+ "\"\""
        addSubDAttrCmdB = "rmanAddAttr "+"%s "%geoShape + "rman__torattr___subdivFacevaryingInterp "+ "\"\""
        pm.mel.eval("%s"%addSubDAttrCmdA)
        pm.mel.eval("%s"%addSubDAttrCmdB)
        
        print "run addSubD Function Completed"
    
      
#---------------------------------------------------賦予 SubD End-----------------------------------------------------------




#---------------------------------------------------刪除 SubD Start-----------------------------------------------------------

    def delSubD(self,singleShape):

        print "run delSubD Function "

        geoShape = self.singleShape 
        try:
            pm.getAttr('%s.rman__torattr___subdivScheme'%geoShape)
            cmds.deleteAttr( "%s.rman__torattr___subdivScheme"%geoShape)
        except:
            print '%s'%geoShape +'has no subdivScheme'
        try:
            pm.getAttr('%s.rman__torattr___subdivFacevaryingInterp'%geoShape)
            cmds.deleteAttr( "%s.rman__torattr___subdivFacevaryingInterp"%geoShape)
        except:
            print '%s'%geoShape +'has no subdivFacevaryingInterp'        
            
            
        print "run delSubD Function Completed"

        
#----------------------------------------------------刪除 SubD End-----------------------------------------------------------------------




#----------------------------------------------------check Value and store the value in Dictionary Start-----------------------------------------------------------------------

    def reStoreValue(self,data):
        self.ribGenDict['currentFrameValue'] = cmds.currentTime( query=True )
        self.lineEdit_A01.setText(str(self.ribGenDict['currentFrameValue']))










#----------------------------------------------------check Value and store the value in Dictionary End-----------------------------------------------------------------------
    



#---------------------------------------------------連結GPU RIB Cache Start--------------------------------------------------------


    def connectGpuRib(self,singleGrp):
        
        print "run connectGpuRib Function "

        #selectedTGrpList= pm.ls( sl=True)
        ribArchiveShapeCount = len(pm.ls(type='RenderManArchive'))      #統計現有的RIB Archive的數量 並在+1
        #ribArchiveShapeCountInt = len(pm.ls(type='RenderManArchive'))+1
        try:
            pm.select('ribAssetGrp')
        except:
            self.createRibAssetGrp = pm.createNode( 'transform',n='ribAssetGrp')


        
        ribArchiveNodetransformName = self.singleGrp
        ribArchiveShapeCountStr = str(ribArchiveShapeCount+1)
        ribTransformName = pm.createNode( 'transform', n="%s"%ribArchiveNodetransformName+"RIBArchive%s"%ribArchiveShapeCountStr ,p='ribAssetGrp')  #產生RIB Archive 最上層group
      #  print ribTransformName
      #  print type(ribTransformName)
        ribArchiveShapeName = pm.createNode('RenderManArchive',n='%s'%ribArchiveNodetransformName+'_ribShape%s'%ribArchiveShapeCountStr) #產生RIB Archive shape 並產生所屬 Transform    
        gpuCacheShapeName = pm.createNode('gpuCache',n='%s'%ribArchiveNodetransformName+'_GpuCacheShape%s'%ribArchiveShapeCountStr) #產生GPUCache shape 並產生所屬 Transform    
        pm.parent(ribArchiveShapeName,ribTransformName)  #將 RIB Archive parent 到 所屬最上層Group
        pm.parent(gpuCacheShapeName,ribTransformName)    #將 GpuCache parent 到 所屬最上層Group
     
        self.gpuCacheShape = gpuCacheShapeName
        self.ribArchiveShape = ribArchiveShapeName
        self.ribTransform = '%s'%ribArchiveNodetransformName+'_rib%s'%ribArchiveShapeCountStr
        self.gpuTransform = '%s'%ribArchiveNodetransformName+'_GpuCache%s'%ribArchiveShapeCountStr   
      #  print self.ribGenDict['currentFrameCheck']
      #  print self.ribGenDict['shutterTiming']
      #  print self.ribGenDict['motionBlurCheck']

        if self.ribGenDict['currentFrameCheck'] == '1':           
            gpuFullName =self.ribGenDict['cacheForder']+'/'+self.ribGenDict['gpuCacheFileName']+'.abc'
            ribFullName =self.ribGenDict['cacheForder']+'/'+self.ribGenDict['gpuCacheFileName']+'.zip'
        else:
            gpuFullName =self.ribGenDict['cacheForder']+'/'+self.ribGenDict['gpuCacheFileName']+'.abc'
          #  ribFullName =self.ribGenDict['cacheForder']+'/'+self.ribGenDict['gpuCacheFileName']+'.$F4.rib'
            ribFullName =self.ribGenDict['cacheForder']+'/'+self.ribGenDict['gpuCacheFileName']+'.zip'
            


        self.addRiAttribute(self)                         #呼叫 連結RIB Archive 跟 GPUCache
        
        
        pm.setAttr('%s'%gpuCacheShapeName +'.cacheFileName','%s'%gpuFullName)
        pm.setAttr('%s'%ribArchiveShapeName +'.filename','%s'%ribFullName)
        
        self.gpuCacheAddAttribute(self)
        
        print "run connectGpuRib Function Completed"
#---------------------------------------------------連結GPU RIB Cache End-------------------------------------------------------






#---------------------------------------------------給予 Attribute End--------------------------------------------------------



    def addRiAttribute(self,data): 
        
        print "run addRiAttribute Function "

        setStartFrame = self.ribGenDict['startFrameValue']
        setEndFrame = self.ribGenDict['endFrameValue']

        expressionCmd_001 ="expression -s "+"\""+'%s'%self.ribArchiveShape +".startframe = "+'%s'%setStartFrame +"\""     #set StartFrame Mel Cmd
        expressionCmd_002 ="expression -s "+"\""+'%s'%self.ribArchiveShape +".endframe = "+'%s'%setEndFrame +"\""     #set StartFrame Mel Cmd    
        expressionCmd_003 ="expression -s "+"\""+'%s'%self.ribArchiveShape +".frame = "+"frame" +"\""     #set StartFrame Mel Cmd          
        expressionCmd_004 ="expression -s "+"\""+'%s'%self.ribTransform +".translateX = "+'%s'%self.gpuTransform +".translateX"+"\""   #set StartFrame Mel Cmd   
        expressionCmd_005 ="expression -s "+"\""+'%s'%self.ribTransform +".translateY = "+'%s'%self.gpuTransform +".translateY"+"\""   #set StartFrame Mel Cmd                 
        expressionCmd_006 ="expression -s "+"\""+'%s'%self.ribTransform +".translateZ = "+'%s'%self.gpuTransform +".translateZ"+"\""   #set StartFrame Mel Cmd                 
        expressionCmd_007 ="expression -s "+"\""+'%s'%self.ribTransform +".rotateX = "+'%s'%self.gpuTransform +".rotateX"+"\""   #set StartFrame Mel Cmd                 
        expressionCmd_008 ="expression -s "+"\""+'%s'%self.ribTransform +".rotateY = "+'%s'%self.gpuTransform +".rotateY"+"\""   #set StartFrame Mel Cmd                 
        expressionCmd_009 ="expression -s "+"\""+'%s'%self.ribTransform +".rotateZ = "+'%s'%self.gpuTransform +".rotateZ"+"\""   #set StartFrame Mel Cmd                 
        expressionCmd_010 ="expression -s "+"\""+'%s'%self.ribTransform +".scaleX = "+'%s'%self.gpuTransform +".scaleX"+"\""   #set StartFrame Mel Cmd                 
        expressionCmd_011 ="expression -s "+"\""+'%s'%self.ribTransform +".scaleY = "+'%s'%self.gpuTransform +".scaleY"+"\""   #set StartFrame Mel Cmd                 
        expressionCmd_012 ="expression -s "+"\""+'%s'%self.ribTransform +".scaleZ = "+'%s'%self.gpuTransform +".scaleZ"+"\""   #set StartFrame Mel Cmd                 

        if self.ribGenDict['currentFrameCheck'] == '0': 
            
            self.melCmd001 = pm.mel.eval(expressionCmd_001)    #run mel command
            self.melCmd002 = pm.mel.eval(expressionCmd_002)
            self.melCmd003 = pm.mel.eval(expressionCmd_003)
        else:
            pass
            
        self.melCmd004 = pm.mel.eval(expressionCmd_004)
        self.melCmd005 = pm.mel.eval(expressionCmd_005)
        self.melCmd006 = pm.mel.eval(expressionCmd_006)
        self.melCmd007 = pm.mel.eval(expressionCmd_007)
        self.melCmd008 = pm.mel.eval(expressionCmd_008)
        self.melCmd009 = pm.mel.eval(expressionCmd_009)
        self.melCmd010 = pm.mel.eval(expressionCmd_010)
        self.melCmd011 = pm.mel.eval(expressionCmd_011)
        self.melCmd012 = pm.mel.eval(expressionCmd_012)

        
        print "run addRiAttribute Function Completed"
#---------------------------------------------------給予 Attribute End--------------------------------------------------------
  
  
  
  
  
  
#---------------------------------------------------給予 GPUCache Attribute 測試 begin--------------------------------------------------------  
  
  
    def gpuCacheAddAttribute(self,data):
       # self.gpuCacheShape = gpuCacheShapeName
       # self.ribArchiveShape = ribArchiveShapeName

        print "run gpuCacheAddAttribute Function "
        
        
        RiAttributeDict = {'cmd01':['CamVisCmd','rman__riattr__visibility_camera'],
                           'cmd02':['IndirectVisCmd','rman__riattr__visibility_indirect'],
                           'cmd03':['TransmissionVisCmd','rman__riattr__visibility_transmission'],
                           'cmd05':['MatteObjCmd','rman__riattr___MatteObject'],              
                           'cmd10':['IdentifierObjCmd','rman__riattr__identifier_objectid'],
                           'cmd11':['TraceDiffMaxCmd','rman__riattr__trace_maxdiffusedepth'],
                           'cmd12':['TraceSpecMaxCmd','rman__riattr__trace_maxspeculardepth'],
                           'cmd14':['LPEGrpCmd','rman__riattr__identifier_lpegroup'],                           
                           'cmd15':['PreShapeMel','rman__torattr___preShapeScript'],
                           'cmd13':['ShadingGrpCmd','rman__torattr___customShadingGroup'],}
                        #   'cmd06':['MatteID0Cmd','rman__riattr__user_MatteID0'],
                       #    'cmd07':['MatteID1Cmd','rman__riattr__user_MatteID1'] ,
                            #'cmd08':['MatteID2Cmd','rman__riattr__user_MatteID2'],
                            #'cmd09':['MatteID3Cmd','rman__riattr__user_MatteID3'],
                            #'cmd16':['SubdivFaceIntCmd','rman__torattr___subdivFacevaryingInterp'],
                            #'cmd17':['SubdivSchemeCmd','rman__torattr___subdivScheme']}



      #  for i in sorted(RiAttributeDict):       
      #      RiAttr = RiAttributeDict[i][1]
      #      addGPUAttrMelCmdA = "rmanAddAttr "+"%s "%self.gpuCacheShape + "%s "%RiAttr + "\"\""       #add GPUCacheShape RiAttribute command
      #      pm.mel.eval("%s"%addGPUAttrMelCmdA)                                                       #add GPUCacheShape RiAttribute mel
      #      addRibAttrMelCmdA = "rmanAddAttr "+"%s "%self.ribArchiveShape + "%s "%RiAttr + "\"\""     #add RibArchiveShape RiAttribute command
     #       pm.mel.eval("%s"%addRibAttrMelCmdA)                                                       #add RibArchiveShape RiAttribute mel   
          #  pm.connectAttr('%s'%self.gpuCacheShape +"." + '%s'%RiAttr , '%s'%self.ribArchiveShape + "." + "%s"%RiAttr)   
            

    #    pm.setAttr('%s'%self.gpuCacheShape+"."+"rman__riattr___MatteObject",0)
        #pm.addAttr( 'cubeGrp_GpuCacheShape1',longName='Custom Shadin Group', attributeType='string' )
        
        
        
        
        
       
        
        print "run gpuCacheAddAttribute Function Completed"
  
  
  
  
  
#---------------------------------------------------給予 GPUCache Attribute 測試 begin--------------------------------------------------------  
  
  
  

  
  
  
#---------------------------------------------------批次更改檔名 Start-----------------------------------------------------------   
  
    def batchRename(self,singleGrp):   
        print "run batchRename Function "
        path = self.ribGenDict['cacheForder']   
        #print os.listdir(path)
        for filename in os.listdir(path):
            if filename[-3:] == "rib" :
                if filename[-4] == "." :
                    if filename[-7] == "." :
                        newName = os.path.join(path,filename[0:-6]+'rib')
                        os.rename(os.path.join(path, filename), os.path.join(path, newName)) 
                        print os.path.join(path,filename) 
                    else:
                        print "nothing rename"
                        print "run batchRename Function Completed"
                        pass

                else:
                    pass
            
            else:
                pass
                
        print "run batchRename Function Completed"

#---------------------------------------------------批次更改檔名 End-----------------------------------------------------------   








#---------------------------------------------------查詢bbbox  start-------------------------------------------------------   


    def bBoxFind(self,singleGrp):
        print " run bBoxFind Function "
        unitNow = pm.currentUnit( query=True, linear=True )
        pm.currentUnit( linear='cm' )
        startFrame = float(self.ribGenDict['startFrameValue'])
        
        if self.ribGenDict['currentFrameCheck'] == "1":
            endFrame = startFrame
        else:
            
            endFrame = float(self.ribGenDict['endFrameValue'])
        stepFrame = 1
        path = self.ribGenDict['cacheForder']
        currentUser = getpass.getuser()
        prmanVersion = pm.mel.eval("rman getversion rfm")
        self.ribGenDict['currentFrameCheck']

#f.dumps(data)

        jsonRibTitle={ "Format" : "RIB Manifest",  #ribArchive 擋頭資料建立
        "Start-Frame" : int(startFrame),
        "End-Frame" : int(endFrame),
        "Created-By": prmanVersion ,
        "For" : currentUser}
        


        j = int(startFrame)

        dtRibDict = {}    
        dictOrder =[] 
        jsObjTitle = json.dumps(jsonRibTitle,sort_keys=0,indent=4)[:-2] +",\n"      #ribArchive 擋頭資料存入json buffer
        jsonName = path +'/'+ "RIBManifest.json"
        f = open(jsonName , 'w')   
        f.write(jsObjTitle)              #ribArchive 擋頭資料寫入json  
        
        addLineDriveFiles = "    "+"\""+"Driver-Files"+"\""+" : {"+" "  #ribArchive 擋頭資料,addLine,存入json buffer
        f.write(addLineDriveFiles)      #ribArchive 擋頭資料,addLine 寫入json
        while j <= endFrame:
            pm.currentTime(j,e=True)  # 跳至下一格
            
          #  print self.singleGrp
            bbSize = pm.xform(self.singleGrp,bb=True,q=True)  # 獲得bbBox資訊
                       
            self.bbMinX = '%.6f'%(bbSize[0])
            self.bbMinY = '%.6f'%(bbSize[1])
            self.bbMinZ = '%.6f'%(bbSize[2])
            self.bbMaxX = '%.6f'%(bbSize[3])
            self.bbMaxY = '%.6f'%(bbSize[4])
            self.bbMaxZ = '%.6f'%(bbSize[5])
            
            self.bBoxValue = self.bbMinX +" "+ self.bbMaxX+ " "+ self.bbMinY +" "+ self.bbMaxY +" "+ self.bbMinZ +" "+ self.bbMaxZ
            currentRibFrame = str("%04d"%j)
            #ribFileName = path+'/' + self.ribGenDict['gpuCacheFileName']+'.' +currentRibFrame +'.zip'
            if self.ribGenDict['currentFrameCheck'] == "1":
                ribFileName = "renderman/ribarchives/"+ self.ribGenDict['gpuCacheFileName'] +'.rib'
            else:
                ribFileName = "renderman/ribarchives/"+ self.ribGenDict['gpuCacheFileName'] +'.' +currentRibFrame +'.rib'


           # ribFileName = self.ribGenDict['ribArchiveFileName']
            jsonRibFrame={                                     #ribArchive each frame 資料建立
                       str(j):{"RIB-File" : ribFileName,
                        "Bounding-Box" : self.bBoxValue}
                       }
            jsObjFrame = json.dumps(jsonRibFrame,sort_keys=0,indent=8)[1:-2] +","   # ribArchive each frame 資料存入json buffer
           # dictOrder.append(str(j))
            f.write(jsObjFrame)              # ribArchive each frame 資料寫入json   
            #print self.bBoxValue
            j = j + stepFrame  
           # print  pm.currentTime(q=True)

            #開啟json檔案，定義檔名，模式為寫入

        
        endLine = "\n    }\n}"
        f.write(endLine) 
        f.close()                                               
    
        pm.currentUnit( linear= unitNow )

        print " run bBoxFind Function Completed "


#---------------------------------------------------查詢bbbox  End----------------------------------------------------------   




#---------------------------------------------------將rib archive打包成zip檔案 start-----------------------------------------------------------   


    def zipRibFiles(self,singleGrp):
        print "run zipRibFiles Function "
        path = self.ribGenDict['cacheForder']
        zName = path+'/' + self.ribGenDict['gpuCacheFileName'] +'.zip'
        #z = zipfile.ZipFile(zName, 'w')
       # print path
      #  print zName
        z = zipfile.ZipFile(zName, 'w',compression = zipfile.ZIP_DEFLATED)




        for fileName in os.listdir(path):
            
            if fileName[-3:] == "rib":
                fileDir = path +'/'+fileName
                relative_path =  "renderman/ribarchives/"+fileName
                z.write(fileDir,relative_path)
              #  removeFile = path + fileName
                os.remove(os.path.join(path, fileName))
                
                
                
                
        ribJsonFile = path + "/RIBManifest.json"
        z.write(ribJsonFile,"RIBManifest.json")
        z.close()
        os.remove(os.path.join(path, "RIBManifest.json"))
       # print self.bBoxValue
        
        print "run zipRibFiles Function Completed "






#----------------------------------------------------將rib archive打包成zip檔案 End----------------------------------------------------------   



















#---------------------------------------------------開啟cache資料夾 start-----------------------------------------------------------   

    def openFolder(self):
        startingDir = cmds.workspace(q=True, rd=True)+'data/cache'
        currentProjWin =''
        for cha in startingDir:
            if cha =="/":
                currentProjWin += '\\'
            else:    
                currentProjWin += cha 
        openCmd = "explorer "+'%s'%currentProjWin
        subprocess.call(openCmd)

#---------------------------------------------------開啟cache資料夾 End-----------------------------------------------------------   
    

#------------------------------------------------run mel command 開始執行Mel 指令 start------------------------------
    def runMelCommandCreateCache(self,singleGrp):
        print "run runMelCommandCreateCache Function"
        
        
        pm.mel.eval('%s'%self.ribGenDict['finalRibExportCmd'])
        if self.checkBox_E01.isChecked() == 1:
            self.gpuCacheMeshReduce(self)
            pm.mel.eval('%s'%self.ribGenDict['finalGpuExportCmd']) 
            print self.originalObjList       
            print self.tempObjList   
            for i in self.originalObjList:
             
                pm.showHidden(i)
            
            for j in self.tempObjList:
                print j
                pm.delete(j)
            
            
        elif self.checkBox_E01.isChecked() == 0:
            pm.mel.eval('%s'%self.ribGenDict['finalGpuExportCmd']) 
            
     #   for i in self.originalObjList:
             
         #   pm.showHidden(i)
            
     #   for j in self.tempObjList:
            
         #   pm.delete(j)
            
          

            
        print "run runMelCommandCreateCache Function completed"
#------------------------------------------------run mel command 開始執行Mel 指令 end------------------------------
 

#---------------------------------------------------開啟cache 資料夾 button Start-----------------------------------------------------------   
            
    def modtoolButton_01(self):

        self.openFolder()
  
       

#---------------------------------------------------開啟cache 資料夾 button Start-----------------------------------------------------------   
    

    def gpuCacheMeshReduce(self,singleGrp):
        print "run gpuCacheMeshReduce Function"
    
           
       # self.singleGrp = pm.ls(sl=True)
#       print self.meshReduceValue
       # self.selectGrpList(self)
        self.selectedShape(self)
        print self.selectedGeoShape
        print self.meshReduceValue
        self.originalObjList=[]            #original modeling shape list
        self.tempObjList=[]                #temp obj list,diupicate form original model,and prepare to reduce

        for selectShape in  self.selectedGeoShape:
            tempGeoName = "temp"+selectShape
            pm.duplicate(selectShape, n =tempGeoName )          # duplicate Oiginal polyMesh
            #print tempGeoName
            selectShapeToTransform = pm.listRelatives(selectShape,p=True)
            self.originalObjList.append(selectShapeToTransform)
            #selectTempShapeToTransform =  pm.listRelatives(tempGeoName,p=True)
            self.tempObjList.append(tempGeoName)
            pm.polyReduce(tempGeoName,khe= 0,ver=1,p=self.meshReduceValue,kqw=0,rpo=True)  #reduce polyMesh, khe,keep Hard Edge, p,peresent ,kqw,keep Quad,rpo, replace original
            
            pm.hide(selectShapeToTransform)
        print self.tempObjList
        print self.originalObjList

        print "run gpuCacheMeshReduce Function Completed"




    
#------------------------------------------Generate RIB Archive Button Def Begin---------------------------------------
    def modpushButton_01(self):   
        self.reStoreValue(self)
        if self.ribGenDict['subdivschemeCheck'] == '1':
            self.selectGrpList(self)                        #  所選取的Group def
          #  print self.selectedTGrpList
            for self.singleGrp in self.selectedTGrpList:    #個別選取Group                              
            #   print self.singleGrp
                pm.select(self.singleGrp)
                self.createSelectFolder(self)               # define create folder def 創建所選取的grp folder
                self.cacheFileName(self)                    # Define RIB Archive and GPUCache File Name   def
                self.getRibExportCmd(self)                  # export command def
              #  
              #  print self.ribGenDict['finalRibExportCmd']
              #  print self.ribGenDict['finalGpuExportCmd']
                self.selectedShape(self)
                
               # print self.selectedGeoShape
                
                for self.singleShape in self.selectedGeoShape:                    #由group中選取shape def
                #    print self.singleShape
                    self.addSubD(self)                                  #對所選取的模型做 SUBD
                self.gpuCacheMeshReduce (self)                    # 執行Mel Command

                self.runMelCommandCreateCache(self)
                print self.singleGrp
                for self.singleShape in self.selectedGeoShape:                    #由group中選取shape def
                 #   print self.singleShape
                    self.delSubD(self)                                  #對所選取的模型做 刪除 SUBD               
                self.connectGpuRib(self)
                if self.ribGenDict['shutterTiming'] == "frameCenter":
                    self.batchRename(self)

                self.bBoxFind(self)

                self.zipRibFiles(self)
                
                
         #   self.delSubD(self)                                  #對所選取的模型做刪除 SUBD
        elif self.ribGenDict['subdivschemeCheck'] == '0':
            self.selectGrpList(self)                        #  所選取的Group def
            for self.singleGrp in self.selectedTGrpList:    #個別選取Group                              
                pm.select(self.singleGrp)
                self.createSelectFolder(self)               # define create folder def 創建所選取的grp folder
                self.cacheFileName(self)                    # Define RIB Archive and GPUCache File Name   def
                self.getRibExportCmd(self)                  # export command def
          #      print self.ribGenDict['finalRibExportCmd']
          #      print self.ribGenDict['finalGpuExportCmd']
                self.selectedShape(self)   
                self.runMelCommandCreateCache(self)             
                self.connectGpuRib(self)
                if self.ribGenDict['shutterTiming'] == "frameCenter":
                    self.batchRename(self)
 
                self.bBoxFind(self)

                self.zipRibFiles(self)





#------------------------------------------Generate RIB Archive Button Def End---------------------------------------

                                                        #





    def modpushButton_02(self):
        print "aaaaa"
        self.selectGrpList(self)  
        for self.singleGrp in self.selectedTGrpList:    #個別選取Group                              

            pm.select(self.singleGrp)
            self.createSelectFolder(self)               # define create folder def 創建所選取的grp folder
            self.cacheFileName(self)                    # Define RIB Archive and GPUCache File Name   def
            self.getRibExportCmd(self)                  # export command def
            self.shaveRibExport(self)   
            self.connectGpuRib(self)

        
#----------------------------------------------------button 3------------------------------------------------- 
    def modpushButton_03(self):
        print '--------------------check start -------------------------'
        print 'currentFrameCheck' + self.ribGenDict['currentFrameCheck']
        print 'startEndFrameCheck' + self.ribGenDict['startEndFrameCheck']
        print "current Frame" + self.ribGenDict['currentFrameValue']
        print "start Fram" + self.ribGenDict['startFrameValue']
        print "end Frame" + self.ribGenDict['endFrameValue']
        print 'motionBlurCheck' + self.ribGenDict['motionBlurCheck']
        print 'cameraBlurCheck' + self.ribGenDict['cameraBlurCheck'] 
        print "shutter Angle" + self.ribGenDict['shutterAngleValue']
        print "shutter Opening on" + self.ribGenDict['shutterOpeningOn']
        print "shutter Opening off" + self.ribGenDict['shutterOpeningOff']
        print "motion sample" + self.ribGenDict['motionSamples']
        print 'delayedReadArchiveCheck' + self.ribGenDict['delayedReadArchiveCheck']
        print 'ReadArchiveCheck' + self.ribGenDict['ReadArchiveCheck']
        print 'shutterTiming' + self.ribGenDict['shutterTiming']
        print 'motionBlurType' + self.ribGenDict['motionBlurType']
        print 'rayTracedMotionBlurCheck' + self.ribGenDict['rayTracedMotionBlurCheck']
        print 'subdivschemeCheck' + self.ribGenDict['subdivschemeCheck']
        print 'assignLamertShader' + self.ribGenDict['assignLamertShader']

        print '--------------------------------end------------------------------------'

        



#def main():
def rib_genMain():
    global ui
    app = QtGui.QApplication.instance()
    if app == None: app = QApplication(sys.argv)
    try:
        ui.close()
        ui.deleteLater()
    except: pass
    ui = mod_MainWindow()
    ui.show()
 
#if __name__ == '__main__':
#    main() 