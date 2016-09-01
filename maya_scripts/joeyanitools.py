# -*- coding: utf-8 -*-
import maya.cmds as cmds
import pymel.core as pm
from maya import OpenMaya
import os as os
import shutil as shutil
import sys
from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(291, 611)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_10 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.line_8 = QtGui.QFrame(self.tab_4)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_10.addWidget(self.line_8, 5, 0, 1, 2)
        self.line_4 = QtGui.QFrame(self.tab_4)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_10.addWidget(self.line_4, 1, 0, 1, 2)
        self.line = QtGui.QFrame(self.tab_4)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_10.addWidget(self.line, 3, 0, 1, 2)
        self.LegMatchLayout = QtGui.QWidget(self.tab_4)
        self.LegMatchLayout.setObjectName("LegMatchLayout")
        self.gridLayout_11 = QtGui.QGridLayout(self.LegMatchLayout)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_4 = QtGui.QLabel(self.LegMatchLayout)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_11.addWidget(self.label_4, 1, 0, 1, 2)
        self.groupBox_3 = QtGui.QGroupBox(self.LegMatchLayout)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.R_LegTo_IK_Button = QtGui.QPushButton(self.groupBox_3)
        self.R_LegTo_IK_Button.setObjectName("R_LegTo_IK_Button")
        self.gridLayout_5.addWidget(self.R_LegTo_IK_Button, 0, 0, 1, 1)
        self.R_LegTo_FK_Button = QtGui.QPushButton(self.groupBox_3)
        self.R_LegTo_FK_Button.setObjectName("R_LegTo_FK_Button")
        self.gridLayout_5.addWidget(self.R_LegTo_FK_Button, 1, 0, 1, 1)
        self.gridLayout_11.addWidget(self.groupBox_3, 2, 0, 2, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.LegMatchLayout)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.L_LegTo_IK_Button = QtGui.QPushButton(self.groupBox_4)
        self.L_LegTo_IK_Button.setObjectName("L_LegTo_IK_Button")
        self.gridLayout_6.addWidget(self.L_LegTo_IK_Button, 0, 0, 1, 1)
        self.L_LegTo_FK_Button = QtGui.QPushButton(self.groupBox_4)
        self.L_LegTo_FK_Button.setObjectName("L_LegTo_FK_Button")
        self.gridLayout_6.addWidget(self.L_LegTo_FK_Button, 1, 0, 1, 1)
        self.gridLayout_11.addWidget(self.groupBox_4, 2, 1, 2, 1)
        self.gridLayout_10.addWidget(self.LegMatchLayout, 4, 0, 1, 2)
        self.ArmMatchLayout = QtGui.QWidget(self.tab_4)
        self.ArmMatchLayout.setObjectName("ArmMatchLayout")
        self.gridLayout_9 = QtGui.QGridLayout(self.ArmMatchLayout)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox = QtGui.QGroupBox(self.ArmMatchLayout)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.R_ArmTo_IK_Button = QtGui.QPushButton(self.groupBox)
        self.R_ArmTo_IK_Button.setObjectName("R_ArmTo_IK_Button")
        self.gridLayout_3.addWidget(self.R_ArmTo_IK_Button, 0, 1, 1, 1)
        self.R_ArmTo_FK_Button = QtGui.QPushButton(self.groupBox)
        self.R_ArmTo_FK_Button.setObjectName("R_ArmTo_FK_Button")
        self.gridLayout_3.addWidget(self.R_ArmTo_FK_Button, 1, 1, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox, 1, 0, 2, 1)
        self.label_3 = QtGui.QLabel(self.ArmMatchLayout)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_9.addWidget(self.label_3, 0, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(self.ArmMatchLayout)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.L_ArmTo_FK_Button = QtGui.QPushButton(self.groupBox_2)
        self.L_ArmTo_FK_Button.setObjectName("L_ArmTo_FK_Button")
        self.gridLayout_4.addWidget(self.L_ArmTo_FK_Button, 1, 1, 1, 1)
        self.L_ArmTo_IK_Button = QtGui.QPushButton(self.groupBox_2)
        self.L_ArmTo_IK_Button.setObjectName("L_ArmTo_IK_Button")
        self.gridLayout_4.addWidget(self.L_ArmTo_IK_Button, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_2, 1, 1, 2, 1)
        self.gridLayout_10.addWidget(self.ArmMatchLayout, 2, 0, 1, 2)
        self.ReferenceNameLayout = QtGui.QWidget(self.tab_4)
        self.ReferenceNameLayout.setObjectName("ReferenceNameLayout")
        self.gridLayout_12 = QtGui.QGridLayout(self.ReferenceNameLayout)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.setNameButton = QtGui.QPushButton(self.ReferenceNameLayout)
        self.setNameButton.setObjectName("setNameButton")
        self.gridLayout_12.addWidget(self.setNameButton, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.ReferenceNameLayout)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_12.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.ReferenceNameLayout, 0, 0, 1, 2)
        self.gridWidget = QtGui.QWidget(self.tab_4)
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout_15 = QtGui.QGridLayout(self.gridWidget)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.label_16 = QtGui.QLabel(self.gridWidget)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_15.addWidget(self.label_16, 0, 0, 1, 1)
        self.BindPose_pushButton = QtGui.QPushButton(self.gridWidget)
        self.BindPose_pushButton.setObjectName("BindPose_pushButton")
        self.gridLayout_15.addWidget(self.BindPose_pushButton, 1, 0, 1, 1)
        self.gridLayout_10.addWidget(self.gridWidget, 6, 0, 1, 2)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridWidget1 = QtGui.QWidget(self.tab)
        self.gridWidget1.setObjectName("gridWidget1")
        self.gridLayout_7 = QtGui.QGridLayout(self.gridWidget1)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.line_5 = QtGui.QFrame(self.gridWidget1)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_7.addWidget(self.line_5, 7, 0, 1, 3)
        self.line_3 = QtGui.QFrame(self.gridWidget1)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_7.addWidget(self.line_3, 5, 0, 1, 3)
        self.line_2 = QtGui.QFrame(self.gridWidget1)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_7.addWidget(self.line_2, 3, 0, 1, 3)
        self.FBXExport_pushButton = QtGui.QPushButton(self.gridWidget1)
        self.FBXExport_pushButton.setObjectName("FBXExport_pushButton")
        self.gridLayout_7.addWidget(self.FBXExport_pushButton, 8, 0, 1, 3)
        self.gridWidget_2 = QtGui.QWidget(self.gridWidget1)
        self.gridWidget_2.setObjectName("gridWidget_2")
        self.gridLayout_14 = QtGui.QGridLayout(self.gridWidget_2)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_8 = QtGui.QLabel(self.gridWidget_2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_14.addWidget(self.label_8, 1, 2, 1, 1)
        self.film_name_01_lineEdit = QtGui.QLineEdit(self.gridWidget_2)
        self.film_name_01_lineEdit.setObjectName("film_name_01_lineEdit")
        self.gridLayout_14.addWidget(self.film_name_01_lineEdit, 2, 4, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridWidget_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_14.addWidget(self.label_7, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.gridWidget_2)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_14.addWidget(self.label_9, 1, 4, 1, 1)
        self.label_10 = QtGui.QLabel(self.gridWidget_2)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_14.addWidget(self.label_10, 2, 0, 1, 1)
        self.film_name_03_lineEdit = QtGui.QLineEdit(self.gridWidget_2)
        self.film_name_03_lineEdit.setObjectName("film_name_03_lineEdit")
        self.gridLayout_14.addWidget(self.film_name_03_lineEdit, 4, 4, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridWidget_2)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_14.addWidget(self.label_6, 0, 0, 1, 5)
        self.film_name_04_lineEdit = QtGui.QLineEdit(self.gridWidget_2)
        self.film_name_04_lineEdit.setObjectName("film_name_04_lineEdit")
        self.gridLayout_14.addWidget(self.film_name_04_lineEdit, 5, 4, 1, 1)
        self.film_name_02_lineEdit = QtGui.QLineEdit(self.gridWidget_2)
        self.film_name_02_lineEdit.setObjectName("film_name_02_lineEdit")
        self.gridLayout_14.addWidget(self.film_name_02_lineEdit, 3, 4, 1, 1)
        self.film_name_05_lineEdit = QtGui.QLineEdit(self.gridWidget_2)
        self.film_name_05_lineEdit.setObjectName("film_name_05_lineEdit")
        self.gridLayout_14.addWidget(self.film_name_05_lineEdit, 6, 4, 1, 1)
        self.label_11 = QtGui.QLabel(self.gridWidget_2)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_14.addWidget(self.label_11, 3, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.gridWidget_2)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_14.addWidget(self.label_12, 4, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.gridWidget_2)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_14.addWidget(self.label_13, 5, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.gridWidget_2)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_14.addWidget(self.label_14, 6, 0, 1, 1)
        self.end_film_03_spinBox = QtGui.QLineEdit(self.gridWidget_2)
        self.end_film_03_spinBox.setObjectName("end_film_03_spinBox")
        self.gridLayout_14.addWidget(self.end_film_03_spinBox, 4, 2, 1, 1)
        self.start_film_01_spinBox = QtGui.QLineEdit(self.gridWidget_2)
        self.start_film_01_spinBox.setObjectName("start_film_01_spinBox")
        self.gridLayout_14.addWidget(self.start_film_01_spinBox, 2, 1, 1, 1)
        self.end_film_01_spinBox = QtGui.QLineEdit(self.gridWidget_2)
        self.end_film_01_spinBox.setObjectName("end_film_01_spinBox")
        self.gridLayout_14.addWidget(self.end_film_01_spinBox, 2, 2, 1, 1)
        self.start_film_04_spinBox = QtGui.QLineEdit(self.gridWidget_2)
        self.start_film_04_spinBox.setObjectName("start_film_04_spinBox")
        self.gridLayout_14.addWidget(self.start_film_04_spinBox, 5, 1, 1, 1)
        self.end_film_04_spinBox = QtGui.QLineEdit(self.gridWidget_2)
        self.end_film_04_spinBox.setObjectName("end_film_04_spinBox")
        self.gridLayout_14.addWidget(self.end_film_04_spinBox, 5, 2, 1, 1)
        self.start_film_05_spinBox = QtGui.QLineEdit(self.gridWidget_2)
        self.start_film_05_spinBox.setObjectName("start_film_05_spinBox")
        self.gridLayout_14.addWidget(self.start_film_05_spinBox, 6, 1, 1, 1)
        self.start_film_03_spinBox = QtGui.QLineEdit(self.gridWidget_2)
        self.start_film_03_spinBox.setObjectName("start_film_03_spinBox")
        self.gridLayout_14.addWidget(self.start_film_03_spinBox, 4, 1, 1, 1)
        self.end_film_02_spinBox = QtGui.QLineEdit(self.gridWidget_2)
        self.end_film_02_spinBox.setObjectName("end_film_02_spinBox")
        self.gridLayout_14.addWidget(self.end_film_02_spinBox, 3, 2, 1, 1)
        self.start_film_02_spinBox = QtGui.QLineEdit(self.gridWidget_2)
        self.start_film_02_spinBox.setObjectName("start_film_02_spinBox")
        self.gridLayout_14.addWidget(self.start_film_02_spinBox, 3, 1, 1, 1)
        self.end_film_05_spinBox = QtGui.QLineEdit(self.gridWidget_2)
        self.end_film_05_spinBox.setObjectName("end_film_05_spinBox")
        self.gridLayout_14.addWidget(self.end_film_05_spinBox, 6, 2, 1, 1)
        self.line_7 = QtGui.QFrame(self.gridWidget_2)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_14.addWidget(self.line_7, 2, 3, 5, 1)
        self.gridLayout_7.addWidget(self.gridWidget_2, 6, 0, 1, 3)
        self.gridWidget2 = QtGui.QWidget(self.gridWidget1)
        self.gridWidget2.setObjectName("gridWidget2")
        self.gridLayout_13 = QtGui.QGridLayout(self.gridWidget2)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.bake_animation_checkBox = QtGui.QCheckBox(self.gridWidget2)
        self.bake_animation_checkBox.setChecked(True)
        self.bake_animation_checkBox.setObjectName("bake_animation_checkBox")
        self.gridLayout_13.addWidget(self.bake_animation_checkBox, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridWidget2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_13.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.gridWidget2, 4, 0, 1, 3)
        self.gridWidget3 = QtGui.QWidget(self.gridWidget1)
        self.gridWidget3.setObjectName("gridWidget3")
        self.gridLayout_2 = QtGui.QGridLayout(self.gridWidget3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.path_lineEdit = QtGui.QLineEdit(self.gridWidget3)
        self.path_lineEdit.setObjectName("path_lineEdit")
        self.gridLayout_2.addWidget(self.path_lineEdit, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridWidget3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.gridWidget3, 2, 0, 1, 3)
        self.gridWidget4 = QtGui.QWidget(self.gridWidget1)
        self.gridWidget4.setObjectName("gridWidget4")
        self.gridLayout_8 = QtGui.QGridLayout(self.gridWidget4)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.Custom_radioButton = QtGui.QRadioButton(self.gridWidget4)
        self.Custom_radioButton.setObjectName("Custom_radioButton")
        self.gridLayout_8.addWidget(self.Custom_radioButton, 0, 2, 1, 1)
        self.label_15 = QtGui.QLabel(self.gridWidget4)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_8.addWidget(self.label_15, 0, 1, 1, 1)
        self.AutoRig_radioButton = QtGui.QRadioButton(self.gridWidget4)
        self.AutoRig_radioButton.setChecked(True)
        self.AutoRig_radioButton.setObjectName("AutoRig_radioButton")
        self.gridLayout_8.addWidget(self.AutoRig_radioButton, 0, 0, 1, 1)
        self.FBXsetName_pushButton = QtGui.QPushButton(self.gridWidget4)
        self.FBXsetName_pushButton.setObjectName("FBXsetName_pushButton")
        self.gridLayout_8.addWidget(self.FBXsetName_pushButton, 1, 0, 1, 3)
        self.gridLayout_7.addWidget(self.gridWidget4, 0, 0, 1, 3)
        self.line_6 = QtGui.QFrame(self.gridWidget1)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_7.addWidget(self.line_6, 1, 0, 1, 3)
        self.horizontalLayout.addWidget(self.gridWidget1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.setNameButton)
        MainWindow.setTabOrder(self.setNameButton, self.R_ArmTo_IK_Button)
        MainWindow.setTabOrder(self.R_ArmTo_IK_Button, self.L_ArmTo_IK_Button)
        MainWindow.setTabOrder(self.L_ArmTo_IK_Button, self.R_ArmTo_FK_Button)
        MainWindow.setTabOrder(self.R_ArmTo_FK_Button, self.L_ArmTo_FK_Button)
        MainWindow.setTabOrder(self.L_ArmTo_FK_Button, self.R_LegTo_IK_Button)
        MainWindow.setTabOrder(self.R_LegTo_IK_Button, self.L_LegTo_IK_Button)
        MainWindow.setTabOrder(self.L_LegTo_IK_Button, self.R_LegTo_FK_Button)
        MainWindow.setTabOrder(self.R_LegTo_FK_Button, self.L_LegTo_FK_Button)
        MainWindow.setTabOrder(self.L_LegTo_FK_Button, self.FBXsetName_pushButton)
        MainWindow.setTabOrder(self.FBXsetName_pushButton, self.path_lineEdit)
        MainWindow.setTabOrder(self.path_lineEdit, self.bake_animation_checkBox)
        MainWindow.setTabOrder(self.bake_animation_checkBox, self.start_film_01_spinBox)
        MainWindow.setTabOrder(self.start_film_01_spinBox, self.end_film_01_spinBox)
        MainWindow.setTabOrder(self.end_film_01_spinBox, self.film_name_01_lineEdit)
        MainWindow.setTabOrder(self.film_name_01_lineEdit, self.start_film_02_spinBox)
        MainWindow.setTabOrder(self.start_film_02_spinBox, self.end_film_02_spinBox)
        MainWindow.setTabOrder(self.end_film_02_spinBox, self.film_name_02_lineEdit)
        MainWindow.setTabOrder(self.film_name_02_lineEdit, self.start_film_03_spinBox)
        MainWindow.setTabOrder(self.start_film_03_spinBox, self.end_film_03_spinBox)
        MainWindow.setTabOrder(self.end_film_03_spinBox, self.film_name_03_lineEdit)
        MainWindow.setTabOrder(self.film_name_03_lineEdit, self.start_film_04_spinBox)
        MainWindow.setTabOrder(self.start_film_04_spinBox, self.end_film_04_spinBox)
        MainWindow.setTabOrder(self.end_film_04_spinBox, self.film_name_04_lineEdit)
        MainWindow.setTabOrder(self.film_name_04_lineEdit, self.start_film_05_spinBox)
        MainWindow.setTabOrder(self.start_film_05_spinBox, self.end_film_05_spinBox)
        MainWindow.setTabOrder(self.end_film_05_spinBox, self.film_name_05_lineEdit)
        MainWindow.setTabOrder(self.film_name_05_lineEdit, self.FBXExport_pushButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Leg</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "R_Leg", None, QtGui.QApplication.UnicodeUTF8))
        self.R_LegTo_IK_Button.setText(QtGui.QApplication.translate("MainWindow", "IK", None, QtGui.QApplication.UnicodeUTF8))
        self.R_LegTo_FK_Button.setText(QtGui.QApplication.translate("MainWindow", "FK", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "L_Leg", None, QtGui.QApplication.UnicodeUTF8))
        self.L_LegTo_IK_Button.setText(QtGui.QApplication.translate("MainWindow", "IK", None, QtGui.QApplication.UnicodeUTF8))
        self.L_LegTo_FK_Button.setText(QtGui.QApplication.translate("MainWindow", "FK", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "R_Arm", None, QtGui.QApplication.UnicodeUTF8))
        self.R_ArmTo_IK_Button.setText(QtGui.QApplication.translate("MainWindow", "IK", None, QtGui.QApplication.UnicodeUTF8))
        self.R_ArmTo_FK_Button.setText(QtGui.QApplication.translate("MainWindow", "FK", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Arm</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "L_Arm", None, QtGui.QApplication.UnicodeUTF8))
        self.L_ArmTo_FK_Button.setText(QtGui.QApplication.translate("MainWindow", "FK", None, QtGui.QApplication.UnicodeUTF8))
        self.L_ArmTo_IK_Button.setText(QtGui.QApplication.translate("MainWindow", "IK", None, QtGui.QApplication.UnicodeUTF8))
        self.setNameButton.setText(QtGui.QApplication.translate("MainWindow", "setName", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">NAME</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Bind Pose</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.BindPose_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Go To Bind Pose", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "IKFK_Match", None, QtGui.QApplication.UnicodeUTF8))
        self.FBXExport_pushButton.setText(QtGui.QApplication.translate("MainWindow", "FBXExport", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">END</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">START</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">NAME</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">1</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Film</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">2</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">3</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">4</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">5</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.bake_animation_checkBox.setText(QtGui.QApplication.translate("MainWindow", "Bake Animation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">OPTIONS</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">PATH</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.Custom_radioButton.setText(QtGui.QApplication.translate("MainWindow", "Custom", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">NAME</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.AutoRig_radioButton.setText(QtGui.QApplication.translate("MainWindow", "AutoRig", None, QtGui.QApplication.UnicodeUTF8))
        self.FBXsetName_pushButton.setText(QtGui.QApplication.translate("MainWindow", "setName", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "FBX_Export", None, QtGui.QApplication.UnicodeUTF8))

class mod_MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent= QtGui.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        self.setupUi(self)
       
        self.setNameButton.clicked.connect(lambda: self.setName())

        self.L_ArmTo_FK_Button.clicked.connect(lambda: self.L_ArmTo_FK())
        self.L_ArmTo_IK_Button.clicked.connect(lambda: self.L_ArmTo_IK())
        self.R_ArmTo_FK_Button.clicked.connect(lambda: self.R_ArmTo_FK())
        self.R_ArmTo_IK_Button.clicked.connect(lambda: self.R_ArmTo_IK())

        self.L_LegTo_FK_Button.clicked.connect(lambda: self.L_LegTo_FK())
        self.L_LegTo_IK_Button.clicked.connect(lambda: self.L_LegTo_IK())
        self.R_LegTo_FK_Button.clicked.connect(lambda: self.R_LegTo_FK())
        self.R_LegTo_IK_Button.clicked.connect(lambda: self.R_LegTo_IK())

        self.BindPose_pushButton.clicked.connect(lambda: self.GO_TO_Bind_Pose())

        self.FBXsetName_pushButton.clicked.connect(lambda: self.setFBXName())
        self.FBXExport_pushButton.clicked.connect(lambda: self.Tools(function = 'FBXExport'))
        
    def setName(self):
        try:
            tgt = pm.ls(sl=1)[0]
            RfName = []
            Ref = []
            Space = []
            try:
                for i in range(len(str(tgt))):
                    if tgt[i] ==':':
                        Ref.append(i)
                names = tgt[Ref[-1]+1:]
                for j in range(len(str(names))):
                    if names[j] =='_':
                        Space.append(j)
                RfName = tgt[:Ref[-1]+1]+names[:Space[0]+1]
            except:
                for i in range(len(str(tgt))):
                    if tgt[i] =='_':
                        RfName.append(i)
                RfName = tgt[:RfName[0]+1]

            ################ArmGrp################
            self.L_ArmFKList = [pm.PyNode(RfName+'FK_L_upperArm_ctrl'),pm.PyNode(RfName+'FK_L_lowerArm_ctrl'),\
                pm.PyNode(RfName+'FK_L_hand_ctrl'),pm.PyNode(RfName+'FK_L_hand_sub_ctrl')]
            self.L_ArmFKJtList = [pm.PyNode(RfName+'FK_L_hand')]

            self.L_ArmIKList = [pm.PyNode(RfName+'IK_L_upperArm_pv_ctrl'),pm.PyNode(RfName+'IK_L_hand_ctrl'),\
                pm.PyNode(RfName+'IK_L_hand_Rot_ctrl_1'),pm.PyNode(RfName+'IK_L_hand_Rot_ctrl_2'),pm.PyNode(RfName+'IK_L_upperArm_ctrl')]
            self.L_ArmIkJtList = [pm.PyNode(RfName+'IK_L_upperArm'),pm.PyNode(RfName+'IK_L_lowerArm'),\
                pm.PyNode(RfName+'IK_L_hand')]

            self.R_ArmFKList = [pm.PyNode(RfName+'FK_R_upperArm_ctrl'),pm.PyNode(RfName+'FK_R_lowerArm_ctrl'),\
                pm.PyNode(RfName+'FK_R_hand_ctrl'),pm.PyNode(RfName+'FK_R_hand_sub_ctrl')]
            self.R_ArmFKJtList = [pm.PyNode(RfName+'FK_R_hand')]

            self.R_ArmIKList = [pm.PyNode(RfName+'IK_R_upperArm_pv_ctrl'),pm.PyNode(RfName+'IK_R_hand_ctrl'),\
                pm.PyNode(RfName+'IK_R_hand_Rot_ctrl_1'),pm.PyNode(RfName+'IK_R_hand_Rot_ctrl_2'),pm.PyNode(RfName+'IK_R_upperArm_ctrl')]
            self.R_ArmIkJtList = [pm.PyNode(RfName+'IK_R_upperArm'),pm.PyNode(RfName+'IK_R_lowerArm'),\
                pm.PyNode(RfName+'IK_R_hand')]

            self.ShoulderList = [pm.PyNode(RfName+'L_shoulder_ctrl'),pm.PyNode(RfName+'R_shoulder_ctrl')]

            self.L_ArmMisc = pm.PyNode(RfName+'L_arm_ikfkSwitch')
            self.R_ArmMisc = pm.PyNode(RfName+'R_arm_ikfkSwitch')
            ################LegGrp################
            self.L_LegFKList = [pm.PyNode(RfName+'FK_L_upperLeg_ctrl'),pm.PyNode(RfName+'FK_L_lowerLeg_ctrl'),\
                pm.PyNode(RfName+'FK_L_foot_ctrl'),pm.PyNode(RfName+'FK_L_toe_ctrl')]
            self.L_LegIKList = [pm.PyNode(RfName+'IK_L_upperLeg_pv_ctrl'),pm.PyNode(RfName+'IK_L_foot_ctrl'),\
                pm.PyNode(RfName+'IK_L_upperLeg_ctrl')]
            self.L_LegIkJtList = [pm.PyNode(RfName+'IK_L_upperLeg'),pm.PyNode(RfName+'IK_L_lowerLeg'),\
                pm.PyNode(RfName+'IK_L_foot')]

            self.R_LegFKList = [pm.PyNode(RfName+'FK_R_upperLeg_ctrl'),pm.PyNode(RfName+'FK_R_lowerLeg_ctrl'),\
                pm.PyNode(RfName+'FK_R_foot_ctrl'),pm.PyNode(RfName+'FK_R_toe_ctrl')]
            self.R_LegIKList = [pm.PyNode(RfName+'IK_R_upperLeg_pv_ctrl'),pm.PyNode(RfName+'IK_R_foot_ctrl'),\
                pm.PyNode(RfName+'IK_R_upperLeg_ctrl')]
            self.R_LegIkJtList = [pm.PyNode(RfName+'IK_R_upperLeg'),pm.PyNode(RfName+'IK_R_lowerLeg'),\
                pm.PyNode(RfName+'IK_R_foot')]

            self.L_LegMisc = pm.PyNode(RfName+'L_leg_ikfkSwitch')
            self.R_LegMisc = pm.PyNode(RfName+'R_leg_ikfkSwitch')
            ################BodyGrp################
            self.SpinalList = [pm.PyNode(RfName+'pelvis_ctrl'),pm.PyNode(RfName+'chest_ctrl'),pm.PyNode(RfName+'hip_ctrl'),\
                pm.PyNode(RfName+'neck_ctrl'),pm.PyNode(RfName+'head_ctrl'),pm.PyNode(RfName+'eye_ctrl'),\
                pm.PyNode(RfName+'L_eye_ctrl'),pm.PyNode(RfName+'R_eye_ctrl'),pm.PyNode(RfName+'mouth_end_ctrl')]
            try:
                self.BendBodyList = [pm.PyNode(RfName+'upPelvis_ctrl'),pm.PyNode(RfName+'downPelvis_ctrl'),\
                    pm.PyNode(RfName+'spline1_ctrl'),pm.PyNode(RfName+'spline2_ctrl')]
            except:
                self.BendBodyList = []
            ################Other################
            self.Other = [pm.PyNode(RfName+'Constrain'),pm.PyNode(RfName+'Mov'),pm.PyNode(RfName+'Turn_buttom'),\
                pm.PyNode(RfName+'Turn_middle'),pm.PyNode(RfName+'Turn_top'),pm.PyNode(RfName+'scale')]
            sys.stdout.write(u'紀錄完畢')
        except:
            sys.stdout.write(u'請選擇目標')

    def GO_TO_Bind_Pose(self):
        pm.undoInfo(ock=True)
        ctrlList = self.L_ArmFKList,self.L_ArmIKList,self.R_ArmFKList,self.R_ArmIKList,\
            self.ShoulderList,self.L_LegFKList,self.L_LegIKList,self.R_LegFKList,\
            self.R_LegIKList,self.SpinalList,self.Other,self.BendBodyList
        attrs = ['tx','ty','tz','rx','ry','rz']
        scale = ['sx','sy','sz']
        for lists in ctrlList:
            for ctrl in lists:
                for x in attrs:
                    if ctrl.attr(x).get(k=1):
                        ctrl.setAttr(x,0)
                    else:
                        pass
        for y in scale:
            self.Other[5].setAttr(y,1)
        pm.undoInfo(cck=True)

    def setFBXName(self):
        try:
            if self.AutoRig_radioButton.isChecked():
                tgt = pm.ls(sl=1)[0]
                RfName = []
                try:
                    for i in range(len(str(tgt))):
                        if tgt[i] ==':':
                            RfName.append(i)
                    RfName = tgt[:RfName[-1]+1]
                except:
                    for i in range(len(str(tgt))):
                        if tgt[i] =='_':
                            RfName.append(i)
                    RfName = tgt[:RfName[0]+1]
                self.unityExport = pm.PyNode(RfName+'Shape'),pm.PyNode(RfName+'Skin_Joint_grp')
            elif self.Custom_radioButton.isChecked():
                self.unityExport = pm.ls(sl=1)
            sys.stdout.write(u'紀錄完畢')
        except:
            sys.stdout.write(u'請選擇目標')

    def Tools(self,function=''):
        pm.undoInfo(ock=True)
        if function == 'copyTime':
            self.select = pm.ls(sl=1)
            self.startTime = self.startTimeEdit.text()
            self.endTime = self.endTimeEdit.text()
            self.copyTime(self.select[0],self.select[1],self.startTime,self.endTime)
        if function == 'MirrorKey':
            self.select = pm.ls(sl=1)
            self.mirrorAttrList = []
            if self.TranslateX_checkBox.checkState():
                self.mirrorAttrList+=['translateX']
            if self.TranslateY_checkBox.checkState():
                self.mirrorAttrList+=['translateY']
            if self.TranslateZ_checkBox.checkState():
                self.mirrorAttrList+=['translateZ']

            if self.RotateX_checkBox.checkState():
                self.mirrorAttrList+=['rotateX']
            if self.RotateY_checkBox.checkState():
                self.mirrorAttrList+=['rotateY']
            if self.RotateZ_checkBox.checkState():
                self.mirrorAttrList+=['rotateZ']

            if self.ScaleX_checkBox.checkState():
                self.mirrorAttrList+=['scaleX']
            if self.ScaleY_checkBox.checkState():
                self.mirrorAttrList+=['scaleY']
            if self.ScaleZ_checkBox.checkState():
                self.mirrorAttrList+=['scaleZ']
            else:
                pass
            self.MirrorKey(self.select[0],mirrorAttr=self.mirrorAttrList,valuePivot=0)
        if function == 'FBXExport':
            if self.bake_animation_checkBox.isChecked():
                self.bake_animation = True
            else:
                self.bake_animation = False
            if self.path_lineEdit.text():
                path = self.path_lineEdit.text()
            else:
                path = False
            Export_01 = self.start_film_01_spinBox.text(),self.end_film_01_spinBox.text(),self.film_name_01_lineEdit.text()
            Export_02 = self.start_film_02_spinBox.text(),self.end_film_02_spinBox.text(),self.film_name_02_lineEdit.text()
            Export_03 = self.start_film_03_spinBox.text(),self.end_film_03_spinBox.text(),self.film_name_03_lineEdit.text()
            Export_04 = self.start_film_04_spinBox.text(),self.end_film_04_spinBox.text(),self.film_name_04_lineEdit.text()
            Export_05 = self.start_film_05_spinBox.text(),self.end_film_05_spinBox.text(),self.film_name_05_lineEdit.text()
            ALL_Export = [Export_01,Export_02,Export_03,Export_04,Export_05]
            for exports in ALL_Export:
                if exports[0] == '' or exports[1] == '' or exports[2] == '':
                    pass
                else:
                    self.unityExportTool(path,int(exports[0]),int(exports[1]),str(exports[2]))
        pm.undoInfo(cck=True)

    def copyTime(self,copyObj,pasteObj,startTime,endTime):
        time = pm.currentTime()
        pm.copyKey(copyObj,t=(startTime,endTime))
        pm.pasteKey(pasteObj,t=time)
        pm.currentTime(time+endTime-startTime)

    def MirrorKey(self,obj,mirrorAttr='',valuePivot=0):
        for i in mirrorAttr:
            pm.scaleKey(obj,at=i,vs=-1,vp=valuePivot)

    def parentTgt(self,tgt1,tgt2,skipTran=[],skipRot=[]):
        con = pm.parentConstraint(tgt1,tgt2,st=skipTran,sr=skipRot)
        try:
            pm.setKeyframe(tgt2,at='translate')
        except:
            pass
        try:
            pm.setKeyframe(tgt2,at='rotateY')
        except:
            pass
        try:
            pm.setKeyframe(tgt2,at='rotateX')
        except:
            pass
        try:
            pm.setKeyframe(tgt2,at='rotateZ')
        except:
            pass
        pm.delete(con)

    def setKet(self,ikList,fkList,misc,to='',leg=0):
        time = pm.currentTime()
        for i in ikList:
            pm.setKeyframe(i,at='translate')
        pm.setKeyframe(fkList[0],at='rotate')
        if leg == 0:
            pm.setKeyframe(fkList[1],at='rotateY')
        else:
            pm.setKeyframe(fkList[1],at='rotateX')
            pm.setKeyframe(fkList[2],at='rotate')
        pm.currentTime(time-1)
        pm.setKeyframe(misc,at='ikfk')
        pm.currentTime(time)
        if to == 'ik':
            pm.setAttr(misc+'.ikfk',1)
        elif to == 'fk':
            pm.setAttr(misc+'.ikfk',0)
        else:
            sys.stdout.write(u'無法切換IKFK')
        pm.setKeyframe(misc,at='ikfk')

    def L_ArmTo_FK(self):
        pm.undoInfo(ock=True)
        if self.L_ArmMisc.ikfk.get() == 1:
            self.parentTgt(self.L_ArmIkJtList[0],self.L_ArmFKList[0],skipTran=['x','y','z'],skipRot=[])
            self.parentTgt(self.L_ArmIkJtList[1],self.L_ArmFKList[1],skipTran=['x','y','z'],skipRot=['x','z'])
            self.parentTgt(self.L_ArmIkJtList[2],self.L_ArmFKList[2],skipTran=['x','y','z'],skipRot=[])
            self.parentTgt(self.L_ArmIkJtList[2],self.L_ArmFKList[3],skipTran=['x','y','z'],skipRot=[])
            self.setKet(self.L_ArmIkJtList,self.L_ArmFKList,self.L_ArmMisc,to='fk')
            sys.stdout.write(u'轉換完成')
        else:
            pass
        pm.undoInfo(cck=True)

    def L_ArmTo_IK(self):
        pm.undoInfo(ock=True)
        if self.L_ArmMisc.ikfk.get() == 0:
            self.parentTgt(self.L_ArmFKList[1],self.L_ArmIKList[0],skipTran=[],skipRot=['x','y','z'])
            self.parentTgt(self.L_ArmFKList[2],self.L_ArmIKList[1],skipTran=[],skipRot=['x','y','z'])
            self.parentTgt(self.L_ArmFKJtList[0],self.L_ArmIKList[2],skipTran=['x','y','z'],skipRot=[])
            self.parentTgt(self.L_ArmFKJtList[0],self.L_ArmIKList[3],skipTran=['x','y','z'],skipRot=[])
            self.setKet(self.L_ArmIkJtList,self.L_ArmFKList,self.L_ArmMisc,to='ik')
            sys.stdout.write(u'轉換完成')
        else:
            pass
        pm.undoInfo(cck=True)

    def R_ArmTo_FK(self):
        pm.undoInfo(ock=True)
        if self.R_ArmMisc.ikfk.get() == 1:
            self.parentTgt(self.R_ArmIkJtList[0],self.R_ArmFKList[0],skipTran=['x','y','z'],skipRot=[])
            self.parentTgt(self.R_ArmIkJtList[1],self.R_ArmFKList[1],skipTran=['x','y','z'],skipRot=['x','z'])
            self.parentTgt(self.R_ArmIkJtList[2],self.R_ArmFKList[2],skipTran=['x','y','z'],skipRot=[])
            self.parentTgt(self.R_ArmIkJtList[2],self.R_ArmFKList[3],skipTran=['x','y','z'],skipRot=[])
            self.setKet(self.R_ArmIkJtList,self.R_ArmFKList,self.R_ArmMisc,to='fk')
            sys.stdout.write(u'轉換完成')
        else:
            pass
        pm.undoInfo(cck=True)

    def R_ArmTo_IK(self):
        pm.undoInfo(ock=True)
        if self.R_ArmMisc.ikfk.get() == 0:
            self.parentTgt(self.R_ArmFKList[1],self.R_ArmIKList[0],skipTran=[],skipRot=['x','y','z'])
            self.parentTgt(self.R_ArmFKList[2],self.R_ArmIKList[1],skipTran=[],skipRot=['x','y','z'])
            self.parentTgt(self.R_ArmFKJtList[0],self.R_ArmIKList[2],skipTran=['x','y','z'],skipRot=[])
            self.parentTgt(self.R_ArmFKJtList[0],self.R_ArmIKList[3],skipTran=['x','y','z'],skipRot=[])
            self.setKet(self.R_ArmIkJtList,self.R_ArmFKList,self.R_ArmMisc,to='ik')
            sys.stdout.write(u'轉換完成')
        else:
            pass
        pm.undoInfo(cck=True)

    def L_LegTo_FK(self):
        pm.undoInfo(ock=True)
        if self.L_LegMisc.ikfk.get() == 1:
            self.parentTgt(self.L_LegIkJtList[0],self.L_LegFKList[0],skipTran=['x','y','z'],skipRot=[])
            self.parentTgt(self.L_LegIkJtList[1],self.L_LegFKList[1],skipTran=['x','y','z'],skipRot=[])
            self.parentTgt(self.L_LegIkJtList[2],self.L_LegFKList[2],skipTran=['x','y','z'],skipRot=[])
            self.setKet(self.L_LegIkJtList,self.L_LegFKList,self.L_LegMisc,to='fk',leg=1)
            sys.stdout.write(u'轉換完成')
        else:
            pass
        pm.undoInfo(cck=True)

    def L_LegTo_IK(self):
        pm.undoInfo(ock=True)
        if self.L_LegMisc.ikfk.get() == 0:
            self.parentTgt(self.L_LegFKList[1],self.L_LegIKList[0],skipTran=[],skipRot=['x','y','z'])
            self.parentTgt(self.L_LegFKList[2],self.L_LegIKList[1],skipTran=[],skipRot=['x','y','z'])
            self.setKet(self.L_LegIkJtList,self.L_LegFKList,self.L_LegMisc,to='ik',leg=1)
            sys.stdout.write(u'轉換完成')
        else:
            pass
        pm.undoInfo(cck=True)

    def R_LegTo_FK(self):
        pm.undoInfo(ock=True)
        if self.R_LegMisc.ikfk.get() == 1:
            self.parentTgt(self.R_LegIkJtList[0],self.R_LegFKList[0],skipTran=['x','y','z'],skipRot=[])
            self.parentTgt(self.R_LegIkJtList[1],self.R_LegFKList[1],skipTran=['x','y','z'],skipRot=[])
            self.parentTgt(self.R_LegIkJtList[2],self.R_LegFKList[2],skipTran=['x','y','z'],skipRot=[])
            self.setKet(self.R_LegIkJtList,self.R_LegFKList,self.R_LegMisc,to='fk',leg=1)
            sys.stdout.write(u'轉換完成')
        else:
            pass
        pm.undoInfo(cck=True)

    def R_LegTo_IK(self):
        pm.undoInfo(ock=True)
        if self.R_LegMisc.ikfk.get() == 0:
            self.parentTgt(self.R_LegFKList[1],self.R_LegIKList[0],skipTran=[],skipRot=['x','y','z'])
            self.parentTgt(self.R_LegFKList[2],self.R_LegIKList[1],skipTran=[],skipRot=['x','y','z'])
            self.setKet(self.R_LegIkJtList,self.R_LegFKList,self.R_LegMisc,to='ik',leg=1)
            sys.stdout.write(u'轉換完成')
        else:
            pass
        pm.undoInfo(cck=True)

    def copyTime(self,tgt,start,end):
        time = pm.currentTime()
        pm.copyKey(tgt,t=(start,end))
        pm.pasteKey(tgt,t=time,c=1)
        pm.currentTime(time+end-start)

    def OffsetTools(self):
        pm.undoInfo(ock=True)
        try:
            moveMD = pm.shadingNode('multiplyDivide',al=1,n='moveMD_1')
            moveCD = pm.shadingNode('condition',al=1,n='moveCD_1')
            cmds.connectAttr(self.spine+'.translateZ',moveCD+'.firstTerm')
            cmds.connectAttr(self.spine+'.translateZ',moveCD+'.colorIfTrueB')
            moveCD.setAttr('operation',2)
            moveCD.setAttr('colorIfFalseB',0)
            cmds.connectAttr(moveCD+'.outColorB',moveMD+'.input1Z')
            moveMD.setAttr('input2Z',-1)
            cmds.connectAttr(moveCD+'.outColorB',self.offset+'.translateZ')
            for j in self.minus:
                cmds.connectAttr(moveMD+'.outputZ',j+'.translateZ')
            sys.stdout.write(u'反轉完成')
        except:
            sys.stdout.write(u'沒有對應名稱或Offset有SetKey')
        pm.undoInfo(cck=True)

    def UndoSetTools(self):
        pm.undoInfo(ock=True)
        try:
            node1 = self.offset.translateZ.inputs()
            node2 = self.minus[0].translateZ.inputs()
            pm.delete(node1,node2)
            sys.stdout.write(u'已刪除Offset')
            self.offset.setAttr('translateZ',0)
        except:
            sys.stdout.write(u'沒有對應名稱或Offset有SetKey')
            pass
        pm.undoInfo(cck=True)

    def unityExportTool(self,path,startFrame,endFrame,name):
        pm.undoInfo(ock=True)
        try:
            pm.select(self.unityExport)
            #endFrame = pm.playbackOptions(q=True,max=1)
            #startFrame = pm.playbackOptions(q=True,min=-1)
            pm.mel.FBXResetExport()
            pm.mel.FBXExportBakeComplexAnimation(v=self.bake_animation)
            pm.mel.FBXExportBakeComplexStart(v=startFrame)
            pm.mel.FBXExportBakeComplexEnd(v=endFrame)
            pm.mel.FBXExportBakeComplexStep(v=1)
            pm.mel.FBXExportCameras(v=False)
            pm.mel.FBXExportLights(v=False)
            pm.mel.FBXExportEmbeddedTextures(v=False)
            pm.mel.FBXExportInAscii(v=False)
            pm.mel.FBXExportGenerateLog(v=True)
            if path == False:
                path = pm.mel.file(q=True,sceneName=True)
                n = []
                for i in range(len(path)):
                    if path[i] == '/':
                        n.append(i)
                pm.mel.FBXExport(s=True, f=path[:n[-1]+1]+name+'.fbx')
            else:
                pm.mel.FBXExport(s=True, f=path+'\\'+name+'.fbx')
            sys.stdout.write(u'已匯出FBX')
        except:
        	sys.stdout.write(u'找不到目標')
        pm.undoInfo(cck=True)

def joeyanitoolsMain():
    global ui
    app = QtGui.QApplication.instance()
    if app == None: app = QApplication(sys.argv)
    try:
        ui.close()
        ui.deleteLater()
    except: pass
    ui = mod_MainWindow()
    ui.show()

 
# if __name__ == '__main__':
#     main() 
