scripts_path = "//Art-1405260002/d/assets"
import sys
sys.path.append(scripts_path + "/scripts/maya_scripts/install")

import Qt
from Qt import QtCore, QtWidgets, QtGui

class lineEditWidget(QtWidgets.QLineEdit):
    def __init__(self, parent=None, mainWindowObj=None):
        QtWidgets.QLineEdit.__init__(self, parent)
        self.mainWindowObj = mainWindowObj

    def focusInEvent(self, e):
        try:
            import MaxPlus
            MaxPlus.CUI.DisableAccelerators()
        except:
            pass