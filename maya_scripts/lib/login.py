import sys
sys.path.append("//Art-1405260002/d/assets/scripts/maya_scripts/lib")
sys.path.append("//Art-1405260002/d/assets/client")

from PySide import QtCore, QtGui
import qt_login_ui
reload(qt_login_ui)

import os
app = QtGui.QApplication.instance()
appName = app.objectName()

server = ""
class loginWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(loginWindow, self).__init__(parent)
        self.setFocus()
        self.setWindowFlags(QtCore.Qt.Tool)
        self.ui = qt_login_ui.Ui_login_window()
        self.ui.setupUi(self)
        self.ui.login_button.clicked.connect(self.login)
        sshFile="//Art-1405260002/d/assets/scripts/maya_scripts/lib/darkorange.stylesheet"     
        with open(sshFile,"r") as fh:
            self.setStyleSheet(fh.read())   

    def login(self):
        global server
        from tactic_client_lib import TacticServerStub

        ticket_path = "c:/sthpw/etc"
        
        if os.path.exists(ticket_path) is False:
            os.makerdirs(ticket_path)

        name = self.ui.login.text()
        password = self.ui.password.text()

        ticket_files = os.listdir("c:/sthpw/etc/")
        ticket_file = "c:/sthpw/etc/" + name + ".tacticrc"

        if len(ticket_files) == 0: 
            file_object = open(ticket_file, "w")
            ticket_content = "login=" + name + "\n" + "server=192.168.201.10" + "\n" + "project=simpleslot"
            file_object.write(ticket_content)
            file_object.close()
            
        server = TacticServerStub(setup=0)
        server.login = name
        server.set_server("192.168.201.10")
        server.set_project("simpleslot")        
        try:
            ticket = server.get_ticket(name, password)
            server.set_ticket(ticket)
            file_object = open(ticket_file, "w")
            ticket_content = "login=" + name + "\n" + "server=192.168.201.10" + "\n" + "ticket=" + ticket + "\n" + "project=simpleslot"
            file_object.write(ticket_content)
            file_object.close()            
            print "ok"
        except:
            print "error"
        loginWidget.close()
        
        
    def loginProcess(self):
        global loginWidget

        if appName == "3dsmax":
            import MaxPlus
            MaxPlus.CUI.DisableAccelerators()

        loginWidget = loginWindow(parent=QtGui.QApplication.activeWindow())

        if appName == "3dsmax":
            _GCProtector.widgets.append(loginWidget)
            loginWidget.setWindowFlags(loginWidget.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
            capsule = loginWidget.effectiveWinId()
            ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
            ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
            ptr = ctypes.pythonapi.PyCObject_AsVoidPtr(capsule)
            #MaxPlus.Win32.Set3dsMaxAsParentWindow(ptr)

        loginWidget.show()

#loginProcess()