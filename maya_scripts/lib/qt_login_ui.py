# -*- coding: utf-8 -*-

scripts_path = "//Art-1405260002/d/assets"

import sys
sys.path.append(scripts_path + "/scripts/maya_scripts/install")

import Qt
from Qt import QtCore, QtWidgets, QtGui

class Ui_login_window(object):
    def setupUi(self, login_window):
        login_window.setObjectName("login_window")
        login_window.resize(229, 100)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(login_window)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_label = QtWidgets.QLabel(login_window)
        self.login_label.setMinimumSize(QtCore.QSize(60, 0))
        self.login_label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.login_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_label.setObjectName("login_label")
        self.horizontalLayout.addWidget(self.login_label)
        self.login = QtWidgets.QLineEdit(login_window)
        self.login.setObjectName("login")
        self.horizontalLayout.addWidget(self.login)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.password_label = QtWidgets.QLabel(login_window)
        self.password_label.setMinimumSize(QtCore.QSize(60, 0))
        self.password_label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.password_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.password_label.setObjectName("password_label")
        self.horizontalLayout_2.addWidget(self.password_label)
        self.password = QtWidgets.QLineEdit(login_window)
        self.password.setBaseSize(QtCore.QSize(0, 0))
        self.password.setObjectName("password")
        self.horizontalLayout_2.addWidget(self.password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.login_button = QtWidgets.QPushButton(login_window)
        icon = QtGui.QIcon()
        icon.addPixmap(QtWidgets.QPixmap("//art-1405260002/d/assets/scripts/maya_scripts/icons/sign-in_222222_12.png"), QtWidgets.QIcon.Normal, QtWidgets.QIcon.Off)
        self.login_button.setIcon(icon)
        self.login_button.setObjectName("login_button")
        self.verticalLayout.addWidget(self.login_button)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)

    def retranslateUi(self, login_window):
        login_window.setWindowTitle(QtWidgets.QApplication.translate("login_window", "Tactic Login", None, QtWidgets.QApplication.UnicodeUTF8))
        self.login_label.setText(QtWidgets.QApplication.translate("login_window", "Login:", None, QtWidgets.QApplication.UnicodeUTF8))
        self.password_label.setText(QtWidgets.QApplication.translate("login_window", "Password:", None, QtWidgets.QApplication.UnicodeUTF8))
        self.login_button.setText(QtWidgets.QApplication.translate("login_window", "Login", None, QtWidgets.QApplication.UnicodeUTF8))

