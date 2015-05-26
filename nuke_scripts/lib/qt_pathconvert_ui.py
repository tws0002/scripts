# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nk_path_convert.ui'
#
# Created: Thu Apr 09 09:34:49 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_pathConvert(object):
    def setupUi(self, pathConvert):
        pathConvert.setObjectName("pathConvert")
        pathConvert.resize(683, 199)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        pathConvert.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(pathConvert)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtGui.QTableWidget(pathConvert)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.search_label = QtGui.QLabel(pathConvert)
        self.search_label.setMinimumSize(QtCore.QSize(60, 0))
        self.search_label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.search_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.search_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.search_label.setObjectName("search_label")
        self.horizontalLayout_2.addWidget(self.search_label)
        self.search = QtGui.QLineEdit(pathConvert)
        self.search.setObjectName("search")
        self.horizontalLayout_2.addWidget(self.search)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.replace_label = QtGui.QLabel(pathConvert)
        self.replace_label.setMinimumSize(QtCore.QSize(60, 0))
        self.replace_label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.replace_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.replace_label.setObjectName("replace_label")
        self.horizontalLayout_3.addWidget(self.replace_label)
        self.replace = QtGui.QLineEdit(pathConvert)
        self.replace.setBaseSize(QtCore.QSize(0, 0))
        self.replace.setObjectName("replace")
        self.horizontalLayout_3.addWidget(self.replace)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.convert_all_button = QtGui.QPushButton(pathConvert)
        self.convert_all_button.setObjectName("convert_all_button")
        self.horizontalLayout.addWidget(self.convert_all_button)
        self.refresh_button = QtGui.QPushButton(pathConvert)
        self.refresh_button.setObjectName("refresh_button")
        self.horizontalLayout.addWidget(self.refresh_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(pathConvert)
        QtCore.QMetaObject.connectSlotsByName(pathConvert)

    def retranslateUi(self, pathConvert):
        pathConvert.setWindowTitle(QtGui.QApplication.translate("pathConvert", "PathConvert", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("pathConvert", "Node", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("pathConvert", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.search_label.setText(QtGui.QApplication.translate("pathConvert", "search", None, QtGui.QApplication.UnicodeUTF8))
        self.replace_label.setText(QtGui.QApplication.translate("pathConvert", "replace", None, QtGui.QApplication.UnicodeUTF8))
        self.convert_all_button.setText(QtGui.QApplication.translate("pathConvert", "Convert All", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh_button.setText(QtGui.QApplication.translate("pathConvert", "Refresh", None, QtGui.QApplication.UnicodeUTF8))

