# -*- coding: utf-8 -*-
import sys
sys.path.append("//Art-1405260002/d/assets/scripts/maya_scripts/lib")
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '//Art-1405260002/d/assets/scripts/web_scripts/ui/web_123rf_download.ui'
#
# Created: Thu Oct 06 14:35:07 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 74)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_lineEdit = QtGui.QLineEdit(Form)
        self.search_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.horizontalLayout.addWidget(self.search_lineEdit)
        self.quota_lineEdit = QtGui.QLineEdit(Form)
        self.quota_lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.quota_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.quota_lineEdit.setObjectName("quota_lineEdit")
        self.horizontalLayout.addWidget(self.quota_lineEdit)
        self.search_button = QtGui.QPushButton(Form)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout.addWidget(self.search_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.download_button = QtGui.QPushButton(Form)
        self.download_button.setEnabled(False)
        self.download_button.setObjectName("download_button")
        self.horizontalLayout_2.addWidget(self.download_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.search_lineEdit.setPlaceholderText(QtGui.QApplication.translate("Form", "搜尋關鍵字", None, QtGui.QApplication.UnicodeUTF8))
        self.quota_lineEdit.setText(QtGui.QApplication.translate("Form", "20", None, QtGui.QApplication.UnicodeUTF8))
        self.search_button.setText(QtGui.QApplication.translate("Form", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.download_button.setText(QtGui.QApplication.translate("Form", "下載", None, QtGui.QApplication.UnicodeUTF8))

