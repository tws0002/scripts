# pyside-uic -o //Art-1405260002/d/assets/scripts/tactic_scripts/lib/qt_mcd_file_upload_utility_ui.py //Art-1405260002/d/assets/scripts/tactic_scripts/ui/qt_mcd_file_upload_utility.ui

#qt_mcd_file_upload_utility
import sys
sys.path.append("//Art-1405260002/d/assets/client")
sys.path.append("//Art-1405260002/d/assets/scripts/tactic_scripts/lib")
sys.path.append("//Art-1405260002/d/assets/scripts/tactic_scripts/ui")
sys.path.append("//Art-1405260002/d/assets/scripts/tactic_scripts")

from PySide import QtCore, QtGui

import qt_mcd_file_upload_utility_ui


reload(qt_mcd_file_upload_utility_ui)

class mainWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Tool)
        self.ui = qt_mcd_file_upload_utility_ui.Ui_MainWindow()
        self.ui.setupUi(self)


widget = mainWindow(parent=QtGui.QApplication.activeWindow())
widget.ui.login_name.setText(login_name)
widget.show()
