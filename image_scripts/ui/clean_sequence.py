# -*- coding: utf-8 -*-
import sys
sys.path.append("//Art-1405260002/d/assets/scripts/maya_scripts/lib")
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '//Art-1405260002/d/assets/scripts/image_scripts/ui/clean_sequence.ui'
#
# Created: Mon Nov 21 14:57:20 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(941, 649)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.tableWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Clean / Merge Image Sequence Folders", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(1).setText(QtGui.QApplication.translate("Form", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Form", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Form", "New Column", None, QtGui.QApplication.UnicodeUTF8))

