# -*- coding: utf-8 -*-
import maya.cmds as cmds
import pymel.core as pm
import maya.mel as mel
from maya import OpenMaya
from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 928)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget_3 = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_14 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.verticalWidget = QtGui.QWidget(self.tab_2)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridWidget = QtGui.QWidget(self.verticalWidget)
        self.gridWidget.setObjectName("gridWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.gridWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtGui.QLabel(self.gridWidget)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.CharacterName_Edit = QtGui.QLineEdit(self.gridWidget)
        self.CharacterName_Edit.setObjectName("CharacterName_Edit")
        self.verticalLayout_2.addWidget(self.CharacterName_Edit)
        self.line_5 = QtGui.QFrame(self.gridWidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        self.tabWidget_2 = QtGui.QTabWidget(self.gridWidget)
        self.tabWidget_2.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridWidget_7 = QtGui.QWidget(self.tab_7)
        self.gridWidget_7.setObjectName("gridWidget_7")
        self.gridLayout_22 = QtGui.QGridLayout(self.gridWidget_7)
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.label_28 = QtGui.QLabel(self.gridWidget_7)
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_22.addWidget(self.label_28, 0, 1, 1, 1)
        self.chrSizeSet_Button = QtGui.QPushButton(self.gridWidget_7)
        self.chrSizeSet_Button.setObjectName("chrSizeSet_Button")
        self.gridLayout_22.addWidget(self.chrSizeSet_Button, 1, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.gridWidget_7)
        self.gridWidget_3 = QtGui.QWidget(self.tab_7)
        self.gridWidget_3.setObjectName("gridWidget_3")
        self.gridLayout_3 = QtGui.QGridLayout(self.gridWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.creatRigLocs_Button = QtGui.QPushButton(self.gridWidget_3)
        self.creatRigLocs_Button.setObjectName("creatRigLocs_Button")
        self.gridLayout_3.addWidget(self.creatRigLocs_Button, 5, 0, 1, 2)
        self.groupBox_7 = QtGui.QGroupBox(self.gridWidget_3)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Breast_checkBox = QtGui.QCheckBox(self.groupBox_7)
        self.Breast_checkBox.setChecked(False)
        self.Breast_checkBox.setObjectName("Breast_checkBox")
        self.verticalLayout_4.addWidget(self.Breast_checkBox)
        self.But_checkBox = QtGui.QCheckBox(self.groupBox_7)
        self.But_checkBox.setChecked(False)
        self.But_checkBox.setObjectName("But_checkBox")
        self.verticalLayout_4.addWidget(self.But_checkBox)
        self.gridLayout_3.addWidget(self.groupBox_7, 1, 1, 1, 1)
        self.groupBox_6 = QtGui.QGroupBox(self.gridWidget_3)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.thumb_comboBox = QtGui.QComboBox(self.groupBox_6)
        self.thumb_comboBox.setObjectName("thumb_comboBox")
        self.thumb_comboBox.addItem("")
        self.thumb_comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.thumb_comboBox)
        self.index_comboBox = QtGui.QComboBox(self.groupBox_6)
        self.index_comboBox.setObjectName("index_comboBox")
        self.index_comboBox.addItem("")
        self.index_comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.index_comboBox)
        self.middle_comboBox = QtGui.QComboBox(self.groupBox_6)
        self.middle_comboBox.setObjectName("middle_comboBox")
        self.middle_comboBox.addItem("")
        self.middle_comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.middle_comboBox)
        self.ring_comboBox = QtGui.QComboBox(self.groupBox_6)
        self.ring_comboBox.setObjectName("ring_comboBox")
        self.ring_comboBox.addItem("")
        self.ring_comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.ring_comboBox)
        self.little_comboBox = QtGui.QComboBox(self.groupBox_6)
        self.little_comboBox.setObjectName("little_comboBox")
        self.little_comboBox.addItem("")
        self.little_comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.little_comboBox)
        self.gridLayout_3.addWidget(self.groupBox_6, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridWidget_3)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.gridWidget_3)
        self.gridWidget_4 = QtGui.QWidget(self.tab_7)
        self.gridWidget_4.setObjectName("gridWidget_4")
        self.gridLayout_5 = QtGui.QGridLayout(self.gridWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox = QtGui.QGroupBox(self.gridWidget_4)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.ArmBend_checkBox = QtGui.QCheckBox(self.groupBox)
        self.ArmBend_checkBox.setCheckable(True)
        self.ArmBend_checkBox.setChecked(False)
        self.ArmBend_checkBox.setAutoRepeat(False)
        self.ArmBend_checkBox.setObjectName("ArmBend_checkBox")
        self.gridLayout_7.addWidget(self.ArmBend_checkBox, 0, 0, 1, 1)
        self.ArmNumber_comboBox = QtGui.QComboBox(self.groupBox)
        self.ArmNumber_comboBox.setObjectName("ArmNumber_comboBox")
        self.ArmNumber_comboBox.addItem("")
        self.ArmNumber_comboBox.addItem("")
        self.ArmNumber_comboBox.addItem("")
        self.ArmNumber_comboBox.addItem("")
        self.ArmNumber_comboBox.addItem("")
        self.ArmNumber_comboBox.addItem("")
        self.gridLayout_7.addWidget(self.ArmNumber_comboBox, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 2, 1, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.gridWidget_4)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_11 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.spinalNumber_comboBox = QtGui.QComboBox(self.groupBox_3)
        self.spinalNumber_comboBox.setObjectName("spinalNumber_comboBox")
        self.spinalNumber_comboBox.addItem("")
        self.spinalNumber_comboBox.addItem("")
        self.spinalNumber_comboBox.addItem("")
        self.gridLayout_11.addWidget(self.spinalNumber_comboBox, 0, 1, 1, 1)
        self.SpinalBend_checkBox = QtGui.QCheckBox(self.groupBox_3)
        self.SpinalBend_checkBox.setChecked(False)
        self.SpinalBend_checkBox.setObjectName("SpinalBend_checkBox")
        self.gridLayout_11.addWidget(self.SpinalBend_checkBox, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_3, 4, 2, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.gridWidget_4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.LegBend_checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.LegBend_checkBox.setChecked(False)
        self.LegBend_checkBox.setObjectName("LegBend_checkBox")
        self.gridLayout_6.addWidget(self.LegBend_checkBox, 0, 0, 1, 1)
        self.LegNumber_comboBox = QtGui.QComboBox(self.groupBox_2)
        self.LegNumber_comboBox.setObjectName("LegNumber_comboBox")
        self.LegNumber_comboBox.addItem("")
        self.LegNumber_comboBox.addItem("")
        self.LegNumber_comboBox.addItem("")
        self.LegNumber_comboBox.addItem("")
        self.LegNumber_comboBox.addItem("")
        self.LegNumber_comboBox.addItem("")
        self.gridLayout_6.addWidget(self.LegNumber_comboBox, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 2, 2, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.gridWidget_4)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_10 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.neckNumber_comboBox = QtGui.QComboBox(self.groupBox_4)
        self.neckNumber_comboBox.setObjectName("neckNumber_comboBox")
        self.neckNumber_comboBox.addItem("")
        self.neckNumber_comboBox.addItem("")
        self.neckNumber_comboBox.addItem("")
        self.neckNumber_comboBox.addItem("")
        self.neckNumber_comboBox.addItem("")
        self.gridLayout_10.addWidget(self.neckNumber_comboBox, 0, 1, 1, 1)
        self.NeckBend_checkBox = QtGui.QCheckBox(self.groupBox_4)
        self.NeckBend_checkBox.setChecked(False)
        self.NeckBend_checkBox.setObjectName("NeckBend_checkBox")
        self.gridLayout_10.addWidget(self.NeckBend_checkBox, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_4, 4, 1, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(self.gridWidget_4)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.SkinJoint_checkBox = QtGui.QCheckBox(self.groupBox_5)
        self.SkinJoint_checkBox.setChecked(True)
        self.SkinJoint_checkBox.setTristate(False)
        self.SkinJoint_checkBox.setObjectName("SkinJoint_checkBox")
        self.gridLayout_9.addWidget(self.SkinJoint_checkBox, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_5, 6, 1, 1, 2)
        self.Animation_radioButton = QtGui.QRadioButton(self.gridWidget_4)
        self.Animation_radioButton.setChecked(True)
        self.Animation_radioButton.setObjectName("Animation_radioButton")
        self.gridLayout_5.addWidget(self.Animation_radioButton, 8, 1, 1, 1)
        self.Unity_radioButton = QtGui.QRadioButton(self.gridWidget_4)
        self.Unity_radioButton.setObjectName("Unity_radioButton")
        self.gridLayout_5.addWidget(self.Unity_radioButton, 8, 2, 1, 1)
        self.startRigging_Button = QtGui.QPushButton(self.gridWidget_4)
        self.startRigging_Button.setEnabled(True)
        self.startRigging_Button.setObjectName("startRigging_Button")
        self.gridLayout_5.addWidget(self.startRigging_Button, 10, 1, 1, 2)
        self.label_4 = QtGui.QLabel(self.gridWidget_4)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 1, 1, 1, 2)
        self.verticalLayout_5.addWidget(self.gridWidget_4)
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridWidget_8 = QtGui.QWidget(self.tab_8)
        self.gridWidget_8.setObjectName("gridWidget_8")
        self.gridLayout_23 = QtGui.QGridLayout(self.gridWidget_8)
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.Q_chrSizeSet_Button = QtGui.QPushButton(self.gridWidget_8)
        self.Q_chrSizeSet_Button.setObjectName("Q_chrSizeSet_Button")
        self.gridLayout_23.addWidget(self.Q_chrSizeSet_Button, 2, 1, 1, 1)
        self.label_29 = QtGui.QLabel(self.gridWidget_8)
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_23.addWidget(self.label_29, 0, 1, 1, 1)
        self.groupBox_8 = QtGui.QGroupBox(self.gridWidget_8)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Q_HorseType_radioButton = QtGui.QRadioButton(self.groupBox_8)
        self.Q_HorseType_radioButton.setObjectName("Q_HorseType_radioButton")
        self.verticalLayout_6.addWidget(self.Q_HorseType_radioButton)
        self.Q_DogCatType_radioButton = QtGui.QRadioButton(self.groupBox_8)
        self.Q_DogCatType_radioButton.setObjectName("Q_DogCatType_radioButton")
        self.verticalLayout_6.addWidget(self.Q_DogCatType_radioButton)
        self.gridLayout_23.addWidget(self.groupBox_8, 1, 1, 1, 1)
        self.verticalLayout_7.addWidget(self.gridWidget_8)
        self.gridWidget_5 = QtGui.QWidget(self.tab_8)
        self.gridWidget_5.setObjectName("gridWidget_5")
        self.gridLayout_20 = QtGui.QGridLayout(self.gridWidget_5)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.Q_creatRigLocs_Button = QtGui.QPushButton(self.gridWidget_5)
        self.Q_creatRigLocs_Button.setObjectName("Q_creatRigLocs_Button")
        self.gridLayout_20.addWidget(self.Q_creatRigLocs_Button, 5, 0, 1, 2)
        self.label_26 = QtGui.QLabel(self.gridWidget_5)
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout_20.addWidget(self.label_26, 0, 0, 1, 2)
        self.verticalLayout_7.addWidget(self.gridWidget_5)
        self.gridWidget_6 = QtGui.QWidget(self.tab_8)
        self.gridWidget_6.setObjectName("gridWidget_6")
        self.gridLayout_21 = QtGui.QGridLayout(self.gridWidget_6)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.groupBox_14 = QtGui.QGroupBox(self.gridWidget_6)
        self.groupBox_14.setObjectName("groupBox_14")
        self.gridLayout_26 = QtGui.QGridLayout(self.groupBox_14)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.Q_SkinJoint_checkBox = QtGui.QCheckBox(self.groupBox_14)
        self.Q_SkinJoint_checkBox.setChecked(True)
        self.Q_SkinJoint_checkBox.setTristate(False)
        self.Q_SkinJoint_checkBox.setObjectName("Q_SkinJoint_checkBox")
        self.gridLayout_26.addWidget(self.Q_SkinJoint_checkBox, 0, 0, 1, 1)
        self.gridLayout_21.addWidget(self.groupBox_14, 4, 1, 1, 2)
        self.Q_startRigging_Button = QtGui.QPushButton(self.gridWidget_6)
        self.Q_startRigging_Button.setEnabled(True)
        self.Q_startRigging_Button.setObjectName("Q_startRigging_Button")
        self.gridLayout_21.addWidget(self.Q_startRigging_Button, 7, 1, 1, 2)
        self.label_27 = QtGui.QLabel(self.gridWidget_6)
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_21.addWidget(self.label_27, 1, 1, 1, 2)
        self.verticalLayout_7.addWidget(self.gridWidget_6)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.tabWidget_2.addTab(self.tab_8, "")
        self.verticalLayout_2.addWidget(self.tabWidget_2)
        self.label_2 = QtGui.QLabel(self.gridWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.selectSkinJoints_pushButton = QtGui.QPushButton(self.gridWidget)
        self.selectSkinJoints_pushButton.setObjectName("selectSkinJoints_pushButton")
        self.verticalLayout_2.addWidget(self.selectSkinJoints_pushButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.gridWidget)
        self.gridLayout_14.addWidget(self.verticalWidget, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_13 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.verticalWidget1 = QtGui.QWidget(self.tab_3)
        self.verticalWidget1.setObjectName("verticalWidget1")
        self.gridLayout_15 = QtGui.QGridLayout(self.verticalWidget1)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.ChangeObjUV_pushButton = QtGui.QPushButton(self.verticalWidget1)
        self.ChangeObjUV_pushButton.setObjectName("ChangeObjUV_pushButton")
        self.gridLayout_15.addWidget(self.ChangeObjUV_pushButton, 30, 0, 1, 2)
        self.line_9 = QtGui.QFrame(self.verticalWidget1)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_15.addWidget(self.line_9, 29, 0, 1, 2)
        self.line_2 = QtGui.QFrame(self.verticalWidget1)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_15.addWidget(self.line_2, 13, 0, 1, 2)
        self.label_16 = QtGui.QLabel(self.verticalWidget1)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_15.addWidget(self.label_16, 26, 0, 1, 2)
        self.line_8 = QtGui.QFrame(self.verticalWidget1)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_15.addWidget(self.line_8, 27, 0, 1, 2)
        self.line_10 = QtGui.QFrame(self.verticalWidget1)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_15.addWidget(self.line_10, 35, 0, 1, 2)
        self.label_17 = QtGui.QLabel(self.verticalWidget1)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_15.addWidget(self.label_17, 32, 0, 1, 1)
        self.renameChildren_pushButton = QtGui.QPushButton(self.verticalWidget1)
        self.renameChildren_pushButton.setObjectName("renameChildren_pushButton")
        self.gridLayout_15.addWidget(self.renameChildren_pushButton, 28, 0, 1, 2)
        self.moveVerticesPower_horizontalSlider = QtGui.QSlider(self.verticalWidget1)
        self.moveVerticesPower_horizontalSlider.setMaximum(100)
        self.moveVerticesPower_horizontalSlider.setPageStep(1)
        self.moveVerticesPower_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.moveVerticesPower_horizontalSlider.setObjectName("moveVerticesPower_horizontalSlider")
        self.gridLayout_15.addWidget(self.moveVerticesPower_horizontalSlider, 32, 1, 1, 1)
        self.moveVerticesSET_pushButton = QtGui.QPushButton(self.verticalWidget1)
        self.moveVerticesSET_pushButton.setObjectName("moveVerticesSET_pushButton")
        self.gridLayout_15.addWidget(self.moveVerticesSET_pushButton, 33, 0, 1, 1)
        self.moveVertices_pushButton = QtGui.QPushButton(self.verticalWidget1)
        self.moveVertices_pushButton.setObjectName("moveVertices_pushButton")
        self.gridLayout_15.addWidget(self.moveVertices_pushButton, 33, 1, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.verticalWidget1)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_18 = QtGui.QLabel(self.tab_5)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_8.addWidget(self.label_18, 5, 0, 1, 1)
        self.ctrlType_comboBox = QtGui.QComboBox(self.tab_5)
        self.ctrlType_comboBox.setObjectName("ctrlType_comboBox")
        self.ctrlType_comboBox.addItem("")
        self.ctrlType_comboBox.addItem("")
        self.ctrlType_comboBox.addItem("")
        self.ctrlType_comboBox.addItem("")
        self.ctrlType_comboBox.addItem("")
        self.ctrlType_comboBox.addItem("")
        self.ctrlType_comboBox.addItem("")
        self.gridLayout_8.addWidget(self.ctrlType_comboBox, 5, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.tab_5)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_8.addWidget(self.label_14, 2, 0, 1, 2)
        self.line_6 = QtGui.QFrame(self.tab_5)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_8.addWidget(self.line_6, 1, 0, 1, 2)
        self.label_15 = QtGui.QLabel(self.tab_5)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_8.addWidget(self.label_15, 4, 0, 1, 2)
        self.label_13 = QtGui.QLabel(self.tab_5)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_8.addWidget(self.label_13, 3, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab_5)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 0, 0, 1, 2)
        self.ControllerSize_horizontalSlider = QtGui.QSlider(self.tab_5)
        self.ControllerSize_horizontalSlider.setMinimum(1)
        self.ControllerSize_horizontalSlider.setMaximum(50)
        self.ControllerSize_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ControllerSize_horizontalSlider.setObjectName("ControllerSize_horizontalSlider")
        self.gridLayout_8.addWidget(self.ControllerSize_horizontalSlider, 3, 1, 1, 1)
        self.setCtrl_pushButton = QtGui.QPushButton(self.tab_5)
        self.setCtrl_pushButton.setObjectName("setCtrl_pushButton")
        self.gridLayout_8.addWidget(self.setCtrl_pushButton, 6, 0, 1, 2)
        self.line_11 = QtGui.QFrame(self.tab_5)
        self.line_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_8.addWidget(self.line_11, 7, 0, 1, 2)
        self.CreateSubCtrl_pushButton = QtGui.QPushButton(self.tab_5)
        self.CreateSubCtrl_pushButton.setObjectName("CreateSubCtrl_pushButton")
        self.gridLayout_8.addWidget(self.CreateSubCtrl_pushButton, 8, 0, 1, 2)
        self.line_12 = QtGui.QFrame(self.tab_5)
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout_8.addWidget(self.line_12, 9, 0, 1, 2)
        self.CreatePathCtrl_pushButton = QtGui.QPushButton(self.tab_5)
        self.CreatePathCtrl_pushButton.setObjectName("CreatePathCtrl_pushButton")
        self.gridLayout_8.addWidget(self.CreatePathCtrl_pushButton, 10, 0, 1, 2)
        self.line_7 = QtGui.QFrame(self.tab_5)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_8.addWidget(self.line_7, 11, 0, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem2, 12, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.Blink_Z_checkBox = QtGui.QCheckBox(self.tab)
        self.Blink_Z_checkBox.setObjectName("Blink_Z_checkBox")
        self.gridLayout.addWidget(self.Blink_Z_checkBox, 12, 2, 1, 1)
        self.Blink_X_checkBox = QtGui.QCheckBox(self.tab)
        self.Blink_X_checkBox.setObjectName("Blink_X_checkBox")
        self.gridLayout.addWidget(self.Blink_X_checkBox, 12, 0, 1, 1)
        self.Blink_Y_checkBox = QtGui.QCheckBox(self.tab)
        self.Blink_Y_checkBox.setObjectName("Blink_Y_checkBox")
        self.gridLayout.addWidget(self.Blink_Y_checkBox, 12, 1, 1, 1)
        self.label_25 = QtGui.QLabel(self.tab)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 11, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 9, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 2)
        self.Vertex_PointConstraint_checkBox = QtGui.QCheckBox(self.tab)
        self.Vertex_PointConstraint_checkBox.setObjectName("Vertex_PointConstraint_checkBox")
        self.gridLayout.addWidget(self.Vertex_PointConstraint_checkBox, 2, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 3)
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)
        self.SET_Name_pushButton = QtGui.QPushButton(self.tab)
        self.SET_Name_pushButton.setObjectName("SET_Name_pushButton")
        self.gridLayout.addWidget(self.SET_Name_pushButton, 3, 0, 1, 3)
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 3)
        self.SET_UpVertex_pushButton = QtGui.QPushButton(self.tab)
        self.SET_UpVertex_pushButton.setObjectName("SET_UpVertex_pushButton")
        self.gridLayout.addWidget(self.SET_UpVertex_pushButton, 5, 0, 1, 3)
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 3)
        self.SET_DownVertex_pushButton = QtGui.QPushButton(self.tab)
        self.SET_DownVertex_pushButton.setObjectName("SET_DownVertex_pushButton")
        self.gridLayout.addWidget(self.SET_DownVertex_pushButton, 7, 0, 1, 3)
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 3)
        self.SET_Size_horizontalSlider = QtGui.QSlider(self.tab)
        self.SET_Size_horizontalSlider.setMinimum(1)
        self.SET_Size_horizontalSlider.setMaximum(100)
        self.SET_Size_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.SET_Size_horizontalSlider.setObjectName("SET_Size_horizontalSlider")
        self.gridLayout.addWidget(self.SET_Size_horizontalSlider, 9, 1, 1, 2)
        self.SET_Match_pushButton = QtGui.QPushButton(self.tab)
        self.SET_Match_pushButton.setObjectName("SET_Match_pushButton")
        self.gridLayout.addWidget(self.SET_Match_pushButton, 10, 0, 1, 3)
        self.Blink_and_Zoom_pushButton = QtGui.QPushButton(self.tab)
        self.Blink_and_Zoom_pushButton.setObjectName("Blink_and_Zoom_pushButton")
        self.gridLayout.addWidget(self.Blink_and_Zoom_pushButton, 13, 0, 1, 3)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 14, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_12 = QtGui.QGridLayout(self.tab_6)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.DynamicsRigging_horizontalSlider = QtGui.QSlider(self.tab_6)
        self.DynamicsRigging_horizontalSlider.setMinimum(1)
        self.DynamicsRigging_horizontalSlider.setMaximum(100)
        self.DynamicsRigging_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.DynamicsRigging_horizontalSlider.setObjectName("DynamicsRigging_horizontalSlider")
        self.gridLayout_12.addWidget(self.DynamicsRigging_horizontalSlider, 5, 1, 1, 1)
        self.line_15 = QtGui.QFrame(self.tab_6)
        self.line_15.setFrameShape(QtGui.QFrame.HLine)
        self.line_15.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.gridLayout_12.addWidget(self.line_15, 1, 0, 1, 2)
        self.label_23 = QtGui.QLabel(self.tab_6)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_12.addWidget(self.label_23, 4, 0, 1, 2)
        self.DynamicsRigging_pushButton = QtGui.QPushButton(self.tab_6)
        self.DynamicsRigging_pushButton.setObjectName("DynamicsRigging_pushButton")
        self.gridLayout_12.addWidget(self.DynamicsRigging_pushButton, 6, 0, 1, 2)
        self.label_24 = QtGui.QLabel(self.tab_6)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_12.addWidget(self.label_24, 5, 0, 1, 1)
        self.label = QtGui.QLabel(self.tab_6)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_12.addWidget(self.label, 0, 0, 1, 2)
        self.label_22 = QtGui.QLabel(self.tab_6)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_12.addWidget(self.label_22, 2, 0, 1, 2)
        self.DynamicsRigging_lineEdit = QtGui.QLineEdit(self.tab_6)
        self.DynamicsRigging_lineEdit.setObjectName("DynamicsRigging_lineEdit")
        self.gridLayout_12.addWidget(self.DynamicsRigging_lineEdit, 3, 0, 1, 2)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem4, 7, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout_15.addWidget(self.tabWidget, 1, 0, 1, 2)
        self.line_16 = QtGui.QFrame(self.verticalWidget1)
        self.line_16.setFrameShape(QtGui.QFrame.HLine)
        self.line_16.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.gridLayout_15.addWidget(self.line_16, 31, 0, 1, 2)
        self.gridLayout_13.addWidget(self.verticalWidget1, 0, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem5, 1, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_17 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridWidget1 = QtGui.QWidget(self.tab_4)
        self.gridWidget1.setObjectName("gridWidget1")
        self.gridLayout_16 = QtGui.QGridLayout(self.gridWidget1)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_20 = QtGui.QLabel(self.gridWidget1)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_16.addWidget(self.label_20, 2, 0, 1, 1)
        self.label_19 = QtGui.QLabel(self.gridWidget1)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_16.addWidget(self.label_19, 0, 0, 1, 1)
        self.line_13 = QtGui.QFrame(self.gridWidget1)
        self.line_13.setFrameShape(QtGui.QFrame.HLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.gridLayout_16.addWidget(self.line_13, 9, 0, 1, 1)
        self.BlendShape_List_pushButton = QtGui.QPushButton(self.gridWidget1)
        self.BlendShape_List_pushButton.setObjectName("BlendShape_List_pushButton")
        self.gridLayout_16.addWidget(self.BlendShape_List_pushButton, 3, 0, 1, 1)
        self.line_14 = QtGui.QFrame(self.gridWidget1)
        self.line_14.setFrameShape(QtGui.QFrame.HLine)
        self.line_14.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.gridLayout_16.addWidget(self.line_14, 1, 0, 1, 1)
        self.Create_AttrToCtrl_pushButton = QtGui.QPushButton(self.gridWidget1)
        self.Create_AttrToCtrl_pushButton.setObjectName("Create_AttrToCtrl_pushButton")
        self.gridLayout_16.addWidget(self.Create_AttrToCtrl_pushButton, 7, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.gridWidget1)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_16.addWidget(self.label_21, 6, 0, 1, 1)
        self.gridWidget2 = QtGui.QWidget(self.gridWidget1)
        self.gridWidget2.setObjectName("gridWidget2")
        self.gridLayout_18 = QtGui.QGridLayout(self.gridWidget2)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.BS_List_scrollArea = QtGui.QScrollArea(self.gridWidget2)
        self.BS_List_scrollArea.setWidgetResizable(True)
        self.BS_List_scrollArea.setObjectName("BS_List_scrollArea")
        self.BS_List_WidgetContents = QtGui.QWidget()
        self.BS_List_WidgetContents.setGeometry(QtCore.QRect(0, 0, 330, 153))
        self.BS_List_WidgetContents.setObjectName("BS_List_WidgetContents")
        self.gridLayout_19 = QtGui.QGridLayout(self.BS_List_WidgetContents)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.BS_List_scrollArea.setWidget(self.BS_List_WidgetContents)
        self.gridLayout_18.addWidget(self.BS_List_scrollArea, 0, 0, 1, 1)
        self.gridLayout_16.addWidget(self.gridWidget2, 5, 0, 1, 1)
        self.IsConnect_checkBox = QtGui.QCheckBox(self.gridWidget1)
        self.IsConnect_checkBox.setObjectName("IsConnect_checkBox")
        self.gridLayout_16.addWidget(self.IsConnect_checkBox, 4, 0, 1, 1)
        self.gridLayout_17.addWidget(self.gridWidget1, 0, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem6, 1, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_4, "")
        self.gridLayout_4.addWidget(self.tabWidget_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.thumb_comboBox.setCurrentIndex(1)
        self.index_comboBox.setCurrentIndex(1)
        self.middle_comboBox.setCurrentIndex(1)
        self.ring_comboBox.setCurrentIndex(1)
        self.little_comboBox.setCurrentIndex(1)
        self.ArmNumber_comboBox.setCurrentIndex(2)
        self.spinalNumber_comboBox.setCurrentIndex(0)
        self.LegNumber_comboBox.setCurrentIndex(0)
        self.neckNumber_comboBox.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget_3, self.CharacterName_Edit)
        MainWindow.setTabOrder(self.CharacterName_Edit, self.renameChildren_pushButton)
        MainWindow.setTabOrder(self.renameChildren_pushButton, self.moveVerticesPower_horizontalSlider)
        MainWindow.setTabOrder(self.moveVerticesPower_horizontalSlider, self.moveVerticesSET_pushButton)
        MainWindow.setTabOrder(self.moveVerticesSET_pushButton, self.moveVertices_pushButton)
        MainWindow.setTabOrder(self.moveVertices_pushButton, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.ctrlType_comboBox)
        MainWindow.setTabOrder(self.ctrlType_comboBox, self.ControllerSize_horizontalSlider)
        MainWindow.setTabOrder(self.ControllerSize_horizontalSlider, self.setCtrl_pushButton)
        MainWindow.setTabOrder(self.setCtrl_pushButton, self.CreateSubCtrl_pushButton)
        MainWindow.setTabOrder(self.CreateSubCtrl_pushButton, self.CreatePathCtrl_pushButton)
        MainWindow.setTabOrder(self.CreatePathCtrl_pushButton, self.Blink_Z_checkBox)
        MainWindow.setTabOrder(self.Blink_Z_checkBox, self.Blink_X_checkBox)
        MainWindow.setTabOrder(self.Blink_X_checkBox, self.Blink_Y_checkBox)
        MainWindow.setTabOrder(self.Blink_Y_checkBox, self.Vertex_PointConstraint_checkBox)
        MainWindow.setTabOrder(self.Vertex_PointConstraint_checkBox, self.SET_Name_pushButton)
        MainWindow.setTabOrder(self.SET_Name_pushButton, self.SET_UpVertex_pushButton)
        MainWindow.setTabOrder(self.SET_UpVertex_pushButton, self.SET_DownVertex_pushButton)
        MainWindow.setTabOrder(self.SET_DownVertex_pushButton, self.SET_Size_horizontalSlider)
        MainWindow.setTabOrder(self.SET_Size_horizontalSlider, self.SET_Match_pushButton)
        MainWindow.setTabOrder(self.SET_Match_pushButton, self.Blink_and_Zoom_pushButton)
        MainWindow.setTabOrder(self.Blink_and_Zoom_pushButton, self.DynamicsRigging_horizontalSlider)
        MainWindow.setTabOrder(self.DynamicsRigging_horizontalSlider, self.DynamicsRigging_pushButton)
        MainWindow.setTabOrder(self.DynamicsRigging_pushButton, self.DynamicsRigging_lineEdit)
        MainWindow.setTabOrder(self.DynamicsRigging_lineEdit, self.BlendShape_List_pushButton)
        MainWindow.setTabOrder(self.BlendShape_List_pushButton, self.IsConnect_checkBox)
        MainWindow.setTabOrder(self.IsConnect_checkBox, self.BS_List_scrollArea)
        MainWindow.setTabOrder(self.BS_List_scrollArea, self.Create_AttrToCtrl_pushButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">1.SET_Name</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">2.SET_Size</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.chrSizeSet_Button.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.creatRigLocs_Button.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("MainWindow", "SubJoint", None, QtGui.QApplication.UnicodeUTF8))
        self.Breast_checkBox.setText(QtGui.QApplication.translate("MainWindow", "Breast", None, QtGui.QApplication.UnicodeUTF8))
        self.But_checkBox.setText(QtGui.QApplication.translate("MainWindow", "Butt", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("MainWindow", "Finger", None, QtGui.QApplication.UnicodeUTF8))
        self.thumb_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.thumb_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.index_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.index_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.middle_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.middle_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.ring_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.ring_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.little_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.little_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">3.Rig_Locator</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Arm", None, QtGui.QApplication.UnicodeUTF8))
        self.ArmBend_checkBox.setText(QtGui.QApplication.translate("MainWindow", "Bend", None, QtGui.QApplication.UnicodeUTF8))
        self.ArmNumber_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.ArmNumber_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.ArmNumber_comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.ArmNumber_comboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.ArmNumber_comboBox.setItemText(4, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.ArmNumber_comboBox.setItemText(5, QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Spinal", None, QtGui.QApplication.UnicodeUTF8))
        self.spinalNumber_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.spinalNumber_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.spinalNumber_comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.SpinalBend_checkBox.setText(QtGui.QApplication.translate("MainWindow", "Bend", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Leg", None, QtGui.QApplication.UnicodeUTF8))
        self.LegBend_checkBox.setText(QtGui.QApplication.translate("MainWindow", "Bend", None, QtGui.QApplication.UnicodeUTF8))
        self.LegNumber_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.LegNumber_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.LegNumber_comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.LegNumber_comboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.LegNumber_comboBox.setItemText(4, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.LegNumber_comboBox.setItemText(5, QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Neck", None, QtGui.QApplication.UnicodeUTF8))
        self.neckNumber_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.neckNumber_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.neckNumber_comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.neckNumber_comboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.neckNumber_comboBox.setItemText(4, QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.NeckBend_checkBox.setText(QtGui.QApplication.translate("MainWindow", "Bend", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "Copy_Joint", None, QtGui.QApplication.UnicodeUTF8))
        self.SkinJoint_checkBox.setText(QtGui.QApplication.translate("MainWindow", "Skin", None, QtGui.QApplication.UnicodeUTF8))
        self.Animation_radioButton.setText(QtGui.QApplication.translate("MainWindow", "Animation", None, QtGui.QApplication.UnicodeUTF8))
        self.Unity_radioButton.setText(QtGui.QApplication.translate("MainWindow", "Unity", None, QtGui.QApplication.UnicodeUTF8))
        self.startRigging_Button.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">4.Rigging</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QtGui.QApplication.translate("MainWindow", "Human", None, QtGui.QApplication.UnicodeUTF8))
        self.Q_chrSizeSet_Button.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">2.SET_Size</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_8.setTitle(QtGui.QApplication.translate("MainWindow", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.Q_HorseType_radioButton.setText(QtGui.QApplication.translate("MainWindow", "Horse", None, QtGui.QApplication.UnicodeUTF8))
        self.Q_DogCatType_radioButton.setText(QtGui.QApplication.translate("MainWindow", "Dog or Cat", None, QtGui.QApplication.UnicodeUTF8))
        self.Q_creatRigLocs_Button.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">3.Rig_Locator</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_14.setTitle(QtGui.QApplication.translate("MainWindow", "Copy_Joint", None, QtGui.QApplication.UnicodeUTF8))
        self.Q_SkinJoint_checkBox.setText(QtGui.QApplication.translate("MainWindow", "Skin", None, QtGui.QApplication.UnicodeUTF8))
        self.Q_startRigging_Button.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">4.Rigging</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QtGui.QApplication.translate("MainWindow", "Quadrupeds", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">5.SelectSkinJoint</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.selectSkinJoints_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Rigging", None, QtGui.QApplication.UnicodeUTF8))
        self.ChangeObjUV_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Change_Obj_UV", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Other</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">POWER</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.renameChildren_pushButton.setText(QtGui.QApplication.translate("MainWindow", "RENAME_Children", None, QtGui.QApplication.UnicodeUTF8))
        self.moveVerticesSET_pushButton.setText(QtGui.QApplication.translate("MainWindow", "SET", None, QtGui.QApplication.UnicodeUTF8))
        self.moveVertices_pushButton.setText(QtGui.QApplication.translate("MainWindow", "MOVE_Vertices", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">TYPE</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.ctrlType_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "circle", None, QtGui.QApplication.UnicodeUTF8))
        self.ctrlType_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "square", None, QtGui.QApplication.UnicodeUTF8))
        self.ctrlType_comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "cube", None, QtGui.QApplication.UnicodeUTF8))
        self.ctrlType_comboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "sphere", None, QtGui.QApplication.UnicodeUTF8))
        self.ctrlType_comboBox.setItemText(4, QtGui.QApplication.translate("MainWindow", "balloon", None, QtGui.QApplication.UnicodeUTF8))
        self.ctrlType_comboBox.setItemText(5, QtGui.QApplication.translate("MainWindow", "pyramid", None, QtGui.QApplication.UnicodeUTF8))
        self.ctrlType_comboBox.setItemText(6, QtGui.QApplication.translate("MainWindow", "arCircle", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">1</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">2</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">SIZE</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Controller</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.setCtrl_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Create_Controller", None, QtGui.QApplication.UnicodeUTF8))
        self.CreateSubCtrl_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Create_SubCtrl", None, QtGui.QApplication.UnicodeUTF8))
        self.CreatePathCtrl_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Create_PathCtrl", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("MainWindow", "Controller", None, QtGui.QApplication.UnicodeUTF8))
        self.Blink_Z_checkBox.setText(QtGui.QApplication.translate("MainWindow", "RotateZ", None, QtGui.QApplication.UnicodeUTF8))
        self.Blink_X_checkBox.setText(QtGui.QApplication.translate("MainWindow", "RotateX", None, QtGui.QApplication.UnicodeUTF8))
        self.Blink_Y_checkBox.setText(QtGui.QApplication.translate("MainWindow", "RotateY", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">5.Blink</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">SIZE</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">1.Name</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.Vertex_PointConstraint_checkBox.setText(QtGui.QApplication.translate("MainWindow", "PointConstraint", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">VertexRigging</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.SET_Name_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">2.UpVertex</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.SET_UpVertex_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">3.DownVertex</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.SET_DownVertex_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">4.Match</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.SET_Match_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.Blink_and_Zoom_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "VertexRigging", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">2.SET_Size</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.DynamicsRigging_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">SIZE</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">DynamicsRigging</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">1.SET_Name</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QtGui.QApplication.translate("MainWindow", "DynamicsRigging", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "SubTool", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">1</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Facial_SetUp</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.BlendShape_List_pushButton.setText(QtGui.QApplication.translate("MainWindow", "BlendShape_List", None, QtGui.QApplication.UnicodeUTF8))
        self.Create_AttrToCtrl_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Create_AttrToCtrl", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">2</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.IsConnect_checkBox.setText(QtGui.QApplication.translate("MainWindow", "Is Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "FacialTool", None, QtGui.QApplication.UnicodeUTF8))

class mod_MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent= QtGui.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.chrSizeSet_Button.clicked.connect(lambda: self.RiggingFunction(function='humanSizeSet'))
        self.creatRigLocs_Button.clicked.connect(lambda: self.RiggingFunction(function='creatRigLocs'))
        self.startRigging_Button.clicked.connect(lambda: self.RiggingFunction(function='startRigging'))

        self.Q_chrSizeSet_Button.clicked.connect(lambda: self.RiggingFunction(function='QuadrupedsSizeSet'))
        self.Q_creatRigLocs_Button.clicked.connect(lambda: self.RiggingFunction(function='Q_creatRigLocs'))
        self.Q_startRigging_Button.clicked.connect(lambda: self.RiggingFunction(function='Q_startRigging'))

        self.selectSkinJoints_pushButton.clicked.connect(lambda: self.RiggingFunction(function='selectSkinJoints'))

        self.SET_Name_pushButton.clicked.connect(lambda: self.VertexRiggingFunction(function='SET_Name'))
        self.SET_UpVertex_pushButton.clicked.connect(lambda: self.VertexRiggingFunction(function='SET_UpVertex'))
        self.SET_DownVertex_pushButton.clicked.connect(lambda: self.VertexRiggingFunction(function='SET_DownVertex'))
        self.SET_Match_pushButton.clicked.connect(lambda: self.VertexRiggingFunction(function='SET_Match'))

        self.Blink_and_Zoom_pushButton.clicked.connect(lambda: self.VertexRiggingFunction(function='Blink_and_Zoom'))

        self.DynamicsRigging_pushButton.clicked.connect(lambda: self.DynamicsRiggingFunction(function='CurveToDynCtrls'))

        self.setCtrl_pushButton.clicked.connect(lambda: self.subToolFunction(function='setCtrl'))
        self.CreateSubCtrl_pushButton.clicked.connect(lambda: self.subToolFunction(function='CreateSubCtrl'))
        self.CreatePathCtrl_pushButton.clicked.connect(lambda: self.subToolFunction(function='CreatePathCtrl'))
        self.moveVerticesSET_pushButton.clicked.connect(lambda: self.subToolFunction(function='moveVerticesSET'))
        self.renameChildren_pushButton.clicked.connect(lambda: self.subToolFunction(function='renameChildren'))
        self.ChangeObjUV_pushButton.clicked.connect(lambda: self.subToolFunction(function='ChangeObjUV'))
        self.moveVertices_pushButton.clicked.connect(lambda: self.subToolFunction(function='moveVertices'))

        self.BlendShape_List_pushButton.clicked.connect(lambda: self.Facial_SetUp_Function(function='facialList'))
        self.Create_AttrToCtrl_pushButton.clicked.connect(lambda: self.Facial_SetUp_Function(function='Create_AttrToCtrl'))

    ############################################################
    def RiggingFunction(self,function=''):
        pm.undoInfo(ock=True)
        self.chrName = self.CharacterName_Edit.text()
        if function == 'humanSizeSet':
            self.delCtrls = self.chrSizeSet(high=17)

        if function == 'creatRigLocs':
            self.gbScale = self.delCtrls[1].getTranslation()[1]/17
            if self.Breast_checkBox.checkState():
                breast = 1
            else:
                breast = 0
            if self.But_checkBox.checkState():
                butt = 1
            else:
                butt = 0
            thumb = int(self.thumb_comboBox.currentText())
            index = int(self.index_comboBox.currentText())
            middle = int(self.middle_comboBox.currentText())
            ring = int(self.ring_comboBox.currentText())
            little = int(self.little_comboBox.currentText())
            pm.delete(self.delCtrls)
            self.RigLocs = self.creatRigLocs(breast=breast,butt=butt,thumb=thumb,index=index,middle=middle,ring=ring,little=little)

        if function == 'startRigging':
            #設定
            if self.ArmBend_checkBox.checkState():
                self.ArmBend =  1
            else:
                self.ArmBend =  0
            if self.LegBend_checkBox.checkState():
                self.LegBend = 1
            else:
                self.LegBend = 0
            if self.NeckBend_checkBox.checkState():
                self.NeckBend = 1
            else:
                self.NeckBend = 0
            if self.SpinalBend_checkBox.checkState():
                self.SpinalBend = 1
            else:
                self.SpinalBend = 0
            if self.Unity_radioButton.isChecked():
                self.forUnity = 1
                self.ArmBend = self.LegBend = self.NeckBend = self.SpinalBend = 0
            else:
                self.forUnity = 0
            self.ArmNumber = [int(self.ArmNumber_comboBox.currentText())+2,int(self.ArmNumber_comboBox.currentText())+2]
            self.LegNumber = [int(self.LegNumber_comboBox.currentText())+2,int(self.LegNumber_comboBox.currentText())+2]
            self.neckNumber = int(self.neckNumber_comboBox.currentText())+2
            self.spinalNumber = int(self.spinalNumber_comboBox.currentText())+2
            if self.ArmNumber[1] == 0:
                self.ArmBend =  0
            else:
                pass
            if self.LegNumber[1] == 0:
                self.LegBend = 0
            else:
                pass
            self.gbScale = (pm.PyNode('LOC_head_end').getTranslation(space='world')[1]/17)*2
            #開始Rig
            self.creatRigJoints()
            self.chrScale,self.Data_On,self.Data_Off,self.Joint_grp,self.ctrl_grp,self.rigJoint_grp,\
                self.loc_grp,self.Chatacter = self.offsetCtrl()
            self.chrSize = self.chrScale+'.scaleX'
            self.startRigging(unity=self.forUnity)
            #複製骨架
            if self.SkinJoint_checkBox.checkState():
                copyJt_grp = self.copyRigJt(self.rigJoint_grp.getChildren(),self.Joint_grp,name='Skin')
                pm.parentConstraint(self.chrScale,copyJt_grp,mo=1)
                pm.scaleConstraint(self.chrScale,copyJt_grp,mo=1)
                self.rigJoint_grp.setAttr('visibility',0)
            #除錯
            mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1","deleteUnusedNodes");')
            all = pm.ls()
            for x in all:
                if x.nodeType() == 'transform' and x.getParent() == None and str(x[:9]) == 'transform':
                    pm.delete(x)

        if function == 'QuadrupedsSizeSet':
            if self.Q_HorseType_radioButton.isChecked():
                self.delCtrls = self.chrSizeSet(high=17)
            elif self.Q_DogCatType_radioButton.isChecked():
                self.delCtrls = self.chrSizeSet(high=6)

        if function == 'Q_creatRigLocs':

            if self.Q_HorseType_radioButton.isChecked():
                self.gbScale = self.delCtrls[1].getTranslation()[1]/17
                self.chrSize = self.gbScale
                self.Quadrupeds_Locs = self.Quadrupeds_creatRigLocs(type='horse')
            elif self.Q_DogCatType_radioButton.isChecked():
                self.gbScale = self.delCtrls[1].getTranslation()[1]/6
                self.chrSize = self.gbScale
                self.Quadrupeds_Locs = self.Quadrupeds_creatRigLocs(type='')
            pm.delete(self.delCtrls)

        if function == 'Q_startRigging':
            self.gbScale = self.chrSize
            self.Quadrupeds_creatRigJoints()
            pm.delete(self.Quadrupeds_Locs[2])
            if self.Q_HorseType_radioButton.isChecked():
                self.gbScale *= 2.0
            elif self.Q_DogCatType_radioButton.isChecked():
                self.gbScale *= 1.0
            self.chrScale,self.Data_On,self.Data_Off,self.Joint_grp,\
                self.ctrl_grp,self.rigJoint_grp,self.loc_grp,self.Chatacter = self.offsetCtrl()
            self.Quadrupeds_StartRigging()
            if self.Q_SkinJoint_checkBox.checkState():
                copyJt_grp = self.copyRigJt(self.rigJoint_grp.getChildren(),self.Joint_grp,name='Skin')
                pm.parentConstraint(self.chrScale,copyJt_grp,mo=1)
                pm.scaleConstraint(self.chrScale,copyJt_grp,mo=1)
                self.rigJoint_grp.setAttr('visibility',0)
            #除錯
            mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1","deleteUnusedNodes");')
            all = pm.ls()
            for x in all:
                if x.nodeType() == 'transform' and x.getParent() == None and str(x[:9]) == 'transform':
                    pm.delete(x)

        if function == 'selectSkinJoints':
            try:
                joint_grp = pm.PyNode(self.chrName+'_Joint_grp')
                rigJoint_grp = pm.PyNode(self.chrName+'_rigJoint_grp')
            except:
                sys.stdout.write(u'找不到joint_grp或是rigJoint_grp')
            skinJoint = self.selectSkinJoints(joint_grp,rigJoint_grp)
            pm.select(skinJoint)

        pm.undoInfo(cck=True)

    def VertexRiggingFunction(self,function=''):
        pm.undoInfo(ock=True)
        self.verSize = self.SET_Size_horizontalSlider.value()*0.1
        if self.Vertex_PointConstraint_checkBox.checkState():
            self.conType = 'point'
        else:
            self.conType = None
        if function == 'SET_Name':
            self.verName = raw_input()
            pm.selectPref(tso=1)
            self.ver_loc,self.ver_aimLoc = self.setAimLoc(self.verName)
        if function == 'SET_UpVertex':
            self.up_verJts,self.up_locs,self.up_high_cvs,self.up_low_cvs,self.up_base_wire = self.SET_UpVertex(self.ver_loc,self.ver_aimLoc,conType=self.conType)
        if function == 'SET_DownVertex':
            self.down_verJts,self.down_locs,self.down_high_cvs,self.down_low_cvs,self.down_base_wire = self.SET_DownVertex(self.ver_loc,self.ver_aimLoc,conType=self.conType)
        if function == 'SET_Match':
            self.SET_Match(self.up_verJts,self.up_locs,self.up_high_cvs,self.up_low_cvs,self.up_base_wire,self.down_verJts,self.down_locs,self.down_high_cvs,self.down_low_cvs,self.down_base_wire)
        if function == 'Blink_and_Zoom':
            try:
                if self.Blink_X_checkBox.checkState():
                    nullRotate = 'rotateX'
                elif self.Blink_Y_checkBox.checkState():
                    nullRotate = 'rotateY'
                elif self.Blink_Z_checkBox.checkState():
                    nullRotate = 'rotateZ'
                else:
                    sys.stdout.write(u'請選擇閉眼軸向')
                obj = pm.ls(sl=1)
                cvs = self.up_low_cvs,self.down_low_cvs,self.up_high_cvs,self.down_high_cvs
                for x in obj:
                    if x.nodeType()=='joint':
                        eyeJoint = x
                    elif x.nodeType()!='joint':
                        eyeCtrl = x
            except:
                sys.stdout.write(u'請選擇EyeJoint和EyeCtrl')
            self.Blink_and_Zoom(eyeJoint,eyeCtrl,cvs,nullRotate=nullRotate)
        pm.undoInfo(cck=True)

    def subToolFunction(self,function=''):
        pm.undoInfo(ock=True)
        self.subSize = self.ControllerSize_horizontalSlider.value()
        if function == 'setCtrl':
            self.setCtrl(pm.ls(sl=1),size=self.subSize,ctrlType=self.ctrlType_comboBox.currentText())
        if function == 'CreateSubCtrl':
            self.CreateSubCtrl(pm.ls(sl=1)[0],pm.ls(sl=1)[1])
        if function == 'CreatePathCtrl':
            self.CreatePathCtrl(pm.ls(sl=1))
        if function == 'renameChildren':
            self.renameChildren(pm.ls(sl=1))
        if function == 'ChangeObjUV':
            self.ChangeObjUV(pm.ls(sl=1)[0],pm.ls(sl=1)[1])
        if function == 'moveVerticesSET':
            pm.selectPref(tso=1)
        if function == 'moveVertices':
            self.moveVertices(self.moveVerticesPower_horizontalSlider.value()*0.01)
        pm.undoInfo(cck=True)

    def Facial_SetUp_Function(self,function=''):
        pm.undoInfo(ock=True)
        if function == 'facialList':
            self.bs = pm.ls(sl=1)[0]
            for i in ui.BS_List_WidgetContents.children():
                if type(i) == QtGui.QCheckBox:
                    i.deleteLater()
            if self.IsConnect_checkBox.checkState():
                IsConnect = 1
            else:
                IsConnect = 0
            self.nameList = self.facialList(self.bs,connect=IsConnect)
            self.buttomList = self.CreateQCheckBox(self.nameList)
        if function == 'Create_AttrToCtrl':
            OK_List = []
            ctrl = pm.ls(sl=1)[0]
            for x in range(len(self.buttomList)):
                if self.buttomList[x].checkState():
                    OK_List.append(x)
            for num in OK_List:
                self.setBlendShapeToCtrl(ctrl,self.bs,self.nameList[num],dv=0,min=0,max=10)
            for i in ui.BS_List_WidgetContents.children():
                if type(i) == QtGui.QCheckBox:
                    i.deleteLater()
            self.nameList = self.facialList(self.bs)
            self.buttomList = self.CreateQCheckBox(self.nameList)
        pm.undoInfo(cck=True)

    def DynamicsRiggingFunction(self,function=''):
        pm.undoInfo(ock=True)
        self.hairName = self.DynamicsRigging_lineEdit.text()
        self.DynCtrlSize = self.DynamicsRigging_horizontalSlider.value()*0.1
        if function == 'CurveToDynCtrls':
            curves = pm.ls(sl=1)
            self.CurveToDynCtrls(curves,size=self.DynCtrlSize,hairName=self.hairName)
        pm.undoInfo(cck=True)

    ####################RigFunction(已整理)####################

    def getTgtAttr(self,tgt):
        '''
        判斷朝向子物件的方向
        '''
        axis = str()
        if tgt.nodeType() == 'joint':
            try: 
                tgt.listRelatives(c=1)
                tgtGrp = tgt.listRelatives(c=1)[0]
            except: 
                tgt.listRelatives(p=1)
                tgtGrp = tgt.listRelatives(p=1)[0]
        else:
            tgtGrp = tgt
        t = tgtGrp.translate.get()
        tol = 0.0001
        for i in range(3):
            if abs(t[i]) > tol:
                if  i == 0: axis = 'X'
                elif i == 1: axis = 'Y'
                elif i == 2: axis = 'Z'
        nrDict = {'X':[1,0,0],'Y':[0,1,0],'Z':[0,0,1]}
        nr = nrDict[axis]
        return nr,axis

    def lockAttrs(self,objs,attrs=['tx','ty','tz','sx','sy','sz','v']):
        '''
        將objs的attrs隱藏並上鎖
        '''
        for x in attrs:
            objs.setAttr(x,keyable=0,lock=1)

    def snap(self,tgt,follower,trans=1,rot=1,scl=1,pivots=1):
        '''
        follower吸附至tgt,依照是否跟隨trans,rot,scl,pivots
        '''
        if trans: follower.setTranslation(tgt.getTranslation(space='world'),space='world')
        if rot:follower.setRotation(tgt.getRotation(space='world'),space='world')
        if scl:follower.setScale(tgt.getScale())
        if pivots:
            follower.setRotatePivot(tgt.getRotatePivot(space='world'))
            follower.setScalePivot(tgt.getScalePivot(space='world'))
        return tgt,follower

    def cvsCtrl(self,size=1.0,name='',axis=None,depth = 1,length = 2,ctrlType='circle',rotateOrder=0):
        '''
        創建控制器
        '''
        s = size
        if ctrlType=='circle':
            ctrl = pm.circle(nr = axis,ch=0,n=name,radius = s)[0]
        if ctrlType=='circleX':
            ctrl = pm.circle(nr = [1,0,0],ch=0,n=name,radius = s)[0]
        if ctrlType=='circleY':
            ctrl = pm.circle(nr = [0,1,0],ch=0,n=name,radius = s)[0]
        if ctrlType=='circleZ':
            ctrl = pm.circle(nr = [0,0,1],ch=0,n=name,radius = s)[0]
        if ctrlType == 'arrow_circle':
            ctrl = pm.curve(d=3,n=name,p=([0,s*0.4492,0],[0,s*0.4452,s*0.3],\
                [0,s*0.0297,s*0.5312],[0,s*-0.3526,s*0.3526],[0,s*-0.4986,0],\
                [0,s*-0.3526,s*-0.3526],[0,s*0.0474,s*-0.5163],[0,s*0.4164,s*-0.2855],\
                [0,s*0.4492,0],[0,s*0.4492,0],[0,s*0.4492,0],[0,s*0.4841,s*-0.0506],\
                [0,s*0.4841,s*-0.0506],[0,s*0.4492,0],[0,s*0.4492,0],[0,s*0.4141,s*-0.0536]))
        if ctrlType=='rombus':
            ctrl = pm.curve(d=1,n=name,ep=([0,s,0],[s,0,0],[0,0,s],[s*-1,0,0],[0,0,s*-1],\
                [0,s,0],[0,0,s],[0,s*-1,0],[0,0,s*-1],[s,0,0],[0,s,0],[s*-1,0,0],[0,s*-1,0],[s,0,0]))
        if ctrlType=='diamond':
            ctrl = pm.curve(d=1,n=name,ep=([0,s*1,0],[0,0,s*1],[0,s*-1,0],[0,0,s*-1],\
                [0,s*1,0],[0,s*0.5,0],[0,0,s*0.5],[0,0,s*1],[0,0,s*0.5],[0,s*-0.5,0],[0,s*-1,0],\
                [0,s*-0.5,0],[0,0,s*-0.5],[0,0,s*-1],[0,0,s*-0.5],[0,s*0.5,0]))
        if ctrlType=='double':
            ctrl = pm.curve(d=1,n=name,ep=([0,0,-2.31-s],[-0.99,0,-0.99-s],[-0.33,0,-0.99-s],\
                [-0.33,0,0.99+s],[-0.99,0,0.99+s],[0,0,2.31+s],[0.99,0,0.99+s],[0.33,0,0.99+s],\
                [0.33,0,-0.99-s],[0.99,0,-0.99-s],[0,0,-2.31-s]))
        if ctrlType=='fingerL':
            ctrl = pm.curve(d=1,n=name,ep=([0,s/2,s/5],[s,s/2,s/5],[s,s/2,s/-5],[0,s/2,s/-5],[0,s/2,s/5]))
        if ctrlType=='fingerR':
            ctrl = pm.curve(d=1,n=name,ep=([0,s/-2,s/5],[s*-1,s/-2,s/5],[s*-1,s/-2,s/-5],[0,s/-2,s/-5],[0,s/-2,s/5]))
        if ctrlType=='square':
            ctrl = pm.curve(d=1,n=name,ep=([s*-0.5,0,s*-0.5],[s*-0.5,0,s*0.5],[s*0.5,0,s*0.5],[s*0.5,0,s*-0.5],[s*-0.5,0,s*-0.5]))
        if ctrlType=='cross':
            ctrl = pm.curve(d=1,n=name,ep=([s*-0.5,0,0],[0,0,s*0.5],[s*0.5,0,0],[0,0,s*-0.5],\
                [s*-0.5,0,0],[s*0.5,0,0],[0,0,s*0.5],[0,0,s*-0.5]))
        if ctrlType == 'cross_2':
            ctrl = pm.curve(d=1,n=name,ep=([s*-0.2145,s*0.03065,0],[s*-0.03065,s*0.03065,0],[s*-0.03065,s*0.2145,0],\
                [s*0.03065,s*0.2145,0],[s*0.03065,s*0.03065,0],[s*0.2145,s*0.03065,0],[s*0.2145,s*-0.03065,0],\
                [s*0.03065,s*-0.03065,s*0.0],[s*0.03065,s*-0.2145,0],[s*-0.03065,s*-0.2145,0],\
                [s*-0.03065,s*-0.03065,0],[s*-0.2145,s*-0.03065,0],[s*-0.2145,s*0.03065,0]))
        if ctrlType=='cube':
            ctrl = pm.curve(d=1,n=name,ep=([s,s,s],[s,s*-1,s],[s*-1,s*-1,s],[s*-1,s,s],\
                [s,s,s,],[s,s,s*-1],[s*-1,s,s*-1],[s*-1,s,s],[s*-1,s*-1,s],[s*-1,s*-1,s*-1],\
                [s*-1,s,s*-1],[s,s,s*-1],[s,s*-1,s*-1],[s*-1,s*-1,s*-1],[s*-1,s*-1,s],[s,s*-1,s],\
                [s,s*-1,s*-1]))
        if ctrlType=='180Thin':
            ctrl = pm.curve(d=1,n=name,ep=([-0.446514*s,0,-1.351664*s],\
                [0.0107043*s,0,-1.001418*s],[-0.339542*s,0,-0.5442*s],\
                [0.0107043*s,0,-1.001418*s],[-0.13006*s,0,-1*s],[-0.393028*s,0,-0.947932*s],\
                [-0.725413*s,0,-0.725516*s],[-0.947961*s,0,-0.392646*s],[-1.026019*s,0,0],\
                [-0.947961*s,0,0.392646*s],[-0.725413*s,0,0.725516*s],[-0.393028*s,0,0.947932*s],\
                [-0.13006*s,0,1*s],[0,0,1*s],[-0.339542*s,0,0.5442*s],[0,0,1*s],\
                [-0.446514*s,0,1.351664*s]))
            ctrl.setAttr('rz',-90)
            pm.makeIdentity(ctrl,a=1)
        if ctrlType=='pyramid':
            depth = depth*s
            ctrl = pm.curve(n=name,d=1,p=((0,0,0),(s,-1*depth,0),(-1*s,-1*depth,0),(0,-1*depth,s),\
                (s,-1*depth,0),(0,-1*depth,-1*s),(-1*s,-1*depth,0),(0,0,0),(0,-1*depth,s),\
                (0,-1*depth,-1*s),(0,0,0)))
        if ctrlType == 'balloon':
            length = length * s
            ctrl = pm.curve(n=name,p=([0,0,-1*length],[-1.125*s,0,-1*length+s*-1],[0,0,(-1*length)+s*-2],\
                [s,0,-1*length+s*-1],[0,0,-1*length],[0,0,-1*length],[0,0,-1*length],[0,0,0]))
        if ctrlType=='sphere':
            ctrl = pm.curve(d=1,n=name,ep=([0,0,1*s],[0,0.5*s,0.866025*s],[0,0.866025*s,0.5*s],\
                [0,1*s,0],[0,0.866025*s,-0.5*s],[0,0.5*s,-0.866025*s],[0,0,-1*s],\
                [0,-0.5*s,-0.866025*s],[0,-0.866025*s,-0.5*s],[0,-1*s,0],[0,-0.866025*s,0.5*s],\
                [0,-0.5*s,0.866025*s],[0,0,1*s],[0.707107*s,0,0.707107*s],[1*s,0,0],\
                [0.707107*s,0,-0.707107*s],[0,0,-1*s],[-0.707107*s,0,-0.707107*s],[-1*s,0,0],\
                [-0.866025*s,0.5*s,0],[-0.5*s,0.866025*s,0],[0,1*s,0],[0.5*s,0.866025*s,0],\
                [0.866025*s,0.5*s,0],[1*s,0,0],[0.866025*s,-0.5*s,0],[0.5*s,-0.866025*s,0],\
                [0,-1*s,0],[-0.5*s,-0.866025*s,0],[-0.866025*s,-0.5*s,0],[-1*s,0,0],\
                [-0.707107*s,0,0.707107*s],[0,0,1*s]))
        if ctrlType=='nail':
            ctrl = pm.curve(d=1,n=name,ep=([0,0,0],[2*s,0,0],[3*s,0,-1*s],[4*s,0,0],\
                [3*s,0,1*s],[2*s,0,0],[4*s,0,0],[3*s,0,-1*s],[3*s,0,1*s]))
        if ctrlType == 'arCircle':
            circleCtrl = pm.circle(r=s,nr=(0,1,0))
            pm.delete(circleCtrl[1])
            ctrl = pm.curve(n=name,d=1,p=((0,0,-1*s),(0,0,1*s),(0.2*s,0,0.8*s),(-0.2*s,0,0.8*s),(0,0,1*s)))
            pm.parent(circleCtrl[0].listRelatives(s=1)[0],ctrl,shape=1,r=1)
            pm.delete(circleCtrl[0])
        if ctrlType=='locator':
            ctrl = pm.curve(d=1,n=name,ep=([-1*s,0,0],[1*s,0,0],[0,0,0],[0,0,-1*s],[0,0,1*s],\
                [0,0,0],[0,1*s,0],[0,-1*s,0]))
        if ctrlType=='fourFat':
            ctrl = pm.curve(d=1,n=name,ep=([0,0,2.209343*s],[0.883737*s,0,1.325606*s],\
                [0.552336*s,0,1.325606*s],[0.552336*s,0,0.552187*s],[1.325606*s,0,0.552187*s],\
                [1.325606*s,0,0.883737*s],[2.209343*s,0,0],[1.325606*s,0,-0.883737*s],\
                [1.325606*s,0,-0.552187*s],[0.552336*s,0,-0.552187*s],[0.552336*s,0,-1.325606*s],\
                [0.883737*s,0,-1.325606*s],[0,0,-2.209343*s],[-0.883737*s,0,-1.325606*s],\
                [-0.552336*s,0,-1.325606*s],[-0.552336*s,0,-0.552187*s],[-1.325606*s,0,-0.552187*s],\
                [-1.325606*s,0,-0.883737*s],[-2.209343*s,0,0],[-1.325606*s,0,0.883737*s],\
                [-1.325606*s,0,0.552187*s],[-0.552336*s,0,0.552187*s],[-0.552336*s,0,1.325606*s],
                [-0.883737*s,0,1.325606*s],[0,0,2.209343*s]))
        if ctrlType == 'semicircle':
            ctrl = pm.curve(d=1,n=name,ep=([s*-0.157,s*0.5,s*-0.993],[s*-0.157,s*0.807,s*-0.946],\
                [s*-0.157,s*1.084,s*-0.805],[s*-0.157,s*1.305,s*-0.584],[s*-0.157,s*1.446,s*-0.307],\
                [s*-0.157,s*1.495,0],[s*-0.157,s*1.446,s*0.307],[s*-0.157,s*1.305,s*0.584],\
                [s*-0.157,s*1.084,0.805],[s*-0.157,s*0.807,s*0.946],[s*-0.157,s*0.5,s*0.993],[s*-0.157,0,s*0.993],\
                [s*0.157,0,s*1.006],[s*0.157,s*0.500,s*1.006],[s*0.157,s*0.811,s*0.958],\
                [s*0.157,s*1.092,s*0.815],[s*0.157,s*1.315,s*0.592],[0.157,s*1.458,s*0.311],\
                [s*0.157,s*1.507,0],[s*0.157,s*1.458,s*-0.311],[s*0.157,s*1.315,s*-0.592],\
                [s*0.157,s*1.092,s*-0.815],[s*0.157,s*0.811,s*-0.958],[s*0.157,s*0.5,s*-1.006],\
                [s*0.157,0,s*-1.006],[s*-0.157,0,s*-0.993],[s*-0.157,s*0.5,s*-0.993]))
        if ctrlType == 'four_arrow':
            ctrl = pm.curve(d=1,n=name,ep=([s*-1.874,0,s*-0.182],[s*-2.139,0,s*-0.182],\
                [s*-2.139,0,s*-0.508],[s*-2.647,0,0],[s*-2.139,0,s*0.508],[s*-2.139,0,s*0.182],\
                [s*-1.874,0,s*0.182],[s*-1.874,0,s*-0.182]))
            arrow_1 = pm.curve(d=1,n=name,ep=([s*-0.182,0,s*1.874],[s*-0.182,0,s*2.139],\
                [s*-0.508,0,s*2.139],[0,0,s*2.647],[s*0.508,0,s*2.139],[s*0.182,0,s*2.139],\
                [s*0.182,0,s*1.874],[s*-0.182,0,s*1.874]))
            arrow_2 = pm.curve(d=1,n=name,ep=([s*1.874,0,s*0.182],[s*2.139,0,s*0.182],\
                [s*2.139,0,s*0.508],[s*2.647,0,0],[s*2.139,0,s*-0.508],[s*2.139,0,s*-0.182],\
                [s*1.874,0,s*-0.182],[s*1.874,0,s*0.182]))
            arrow_3 = pm.curve(d=1,n=name,ep=([s*0.182,0,s*-1.874],[s*0.182,0,s*-2.139],\
                [s*0.508,0,s*-2.139],[0,0,s*-2.647],[s*-0.508,0,s*-2.139],[s*-0.182,0,s*-2.139],\
                [s*-0.182,0,s*-1.874],[s*0.182,0,s*-1.874]))
            pm.parent(arrow_1.listRelatives(s=1)[0],arrow_2.listRelatives(s=1)[0],\
                arrow_3.listRelatives(s=1)[0],ctrl,shape=1,r=1)
            pm.delete(arrow_1,arrow_2,arrow_3)
        if rotateOrder == 1:
            ctrl.setAttr('rotateOrder',k=1)
        return ctrl

    def ctrlGrp(self,tgt,size=1.0,parent=1,point=0,orient=0,scale=0,depth=1,length=2,lock=['sx','sy','sz','v'],ctrlType='circle',rotateOrder=0):
        '''
        創建指定的ctrl控制tgt,依照種類設定控制方式,parent,point,orient,scale
        lock為ctrl上鎖的attr
        '''
        try:
            nr,axis = self.getTgtAttr(tgt)
        except:
            nr=[0,1,0]
            s=1
            axis=None
        ctrl = self.cvsCtrl(size=size,name=tgt+'_ctrl',axis=nr,depth=depth,length=length,ctrlType=ctrlType,rotateOrder=rotateOrder)
        upper = pm.group(n=ctrl+'_upper',em=1)
        cons = pm.group(n=ctrl+'_cons',em=1)
        pm.parent(ctrl,upper)
        pm.parent(upper,cons)
        self.snap(tgt,cons)
        grps = [upper,cons]
        if orient == 1:
            self.snap(tgt,grps[-1],rot=0)
        else:
            self.snap(tgt,grps[-1])
        if parent==1:
            parCon1 = pm.parentConstraint(ctrl,tgt)
        else:
            if point ==1:
                parCon1 = pm.pointConstraint(ctrl,tgt)
            parCon1 = None
        if scale==1:
            parCon2 = pm.scaleConstraint(ctrl,tgt)
        else:
            parCon2 = None
        self.lockAttrs(ctrl,attrs=lock)
        return grps,ctrl,parCon1,parCon2

    def setCtrl(self,tgt,ctrlType='',size=1.0,depth=1,length=2,lock=['sx','sy','sz','v'],rotateOrder=0):
        '''
        將tgt內的所有物件做連續串聯ctrl, cons>upper>ctrl
        '''
        ctrlList = []
        upperList = []
        consList = []
        parConList1 = []
        parConList2 = []
        for i in tgt:
            temp = self.ctrlGrp(i,size=size,parent=1,lock=lock,depth=depth,length=length,ctrlType=ctrlType)
            if rotateOrder == 1:
                temp[1].setAttr('rotateOrder',k=1)
            ctrlList.append(temp[1])
            upperList.append(temp[0][0])
            consList.append(temp[0][1])
            parConList1.append(temp[2])
            parConList2.append(temp[3])
            if len(consList)>1:
                pm.parent(consList[-1],ctrlList[-2])
        return ctrlList,upperList,consList

    ####################RigFunction(未整理)####################

    def blendColorNode(self,Blend,Color1,Color2,OutColor,Channel=4):
        blendColor = pm.shadingNode('blendColors',al=1)
        pm.connectAttr(Blend,blendColor+'.blender')
        if Channel == 1:
            try:pm.connectAttr(Color1,blendColor+'.color1R')
            except:blendColor.setAttr('color1R',Color1)
            try:pm.connectAttr(Color2,blendColor+'.color2R')
            except:blendColor.setAttr('color2R',Color2)
            try:pm.connectAttr(blendColor+'.outputR',OutColor)
            except: pass
        if Channel == 4:
            try:pm.connectAttr(Color1,blendColor+'.color1')
            except:blendColor.setAttr('color1',Color1)
            try:pm.connectAttr(Color2,blendColor+'.color2')
            except:blendColor.setAttr('color2',Color2)
            try:pm.connectAttr(blendColor+'.output',OutColor)
            except: pass
        return blendColor

    def MultiplyDivideNode(self,operation,Input1,Input2,Output,Channel=4):
        MultiplyDivide = pm.shadingNode('multiplyDivide',al=1)
        try:MultiplyDivide.setAttr('operation',operation)
        except: pass
        if Channel ==1:
            try:pm.connectAttr(Input1,MultiplyDivide+'.input1X')
            except:MultiplyDivide.setAttr('input1X',Input1)
            try:pm.connectAttr(Input2,MultiplyDivide+'.input2X')
            except:MultiplyDivide.setAttr('input2X',Input2)
            try:pm.connectAttr(MultiplyDivide+'.outputX',Output)
            except: pass
        if Channel ==2:
            try:pm.connectAttr(Input1[0],MultiplyDivide+'.input1X')
            except:MultiplyDivide.setAttr('input1X',Input1[0])
            try:pm.connectAttr(Input1[1],MultiplyDivide+'.input1Y')
            except:MultiplyDivide.setAttr('input1Y',Input1[1])
            try:pm.connectAttr(Input2[0],MultiplyDivide+'.input2X')
            except:MultiplyDivide.setAttr('input2X',Input2[0])
            try:pm.connectAttr(Input2[1],MultiplyDivide+'.input2Y')
            except:MultiplyDivide.setAttr('input2Y',Input2[1])
            try:pm.connectAttr(MultiplyDivide+'.output',Output)
            except: pass
        if Channel ==3:
            try:pm.connectAttr(Input1[0],MultiplyDivide+'.input1X')
            except:MultiplyDivide.setAttr('input1X',Input1[0])
            try:pm.connectAttr(Input1[1],MultiplyDivide+'.input1Y')
            except:MultiplyDivide.setAttr('input1Y',Input1[1])
            try:pm.connectAttr(Input1[2],MultiplyDivide+'.input1Z')
            except:MultiplyDivide.setAttr('input1Z',Input1[2])
            try:pm.connectAttr(Input2[0],MultiplyDivide+'.input2X')
            except:MultiplyDivide.setAttr('input2X',Input2[0])
            try:pm.connectAttr(Input2[1],MultiplyDivide+'.input2Y')
            except:MultiplyDivide.setAttr('input2Y',Input2[1])
            try:pm.connectAttr(Input2[2],MultiplyDivide+'.input2Z')
            except:MultiplyDivide.setAttr('input2Z',Input2[2])
            try:pm.connectAttr(MultiplyDivide+'.output',Output)
            except: pass
        if Channel ==4:
            try:pm.connectAttr(Input1,MultiplyDivide+'.input1')
            except:MultiplyDivide.setAttr('input1',Input1)
            try:pm.connectAttr(Input2,MultiplyDivide+'.input2')
            except:MultiplyDivide.setAttr('input2',Input2)
            try:pm.connectAttr(MultiplyDivide+'.output',Output)
            except: pass
        return MultiplyDivide

    def plusMinusAverageNode(self,operation,Input0,Input1,Output,Channel=4):
        PlusMinusAverage = pm.shadingNode('plusMinusAverage',al=1)
        try:PlusMinusAverage.setAttr('operation',operation)
        except: pass
        if Channel ==1:
            try:pm.connectAttr(Input0,PlusMinusAverage+'.input1D[0]')
            except:PlusMinusAverage.setAttr('input1D[0]',Input0)
            try:pm.connectAttr(Input1,PlusMinusAverage+'.input1D[1]')
            except:PlusMinusAverage.setAttr('input1D[1]',Input1)
            try:pm.connectAttr(PlusMinusAverage+'.output1D',Output)
            except: pass
        if Channel ==2:
            try:pm.connectAttr(Input0[0],PlusMinusAverage+'.input3D[0].input3Dx')
            except:PlusMinusAverage.setAttr('input3D[0].input3Dx',Input0[0])
            try:pm.connectAttr(Input0[1],PlusMinusAverage+'.input3D[0].input3Dy')
            except:PlusMinusAverage.setAttr('input3D[0].input3Dy',Input0[1])
            try:pm.connectAttr(Input1[0],PlusMinusAverage+'.input3D[1].input3Dx')
            except:PlusMinusAverage.setAttr('input3D[1].input3Dx',Input1[0])
            try:pm.connectAttr(Input1[1],PlusMinusAverage+'.input3D[1].input3Dy')
            except:PlusMinusAverage.setAttr('input3D[1].input3Dy',Input1[1])
            try:pm.connectAttr(PlusMinusAverage+'.output3D',Output)
            except: pass
        if Channel ==3:
            try:pm.connectAttr(Input0[0],PlusMinusAverage+'.input3D[0].input3Dx')
            except:PlusMinusAverage.setAttr('input3D[0].input3Dx',Input0[0])
            try:pm.connectAttr(Input0[1],PlusMinusAverage+'.input3D[0].input3Dy')
            except:PlusMinusAverage.setAttr('input3D[0].input3Dy',Input0[1])
            try:pm.connectAttr(Input0[2],PlusMinusAverage+'.input3D[0].input3Dz')
            except:PlusMinusAverage.setAttr('input3D[0].input3Dz',Input0[2])
            try:pm.connectAttr(Input1[0],PlusMinusAverage+'.input3D[1].input3Dx')
            except:PlusMinusAverage.setAttr('input3D[1].input3Dx',Input1[0])
            try:pm.connectAttr(Input1[1],PlusMinusAverage+'.input3D[1].input3Dy')
            except:PlusMinusAverage.setAttr('input3D[1].input3Dy',Input1[1])
            try:pm.connectAttr(Input1[2],PlusMinusAverage+'.input3D[1].input3Dz')
            except:PlusMinusAverage.setAttr('input3D[1].input3Dz',Input1[2])
            try:pm.connectAttr(PlusMinusAverage+'.output3D',Output)
            except: pass
        if Channel ==4:
            try:pm.connectAttr(Input0,PlusMinusAverage+'.input3D[0]')
            except:PlusMinusAverage.setAttr('input3D[0]',Input0)
            try:pm.connectAttr(Input1,PlusMinusAverage+'.input3D[1]')
            except:PlusMinusAverage.setAttr('input3D[1]',Input1)
            try:pm.connectAttr(PlusMinusAverage+'.output3D',Output)
            except: pass
        return PlusMinusAverage

    def conditionNode(self,operation,firstTerm,secondTerm,colorIfTrue,colorIfFalse,outColor,Channel=4):
        Condition = pm.shadingNode('condition',al=1)
        try:Condition.setAttr('operation',operation)
        except: pass
        try:pm.connectAttr(firstTerm,Condition+'.firstTerm')
        except:Condition.setAttr('firstTerm',firstTerm)
        try:pm.connectAttr(secondTerm,Condition+'.secondTerm')
        except:Condition.setAttr('secondTerm',secondTerm)    
        if Channel ==1:
            try:pm.connectAttr(colorIfTrue,Condition+'.colorIfTrueR')
            except:Condition.setAttr('colorIfTrueR',colorIfTrue)
            try:pm.connectAttr(colorIfFalse,Condition+'.colorIfFalseR')
            except:Condition.setAttr('colorIfFalseR',colorIfFalse)
            try:pm.connectAttr(outColor,Condition+'.outColorR')
            except:pass
        if Channel ==4:
            try:pm.connectAttr(colorIfTrue,Condition+'.colorIfTrue')
            except:Condition.setAttr('colorIfTrue',colorIfTrue)
            try:pm.connectAttr(colorIfFalse,Condition+'.colorIfFalse')
            except:Condition.setAttr('colorIfFalse',colorIfFalse)
            try:pm.connectAttr(outColor,Condition+'.outColor')
            except:pass
        return Condition

    def clampNode(self,input,max,min,output,Channel=4):
        Clamp = pm.shadingNode('clamp',al=1)
        if Channel==1:
            try:pm.connectAttr(input,Clamp+'.inputR')
            except:Clamp.setAttr('inputR',input)
            try:pm.connectAttr(max,Clamp+'.maxR')
            except:Clamp.setAttr('maxR',max)
            try:pm.connectAttr(min,Clamp+'.minR')
            except:Clamp.setAttr('minR',min)
            try:pm.connectAttr(output,Clamp+'.outputR')
            except:pass
        return Clamp

    def reverseNode(self,input,output,Channel=4):
        Reverse = pm.shadingNode('reverse',al=1)
        if Channel==1:
            try:pm.connectAttr(input,Reverse+'.inputX')
            except:Reverse.setAttr('inputX',input)
            try:pm.connectAttr(output,Reverse+'.outputX')
            except:pass
        if Channel==2:
            try:pm.connectAttr(input[0],Reverse+'.inputX')
            except:Reverse.setAttr('inputX',input[0])
            try:pm.connectAttr(input[1],Reverse+'.inputY')
            except:Reverse.setAttr('inputY',input[1])
            try:pm.connectAttr(output[0],Reverse+'.outputX')
            except:pass
            try:pm.connectAttr(output[1],Reverse+'.outputY')
            except:pass
        if Channel==3:
            try:pm.connectAttr(input[0],Reverse+'.inputX')
            except:Reverse.setAttr('inputX',input[0])
            try:pm.connectAttr(input[1],Reverse+'.inputY')
            except:Reverse.setAttr('inputY',input[1])
            try:pm.connectAttr(input[2],Reverse+'.inputZ')
            except:Reverse.setAttr('inputZ',input[2])
            try:pm.connectAttr(output[0],Reverse+'.outputX')
            except:pass
            try:pm.connectAttr(output[1],Reverse+'.outputY')
            except:pass
            try:pm.connectAttr(output[2],Reverse+'.outputZ')
            except:pass
        if Channel==4:
            try:pm.connectAttr(input,Reverse+'.input')
            except:Reverse.setAttr('input',input)
            try:pm.connectAttr(output,Reverse+'.output')
            except:pass
        return Reverse

    def LookPoleVectorCvs(self,tgt1,tgt2,name=''):
        cvs = pm.curve(d=1,name=name,ep=(tgt1.getTranslation(space='world'),tgt2.getTranslation(space='world')))
        pm.setAttr(cvs + '.overrideEnabled', 1)
        pm.setAttr(cvs + '.overrideDisplayType', 2)
        clu1=pm.cluster(cvs+'.cv[0]')[1]
        clu2=pm.cluster(cvs+'.cv[1]')[1]
        pm.parent(clu1,tgt1)
        pm.parent(clu2,tgt2)
        clu1.hide()
        clu2.hide()
        return cvs

    def addSwitch(self,obj,name='',at='',dv='',min='',max='',k=1):
        pm.select(obj)
        pm.addAttr(ln=name,at=at,dv=dv,min=min,max=max,k=k)

    def tgtLoc(self,tgts):
        locList = []
        try:
            worldLoc = pm.PyNode(self.chrName+'_world_loc')
        except:
            worldLoc = pm.spaceLocator(n=self.chrName+'_world_loc')
        locList.append(worldLoc)
        for x in tgts:
            try:
                loc = pm.PyNode(x+'_loc')
            except:
                loc = pm.spaceLocator(n=x+'_loc')
            pm.parentConstraint(x,loc)
            locList.append(loc)
        return locList

    def ctrlFollow(self,ctrl,tgts,ctrlType=''):
        consParConList=[]
        locList = self.tgtLoc(tgts)
        upper = ctrl.listRelatives(p=1)[0]
        cons = upper.listRelatives(p=1)[0]
        ctrlLoc = pm.spaceLocator(n=ctrl+'_loc')
        self.snap(ctrl,ctrlLoc)
        self.snap(tgts[-1],ctrlLoc,rot=0)
        if ctrlType == 'fk':
            pm.parentConstraint(tgts[-1],upper,mo=1,sr=['x','y','z'])
            pm.parentConstraint(ctrlLoc,cons,mo=1,st=['x','y','z'])
        if ctrlType == 'ik':
            pm.parentConstraint(ctrlLoc,cons,mo=1)        
        consParCon = pm.parentConstraint(locList,ctrlLoc,mo=1)
        for j in range(len(tgts)):
            n=[]
            for x in range(len(str(tgts[j]))):
                if tgts[j][x]=='_':
                    n.append(x)
            n=tgts[j][n[0]+1:]
            self.addSwitch(ctrl,name=n+'_Follow',at='float',dv=0,min=0,max=1,k=1)
            w={0:'W1',1:'W2',2:'W3',3:'W4',4:'W5'}
            weight=w[j]
            pm.connectAttr(ctrl+'.'+n+'_Follow',consParCon+'.'+locList[j+1]+weight)
        self.addSwitch(ctrl,name='world_Follow',at='float',dv=0,min=0,max=1,k=1)
        pm.connectAttr(ctrl+'.world_Follow',consParCon+'.'+self.chrName+'_world_locW0')
        locList.append(ctrlLoc)
        return locList

    def createIk(self,jt,stJt='',secondJt='',endJt='',pvCvsJt='',type='r',pvOrientation=1,loc='',About='',ikType=''):
        solver = {'r':'ikRPsolver','c':'ikSCsolver','s':'ikSplineSolver'}
        s = solver[type]
        jtName=stJt+'_ik'
        grpsList = []
        ctrlList = []
        if ikType == 'arm':
            grpsTip,ctrlTip,parCon1Tip,parCon2Tip=self.ctrlGrp(endJt,size=self.gbScale*0.2,parent=0,lock=['v'],ctrlType='cube',orient=0)
            grpsEnd,ctrlEnd,parCon1End,parCon2End=self.ctrlGrp(stJt,size=self.gbScale*0.4,parent=0,point=1,lock=['rx','ry','rz','sx','sy','sz','v'],ctrlType='circle')
            IK_Rot_ctrl_1 = self.cvsCtrl(size=self.gbScale*0.22,name=endJt+'_Rot_ctrl_1',ctrlType='sphere',rotateOrder=1)
            IK_Rot_ctrl_1_upper = pm.group(n=IK_Rot_ctrl_1+'_upper')
            IK_Rot_ctrl_1_cons = pm.group(n=IK_Rot_ctrl_1+'_cons')
            pm.parent(IK_Rot_ctrl_1,IK_Rot_ctrl_1_upper)
            pm.parent(IK_Rot_ctrl_1_upper,IK_Rot_ctrl_1_cons)
            IK_Rot_ctrl_2 = self.cvsCtrl(size=self.gbScale*0.18,name=endJt+'_Rot_ctrl_2',ctrlType='sphere',rotateOrder=1)
            self.addSwitch(IK_Rot_ctrl_1,name='sub_ctrl',at='long',dv=0,min=0,max=1)
            IK_Rot_ctrl_1.setAttr('sub_ctrl',keyable=0,channelBox=1)
            pm.connectAttr(IK_Rot_ctrl_1+'.sub_ctrl',IK_Rot_ctrl_2+'.visibility')
            self.snap(endJt,IK_Rot_ctrl_1_cons)
            self.snap(endJt,IK_Rot_ctrl_2)
            pm.parent(IK_Rot_ctrl_1_cons,ctrlTip)
            pm.parent(IK_Rot_ctrl_2,IK_Rot_ctrl_1)
            self.lockAttrs(IK_Rot_ctrl_1,attrs=['tx','ty','tz','sx','sy','sz','v'])
            self.lockAttrs(IK_Rot_ctrl_2,attrs=['tx','ty','tz','sx','sy','sz','v'])
            pm.orientConstraint(IK_Rot_ctrl_2,endJt,mo=1)
            pm.connectAttr(ctrlTip+'.scale',endJt+'.scale')
            ctrlList.append(ctrlTip)
            ctrlList.append(ctrlEnd)
            ctrlList.append(IK_Rot_ctrl_1)
            ctrlList.append(IK_Rot_ctrl_2)
        if ikType == 'leg':
            grpsTip,ctrlTip,parCon1Tip,parCon2Tip=self.ctrlGrp(endJt,size=self.gbScale*0.2,parent=0,lock=['v'],ctrlType='cube',orient=1,rotateOrder=1)
            grpsTip[1].setAttr('r',[0,0,0])
            grpsEnd,ctrlEnd,parCon1End,parCon2End=self.ctrlGrp(stJt,size=self.gbScale*0.4,parent=0,point=1,lock=['rx','ry','rz','sx','sy','sz','v'],ctrlType='circle')
            ctrlList.append(ctrlTip)
            ctrlList.append(ctrlEnd)
        grpsList.append(grpsTip)
        grpsList.append(grpsEnd)
        self.addSwitch(ctrlTip,name='sub_ctrl',at='long',dv=0,min=0,max=1)
        ctrlTip.setAttr('sub_ctrl',keyable=0,channelBox=1)
        pm.connectAttr(ctrlTip+'.sub_ctrl',grpsEnd[0]+'.visibility')
        ik = pm.ikHandle(sj=stJt,ee=endJt,n=jtName,sol=s)[0]
        ik.hide()
        pv = pm.spaceLocator(name=stJt+'_pv')
        self.snap(jt[1],pv)
        pv.hide()
        pvMove=abs(secondJt.translateX.get())+abs(endJt.translateX.get())
        pvt=pv.translateZ.get()
        PoleVectorCvs=self.LookPoleVectorCvs(pvCvsJt,pv,name = self.chrName+'_'+About+'_'+ikType+'_PoleVectorCvs')
        ctrlsize=secondJt.radius.get()/2
        pvGrp = self.ctrlGrp(pv,size=0.2*self.gbScale,parent=0,scale=0,lock=['rx','ry','rz','sx','sy','sz','v'],ctrlType='rombus')[:2]
        if ikType == 'arm':
            pvGrp[0][1].setAttr('translateZ',pvt-pvMove)
            pm.parent(pv,pvGrp[1])
            pv.setAttr('translate',[0,0,0])
            pvGrp[0][1].setAttr('rotate',[0,0,0])
            worldLoc = None
        if ikType == 'leg':
            pvGrp[0][1].setAttr('translateZ',pvt+pvMove)
            PvUpperJt = pm.duplicate(stJt,n=self.chrName+About+'_leg_pv_upper',po=1)[0]
            PvEndJt = pm.duplicate(endJt,n=self.chrName+About+'_leg_pv_lower',po=1)[0]
            worldLoc = pm.spaceLocator(n=self.chrName+About+'_leg_pv_World')
            pm.parent(PvEndJt,PvUpperJt)
            self.jointOrient([PvUpperJt,PvEndJt],[0,-1,0],[1,0,0],[0,-1,0])
            pvIk = pm.ikHandle(sj=PvUpperJt,ee=PvEndJt,n=self.chrName+'_pv'+About+'_ik',sol='ikSCsolver')[0]
            pvIk.hide()
            self.addSwitch(pvGrp[1],name='Knee_Leg_Follow',at='float',dv=1,min=0,max=1,k=1)
            pm.parent(pvIk,ctrlTip)
            pm.parent(pv,pvGrp[1])
            pv.setAttr('translate',[0,0,0])
            pvGrp[0][1].setAttr('rotate',[0,0,0])
            pvPanCon = pm.parentConstraint(PvUpperJt,worldLoc,pvGrp[0][1],mo=1)
            pm.connectAttr(pvGrp[1]+'.Knee_Leg_Follow',pvPanCon+'.'+PvUpperJt+'W0')
            pvRN1 = self.reverseNode(pvPanCon+'.'+PvUpperJt+'W0',None,Channel=1)
            pm.connectAttr(pvRN1+'.outputX',pvPanCon+'.'+worldLoc+'W1')
        attPv = pm.poleVectorConstraint(pv,ik)
        pm.parent(ik,ctrlTip)
        if ikType == 'leg':
            footIk = pm.ikHandle(sj=endJt,ee=jt[-2],n=About+'_footIk',sol='ikSCsolver')[0]
            toeIk = pm.ikHandle(sj=jt[-2],ee=jt[-1],n=About+'_toeIk',sol='ikSCsolver')[0]
            footIk.hide()
            toeIk.hide()
            anklePv = self.cvsCtrl(size=0.15*self.gbScale,name=About+'_anklePv_ctrl',ctrlType='cross')
            topCtrl = self.cvsCtrl(size=0.15*self.gbScale,name=About+'_top_ctrl',ctrlType='cross')
            heelCtrl = self.cvsCtrl(size=0.15*self.gbScale,name=About+'_heel_ctrl',ctrlType='cross')
            leftCtrl = self.cvsCtrl(size=0.1*self.gbScale,name=About+'_left_ctrl',ctrlType='cross')
            rightCtrl = self.cvsCtrl(size=0.1*self.gbScale,name=About+'_right_ctrl',ctrlType='cross')
            footPvGrp = pm.group(n=About+'_footPv_grp',em=1)
            toeIkGrp = pm.group(n=About+'_toeIk_grp',em=1)
            ankleIkGrp = pm.group(n=About+'_ankleIk_grp',em=1)
            heelCtrlGrp = pm.group(n=About+'_heelCtrl_grp',em=1)
            topCtrlGrp = pm.group(n=About+'_topCtrl_grp',em=1)
            footCtrlGrp = pm.group(n=About+'_footCtrl_grp',em=1)
            leftGrp = pm.group(n=About+'_left_grp',em=1)
            rightGrp = pm.group(n=About+'_right_grp',em=1)
            topCtrlCons = pm.group(n=About+'_topCtrl_cons',em=1)
            heelCtrlCons = pm.group(n=About+'_heelCtrl_cons',em=1)
            legGrp1 = (ankleIkGrp,anklePv)
            for j in legGrp1:
                self.snap(endJt,j,rot=0)
            self.snap(jt[-1],topCtrlGrp,rot=0)
            legGrp2 = (topCtrl,topCtrlCons)
            for k in legGrp2:
                self.snap(topCtrlGrp,k,rot=0)
            legGrp3 = (heelCtrlGrp,heelCtrlCons,heelCtrl)
            for l in legGrp3:
                self.snap(loc,l,rot=0)
            legGrp4 = (toeIkGrp,leftGrp,leftCtrl,rightGrp,rightCtrl,footCtrlGrp)
            for m in legGrp4:
                self.snap(jt[-2],m,rot=0)
            pm.parent(toeIk,toeIkGrp)
            pm.parent(footIk,ik,footCtrlGrp)
            pm.parent(toeIkGrp,footCtrlGrp,leftGrp)
            pm.parent(leftGrp,leftCtrl,rightCtrl,rightGrp)
            pm.parent(rightGrp,topCtrlGrp)
            pm.parent(topCtrl,topCtrlCons)
            pm.parent(topCtrlCons,topCtrlGrp,heelCtrlGrp)
            pm.parent(heelCtrl,heelCtrlCons)
            pm.parent(heelCtrlGrp,heelCtrlCons,ankleIkGrp)
            pm.parent(anklePv,ankleIkGrp,footPvGrp)
            pm.parent(footPvGrp,ctrlTip)
            lowerDist = endJt.translateX.get()
            if lowerDist < 0:
                lowerDist=lowerDist*-1
            leftCtrl.setAttr('tx',lowerDist/5)
            rightCtrl.setAttr('tx',lowerDist/5*-1)
            lockCtrls = (anklePv,topCtrl,heelCtrl,leftCtrl,rightCtrl)
            for i in lockCtrls:
                self.lockAttrs(i,attrs=['sx','sy','sz','v'])
            name = ('roll','toeRot','side')
            self.addSwitch(ctrlTip,name='toeLift',at='float',dv=40,min=1,max=360,k=0)
            self.addSwitch(ctrlTip,name='toeStraight',at='float',dv=70,min=0,max=360,k=0)
            for i in name:
                self.addSwitch(ctrlTip,name=i,at='float',dv=0,min=-360,max=360)
            pm.connectAttr(ctrlTip+'.toeRot',toeIkGrp+'.rotateX')
            pm.connectAttr(anklePv+'.rotate',ankleIkGrp+'.rotate')
            footPMA1 = self.plusMinusAverageNode(2,anklePv+'.translate',anklePv.translate.get(),ankleIkGrp+'.rotatePivot',Channel=4)
            pm.connectAttr(topCtrl+'.translate',topCtrlGrp+'.rotatePivot')
            pm.connectAttr(heelCtrl+'.translate',heelCtrlGrp+'.rotatePivot')
            pm.connectAttr(leftCtrl+'.translate',leftGrp+'.rotatePivot')
            pm.connectAttr(rightCtrl+'.translate',rightGrp+'.rotatePivot')
            self.addSwitch(ctrlTip,name='footPv_Display',at='float',dv=1,min=0,max=1)
            pm.connectAttr(ctrlTip+'.footPv_Display',footPvGrp+'.visibility')
            ctrlTip.setAttr('footPv_Display',0)
            ctrlTip.setAttr('footPv_Display',keyable=0,channelBox=1)
            if About == 'L':
                footSide=1
            if About == 'R':
                footSide=-1
            footMD1 = self.MultiplyDivideNode(1,ctrlTip+'.side',footSide,None,Channel=1)
            footMD2 = self.MultiplyDivideNode(1,ctrlTip+'.side',footSide,None,Channel=1)
            footCN1 = self.clampNode(footMD1+'.outputX',0,-360,None,Channel=1)
            footCN2 = self.clampNode(footMD2+'.outputX',360,0,None,Channel=1)
            pm.connectAttr(footCN1+'.outputR',leftGrp+'.rotateZ')
            pm.connectAttr(footCN2+'.outputR',rightGrp+'.rotateZ')
            LegCN1 = self.clampNode(ctrlTip+'.roll',0,-360,None,Channel=1)
            LegCN2 = self.clampNode(heelCtrl+'.rotateX',0,-360,None,Channel=1)
            LegPMA1 = self.plusMinusAverageNode(1,LegCN1+'.outputR',LegCN2+'.outputR',heelCtrlGrp+'.rotateX',Channel=1)
            pm.connectAttr(heelCtrl+'.rotateY',heelCtrlGrp+'.rotateY')
            pm.connectAttr(heelCtrl+'.rotateZ',heelCtrlGrp+'.rotateZ')
            pm.connectAttr(topCtrl+'.rotateY',topCtrlGrp+'.rotateY')
            LegPMA2 = self.plusMinusAverageNode(2,ctrlTip+'.toeStraight',ctrlTip+'.toeLift',None,Channel=1)
            LegPMA3 = self.plusMinusAverageNode(2,ctrlTip+'.roll',ctrlTip+'.toeLift',None,Channel=1)
            LegCN3 = self.clampNode(LegPMA3+'.output1D',LegPMA2+'.output1D',0,None,Channel=1)
            LegMD1 = self.MultiplyDivideNode(2,LegCN3+'.outputR',LegPMA2+'.output1D',None,Channel=1)
            LegMD2 = self.MultiplyDivideNode(1,LegMD1+'.outputX',ctrlTip+'.roll',None,Channel=1) 
            LegPMA4 = self.plusMinusAverageNode(1,topCtrl+'.rotateX',LegMD2+'.outputX',topCtrlGrp+'.rotateX',Channel=1)
            LegCN4 = self.clampNode(ctrlTip+'.roll',ctrlTip+'.toeLift',0,None,Channel=1)
            LegMD3 = self.MultiplyDivideNode(2,LegCN4+'.outputR',ctrlTip+'.toeLift',None,Channel=1)
            LegPMA5 = self.plusMinusAverageNode(2,1,LegMD1+'.outputX',None,Channel=1)
            LegMD4 = self.MultiplyDivideNode(1,LegMD3+'.outputX',LegPMA5+'.output1D',None,Channel=1)
            LegMD5 = self.MultiplyDivideNode(1,LegMD4+'.outputX',ctrlTip+'.roll',footCtrlGrp+'.rotateX',Channel=1)
        else:
            PvUpperJt = None
        return ik,grpsList,ctrlList,pvGrp,PoleVectorCvs,pvGrp[1],PvUpperJt,worldLoc

    def IKFKJointCopy(self,tgt,name=''):
        jtList = []
        for i in range(len(tgt)):
            position = []
            for x in range(len(str(tgt[i]))):
                if str(tgt[i])[x] == '_':
                    position.append(x)
            num = position[0]
            jt=pm.duplicate(tgt[i],n=tgt[i][:num]+'_'+name+tgt[i][num:],po=1)[0]
            pm.parent(jt,w=1)
            jtList.append(jt)
            if len(jtList) >1:
                pm.parent(jtList[-1],jtList[-2])
            #jtList[i].setAttr('visibility',0)
            jtList[i].setAttr('drawStyle',2)
        return jtList

    def ikfkMatch(self,jt,ikType='',About='',loc='',bend=1):
        ikList = self.IKFKJointCopy(jt,name='IK')
        fkList = self.IKFKJointCopy(jt,name='FK')
        if About=='L':
            w={'arm':-1,'leg':1}
        elif About=='R':
            w={'arm':1,'leg':-1}
        world=w[ikType]
        if ikType=='leg':
            fkList.remove(fkList[-1])
        else:pass
        #FK
        FkCtrlList,upperList,consList=self.setCtrl(fkList,size=0.3*self.gbScale,lock=['tx','ty','tz','sx','sy','sz','v'],ctrlType='circle',rotateOrder=1)
        lockAttr = ['tx','ty','tz']
        for x in lockAttr:
            FkCtrlList[0].setAttr(x,keyable=1,lock=0)
        self.lockAttrs(FkCtrlList[1],attrs=['rx','rz'])
        FkCtrlList[2].setAttr('scaleX',l=0,k=1)
        FkCtrlList[2].setAttr('scaleY',l=0,k=1)
        FkCtrlList[2].setAttr('scaleZ',l=0,k=1)
        pm.pointConstraint(jt[1],consList[1])
        pm.pointConstraint(jt[2],consList[2])
        pm.connectAttr(FkCtrlList[2]+'.scale',fkList[2]+'.scale')
        #ArmIk
        if ikType=='arm':
            ik,ikgrps,ikCtrlList,pvGrp,PoleVectorCvs,pv,PvUpperJt,worldLoc = \
                self.createIk(jt,stJt=ikList[0],secondJt=ikList[1],endJt=ikList[2],\
                pvCvsJt=jt[1],pvOrientation=world,About=About,ikType='arm')
            hand_sub_ctrl = self.cvsCtrl(size=0.25*self.gbScale,name=fkList[-1]+'_sub_ctrl',ctrlType='circleX',rotateOrder=1)
            self.snap(FkCtrlList[-1],hand_sub_ctrl)
            pm.parent(hand_sub_ctrl,FkCtrlList[-1])
            pm.delete(fkList[2].rotateX.inputs()[0])
            pm.orientConstraint(hand_sub_ctrl,fkList[2],mo=1)
            for i in range(len(FkCtrlList)-1):
                self.addSwitch(FkCtrlList[i],name='Stretchy',at='float',dv=1,min=0,max=10,k=1)
            self.addSwitch(FkCtrlList[2],name='sub_ctrl',at='long',dv=0,min=0,max=1)
            FkCtrlList[2].setAttr('sub_ctrl',keyable=0,channelBox=1)
            pm.connectAttr(FkCtrlList[2]+'.sub_ctrl',hand_sub_ctrl+'.visibility')
            self.lockAttrs(hand_sub_ctrl,attrs=['tx','ty','tz','sx','sy','sz','v'])
            FkCtrlList.append(hand_sub_ctrl)
        #LegIk
        elif ikType=='leg':
            ik,ikgrps,ikCtrlList,pvGrp,PoleVectorCvs,pv,PvUpperJt,worldLoc = \
                self.createIk(ikList,stJt=ikList[0],secondJt=ikList[1],endJt=ikList[2],\
                pvCvsJt=jt[1],pvOrientation=world,loc=loc,About=About,ikType='leg')
            for i in range(len(FkCtrlList)-1):
                self.addSwitch(FkCtrlList[i],name='Stretchy',at='float',dv=1,min=0,max=10,k=1)
            pm.connectAttr(ikCtrlList[0]+'.scale',ikList[2]+'.scale')
        #ikfkSwitch
        ctrlsize=ikList[1].radius.get()/2
        ikfkSwitch=self.cvsCtrl(size=0.2*self.gbScale,name=self.chrName+'_'+About+'_'+ikType+'_'+'ikfkSwitch',ctrlType='diamond')
        switchGrp=pm.group(ikfkSwitch,n=ikfkSwitch+'_cons')
        if ikType == 'arm':
            ikfkSwitch.setAttr('translateY',abs(ikList[2].translateX.get()/2))
        else:
            ikfkSwitch.setAttr('translateX',ikList[2].translateX.get()/2)
        ikfkSwitch.setAttr('rotateX',90)
        self.lockAttrs(ikfkSwitch,attrs=['tx','ty','tz','rx','ry','rz','sx','sy','sz','v'])
        self.snap(ikList[2],switchGrp,rot=0,scl=0,pivots=0)
        pm.pointConstraint(jt[2],switchGrp,mo=1)
        #addSwitch
        self.addSwitch(ikfkSwitch,name='ikfk',at='float',dv=1,min=0,max=1)
        if bend == 1:
            self.addSwitch(ikfkSwitch,name='Auto_IK_Stretchy',at='float',dv=1,min=0,max=1)
            self.addSwitch(ikfkSwitch,name='Auto_Sqiash_Stretchy',at='float',dv=1,min=0,max=1)
            self.addSwitch(ikfkSwitch,name='Auto_Sqiash_Stretchy_Width',at='float',dv=1,min=0,max=10)
            self.addSwitch(ikfkSwitch,name=ikType+'_width',at='float',dv=1,min=0,max=10)
            self.addSwitch(ikfkSwitch,name=ikType+'_Stretchy',at='float',dv=0,min=0,max=30)
            self.addSwitch(ikfkSwitch,name='Upper_'+ikType+'_Stretchy',at='float',dv=0,min=0,max=30)
            self.addSwitch(ikfkSwitch,name='Lower_'+ikType+'_Stretchy',at='float',dv=0,min=0,max=30)
            self.addSwitch(ikfkSwitch,name='bend_Display',at='float',dv=1,min=0,max=1)
            self.addSwitch(ikfkSwitch,name='twist_Display',at='float',dv=1,min=0,max=1)
            ikfkSwitch.setAttr('bend_Display',keyable=0,channelBox=1)
            ikfkSwitch.setAttr('twist_Display',keyable=0,channelBox=1)
            ikfkSwitch.setAttr('bend_Display',0)
            ikfkSwitch.setAttr('twist_Display',0)
            self.addSwitch(ikCtrlList[0],name='Arc',at='float',dv=0,min=-100,max=100,k=1)
        else:
            pass
        self.addSwitch(ikCtrlList[0],name='Twist',at='float',dv=0,min=-180,max=180,k=1)
        #ikCtrlDisplay
        ikDis=(ikgrps[0][-1],ikgrps[1][-1],pvGrp[0][-1],PoleVectorCvs)
        ikCtrlGrp = pm.group(em=1,n=jt[0]+'_ikCtrl_grp')
        self.snap(jt[0],ikCtrlGrp,rot=0)
        for i in ikDis:
            pm.parent(i,ikCtrlGrp)
            pm.connectAttr(ikfkSwitch+'.ikfk',i+'.visibility')
        pm.parent(PoleVectorCvs,w=1)
        #fkCtrlDisplay
        fkCtrlGrp = pm.group(em=1,n=jt[0]+'_fkCtrl_grp')
        self.snap(jt[0],fkCtrlGrp,rot=0)
        pm.parent(consList[0],fkCtrlGrp)
        fkReNode = pm.shadingNode('reverse',al=1)
        pm.connectAttr(ikfkSwitch+'.ikfk',fkReNode+'.inputX')
        pm.connectAttr(fkReNode+'.outputX',fkCtrlGrp+'.visibility')
        #IKFK_blendColorNode
        for i in range(len(fkList)):
            self.blendColorNode(ikfkSwitch+'.ikfk',ikList[i]+'.rotate',fkList[i]+'.rotate',jt[i]+'.rotate')
        self.blendColorNode(ikfkSwitch+'.ikfk',ikList[0]+'.translate',fkList[0]+'.translate',jt[0]+'.translate')
        self.blendColorNode(ikfkSwitch+'.ikfk',ikList[2]+'.scale',fkList[2]+'.scale',jt[2]+'.scale')
        if ikType=='leg':
            self.blendColorNode(ikfkSwitch+'.ikfk',ikList[3]+'.scale',fkList[3]+'.scale',jt[3]+'.scale')
        #Twist
        pm.connectAttr(ikCtrlList[0]+'.Twist',ik+'.twist')
        #append
        pvList=[]
        pvList.append(pv)
        pvList.append(PoleVectorCvs)
        return ikfkSwitch,ikCtrlList,FkCtrlList,ikList,fkList,pvList,ik,PvUpperJt,worldLoc

    def splineIkJoint(self,jt1,jt2,number=6,name='_BendJt_1'):
        tran = (jt2.translateX.get()/(number-1))
        spjtList = []
        for i in range(number):
            spjt = pm.duplicate(jt1,po=1,n=jt1+name)[0]
            spjt.setAttr('preferredAngle',[0,0,0])
            pm.parent(spjt,w=1)
            spjtList.append(spjt)
            if len(spjtList) > 1 :
                pm.parent(spjtList[-1],spjtList[-2])
                spjtList[-1].setAttr('translateX',tran)
            pm.parent(spjtList[0],w=1)
        return spjtList

    def splineIkInfo(self,spJts):
        ik = pm.ikHandle(sj=spJts[0],ee=spJts[-1],n=spJts[0]+'_splineIk',sol='ikSplineSolver')
        ik[2].rename(spJts[0]+'_splineCvs')
        pm.parent(ik[2],w=1)
        ik[0].setAttr('v',0)
        crv = ik[2].listRelatives(shapes=1)[0]
        cv=crv.getCVs()
        cvsInfo=pm.arclen(ik[2],ch=1)
        return ik,cv,cvsInfo,crv

    def skinSplineCvs(self,jt,tgt,num):
        spCtrlJtList = []
        for i in range(num):
            spCtrlJt=pm.duplicate(jt,po=1,n=jt+'_Bend_1')[0]
            spCtrlJt.setTranslation(tgt[i],space='world')
            spCtrlJtList.append(spCtrlJt)
            if len(spCtrlJtList) > 1:
                pm.parent(spCtrlJtList[-1],spCtrlJtList[-2])
        return spCtrlJtList

    def betweenConstraint(self,tgt1,tgt2,obj,aim,part=2,delParcon=0,type='point',Vector=[0,1,0]):
        if type=='point':
            parCon=pm.pointConstraint(tgt1,tgt2,obj)
        if type=='parent':
            parCon=pm.parentConstraint(tgt1,tgt2,obj)
        if part==2:
            parCon.setAttr(tgt2+'W1',2)
        else:pass
        if delParcon ==1:
            pm.delete(parCon)
            parCon=None
        else:pass   
        if aim:
            aimCon=pm.aimConstraint(aim,obj,mo=1)
            aimCon.setAttr('worldUpType',2)
            aimCon.setAttr('worldUpVector',Vector)
            pm.connectAttr(aim+'.worldMatrix',aimCon+'.worldUpMatrix')
            if delParcon ==1:
                pm.delete(aimCon)
            else:pass
        else:
            aimCon=None
        return parCon,aimCon

    def distancetgt(self,tgt1,tgt2):
        tgtLoc1=tgt1.getTranslation(space='world')
        tgtLoc2=tgt2.getTranslation(space='world')
        distShapes=pm.distanceDimension(sp=tgtLoc1,ep=tgtLoc2)
        dist=distShapes.distance.get()
        loc=distShapes.listConnections()
        loc[0].rename(tgt1+'_loc')
        loc[1].rename(tgt2+'_loc')
        pm.pointConstraint(tgt1,loc[0])
        pm.pointConstraint(tgt2,loc[1])
        return distShapes,dist,loc

    def addTwistJoint(self,tgtJoint,number,ikType=''):
        twistJt = []
        lowerLen = tgtJoint[2].getTranslation()[0]
        for x in range(number):
            jt = pm.duplicate(tgtJoint[1],po=1,n=tgtJoint[1]+'_twistJt_1')[0]
            twistJt.append(jt)
        for x in range(number-1):
            pm.parent(twistJt[x+1],twistJt[x])
            twistJt[x+1].setAttr('translateX',lowerLen/(number-1))
        twistIk = pm.ikHandle(sj=twistJt[0],ee=twistJt[-1],n=twistJt[0][:-3]+'_Ik',sol='ikSplineSolver')
        pm.parent(twistIk[2],tgtJoint[1])
        nonrollJt_1 = pm.duplicate(tgtJoint[-1],po=1,n=tgtJoint[-1]+'_nonroll_1')[0]
        nonrollJt_2 = pm.duplicate(tgtJoint[-1],po=1,n=tgtJoint[-1]+'_nonroll_2')[0]
        pm.parent(nonrollJt_2,nonrollJt_1)
        nonrollJt_2.setAttr('translateX',lowerLen/2)
        auxJt_1 = pm.duplicate(tgtJoint[-1],po=1,n=tgtJoint[-1]+'_aux_1')[0]
        auxJt_2 = pm.duplicate(tgtJoint[-1],po=1,n=tgtJoint[-1]+'_aux_2')[0]
        auxJt_3 = pm.duplicate(tgtJoint[-1],po=1,n=tgtJoint[-1]+'_aux_3')[0]
        pm.parent(auxJt_2,auxJt_1)
        pm.parent(auxJt_3,auxJt_2)
        auxJt_2.setAttr('translateX',lowerLen/4)
        auxJt_3.setAttr('translateX',lowerLen/4)
        NonrollIk = pm.ikHandle(sj=nonrollJt_1,ee=nonrollJt_2,n=nonrollJt_1+'_nonrollIk',sol='ikSplineSolver')
        AuxIk = pm.ikHandle(sj=auxJt_1,ee=auxJt_3,n=auxJt_1+'_auxIk',sol='ikSplineSolver')
        twistIKs = twistIk,NonrollIk,AuxIk
        for ik in twistIKs:
            pm.parent(ik[0],tgtJoint[2])
            for x in range(3):
                ik[x].setAttr('v',0)
        pm.parent(NonrollIk[2],tgtJoint[-1])
        pm.parent(AuxIk[2],tgtJoint[-1])
        AuxIk[0].setAttr('dTwistControlEnable',1)
        if ikType=='arm':
            pm.connectAttr(auxJt_2+'.rotateX',twistIk[0]+'.twist')
        elif ikType=='leg':
            pm.connectAttr(auxJt_2+'.rotateX',twistIk[0]+'.roll')
        AuxIk[0].setAttr('dWorldUpType',4)
        AuxIk[0].setAttr('dWorldUpAxis',0)
        hideJt = nonrollJt_1,nonrollJt_2,auxJt_1,auxJt_2,auxJt_3,twistJt[0],twistJt[-1]
        for x in hideJt:
            x.setAttr('drawStyle',2)
        if ikType=='arm': 
            AuxIk[0].setAttr('dWorldUpAxis',3)
            AuxIk[0].setAttr('dWorldUpVector',[0,0,1])
            AuxIk[0].setAttr('dWorldUpVectorEnd',[0,0,1])
        if ikType=='leg':
            AuxIk[0].setAttr('dWorldUpVector',[0,1,0])
            AuxIk[0].setAttr('dWorldUpVectorEnd',[0,1,0])
            tgtJoint[-1].setAttr('drawStyle',2)
        pm.connectAttr(nonrollJt_1+'.worldMatrix',AuxIk[0]+'.dWorldUpMatrix')
        pm.connectAttr(tgtJoint[-1]+'.worldMatrix',AuxIk[0]+'.dWorldUpMatrixEnd')
        #group_and_parent
        twist_grp = pm.group(n=tgtJoint[1]+'_twistJt_grp',em=1)
        pm.parent(twistJt[0],nonrollJt_1,auxJt_1,twistIk[0],NonrollIk[0],AuxIk[0],twist_grp)
        pm.parent(twist_grp,self.rigJoint_grp)

    def ikfkFunction(self,jt,ikType='',About='',loc='',JtNumber=[6,6],bend=1):
        upper=jt[0]
        lower=jt[1]
        end=jt[2]
        tip=jt[3]
        lowerDist = lower.translateX.get()
        endDist = end.translateX.get()
        Spacing=abs(lowerDist)+abs(endDist)
        if ikType=='arm':
            matchJt = []
            matchJt.append(upper)
            matchJt.append(lower)
            matchJt.append(tip)
        elif ikType=='leg':
            matchJt = []
            for i in range(len(jt)):
                matchJt.append(jt[i])
            matchJt.remove(end)
        #ikfkMatch
        ikfkSwitch,ikCtrlList,fkCtrlList,ikList,fkList,pv,ik,PvUpperJt,worldLoc = \
            self.ikfkMatch(matchJt,ikType=ikType,About=About,loc=loc,bend=bend)
        if bend == 1:
            #splineJt*2
            upperSpJt=self.splineIkJoint(upper,lower,number=JtNumber[0])
            lowerSpJt=self.splineIkJoint(lower,end,number=JtNumber[1])
            upperSpJtGrp = pm.group(em=1,n=upper+'_BendJtGrp')
            lowerSpJtGrp = pm.group(em=1,n=lower+'_BendJtGrp')
            self.snap(upper,upperSpJtGrp,rot=0)
            self.snap(lower,lowerSpJtGrp,rot=0)
            pm.parent(upperSpJt[0],upperSpJtGrp)
            pm.parent(lowerSpJt[0],lowerSpJtGrp)
            NoneJts = upperSpJt[0],upperSpJt[-1],lowerSpJt[0],lowerSpJt[-1]
            for x in NoneJts:
                x.setAttr('drawStyle',2)
            #splineIkInfo
            upperIk,upperCv,upperCvsInfo,upperCrv = self.splineIkInfo(upperSpJt)
            lowerIk,lowerCv,lowerCvsInfo,lowerCrv = self.splineIkInfo(lowerSpJt)
            pm.parent(upperIk[0],upperSpJtGrp)
            pm.parent(lowerIk[0],lowerSpJtGrp)
            #skinSplineCvs
            upperBendCtrlList = self.skinSplineCvs(upper,upperCv,4)
            lowerBendCtrlList = self.skinSplineCvs(lower,lowerCv,4)
            #SplineCvsJt -> CtrlGrp
            upperCons1,upperCtrl1,parCon1,parCon2 = self.ctrlGrp(upperBendCtrlList[1],\
                parent=0,size=0.25*self.gbScale,lock=['rx','ry','rz','sx','v'],ctrlType='circle')
            upperCons2,upperCtrl2,parCon1,parCon2 = self.ctrlGrp(upperBendCtrlList[2],\
                parent=0,size=0.25*self.gbScale,lock=['rx','ry','rz','sx','v'],ctrlType='circle')
            upperCons3,upperCtrl3,parCon1,parCon2 = self.ctrlGrp(upperBendCtrlList[3],\
                parent=0,size=0.25*self.gbScale,lock=['rx','ry','rz','sx','v'],ctrlType='circle')
            lowerCons1,lowerCtrl1,parCon1,parCon2 = self.ctrlGrp(lowerBendCtrlList[1],\
                parent=0,size=0.25*self.gbScale,lock=['rx','ry','rz','sx','v'],ctrlType='circle')
            lowerCons2,lowerCtrl2,parCon1,parCon2 = self.ctrlGrp(lowerBendCtrlList[2],\
                parent=0,size=0.25*self.gbScale,lock=['rx','ry','rz','sx','v'],ctrlType='circle')
            for k in range(4):
                pm.parent(upperBendCtrlList[k],w=1)
                pm.parent(lowerBendCtrlList[k],w=1)
            pm.skinCluster(upperBendCtrlList,upperIk[2],tsb=1,normalizeWeights=2)
            pm.skinCluster(lowerBendCtrlList,lowerIk[2],tsb=1,normalizeWeights=2)
            pm.parent(upperBendCtrlList[1],upperCtrl1)
            pm.parent(upperBendCtrlList[2],upperCtrl2)
            pm.parent(upperBendCtrlList[3],upperCtrl3)
            pm.parent(lowerBendCtrlList[1],lowerCtrl1)
            pm.parent(lowerBendCtrlList[2],lowerCtrl2)
            pm.parent(lowerBendCtrlList[0],upperCtrl3)
            BendCtrlList = upperBendCtrlList[0],upperBendCtrlList[1],upperBendCtrlList[2],\
                upperBendCtrlList[3],lowerBendCtrlList[0],lowerBendCtrlList[1],lowerBendCtrlList[2],\
                lowerBendCtrlList[3]
            for x in BendCtrlList:   
                x.setAttr('drawStyle',2)
            pm.parentConstraint(upper,upperBendCtrlList[0])
            pm.parentConstraint(tip,lowerBendCtrlList[3])
            self.betweenConstraint(upperCtrl3,upper,upperCons1[1],upperCtrl3,Vector=[0,1,0])
            self.betweenConstraint(upper,upperCtrl3,upperCons2[1],upperCtrl3,Vector=[0,1,0])
            if ikType=='arm':    
                self.betweenConstraint(tip,upperCtrl3,lowerCons1[1],upperCtrl3,Vector=[0,1,0])
                self.betweenConstraint(upperCtrl3,tip,lowerCons2[1],upperCtrl3,Vector=[0,1,0])
            if ikType=='leg':
                self.betweenConstraint(tip,upperCtrl3,lowerCons1[1],upperCtrl3,Vector=[0,-1,0])
                self.betweenConstraint(upperCtrl3,tip,lowerCons2[1],upperCtrl3,Vector=[0,-1,0])
            spCtrlCons = pm.group(upperCons1[1],upperCons2[1],upperCons3[1],lowerCons1[1],\
                lowerCons2[1],n=About+'_'+ikType+'_Bend_grp')
            pm.connectAttr(ikfkSwitch+'.bend_Display',spCtrlCons+'.visibility')
            upperlength = upperCvsInfo.arcLength.get()
            lowerlength = lowerCvsInfo.arcLength.get()
            upperMD1 = self.MultiplyDivideNode(1,self.chrSize,upperlength,None,Channel=1)
            upperMD2 = self.MultiplyDivideNode(2,upperCvsInfo+'.arcLength',upperMD1+'.outputX',None,Channel=1)
            lowerMD1 = self.MultiplyDivideNode(1,self.chrSize,lowerlength,None,Channel=1)
            lowerMD2 = self.MultiplyDivideNode(2,lowerCvsInfo+'.arcLength',lowerMD1+'.outputX',None,Channel=1)
            for i in range(len(upperSpJt)-1):
                pm.connectAttr(upperMD2+'.outputX',upperSpJt[i]+'.scaleX')
                pm.connectAttr(lowerMD2+'.outputX',lowerSpJt[i]+'.scaleX')
            bendCtrlList= upperCtrl1,upperCtrl2,upperCtrl3,lowerCtrl1,lowerCtrl2
            #IK拉伸功能
            distShapes,dist,ikloc = self.distancetgt(upper,ikCtrlList[0])
            ikloc[0].rename(About+'_upper_'+ikType+'Loc')
            ikloc[1].rename(About+'_lower_'+ikType+'Loc')
            stretchyMD1 = self.MultiplyDivideNode(1,self.chrSize,Spacing,None,Channel=1)
            stretchyMD2 = self.MultiplyDivideNode(1,self.chrSize,Spacing,None,Channel=1)
            stretchyMD3 = self.MultiplyDivideNode(2,distShapes+'.distance',stretchyMD2+'.outputX',None,Channel=1)    
            stretchyCN1 = self.conditionNode(3,distShapes+'.distance',stretchyMD1+'.outputX',stretchyMD3+'.outputX',1,None,Channel=1)    
            stretchyBC1 = self.blendColorNode(ikfkSwitch+'.Auto_IK_Stretchy',stretchyCN1+'.outColorR',1,None,Channel=1)
            stretchyBC2 = self.blendColorNode(ikfkSwitch+'.ikfk',stretchyBC1+'.outputR',fkCtrlList[0]+'.Stretchy',upper+'.scaleX',Channel=1)
            stretchyBC3 = self.blendColorNode(ikfkSwitch+'.ikfk',stretchyBC1+'.outputR',fkCtrlList[1]+'.Stretchy',lower+'.scaleX',Channel=1)
            pm.connectAttr(stretchyBC2+'.outputR',ikList[0]+'.scaleX')
            pm.connectAttr(stretchyBC3+'.outputR',ikList[1]+'.scaleX')
            #upperSkin and axisSkin
            axisSkinJt=pm.duplicate(lower,po=1,n=lower+'_BendJt_0')[0]
            pm.parentConstraint(upperCtrl3,axisSkinJt)
            pm.parent(axisSkinJt,w=1)
            upperSkinJt=pm.duplicate(upper,po=1,n=upper+'_BendJt_0')[0]
            pm.parent(upperSkinJt,w=1)
            pm.parentConstraint(upper,upperSkinJt)
            #IK擠壓功能
            lengthCvs = pm.curve(d=1,n=upper+'_length',ep=(upper.getTranslation(space='world'),end.getTranslation(space='world')))
            lengthCvsInfo = pm.arclen(lengthCvs,ch=1)
            SqiashCN1 = self.conditionNode(2,distShapes+'.distance',lengthCvsInfo+'.arcLength',distShapes+'.distance',Spacing,None,Channel=1)
            SqiashMD1 = self.MultiplyDivideNode(1,self.chrSize,Spacing,SqiashCN1+'.secondTerm',Channel=1)
            SqiashPMA1 = self.plusMinusAverageNode(1,SqiashCN1+'.outColorR',Spacing*-1,None,Channel=1)
            SqiashMD2 = self.MultiplyDivideNode(1,self.chrSize,Spacing,None,Channel=1)
            SqiashMD3 = self.MultiplyDivideNode(2,[SqiashPMA1+'.output1D',SqiashPMA1+'.output1D',SqiashPMA1+'.output1D'],[SqiashMD2+'.outputX',SqiashMD2+'.outputX',SqiashMD2+'.outputX'],None,Channel=3)
            SqiashMD4 = self.MultiplyDivideNode(1,[-0.3,-0.25,-0.2],[ikfkSwitch+'.Auto_Sqiash_Stretchy_Width',ikfkSwitch+'.Auto_Sqiash_Stretchy_Width',ikfkSwitch+'.Auto_Sqiash_Stretchy_Width'],None,Channel=3)
            SqiashMD5 = self.MultiplyDivideNode(1,[-0.15,-0.1,1],[ikfkSwitch+'.Auto_Sqiash_Stretchy_Width',ikfkSwitch+'.Auto_Sqiash_Stretchy_Width',ikfkSwitch+'.Auto_Sqiash_Stretchy_Width'],None,Channel=3)
            SqiashMD6 = self.MultiplyDivideNode(1,SqiashMD3+'.output',SqiashMD4+'.output',None)
            SqiashMD7 = self.MultiplyDivideNode(1,SqiashMD3+'.output',SqiashMD5+'.output',None)
            SqiashPMA2 = self.plusMinusAverageNode(1,SqiashMD6+'.output',[1,1,1],None)
            SqiashPMA3 = self.plusMinusAverageNode(1,SqiashMD7+'.output',[1,1,1],None)
            SqiashBC1 = self.blendColorNode(ikfkSwitch+'.ikfk',SqiashPMA2+'.output3D',[1,1,1],None)
            SqiashBC2 = self.blendColorNode(ikfkSwitch+'.ikfk',SqiashPMA3+'.output3D',[1,1,1],None)
            SqiashBC3 = self.blendColorNode(ikfkSwitch+'.Auto_Sqiash_Stretchy',SqiashBC1+'.output',[1,1,1],None)
            SqiashBC4 = self.blendColorNode(ikfkSwitch+'.Auto_Sqiash_Stretchy',SqiashBC2+'.output',[1,1,1],None)
            SqiashMD8 = self.MultiplyDivideNode(1,[ikfkSwitch+'.'+ikType+'_width',ikfkSwitch+'.'+ikType+'_width',ikfkSwitch+'.'+ikType+'_width'],[SqiashBC3+'.outputR',SqiashBC3+'.outputG',SqiashBC1+'.outputB'],None,Channel=3)
            SqiashMD9 = self.MultiplyDivideNode(1,[ikfkSwitch+'.'+ikType+'_width',ikfkSwitch+'.'+ikType+'_width'],[SqiashBC4+'.outputR',SqiashBC4+'.outputG'],None,Channel=2)
            Sqiash_upper1 = self.plusMinusAverageNode(1,[1,SqiashMD8+'.outputY',SqiashMD8+'.outputY'],[1,upperCtrl1+'.scaleY',upperCtrl1+'.scaleZ'],None,Channel=3)
            Sqiash_upper2 = self.plusMinusAverageNode(1,[1,SqiashMD8+'.outputZ',SqiashMD8+'.outputZ'],[1,upperCtrl1+'.scaleY',upperCtrl1+'.scaleZ'],None,Channel=3)
            Sqiash_upper3 = self.plusMinusAverageNode(1,[1,SqiashMD9+'.outputX',SqiashMD9+'.outputX'],[1,upperCtrl2+'.scaleY',upperCtrl2+'.scaleZ'],None,Channel=3)
            Sqiash_upper4 = self.plusMinusAverageNode(1,[1,SqiashMD9+'.outputY',SqiashMD9+'.outputY'],[1,upperCtrl2+'.scaleY',upperCtrl2+'.scaleZ'],None,Channel=3)
            Sqiash_axis = self.plusMinusAverageNode(1,[1,SqiashMD8+'.outputX',SqiashMD8+'.outputX'],[1,upperCtrl3+'.scaleY',upperCtrl3+'.scaleZ'],None,Channel=3)
            Sqiash_lower1 = self.plusMinusAverageNode(1,[1,SqiashMD9+'.outputY',SqiashMD9+'.outputY'],[1,lowerCtrl2+'.scaleY',lowerCtrl2+'.scaleZ'],None,Channel=3)
            Sqiash_lower2 = self.plusMinusAverageNode(1,[1,SqiashMD9+'.outputX',SqiashMD9+'.outputX'],[1,lowerCtrl2+'.scaleY',lowerCtrl2+'.scaleZ'],None,Channel=3)
            Sqiash_lower3 = self.plusMinusAverageNode(1,[1,SqiashMD8+'.outputY',SqiashMD8+'.outputY'],[1,lowerCtrl1+'.scaleY',lowerCtrl1+'.scaleZ'],None,Channel=3)
            Sqiash_lower4 = self.plusMinusAverageNode(1,[1,SqiashMD8+'.outputZ',SqiashMD8+'.outputZ'],[1,lowerCtrl1+'.scaleY',lowerCtrl1+'.scaleZ'],None,Channel=3)
            Sqiash_grp = Sqiash_upper1,Sqiash_upper2,Sqiash_upper3,Sqiash_upper4,Sqiash_axis,Sqiash_lower1,Sqiash_lower2,Sqiash_lower3,Sqiash_lower4
            for x in Sqiash_grp:
                x.setAttr('input3D[2]',[-1,-1,-1])
            lowerSpJt.reverse()
            z = len(lowerSpJt)
            SqiashGrp01 = lowerSpJt[-1],axisSkinJt
            for i in range(2):
                pm.connectAttr(Sqiash_axis+'.output3Dy',SqiashGrp01[i]+'.scaleY')
                pm.connectAttr(Sqiash_axis+'.output3Dz',SqiashGrp01[i]+'.scaleZ')
            if z>=3:
                pm.connectAttr(Sqiash_lower1+'.output3Dy',lowerSpJt[1]+'.scaleY')
                pm.connectAttr(Sqiash_lower1+'.output3Dz',lowerSpJt[1]+'.scaleZ')
                pm.connectAttr(Sqiash_upper1+'.output3Dy',upperSpJt[1]+'.scaleY')
                pm.connectAttr(Sqiash_upper1+'.output3Dz',upperSpJt[1]+'.scaleZ')
                if z>=4:
                    pm.connectAttr(Sqiash_lower2+'.output3Dy',lowerSpJt[2]+'.scaleY')
                    pm.connectAttr(Sqiash_lower2+'.output3Dz',lowerSpJt[2]+'.scaleZ')
                    pm.connectAttr(Sqiash_upper2+'.output3Dy',upperSpJt[2]+'.scaleY')
                    pm.connectAttr(Sqiash_upper2+'.output3Dz',upperSpJt[2]+'.scaleZ')
                    if z>=5:
                        pm.connectAttr(Sqiash_lower3+'.output3Dy',lowerSpJt[3]+'.scaleY')
                        pm.connectAttr(Sqiash_lower3+'.output3Dz',lowerSpJt[3]+'.scaleZ')
                        pm.connectAttr(Sqiash_upper3+'.output3Dy',upperSpJt[3]+'.scaleY')
                        pm.connectAttr(Sqiash_upper3+'.output3Dz',upperSpJt[3]+'.scaleZ')
                        if z>=6:
                            pm.connectAttr(Sqiash_lower4+'.output3Dy',lowerSpJt[4]+'.scaleY')
                            pm.connectAttr(Sqiash_lower4+'.output3Dz',lowerSpJt[4]+'.scaleZ')
                            pm.connectAttr(Sqiash_upper4+'.output3Dy',upperSpJt[4]+'.scaleY')
                            pm.connectAttr(Sqiash_upper4+'.output3Dz',upperSpJt[4]+'.scaleZ')
            lowerSpJt.reverse()
            #UpLo_Stretchy
            UpLoStretchyMD1 = self.MultiplyDivideNode(2,[ikfkSwitch+'.'+ikType+'_Stretchy',ikfkSwitch+'.Upper_'+ikType+'_Stretchy',ikfkSwitch+'.Lower_'+ikType+'_Stretchy'],[10,10,10],None,Channel=3)
            UpLoStretchyPMA1 = self.plusMinusAverageNode(1,[UpLoStretchyMD1+'.outputX',UpLoStretchyMD1+'.outputX'],[UpLoStretchyMD1+'.outputY',UpLoStretchyMD1+'.outputZ'],None,Channel=2)
            if About=='L':
                UpLoStretchyMD2 = self.MultiplyDivideNode(1,[UpLoStretchyPMA1+'.output3D.output3Dx',UpLoStretchyPMA1+'.output3D.output3Dy'],[10,10],None,Channel=2)
                UpLoStretchyPMA2 = self.plusMinusAverageNode(1,[UpLoStretchyMD2+'.outputX',UpLoStretchyMD2+'.outputY'],[lowerDist,endDist],None,Channel=2)
            if About=='R':
                UpLoStretchyMD2 = self.MultiplyDivideNode(1,[UpLoStretchyPMA1+'.output3D.output3Dx',UpLoStretchyPMA1+'.output3D.output3Dy'],[-10,-10],None,Channel=2)
                UpLoStretchyPMA2 = self.plusMinusAverageNode(1,[UpLoStretchyMD2+'.outputX',UpLoStretchyMD2+'.outputY'],[lowerDist,endDist],None,Channel=2)
            UpLoStretchyPMA3 = self.plusMinusAverageNode(1,UpLoStretchyPMA2+'.output3Dx',UpLoStretchyPMA2+'.output3Dy',None,Channel=1)
            UpLoStretchyMD3 = self.MultiplyDivideNode(2,Spacing,UpLoStretchyPMA3+'.output1D',None,Channel=1)
            UpLoStretchyCN1 = self.clampNode(UpLoStretchyMD3+'.outputX',5,1,None,Channel=1)
            UpLoStretchyMD4 = self.MultiplyDivideNode(1,[UpLoStretchyPMA2+'.output3Dx',UpLoStretchyPMA2+'.output3Dy'],[UpLoStretchyCN1+'.outputR',UpLoStretchyCN1+'.outputR'],None,Channel=2)
            pm.connectAttr(UpLoStretchyMD4+'.outputX',ikList[1]+'.translateX')
            pm.connectAttr(UpLoStretchyMD4+'.outputY',ikList[2]+'.translateX')
            pm.connectAttr(ikList[1]+'.translateX',jt[1]+'.translateX')
            pm.connectAttr(ikList[2]+'.translateX',jt[2]+'.translateX')
            #Arc
            ArcMD1 = self.MultiplyDivideNode(1,[self.chrSize,self.chrSize,self.chrSize],[Spacing,Spacing,Spacing],None,Channel=3)
            ArcMD2 = self.MultiplyDivideNode(2,distShapes+'.distance',ArcMD1+'.outputX',None,Channel=1)
            ArcRN1 = self.reverseNode(ArcMD2+'.outputX',None,Channel=1)
            ArcCN1 = self.clampNode(ArcRN1+'.outputX',1,0,None,Channel=1)
            ArcMD3 = self.MultiplyDivideNode(1,ikCtrlList[0]+'.Arc',-1,None,Channel=1)
            ArcMD4 = self.MultiplyDivideNode(1,ArcCN1+'.outputR',ArcMD3+'.outputX',None,Channel=1)
            upperConsList = upperCons1[0],upperCons2[0]
            lowerConsList = lowerCons1[0],lowerCons2[0]
            for i in range(2):
                pm.connectAttr(ArcMD4+'.outputX',upperConsList[i]+'.translateZ')
            for j in range(2):
                pm.connectAttr(ArcMD4+'.outputX',lowerConsList[j]+'.translateZ')
            #Elobow_Lock
            pvNull = pm.group(em=1)
            pm.parent(pvNull,lower)
            pvNull.setAttr('translate',[0,0,0])
            pvNull.setAttr('rotate',[0,0,0])
            Elobow_LockParcon = pm.parentConstraint(pv[0],pvNull,upperCons3[0])
            if ikType == 'arm':
                self.addSwitch(pv[0],name='Elobow_Lock',at='float',dv=0,min=0,max=1,k=1)
                ElobowLockMD1 = self.MultiplyDivideNode(1,pv[0]+'.Elobow_Lock',ikfkSwitch+'.ikfk',Elobow_LockParcon+'.'+pv[0]+'W0',Channel=1)
            if ikType == 'leg':
                self.addSwitch(pv[0],name='Knee_Lock',at='float',dv=0,min=0,max=1,k=1)
                ElobowLockMD1 = self.MultiplyDivideNode(1,pv[0]+'.Knee_Lock',ikfkSwitch+'.ikfk',Elobow_LockParcon+'.'+pv[0]+'W0',Channel=1)
            ElobowLockRN1 = self.reverseNode(Elobow_LockParcon+'.'+pv[0]+'W0',None,Channel=1)
            pm.connectAttr(ElobowLockRN1+'.outputX',Elobow_LockParcon+'.'+pvNull+'W1')
            #upper_lower_twistCtrl
            upperTwistLoc = pm.group(em=1,n=upper+'_upperTwist')
            lowerTwistLoc = pm.group(em=1,n=lower+'_lowerTwist')
            self.betweenConstraint(upperSpJt[0],upperSpJt[-1],upperTwistLoc,upperCtrl3,part=1,delParcon=1,type='parent')
            self.betweenConstraint(lowerSpJt[0],lowerSpJt[-1],lowerTwistLoc,upperCtrl3,part=1,delParcon=1,type='parent')
            upperTwistCtrl = self.ctrlGrp(upperTwistLoc,size=0.3*self.gbScale,parent=0,lock=['tx','ty','tz','ry','rz','sx','sy','sz','v'],ctrlType='180Thin')
            lowerTwistCtrl = self.ctrlGrp(lowerTwistLoc,size=0.3*self.gbScale,parent=0,lock=['tx','ty','tz','ry','rz','sx','sy','sz','v'],ctrlType='180Thin')
            pm.delete(upperTwistLoc,lowerTwistLoc)
            if About=='L':
                tParCon1,tAimCon1 = self.betweenConstraint(upperSpJt[0],upperSpJt[-1],upperTwistCtrl[0][1],upperCtrl3,part=1,type='point',Vector=[0,0,1])
                tParCon2,tAimCon2 = self.betweenConstraint(lowerSpJt[0],lowerSpJt[-1],lowerTwistCtrl[0][1],tip,part=1,type='point',Vector=[0,0,1])
                pm.delete(tAimCon1,tAimCon2)
                pm.orientConstraint(upper,upperTwistCtrl[0][1],mo=0,o=[180,0,0])
                pm.orientConstraint(lower,lowerTwistCtrl[0][1],mo=0,o=[180,0,0])
            if About=='R':
                tParCon1,tAimCon1 = self.betweenConstraint(upperSpJt[0],upperSpJt[-1],upperTwistCtrl[0][1],upperCtrl3,part=1,type='point',Vector=[0,0,-1])
                tParCon2,tAimCon2 = self.betweenConstraint(lowerSpJt[0],lowerSpJt[-1],lowerTwistCtrl[0][1],tip,part=1,type='point',Vector=[0,0,-1])
                pm.delete(tAimCon1,tAimCon2)
                pm.orientConstraint(upper,upperTwistCtrl[0][1],mo=0,o=[360,0,0])
                pm.orientConstraint(lower,lowerTwistCtrl[0][1],mo=0,o=[360,0,0])
            twistCtrlList = upperTwistCtrl[1],lowerTwistCtrl[1]
            pm.connectAttr(ikfkSwitch+'.twist_Display',lowerTwistCtrl[0][1]+'.visibility')
            pm.connectAttr(ikfkSwitch+'.twist_Display',upperTwistCtrl[0][1]+'.visibility')
            #IKFKAutoArmTwist
            #upperTwis 
            upperIk[0].setAttr('dTwistControlEnable',1)
            if About=='L':
                pm.connectAttr(upperTwistCtrl[1]+'.rotateX',upperIk[0]+'.twist')
            if About=='R':
                self.MultiplyDivideNode(1,upperTwistCtrl[1]+'.rotateX',-0.5,upperIk[0]+'.twist',Channel=1)
            upperIk[0].setAttr('dWorldUpType',4)
            upperIk[0].setAttr('dWorldUpAxis',0)
            upperIk[0].setAttr('dWorldUpVector',[0,1,0])
            upperIk[0].setAttr('dWorldUpVectorEnd',[0,1,0])
            pm.connectAttr(upper+'.worldMatrix',upperIk[0]+'.dWorldUpMatrix')
            pm.connectAttr(lower+'.worldMatrix',upperIk[0]+'.dWorldUpMatrixEnd')
            #lowerTwist
            endJt1=pm.duplicate(lower,po=1,n=tip+'_end1')[0]
            endJt2=pm.duplicate(lower,po=1,n=tip+'_end2')[0]
            self.snap(tip,endJt1,rot=0,scl=0,pivots=0)
            self.snap(tip,endJt2,rot=0,scl=0,pivots=0)
            pm.parent(endJt1,endJt2,lower)
            endJt1.setAttr('drawStyle',2)
            endJt2.setAttr('drawStyle',2)
            if About=='L':
                pm.setAttr(endJt2+'.translateX',endDist/3+endJt2.translateX.get())
            if About=='R':
                pm.setAttr(endJt2+'.translateX',(endDist*-1)/3+endJt2.translateX.get())
            pm.parent(endJt1,tip)
            pm.parent(endJt2,endJt1)
            twistNonroll=self.splineIkJoint(endJt1,endJt2,number=2,name='_nonroll_1')
            twistAux = self.splineIkJoint(endJt1,endJt2,number=3,name='_aux_1')
            NonrollIk = pm.ikHandle(sj=twistNonroll[0],ee=twistNonroll[-1],n=twistNonroll[0]+'_nonrollIk',sol='ikSplineSolver')
            AuxIk = pm.ikHandle(sj=twistAux[0],ee=twistAux[-1],n=twistAux[0]+'_auxIk',sol='ikSplineSolver')
            twistIkCvs = NonrollIk,AuxIk
            for i in twistIkCvs:
                pm.parent(i[2],tip)
                pm.parent(i[0],lowerSpJtGrp)
                for j in range(3):
                    i[j].setAttr('v',0)
            pm.parent(twistNonroll[0],twistAux[0],lowerSpJtGrp)       
            AuxIk[0].setAttr('dTwistControlEnable',1)
            if About=='L':
                lowerTwistPMA1 = self.plusMinusAverageNode(1,twistAux[1]+'.rotateX',lowerTwistCtrl[1]+'.rotateX',lowerIk[0]+'.twist',Channel=1)
            if About=='R':
                R_lowerTwistMD1 = self.MultiplyDivideNode(1,lowerTwistCtrl[1]+'.rotateX',-1,None,Channel=1)
                lowerTwistPMA1 = self.plusMinusAverageNode(1,twistAux[1]+'.rotateX',R_lowerTwistMD1+'.outputX',lowerIk[0]+'.twist',Channel=1)
            AuxIk[0].setAttr('dWorldUpType',4)
            AuxIk[0].setAttr('dWorldUpAxis',0)
            upper.setAttr('drawStyle',2)
            lower.setAttr('drawStyle',2)
            end.setAttr('drawStyle',2)
            endJt2.setAttr('drawStyle',2)
            AuxIk[0].setAttr('dWorldUpVector',[0,1,0])
            AuxIk[0].setAttr('dWorldUpVectorEnd',[0,1,0])
            if ikType=='leg':
                matchJt[-1].setAttr('drawStyle',2)
            pm.connectAttr(twistNonroll[0]+'.worldMatrix',AuxIk[0]+'.dWorldUpMatrix')
            pm.connectAttr(tip+'.worldMatrix',AuxIk[0]+'.dWorldUpMatrixEnd')
        else:
            if JtNumber[1] == 2:
                pass
            else:
                self.addTwistJoint(jt,JtNumber[1],ikType=ikType)
            bendCtrlList = None
            twistCtrlList = None
            end.setAttr('drawStyle',2)
            fkCtrlList[0].deleteAttr('Stretchy')
            fkCtrlList[1].deleteAttr('Stretchy')
            if ikType == 'leg':
                matchJt[-1].setAttr('drawStyle',2)
        #setGroup
        try:
            data_grp = pm.group(lengthCvs,ikloc[0],ikloc[1],upperCrv,\
                lowerCrv,distShapes,worldLoc,n=self.chrName+'_'+About+'_'+ikType+'_data_grp')
            skinJt_grp = pm.group(axisSkinJt,upperSkinJt,upperSpJtGrp,\
                lowerSpJtGrp,upperBendCtrlList[0],lowerBendCtrlList[-1],\
                n=self.chrName+'_'+About+'_'+ikType+'_skinJt_grp')
        except:
            data_grp = worldLoc
            skinJt_grp = None
        ikCtrlList += pv
        try:
            ikList.append(PvUpperJt)
        except:
            pass
        return ikCtrlList,fkCtrlList,bendCtrlList,twistCtrlList,ikfkSwitch,ikList,fkList,skinJt_grp,data_grp,worldLoc

    def armLegDoCtrl(self,tgt,About='',Ankle=None,JtNumber=[6,6],bend=1):
        try:
            loc = Ankle
        except:
            pass
        if len(tgt)==6:
            ikCtrlList,fkCtrlList,bendCtrlList,twistCtrlList,ikfkSwitch,ikList,fkList,skinJt_grp,data_grp,worldLoc = \
                self.ikfkFunction(tgt,ikType='leg',About=About,loc=loc,JtNumber=JtNumber,bend=bend)
        if len(tgt)==4:
            ikCtrlList,fkCtrlList,bendCtrlList,twistCtrlList,ikfkSwitch,ikList,fkList,skinJt_grp,data_grp,worldLoc = \
                self.ikfkFunction(tgt,ikType='arm',About=About,JtNumber=JtNumber,bend=bend)
        pm.select(cl=1)
        return ikCtrlList,fkCtrlList,bendCtrlList,twistCtrlList,ikfkSwitch,ikList,fkList,skinJt_grp,data_grp,worldLoc

    def spinalDoCtrl(self,jts,JtNumber=7,bend=1,unity=1):
        pelvis = jts[0]
        pelvisUp = jts[1]
        pelvisDown = jts[2]
        chest = jts[3]
        hip = jts[4]
        #splineJoints
        if bend == 1:
            splineJts = self.splineIkJoint(pelvisUp,chest,number=JtNumber,name='_Spinal_1')
            splineIk = pm.ikHandle(sj=splineJts[0],ee=splineJts[-1],n=splineJts[0]+'_splineIk',sol='ikSplineSolver')
            splineIk[2].rename('spinalIk_curve')
            pm.parent(splineIk[2],w=1)
            splineIk[0].setAttr('v',0)
            clu1 = pm.cluster(splineIk[2]+'.cv[3]')[1]
            clu2 = pm.cluster(splineIk[2]+'.cv[1]',splineIk[2]+'.cv[2]')[1]
            clu3 = pm.cluster(splineIk[2]+'.cv[0]')[1]
            clu1.setAttr('v',0)
            clu2.setAttr('v',0)
            clu3.setAttr('v',0)
            splineCrv = splineIk[2].listRelatives(shapes=1)[0]
            splineCv=splineCrv.getCVs()
            splineCvsInfo=pm.arclen(splineIk[2],ch=1)
            #CtrlSet
            ctrlAxis = self.getTgtAttr(pelvisUp)[1]
            nrDict = {'X':'circleX','Y':'circleY','Z':'circleZ'}
            nr = nrDict[ctrlAxis]
            pelvisGrps,pelvisCtrl,pelvisParCon1,pelvisParCon2 = self.ctrlGrp(pelvis,size=1*self.gbScale,parent=0,ctrlType='arCircle',rotateOrder=1)
            pelvisGrps[1].setAttr('rotate',[180,0,90])
            splineGrps,splineCtrl,splineParCon1,splineParCon2 = self.ctrlGrp(pelvisUp,size=0.85*self.gbScale,parent=0,ctrlType='arCircle',rotateOrder=1)
            splineReName = splineGrps[0],splineGrps[1],splineCtrl
            for x in splineReName:
                x.rename(x.replace("upPelvis","spline"))
            pelvisUpGrps,pelvisUpCtrl,pelvisUpParCon1,pelvisUpParCon2 = self.ctrlGrp(pelvisUp,size=self.gbScale,depth=-0.3,parent=0,ctrlType='pyramid',rotateOrder=1)
            pelvisDownGrps,pelvisDownCtrl,pelvisDownParCon1,pelvisDownParCon2 = self.ctrlGrp(pelvisDown,size=self.gbScale,depth=0.3,parent=0,ctrlType='pyramid',rotateOrder=1)
            chestGrps,chestCtrl,chestParCon1,chestParCon2 = self.ctrlGrp(chest,size=0.75*self.gbScale,parent=0,ctrlType='arCircle',rotateOrder=1)
            hipGrps,hipCtrl,hipParCon1,hipParCon2 = self.ctrlGrp(hip,size=0.85*self.gbScale,parent=0,ctrlType=nr,rotateOrder=1)
            pelvisUp_tran = pelvisUp.getTranslation(space='world')
            chest_tran = chest.getTranslation(space='world')
            spline_tran = ((chest_tran-pelvisUp_tran)/2)+pelvisUp_tran
            splineGrps[1].setTranslation(spline_tran,space='world')
            spinalCtrls = pelvisCtrl,pelvisUpCtrl,splineCtrl,pelvisDownCtrl,chestCtrl
            for x in spinalCtrls:
                x.setAttr('rotateX',-180)
                x.setAttr('rotateZ',90)
                pm.makeIdentity(x,r=1,a=1)
            pm.parent(splineIk[0],pelvisUpCtrl)
            pm.parent(clu1,chestCtrl)
            pm.parent(clu2,splineCtrl)
            pm.parent(clu3,pelvisUpCtrl)
            pm.parent(chestGrps[1],splineCtrl)
            pm.parent(splineGrps[1],hipGrps[1],pelvisUpCtrl)
            pm.parent(hipGrps[1],pelvisDownCtrl)
            pm.parent(pelvisUpGrps[1],pelvisDownGrps[1],pelvisCtrl)
            #產生額外頻道
            Switch1 = ('Auto_Stretchy','Auto_Sqiash_Stretchy')
            Switch2 = ('Auto_Sqiash_Stretchy_Width','Chest_Width')
            for i in Switch1:
                self.addSwitch(chestCtrl,name=i,at='float',dv=1,min=0,max=1)
            for j in Switch2:
                self.addSwitch(chestCtrl,name=j,at='float',dv=1,min=0,max=10)
            self.addSwitch(pelvisCtrl,name='sub_ctrl',at='float',dv=0,min=0,max=1)
            pelvisCtrl.setAttr('sub_ctrl',keyable=0,channelBox=1)
            #sub_ctrl顯示
            pm.connectAttr(pelvisCtrl+'.sub_ctrl',pelvisUpCtrl.listRelatives(c=1)[0]+'.visibility')
            pm.connectAttr(pelvisCtrl+'.sub_ctrl',pelvisDownCtrl.listRelatives(c=1)[0]+'.visibility')
            #旋轉
            splineIk[0].setAttr('dTwistControlEnable',1)
            splineIk[0].setAttr('dWorldUpType',4)
            splineIk[0].setAttr('dWorldUpAxis',3)
            splineIk[0].setAttr('dWorldUpVector',[0,0,1])
            splineIk[0].setAttr('dWorldUpVectorEnd',[0,0,1])
            pm.connectAttr(pelvisUpCtrl+'.worldMatrix',splineIk[0]+'.dWorldUpMatrix')
            pm.connectAttr(chestCtrl+'.worldMatrix',splineIk[0]+'.dWorldUpMatrixEnd')
            #拉長
            splineLength = splineCvsInfo.arcLength.get()
            splineMD1 = self.MultiplyDivideNode(1,self.chrSize,splineLength,None,Channel=1)
            splineMD2 = self.MultiplyDivideNode(2,splineCvsInfo+'.arcLength',splineMD1+'.outputX',None,Channel=1)
            splineBC1 = self.blendColorNode(chestCtrl+'.Auto_Stretchy',splineMD2+'.outputX',1,None,Channel=1)
            for i in range(len(splineJts)):
                pm.connectAttr(splineBC1+'.outputR',splineJts[i]+'.scaleX')
            #拉伸擠壓
            lengthCvs = pm.curve(d=1,n=chest+'_length',ep=(pelvisUp.getTranslation(space='world'),chest.getTranslation(space='world')))
            lengthCvsInfo = pm.arclen(lengthCvs,ch=1)
            splineSqiashCN1 = self.conditionNode(2,splineCvsInfo+'.arcLength',lengthCvsInfo+'.arcLength',splineCvsInfo+'.arcLength',splineLength,None,Channel=1)
            splineSqiashCN2 = self.conditionNode(4,splineCvsInfo+'.arcLength',lengthCvsInfo+'.arcLength',splineCvsInfo+'.arcLength',splineLength,None,Channel=1)
            splineSqiashPMA1 = self.plusMinusAverageNode(1,splineSqiashCN1+'.outColorR',splineLength*-1,None,Channel=1)
            splineSqiashPMA2 = self.plusMinusAverageNode(1,splineSqiashCN2+'.outColorR',splineLength*-1,None,Channel=1)
            splineSqiashPMA3 = self.plusMinusAverageNode(1,splineSqiashPMA1+'.output1D',splineSqiashPMA2+'.output1D',None,Channel=1)
            splineSqiashMD2 = self.MultiplyDivideNode(1,self.chrSize,splineLength,None,Channel=1)
            splineSqiashMD3 = self.MultiplyDivideNode(2,[splineSqiashPMA3+'.output1D',splineSqiashPMA3+'.output1D',splineSqiashPMA3+'.output1D'],[splineSqiashMD2+'.outputX',splineSqiashMD2+'.outputX',splineSqiashMD2+'.outputX'],None,Channel=3)
            if JtNumber == 7:
                splineSqiashMD4 = self.MultiplyDivideNode(1,[-0.1,-0.2,-0.3],[chestCtrl+'.Auto_Sqiash_Stretchy_Width',chestCtrl+'.Auto_Sqiash_Stretchy_Width',chestCtrl+'.Auto_Sqiash_Stretchy_Width'],None,Channel=3)
            elif JtNumber == 5:
                splineSqiashMD4 = self.MultiplyDivideNode(1,[-0.15,0,-0.3],[chestCtrl+'.Auto_Sqiash_Stretchy_Width',chestCtrl+'.Auto_Sqiash_Stretchy_Width',chestCtrl+'.Auto_Sqiash_Stretchy_Width'],None,Channel=3)
            elif JtNumber == 3:
                splineSqiashMD4 = self.MultiplyDivideNode(1,[0,0,-0.3],[chestCtrl+'.Auto_Sqiash_Stretchy_Width',chestCtrl+'.Auto_Sqiash_Stretchy_Width',chestCtrl+'.Auto_Sqiash_Stretchy_Width'],None,Channel=3)
            else:
                pass
            splineSqiashMD5 = self.MultiplyDivideNode(1,splineSqiashMD3+'.output',splineSqiashMD4+'.output',None)
            splineSqiashPMA4 = self.plusMinusAverageNode(1,splineSqiashMD5+'.output',[1,1,1],None)
            splineSqiashBC1 = self.blendColorNode(chestCtrl+'.Auto_Sqiash_Stretchy',splineSqiashPMA4+'.output3D',[1,1,1],None)
            splineSqiashMD6 = self.MultiplyDivideNode(1,[chestCtrl+'.Chest_Width',chestCtrl+'.Chest_Width',chestCtrl+'.Chest_Width'],[splineSqiashBC1+'.outputR',splineSqiashBC1+'.outputG',splineSqiashBC1+'.outputB'],None,Channel=3)
            if JtNumber == 7:
                splineSqiashGrp01 = splineJts[1],splineJts[5]
                splineSqiashGrp02 = splineJts[2],splineJts[4]
                for i in range(2):
                    pm.connectAttr(splineSqiashMD6+'.outputX',splineSqiashGrp01[i]+'.scaleY')
                    pm.connectAttr(splineSqiashMD6+'.outputX',splineSqiashGrp01[i]+'.scaleZ')
                for j in range(2):
                    pm.connectAttr(splineSqiashMD6+'.outputY',splineSqiashGrp02[j]+'.scaleY')
                    pm.connectAttr(splineSqiashMD6+'.outputY',splineSqiashGrp02[j]+'.scaleZ')
                pm.connectAttr(splineSqiashMD6+'.outputZ',splineJts[3]+'.scaleY')
                pm.connectAttr(splineSqiashMD6+'.outputZ',splineJts[3]+'.scaleZ')
            if JtNumber == 5:
                splineSqiashGrp01 = splineJts[1],splineJts[3]
                for i in range(2):
                    pm.connectAttr(splineSqiashMD6+'.outputX',splineSqiashGrp01[i]+'.scaleY')
                    pm.connectAttr(splineSqiashMD6+'.outputX',splineSqiashGrp01[i]+'.scaleZ')
                pm.connectAttr(splineSqiashMD6+'.outputZ',splineJts[2]+'.scaleY')
                pm.connectAttr(splineSqiashMD6+'.outputZ',splineJts[2]+'.scaleZ')
            if JtNumber == 3:
                pm.connectAttr(splineSqiashMD6+'.outputZ',splineJts[1]+'.scaleY')
                pm.connectAttr(splineSqiashMD6+'.outputZ',splineJts[1]+'.scaleZ')
            pm.parentConstraint(pelvisCtrl,pelvis,mo=1)
            pm.parentConstraint(pelvisUpCtrl,pelvisUp,mo=1)
            pm.parentConstraint(hipCtrl,pelvisDown,mo=1)
            pm.orientConstraint(chestCtrl,chest,mo=1)
            pm.pointConstraint(splineJts[-1],chest,mo=1)
            #分類
            spinal_SkinJt_grp = pm.group(em=1,n=self.chrName+'_spinal_SkinJt_grp')
            splineJts[-1].setAttr('drawStyle',2)
            pelvis.setAttr('drawStyle',2)
            pelvisUp.setAttr('drawStyle',2)
            pelvisDown.setAttr('drawStyle',2)
            pm.parent(splineJts[0],spinal_SkinJt_grp)
            spinal_Data_grp = pm.group(splineIk[2],lengthCvs,n=self.chrName+'_spinal_data_grp')
            spinalCtrls = pelvisCtrl,pelvisUpCtrl,pelvisDownCtrl,chestCtrl,hipCtrl
        elif bend == 0:
            #轉正骨架
            pm.parent(chest,hip,w=1)
            try:
                breasts = chest.listRelatives()
                pm.parent(breasts[0],breasts[1],w=1)
            except:
                pass
            pelvis.setAttr('jointOrient',[0,0,0])
            chest.setAttr('jointOrient',[0,0,0])
            hip.setAttr('jointOrient',[0,0,0])
            try:
                pm.parent(breasts[0],breasts[1],chest)
            except:
                pass
            #架設控制器
            if unity == 1:
                pm.parent(chest,pelvis)
                pm.parent(pelvis,hip)
                pm.delete(pelvisUp,pelvisDown)
                self.jointOrient([pelvis,chest],[0,1,0],[0,0,-1],[0,1,0])
                pelvisGrps,pelvisCtrl,pelvisParCon1,pelvisParCon2 = self.ctrlGrp(pelvis,size=0.85*self.gbScale,ctrlType='arCircle',rotateOrder=1)
                chestGrps,chestCtrl,chestParCon1,chestParCon2 = self.ctrlGrp(chest,size=0.75*self.gbScale,ctrlType='arCircle',rotateOrder=1)
                hipGrps,hipCtrl,hipParCon1,hipParCon2 = self.ctrlGrp(hip,size=1*self.gbScale,ctrlType='arCircle',rotateOrder=1)
                pm.parent(chestGrps[1],pelvisCtrl)
                pm.parent(pelvisGrps[1],hipCtrl)
                spinalCtrls = hipCtrl,None,None,chestCtrl,None,hipCtrl
            elif unity == 0:
                spinalJt = pm.duplicate(pelvis,n=pelvis.replace('pelvis','spinal'),po=1)[0]
                chestTran = chest.getTranslation(space='world')
                pelvisTran = pelvis.getTranslation(space='world')
                spinalJt.setTranslation(((chestTran-pelvisTran)/2)+pelvisTran,space='world')
                pm.parent(chest,spinalJt)
                pm.delete(pelvisUp,pelvisDown)
                self.jointOrient([spinalJt,chest],[0,1,0],[0,0,-1],[0,1,0])
                pm.makeIdentity(pelvis,a=1)
                pelvis.setAttr('jointOrient',[0,0,0])
                pm.parent(spinalJt,hip,pelvis)
                pelvisGrps,pelvisCtrl,pelvisParCon1,pelvisParCon2 = self.ctrlGrp(pelvis,size=1*self.gbScale,ctrlType='arCircle',rotateOrder=1)
                spinalGrps,spinalCtrl,spinalParCon1,spinalParCon2 = self.ctrlGrp(spinalJt,size=0.85*self.gbScale,ctrlType='arCircle',rotateOrder=1)
                chestGrps,chestCtrl,chestParCon1,chestParCon2 = self.ctrlGrp(chest,size=0.75*self.gbScale,ctrlType='arCircle',rotateOrder=1)
                hipGrps,hipCtrl,hipParCon1,hipParCon2 = self.ctrlGrp(hip,size=0.85*self.gbScale,ctrlType='arCircle',rotateOrder=1)
                
                '''
                bodyCtrl = self.cvsCtrl(size=1*self.gbScale,name=self.chrName+'_body_ctrl',ctrlType='four_arrow')
                bodyUpper = pm.group(n=bodyCtrl+'_upper',em=1)
                bodyCons = pm.group(n=bodyCtrl+'_cons',em=1)
                pm.parent(bodyCtrl,bodyUpper)
                pm.parent(bodyUpper,bodyCons)
                '''

                pm.parent(chestGrps[1],spinalCtrl)
                pm.parent(spinalGrps[1],hipGrps[1],pelvisCtrl)
                spinalCtrls = pelvisCtrl,None,None,chestCtrl,hipCtrl
            spinal_SkinJt_grp = spinal_Data_grp = None
        return spinalCtrls,spinal_SkinJt_grp,spinal_Data_grp

    def neckDoCtrl(self,neck,head,JtNumber=3,bend=1):
        if bend == 1:
            neckJts = self.splineIkJoint(neck,head,number=JtNumber,name='_NeckJt_1')
            neckIk = pm.ikHandle(sj=neckJts[0],ee=neckJts[-1],n=neckJts[0]+'_neckIk',sol='ikSplineSolver')
            neckIk[2].rename('neckIk_curve')
            pm.parent(neckIk[2],w=1)
            neckIk[0].setAttr('v',0)
            clu1=pm.cluster(neckIk[2]+'.cv[2]',neckIk[2]+'.cv[3]')[1]
            clu2=pm.cluster(neckIk[2]+'.cv[0]',neckIk[2]+'.cv[1]')[1]
            clu1.setAttr('v',0)
            clu2.setAttr('v',0)
            neckCvsInfo=pm.arclen(neckIk[2],ch=1)
            #控制器
            ctrlAxis = self.getTgtAttr(neck)[1]
            nrDict = {'X':'circleX','Y':'circleY','Z':'circleZ'}
            nr = nrDict[ctrlAxis]
            neckGrps,neckCtrl,neckParCon1,neckParCon2 = self.ctrlGrp(neck,size=0.5*self.gbScale,parent=0,ctrlType=nr,rotateOrder=1)
            headGrps,headCtrl,headParCon1,headParCon2 = self.ctrlGrp(head,size=0.5*self.gbScale,parent=0,ctrlType=nr,rotateOrder=1)
            pm.parent(clu1,neckIk[0],headCtrl)
            pm.parent(clu2,neckCtrl)
            pm.parentConstraint(neckCtrl,neck)
            pm.parentConstraint(headCtrl,head)
            #旋轉
            neckIk[0].setAttr('dTwistControlEnable',1)
            neckIk[0].setAttr('dWorldUpType',4)
            neckIk[0].setAttr('dWorldUpAxis',3)
            neckIk[0].setAttr('dWorldUpVector',[0,0,1])
            neckIk[0].setAttr('dWorldUpVectorEnd',[0,0,1])
            pm.connectAttr(neckCtrl+'.worldMatrix',neckIk[0]+'.dWorldUpMatrix')
            pm.connectAttr(headCtrl+'.worldMatrix',neckIk[0]+'.dWorldUpMatrixEnd')
            #拉長
            neckLength = neckCvsInfo.arcLength.get()
            neckMD1 = self.MultiplyDivideNode(1,self.chrSize,neckLength,None,Channel=1)
            neckMD2 = self.MultiplyDivideNode(2,neckCvsInfo+'.arcLength',neckMD1+'.outputX',None,Channel=1)
            for i in range(len(neckJts)):
                pm.connectAttr(neckMD2+'.outputX',neckJts[i]+'.scaleX')
            #display
            neckJts[0].setAttr('drawStyle',2)
            neckJts[-1].setAttr('drawStyle',2)
            #分類
            head_data_grp = pm.group(neckIk[2],n=self.chrName+'_head_data_grp')
            head_skinJt_grp = pm.group(neckJts[0],n=self.chrName+'_head_skinJt_grp')
            neckCtrlGrp = neckCtrl,headCtrl
        else:
            ctrlAxis = self.getTgtAttr(neck)[1]
            nrDict = {'X':'circleX','Y':'circleY','Z':'circleZ'}
            nr = nrDict[ctrlAxis]
            neckGrps,neckCtrl,neckParCon1,neckParCon2 = self.ctrlGrp(neck,size=0.5*self.gbScale,parent=0,ctrlType=nr,rotateOrder=1)
            headGrps,headCtrl,headParCon1,headParCon2 = self.ctrlGrp(head,size=0.5*self.gbScale,parent=0,ctrlType=nr,rotateOrder=1)
            pm.parentConstraint(neckCtrl,neck)
            pm.parentConstraint(headCtrl,head)
            neckCtrlGrp = neckCtrl,headCtrl
            head_data_grp = head_skinJt_grp = None
        return neckCtrlGrp,head_skinJt_grp,head_data_grp

    def fingerConnection(self,fingerAxis,ctrlChannel,power):
        fingerCN = self.conditionNode(2,ctrlChannel,0,[power[0],power[0],power[0]],[power[1],power[1],power[1]],None,Channel=4)
        fingerMD = self.MultiplyDivideNode(1,ctrlChannel,fingerCN+'.outColorR',None,Channel=1)
        fingerPMA = self.plusMinusAverageNode(1,fingerMD+'.outputX',0,fingerAxis,Channel=1)
        return fingerPMA

    def fingerDoCtrl(self,fingers,axis='',About='',loc=None):
        nrDict = {'X':'rotateX','Y':'rotateY','Z':'rotateZ'}
        fingerLoc = loc
        nr=nrDict[axis]
        ctrlAxis = {'L':'fingerL','R':'fingerR'}
        ctrlType=ctrlAxis[About]
        ###fingerTipCtrl###
        fingerTipCtrl = self.cvsCtrl(size=0.1*self.gbScale,name=self.chrName+'_'+About+'_fingerTipCtrl',axis=None,ctrlType='sphere')
        if len(fingers[0].listRelatives(ad=1)) == 3:
            switch1 = [['Thumb_Base','Thumb_Mid','Thumb_Tip']]
        elif len(fingers[0].listRelatives(ad=1)) == 2:
            switch1 = [['Thumb_Base','Thumb_Tip']]
        switch1 += [['Index_Base','Index_Mid','Index_Tip'],['Middle_Base','Middle_Mid','Middle_Tip']\
            ,['Ring_Base','Ring_Mid','Ring_Tip'],['Little_Base','Little_Mid','Little_Tip']]
        switch2 = ('Thumb_Spread','Index_Spread','Middle_Spread','Ring_Spread','Little_Spread')
        switch3 = ('Thumb_Rotate','Index_Rotate','Middle_Rotate','Ring_Rotate','Little_Rotate')
        self.addSwitch(fingerTipCtrl,name='CURL',at='float',dv=0,min=0,max=1)
        fingerTipCtrl.setAttr('CURL',keyable=0,channelBox=1)
        for switch in switch1:
            for n in switch:
                self.addSwitch(fingerTipCtrl,name=n,at='float',dv=0,min=-10,max=10)
        self.addSwitch(fingerTipCtrl,name='SPREAD',at='float',dv=0,min=0,max=1)
        fingerTipCtrl.setAttr('SPREAD',keyable=0,channelBox=1)
        for switch in switch2:
            self.addSwitch(fingerTipCtrl,name=switch,at='float',dv=0,min=-10,max=10)
        self.addSwitch(fingerTipCtrl,name='ROTATE',at='float',dv=0,min=0,max=1)
        fingerTipCtrl.setAttr('ROTATE',keyable=0,channelBox=1)
        for switch in switch3:
            self.addSwitch(fingerTipCtrl,name=switch,at='float',dv=0,min=-10,max=10)
        self.snap(fingerLoc,fingerTipCtrl)
        ###setCtrl###
        fingerconsList = []
        fingerupperList = []
        fingerctrlList = []
        CurlPmaList = []
        for i in range(len(fingers)):
            finger = fingers[i].listRelatives(ad=1)
            finger.append(fingers[i])
            finger_jtList = finger[:0:-1]
            ctrlList,upperList,consList = self.setCtrl(finger_jtList,lock=['sx','sy','sz','v'],ctrlType=ctrlType,size=0.1*self.gbScale)
            self.addSwitch(ctrlList[0],name='sub_ctrl',at='long',dv=0,min=0,max=1)
            pm.connectAttr(ctrlList[0]+'.sub_ctrl',consList[1]+'.visibility')
            ctrlList[0].setAttr('sub_ctrl',keyable=0,channelBox=1)
            fingerconsList.append(consList)
            fingerupperList.append(upperList)
            fingerctrlList.append(ctrlList)
            for j in range(len(finger_jtList)-1):
                num = {0:'finger_1',1:'finger_2',2:'finger_3',3:'finger_4',4:'finger_5'}
                switchName=num[j]
                self.addSwitch(ctrlList[0],name=switchName,at='float',dv=0,min=-360,max=360)
        ###connectAttr###
        fourFinger = [fingerupperList[1],fingerupperList[2],fingerupperList[3],fingerupperList[4]]
        SpreadGrp = []
        CurlGrp = []
        CurlPmaList = []
        if len(fingerupperList[0]) == 3:
            thumbCurlGrp = [fingerupperList[0][0],fingerupperList[0][1],fingerupperList[0][2]]
            CurlGrp.append(thumbCurlGrp)
            SpreadGrp.append(fingerupperList[0][0])
        elif len(fingerupperList[0]) == 2:
            thumbCurlGrp = [fingerupperList[0][0],fingerupperList[0][1]]
            CurlGrp.append(thumbCurlGrp)
            SpreadGrp.append(fingerupperList[0][0])
        for upperList in fourFinger:
            if len(upperList) == 4:
                curl = []
                curl.append(upperList[1])
                curl.append(upperList[2])
                curl.append(upperList[3])
                CurlGrp.append(curl)
                SpreadGrp.append(upperList[1])
            elif len(upperList) == 3:
                curl = []
                curl.append(upperList[0])
                curl.append(upperList[1])
                curl.append(upperList[2])
                CurlGrp.append(curl)
                SpreadGrp.append(upperList[0])
        for Curl in range(len(CurlGrp)):
            CurlPmas = []
            for n in range(len(CurlGrp[Curl])):
                CurlPma = self.fingerConnection(CurlGrp[Curl][n]+'.rotateZ',fingerTipCtrl+'.'+switch1[Curl][n],(2,10))
                CurlPmas.append(CurlPma)
            CurlPmaList.append(CurlPmas)
        for Spread in range(len(SpreadGrp)):
            self.fingerConnection(SpreadGrp[Spread]+'.rotateY',fingerTipCtrl+'.'+switch2[Spread],(2,2))
        for Rotate in range(len(SpreadGrp)):
            self.fingerConnection(SpreadGrp[Rotate]+'.rotateX',fingerTipCtrl+'.'+switch3[Rotate],(2,2))
        if len(fingerupperList[0]) == 3:
            pm.connectAttr(fingerctrlList[0][0]+'.finger_1',CurlPmaList[0][1]+'.input1D[1]')
            pm.connectAttr(fingerctrlList[0][0]+'.finger_2',CurlPmaList[0][2]+'.input1D[1]')
        elif len(fingerupperList[0]) == 2:
            pm.connectAttr(fingerctrlList[0][0]+'.finger_1',CurlPmaList[0][1]+'.input1D[1]')
        fourFingerCtrls = [fingerctrlList[1],fingerctrlList[2],fingerctrlList[3],fingerctrlList[4]]
        fourPmaList = CurlPmaList[1],CurlPmaList[2],CurlPmaList[3],CurlPmaList[4]
        for ctrlLists in range(len(fourFingerCtrls)):
            if len(fourFingerCtrls[ctrlLists]) == 4:
                for n in range(3):
                    ChannelName = ('.finger_1','.finger_2','.finger_3')
                    pm.connectAttr(fourFingerCtrls[ctrlLists][0]+ChannelName[n],fourPmaList[ctrlLists][n]+'.input1D[1]')
            elif len(fourFingerCtrls[ctrlLists]) == 3:
                for n in range(2):
                    ChannelName = ('.finger_1','.finger_2')
                    pm.connectAttr(fourFingerCtrls[ctrlLists][0]+ChannelName[n],fourPmaList[ctrlLists][n+1]+'.input1D[1]')
        pm.select(cl=1)
        for finger in fingers:
            ch = finger.listRelatives(ad=1)
            ch[0].setAttr('drawStyle',2)
        return fingerTipCtrl,fingerconsList

    def breastDoCtrl(self,breastJt,breastMidJt,nippleJt):
        breast_curve = pm.curve(d=1,n=breastJt+'_curve',ep=(breastJt.getTranslation(space='world'),nippleJt.getTranslation(space='world')))
        breastIk = pm.ikHandle(sj=breastJt,ee=nippleJt,c=breast_curve,n=breastJt+'_ik',sol='ikSplineSolver',ccv=0,pcv=0)
        bottomBreastCtrl = self.ctrlGrp(breastJt,size=self.gbScale*0.3,parent=0,ctrlType='circleZ',lock=['rx','ry','rz','sx','sy','sz','v'])
        bottomBreastCtrl[0][0].rename(breastJt+'buttom_ctrl_upper')
        bottomBreastCtrl[0][1].rename(breastJt+'buttom_ctrl_cons')
        bottomBreastCtrl[1].rename(breastJt+'buttom_ctrl')
        breastCtrl = self.ctrlGrp(breastJt,size=self.gbScale*0.5,parent=0,ctrlType='circleZ',rotateOrder=1)
        nippleCtrl = self.ctrlGrp(nippleJt,size=self.gbScale*0.1,parent=0,ctrlType='circleZ',lock=['rx','ry','rz','sx','sy','sz','v'])
        pm.parent(bottomBreastCtrl[0][1],nippleCtrl[0][1],breastCtrl[1])
        self.addSwitch(bottomBreastCtrl[1],name='Auto_Stretchy',at='float',dv=1,min=0,max=1,k=0)
        self.addSwitch(bottomBreastCtrl[1],name='Auto_Sqiash_Stretchy',at='float',dv=1,min=0,max=1,k=0)
        breastIkCrv = breast_curve.listRelatives(shapes=1)[0]
        breastIkCv = breastIkCrv.getCVs()
        breastClu = pm.cluster(breast_curve+'.cv[0]')[1]
        nippleClu = pm.cluster(breast_curve+'.cv[1]')[1]
        breastClu.setAttr('visibility',0)
        nippleClu.setAttr('visibility',0)
        pm.parent(breastClu,bottomBreastCtrl[1])
        pm.parent(nippleClu,nippleCtrl[1])
        #拉伸
        breastIkCvsInfo = pm.arclen(breast_curve,ch=1)
        breastIkCvsInfo.rename(breastJt+'_IkCvsInfo')
        breastLength = breastIkCvsInfo.arcLength.get()
        breastMD1 = self.MultiplyDivideNode(1,self.chrSize,breastLength,None,Channel=1)
        breastMD2 = self.MultiplyDivideNode(2,breastIkCvsInfo+'.arcLength',breastMD1+'.outputX',None,Channel=1)
        breastBC1 = self.blendColorNode(bottomBreastCtrl[1]+'.Auto_Stretchy',breastMD2+'.outputX',1,None,Channel=1)
        pm.connectAttr(breastBC1+'.outputR',breastJt+'.scaleZ')
        pm.connectAttr(breastBC1+'.outputR',breastMidJt+'.scaleZ')
        #拉伸擠壓
        breast_lengthCvs = pm.curve(d=1,n=breastJt+'_length',ep=(breastJt.getTranslation(space='world'),nippleJt.getTranslation(space='world')))
        lengthCvsInfo = pm.arclen(breast_lengthCvs,ch=1)
        breastSqiashCN1 = self.conditionNode(2,breastIkCvsInfo+'.arcLength',lengthCvsInfo+'.arcLength',breastIkCvsInfo+'.arcLength',breastLength,None,Channel=1)
        breastSqiashCN2 = self.conditionNode(4,breastIkCvsInfo+'.arcLength',lengthCvsInfo+'.arcLength',breastIkCvsInfo+'.arcLength',breastLength,None,Channel=1)
        breastSqiashPMA1 = self.plusMinusAverageNode(1,breastSqiashCN1+'.outColorR',breastLength*-1,None,Channel=1)
        breastSqiashPMA2 = self.plusMinusAverageNode(1,breastSqiashCN2+'.outColorR',breastLength*-1,None,Channel=1)
        breastSqiashPMA3 = self.plusMinusAverageNode(1,breastSqiashPMA1+'.output1D',breastSqiashPMA2+'.output1D',None,Channel=1)
        breastSqiashMD2 = self.MultiplyDivideNode(1,self.chrSize,breastLength,None,Channel=1)
        breastSqiashMD3 = self.MultiplyDivideNode(2,[breastSqiashPMA3+'.output1D',breastSqiashPMA3+'.output1D',breastSqiashPMA3+'.output1D'],[breastSqiashMD2+'.outputX',breastSqiashMD2+'.outputX',breastSqiashMD2+'.outputX'],None,Channel=3)
        breastSqiashMD4 = self.MultiplyDivideNode(1,breastSqiashMD3+'.output',[0,0,-0.3],None)
        breastSqiashPMA4 = self.plusMinusAverageNode(1,breastSqiashMD4+'.output',[1,1,1],None)
        breastSqiashBC1 = self.blendColorNode(bottomBreastCtrl[1]+'.Auto_Sqiash_Stretchy',breastSqiashPMA4+'.output3D',[1,1,1],None)
        pm.connectAttr(breastSqiashBC1+'.outputB',breastMidJt+'.scaleX')
        pm.connectAttr(breastSqiashBC1+'.outputB',breastMidJt+'.scaleY')
        breast_data_grp = pm.group(breastIk[0],breast_curve,breast_lengthCvs,n=self.chrName+breastJt+'_grp')
        return breastCtrl[1],breast_data_grp

    def penisDoCtrl(self,bottom,mid,top):  
        bottom_1 = pm.duplicate(bottom,n=bottom+'_1',po=1)[0]
        bottom_2 = pm.duplicate(bottom,n=bottom+'_2',po=1)[0]
        bottom_3 = pm.duplicate(bottom,n=bottom+'_3',po=1)[0]
        tran_1 = bottom.getTranslation(space='object')
        tran_2 = mid.getTranslation(space='object')
        tran = (tran_2-tran_1)/3
        bottoms = bottom_1,bottom_2,bottom_3,bottom
        for x in range(len(bottoms)-1):
            pm.parent(bottoms[x],bottoms[x+1])
            bottoms[x].setAttr('translate',tran)
        pm.parent(mid,bottom_1)
        bottom_grps,bottom_ctrl = self.ctrlGrp(bottom,size=1.0*self.gbScale,parent=0,lock=['v'],ctrlType='circleZ',rotateOrder=1)[0:2]
        bottom_grps_2,bottom_ctrl_2 = self.ctrlGrp(bottom_2,size=1.0*self.gbScale,parent=0,lock=['rx','ry','rz','sx','sy','sz','v'],ctrlType='circleZ',rotateOrder=0)[0:2]
        bottom_grps_3,bottom_ctrl_3 = self.ctrlGrp(bottom_3,size=1.0*self.gbScale,parent=0,lock=['rx','ry','rz','sx','sy','sz','v'],ctrlType='circleZ',rotateOrder=0)[0:2]
        mid_grps,mid_ctrl = self.ctrlGrp(mid,size=1.0*self.gbScale,lock=['sx','sy','sz','v'],ctrlType='circleZ',rotateOrder=1)[0:2]
        top_grps,top_ctrl = self.ctrlGrp(top,size=0.5*self.gbScale,parent=0,lock=['rx','ry','rz','sx','sy','sz','v'],ctrlType='circleZ',rotateOrder=0)[0:2]
        pm.parent(top_grps[1],mid_ctrl)
        bottom_ik,bottom_cv,bottom_cvsInfo,bottom_crv = self.splineIkInfo(bottoms[-1::-1])
        top_ik,top_cv,top_cvsInfo,top_crv = self.splineIkInfo([mid,top])
        topClu_1 = pm.cluster(top_ik[2]+'.cv[2]',top_ik[2]+'.cv[3]')[1]
        topClu_2 = pm.cluster(top_ik[2]+'.cv[0]',top_ik[2]+'.cv[1]')[1]
        bottomClu_1 = pm.cluster(bottom_ik[2]+'.cv[3]')[1]
        bottomClu_2 = pm.cluster(bottom_ik[2]+'.cv[2]')[1]
        bottomClu_3 = pm.cluster(bottom_ik[2]+'.cv[1]')[1]
        bottomClu_4 = pm.cluster(bottom_ik[2]+'.cv[0]')[1]
        pm.parent(topClu_1,top_ctrl)
        pm.parent(bottomClu_1,topClu_2,mid_ctrl)
        pm.parent(bottomClu_2,bottom_ctrl_2)
        pm.parent(bottomClu_3,bottom_ctrl_3)
        pm.parent(bottomClu_4,bottom_ctrl)
        pm.parent(bottom_grps_2[1],bottom_grps_3[1],mid_grps[1],bottom_ctrl)
        AllClu = topClu_1,topClu_2,bottomClu_1,bottomClu_2,bottomClu_3,bottomClu_4
        for clu in AllClu:
            clu.hide()
        #Add Attrs
        self.addSwitch(mid_ctrl,name='twist',at='float',dv=0,min=-360,max=360,k=1)
        self.addSwitch(mid_ctrl,name='top_width',at='float',dv=1,min=0,max=10,k=1)
        self.addSwitch(mid_ctrl,name='bottom_width',at='float',dv=1,min=0,max=10,k=1)
        pm.connectAttr(mid_ctrl+'.twist',bottom_ik[0]+'.twist')
        #Bottom
        bottomSizeMD = pm.shadingNode('multiplyDivide',al=1)
        bottomCN = pm.shadingNode('condition',al=1)
        bottomMD = pm.shadingNode('multiplyDivide',al=1)
        bottomPlus = pm.shadingNode('plusMinusAverage',al=1)
        pm.connectAttr(bottom_cvsInfo+'.arcLength',bottomMD+'.input2X')
        pm.connectAttr(bottom_cvsInfo+'.arcLength',bottomMD+'.input2Y')
        pm.connectAttr(bottom_cvsInfo+'.arcLength',bottomMD+'.input1Z')
        bottomLength = bottom_cvsInfo.arcLength.get()
        bottomMD.setAttr('operation',2)
        bottomMD.setAttr('input1X',bottomLength)
        bottomMD.setAttr('input1Y',bottomLength)
        bottomMD.setAttr('input2Z',bottomLength)
        bottomCN.setAttr('operation',1)
        pm.connectAttr(bottomMD+'.output',bottomSizeMD+'.input1')
        pm.connectAttr(bottom_ctrl+'.scaleZ',bottomSizeMD+'.input2X')
        pm.connectAttr(bottom_ctrl+'.scaleZ',bottomSizeMD+'.input2Y')
        pm.connectAttr(bottom_cvsInfo+'.arcLength',bottomCN+'.firstTerm')
        pm.connectAttr(bottomSizeMD+'.output',bottomCN+'.colorIfTrue')
        pm.connectAttr(bottomCN+'.outColor',bottomPlus+'.input3D[0]')
        pm.connectAttr(mid_ctrl+'.bottom_width',bottomPlus+'.input3D[1].input3Dx')
        pm.connectAttr(mid_ctrl+'.bottom_width',bottomPlus+'.input3D[1].input3Dy')
        bottomPlus.setAttr('input3D[2].input3Dx',-1)
        bottomPlus.setAttr('input3D[2].input3Dy',-1)
        for jt in bottoms:
            pm.connectAttr(bottomPlus+'.output3D',jt+'.scale')
        #Top
        topSizeMD = pm.shadingNode('multiplyDivide',al=1)
        topCN = pm.shadingNode('condition',al=1)
        topMD = pm.shadingNode('multiplyDivide',al=1)
        topPlus = pm.shadingNode('plusMinusAverage',al=1)
        pm.connectAttr(top_cvsInfo+'.arcLength',topMD+'.input2X')
        pm.connectAttr(top_cvsInfo+'.arcLength',topMD+'.input2Y')
        pm.connectAttr(top_cvsInfo+'.arcLength',topMD+'.input1Z')
        topLength = top_cvsInfo.arcLength.get()
        topMD.setAttr('operation',2)
        topMD.setAttr('input1X',topLength)
        topMD.setAttr('input1Y',topLength)
        topMD.setAttr('input2Z',topLength)
        topCN.setAttr('operation',1)
        pm.connectAttr(topMD+'.output',topSizeMD+'.input1')
        pm.connectAttr(top_ctrl+'.scaleZ',topSizeMD+'.input2X')
        pm.connectAttr(top_ctrl+'.scaleZ',topSizeMD+'.input2Y')
        pm.connectAttr(top_cvsInfo+'.arcLength',topCN+'.firstTerm')
        pm.connectAttr(topSizeMD+'.output',topCN+'.colorIfTrue')
        pm.connectAttr(topCN+'.outColor',topPlus+'.input3D[0]')
        pm.connectAttr(mid_ctrl+'.top_width',topPlus+'.input3D[1].input3Dx')
        pm.connectAttr(mid_ctrl+'.top_width',topPlus+'.input3D[1].input3Dy')
        topPlus.setAttr('input3D[2].input3Dx',-1)
        topPlus.setAttr('input3D[2].input3Dy',-1)
        pm.connectAttr(topPlus+'.output3D',mid+'.scale')
        #Constraint
        pm.parentConstraint(mid_ctrl,mid,mo=1)
        pm.aimConstraint(mid_ctrl,bottom_grps_2[0],mo=1)
        pm.aimConstraint(mid_ctrl,bottom_grps_3[0],mo=1)
        bottom_2_par = pm.pointConstraint(mid_ctrl,bottom_ctrl,bottom_grps_2[0])
        bottom_3_par = pm.pointConstraint(mid_ctrl,bottom_ctrl,bottom_grps_3[0])
        bottom_2_par.setAttr(mid_ctrl+'W0',2)
        bottom_3_par.setAttr(bottom_ctrl+'W1',2)
        data_grp = pm.group(n='penis_data_grp',em=1)
        pm.parent(bottom_ik[0],bottom_ik[2],top_ik[0],top_ik[2],data_grp)
        return bottom_grps,data_grp,bottom

    def eyeDoCtrl(self,eyeJt,headCtrl):
        eyeCons = []
        eyeUpper = []
        eyeCtrl = []
        for jt in eyeJt:
            tran = jt.getTranslation(space='world')
            ctrl_loc = pm.spaceLocator(n=jt+'_loc')
            aim_loc = pm.spaceLocator(n=jt+'_aim_loc')
            ctrl_loc.setAttr('translate',[tran[0],tran[1],tran[2]+(self.gbScale*2)])
            aim_loc.setAttr('translate',[tran[0],tran[1]+(self.gbScale*2),tran[2]])
            ctrl_loc.setAttr('visibility',0)
            aim_loc.setAttr('visibility',0)
            grps,ctrl= self.ctrlGrp(jt,size=self.gbScale*0.1,parent=0,lock=['rx','ry','rz','sx','sy','sz','v'],ctrlType='circleZ')[:2]
            self.snap(ctrl_loc,grps[1])
            pm.delete(ctrl_loc)
            pm.aimConstraint(ctrl,jt,wut='objectrotation',wuo=aim_loc,mo=1)
            pm.parent(aim_loc,headCtrl)
            eyeCons.append(grps[1])
            eyeUpper.append(grps[0])
            eyeCtrl.append(ctrl)
        tran = eyeJt[0].getTranslation(space='world')
        tran = [0,tran[1],tran[2]+(self.gbScale*2)]
        loc = pm.spaceLocator(n=self.chrName+'_eye')
        loc.setAttr('translate',tran)
        grps,ctrl= self.ctrlGrp(loc,size=self.gbScale*0.3,parent=0,lock=['rx','ry','rz','sx','sy','sz','v'],ctrlType='circleZ')[:2]
        pm.delete(loc)
        pm.parent(eyeCons[0],eyeCons[1],ctrl)
        eyeCons.append(grps[1])
        eyeUpper.append(grps[0])
        eyeCtrl.append(ctrl)
        pm.select(cl=1)
        return eyeCtrl,eyeUpper,eyeCons

    def mouthDoCtrl(self,jts,aim):
        grps,ctrl = self.ctrlGrp(jts[1],size=self.gbScale*0.05,parent=0,lock=['rx','ry','rz','sx','sy','sz','v'],ctrlType='circleZ')[:2]
        pm.aimConstraint(ctrl,jts[0],mo=1,wut='objectrotation',wuo=aim)
        pm.parent(grps[1],aim)
        #tooth
        upTooth = pm.duplicate(jts[0],po=1,n=self.chrName+'_up_tooth')[0]
        downTooth = pm.duplicate(jts[0],po=1,n=self.chrName+'_down_tooth')[0]
        upTooth.setAttr('radius',(upTooth.radius.get()/2))
        downTooth.setAttr('radius',(downTooth.radius.get()/2))
        pm.select(ctrl)
        pm.addAttr(ln='up_tooth',at='float',dv=0,min=-180,max=180,k=1)
        pm.addAttr(ln='down_tooth',at='float',dv=0,min=-180,max=180,k=1)
        pm.select(cl=1)
        pm.connectAttr(ctrl+'.up_tooth',upTooth+'.rotateX')
        down_PMA = pm.shadingNode('plusMinusAverage',al=1)
        pm.connectAttr(jts[0]+'.rotate',down_PMA+'.input3D[0]')
        pm.connectAttr(ctrl+'.down_tooth',down_PMA+'.input3D[1].input3Dx')
        pm.connectAttr(down_PMA+'.output3D',downTooth+'.rotate')
        return ctrl,grps[0],grps[1]

    ####################HumanAutoRigging####################

    def creatLoc(self,name,tran,size):
        '''
        將Name,tran指定為Locator的名字和位置
        '''
        loc = pm.spaceLocator(n='LOC_'+name)
        locShape = loc.getChildren()[0]
        locShape.setAttr('localScale',[size,size,size])
        locCons  = pm.group(loc,n=loc+'_cons')
        locCons.setTranslation(tran)
        return loc,locCons

    def clusterIntoLocs(self,loc1,loc2):
        '''
        在兩個Locator之間創建一條curve並鎖定在兩個Locator之間
        '''
        cvsClus = []
        locs = loc1,loc2
        cvs = pm.curve(d=1,ep=(loc1.getTranslation(space='world'),loc2.getTranslation(space='world')))
        clus = pm.cluster(cvs.cv[0])[1],pm.cluster(cvs.cv[1])[1]
        cvs.setAttr('overrideEnabled',1)
        cvs.setAttr('overrideDisplayType',2)
        for x in range(2):
            pm.parent(clus[x],locs[x])
            clus[x].setAttr('visibility',0)
            cvsClus.append(cvs)
            cvsClus.append(clus)
        return cvsClus

    def locJt_Scale(self,grp,size):
        '''
        將AutoRig的部位群組(grp)內容所有的Locator大小更改為變數self.gbScale*size
        '''
        for x in range(len(grp)):
            if grp[x].nodeType() == 'joint':
                grp[x].setAttr('radius',size)
            else:
                locShape = grp[x].getChildren()[0]
                locShape.setAttr('localScale',[size,size,size])

    def mirrorLoc(self,leftGrp,rightGrp):
        '''
        鏡像左右的Locator
        '''
        nodes = []
        for x in range(len(leftGrp)):
            tranMd = pm.shadingNode('multiplyDivide',al=1)
            rotMd = pm.shadingNode('multiplyDivide',al=1)
            tranMd.setAttr('input2',[-1,1,1])
            rotMd.setAttr('input2',[1,-1,-1])
            pm.connectAttr(leftGrp[x]+'.translate',tranMd+'.input1')
            pm.connectAttr(tranMd+'.output',rightGrp[x]+'.translate')
            pm.connectAttr(leftGrp[x]+'.rotate',rotMd+'.input1')
            pm.connectAttr(rotMd+'.output',rightGrp[x]+'.rotate')
            nodes.append(tranMd)
            nodes.append(rotMd)
        return nodes

    def findObjInList(self,list,name):
        '''
        在群組中尋找目標
        '''
        for x in range(len(list)):
            try:
                second = list[x].index(name)
                first = x
            except:
                pass
        return first,second

    def betweenTgt(self,point,aim,tgt,axis,attr,power):
        '''
        將tgt限制在point和aim兩個目標之間,並設定aimConstraint的worldUpVector=(axis)和pointConstraint的力距power
        '''
        pointCon = pm.pointConstraint(point,aim,tgt)
        aimCon = pm.aimConstraint(aim,tgt,mo=1,wu=axis)
        try:
            pointCon.setAttr(attr,power)
        except:
            pass
        return pointCon,aimCon

    def jointOrient(self,jts,aim,up,wu,setZero=''):
        '''
        將jts底層所有joint指向改為aim(軸向指向下一階骨架),up(設定朝上軸向),
        wu(aimConstraint的World up vector)
        '''
        for jt in jts[1:]:
            pm.parent(jt,w=1)
        for x in range(len(jts)):
            try:
                aimCon = pm.aimConstraint(jts[x+1],jts[x],aim=aim,u=up,wut='vector',wu=wu)
                pm.delete(aimCon)
                pm.select(jts[x])
                pm.makeIdentity(apply=1,r=1)
                if setZero == 'x':
                    jts[x].setAttr('jointOrientX',0)
                elif setZero == 'y':
                    jts[x].setAttr('jointOrientY',0)
                elif setZero == 'z':
                    jts[x].setAttr('jointOrientZ',0)
                else:
                    pass
            except:
                pass
        for y in range(len(jts)):
            try:
                pm.parent(jts[y+1],jts[y])
            except:
                jts[y].setAttr('jointOrient',[0,0,0])
                pm.makeIdentity(apply=1,r=1)

    def selectSkinJoints(self,joint_grp,rigJoint_grp):
        pm.select(joint_grp,hi=1)
        skinJt_grp = pm.ls(sl=1)
        if len(skinJt_grp) < 2:
            pm.select(rigJoint_grp,hi=1)
            skinJt_grp = pm.ls(sl=1)
        skinJoint = []
        for x in skinJt_grp:
            if x.nodeType() == 'joint':
                if x.drawStyle.get() == 0:
                    skinJoint.append(x)
        pm.select(cl=1)
        return skinJoint

    def chrSizeSet(self,high=0):
        '''
        設定角色大小
        '''
        try:
            pm.PyNode(self.chrName+'_locScale')
            pm.warning(u'有相同名稱Rig')
            ctrls = None
        except:
            try:
                bottomCtrl = pm.PyNode(self.chrName+'_bottom')
                pm.warning(u'有相同名稱Rig')
                ctrls = None
            except:
                bottomCtrl = self.cvsCtrl(size=5,ctrlType='arCircle',name=self.chrName+'_bottom')
                topCtrl = self.cvsCtrl(size=5,ctrlType='arCircle',name=self.chrName+'_top')
                self.lockAttrs(bottomCtrl,attrs=['tx','tz','rx','ry','rz','sx','sy','sz','v'])
                self.lockAttrs(topCtrl,attrs=['tx','tz','rx','ry','rz','sx','sy','sz','v'])
                topCtrl.setTranslation([0,high,0])
                ctrls = bottomCtrl,topCtrl
                pm.select(cl=1)
        return ctrls

    def resetName(self):
        pelvis = ['pelvis','upPelvis','downPelvis','chest','hip']
        L_leg = ['L_upperLeg','L_lowerLeg','L_endLeg','L_foot','L_toe','L_toe_end','L_heel']
        R_leg = ['R_upperLeg','R_lowerLeg','R_endLeg','R_foot','R_toe','R_toe_end','R_heel']
        head = ['neck','head','head_end']
        L_shoulder = ['L_shoulder']
        L_arm = ['L_upperArm','L_lowerArm','L_endArm','L_hand']
        R_shoulder = ['R_shoulder']
        R_arm = ['R_upperArm','R_lowerArm','R_endArm','R_hand']
        L_thumb = ['L_thumb_1','L_thumb_2','L_thumb_3','L_thumb_4']
        L_index = ['L_index_1','L_index_2','L_index_3','L_index_4','L_index_5']
        L_middle = ['L_middle_1','L_middle_2','L_middle_3','L_middle_4','L_middle_5']
        L_ring = ['L_ring_1','L_ring_2','L_ring_3','L_ring_4','L_ring_5']
        L_little = ['L_little_1','L_little_2','L_little_3','L_little_4','L_little_5']
        R_thumb = ['R_thumb_1','R_thumb_2','R_thumb_3','R_thumb_4']
        R_index = ['R_index_1','R_index_2','R_index_3','R_index_4','R_index_5']
        R_middle = ['R_middle_1','R_middle_2','R_middle_3','R_middle_4','R_middle_5']
        R_ring = ['R_ring_1','R_ring_2','R_ring_3','R_ring_4','R_ring_5']
        R_little = ['R_little_1','R_little_2','R_little_3','R_little_4','R_little_5']
        face = ['L_eye','R_eye','mouth','mouth_end']
        L_breast = ['L_breast','L_midBreast','L_nipple']
        R_breast = ['R_breast','R_midBreast','R_nipple']
        L_butt = ['L_butt','L_butt_end']
        R_butt = ['R_butt','R_butt_end']
        allName = pelvis,L_leg,R_leg,head,L_shoulder,L_arm,R_shoulder,R_arm,L_thumb,L_index,L_middle,L_ring,\
            L_little,R_thumb,R_index,R_middle,R_ring,R_little,face,L_breast,R_breast,L_butt,R_butt
        return allName

    def creatRigLocs(self,breast=1,butt=1,thumb=3,index=4,middle=4,ring=4,little=4):
        '''
        創建AutoRig對位Locator
        '''
        ###分配RIG區域名稱,預設位置###
        pelvis_locsTran = [[0,10,0],[0,10,0],[0,10,0],[0,12,0],[0,9,0]]
        L_leg_locsTran = [[1,9,0],[1,5,0],[1,1,0],[1,1,0],[1,0,1],[1,0,2],[1,0,-1]]
        R_leg_locsTran = [[-1,9,0],[-1,5,0],[-1,1,0],[-1,1,0],[-1,0,1],[-1,0,2],[-1,0,-1]]
        head_locsTran = [[0,14,0],[0,15,0],[0,17,0]]
        L_shoulder_locsTran = [[0.3,13.5,0]]
        L_arm_locsTran = [[1.8,13.5,0],[4.3,13.5,0],[6.8,13.5,0],[6.8,13.5,0]]
        R_shoulder_locsTran = [[-0.3,13.5,0]]
        R_arm_locsTran = [[-1.8,13.5,0],[-4.3,13.5,0],[-6.8,13.5,0],[-6.8,13.5,0]]
        L_thumb_locsTran = [[7,13.5,0.25],[7.3,13.5,0.25],[7.6,13.5,0.25],[7.9,13.5,0.25]]
        L_index_locsTran = [[7.1,13.5,0.15],[7.6,13.5,0.15],[7.9,13.5,0.15],[8.1,13.5,0.15],[8.3,13.5,0.15]]
        L_middle_locsTran = [[7.1,13.5,0],[7.6,13.5,0],[7.9,13.5,0],[8.1,13.5,0],[8.3,13.5,0]]
        L_ring_locsTran = [[7.1,13.5,-0.15],[7.6,13.5,-0.15],[7.9,13.5,-0.15],[8.1,13.5,-0.15],[8.3,13.5,-0.15]]
        L_little_locsTran = [[7.1,13.5,-0.3],[7.6,13.5,-0.3],[7.9,13.5,-0.3],[8.1,13.5,-0.3],[8.3,13.5,-0.3]]
        R_thumb_locsTran = [[-7,13.5,0.25],[-7.3,13.5,0.25],[-7.6,13.5,0.25],[-7.9,13.5,0.25]]
        R_index_locsTran = [[-7.1,13.5,0.15],[-7.6,13.5,0.15],[-7.9,13.5,0.15],[-8.1,13.5,0.15],[-8.3,13.5,0.15]]
        R_middle_locsTran = [[-7.1,13.5,0],[-7.6,13.5,0],[-7.9,13.5,0],[-8.1,13.5,0],[-8.3,13.5,0]]
        R_ring_locsTran  = [[-7.1,13.5,-0.15],[-7.6,13.5,-0.15],[-7.9,13.5,-0.15],[-8.1,13.5,-0.15],[-8.3,13.5,-0.15]]
        R_little_locsTran = [[-7.1,13.5,-0.3],[-7.6,13.5,-0.3],[-7.9,13.5,-0.3],[-8.1,13.5,-0.3],[-8.3,13.5,-0.3]]
        face_locsTran = [[0.3,16,0.7],[-0.3,16,0.7],[0,15.2,0.2],[0,15.2,1.2]]
        L_breast_locsTran = [[0.5,13,0.5],[0.5,13,1],[0.5,13,1.5]]
        R_breast_locsTran = [[-0.5,13,0.5],[-0.5,13,1],[-0.5,13,1.5]]
        L_butt_locsTran = [[0.6,8.75,0.02],[0.6,8.75,-1]]
        R_butt_locsTran = [[-0.6,8.75,0.02],[-0.6,8.75,-1]]
        locsName = self.resetName()
        locsTran = pelvis_locsTran,L_leg_locsTran,R_leg_locsTran,head_locsTran,L_shoulder_locsTran,L_arm_locsTran,R_shoulder_locsTran,R_arm_locsTran,L_thumb_locsTran,L_index_locsTran,L_middle_locsTran,L_ring_locsTran,L_little_locsTran,R_thumb_locsTran,R_index_locsTran,R_middle_locsTran,R_ring_locsTran,R_little_locsTran,face_locsTran,L_breast_locsTran,R_breast_locsTran,L_butt_locsTran,R_butt_locsTran
        for x in range(len(locsTran)):
            for y in range(len(locsTran[x])):
                for z in range(3):
                    locsTran[x][y][z]*=self.gbScale
        locs = ([],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
        locsCons = ([],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
        jts = ([],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
        ###創建RigLocator初始對應位置###
        try:
            chr_locScale = pm.PyNode(self.chrName+'_locScale')
            pm.warning(u'有相同名稱Rig')
            jts,locScale,nodes = None,None,None
        except:
            locScale = pm.group(n=self.chrName+'_locScale',em=1)
            for x in range(len(locsName)):
                for y in range(len(locsName[x])):
                    loc,locCons = self.creatLoc(locsName[x][y],locsTran[x][y],self.gbScale/5)
                    jt = pm.joint(n=self.chrName+'_'+locsName[x][y],p=locsTran[x][y],rad=self.gbScale/5)
                    pm.parentConstraint(loc,jt)
                    locs[x].append(loc)
                    locsCons[x].append(locCons)
                    jts[x].append(jt)
                    if len(locsCons[x]) > 1:
                        pm.parent(locsCons[x][y],locs[x][y-1])
            jtsGrp = pm.group(n=self.chrName+'_jtsGrp',em=1)
            for x in jts:
                pm.parent(x,jtsGrp)
            jtsGrp.setAttr('visibility',0)
            pm.parent(jtsGrp,locScale)
            ###設定Locator,Jt大小###
            for x in range(len(locs)):
                for y in range(len(locs[x])):
                    self.locJt_Scale(locs[x],self.gbScale/5)
                    self.locJt_Scale(jts[x],self.gbScale/5)
            for i in range(10):
                self.locJt_Scale(locs[i+8],self.gbScale/(5*3))
                self.locJt_Scale(jts[i+8],self.gbScale/(5*3))
            for j in range(2):
                self.locJt_Scale(locs[j+21],self.gbScale/(5*3))
                self.locJt_Scale(jts[j+21],self.gbScale/(5*3))
            ###依照需求骨架設定###
            ###breast###
            if breast == 0:
                pm.delete(locsCons[19],locsCons[20],jts[19],jts[20])
            else:
                pass
            ###butt###
            if butt == 0:
                pm.delete(locsCons[21],locsCons[22],jts[21],jts[22])
            else:
                pass
            ###finger###
            fingerNumber = index,middle,ring,little
            if thumb == 2:
                pm.delete(locsCons[8][3],locsCons[13][3],jts[8][3],jts[13][3])
                locs[8].remove(locs[8][-1])
                locs[13].remove(locs[13][-1])
                locsCons[8].remove(locsCons[8][-1])
                locsCons[13].remove(locsCons[13][-1])
            else:
                pass
            for finger in range(len(fingerNumber)):
                if fingerNumber[finger] == 3:
                    pm.delete(locsCons[9+finger][4],locsCons[14+finger][4],jts[9+finger][4],jts[14+finger][4])
                    locs[9+finger].remove(locs[9+finger][-1])
                    locs[14+finger].remove(locs[14+finger][-1])
                    locsCons[9+finger].remove(locsCons[9+finger][-1])
                    locsCons[14+finger].remove(locsCons[14+finger][-1])
                else:
                    pass
            ###設定Locator之間的層級和Curve###
            pm.parent(locsCons[0][0],locScale)
            pm.parent(locsCons[0][4],locs[0][0])
            pm.parent(locsCons[1][0],locsCons[2][0],locs[0][4])
            pm.parent(locsCons[5][0],locs[4][0])
            pm.parent(locsCons[7][0],locs[6][0])
            pm.parent(locsCons[8][0],locsCons[9][0],locsCons[10][0],locsCons[11][0],locsCons[12][0],locs[5][3])
            pm.parent(locsCons[13][0],locsCons[14][0],locsCons[15][0],locsCons[16][0],locsCons[17][0],locs[7][3])
            pm.parent(locsCons[18][0],locsCons[18][1],locsCons[18][2],locs[3][1])
            pm.parent(locsCons[1][6],locs[1][3])
            pm.parent(locsCons[2][6],locs[2][3])
            pm.parent(locsCons[3][0],locsCons[4][0],locsCons[6][0],locs[0][3])
            if breast == 1:
                pm.parent(locsCons[19][0],locsCons[20][0],locs[0][3])
            else:
                pass
            if butt == 1:
                pm.parent(locsCons[21][0],locs[1][0])
                pm.parent(locsCons[22][0],locs[2][0])
            else:
                pass
            cvsClusList = []
            cvsGrp = pm.group(n='cvs_grp',em=1)
            for x in range(len(locsCons)):
                for y in range(len(locsCons[x])):
                    try:
                        parloc = locsCons[x][y].getParent()
                        cvsClus = self.clusterIntoLocs(locs[x][y],parloc)
                        pm.parent(cvsClus[0],cvsGrp)
                        cvsClusList.append(cvsClus)
                    except:
                        pass
            pm.parent(cvsGrp,locScale)
            pm.delete(cvsClusList[0])
            pm.parent(locsCons[5][0],locsCons[5][1],locsCons[5][3],locsCons[7][0],locsCons[7][1],locsCons[7][3]\
                ,locsCons[3][1],locsCons[3][2],locsCons[18][0],locsCons[18][1],locsCons[18][2],locsCons[18][3],locs[0][3])
            if breast == 1:
                pm.parent(locsCons[19][1],locsCons[19][2],locsCons[20][1],locsCons[20][2],locs[0][3])
            else:
                pass
            pm.parent(locsCons[1][1],locsCons[2][1],locs[0][4])
            pm.parent(locsCons[0][3],locsCons[0][4],locsCons[1][3],locsCons[2][3],locScale)
            pm.parent(locsCons[0][2],locs[0][0])
            pm.parent(locsCons[1][2],locs[1][3])
            pm.parent(locsCons[2][2],locs[2][3])
            pm.parent(locsCons[5][2],locs[5][3])
            pm.parent(locsCons[7][2],locs[7][3])
            for x in range(5):
                for y in locsCons[x+8]:
                    pm.parent(y,locs[5][3])
                for z in locsCons[x+13]:
                    pm.parent(z,locs[7][3])
            hideLocs = locsCons[0][1],locsCons[0][2],locsCons[1][2],locsCons[2][2],locsCons[5][2],locsCons[7][2]
            for x in hideLocs:
                x.setAttr('visibility',0)
            ###設定手腳Locator Constraint###
            for x in locsCons[18]:
                pm.parentConstraint(locs[3][1],x,mo=1,sr=['x','y','z']) 
            self.betweenTgt(locs[1][0],locs[1][3],locsCons[1][1],[1,0,0],None,None)
            self.betweenTgt(locs[2][0],locs[2][3],locsCons[2][1],[-1,0,0],None,None)
            self.betweenTgt(locs[5][0],locs[5][3],locsCons[5][1],[0,1,0],None,None)
            self.betweenTgt(locs[7][0],locs[7][3],locsCons[7][1],[0,1,0],None,None)
            self.betweenTgt(locs[3][0],locs[3][2],locsCons[3][1],[-1,0,0],str(locs[3][0])+'W0',2)
            self.betweenTgt(locs[0][3],locs[0][4],locsCons[0][0],[0,1,0],str(locs[0][4])+'W1',2)
            if breast == 1:
                self.betweenTgt(locs[19][0],locs[19][2],locsCons[19][1],[0,1,0],None,None)
                self.betweenTgt(locs[20][0],locs[20][2],locsCons[20][1],[0,1,0],None,None)
            else:
                pass
            ###finger###
            if thumb == 3:
                self.betweenTgt(locs[8][1],locs[8][3],locsCons[8][2],[0,1,0],None,None)
                self.betweenTgt(locs[13][1],locs[13][3],locsCons[13][2],[0,1,0],None,None)
            else:
                self.betweenTgt(locs[8][0],locs[8][2],locsCons[8][1],[0,1,0],None,None)
                self.betweenTgt(locs[13][0],locs[13][2],locsCons[13][1],[0,1,0],None,None)
            for fingers in range(4):
                if fingerNumber[fingers] == 4:
                    self.betweenTgt(locs[9+(fingers)][0],locs[9+(fingers)][-1],locsCons[9+(fingers)][1],[0,1,0],str(locs[9+(fingers)][0])+'W0',1.4)
                    self.betweenTgt(locs[14+(fingers)][0],locs[14+(fingers)][-1],locsCons[14+(fingers)][1],[0,1,0],str(locs[14+(fingers)][0])+'W0',1.4)
                    self.betweenTgt(locs[9+(fingers)][0],locs[9+(fingers)][-1],locsCons[9+(fingers)][2],[0,1,0],str(locs[9+(fingers)][0])+'W0',0.5)
                    self.betweenTgt(locs[14+(fingers)][0],locs[14+(fingers)][-1],locsCons[14+(fingers)][2],[0,1,0],str(locs[14+(fingers)][0])+'W0',0.5)
                    self.betweenTgt(locs[9+(fingers)][0],locs[9+(fingers)][-1],locsCons[9+(fingers)][3],[0,1,0],str(locs[9+(fingers)][0])+'W0',0.2)
                    self.betweenTgt(locs[14+(fingers)][0],locs[14+(fingers)][-1],locsCons[14+(fingers)][3],[0,1,0],str(locs[14+(fingers)][0])+'W0',0.2)
                else:
                    self.betweenTgt(locs[9+(fingers)][0],locs[9+(fingers)][-1],locsCons[9+(fingers)][1],[0,1,0],str(locs[9+(fingers)][0])+'W0',1)
                    self.betweenTgt(locs[14+(fingers)][0],locs[14+(fingers)][-1],locsCons[14+(fingers)][1],[0,1,0],str(locs[14+(fingers)][0])+'W0',1)
                    self.betweenTgt(locs[9+(fingers)][0],locs[9+(fingers)][-1],locsCons[9+(fingers)][2],[0,1,0],str(locs[9+(fingers)][0])+'W0',0.25)
                    self.betweenTgt(locs[14+(fingers)][0],locs[14+(fingers)][-1],locsCons[14+(fingers)][2],[0,1,0],str(locs[14+(fingers)][0])+'W0',0.25)
            ###鏡像LocatorAttr###
            nodes = self.mirrorLoc(locs[1],locs[2])
            nodes += self.mirrorLoc(locs[4],locs[6])
            nodes += self.mirrorLoc(locs[5],locs[7])
            nodes += self.mirrorLoc(locs[8],locs[13])
            nodes += self.mirrorLoc(locs[9],locs[14])
            nodes += self.mirrorLoc(locs[10],locs[15])
            nodes += self.mirrorLoc(locs[11],locs[16])
            nodes += self.mirrorLoc(locs[12],locs[17])
            if breast == 1:
                nodes += self.mirrorLoc(locs[19],locs[20])
            else:
                pass
            if butt == 1:
                nodes += self.mirrorLoc(locs[21],locs[22])
            else:
                pass
            tranMd = pm.shadingNode('multiplyDivide',al=1)
            tranMd.setAttr('input2',[-1,1,1])
            pm.connectAttr(locs[18][0]+'.translate',tranMd+'.input1')
            pm.connectAttr(tranMd+'.output',locs[18][1]+'.translate')
            nodes.append(tranMd)
            ###設定LocatorAttr###
            ###translate,rotate###
            lockLocs = 'LOC_L_hand','LOC_R_hand'
            for x in lockLocs:
                first,second = self.findObjInList(locs,x)
                self.lockAttrs(locs[first][second],attrs=['sx','sy','sz','v'])
            ###ty,tz,rx###
            lockLocs = 'LOC_chest','LOC_neck','LOC_L_lowerLeg','LOC_R_lowerLeg'
            for x in lockLocs:
                first,second = self.findObjInList(locs,x)
                self.lockAttrs(locs[first][second],attrs=['tx','ry','rz','sx','sy','sz','v'])
            ###tx,ty###
            lockLocs = ['LOC_L_index_2','LOC_L_index_3','LOC_L_middle_2','LOC_L_middle_3'\
                ,'LOC_L_ring_2','LOC_L_ring_3','LOC_L_little_2','LOC_L_little_3'\
                ,'LOC_R_index_2','LOC_R_index_3','LOC_R_middle_2','LOC_R_middle_3'\
                ,'LOC_R_ring_2','LOC_R_ring_3','LOC_R_little_2','LOC_R_little_3']
            if index == 4:
                lockLocs.append('LOC_L_index_4')
                lockLocs.append('LOC_R_index_4')
            else:
                pass
            if middle == 4:
                lockLocs.append('LOC_L_middle_4')
                lockLocs.append('LOC_R_middle_4')
            else:
                pass
            if ring == 4:
                lockLocs.append('LOC_L_ring_4')
                lockLocs.append('LOC_R_ring_4')
            else:
                pass
            if little == 4:
                lockLocs.append('LOC_L_little_4')
                lockLocs.append('LOC_R_little_4')
            else:
                pass
            for x in lockLocs:
                first,second = self.findObjInList(locs,x)
                self.lockAttrs(locs[first][second],attrs=['tz','rx','ry','rz','sx','sy','sz','v'])
            ###tx,tz###
            if thumb == 3:
                lockLocs = ['LOC_L_lowerArm','LOC_R_lowerArm','LOC_L_thumb_3','LOC_R_thumb_3']
            else:
                lockLocs = ['LOC_L_lowerArm','LOC_R_lowerArm','LOC_L_thumb_2','LOC_R_thumb_2']
            for x in lockLocs:
                first,second = self.findObjInList(locs,x)
                self.lockAttrs(locs[first][second],attrs=['ty','rx','ry','rz','sx','sy','sz','v'])
            ###ty,tz###
            lockLocs = 'LOC_hip','LOC_mouth','LOC_L_lowerLeg','LOC_R_lowerLeg','LOC_L_toe','LOC_R_toe'\
                ,'LOC_L_heel','LOC_R_heel','LOC_head_end','LOC_mouth_end'
            for x in lockLocs:
                first,second = self.findObjInList(locs,x)
                self.lockAttrs(locs[first][second],attrs=['tx','rx','ry','rz','sx','sy','sz','v'])
            ###tz###
            lockLocs = ['LOC_L_toe_end','LOC_R_toe_end']
            for x in lockLocs:
                first,second = self.findObjInList(locs,x)
                self.lockAttrs(locs[first][second],attrs=['tx','ty','rx','ry','rz','sx','sy','sz','v'])
            if breast == 1:
                lockLocs = ['LOC_L_midBreast','LOC_R_midBreast']
                for x in lockLocs:
                    first,second = self.findObjInList(locs,x)
                    self.lockAttrs(locs[first][second],attrs=['tx','ty','rx','ry','rz','sx','sy','sz','v'])
            else:
                pass
            ###ty###
            lockLocs = ['LOC_pelvis','LOC_head']
            for x in lockLocs:
                first,second = self.findObjInList(locs,x)
                self.lockAttrs(locs[first][second],attrs=['tx','tz','rx','ry','rz','sx','sy','sz','v'])
            ###translate###
            lockLocs = ['LOC_L_upperArm','LOC_R_upperArm','LOC_L_foot','LOC_R_foot','LOC_L_upperLeg'\
                ,'LOC_R_upperLeg','LOC_L_shoulder','LOC_R_shoulder','LOC_L_eye','LOC_R_eye'\
                ,'LOC_L_thumb_1','LOC_L_index_1','LOC_L_middle_1','LOC_L_ring_1','LOC_L_little_1'\
                ,'LOC_R_thumb_1','LOC_R_index_1','LOC_R_middle_1','LOC_R_ring_1','LOC_R_little_1']
            if breast == 1:
                lockLocs.append('LOC_L_breast')
                lockLocs.append('LOC_R_breast')
                lockLocs.append('LOC_L_nipple')
                lockLocs.append('LOC_R_nipple')
            else:
                pass
            if butt == 1:
                lockLocs.append('LOC_L_butt')
                lockLocs.append('LOC_L_butt_end')
                lockLocs.append('LOC_R_butt')
                lockLocs.append('LOC_R_butt_end')
            else:
                pass
            if thumb == 3:
                lockLocs.append('LOC_L_thumb_2')
                lockLocs.append('LOC_R_thumb_2')
                lockLocs.append('LOC_L_thumb_4')
                lockLocs.append('LOC_R_thumb_4')
            else:
                lockLocs.append('LOC_L_thumb_3')
                lockLocs.append('LOC_R_thumb_3')
            if index == 4:
                lockLocs.append('LOC_L_index_5')
                lockLocs.append('LOC_R_index_5')
            else:
                lockLocs.append('LOC_L_index_4')
                lockLocs.append('LOC_R_index_4')
            if middle == 4:
                lockLocs.append('LOC_L_middle_5')
                lockLocs.append('LOC_R_middle_5')
            else:
                lockLocs.append('LOC_L_middle_4')
                lockLocs.append('LOC_R_middle_4')
            if ring == 4:
                lockLocs.append('LOC_L_ring_5')
                lockLocs.append('LOC_R_ring_5')
            else:
                lockLocs.append('LOC_L_ring_4')
                lockLocs.append('LOC_R_ring_4')
            if little == 4:
                lockLocs.append('LOC_L_little_5')
                lockLocs.append('LOC_R_little_5')
            else:
                lockLocs.append('LOC_L_little_4')
                lockLocs.append('LOC_R_little_4')
            pm.select(cl=1)
        return jts,locScale,nodes

    def creatRigJoints(self):
        '''
        搜尋指定名稱的Locator並轉換為Joint，並做jointOrient處理
        '''
        #刪除Locator並保存Joint
        name = self.resetName()
        jts = ([],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
        cons = []
        for x in range(len(jts)):
            for y in name[x]:
                try:
                    jt = pm.PyNode(self.chrName+'_'+y)
                    con = jt.rotateX.inputs()[0]
                    jts[x].append(jt)
                    cons.append(con)
                except:
                    pass
        for y in jts:
            try:
                pm.parent(y,w=1)
            except:
                pass
        pm.delete(cons)
        pm.delete(pm.PyNode(self.chrName+'_locScale'))
        #刪除鏡像Joint
        pm.delete(jts[2],jts[6],jts[7],jts[13],jts[14],jts[15],jts[16],jts[17])
        try:
            pm.delete(jts[20])
        except:
            pass
        try:
            pm.delete(jts[22])
        except:
            pass
        #jointOrient
        legJts = jts[1][0],jts[1][1],jts[1][2],jts[1][3]
        footJts = jts[1][4],jts[1][5],jts[1][6]
        leg_foot = legJts,footJts,jts[9],jts[10],jts[11],jts[12]
        arm_finger = jts[5],jts[9],jts[10],jts[11],jts[12]
        fingerJts = jts[8],jts[9],jts[10],jts[11],jts[12]
        jts[0][0].setAttr('jointOrient',[180,0,90])
        thumbJt = []                                   #finger_thumb
        thumbJt.append(jts[5][3])
        for j in jts[8]:
            thumbJt.append(j)
        self.jointOrient(thumbJt,[1,0,0],[0,0,-1],[1,0,0])
        pm.parent(jts[8][0],w=1)
        for i in leg_foot:
            self.jointOrient(i,[1,0,0],[0,1,0],[1,0,0])    #arm_leg_finger
        for k in arm_finger:
            self.jointOrient(k,[1,0,0],[0,1,0],[1,0,0],setZero='x')
        for l in fingerJts:
            for m in l:
                m.setAttr('segmentScaleCompensate',0)
        jts[1][2].setAttr('jointOrient',[0,0,0])
        jts[5][2].setAttr('jointOrient',[0,0,0])
        jts[5][3].setAttr('jointOrient',[0,0,0])
        pm.parent(jts[1][3],w=1)
        jts[1][2].setAttr('jointOrient',[0,0,0])
        pm.parent(jts[1][3],jts[1][2])
        self.jointOrient(jts[3],[1,0,0],[0,1,0],[1,0,0])    #head
        mouth = jts[18][2],jts[18][3]
        self.jointOrient(mouth,[0,0,1],[0,1,0],[0,1,0])    #mouth
        try:
            self.jointOrient(jts[21],[0,0,1],[0,1,0],[0,1,0])    #butt
        except:
            pass
        try:
            self.jointOrient(jts[19],[0,0,1],[0,1,0],[0,1,0])    #breast
        except:
            pass
        chest = jts[0][1],jts[0][3]
        hip = jts[0][2],jts[0][4]
        self.jointOrient(chest,[1,0,0],[0,1,0],[1,0,0])    #chest
        self.jointOrient(hip,[-1,0,0],[0,1,0],[-1,0,0])    #hip
        #將Joint串接
        pm.parent(jts[18][0],jts[18][1],jts[18][2],jts[3][1])    #face
        pm.parent(jts[1][4],jts[1][6],jts[1][3])    #leg
        pm.parent(jts[0][1],jts[0][2],jts[0][0])        #pevis
        pm.parent(jts[1][0],jts[0][4])    #hip
        pm.parent(jts[8][0],jts[9][0],jts[10][0],jts[11][0],jts[12][0],jts[5][3])    #finger
        pm.parent(jts[5][0],jts[4][0])    #shoulder
        pm.parent(jts[3][0],jts[4][0],jts[0][3])    #chest
        try:
            pm.parent(jts[19][0],jts[0][3])    #breast
        except:
            pass
        try:
            pm.parent(jts[21][0],jts[1][0])    #butt 
        except:
            pass
        #preferredAngle
        jts[5][1].setAttr('preferredAngleY',-90)
        jts[1][1].setAttr('preferredAngleY',90)
        #mirrorJoint
        mirror = jts[1][0],jts[4][0]
        try:
            mirror = jts[1][0],jts[4][0],jts[19][0]
        except:
            pass
        for j in mirror:
            pm.mirrorJoint(j,mb=True,myz=True,sr=('L_','R_'))
        return jts

    def offsetCtrl(self):
        '''
        創建角色層級
        '''
        try:
            pm.PyNode(self.chrName.upper())
            chrScale,Data_On,Data_Off,Joint_grp,ctrl_grp,rigJoint_grp,loc_grp,Chatacter=None
            pm.warning(u'有相同名稱offset_Group')
        except:
            Chatacter = pm.group(em=1,n=self.chrName.upper())
            Constrain = self.cvsCtrl(size=self.gbScale,name=self.chrName+'_Constrain',ctrlType='locator')
            Mov = self.cvsCtrl(size=self.gbScale,name=self.chrName+'_Mov',ctrlType='fourFat')
            Constrain.setAttr('translateZ',4*self.gbScale)
            pm.makeIdentity(Constrain,a=1)
            Constrain.setAttr('scalePivot',[0,0,0])
            Constrain.setAttr('rotatePivot',[0,0,0])
            turn_buttom = pm.group(em=1,n=self.chrName+'_Turn_buttom')
            turn_middle = pm.group(em=1,n=self.chrName+'_Turn_middle')
            turn_top = pm.group(em=1,n=self.chrName+'_Turn_top')
            chrScale = pm.group(em=1,n=self.chrName+'_scale')
            ctrl_grp = pm.group(em=1,n=self.chrName+'_ctrl_grp')
            rigJoint_grp = pm.group(em=1,n=self.chrName+'_rigJoint_grp')
            loc_grp = pm.group(em=1,n=self.chrName+'_loc_grp')
            Fixed = pm.group(em=1,n=self.chrName+'_Fixed')
            Shape = pm.group(em=1,n=self.chrName+'_Shape')
            Data = pm.group(em=1,n=self.chrName+'_Data')
            Joint_grp = pm.group(em=1,n=self.chrName+'_Joint_grp')
            Data_On = pm.group(em=1,n=self.chrName+'_Data_On')
            Data_Off = pm.group(em=1,n=self.chrName+'_Data_Off')
            chrPelvis = pm.PyNode(self.chrName+'_pelvis')
            chrTop = pm.PyNode(self.chrName+'_head_end')
            self.snap(chrPelvis,turn_middle,trans=0,rot=0,scl=0,pivots=1)
            self.snap(chrTop,turn_top,trans=0,rot=0,scl=0,pivots=1)
            pm.parent(ctrl_grp,rigJoint_grp,loc_grp,chrScale)
            pm.parent(chrScale,turn_top)
            pm.parent(turn_top,turn_middle)
            pm.parent(turn_middle,turn_buttom)
            pm.parent(turn_buttom,Mov)
            pm.parent(Mov,Constrain)
            pm.parent(Data_On,Data_Off,Data)
            pm.parent(Shape,Data,Joint_grp,Fixed)
            pm.parent(Constrain,Fixed,Chatacter)
            offsetGrps = Constrain,Mov,turn_buttom,turn_middle,turn_top
            for x in offsetGrps:
                self.lockAttrs(x,attrs=['sx','sy','sz','v'])
            self.lockAttrs(chrScale,attrs=['v'])
            self.lockAttrs(Chatacter,attrs=['tx','ty','tz','rx','ry','rz','sx','sy','sz'])
            pm.select(cl=1)
            Data_Off.setAttr('visibility',0)
            loc_grp.setAttr('visibility',0)
        return chrScale,Data_On,Data_Off,Joint_grp,ctrl_grp,rigJoint_grp,loc_grp,Chatacter

    def startRigging(self,unity=0):
        '''
        開始Rig
        '''
        name = self.resetName()
        jts = ([],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
        for x in range(len(jts)):
            for y in name[x]:
                try:
                    jt = pm.PyNode(self.chrName+'_'+y)
                    jts[x].append(jt)
                except:
                    pass
        rigJoints = jts[1][0],jts[1][6],jts[2][0],jts[2][6],jts[3][0],jts[4][0],\
            jts[5][0],jts[6][0],jts[7][0],jts[8][0],jts[9][0],jts[10][0],jts[11][0],\
            jts[12][0],jts[13][0],jts[14][0],jts[15][0],jts[16][0],jts[17][0]
        try:
            rigJoints.append(jts[19][0])
            rigJoints.append(jts[20][0])
        except:
            pass
        try:
            rigJoints.append(jts[21][0])
            rigJoints.append(jts[22][0])
        except:
            pass
        for y in rigJoints:
            pm.parent(y,w=1)
        ###ArmRig###
        L_ArmRig = self.armLegDoCtrl(jts[5],About='L',Ankle=None,JtNumber=self.ArmNumber,bend=self.ArmBend)
        R_ArmRig = self.armLegDoCtrl(jts[7],About='R',Ankle=None,JtNumber=self.ArmNumber,bend=self.ArmBend)
        ###LegRig###
        L_Legs = jts[1][:-1]
        R_Legs = jts[2][:-1]
        L_LegRig = self.armLegDoCtrl(L_Legs,About='L',Ankle=jts[1][6],JtNumber=self.LegNumber,bend=self.LegBend)
        R_LegRig = self.armLegDoCtrl(R_Legs,About='R',Ankle=jts[2][6],JtNumber=self.LegNumber,bend=self.LegBend)
        pm.delete(jts[1][6],jts[2][6])
        ###forUnity###
        if unity == 1:
            pm.parent(jts[1][3],jts[1][1])
            pm.parent(jts[2][3],jts[2][1])
            pm.parent(jts[5][3],jts[5][1])
            pm.parent(jts[7][3],jts[7][1])
            pm.delete(jts[1][2],jts[2][2],jts[5][2],jts[7][2])
        else:
            pass
        ###spinal###
        spinalRig = self.spinalDoCtrl(jts[0],JtNumber=self.spinalNumber,bend=self.SpinalBend,unity=self.forUnity)
        ###head###
        headRig = self.neckDoCtrl(jts[3][0],jts[3][1],JtNumber=self.neckNumber,bend=self.NeckBend)
        ###mouth###
        mouthRig = self.mouthDoCtrl([jts[18][2],jts[18][3]],headRig[0][1])
        ###finger###
        L_finger = jts[8][0],jts[9][0],jts[10][0],jts[11][0],jts[12][0]
        R_finger = jts[13][0],jts[14][0],jts[15][0],jts[16][0],jts[17][0]
        L_fingerRig = self.fingerDoCtrl(L_finger,axis='Z',About='L',loc=jts[5][3])
        R_fingerRig = self.fingerDoCtrl(R_finger,axis='Z',About='R',loc=jts[7][3])
        L_fingerCtrl_grp = pm.group(n=self.chrName+'_L_fingerCtrl_grp',em=1)
        R_fingerCtrl_grp = pm.group(n=self.chrName+'_R_fingerCtrl_grp',em=1)
        self.snap(jts[5][3],L_fingerCtrl_grp,trans=1,rot=1)
        self.snap(jts[7][3],R_fingerCtrl_grp,trans=1,rot=1)
        for x in range(5):
            pm.parent(L_fingerRig[1][x][0],L_fingerCtrl_grp)
            pm.parent(R_fingerRig[1][x][0],R_fingerCtrl_grp)
        ###eye###
        EyeRig = self.eyeDoCtrl([jts[18][0],jts[18][1]],headRig[0][1])
        ###shoulder###
        L_shoulderRig = self.ctrlGrp(jts[4][0],size=0.5*self.gbScale,lock=['sx','sy','sz','v'],ctrlType='circleX',rotateOrder=1)
        R_shoulderRig = self.ctrlGrp(jts[6][0],size=0.5*self.gbScale,lock=['sx','sy','sz','v'],ctrlType='circleX',rotateOrder=1)
        ###butt bend###
        try:
            L_buttRig =  self.ctrlGrp(jts[21][1],size=0.25*self.gbScale,parent=0,point=0,orient=0,scale=0,lock=['rx','ry','rz','sx','sy','sz','v'],ctrlType='circle')
            R_buttRig =  self.ctrlGrp(jts[22][1],size=0.25*self.gbScale,parent=0,point=0,orient=0,scale=0,lock=['rx','ry','rz','sx','sy','sz','v'],ctrlType='circle')
            pm.aimConstraint(L_buttRig[1],jts[21][0],mo=1,aim=[1,0,0],u=[0,1,0],wuo=jts[1][0],wut='objectrotation',wu=[0,1,0])
            pm.aimConstraint(R_buttRig[1],jts[22][0],mo=1,aim=[1,0,0],u=[0,1,0],wuo=jts[2][0],wut='objectrotation',wu=[0,1,0])
            pm.parentConstraint(jts[1][0],L_buttRig[0][1],mo=1)
            pm.parentConstraint(jts[2][0],R_buttRig[0][1],mo=1)
        except:
            pass
        ###breast bend###
        try:
            L_breastRig = self.breastDoCtrl(jts[19][0],jts[19][1],jts[19][2])
            R_breastRig = self.breastDoCtrl(jts[20][0],jts[20][1],jts[20][2])
        except:
            pass
        ###隱藏不使用Joint###
        jts[3][2].setAttr('drawStyle',2)
        jts[18][3].setAttr('drawStyle',2)
        try:
            jts[21][1].setAttr('drawStyle',2)
            jts[22][1].setAttr('drawStyle',2)
        except:
            pass
        ###分類###
        ###Data_On###
        pm.parent(L_ArmRig[0][5],R_ArmRig[0][5],L_LegRig[0][3],R_LegRig[0][3],self.Data_On)
        ###Data_Off###
        pm.parent(L_ArmRig[8],R_ArmRig[8],L_LegRig[8],R_LegRig[8],self.Data_Off)
        ###rigJoint_grp###
        if self.forUnity == 0:
            pm.parent(L_ArmRig[7],R_ArmRig[7],L_LegRig[7],R_LegRig[7],jts[0][0],self.rigJoint_grp)
        else:
            pm.parent(L_ArmRig[7],R_ArmRig[7],L_LegRig[7],R_LegRig[7],jts[0][4],self.rigJoint_grp)
        ###neck bend###
        try:
            pm.parent(headRig[2],self.Data_Off)
            pm.parent(headRig[1],self.rigJoint_grp)
        except:
            pass
        ###spinal bend###
        try:
            pm.parent(spinalRig[2],self.Data_Off)
            pm.parent(spinalRig[1],self.rigJoint_grp)
        except:
            pass
        ###Finger to hand###
        pm.parent(L_finger,jts[5][3])
        pm.parent(R_finger,jts[7][3])
        ###Arm to shoulder###
        pm.parent(L_ArmRig[5][0],L_ArmRig[6][0],jts[5][0],jts[4][0])
        pm.parent(R_ArmRig[5][0],R_ArmRig[6][0],jts[7][0],jts[6][0])
        ###Leg tp hip###
        pm.parent(L_LegRig[5][0],L_LegRig[5][5],L_LegRig[6][0],jts[1][0],jts[0][4])
        pm.parent(R_LegRig[5][0],R_LegRig[5][5],R_LegRig[6][0],jts[2][0],jts[0][4])
        ###neck,shoulder to chest###
        pm.parent(jts[3][0],jts[4][0],jts[6][0],jts[0][3])
        ###ctrls to ctrl_grp###
        ArmLegType = L_ArmRig,R_ArmRig,L_LegRig,R_LegRig
        for x in ArmLegType:
            try:
                pm.parent(x[0][0].getParent(3),x[1][0].getParent(3),x[2][0].getParent(3),x[3][0].getParent(2),x[3][1].getParent(2),x[4].getParent(1),self.ctrl_grp)
            except:
                pm.parent(x[0][0].getParent(3),x[1][0].getParent(3),x[4].getParent(1),self.ctrl_grp)
        pm.parent(spinalRig[0][0].getParent(2),headRig[0][1].getParent(2),L_fingerCtrl_grp,R_fingerCtrl_grp,EyeRig[2][2],self.ctrl_grp)
        ###to chest###
        pm.parent(L_shoulderRig[0][1],R_shoulderRig[0][1],headRig[0][0].getParent(2),spinalRig[0][3])
        ###if butt###
        try:
            pm.parent(jts[21][0],jts[1][0])
            pm.parent(jts[22][0],jts[2][0])
            pm.parent(L_buttRig[0][1],R_buttRig[0][1],self.ctrl_grp)
            self.addSwitch(spinalRig[0][4],name='sub_ctrl',at='long',dv=0,min=0,max=1)
            pm.connectAttr(spinalRig[0][4]+'.sub_ctrl',L_buttRig[0][1]+'.visibility')
            pm.connectAttr(spinalRig[0][4]+'.sub_ctrl',R_buttRig[0][1]+'.visibility')
            spinalRig[0][4].setAttr('sub_ctrl',keyable=0,channelBox=1)
        except:
            pass
        ###if breast###
        try:
            pm.parent(L_breastRig[1],R_breastRig[1],self.Data_Off)
            pm.parent(jts[19][0],jts[20][0],jts[0][3])
            pm.parent(L_breastRig[0].getParent(2),R_breastRig[0].getParent(2),spinalRig[0][3])
            self.addSwitch(spinalRig[0][3],name='sub_ctrl',at='long',dv=0,min=0,max=1)
            pm.connectAttr(spinalRig[0][3]+'.sub_ctrl',L_breastRig[0].getParent(2)+'.visibility')
            pm.connectAttr(spinalRig[0][3]+'.sub_ctrl',R_breastRig[0].getParent(2)+'.visibility')
            spinalRig[0][3].setAttr('sub_ctrl',keyable=0,channelBox=1)
        except:
            pass
        ###fingerCtrl_grp constraint###
        pm.parentConstraint(jts[5][3],L_fingerCtrl_grp,mo=1)
        pm.parentConstraint(jts[7][3],R_fingerCtrl_grp,mo=1)
        pm.scaleConstraint(jts[5][3],L_fingerCtrl_grp,mo=1)
        pm.scaleConstraint(jts[7][3],R_fingerCtrl_grp,mo=1)
        ###fingerTipCtrl constraint###
        self.snap(L_ArmRig[4],L_fingerRig[0],trans=1,rot=0,scl=0,pivots=1)
        self.snap(R_ArmRig[4],R_fingerRig[0],trans=1,rot=0,scl=0,pivots=1)
        pm.parent(L_fingerRig[0],L_ArmRig[4].getParent(1))
        pm.parent(R_fingerRig[0],R_ArmRig[4].getParent(1))
        self.lockAttrs(L_fingerRig[0],attrs=['tx','ty','tz','rx','ry','rz','sx','sy','sz','v'])
        self.lockAttrs(R_fingerRig[0],attrs=['tx','ty','tz','rx','ry','rz','sx','sy','sz','v'])
        ###ctrlFollow設定###
        L_armFollow = jts[0][0],jts[4][0]
        R_armFollow = jts[0][0],jts[6][0]
        if self.forUnity == 1:
            legFollow = [jts[0][0]]
        else:
            legFollow = [jts[0][0],jts[0][4]]
        headFollow = [jts[0][0],jts[3][0]]
        L_IKarmFollowLocs = self.ctrlFollow(L_ArmRig[0][0],L_armFollow,ctrlType='ik')
        R_IKarmFollowLocs = self.ctrlFollow(R_ArmRig[0][0],R_armFollow,ctrlType='ik')
        L_IKlegFollowLocs = self.ctrlFollow(L_LegRig[0][0],legFollow,ctrlType='ik')
        R_IKlegFollowLocs = self.ctrlFollow(R_LegRig[0][0],legFollow,ctrlType='ik')
        L_FKarmFollowLocs = self.ctrlFollow(L_ArmRig[1][0],L_armFollow,ctrlType='fk')
        R_FKarmFollowLocs = self.ctrlFollow(R_ArmRig[1][0],R_armFollow,ctrlType='fk')
        L_FKlegFollowLocs = self.ctrlFollow(L_LegRig[1][0],legFollow,ctrlType='fk')
        R_FKlegFollowLocs = self.ctrlFollow(R_LegRig[1][0],legFollow,ctrlType='fk')
        headFollowLocs = self.ctrlFollow(headRig[0][1],headFollow,ctrlType='fk')
        eyeFollowLocs = self.ctrlFollow(EyeRig[0][2],[jts[3][0],jts[3][1]],ctrlType='ik')
        pm.parentConstraint(jts[4][0],L_ArmRig[0][1].getParent(2),mo=1)
        pm.parentConstraint(jts[6][0],R_ArmRig[0][1].getParent(2),mo=1)
        pm.parentConstraint(jts[0][4],L_LegRig[0][1].getParent(2),mo=1)
        pm.parentConstraint(jts[0][4],R_LegRig[0][1].getParent(2),mo=1)
        #Loc_grp
        pm.parent(L_IKarmFollowLocs,R_IKarmFollowLocs,L_IKlegFollowLocs,\
            R_IKlegFollowLocs,L_FKarmFollowLocs,R_FKarmFollowLocs,\
            L_FKlegFollowLocs,R_FKlegFollowLocs,headFollowLocs,\
            eyeFollowLocs,L_ArmRig[9],R_ArmRig[9],L_LegRig[9],R_LegRig[9],self.loc_grp)
        pm.select(cl=1)

    def copyRigJt(self,copyTgt,parentGrp,name=''):
        jtGrp = pm.group(n=self.chrName+'_'+name+'_Joint_grp')
        pm.parent(jtGrp,parentGrp)
        for jts in range(len(copyTgt)):
            copyJt = pm.duplicate(copyTgt[jts],n=name+'_'+copyTgt[jts])[0]
            pm.parent(copyJt,w=1)
            pm.select(copyJt,hi=1)
            all = pm.ls(sl=1)[1:]
            deleteObj = []
            for x in all:
                x.rename(x.name().replace(self.chrName,name+'_'+self.chrName))
                if x.nodeType() != 'joint' and len(x.getChildren()) == 0:
                    deleteObj.append(x)
                elif x.visibility.get() == 0:
                    deleteObj.append(x)
                elif len(x.getChildren()) == 0 and x.drawStyle.get() == 2:
                    deleteObj.append(x)
                else:
                    pass
            pm.delete(deleteObj)
            pm.select(copyJt,hi=1)
            all = pm.ls(sl=1)
            for okJt in all:
                source = pm.PyNode(okJt.replace(name+'_',''))
                pm.connectAttr(source+'.translate',okJt+'.translate')
                pm.connectAttr(source+'.rotate',okJt+'.rotate')
                pm.connectAttr(source+'.scale',okJt+'.scale')
            pm.parent(copyJt,jtGrp)
        pm.select(cl=1)
        return jtGrp

    ####################QuadrupedsAutoRigging####################

    def Quadrupeds_resetName(self):
        pelvis = ['pelvis','upPelvis','downPelvis','chest','hip','spinal']
        head = ['neck','head','head_end']
        face = ['L_eye','R_eye','mouth','mouth_end','L_ear','R_ear','L_ear_end','R_ear_end']
        L_frontPaw = ['L_clavicle','L_upperArm','L_lowerArm','L_endArm','L_frontFoot','L_arm_claw','L_arm_claw_end','L_arm_heel']
        R_frontPaw = ['R_clavicle','R_upperArm','R_lowerArm','R_endArm','R_frontFoot','R_arm_claw','R_arm_claw_end','R_arm_heel']
        L_BackPaw = ['L_ischium','L_upperLeg','L_lowerLeg','L_engLeg','L_backFoot','L_foot_claw','L_foot_claw_end','L_leg_heel']
        R_BackPaw = ['R_ischium','R_upperLeg','R_lowerLeg','R_engLeg','R_backFoot','R_foot_claw','R_foot_claw_end','R_leg_heel']
        tail = ['upperTail','tail_1','tail_2','endTail']
        allName = pelvis,head,face,L_frontPaw,R_frontPaw,L_BackPaw,R_BackPaw,tail
        return allName

    def Quadrupeds_creatRigLocs(self,type=''):
        if type == 'horse':
            pelvis_locsTran = [[0,11,2],[0,11,2],[0,11,2],[0,11,8],[0,11,0],[0,11,5]]
            head_locsTran = [[0,10,9.5],[0,14.6,12.7],[0,17,12.7]]
            face_locsTran = [[1,14,13.6],[-1,14,13.6],[0,13.5,12.75],\
                [0,11,15.5],[0.6,15,13.2],[-0.6,15,13.2],[0.6,16,13.2],[-0.6,16,13.2]]
            L_frontPaw_locsTran = [[1,8.5,9.5],[1,7,8.3],[1,3.5,8.3],\
                [1,1.4,8.3],[1,1.4,8.3],[1,0.65,8.6],[1,0,9.5],[1,0,8]]
            R_frontPaw_locsTran = [[-1,8.5,9.5],[-1,7,8.3],[-1,3.5,8.3],\
                [-1,1.4,8.3],[-1,1.4,8.3],[-1,0.65,8.6],[-1,0,9.5],[-1,0,8]]
            L_BackPaw_locsTran = [[1.5,9.4,-2],[1.5,7,-0.25],[1.5,4.4,-1.65],\
                [1.5,1.2,-1.3],[1.5,1.2,-1.3],[1.5,0.55,-0.8],[1.5,0,0],[1.5,0,-1.5]]
            R_BackPaw_locsTran = [[-1.5,9.4,-2],[-1.5,7,-0.25],[-1.5,4.4,-1.65],\
                [-1.5,1.2,-1.3],[-1.5,1.2,-1.3],[-1.5,0.55,-0.8],[-1.5,0,0],[-1.5,0,-1.5]]
            tail_locsTran = [[0,11,-1.3],[0,11,-4.55],[0,11,-7.75],[0,11,-11]]
        else:
            pelvis_locsTran = [[0,4,1],[0,4,1],[0,4,1],[0,4,3.6],[0,4,0],[0,4,2.3]]
            head_locsTran = [[0,3.7,4],[0,4.6,4.7],[0,6,4.7]]
            face_locsTran = [[0.3,4.8,5.6],[-0.3,4.8,5.6],[0,4.2,5.3],[0,4.2,6.5],\
                [0.5,5,5],[-0.5,5,5],[0.5,5.7,5],[-0.5,5.7,5]]
            L_frontPaw_locsTran = [[0.7,3.35,3.7],[0.7,2.1,3.4],[0.7,0.7,3.4],\
                [0.7,0.3,3.4],[0.7,0.3,3.4],[0.7,0,3.6],[0.7,0,3.9],[0.7,0,3.3]]
            R_frontPaw_locsTran = [[-0.7,3.35,3.7],[-0.7,2.1,3.4],[-0.7,0.7,3.4],\
                [-0.7,0.3,3.4],[-0.7,0.3,3.4],[-0.7,0,3.6],[-0.7,0,3.9],[-0.7,0,3.3]]
            L_BackPaw_locsTran = [[0.7,3.7,0],[0.7,2,0],[0.7,1,-0.75],[0.7,0.32,-0.6],\
                [0.7,0.32,-0.6],[0.7,0,-0.4],[0.7,0,0],[0.7,0,-0.7]]
            R_BackPaw_locsTran = [[-0.7,3.7,0],[-0.7,2,0],[-0.7,1,-0.75],[-0.7,0.32,-0.6],\
                [-0.7,0.32,-0.6],[-0.7,0,-0.4],[-0.7,0,0],[-0.7,0,-0.7]]
            tail_locsTran = [[0,4,-0.5],[0,4,-1.7],[0,4,-2.8],[0,4,-4]]
        ###Loc_Joint連接###
        locsName = self.Quadrupeds_resetName()
        locsTran = pelvis_locsTran,head_locsTran,face_locsTran,\
            L_frontPaw_locsTran,R_frontPaw_locsTran,L_BackPaw_locsTran,\
            R_BackPaw_locsTran,tail_locsTran
        for x in range(len(locsTran)):
            for y in range(len(locsTran[x])):
                for z in range(3):
                    locsTran[x][y][z]*=self.gbScale
        locs = ([],[],[],[],[],[],[],[])
        locsCons = ([],[],[],[],[],[],[],[])
        jts = ([],[],[],[],[],[],[],[])
        locScale = pm.group(n=self.chrName+'_locScale',em=1)
        for x in range(len(locsName)):
            for y in range(len(locsName[x])):
                loc,locCons = self.creatLoc(locsName[x][y],locsTran[x][y],self.gbScale/5)
                jt = pm.joint(n=self.chrName+'_'+locsName[x][y],p=locsTran[x][y],rad=self.gbScale/5)
                pm.parentConstraint(loc,jt)
                locs[x].append(loc)
                locsCons[x].append(locCons)
                jts[x].append(jt)
                if len(locsCons[x]) > 1:
                    pm.parent(locsCons[x][y],locs[x][y-1])
        jtsGrp = pm.group(n=self.chrName+'_jtsGrp',em=1)
        for x in jts:
            pm.parent(x,jtsGrp)
        jtsGrp.setAttr('visibility',0)
        pm.parent(jtsGrp,locScale)
        ###設定Locator,Jt大小###
        for x in range(len(locs)):
            for y in range(len(locs[x])):
                self.locJt_Scale(locs[x],self.gbScale/5)
                self.locJt_Scale(jts[x],self.gbScale/5)
        self.locJt_Scale(locs[2],self.gbScale/(5*2))
        self.locJt_Scale(jts[2],self.gbScale/(5*2))
        for x in range(4):
            for y in range(3):
                locs[x+3][y+5].setAttr('localScale',[self.gbScale/(5*2),self.gbScale/(5*2),self.gbScale/(5*2)])
                jts[x+3][y+5].setAttr('radius',self.gbScale/(5*2))
        ###設定Locator之間的層級和Curve###
        pm.parent(locsCons[0][0],locScale)
        pm.parent(locsCons[0][5],locs[0][1])
        pm.parent(locsCons[0][2],locsCons[0][3],locsCons[0][4],locs[0][0])
        pm.parent(locsCons[2][0],locsCons[2][1],locsCons[2][2],locsCons[2][4],locsCons[2][5],locs[1][1])
        pm.parent(locsCons[2][6],locs[2][4])
        pm.parent(locsCons[2][7],locs[2][5])
        pm.parent(locsCons[7][0],locs[0][4])
        pm.parent(locsCons[3][7],locs[3][4])
        pm.parent(locsCons[4][7],locs[4][4])
        pm.parent(locsCons[5][7],locs[5][4])
        pm.parent(locsCons[6][7],locs[6][4])
        pm.parent(locsCons[1][0],locsCons[3][0],locsCons[4][0],locs[0][3])
        pm.parent(locsCons[5][0],locsCons[6][0],locs[0][4])
        cvsClusList = []
        cvsGrp = pm.group(n='cvs_grp',em=1)
        for x in range(len(locsCons)):
            for y in range(len(locsCons[x])):
                try:
                    parloc = locsCons[x][y].getParent()
                    cvsClus = self.clusterIntoLocs(locs[x][y],parloc)
                    pm.parent(cvsClus[0],cvsGrp)
                    cvsClusList.append(cvsClus)
                except:
                    pass
        pm.parent(cvsGrp,locScale)
        pm.delete(cvsClusList[0])
        pm.parent(locsCons[3][1],locsCons[3][2],locsCons[3][4],\
            locsCons[4][1],locsCons[4][2],locsCons[4][4],locs[0][3])
        pm.parent(locsCons[5][1],locsCons[5][2],locsCons[5][4],\
            locsCons[6][1],locsCons[6][2],locsCons[6][4],locsCons[7][3],locs[0][4])
        pm.parent(locsCons[0][3],locsCons[0][4],locScale)
        pm.parent(locsCons[2][3],locs[1][1])
        pm.parent(locsCons[3][3],locs[3][4])
        pm.parent(locsCons[4][3],locs[4][4])
        pm.parent(locsCons[5][3],locs[5][4])
        pm.parent(locsCons[6][3],locs[6][4])
        hideLocs = locsCons[0][1],locsCons[0][2],locsCons[3][3],locsCons[4][3],locsCons[5][3],\
            locsCons[6][3],locsCons[7][1],locsCons[7][2]
        for x in hideLocs:
            x.hide()
        ###設定Locator Constraint###
        self.betweenTgt(locs[0][1],locs[0][3],locsCons[0][5],[1,0,0],None,None)
        self.betweenTgt(locs[0][3],locs[0][4],locsCons[0][0],[1,0,0],locs[0][3]+'W0',0.4)
        self.betweenTgt(locs[3][1],locs[3][4],locsCons[3][2],[1,0,0],locs[3][1]+'W0',0.3)
        self.betweenTgt(locs[4][1],locs[4][4],locsCons[4][2],[1,0,0],locs[4][1]+'W0',0.3)
        self.betweenTgt(locs[5][1],locs[5][4],locsCons[5][2],[1,0,0],locs[5][1]+'W0',0.5)
        self.betweenTgt(locs[6][1],locs[6][4],locsCons[6][2],[1,0,0],locs[6][1]+'W0',0.5)
        self.betweenTgt(locs[7][0],locs[7][3],locsCons[7][1],[1,0,0],locs[7][0]+'W0',2)
        self.betweenTgt(locs[7][0],locs[7][3],locsCons[7][2],[1,0,0],locs[7][3]+'W1',2)
        ###鏡像LocatorAttr###
        nodes = self.mirrorLoc(locs[3],locs[4])
        nodes += self.mirrorLoc(locs[5],locs[6])
        eyeMd = pm.shadingNode('multiplyDivide',al=1)
        earMd = pm.shadingNode('multiplyDivide',al=1)
        eyeMd.setAttr('input2',[-1,1,1])
        earMd.setAttr('input2',[-1,1,1])
        pm.connectAttr(locs[2][0]+'.translate',eyeMd+'.input1')
        pm.connectAttr(locs[2][4]+'.translate',earMd+'.input1')
        pm.connectAttr(eyeMd+'.output',locs[2][1]+'.translate')
        pm.connectAttr(earMd+'.output',locs[2][5]+'.translate')
        nodes.append(eyeMd)
        nodes.append(earMd)
        ###設定LocatorAttr###
        ###ty,tz###
        lockLocs = 'LOC_head','LOC_head_end','LOC_mouth','LOC_mouth_end','LOC_neck',\
            'LOC_chest','LOC_pelvis','LOC_hip','LOC_upperTail','LOC_endTail',\
            'LOC_L_arm_claw','LOC_L_arm_claw_end','LOC_L_arm_heel','LOC_R_arm_claw',\
            'LOC_R_arm_claw_end','LOC_R_arm_heel','LOC_L_foot_claw','LOC_L_foot_claw_end',\
            'LOC_L_leg_heel','LOC_R_foot_claw','LOC_R_foot_claw_end','LOC_R_leg_heel',\
            'LOC_L_lowerArm','LOC_R_lowerArm','LOC_L_lowerLeg','LOC_R_lowerLeg'
        for x in lockLocs:
            first,second = self.findObjInList(locs,x)
            self.lockAttrs(locs[first][second],attrs=['tx','rx','ry','rz','sx','sy','sz','v'])
        ###translate###
        lockLocs = 'LOC_L_clavicle','LOC_L_upperArm','LOC_R_clavicle','LOC_R_upperArm',\
            'LOC_L_ischium','LOC_L_upperLeg','LOC_R_ischium','LOC_R_upperLeg'
        for x in lockLocs:
            first,second = self.findObjInList(locs,x)
            self.lockAttrs(locs[first][second],attrs=['rx','ry','rz','sx','sy','sz','v'])
        ###translate,ry###
        lockLocs = 'LOC_L_frontFoot','LOC_R_frontFoot','LOC_L_backFoot','LOC_R_backFoot'
        for x in lockLocs:
            first,second = self.findObjInList(locs,x)
            self.lockAttrs(locs[first][second],attrs=['rx','rz','sx','sy','sz','v'])
        return jts,locScale,nodes

    def Quadrupeds_creatRigJoints(self):
        name = self.Quadrupeds_resetName()
        jts = ([],[],[],[],[],[],[],[])
        cons = []
        for x in range(len(jts)):
            for y in name[x]:
                try:
                    jt = pm.PyNode(self.chrName+'_'+y)
                    con = jt.rotateX.inputs()[0]
                    jts[x].append(jt)
                    cons.append(con)
                except:
                    pass
        for y in jts:
            try:
                pm.parent(y,w=1)
            except:
                pass
        pm.delete(cons)
        pm.delete(pm.PyNode(self.chrName+'_locScale'))
        #刪除鏡像Joint
        pm.delete(jts[2][5],jts[2][7],jts[4],jts[6])
        #jointOrient
        frontPaw = jts[3][0],jts[3][1],jts[3][2],jts[3][3]
        backPaw = jts[5][0],jts[5][1],jts[5][2],jts[5][3]
        frontClaw = jts[3][4],jts[3][5],jts[3][6],jts[3][7]
        backClaw = jts[5][4],jts[5][5],jts[5][6],jts[5][7]
        pawAndClaw = frontPaw,backPaw,frontClaw,backClaw
        chest = jts[0][1],jts[0][3],jts[0][5]
        hip = jts[0][2],jts[0][4]
        headJts = jts[1],[jts[2][4],jts[2][6]]
        month = [jts[2][2],jts[2][3]]
        for x in pawAndClaw:
            self.jointOrient(x,[0,-1,0],[0,0,1],[0,0,1])
        for x in headJts:
            self.jointOrient(x,[0,1,0],[0,0,1],[0,0,1])
        self.jointOrient(chest,[0,0,1],[0,1,0],[0,1,0])
        self.jointOrient(hip,[0,0,-1],[0,1,0],[0,-1,0])
        hip[1].setAttr('jointOrientX',180)
        self.jointOrient(jts[7],[0,0,1],[0,1,0],[0,1,0])
        self.jointOrient(month,[0,0,1],[0,1,0],[0,1,0])
        #將Joint串接
        pm.parent(jts[2][0],jts[2][1],jts[2][2],jts[2][4],jts[1][1])
        pm.parent(jts[0][1],jts[0][2],jts[0][0])
        pm.parent(jts[0][5],jts[0][1])
        pm.parent(jts[1][0],jts[3][0],jts[0][3])
        pm.parent(jts[5][0],jts[7][0],jts[0][4])
        pm.parent(jts[7][3],jts[7][0])
        pm.parent(jts[3][4],jts[3][3])
        pm.parent(jts[5][4],jts[5][3])
        pm.parent(jts[3][7],jts[3][4])
        pm.parent(jts[5][7],jts[5][4])
        #preferredAngle
        jts[3][2].setAttr('preferredAngleX',90)
        jts[5][2].setAttr('preferredAngleX',-90)
        #mirrorJoint
        mirror = jts[2][4],jts[3][0],jts[5][0]
        for x in mirror:
            pm.mirrorJoint(x,mb=True,myz=True,sr=('L_','R_'))
        return jts

    def Stretchy_Joint(self,Switch,CvsInfo,Stretchy_axis='',Switch_Attr='',extrusion=0):
        MDaxis_1 = {'X':'X','Y':'Y','Z':'Z'}
        MDaxis_2 = {'X':'Y','Y':'X','Z':'X'}
        MDaxis_3 = {'X':'Z','Y':'Z','Z':'Y'}
        Plusaxis_1 = {'X':'x','Y':'y','Z':'z'}
        Plusaxis_2 = {'X':'y','Y':'x','Z':'x'}
        Plusaxis_3 = {'X':'z','Y':'z','Z':'y'}
        CNaxis_1 = {'X':'R','Y':'G','Z':'B'}
        CNaxis_2 = {'X':'G','Y':'R','Z':'R'}
        CNaxis_3 = {'X':'B','Y':'B','Z':'G'}
        MD_Input_1 = MDaxis_1[Stretchy_axis]
        MD_Input_2 = MDaxis_2[Stretchy_axis]
        MD_Input_3 = MDaxis_3[Stretchy_axis]
        Plus_Input_1 = Plusaxis_1[Stretchy_axis]
        Plus_Input_2 = Plusaxis_2[Stretchy_axis]
        Plus_Input_3 = Plusaxis_3[Stretchy_axis]
        CN_Input_1 = CNaxis_1[Stretchy_axis]
        CN_Input_2 = CNaxis_2[Stretchy_axis]
        CN_Input_3 = CNaxis_3[Stretchy_axis]
        #IK_Stretchy(Node)
        Stretchy_CN = pm.shadingNode('condition',al=1)
        Stretchy_axis_CN = pm.shadingNode('condition',al=1)
        Sqiash_axis_CN = pm.shadingNode('condition',al=1)
        Stretchy_plus = pm.shadingNode('plusMinusAverage',al=1)
        Stretchy_MD_size = pm.shadingNode('multiplyDivide',al=1)
        Stretchy_axis_MD = pm.shadingNode('multiplyDivide',al=1)
        Sqiash_axis_MD = pm.shadingNode('multiplyDivide',al=1)
        Stretchy_MD_info = pm.shadingNode('multiplyDivide',al=1)
        Stretchy_Length = CvsInfo.arcLength.get()
        ##IK_Stretchy(ConnectAttr)
        Stretchy_MD_info.setAttr('operation',2)
        Stretchy_axis_CN.setAttr('operation',0)
        Sqiash_axis_CN.setAttr('operation',0)
        Stretchy_axis_CN.setAttr('secondTerm',1)
        Sqiash_axis_CN.setAttr('secondTerm',1)
        if extrusion == 0:
            Stretchy_CN.setAttr('operation',2)
        if extrusion == 1:
            Stretchy_CN.setAttr('operation',1)
        pm.connectAttr(self.chrScale+'.scale',Stretchy_MD_size+'.input1')
        Stretchy_MD_size.setAttr('input2',[Stretchy_Length,Stretchy_Length,Stretchy_Length])
        pm.connectAttr(Stretchy_MD_size+'.output',Stretchy_axis_MD+'.input1')
        pm.connectAttr(Stretchy_MD_size+'.output',Sqiash_axis_MD+'.input1')
        pm.connectAttr(Switch+'.'+Switch_Attr[0],Stretchy_axis_MD+'.input2'+MD_Input_1)
        pm.connectAttr(Switch+'.'+Switch_Attr[1],Sqiash_axis_MD+'.input2'+MD_Input_2)
        pm.connectAttr(Switch+'.'+Switch_Attr[1],Sqiash_axis_MD+'.input2'+MD_Input_3)
        pm.connectAttr(CvsInfo+'.arcLength',Stretchy_MD_info+'.input1'+MD_Input_1)
        pm.connectAttr(CvsInfo+'.arcLength',Stretchy_MD_info+'.input2'+MD_Input_2)
        pm.connectAttr(CvsInfo+'.arcLength',Stretchy_MD_info+'.input2'+MD_Input_3)
        pm.connectAttr(Switch+'.'+Switch_Attr[0],Stretchy_axis_CN+'.firstTerm')
        pm.connectAttr(Stretchy_axis_MD+'.output',Stretchy_axis_CN+'.colorIfTrue')
        pm.connectAttr(CvsInfo+'.arcLength',Stretchy_axis_CN+'.colorIfFalseR')
        pm.connectAttr(CvsInfo+'.arcLength',Stretchy_axis_CN+'.colorIfFalseG')
        pm.connectAttr(CvsInfo+'.arcLength',Stretchy_axis_CN+'.colorIfFalseB')
        pm.connectAttr(Switch+'.'+Switch_Attr[1],Sqiash_axis_CN+'.firstTerm')
        pm.connectAttr(Sqiash_axis_MD+'.output',Sqiash_axis_CN+'.colorIfTrue')
        pm.connectAttr(CvsInfo+'.arcLength',Sqiash_axis_CN+'.colorIfFalseR')
        pm.connectAttr(CvsInfo+'.arcLength',Sqiash_axis_CN+'.colorIfFalseG')
        pm.connectAttr(CvsInfo+'.arcLength',Sqiash_axis_CN+'.colorIfFalseB')
        pm.connectAttr(Stretchy_axis_CN+'.outColor'+CN_Input_1,Stretchy_MD_info+'.input2'+MD_Input_1)
        pm.connectAttr(Sqiash_axis_CN+'.outColor'+CN_Input_2,Stretchy_MD_info+'.input1'+MD_Input_2)
        pm.connectAttr(Sqiash_axis_CN+'.outColor'+CN_Input_3,Stretchy_MD_info+'.input1'+MD_Input_3)
        pm.connectAttr(CvsInfo+'.arcLength',Stretchy_CN+'.firstTerm')
        pm.connectAttr(Stretchy_MD_size+'.output'+MD_Input_1,Stretchy_CN+'.secondTerm')
        pm.connectAttr(Stretchy_MD_info+'.output',Stretchy_CN+'.colorIfTrue')
        pm.connectAttr(Stretchy_CN+'.outColor',Stretchy_plus+'.input3D[0]')
        pm.connectAttr(Switch+'.'+Switch_Attr[2],Stretchy_plus+'.input3D[1].input3D'+Plus_Input_2)
        pm.connectAttr(Switch+'.'+Switch_Attr[2],Stretchy_plus+'.input3D[1].input3D'+Plus_Input_3)
        Stretchy_plus.setAttr('input3D[2].input3D'+Plus_Input_2,-1)
        Stretchy_plus.setAttr('input3D[2].input3D'+Plus_Input_3,-1)
        return Stretchy_plus

    def Quadrupeds_IK_Function(self,ikList,Ankle,ikfkSwitch,About='',ikType=''):
        #Create_ikHandle_PoleVector
        paw_IK = pm.ikHandle(sj=ikList[0],ee=ikList[2],n=self.chrName+'_'+About+'_'+ikType+'_pawIk',sol='ikRPsolver')[0]
        foot_IK = pm.ikHandle(sj=ikList[3],ee=ikList[4],n=self.chrName+'_'+About+'_'+ikType+'_footIk',sol='ikSCsolver')[0]
        toe_IK = pm.ikHandle(sj=ikList[4],ee=ikList[5],n=self.chrName+'_'+About+'_'+ikType+'_toeIk',sol='ikSCsolver')[0]
        pv = pm.spaceLocator(name=self.chrName+'_'+About+'_'+ikType+'_'+'PV')
        for x in [paw_IK,foot_IK,toe_IK,pv]:
            x.hide()
        pv.setTranslation(ikList[1].getTranslation(space='world'))
        if ikType == 'front':
            pv.setAttr('translateZ',pv.translateZ.get()+abs(ikList[1].translateY.get())*1.5)
        else:
            pv.setAttr('translateZ',pv.translateZ.get()+abs(ikList[1].translateY.get())*-1.5)
        pm.poleVectorConstraint(pv,paw_IK)

        PoleCvs = self.LookPoleVectorCvs(ikList[1],pv,name = self.chrName+'_'+About+'_'+ikType+'_PoleVectorCvs')

        pm.parent(PoleCvs,self.Data_On)
        #Create_IK_Ctrl_Grp
        IK_foot_grps,IK_foot_Ctrl = self.ctrlGrp(ikList[3],size=self.gbScale*0.2,parent=0,lock=['v'],ctrlType='cube',orient=1,rotateOrder=1)[:2]
        IK_upper_grps,IK_upper_Ctrl = self.ctrlGrp(ikList[0],size=self.gbScale*0.4,parent=0,point=1,lock=['rx','ry','rz','sx','sy','sz','v'],ctrlType='circle')[:2]
        IK_pv_grps,IK_pv_Ctrl = self.ctrlGrp(pv,size=0.2*self.gbScale,parent=0,scale=0,lock=['rx','ry','rz','sx','sy','sz','v'],ctrlType='rombus')[:2]
        anklePv = self.cvsCtrl(size=0.5*self.gbScale,name=self.chrName+'_'+About+'_'+ikType+'_anklePv_ctrl',ctrlType='cross')
        topCtrl = self.cvsCtrl(size=0.15*self.gbScale,name=self.chrName+'_'+About+'_'+ikType+'_top_ctrl',ctrlType='cross')
        heelCtrl = self.cvsCtrl(size=0.15*self.gbScale,name=self.chrName+'_'+About+'_'+ikType+'_heel_ctrl',ctrlType='cross')
        leftCtrl = self.cvsCtrl(size=0.1*self.gbScale,name=self.chrName+'_'+About+'_'+ikType+'_left_ctrl',ctrlType='cross')
        rightCtrl = self.cvsCtrl(size=0.1*self.gbScale,name=self.chrName+'_'+About+'_'+ikType+'_right_ctrl',ctrlType='cross')
        footPvGrp = pm.group(n=self.chrName+'_'+About+'_'+ikType+'_footPv_grp',em=1)
        toeIkGrp = pm.group(n=self.chrName+'_'+About+'_'+ikType+'_toeIk_grp',em=1)
        ankleIkGrp = pm.group(n=self.chrName+'_'+About+'_'+ikType+'_ankleIk_grp',em=1)
        heelCtrlGrp = pm.group(n=self.chrName+'_'+About+'_'+ikType+'_heelCtrl_grp',em=1)
        topCtrlGrp = pm.group(n=self.chrName+'_'+About+'_'+ikType+'_topCtrl_grp',em=1)
        footCtrlGrp = pm.group(n=self.chrName+'_'+About+'_'+ikType+'_footCtrl_grp',em=1)
        leftGrp = pm.group(n=self.chrName+'_'+About+'_'+ikType+'_left_grp',em=1)
        rightGrp = pm.group(n=self.chrName+'_'+About+'_'+ikType+'_right_grp',em=1)
        topCtrlCons = pm.group(n=self.chrName+'_'+About+'_'+ikType+'_topCtrl_cons',em=1)
        heelCtrlCons = pm.group(n=self.chrName+'_'+About+'_'+ikType+'_heelCtrl_cons',em=1)
        #AddAttr
        Attrs = ['roll','toeRot','side']
        self.addSwitch(IK_foot_Ctrl,name='toeLift',at='float',dv=40,min=1,max=360,k=0)
        self.addSwitch(IK_foot_Ctrl,name='toeStraight',at='float',dv=70,min=0,max=360,k=0)
        for attr in Attrs:
            self.addSwitch(IK_foot_Ctrl,name=attr,at='float',dv=0,min=-360,max=360)
        self.addSwitch(IK_foot_Ctrl,name='footPv_Display',at='float',dv=0,min=0,max=1)
        self.addSwitch(IK_foot_Ctrl,name='sub_ctrl',at='long',dv=0,min=0,max=1)
        IK_foot_Ctrl.setAttr('footPv_Display',keyable=0,channelBox=1)
        IK_foot_Ctrl.setAttr('sub_ctrl',keyable=0,channelBox=1)
        self.addSwitch(IK_pv_Ctrl,name='Knee_Lock',at='float',dv=0,min=0,max=1,k=1)
        self.addSwitch(IK_pv_Ctrl,name='Knee_Leg_Follow',at='float',dv=1,min=0,max=1,k=1)
        #ConnectAttr
        pm.connectAttr(IK_foot_Ctrl+'.sub_ctrl',IK_upper_grps[1]+'.visibility')
        pm.connectAttr(IK_foot_Ctrl+'.scale',ikList[2]+'.scale')
        #Knee_Function
        PvUpperJt = pm.duplicate(ikList[0],n=self.chrName+'_'+About+'_'+ikType+'_pv_upperJt',po=1)[0]
        PvEndJt = pm.duplicate(ikList[2],n=self.chrName+'_'+About+'_'+ikType+'_pv_lowerJt',po=1)[0]
        worldLoc = pm.spaceLocator(n=self.chrName+'_'+About+'_'+ikType+'_paw_pv_World')
        pm.parent(PvEndJt,PvUpperJt)
        pvIk = pm.ikHandle(sj=PvUpperJt,ee=PvEndJt,n=self.chrName+'_'+About+'_'+ikType+'_pvIk',sol='ikSCsolver')[0]
        pvIk.hide()
        pm.parent(pvIk,IK_foot_Ctrl)
        pvPanCon = pm.parentConstraint(PvUpperJt,worldLoc,IK_pv_grps[1],mo=1)
        pm.connectAttr(IK_pv_Ctrl+'.Knee_Leg_Follow',pvPanCon+'.'+PvUpperJt+'W0')
        pvRN1 = self.reverseNode(pvPanCon+'.'+PvUpperJt+'W0',None,Channel=1)
        pm.connectAttr(pvRN1+'.outputX',pvPanCon+'.'+worldLoc+'W1')
        #Roll_Function
        legGrp1 = (ankleIkGrp,anklePv)
        for G1 in legGrp1:
            self.snap(ikList[2],G1,rot=0)
        self.snap(ikList[5],topCtrlGrp,rot=0)
        legGrp2 = (topCtrl,topCtrlCons)
        for G2 in legGrp2:
            self.snap(topCtrlGrp,G2,rot=0)
        legGrp3 = (heelCtrlGrp,heelCtrlCons,heelCtrl)
        for G3 in legGrp3:
            self.snap(Ankle,G3,rot=0)
        legGrp4 = (toeIkGrp,leftGrp,leftCtrl,rightGrp,rightCtrl,footCtrlGrp)
        for G4 in legGrp4:
            self.snap(ikList[4],G4,rot=0)
        pm.parent(toe_IK,toeIkGrp)
        pm.parent(foot_IK,paw_IK,footCtrlGrp)
        pm.parent(toeIkGrp,footCtrlGrp,leftGrp)
        pm.parent(leftGrp,leftCtrl,rightCtrl,rightGrp)
        pm.parent(rightGrp,topCtrlGrp)
        pm.parent(topCtrl,topCtrlCons)
        pm.parent(topCtrlCons,topCtrlGrp,heelCtrlGrp)
        pm.parent(heelCtrl,heelCtrlCons)
        pm.parent(heelCtrlGrp,heelCtrlCons,ankleIkGrp)
        pm.parent(anklePv,ankleIkGrp,footPvGrp)
        pm.parent(footPvGrp,IK_foot_Ctrl)
        pm.parent(pv,IK_pv_Ctrl)
        lockCtrls = (anklePv,topCtrl,heelCtrl,leftCtrl,rightCtrl)
        for attr in lockCtrls:
            self.lockAttrs(attr,attrs=['sx','sy','sz','v'])
        turnPvTran = ikList[5].translateY.get()
        rightCtrl.setAttr('translateX',turnPvTran)
        leftCtrl.setAttr('translateX',turnPvTran*-1)
        pm.connectAttr(IK_foot_Ctrl+'.toeRot',toeIkGrp+'.rotateX')
        pm.connectAttr(anklePv+'.rotate',ankleIkGrp+'.rotate')
        footPMA1 = self.plusMinusAverageNode(2,anklePv+'.translate',anklePv.translate.get(),ankleIkGrp+'.rotatePivot',Channel=4)
        pm.connectAttr(topCtrl+'.translate',topCtrlGrp+'.rotatePivot')
        pm.connectAttr(heelCtrl+'.translate',heelCtrlGrp+'.rotatePivot')
        pm.connectAttr(leftCtrl+'.translate',leftGrp+'.rotatePivot')
        pm.connectAttr(rightCtrl+'.translate',rightGrp+'.rotatePivot')
        pm.connectAttr(IK_foot_Ctrl+'.footPv_Display',footPvGrp+'.visibility')
        if About == 'L':
            footSide=1
        if About == 'R':
            footSide=-1
        footMD1 = self.MultiplyDivideNode(1,IK_foot_Ctrl+'.side',footSide,None,Channel=1)
        footMD2 = self.MultiplyDivideNode(1,IK_foot_Ctrl+'.side',footSide,None,Channel=1)
        footCN1 = self.clampNode(footMD1+'.outputX',0,-360,None,Channel=1)
        footCN2 = self.clampNode(footMD2+'.outputX',360,0,None,Channel=1)
        pm.connectAttr(footCN1+'.outputR',leftGrp+'.rotateZ')
        pm.connectAttr(footCN2+'.outputR',rightGrp+'.rotateZ')
        LegCN1 = self.clampNode(IK_foot_Ctrl+'.roll',0,-360,None,Channel=1)
        LegCN2 = self.clampNode(heelCtrl+'.rotateX',0,-360,None,Channel=1)
        LegPMA1 = self.plusMinusAverageNode(1,LegCN1+'.outputR',LegCN2+'.outputR',heelCtrlGrp+'.rotateX',Channel=1)
        pm.connectAttr(heelCtrl+'.rotateY',heelCtrlGrp+'.rotateY')
        pm.connectAttr(heelCtrl+'.rotateZ',heelCtrlGrp+'.rotateZ')
        pm.connectAttr(topCtrl+'.rotateY',topCtrlGrp+'.rotateY')
        LegPMA2 = self.plusMinusAverageNode(2,IK_foot_Ctrl+'.toeStraight',IK_foot_Ctrl+'.toeLift',None,Channel=1)
        LegPMA3 = self.plusMinusAverageNode(2,IK_foot_Ctrl+'.roll',IK_foot_Ctrl+'.toeLift',None,Channel=1)
        LegCN3 = self.clampNode(LegPMA3+'.output1D',LegPMA2+'.output1D',0,None,Channel=1)
        LegMD1 = self.MultiplyDivideNode(2,LegCN3+'.outputR',LegPMA2+'.output1D',None,Channel=1)
        LegMD2 = self.MultiplyDivideNode(1,LegMD1+'.outputX',IK_foot_Ctrl+'.roll',None,Channel=1) 
        LegPMA4 = self.plusMinusAverageNode(1,topCtrl+'.rotateX',LegMD2+'.outputX',topCtrlGrp+'.rotateX',Channel=1)
        LegCN4 = self.clampNode(IK_foot_Ctrl+'.roll',IK_foot_Ctrl+'.toeLift',0,None,Channel=1)
        LegMD3 = self.MultiplyDivideNode(2,LegCN4+'.outputR',IK_foot_Ctrl+'.toeLift',None,Channel=1)
        LegPMA5 = self.plusMinusAverageNode(2,1,LegMD1+'.outputX',None,Channel=1)
        LegMD4 = self.MultiplyDivideNode(1,LegMD3+'.outputX',LegPMA5+'.output1D',None,Channel=1)
        LegMD5 = self.MultiplyDivideNode(1,LegMD4+'.outputX',IK_foot_Ctrl+'.roll',footCtrlGrp+'.rotateX',Channel=1)
        #IK_Stretchy(CvsInfo)
        upperTran = ikList[0].getTranslation(space='world')
        endTran = ikList[2].getTranslation(space='world')
        Paw_Length_Cvs = pm.curve(d=1,n=self.chrName+'_'+About+'_'+ikType+'_paw_Cvs',ep=(upperTran,endTran))
        Paw_Length_CvsInfo = pm.arclen(Paw_Length_Cvs,ch=1)
        upper_Clu = pm.cluster(Paw_Length_Cvs+'.cv[0]')[1]
        end_Clu = pm.cluster(Paw_Length_Cvs+'.cv[1]')[1]
        pm.parent(upper_Clu,IK_upper_Ctrl)
        pm.parent(end_Clu,IK_foot_Ctrl)
        upper_Clu.hide()
        end_Clu.hide()
        Paw_Plus = self.Stretchy_Joint(ikfkSwitch,Paw_Length_CvsInfo,Stretchy_axis='Y',\
            Switch_Attr=['Auto_IK_Stretchy','Auto_Sqiash_Stretchy',ikType+'_Paw_Width'])
        pm.connectAttr(Paw_Plus+'.output3D',ikList[0]+'.scale')
        pm.connectAttr(Paw_Plus+'.output3D',ikList[1]+'.scale')
        #Create_List
        IK_ctrl_cons = IK_foot_grps[1],IK_upper_grps[1],IK_pv_grps[1]
        IK_ctrls = IK_foot_Ctrl,IK_upper_Ctrl,IK_pv_Ctrl
        PvworldLoc = worldLoc
        return IK_ctrls,IK_ctrl_cons,PvUpperJt,PvworldLoc,Paw_Length_Cvs

    def PawRiggingFunction(self,pawJts,Ankle,About='',ikType=''):
        #Start
        shoulder = pawJts[0]
        upper = pawJts[1]
        lower = pawJts[2]
        end = pawJts[3]
        foot = pawJts[4]
        claw = pawJts[5]
        clawEnd = pawJts[6]
        #ikfkSwitch
        ikfkSwitch = self.cvsCtrl(size=0.2*self.gbScale,name=self.chrName+'_'+About+'_'+ikType+'_ikfkSwitch',ctrlType='diamond')
        switchGrp = pm.group(ikfkSwitch,n=ikfkSwitch+'_cons')
        self.snap(end,switchGrp,rot=0)
        switchGrp.setAttr('translateX',switchGrp.translateX.get()-(pawJts[2].translateY.get()/2))
        pm.pointConstraint(end,switchGrp,mo=1)
        self.lockAttrs(ikfkSwitch,attrs=['tx','ty','tz','rx','ry','rz','sx','sy','sz','v'])
        self.addSwitch(ikfkSwitch,name='ikfk',at='float',dv=1,min=0,max=1)
        self.addSwitch(ikfkSwitch,name='Auto_IK_Stretchy',at='float',dv=1,min=0,max=1)
        self.addSwitch(ikfkSwitch,name='Auto_Sqiash_Stretchy',at='float',dv=1,min=0,max=1)
        self.addSwitch(ikfkSwitch,name=ikType+'_Paw_Width',at='float',dv=1,min=0,max=10)
        self.addSwitch(ikfkSwitch,name='ikDisplay',at='float',dv=1,min=0,max=1)
        self.addSwitch(ikfkSwitch,name='fkDisplay',at='float',dv=1,min=0,max=1)
        ikfkSwitch.setAttr('ikDisplay',keyable=0,channelBox=1)
        ikfkSwitch.setAttr('fkDisplay',keyable=0,channelBox=1)
        #Create_IKFK_Joint
        for x in pawJts[4:]:
            x.setAttr('segmentScaleCompensate',0)
        pm.parent(upper,w=1)
        end.setAttr('drawStyle',2)
        clawEnd.setAttr('drawStyle',2)
        paws = pawJts[1:]
        ikList = self.IKFKJointCopy(paws,name='IK')
        fkList = self.IKFKJointCopy(paws,name='FK')
        for x in range(len(ikList)):
            self.blendColorNode(ikfkSwitch+'.ikfk',ikList[x]+'.rotate',fkList[x]+'.rotate',paws[x]+'.rotate')
            self.blendColorNode(ikfkSwitch+'.ikfk',ikList[x]+'.translate',fkList[x]+'.translate',paws[x]+'.translate')
            self.blendColorNode(ikfkSwitch+'.ikfk',ikList[x]+'.scale',fkList[x]+'.scale',paws[x]+'.scale')
        #IK_Function
        IK_ctrls,IK_ctrl_cons,PvUpperJt,PvworldLoc,Paw_Length_Cvs = self.Quadrupeds_IK_Function(ikList,Ankle,ikfkSwitch,About=About,ikType=ikType)
        IK_grp = pm.group(IK_ctrl_cons,n=self.chrName+'_'+About+'_'+ikType+'_IK_grp')
        pm.delete(Ankle)
        #FK_Function
        fk_to_constraint = fkList[0:3] 
        fk_to_constraint += fkList[4:-1]
        FK_ctrls,FK_ctrl_uppers,FK_ctrl_cons = self.setCtrl(fk_to_constraint,size=0.3*self.gbScale,lock=['tx','ty','tz','sx','sy','sz','v'],ctrlType='circle',rotateOrder=1)
        FK_grp = pm.group(FK_ctrl_cons[0],n=self.chrName+'_'+About+'_'+ikType+'_FK_grp')
        FK_ctrls[2].setAttr('scaleX',l=0,k=1)
        FK_ctrls[2].setAttr('scaleY',l=0,k=1)
        FK_ctrls[2].setAttr('scaleZ',l=0,k=1)
        pm.scaleConstraint(FK_ctrls[2],fk_to_constraint[2])
        #Shoulder_Function
        Shoulder_grps,Shoulder_ctrl = self.ctrlGrp(shoulder,size=0.75*self.gbScale,parent=1,lock=['sx','sy','sz','v'],ctrlType='circle',rotateOrder=1)[:2]
        #Connect_Parent_Group
        pm.connectAttr(ikfkSwitch+'.ikDisplay',IK_grp+'.visibility')
        pm.connectAttr(ikfkSwitch+'.fkDisplay',FK_grp+'.visibility')
        pm.parent(ikList[0],fkList[0],PvUpperJt,upper,shoulder)
        pm.parent(Paw_Length_Cvs,self.Data_Off)
        pm.parent(PvworldLoc,self.loc_grp)
        pm.parent(switchGrp,IK_grp,FK_grp,Shoulder_grps[1],self.ctrl_grp)
        return IK_ctrls,FK_ctrls,[Shoulder_ctrl],IK_ctrl_cons,FK_ctrl_cons,[Shoulder_grps[1]]

    def PelvisRiggingFunction(self,jts,pelvisNumber=4):
        pelvis = jts[0]
        upPelvis = jts[1]
        downPelvis = jts[2]
        chest = jts[3]
        hip = jts[4]
        spinal = jts[5]
        #Create_Ctrl
        Pelvis_grps,Pelvis_ctrl = self.ctrlGrp(pelvis,size=1.5*self.gbScale,parent=0,lock=[],ctrlType='arCircle',rotateOrder=1)[:2]
        upPelvis_grps,upPelvis_ctrl = self.ctrlGrp(upPelvis,size=1.25*self.gbScale,parent=0,depth=0.25,lock=[],ctrlType='pyramid',rotateOrder=1)[:2]
        downPelvis_grps,downPelvis_ctrl = self.ctrlGrp(downPelvis,size=1.25*self.gbScale,parent=0,depth=0.25,lock=[],ctrlType='pyramid',rotateOrder=1)[:2]
        Chest_grps,Chest_ctrl = self.ctrlGrp(chest,size=1*self.gbScale,parent=0,lock=[],ctrlType='arCircle',rotateOrder=1)[:2]
        Spinal_grps,Spinal_ctrl = self.ctrlGrp(spinal,size=1.25*self.gbScale,parent=0,lock=[],ctrlType='arCircle',rotateOrder=1)[:2]
        Hip_grps,Hip_ctrl = self.ctrlGrp(hip,size=1.25*self.gbScale,parent=0,lock=[],ctrlType='arCircle',rotateOrder=1)[:2]
        ctrls = [Pelvis_ctrl,Chest_ctrl,Spinal_ctrl,Hip_ctrl,upPelvis_ctrl]
        for x in ctrls:
            x.setRotation([-90,0,0])
            pm.select(x)
            pm.makeIdentity(apply=1,r=1)
            self.lockAttrs(x,attrs=['sx','sy','sz','v'])
        downPelvis_ctrl.setRotation([90,0,0])
        pm.select(downPelvis_ctrl)
        pm.makeIdentity(apply=1,r=1)
        self.lockAttrs(downPelvis_ctrl,attrs=['sx','sy','sz','v'])
        pm.delete(spinal)
        #Ctrl_Parent
        pm.parent(upPelvis_grps[1],downPelvis_grps[1],Pelvis_ctrl)
        pm.parent(Spinal_grps[1],upPelvis_ctrl)
        pm.parent(Chest_grps[1],Spinal_ctrl)
        pm.parent(Hip_grps[1],downPelvis_ctrl)
        #AddAttr_Constraint
        self.addSwitch(Pelvis_ctrl,name='sub_ctrl',at='float',dv=0,min=0,max=1)
        self.addSwitch(Chest_ctrl,name='Auto_Stretchy',at='float',dv=1,min=0,max=1)
        self.addSwitch(Chest_ctrl,name='Auto_Sqiash_Stretchy',at='float',dv=1,min=0,max=1)
        self.addSwitch(Chest_ctrl,name='Chest_Width',at='float',dv=1,min=0,max=10)
        pm.connectAttr(Pelvis_ctrl+'.sub_ctrl',downPelvis_ctrl.listRelatives(c=1)[0]+'.visibility')
        pm.connectAttr(Pelvis_ctrl+'.sub_ctrl',upPelvis_ctrl.listRelatives(c=1)[0]+'.visibility')
        pm.parentConstraint(Pelvis_ctrl,pelvis)
        pm.parentConstraint(Chest_ctrl,chest)
        pm.parentConstraint(Hip_ctrl,hip)
        pm.parent(Pelvis_grps[1],self.ctrl_grp)
        #Create_Spinal_Joint
        spinals = []
        spinalDis = chest.translateZ.get()/(pelvisNumber-1)
        for x in range(pelvisNumber):
            jt = pm.duplicate(upPelvis,n=self.chrName+'_spinal_1',po=1)[0]
            pm.parent(jt,w=1)
            spinals.append(jt)
            if len(spinals) > 1:
                pm.parent(spinals[x],spinals[x-1])
                spinals[x].setAttr('translateZ',spinalDis)
        self.jointOrient(spinals,[1,0,0],[0,1,0],[0,1,0])
        pm.parent(spinals[0],self.rigJoint_grp)
        upPelvis.setAttr('drawStyle',2)
        spinals[-1].setAttr('drawStyle',2)
        #Spinal_IK_Function
        IK_spline,IK_spline_effector,IK_spline_Cvs = pm.ikHandle(sj=spinals[0],ee=spinals[-1],n=self.chrName+'_splineIk',sol='ikSplineSolver')
        IK_spline.hide()
        IK_spline_Cvs.rename(self.chrName+'_splineIk_Cvs')
        SpinalClu_chest = pm.cluster(IK_spline_Cvs+'.cv[3]')[1]
        SpinalClu_spinal = pm.cluster(IK_spline_Cvs+'.cv[1]',IK_spline_Cvs+'.cv[2]')[1]
        SpinalClu_upPelvis = pm.cluster(IK_spline_Cvs+'.cv[0]')[1]
        pm.parent(IK_spline,Chest_ctrl)
        pm.parent(SpinalClu_chest,Chest_ctrl)
        pm.parent(SpinalClu_spinal,Spinal_ctrl)
        pm.parent(SpinalClu_upPelvis,upPelvis_ctrl)
        pm.parent(IK_spline_Cvs,self.Data_Off)
        for x in [SpinalClu_chest,SpinalClu_spinal,SpinalClu_upPelvis]:
            x.hide()
        spline_Length_CvsInfo = pm.arclen(IK_spline_Cvs,ch=1)
        SplinePlus = self.Stretchy_Joint(Chest_ctrl,spline_Length_CvsInfo,Stretchy_axis='X',\
            Switch_Attr=['Auto_Stretchy','Auto_Sqiash_Stretchy','Chest_Width'],extrusion=1)
        for x in spinals:
            pm.connectAttr(SplinePlus+'.output3D',x+'.scale')
        #Create_List
        Pelvis_ctrl_List = Pelvis_ctrl,upPelvis_ctrl,downPelvis_ctrl,Chest_ctrl,Spinal_ctrl,Hip_ctrl
        Pelvis_cons_List = Pelvis_grps[1],upPelvis_grps[1],downPelvis_grps[1],Chest_grps[1],Spinal_grps[1],Hip_grps[1]
        return Pelvis_ctrl_List,Pelvis_cons_List

    def TailRiggingFunction(self,jts,pelvisNumber=6):
        upperTail = jts[0]
        Tail_1 = jts[1]
        Tail_2 = jts[2]
        Tail_end = jts[3]
        #Create_Spinal_Joint
        tail_spinals = []
        spinalDis = Tail_end.translateZ.get()/(pelvisNumber-1)
        for x in range(pelvisNumber):
            jt = pm.duplicate(upperTail,n=self.chrName+'_tail_spinal_1',po=1)[0]
            pm.parent(jt,w=1)
            tail_spinals.append(jt)
            if len(tail_spinals) > 1:
                pm.parent(tail_spinals[x],tail_spinals[x-1])
                tail_spinals[x].setAttr('translateZ',spinalDis)
        self.jointOrient(tail_spinals,[1,0,0],[0,1,0],[0,1,0])
        pm.parent(tail_spinals[0],self.rigJoint_grp)
        tail_spinals[0].setAttr('drawStyle',2)
        Tail_end.setAttr('drawStyle',2)
        tail_spinals[-1].setAttr('drawStyle',2)
        #Create_Ctrl
        upperTail_grps,upperTail_ctrl = self.ctrlGrp(upperTail,size=1*self.gbScale,parent=0,lock=['sx','sy','sz'],ctrlType='circle',rotateOrder=1)[:2]
        tail_grps_1,tail_ctrl_1 = self.ctrlGrp(Tail_1,size=0.5*self.gbScale,parent=0,lock=['sx','sy','sz'],ctrlType='circle',rotateOrder=1)[:2]
        tail_grps_2,tail_ctrl_2 = self.ctrlGrp(Tail_2,size=0.5*self.gbScale,parent=0,lock=['sx','sy','sz'],ctrlType='circle',rotateOrder=1)[:2]
        pm.delete(Tail_1,Tail_2,Tail_end)
        #Ctrl_Parent
        pm.parent(tail_grps_2[1],tail_ctrl_1)
        pm.parent(tail_grps_1[1],upperTail_ctrl)
        #AddAttr_Constraint
        self.addSwitch(upperTail_ctrl,name='Auto_Stretchy',at='float',dv=1,min=0,max=1)
        self.addSwitch(upperTail_ctrl,name='Auto_Sqiash_Stretchy',at='float',dv=1,min=0,max=1)
        self.addSwitch(upperTail_ctrl,name='Tail_Width',at='float',dv=1,min=0,max=10)
        pm.parent(upperTail_grps[1],self.ctrl_grp)
        pm.parentConstraint(upperTail_ctrl,upperTail)
        #Spinal_IK_Function
        IK_tail,IK_tail_effector,IK_tail_Cvs = pm.ikHandle(sj=tail_spinals[0],ee=tail_spinals[-1],n=self.chrName+'_tailIk',sol='ikSplineSolver')
        IK_tail.hide()
        IK_tail_Cvs.rename(self.chrName+'_tailIk_Cvs')
        TailClu_upperTail = pm.cluster(IK_tail_Cvs+'.cv[0]')[1]
        TailClu_tail_1 = pm.cluster(IK_tail_Cvs+'.cv[1]')[1]
        TailClu_tail_2 = pm.cluster(IK_tail_Cvs+'.cv[2]',IK_tail_Cvs+'.cv[3]')[1]
        pm.parent(IK_tail,upperTail_ctrl)
        pm.parent(TailClu_upperTail,upperTail_ctrl)
        pm.parent(TailClu_tail_1,tail_ctrl_1)
        pm.parent(TailClu_tail_2,tail_ctrl_2)
        pm.parent(IK_tail_Cvs,self.Data_Off)
        for x in [TailClu_upperTail,TailClu_tail_1,TailClu_tail_2]:
            x.hide()
        spline_Length_CvsInfo = pm.arclen(IK_tail_Cvs,ch=1)
        SplinePlus = self.Stretchy_Joint(upperTail_ctrl,spline_Length_CvsInfo,Stretchy_axis='X',\
            Switch_Attr=['Auto_Stretchy','Auto_Sqiash_Stretchy','Tail_Width'],extrusion=1)
        for x in tail_spinals:
            pm.connectAttr(SplinePlus+'.output3D',x+'.scale')
        #Create_List
        Tail_ctrl_List = upperTail_ctrl,tail_ctrl_1,tail_ctrl_2
        Tail_cons_List = upperTail_grps[1],tail_grps_1[1],tail_grps_2[1]
        return Tail_ctrl_List,Tail_cons_List

    def Quadrupeds_NeckRiggingFunction(self,jts,pelvisNumber=4):
        #Create_Spinal_Joint
        Neck = jts[0]
        Head = jts[1]
        #Create_Spinal_Joint
        neck_spinals = []
        spinalDis = Head.translateY.get()/(pelvisNumber-1)
        for x in range(pelvisNumber):
            jt = pm.duplicate(Neck,n=self.chrName+'_neck_spinal_1',po=1)[0]
            pm.parent(jt,w=1)
            neck_spinals.append(jt)
            if len(neck_spinals) > 1:
                pm.parent(neck_spinals[x],neck_spinals[x-1])
                neck_spinals[x].setAttr('translateY',spinalDis)
        self.jointOrient(neck_spinals,[0,1,0],[0,0,1],[0,0,1])
        pm.parent(neck_spinals[0],self.rigJoint_grp)
        neck_spinals[0].setAttr('drawStyle',2)
        neck_spinals[-1].setAttr('drawStyle',2)
        #Create_Ctrl
        neck_grps,neck_ctrl = self.ctrlGrp(Neck,size=0.75*self.gbScale,parent=0,lock=['sx','sy','sz'],ctrlType='circle',rotateOrder=1)[:2]
        head_grps,head_ctrl = self.ctrlGrp(Head,size=1*self.gbScale,parent=0,lock=['sx','sy','sz'],ctrlType='circle',rotateOrder=1)[:2]
        #AddAttr_Constraint
        self.addSwitch(head_ctrl,name='Auto_Stretchy',at='float',dv=1,min=0,max=1)
        self.addSwitch(head_ctrl,name='Auto_Sqiash_Stretchy',at='float',dv=1,min=0,max=1)
        self.addSwitch(head_ctrl,name='Neck_Width',at='float',dv=1,min=0,max=10)
        pm.parent(neck_grps[1],self.ctrl_grp)
        pm.parent(head_grps[1],self.ctrl_grp)
        pm.parentConstraint(head_ctrl,Head)
        pm.parentConstraint(neck_ctrl,Neck)
        #Spinal_IK_Function
        IK_neck,IK_neck_effector,IK_neck_Cvs = pm.ikHandle(sj=neck_spinals[0],ee=neck_spinals[-1],n=self.chrName+'_neckIk',sol='ikSplineSolver')
        IK_neck.hide()
        IK_neck_Cvs.rename(self.chrName+'_splineIk_Cvs')
        NeckClu_1 = pm.cluster(IK_neck_Cvs+'.cv[2]',IK_neck_Cvs+'.cv[3]')[1]
        NeckClu_2 = pm.cluster(IK_neck_Cvs+'.cv[0]',IK_neck_Cvs+'.cv[1]')[1]
        pm.parent(IK_neck,neck_ctrl)
        pm.parent(NeckClu_1,head_ctrl)
        pm.parent(NeckClu_2,neck_ctrl)
        pm.parent(IK_neck_Cvs,self.Data_Off)
        for x in [NeckClu_1,NeckClu_2]:
            x.hide()
        spline_Length_CvsInfo = pm.arclen(IK_neck_Cvs,ch=1)
        SplinePlus = self.Stretchy_Joint(head_ctrl,spline_Length_CvsInfo,Stretchy_axis='Y',\
            Switch_Attr=['Auto_Stretchy','Auto_Sqiash_Stretchy','Neck_Width'],extrusion=1)
        for x in neck_spinals:
            pm.connectAttr(SplinePlus+'.output3D',x+'.scale')
        #Create_List
        Neck_ctrl_List = neck_ctrl,head_ctrl
        Neck_cons_List = neck_grps[1],head_grps[1]
        return Neck_ctrl_List,Neck_cons_List

    def Quadrupeds_StartRigging(self):
        name = self.Quadrupeds_resetName()
        jts = ([],[],[],[],[],[],[],[])
        for x in range(len(jts)):
            for y in name[x]:
                try:
                    jt = pm.PyNode(self.chrName+'_'+y)
                    jts[x].append(jt)
                except:
                    pass
        rigJoints = jts[1][0],jts[3][0],jts[3][7],jts[4][0],jts[4][7],\
            jts[5][0],jts[5][7],jts[6][0],jts[6][7],jts[7][0]
        for x in rigJoints:
            pm.parent(x,w=1)
        #PelvisRiggingFunction
        Pelvis_Rig = self.PelvisRiggingFunction(jts[0],pelvisNumber=4)
        #PawRiggingFunction
        L_frontPaw = jts[3][:-1]
        R_frontPaw = jts[4][:-1]
        L_backPaw = jts[5][:-1]
        R_backPaw = jts[6][:-1]
        L_frontPaw_Rig = self.PawRiggingFunction(L_frontPaw,jts[3][7],About='L',ikType='front')
        R_frontPaw_Rig = self.PawRiggingFunction(R_frontPaw,jts[4][7],About='R',ikType='front')
        L_backPaw_Rig = self.PawRiggingFunction(L_backPaw,jts[5][7],About='L',ikType='back')
        R_backPaw_Rig = self.PawRiggingFunction(R_backPaw,jts[6][7],About='R',ikType='back')
        pm.parentConstraint(jts[3][0],L_frontPaw_Rig[3][1],mo=1)
        pm.parentConstraint(jts[4][0],R_frontPaw_Rig[3][1],mo=1)
        pm.parentConstraint(jts[5][0],L_backPaw_Rig[3][1],mo=1)
        pm.parentConstraint(jts[6][0],R_backPaw_Rig[3][1],mo=1)
        pm.parent(L_frontPaw_Rig[5][0],Pelvis_Rig[0][3])
        pm.parent(R_frontPaw_Rig[5][0],Pelvis_Rig[0][3])
        pm.parent(L_backPaw_Rig[5][0],Pelvis_Rig[0][5])
        pm.parent(R_backPaw_Rig[5][0],Pelvis_Rig[0][5])
        #TailRiggingFunction
        Tail_Rig = self.TailRiggingFunction(jts[7],pelvisNumber=6)
        pm.parent(Tail_Rig[1][0],Pelvis_Rig[0][5])
        #Quadrupeds_NeckRiggingFunction
        Neck_Rig = self.Quadrupeds_NeckRiggingFunction(jts[1],pelvisNumber=4)
        jts[1][2].setAttr('drawStyle',2)
        pm.parent(Neck_Rig[1][0],Pelvis_Rig[0][3])
        #EyeRiggingFunction
        Eye_Rig = self.eyeDoCtrl([jts[2][0],jts[2][1]],Neck_Rig[0][1])
        pm.parent(Eye_Rig[2][2],self.ctrl_grp)
        #EarRiggingFunction
        L_ear_grps,L_ear_ctrl = self.ctrlGrp(jts[2][4],size=0.5*self.gbScale,lock=['sx','sy','sz'],ctrlType='circle',rotateOrder=1)[:2]
        R_ear_grps,R_ear_ctrl = self.ctrlGrp(jts[2][5],size=0.5*self.gbScale,lock=['sx','sy','sz'],ctrlType='circle',rotateOrder=1)[:2]
        jts[2][6].setAttr('drawStyle',2)
        jts[2][7].setAttr('drawStyle',2)
        pm.parent(L_ear_grps[1],R_ear_grps[1],Neck_Rig[0][1])
        #MonthRiggingFunction
        MonthRig = self.mouthDoCtrl([jts[2][2],jts[2][3]],Neck_Rig[0][1])
        jts[2][3].setAttr('drawStyle',2)
        #ctrlFollow設定
        L_frontPawFollow = jts[0][0],jts[3][0]
        R_frontPawFollow = jts[0][0],jts[4][0]
        L_backPawFollow = jts[0][0],jts[5][0]
        R_backPawFollow = jts[0][0],jts[6][0]
        headFollow = jts[0][0],jts[1][0]
        eyeFollow = jts[1][0],jts[1][1]
        L_frontPawIK_Locs = self.ctrlFollow(L_frontPaw_Rig[0][0],L_frontPawFollow,ctrlType='ik')
        L_frontPawFK_Locs = self.ctrlFollow(L_frontPaw_Rig[1][0],L_frontPawFollow,ctrlType='fk')
        R_frontPawIK_Locs = self.ctrlFollow(R_frontPaw_Rig[0][0],R_frontPawFollow,ctrlType='ik')
        R_frontPawFK_Locs = self.ctrlFollow(R_frontPaw_Rig[1][0],R_frontPawFollow,ctrlType='fk')
        L_backPawIK_Locs = self.ctrlFollow(L_backPaw_Rig[0][0],L_backPawFollow,ctrlType='ik')
        L_backPawFK_Locs = self.ctrlFollow(L_backPaw_Rig[1][0],L_backPawFollow,ctrlType='fk')
        R_backPawIK_Locs = self.ctrlFollow(R_backPaw_Rig[0][0],R_backPawFollow,ctrlType='ik')
        R_backPawFK_Locs = self.ctrlFollow(R_backPaw_Rig[1][0],R_backPawFollow,ctrlType='fk')
        headFollow_Locs = self.ctrlFollow(Neck_Rig[0][1],headFollow,ctrlType='fk')
        eyeFollow_Locs = self.ctrlFollow(Eye_Rig[0][2],eyeFollow,ctrlType='ik')
        pm.parent(L_frontPawIK_Locs,L_frontPawFK_Locs,R_frontPawIK_Locs,R_frontPawFK_Locs,\
            L_backPawIK_Locs,L_backPawFK_Locs,R_backPawIK_Locs,R_backPawFK_Locs,\
            headFollow_Locs,eyeFollow_Locs,self.loc_grp)
        #JointParent
        pm.parent(jts[1][0],jts[3][0],jts[4][0],jts[0][3])
        pm.parent(jts[5][0],jts[6][0],jts[7][0],jts[0][4])
        pm.parent(jts[0][0],self.rigJoint_grp)
        pm.select(cl=1)

    ####################VertexRigging工具####################

    def getUParam(self,pnt = [], crv = None):
        point = OpenMaya.MPoint(pnt[0],pnt[1],pnt[2])
        curveFn = OpenMaya.MFnNurbsCurve(self.getDagPath(crv))
        paramUtill=OpenMaya.MScriptUtil()
        paramPtr=paramUtill.asDoublePtr()
        isOnCurve = curveFn.isPointOnCurve(point)
        if isOnCurve == True:
            curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )
        else :
            point = curveFn.closestPoint(point,paramPtr,0.001,OpenMaya.MSpace.kObject)
            curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )
        param = paramUtill.getDouble(paramPtr)  
        return param
    
    def getDagPath(self,objectName):
        if isinstance(objectName, list)==True:
            oNodeList=[]
            for o in objectName:
                selectionList = OpenMaya.MSelectionList()
                selectionList.add(o)
                oNode = OpenMaya.MDagPath()
                selectionList.getDagPath(0, oNode)
                oNodeList.append(oNode)
            return oNodeList
        else:
            selectionList = OpenMaya.MSelectionList()
            selectionList.add(objectName)
            oNode = OpenMaya.MDagPath()
            selectionList.getDagPath(0, oNode)
            return oNode
    
    def vertexToJoint(self,point,Loc='',aimObj='',conType='',name=''):
        verJts = []
        centerJts = []
        locs = []
        for x in range(len(point)):
            pm.select(cl=1)
            verJt = pm.joint(p=pm.xform(point[x],q=1,ws=1,t=1),n=name+'_verJt_'+str(x+1))
            pm.select(cl=1)
            center = pm.joint(p=pm.xform(Loc,q=1,ws=1,t=1),n=name+'_center_'+str(x+1))
            center.setAttr('drawStyle',2)
            pm.joint(center,e=1,oj='xyz',sao='yup',ch=1,zso=1)
            loc=pm.spaceLocator(n=name+'_loc_1')
            loc.setAttr('translate',pm.xform(point[x],q=1,ws=1,t=1))
            pm.parent(verJt,center)
            pm.aimConstraint(loc,center,mo=1,aim=(1,0,0),u=(0,1,0),wut='object',wuo=aimObj)
            if conType == 'point':
                pm.pointConstraint(loc,center,mo=1)
            else:
                pass
            verJts.append(verJt)
            centerJts.append(center)
            locs.append(loc)
        verJt_grp = pm.group(centerJts,n=name+'_verJt_grp',w=1)
        loc_grp = pm.group(locs,n=name+'_verLoc_grp',w=1)
        return verJts,locs
    
    def cvsToLoc(self,loc,pos,name=''):
        cvs = str(pm.curve(d=1,n=name+'_cvs',ep=(pos)))
        for i in loc:
            pos = pm.xform(i,q=1,ws=1,t=1)
            u = self.getUParam(pos,cvs)
            pci = pm.createNode('pointOnCurveInfo',n=name+'_pci_1')
            pm.connectAttr(cvs+'.worldSpace',pci+'.inputCurve')
            pm.setAttr(pci+'.parameter',u)
            pm.connectAttr(pci+'.position',i+'.t')
        return cvs
    
    def setAimLoc(self,verName):
        loc = pm.spaceLocator(n=verName+'_loc')
        aimLoc = pm.spaceLocator(n=verName+'_aimLoc')
        aim_Loc_shape = aimLoc.getChildren()[0]
        aim_Loc_shape.setAttr('localScale',[0.5,0.5,0.5])
        return loc,aimLoc
    
    def SET_UpVertex(self,loc,aimLoc,conType=''):
        up_point = pm.ls(os=True,fl=1)
        up_verJts,up_locs = self.vertexToJoint(up_point,Loc=loc,aimObj=aimLoc,conType=conType,name=self.verName+'_up')
        up_pos = []
        for x in up_point:
            up_pos.append(pm.xform(x,q=1,ws=1,t=1))
        up_high_cvs = self.cvsToLoc(up_locs,up_pos,name=self.verName+'_up_high')
        up_low_cvs = pm.duplicate(up_high_cvs,n=up_high_cvs.replace('high','low'))[0]
        pm.rebuildCurve(up_low_cvs,rt=0,d=3,kr=4)
        pm.wire(up_high_cvs,wire=str(up_low_cvs))
        up_base_wire = pm.PyNode(str(up_low_cvs)+'BaseWire')
        pm.select(cl=1)
        return up_verJts,up_locs,up_high_cvs,up_low_cvs,up_base_wire
    
    def SET_DownVertex(self,loc,aimLoc,conType=''):
        down_point = pm.ls(os=True,fl=1)
        down_verJts,down_locs = self.vertexToJoint(down_point,Loc=loc,aimObj=aimLoc,conType=conType,name=self.verName+'_down')
        down_pos = []
        for y in down_point:
            down_pos.append(pm.xform(y,q=1,ws=1,t=1))
        down_high_cvs = self.cvsToLoc(down_locs,down_pos,name=self.verName+'_down_high')
        down_low_cvs = pm.duplicate(down_high_cvs,n=down_high_cvs.replace('high','low'))[0]
        pm.rebuildCurve(down_low_cvs,rt=0,d=3,kr=4)
        pm.wire(down_high_cvs,wire=str(down_low_cvs))
        down_base_wire = pm.PyNode(str(down_low_cvs)+'BaseWire')
        pm.select(cl=1)
        return down_verJts,down_locs,down_high_cvs,down_low_cvs,down_base_wire
    
    def SET_Match(self,up_verJts,up_locs,up_high_cvs,up_low_cvs,up_base_wire,down_verJts,down_locs,down_high_cvs,down_low_cvs,down_base_wire):
        for jts in up_verJts:
            jts.setAttr('radius',self.verSize)
        for jts in down_verJts:
            jts.setAttr('radius',self.verSize)
        verLoc_grp = pm.group(em=1,n=self.verName+'_verLoc_grp')
        verLoc_grp.setAttr('visibility',0)
        pm.parent(self.ver_aimLoc,up_locs[0].getParent(1),down_locs[0].getParent(1),verLoc_grp)
        verJt_grp = pm.group(em=1,n=self.verName+'_verJt_grp')
        pm.select(cl=1)
        main_verJt = pm.joint(p=pm.xform(self.ver_loc,q=1,ws=1,t=1),rad=self.verSize,n=self.verName+'_verJt')
        pm.parent(main_verJt,up_verJts[0].getParent(2),down_verJts[0].getParent(2),verJt_grp)
        cvs_grp = pm.group(em=1,n=self.verName+'_verCvs_grp')
        cvs_grp.setAttr('visibility',0)
        pm.parent(up_high_cvs,down_high_cvs,up_low_cvs,down_low_cvs,up_base_wire,down_base_wire,cvs_grp)
        pm.delete(self.ver_loc)
        CVs = up_low_cvs.getCVs()
        CVs.remove(CVs[1])
        CVs.remove(CVs[5])
        for x in down_low_cvs.getCVs()[2:5]:
            CVs.append(x)
        skinJts = []
        skinJts_grp = pm.group(n=self.verName+'_skinJt_grp',em=1)
        skinJts_grp.setAttr('visibility',0)
        verCtrl_grp = pm.group(n=self.verName+'_verCtrl_grp',em=1)
        for y in range(len(CVs)):
            pm.select(cl=1)
            skinjt = pm.joint(p=[0,0,0],n=self.verName+'_skinJt_'+str(y+1),rad=self.verSize)
            jtCons = pm.group(n=str(skinjt)+'_cons',w=1)
            jtCons.setAttr('translate',CVs[y])
            pm.parent(skinjt,jtCons)
            skinJts.append(skinjt)
            ctrls = self.ctrlGrp(skinjt,size=self.verSize,parent=0,lock=['rx','ry','rz','sx','sy','sz','v'],ctrlType='circleZ')
            ctrls[0][0].rename(ctrls[0][0].replace('_skinJt_','_ver_'))
            ctrls[0][1].rename(ctrls[0][1].replace('_skinJt_','_ver_'))
            ctrls[1].rename(ctrls[1].replace('_skinJt_','_ver_'))
            pm.connectAttr(ctrls[1]+'.translate',skinjt+'.translate')
            pm.parent(ctrls[0][1],verCtrl_grp)
            pm.parent(jtCons,skinJts_grp)
            self.MultiplyDivideNode(1,ctrls[1]+'.translate',(-1,-1,-1),ctrls[0][0]+'.translate',Channel=4)
        pm.skinCluster(skinJts[:5],up_low_cvs)
        pm.skinCluster(skinJts[0],skinJts[4:8],down_low_cvs)
        all_grp = pm.group(em=1,n=self.verName+'_ver_grp')
        pm.parent(verJt_grp,cvs_grp,skinJts_grp,verLoc_grp,verCtrl_grp,all_grp)

    def Blink_and_Zoom(self,tgt,ctrl,cvs,nullRotate=''):
        up_low_cvs,down_low_cvs,up_high_cvs,down_high_cvs = cvs
        #def_low
        up_def_low_cvs = pm.duplicate(up_low_cvs,n=up_low_cvs.replace('low','def_low'))[0]
        down_def_low_cvs = pm.duplicate(down_low_cvs,n=down_low_cvs.replace('low','def_low'))[0]
        #blink_low
        up_blink_low_cvs = pm.duplicate(up_low_cvs,n=up_low_cvs.replace('low','blink_low'))[0]
        down_blink_low_cvs = pm.duplicate(down_low_cvs,n=down_low_cvs.replace('low','blink_low'))[0]
        #blink_high
        up_blink_high_cvs = pm.duplicate(up_high_cvs,n=up_high_cvs.replace('high','blink_high'))[0]
        down_blink_high_cvs = pm.duplicate(down_high_cvs,n=down_high_cvs.replace('high','blink_high'))[0]
        #blink_low_cvs_BS
        up_blink_low_cvs_BS = pm.blendShape(down_def_low_cvs,up_blink_low_cvs,n=self.verName+'_up_blink_low_cvs_BS')[0]
        down_blink_low_cvs_BS = pm.blendShape(up_def_low_cvs,down_blink_low_cvs,n=self.verName+'_down_blink_low_cvs_BS')[0]
        #blink_high_wire
        pm.wire(up_blink_high_cvs,wire=str(up_blink_low_cvs))
        pm.wire(down_blink_high_cvs,wire=str(down_blink_low_cvs))
        #blink_high_cvs_BS
        up_blink_high_cvs_BS = pm.blendShape(up_blink_high_cvs,up_high_cvs,n=self.verName+'_up_blink_high_cvs_BS')[0]
        down_blink_high_cvs_BS = pm.blendShape(down_blink_high_cvs,down_high_cvs,n=self.verName+'_down_blink_high_cvs_BS')[0]
        up_blink_high_cvs_BS.setAttr(str(up_blink_high_cvs),1)
        down_blink_high_cvs_BS.setAttr(str(down_blink_high_cvs),1)
        #AddAttr_to_ctrl
        top = tgt.listRelatives(p=1)[0]
        tran = tgt.getTranslation(space='world')
        rot = tgt.getRotation(space='world')
        ver_info = pm.spaceLocator(n=self.verName+'_ver_info')
        ver_info.setAttr('translate',tran)
        ver_info.setAttr('rotate',rot)
        pm.parent(ver_info,tgt)
        ver_null = pm.group(n=self.verName+'_null',em=1)
        ver_cons = pm.group(n=self.verName+'_cons')
        ver_cons.setAttr('translate',tran)
        ver_cons.setAttr('rotate',rot)
        pm.parent(ver_cons,top)
        pm.orientConstraint(ver_info,ver_null,mo=1)
        self.addSwitch(ctrl,name='blink',at='float',dv=0,min=0,max=1,k=1)
        ctrl.setAttr('blink',keyable=0,channelBox=1)
        self.addSwitch(ctrl,name='up_blink',at='float',dv=0,min=0,max=10)
        self.addSwitch(ctrl,name='down_blink',at='float',dv=0,min=0,max=10)
        self.addSwitch(ctrl,name='blinkRange',at='float',dv=0,min=-90,max=90,k=1)
        self.addSwitch(ctrl,name='zoomRange',at='float',dv=0,min=-90,max=90,k=1)
        self.addSwitch(ctrl,name='eyelashesRange',at='float',dv=0,min=-90,max=90,k=1)
        ctrl.setAttr('blinkRange',25)
        ctrl.setAttr('zoomRange',-30)
        ctrl.setAttr('eyelashesRange',25)
        pm.select(up_high_cvs)
        up_high_cvs_shape = pm.ls(sl=1)[0].listRelatives()[0]
        upCon = up_high_cvs_shape.listConnections()
        for x in upCon:
            if x.nodeType()=='blendShape':
                up_BlendShape = x
            elif x.nodeType()=='tweak':
                up_Tweak = x
        pm.reorderDeformers(up_Tweak,up_BlendShape)
        pm.select(down_high_cvs)
        down_high_cvs_shape = pm.ls(sl=1)[0].listRelatives()[0]
        downCon = down_high_cvs_shape.listConnections()
        for x in downCon:
            if x.nodeType()=='blendShape':
                down_BlendShape = x
            elif x.nodeType()=='tweak':
                down_Tweak = x
        pm.reorderDeformers(down_Tweak,down_BlendShape)
        #Blink_and_Zoom
        up_blinkCN = self.MultiplyDivideNode(1,ctrl+'.up_blink',0.1,None,Channel=1)
        down_blinkCN = self.MultiplyDivideNode(1,ctrl+'.down_blink',0.1,None,Channel=1)
        BlinkCN = self.clampNode(ver_null+'.'+nullRotate,ctrl+'.blinkRange',0,None,Channel=1)
        ZoomCN = self.clampNode(ver_null+'.'+nullRotate,0,ctrl+'.zoomRange',None,Channel=1)
        BlinkMD = self.MultiplyDivideNode(2,BlinkCN+'.outputR',ctrl+'.blinkRange',None,Channel=1)
        ZoomMD_1 = self.MultiplyDivideNode(2,ZoomCN+'.outputR',ctrl+'.zoomRange',None,Channel=1)
        ZoomMD_2 = self.MultiplyDivideNode(1,ZoomMD_1+'.outputX',-1,None,Channel=1)
        upLidBlinkCN_1 = self.clampNode(ZoomMD_2+'.outputX',0.2,0,None,Channel=1)
        upLidBlinkMD_1 = self.MultiplyDivideNode(1,upLidBlinkCN_1+'.outputR',-1,None,Channel=1)
        upLidBlinkCN_2 = self.clampNode(BlinkMD+'.outputX',1,0,None,Channel=1)
        upLidBlinkPlus = self.plusMinusAverageNode(1,upLidBlinkCN_2+'.outputR',upLidBlinkMD_1+'.outputX',None,Channel=1)
        downLidBlinkCN = self.clampNode(BlinkMD+'.outputX',1,0,None,Channel=1)
        up_blinkPlus = self.plusMinusAverageNode(1,up_blinkCN+'.outputX',0,up_blink_low_cvs_BS+'.'+self.verName+'_down_def_low_cvs',Channel=1)
        down_blinkPlus = self.plusMinusAverageNode(1,down_blinkCN+'.outputX',0,down_blink_low_cvs_BS+'.'+self.verName+'_up_def_low_cvs',Channel=1)
        pm.connectAttr(upLidBlinkPlus+'.output1D',up_blinkPlus+'.input1D[1]')
        for jt in self.up_verJts:
            verJtMD_1 = self.MultiplyDivideNode(1,up_blinkPlus+'.output1D',ctrl+'.eyelashesRange',jt+'.rotateX',Channel=1)

    ####################SubRig工具####################

    def CreateSubCtrl(self,ctrl,follower):
        tran = follower.getTranslation(space='world')
        rot = follower.getRotation(space='world')
        loc = pm.spaceLocator(n='LOC_'+str(follower))
        loc.setAttr('translate',tran)
        loc.setAttr('rotate',rot)
        subCtrl = self.cvsCtrl(size=self.subSize,name='sub_'+follower,ctrlType=self.ctrlType_comboBox.currentText())
        upper = pm.group(subCtrl,n=subCtrl+'_upper')
        cons = pm.group(upper,n=subCtrl+'_cons')
        self.snap(loc,cons)
        pm.parent(loc,subCtrl)
        loc.setAttr('visibility',0)
        pm.parentConstraint(ctrl,cons,mo=1)
        try:
            pm.parentConstraint(loc,follower,mo=1)
        except:
            try:
                pm.pointConstraint(loc,follower,mo=1)
            except:
                pm.orientConstraint(loc,follower,mo=1)
        return subCtrl,loc

    def CreatePathCtrl(self,cvs):
        tran = 'translateY'
        locs = []
        cons = []
        for x in cvs:
            cvsShape = x.getChildren()[0]
            loc = pm.shadingNode('locator',al=1)
            loc.rename(x+'_loc')
            cvsInfo = pm.arclen(x,ch=1)
            path = pm.shadingNode('motionPath',al=1,n=x+'_path')
            plus = pm.shadingNode('plusMinusAverage',al=1)
            md1 = pm.shadingNode('multiplyDivide',al=1)
            md2 = pm.shadingNode('multiplyDivide',al=1)
            pm.connectAttr(cvsShape+'.worldSpace',path+'.geometryPath')
            pm.connectAttr(path+'.allCoordinates',loc+'.translate')
            pm.connectAttr(path+'.rotate',loc+'.rotate')
            path.setAttr('fractionMode',1)
            self.addSwitch(loc,name='u_value',at='float',dv=0,min=0,max=1,k=1)
            pm.connectAttr(loc+'.u_value',plus+'.input1D[0]')
            pm.connectAttr(plus+'.output1D',path+'.uValue')
            grps,ctrl,parCon1,parCon2 = self.ctrlGrp(loc,size=self.subSize,parent=0,lock=['tx','tz','rx','ry','rz','sx','sy','sz','v'],ctrlType='sphere')
            pm.transformLimits(ctrl,ety=(1,0),ty=(0,1))
            pm.parentConstraint(loc,grps[1],mo=1)
            pm.connectAttr(ctrl+'.'+tran,md1+'.input1X')
            pm.connectAttr(cvsInfo+'.arcLength',md1+'.input2X')
            md1.setAttr('operation',2)
            pm.connectAttr(md1+'.outputX',plus+'.input1D[1]')
            pm.connectAttr(ctrl+'.'+tran,md2+'.input1X')
            pm.connectAttr(md2+'.outputX',grps[0]+'.'+tran)
            md2.setAttr('input2X',-1)
            locs.append(loc)
            cons.append(grps[1])
        pm.select(locs)
        locGrp = pm.group(n=cvs[0]+'_loc_grp',w=1)
        locGrp.setAttr('visibility',0)
        pm.select(cons)
        pm.group(n=cvs[0]+'_ctrl_grp',w=1)
        pm.select(cl=1)
        return ctrl,grps[0],grps[1]

    def renameChildren(self,grps):
        '''
        將選取的Group底層無子項目的transform物件改名為 Group_[流水號]
        '''
        for i in range(len(grps)):
            pm.select(grps[i].getChildren())
            tgt=pm.ls(sl=1)
            objList = []
            for x in tgt:
                if x.nodeType()=='joint':
                    objList.append(x)
                elif x.nodeType()=='transform':
                    try:
                        tgts = x.getChildren()[0]
                        if tgts.nodeType() != 'transform':
                            objList.append(x)
                    except:
                        pass
                elif x.nodeType()=='transform' and x.getChildren()[0] == False:
                    objList.append(x)
                else:
                    pass
            if str(grps[i][-3:]) =='grp' or str(grps[i][-3:]) =='GRP':
                for y in objList:
                    y.rename(grps[i][:-3]+'1')
                sys.stdout.write(u'已重新命名')
            else:
                sys.stdout.write(u'Group最後名稱改為_grp或是_GRP')
        pm.select(cl=1)

    def moveVertices(self,power):
        point = pm.ls(os=True)
        tranList = []
        for x in point:
            tran = x.getPosition(space = 'world')
            tranList.append(tran)
        for y in range(len(point)-1):
            point[y].setPosition(tranList[y]-(tranList[y]-tranList[y+1])*power)

    def ChangeObjUV(self,New,Old):
        Orig = Old.listRelatives()[1]
        Orig.setAttr('intermediateObject',0)
        pm.transferAttributes(New,Orig,pos=0,nml=0,uvs=2,col=2,spa=5,sm=3,fuv=0,clb=1)
        pm.delete(Orig,ch=1)
        Orig.setAttr('intermediateObject',1)

    ####################Facial_SetUp工具####################

    def facialList(self,bs,connect=0):
        names = bs.listConnections()
        nameList = []
        for name in names:
            if name.nodeType() == 'transform':
                if connect == 0:
                    try:
                        con = pm.listConnections(bs+'.'+str(name),d=1)
                        if len(con) == 0:
                            nameList.append(str(name))
                    except:
                        pass
                elif connect == 1:
                    nameList.append(str(name))
        return nameList

    def CreateQCheckBox(self,nameList):
        buttomList = []
        for name in nameList:
            Btn = QtGui.QCheckBox(ui.BS_List_WidgetContents)
            Btn.setText(str(name))
            buttomList.append(Btn)
            self.BS_List_WidgetContents.children()[0].addWidget(Btn)
        return buttomList

    def setBlendShapeToCtrl(self,ctrl,bs,bsName,dv=0,min=0,max=10):
        pm.select(ctrl)
        pm.addAttr(ln=bsName,at='float',dv=dv,min=min,max=max,k=1)
        MultiplyDivide = pm.shadingNode('multiplyDivide',al=1)
        MultiplyDivide.setAttr('operation',2)
        MultiplyDivide.setAttr('input2X',max)
        pm.connectAttr(ctrl+'.'+bsName,MultiplyDivide+'.input1X')
        pm.connectAttr(MultiplyDivide+'.outputX',bs+'.'+bsName)
        pm.select(ctrl)

    ####################DynamicsRigging####################

    def DynJointCtrls(self,Cvs,size):
        CvsShape = Cvs.listRelatives()[0]
        Cv = CvsShape.getCVs(space='preTransform')
        DynJtList = []
        SkinJtList = []
        for x in range(len(Cv)):
            pm.select(cl=1)
            Dynjt = pm.joint(n='Dyn_'+Cvs+'_'+str(x+1),p=Cv[x],rad=size)
            pm.select(cl=1)
            Skinjt = pm.joint(n='Skin_'+Cvs+'_'+str(x+1),p=Cv[x],rad=size)
            DynJtList.append(Dynjt)
            SkinJtList.append(Skinjt)
        self.jointOrient(DynJtList,[1,0,0],[0,1,0],[1,0,0])
        self.jointOrient(SkinJtList,[1,0,0],[0,1,0],[1,0,0])
        ctrlList,upperList,consList = self.setCtrl(SkinJtList[:-1],ctrlType='circle',size=size)
        for x in range(len(consList)):
            self.addSwitch(ctrlList[x],name='Dynamics',at='float',dv=1,min=0,max=1)
            MD = self.MultiplyDivideNode(1,(DynJtList[x]+'.rotateX',DynJtList[x]+'.rotateY',DynJtList[x]+'.rotateZ'),(ctrlList[x]+'.Dynamics',ctrlList[x]+'.Dynamics',ctrlList[x]+'.Dynamics'),upperList[x]+'.rotate',Channel=3)
        return consList[0],SkinJtList[0],DynJtList

    def CurveToDynCtrls(self,curves,size=1.0,hairName=''):
        ConList = []
        SkinJtList = []
        DynJtList = []
        DynTopList = []
        follicleList = []
        outputCvsList = []
        DynIkList = []
        for cvs in curves:
            con,skinJt,dynJts = self.DynJointCtrls(cvs,size)
            ConList.append(con)
            SkinJtList.append(skinJt)
            DynJtList.append(dynJts)
            DynTopList.append(dynJts[0])
        pm.select(curves)
        pm.runtime.MakeCurvesDynamic()
        for x in range(len(curves)):
            follicle = curves[x].listRelatives(p=1)[0].listRelatives(c=1)[0]
            outputCvs = follicle.outputs()[1]
            follicleList.append(follicle)
            outputCvsList.append(outputCvs)
        system = follicle.outputs()[0].listRelatives(c=1)[0]
        nucleus = system.outputs()[0]
        system.listRelatives(p=1)[0].rename(hairName+'_hairSystem')
        follicle.listRelatives(p=1)[0].listRelatives(p=1)[0].rename(hairName+'_Follicles')
        outputCvs.listRelatives(p=1)[0].rename(hairName+'_OutputCurves')
        for x in range(len(curves)):
            DynIk = pm.ikHandle(sj=DynJtList[x][0],ee=DynJtList[x][-1],c=outputCvsList[x],n=DynJtList[x][0]+'_ik',sol='ikSplineSolver',ccv=0,pcv=0)[0]
            DynIkList.append(DynIk)
            follicleList[x].setAttr('pointLock',1)
        system.setAttr('active',0)
        system.setAttr('stiffness',1)
        pm.select(DynTopList,SkinJtList,follicle.listRelatives(p=1)[0].listRelatives(p=1)[0],ConList)
        followGrp = pm.group(n=hairName+'_follow_grp')
        pm.select(system.listRelatives(p=1)[0],nucleus)
        cacheGrp = pm.group(n=hairName+'_cache_grp')
        pm.select(DynIkList,outputCvs.listRelatives(p=1)[0])
        dataGrp = pm.group(n=hairName+'_Data_grp')
        pm.hide(DynTopList,follicle.listRelatives(p=1)[0].listRelatives(p=1)[0],cacheGrp,dataGrp)

def joeyautoriggingMain():
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


joeyautoriggingMain()