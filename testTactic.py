from PySide import QtCore, QtGui
import jc_maya_aux_functions as jc
scripts_path = "//Art-1405260002/d/assets"
import sys
import subprocess
tactic_client_path = scripts_path + "/client"
sys.path.append(scripts_path + "/client")
sys.path.append(scripts_path + "/scripts/maya_scripts/lib")
sys.path.append(scripts_path + "/scripts/maya_scripts/ui")
sys.path.append(scripts_path + "/scripts/maya_scripts")
sys.path.append(scripts_path + "/scripts/maya_scripts/install")
sys.path.append(scripts_path + "/scripts/install")
sys.path.append(scripts_path + "/scripts/python-dateutil-2.3")
sys.path.append(scripts_path + "/scripts/six-1.8.0")

import jc_export_data_to_nuke
reload(jc_export_data_to_nuke)

app = QtGui.QApplication.activeWindow().parent() #active window is script editor
app.objectName() # mayawindow

widgets = app.children()
for widget in widgets:
    if widget.objectName() == 'main_window':
        w = widget

w.exportNuke()