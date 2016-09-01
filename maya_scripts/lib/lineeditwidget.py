from PySide import QtCore, QtGui

class lineEditWidget(QtGui.QLineEdit):
    def __init__(self, parent=None, mainWindowObj=None):
        QtGui.QLineEdit.__init__(self, parent)
        self.mainWindowObj = mainWindowObj

    def focusInEvent(self, e):
        try:
            import MaxPlus
            MaxPlus.CUI.DisableAccelerators()
        except:
            pass