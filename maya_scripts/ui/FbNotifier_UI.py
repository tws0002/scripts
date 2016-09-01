# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '//Art-1405260002/d/assets/scripts/tactic_scripts/ui/FbNotifier.ui'
#
# Created: Wed Aug 03 17:19:33 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FbNotifier(object):
    def setupUi(self, FbNotifier):
        FbNotifier.setObjectName("FbNotifier")
        FbNotifier.resize(400, 300)
        self.verticalLayout_2 = QtGui.QVBoxLayout(FbNotifier)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget = QtGui.QListWidget(FbNotifier)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.pushButton = QtGui.QPushButton(FbNotifier)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)

        self.retranslateUi(FbNotifier)
        QtCore.QMetaObject.connectSlotsByName(FbNotifier)

    def retranslateUi(self, FbNotifier):
        FbNotifier.setWindowTitle(QtGui.QApplication.translate("FbNotifier", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("FbNotifier", "Start", None, QtGui.QApplication.UnicodeUTF8))

