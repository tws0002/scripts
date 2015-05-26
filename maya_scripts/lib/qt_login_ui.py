# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tactic_login.ui'
#
# Created: Thu Apr 02 15:57:47 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_login_window(object):
    def setupUi(self, login_window):
        login_window.setObjectName("login_window")
        login_window.resize(229, 100)
        self.verticalLayout_2 = QtGui.QVBoxLayout(login_window)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_label = QtGui.QLabel(login_window)
        self.login_label.setMinimumSize(QtCore.QSize(60, 0))
        self.login_label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.login_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_label.setObjectName("login_label")
        self.horizontalLayout.addWidget(self.login_label)
        self.login = QtGui.QLineEdit(login_window)
        self.login.setObjectName("login")
        self.horizontalLayout.addWidget(self.login)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.password_label = QtGui.QLabel(login_window)
        self.password_label.setMinimumSize(QtCore.QSize(60, 0))
        self.password_label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.password_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.password_label.setObjectName("password_label")
        self.horizontalLayout_2.addWidget(self.password_label)
        self.password = QtGui.QLineEdit(login_window)
        self.password.setBaseSize(QtCore.QSize(0, 0))
        self.password.setObjectName("password")
        self.horizontalLayout_2.addWidget(self.password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.login_button = QtGui.QPushButton(login_window)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//art-1405260002/d/assets/scripts/maya_scripts/icons/sign-in_222222_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_button.setIcon(icon)
        self.login_button.setObjectName("login_button")
        self.verticalLayout.addWidget(self.login_button)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)

    def retranslateUi(self, login_window):
        login_window.setWindowTitle(QtGui.QApplication.translate("login_window", "Tactic Login", None, QtGui.QApplication.UnicodeUTF8))
        self.login_label.setText(QtGui.QApplication.translate("login_window", "Login:", None, QtGui.QApplication.UnicodeUTF8))
        self.password_label.setText(QtGui.QApplication.translate("login_window", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.login_button.setText(QtGui.QApplication.translate("login_window", "Login", None, QtGui.QApplication.UnicodeUTF8))

