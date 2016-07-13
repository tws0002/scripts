# -*- coding: utf-8 -*-
import sys
sys.path.append("//Art-1405260002/d/assets/scripts/maya_scripts/lib")
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '//Art-1405260002/d/assets/scripts/image_scripts/ui/sequence_crop.ui'
#
# Created: Tue Jul 12 16:05:36 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SequenceCrop(object):
    def setupUi(self, SequenceCrop):
        SequenceCrop.setObjectName("SequenceCrop")
        SequenceCrop.resize(633, 151)
        self.gridLayout_2 = QtGui.QGridLayout(SequenceCrop)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setContentsMargins(6, 12, 6, 12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.input_label = QtGui.QLabel(SequenceCrop)
        self.input_label.setMinimumSize(QtCore.QSize(100, 0))
        self.input_label.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Adobe Clean Light")
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.input_label.setFont(font)
        self.input_label.setAlignment(QtCore.Qt.AlignCenter)
        self.input_label.setIndent(0)
        self.input_label.setObjectName("input_label")
        self.horizontalLayout_4.addWidget(self.input_label)
        self.input_path = QtGui.QLineEdit(SequenceCrop)
        self.input_path.setMinimumSize(QtCore.QSize(400, 0))
        self.input_path.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.input_path.setText("")
        self.input_path.setObjectName("input_path")
        self.horizontalLayout_4.addWidget(self.input_path)
        self.input_folder_button = QtGui.QPushButton(SequenceCrop)
        self.input_folder_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/maya_scripts/icons/folder-open-o_d7801a_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.input_folder_button.setIcon(icon)
        self.input_folder_button.setIconSize(QtCore.QSize(12, 12))
        self.input_folder_button.setFlat(False)
        self.input_folder_button.setObjectName("input_folder_button")
        self.horizontalLayout_4.addWidget(self.input_folder_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.input_label_2 = QtGui.QLabel(SequenceCrop)
        self.input_label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.input_label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Adobe Clean Light")
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.input_label_2.setFont(font)
        self.input_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.input_label_2.setIndent(0)
        self.input_label_2.setObjectName("input_label_2")
        self.horizontalLayout_5.addWidget(self.input_label_2)
        self.input_path_2 = QtGui.QLineEdit(SequenceCrop)
        self.input_path_2.setMinimumSize(QtCore.QSize(400, 0))
        self.input_path_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.input_path_2.setObjectName("input_path_2")
        self.horizontalLayout_5.addWidget(self.input_path_2)
        self.input_folder_button_2 = QtGui.QPushButton(SequenceCrop)
        self.input_folder_button_2.setText("")
        self.input_folder_button_2.setIcon(icon)
        self.input_folder_button_2.setIconSize(QtCore.QSize(12, 12))
        self.input_folder_button_2.setFlat(False)
        self.input_folder_button_2.setObjectName("input_folder_button_2")
        self.horizontalLayout_5.addWidget(self.input_folder_button_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.progress_bar = QtGui.QProgressBar(SequenceCrop)
        self.progress_bar.setEnabled(True)
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName("progress_bar")
        self.verticalLayout_2.addWidget(self.progress_bar)
        self.status_line = QtGui.QLabel(SequenceCrop)
        self.status_line.setMinimumSize(QtCore.QSize(0, 23))
        self.status_line.setMaximumSize(QtCore.QSize(16777215, 23))
        self.status_line.setFrameShape(QtGui.QFrame.Panel)
        self.status_line.setLineWidth(1)
        self.status_line.setMidLineWidth(0)
        self.status_line.setAlignment(QtCore.Qt.AlignCenter)
        self.status_line.setObjectName("status_line")
        self.verticalLayout_2.addWidget(self.status_line)
        self.convert_button = QtGui.QPushButton(SequenceCrop)
        self.convert_button.setObjectName("convert_button")
        self.verticalLayout_2.addWidget(self.convert_button)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(SequenceCrop)
        QtCore.QMetaObject.connectSlotsByName(SequenceCrop)

    def retranslateUi(self, SequenceCrop):
        SequenceCrop.setWindowTitle(QtGui.QApplication.translate("SequenceCrop", "SequenceCrop - by Julio", None, QtGui.QApplication.UnicodeUTF8))
        self.input_label.setText(QtGui.QApplication.translate("SequenceCrop", "Input Path", None, QtGui.QApplication.UnicodeUTF8))
        self.input_label_2.setText(QtGui.QApplication.translate("SequenceCrop", "Output Path", None, QtGui.QApplication.UnicodeUTF8))
        self.status_line.setText(QtGui.QApplication.translate("SequenceCrop", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.convert_button.setText(QtGui.QApplication.translate("SequenceCrop", "Convert", None, QtGui.QApplication.UnicodeUTF8))


