'''
import subprocess
import fileinput

input = "//Art-1405260002/d/assets/scripts/tactic_scripts/ui/FbNotifier.ui"
output = "//Art-1405260002/d/assets/scripts/tactic_scripts/ui/FbNotifier_UI.py"
subprocess.call("C:/Python27/scripts/pyside-uic -o %s %s" % (output, input))

with open(output, 'r') as data:
    filedata = data.read()

header = "# -*- coding: utf-8 -*-\n"
header = header + "import sys\nsys.path.append(\"//Art-1405260002/d/assets/scripts/maya_scripts/lib\")\n"

filedata = header + filedata
with open(output, 'w') as data:
    data.write(filedata)

python "//Art-1405260002/d/assets/scripts/tactic_scripts/FbNotifier.py"

pyinstaller --onefile --noconsole --windowed  --hidden-import=xmlrpclib  --hidden-import=hashlib --icon=//Art-1405260002/d/assets/scripts/tactic_scripts/icon/kiwi.ico FbNotifier.py
'''
import sys
scripts_path = "//Art-1405260002/d/assets"
sys.path.append(scripts_path +  "/client")
sys.path.append(scripts_path + "/scripts/tactic_scripts/ui")
from fogbugz import FogBugz
from dateutil import parser
import time, pytz, datetime, socket

import FbNotifier_UI
from tactic_client_lib import TacticServerStub
import Skype4Py
from PySide import QtCore, QtGui

server = TacticServerStub(setup=False)

tactic_server_ip = socket.gethostbyname("vg.com")

server.set_server(tactic_server_ip)
server.set_project("simpleslot")
ticket = server.get_ticket("julio", "1234")
server.set_ticket(ticket)

fb = FogBugz("https://fb.vir888.com")
fb.logon("ART-Julio", "chicago")

class MainWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = FbNotifier_UI.Ui_FbNotifier()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.listen)
        self.ui.tableWidget.setColumnWidth(0,150)
        self.ui.tableWidget.setColumnWidth(1,390)
        self.ui.tableWidget.setColumnWidth(2,80)
        self.ui.tableWidget.setColumnWidth(3,80)
        self.ui.tableWidget.setColumnWidth(4,80)

        self.ui.tableWidget.itemClicked.connect(self.skypeMessage)
        self.skype4py = None
        self.listener = ListenerThread()
        self.listener.signal.data.connect(self.updateStatus)
        self.listener.signal.clearTable.connect(self.clearTable)
        sshFile = scripts_path + "/scripts/maya_scripts/lib/darkorange.stylesheet"
        with open(sshFile, "r") as fh:
            self.setStyleSheet(fh.read())

    def skypeMessage(self):
        if self.ui.tableWidget.currentItem().background().color().name() == '#522222':
            row = self.ui.tableWidget.currentRow()
            skype = self.ui.tableWidget.item(row,4).text()
            msg = 'FB!'
            if self.skype4py == None:
                try:
                    self.skype4py = Skype4Py.Skype()
                    self.skype4py.Attach()
                except:
                    pass
            self.skype4py.SendMessage(skype, msg)

    def clearTable(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem('User'))
        self.ui.tableWidget.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem('Casename'))
        self.ui.tableWidget.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem('Estimate'))
        self.ui.tableWidget.setHorizontalHeaderItem(3, QtGui.QTableWidgetItem('Elapsed'))
        self.ui.tableWidget.setHorizontalHeaderItem(4, QtGui.QTableWidgetItem('Skype'))

    def listen(self):
        self.clearTable()
        if not self.listener.isRunning():
            self.listener.start()
        else:
            self.listener.terminate()
            self.listener.start()

    def updateStatus(self, data):
        user, casename, estimate, elapsed, dept_id, skype = data
        #print user, casename, estimate, elapsed
        #output = "%s %s %s %s" % (user.ljust(40), casename.ljust(80), str(int(estimate)).ljust(4), str(int(elapsed)).ljust(4))
        #qitem = QtGui.QListWidgetItem(output)
        if dept_id == 0:
            bgcolor = '#525242'
        elif dept_id == 1:
            bgcolor = '#425242'
        elif dept_id == 2:
            bgcolor = '#424252'

        if int(estimate) == 0 or int(elapsed) == 0:
            bgcolor = '#522222'
        if (elapsed - estimate) > 0:
            bgcolor = '#522222'

        rowPosition = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowPosition)

        userWidgetItem = QtGui.QTableWidgetItem(user)
        userWidgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
        userWidgetItem.setTextAlignment(QtCore.Qt.AlignVCenter)
        userWidgetItem.setBackground(QtGui.QColor(bgcolor))

        casenameWidgetItem = QtGui.QTableWidgetItem(casename)
        casenameWidgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
        casenameWidgetItem.setTextAlignment(QtCore.Qt.AlignVCenter)
        casenameWidgetItem.setBackground(QtGui.QColor(bgcolor))

        estimateWidgetItem = QtGui.QTableWidgetItem(str(int(estimate)))
        estimateWidgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
        estimateWidgetItem.setTextAlignment(QtCore.Qt.AlignVCenter)
        estimateWidgetItem.setBackground(QtGui.QColor(bgcolor))

        elapsedWidgetItem = QtGui.QTableWidgetItem(str(int(elapsed)))
        elapsedWidgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
        elapsedWidgetItem.setTextAlignment(QtCore.Qt.AlignVCenter)
        elapsedWidgetItem.setBackground(QtGui.QColor(bgcolor))

        skypeWidgetItem = QtGui.QTableWidgetItem(skype)
        skypeWidgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
        skypeWidgetItem.setTextAlignment(QtCore.Qt.AlignVCenter)
        skypeWidgetItem.setBackground(QtGui.QColor(bgcolor))

        self.ui.tableWidget.setRowHeight(rowPosition,20)
        self.ui.tableWidget.setItem(rowPosition, 0, userWidgetItem)

        self.ui.tableWidget.setRowHeight(rowPosition,20)
        self.ui.tableWidget.setItem(rowPosition, 1, casenameWidgetItem)

        self.ui.tableWidget.setRowHeight(rowPosition,20)
        self.ui.tableWidget.setItem(rowPosition, 2, estimateWidgetItem)

        self.ui.tableWidget.setRowHeight(rowPosition,20)
        self.ui.tableWidget.setItem(rowPosition, 3, elapsedWidgetItem)

        self.ui.tableWidget.setRowHeight(rowPosition,20)
        self.ui.tableWidget.setItem(rowPosition, 4, skypeWidgetItem)

        #self.ui.listWidget.addItem(qitem)


#%%
class MySignal(QtCore.QObject):
    data = QtCore.Signal(list)
    clearTable = QtCore.Signal()

class ListenerThread(QtCore.QThread):
    global outputQueue
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.listening = True
        self.signal = MySignal()

    def getActive(self, user, dept_id, skype):
        resp = fb.search(q='assignedto:"' + user + '" status:"Active"', cols='ixBug,sTitle,hrsElapsed,hrsCurrEst,dtOpened')
        alldates = []
        for case in resp.cases.findAll('case'):
            opened = case.dtopened.string.encode('UTF-8')
            alldates.append(parser.parse(opened))

        now = datetime.datetime.now(pytz.utc)

        youngest = max(dt for dt in alldates if dt < now).date()

        for case in resp.cases.findAll('case'):
            code, casename, elapsed, estimate, opened = (case.ixbug.string.encode('UTF-8'),case.stitle.string.encode('UTF-8'),case.hrselapsed.string.encode('UTF-8'), case.hrscurrest.string.encode('UTF-8'), case.dtopened.string.encode('UTF-8'))
            opened_date = parser.parse(opened).date()
            if opened_date == youngest:
                data = [user, casename.decode('utf-8'), float(estimate), float(elapsed), dept_id, skype]
                self.signal.data.emit(data)

    def run(self):
        expr = "@SOBJECT(sthpw/login['department','3d']['section','model'])"
        model = server.eval(expr)

        expr = "@SOBJECT(sthpw/login['department','3d']['section','animation'])"
        animation = server.eval(expr)

        expr = "@SOBJECT(sthpw/login['department','3d']['section','game'])"
        gaming = server.eval(expr)
        while self.listening == True:
            for user in gaming:
                fb_name = user['fogbugz_id']
                try:
                    self.getActive(fb_name, 0, user['skype'])
                except:
                    print "shit"

            for user in model:
                fb_name = user['fogbugz_id']
                try:
                    self.getActive(fb_name, 1,  user['skype'])
                except:
                    print "shit"

            for user in animation:
                fb_name = user['fogbugz_id']
                try:
                    self.getActive(fb_name, 2,  user['skype'])
                except:
                    print "shit"

            time.sleep(3600)
            self.signal.clearTable.emit()




#%%
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    app.exec_()


