'''

import subprocess
import fileinput

input = "//Art-1405260002/d/assets/scripts/maya_scripts/ui/qt_main_ui_v03.ui"
output = "//Art-1405260002/d/assets/scripts/maya_scripts/lib/qt_main_ui_v03.py"
subprocess.call("C:/Python27/scripts/pyside-uic -o %s %s" % (output, input))

with open(output, 'r') as data:
    filedata = data.read()

header = "# -*- coding: utf-8 -*-\n"
header = header + "import sys\nsys.path.append(\"//Art-1405260002/d/assets/scripts/maya_scripts/lib\")\n"

filedata = filedata.replace('../', '//Art-1405260002/d/assets/scripts/maya_scripts/')
filedata = filedata.replace("self.asset_process_list = processListWidget(self.assets_tab)", "self.asset_process_list = processListWidget(self.assets_tab, mainWindowObj=main_window)")
filedata = filedata.replace("self.shot_process_list = processListWidget(self.shots_tab)", "self.shot_process_list = processListWidget(self.shots_tab, mainWindowObj=main_window)")
filedata = filedata.replace("from processlistwidget import processListWidget", "import processlistwidget\nfrom processlistwidget import processListWidget\nreload(processlistwidget)")
filedata = filedata.replace("from lineeditwidget import lineEditWidget", "import lineeditwidget\nfrom lineeditwidget import lineEditWidget\nreload(lineeditwidget)")

filedata = header + filedata
with open(output, 'w') as data:
    data.write(filedata)

python "//Art-1405260002/d/assets/scripts/maya_scripts/qt_tactic_main.py"
'''
scripts_path = "//Art-1405260002/d/assets"
import sys
tactic_client_path = scripts_path + "/client"
sys.path.append(scripts_path + "/client")
sys.path.append(scripts_path + "/scripts/maya_scripts/lib")
sys.path.append(scripts_path + "/scripts/maya_scripts/ui")
sys.path.append(scripts_path + "/scripts/maya_scripts")
sys.path.append(scripts_path + "/scripts/maya_scripts/install")
sys.path.append(scripts_path + "/scripts/install")
sys.path.append(scripts_path + "/scripts/python-dateutil-2.3")
sys.path.append(scripts_path + "/scripts/six-1.8.0")
import datetime
import time
global server, widget
import Qt

from Qt import QtCore, QtWidgets, QtGui

from tactic_client_lib import TacticServerStub

import ctypes
import qt_main_ui_v03 as qt_main_ui
import qt_login_ui
import os, shutil
import subprocess
import socket
import jc_maya_aux_functions as jc
from dateutil import parser
try:
    import maya.cmds as cmds
except:
    pass
try:
    import MaxPlus
except:
    pass
    
reload(qt_main_ui)
reload(qt_login_ui)
reload(jc)

app = QtWidgets.QApplication.instance()
if not app:
    app = QtWidgets.QApplication([])

appName = app.objectName()
if "Maya" in app.applicationDisplayName():
    appName = "Maya"

notready_icon = QtGui.QIcon(scripts_path + '/scripts/maya_scripts/icons/proc_list/notready.png')
ready_icon = QtGui.QIcon(scripts_path + '/scripts/maya_scripts/icons/proc_list/ready.png')
inprogress_icon = QtGui.QIcon(scripts_path + '/scripts/maya_scripts/icons/proc_list/inprogress.png')
standby_icon = QtGui.QIcon(scripts_path + '/scripts/maya_scripts/icons/proc_list/standby.png')
review_icon = QtGui.QIcon(scripts_path + '/scripts/maya_scripts/icons/proc_list/review.png')
complete_icon = QtGui.QIcon(scripts_path + '/scripts/maya_scripts/icons/proc_list/complete.png')

class _GCProtector(object):
    widgets = []


class loginWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(loginWindow, self).__init__(parent)
        self.setFocus()
        self.setWindowFlags(QtCore.Qt.Tool)
        self.ui = qt_login_ui.Ui_login_window()
        self.ui.setupUi(self)
        self.ui.login_button.clicked.connect(self.login)
        self.ui.password.returnPressed.connect(self.login)
        if "Nuke" in appName:
            pass
        else:
            sshFile = scripts_path + "/scripts/maya_scripts/lib/darkorange.stylesheet"
            with open(sshFile, "r") as fh:
                self.setStyleSheet(fh.read())

    def login(self):
        from tactic_client_lib import TacticServerStub

        ticket_path = "c:/sthpw/etc"

        if os.path.exists(ticket_path) is False:
            os.makedirs(ticket_path)

        name = self.ui.login.text()
        password = self.ui.password.text()

        ticket_files = os.listdir("c:/sthpw/etc/")
        ticket_file = "c:/sthpw/etc/" + name + ".tacticrc"

        tactic_server_ip = socket.gethostbyname('vg.com')

        if len(ticket_files) == 0:
            file_object = open(ticket_file, "w")
            ticket_content = "login=" + name + "\n" + "server=" + tactic_server_ip + "\n" + "project=simpleslot"
            file_object.write(ticket_content)
            file_object.close()

        server = TacticServerStub(setup=0)
        server.login = name
        server.set_server(tactic_server_ip)
        server.set_project("simpleslot")
        ticket = server.get_ticket(name, password)
        server.set_ticket(ticket)

        file_object = open(ticket_file, "w")
        ticket_content = "login=" + name + "\n" + "server=" + tactic_server_ip + "\n" + "ticket=" + ticket + "\n" + "project=simpleslot"
        file_object.write(ticket_content)
        file_object.close()

        mainProcess(server=server)


class mainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Tool)
        self.ui = qt_main_ui.Ui_main_window()
        self.ui.setupUi(self)

        self.ui.project_list.itemSelectionChanged.connect(self.getItems)

        self.ui.tabProductionType.currentChanged.connect(self.getItems)
        self.ui.asset_list.itemClicked.connect(self.getProcess)
        self.ui.shot_list.itemClicked.connect(self.getProcess)

        self.ui.asset_process_list.itemClicked.connect(self.finalPath)
        self.ui.shot_process_list.itemClicked.connect(self.finalPath)

        self.ui.save_button.clicked.connect(self.tacticSave)
        self.ui.open_button.clicked.connect(self.tacticLoad)
        self.ui.file_list.itemDoubleClicked.connect(self.tacticLoad)
        self.ui.open_path_button.clicked.connect(self.openPath)
        self.ui.publish_button.clicked.connect(self.publishMaster)
        self.ui.logout_button.clicked.connect(self.logOut)

        self.ui.inprogress_button.clicked.connect(self.setInProgressFilter)
        self.ui.ready_button.clicked.connect(self.setReadyFilter)
        self.ui.complete_button.clicked.connect(self.setCompleteFilter)
        self.ui.recent_button.clicked.connect(self.setRecentFilter)

        self.ui.file_list.itemClicked.connect(self.getNotes)
        #self.ui.file_list.itemClicked.connect(self.getThumbnail)
        #self.ui.save_note.clicked.connect(self.saveNotes)
        self.ui.note_list.itemDoubleClicked.connect(self.delNotes)
        self.ui.note.returnPressed.connect(self.saveNotes)
        self.ui.note.setStyleSheet("""background-color: rgb(170,170,170);color: black;""")

        self.ui.filter_character.setToolTip(u"角色")
        self.ui.filter_vehicle.setToolTip(u"車")
        self.ui.filter_sets.setToolTip(u"場景")
        self.ui.filter_prop.setToolTip(u"道具")
        self.ui.filter_other.setToolTip(u"其它")

        self.ui.filter_all.clicked.connect(lambda: self.showItemByType(1))
        self.ui.filter_character.clicked.connect(lambda: self.showItemByType(2))
        self.ui.filter_vehicle.clicked.connect(lambda: self.showItemByType(3))
        self.ui.filter_sets.clicked.connect(lambda: self.showItemByType(4))
        self.ui.filter_prop.clicked.connect(lambda: self.showItemByType(5))
        self.ui.filter_other.clicked.connect(lambda: self.showItemByType(6))

        if "Nuke" in appName:
            pass
        else:
            sshFile = scripts_path + "/scripts/maya_scripts/lib/darkorange.stylesheet"
            with open(sshFile, "r") as fh:
                self.setStyleSheet(fh.read())

    def focusInEvent(self, event):
        #self.focus_in.emit()
        QtWidgets.QWidget.focusInEvent(self, event)

    def showItemByType(self, id):
        count = self.ui.asset_list.count()
        for i in range(0, count):
            self.ui.asset_list.item(i).setHidden(0)
            if id == 1:
                self.clearItemFilter()
                self.ui.filter_all.setChecked(True)
                self.ui.asset_list.item(i).setHidden(0)
            elif id == 2:
                self.clearItemFilter()
                self.ui.filter_character.setChecked(True)
                if self.ui.asset_list.item(i).background().color().name() != '#525252':
                    self.ui.asset_list.item(i).setHidden(1)
            elif id == 3:
                self.clearItemFilter()
                self.ui.filter_vehicle.setChecked(True)                
                if self.ui.asset_list.item(i).background().color().name() != '#494949':
                    self.ui.asset_list.item(i).setHidden(1)
            elif id == 4:
                self.clearItemFilter()
                self.ui.filter_sets.setChecked(True)                
                if self.ui.asset_list.item(i).background().color().name() != '#424242':
                    self.ui.asset_list.item(i).setHidden(1)
            elif id == 5:
                self.clearItemFilter()
                self.ui.filter_prop.setChecked(True)                
                if self.ui.asset_list.item(i).background().color().name() != '#393939':
                    self.ui.asset_list.item(i).setHidden(1)
            elif id == 6:
                self.clearItemFilter()
                self.ui.filter_other.setChecked(True)                
                if self.ui.asset_list.item(i).background().color().name() != '#323232':
                    self.ui.asset_list.item(i).setHidden(1)

    def clearItemFilter(self):
        self.ui.filter_all.setChecked(False)
        self.ui.filter_character.setChecked(False)
        self.ui.filter_vehicle.setChecked(False)
        self.ui.filter_sets.setChecked(False)
        self.ui.filter_prop.setChecked(False)
        self.ui.filter_other.setChecked(False)


    def getNotes(self):
        self.ui.note_list.clear()

        expr = "@GET(sthpw/task['search_code','%s']['process','%s'].description)" % (self.item['code'], self.task['process'])
        temp = self.server.eval(expr)[0]

        if temp != "":
            notes = temp.split("\n")
            for note in notes:
                filename, msg = note.split("#")
                msg_day, msd_month = msg.split(" ")[0].split("/")

                if filename == self.ui.file_list.currentItem().text().split("  ")[1]:
                    self.ui.note_list.addItem(msg)
                    self.ui.note_list.scrollToItem(self.ui.note_list.item(self.ui.note_list.count() - 1))
        self.getThumbnail()        



    def saveNotes(self, *args):
        if args:
            note = args[0]
        else:
            note = self.ui.note.text().replace("\n", "")

        name = self.server.login

        if note != "":
            expr = "@GET(sthpw/task['search_code','%s']['process','%s'].description)" % (self.item['code'], self.task['process'])
            temp = self.server.eval(expr)
            if temp != []:
                notes = temp[0].split("\n")
            if notes[0] == "":
                notes.pop(0)
            for task in self.tasks:
                if task.get('process') == self.task['process']:
                    sk = task.get('__search_key__')

            now = datetime.datetime.now()
            now = now.strftime("%m/%d %H:%M")
            note = self.ui.file_list.currentItem().text().split("  ")[1] + "#" + now + "(" + name + "):     " + note
            notes.append(note)
            notes = "\n".join(notes)
            data = {'description': notes}

            self.server.update(sk, data)
            self.getNotes()
            self.ui.note.clear()

    def delNotes(self):
        selected_note = self.ui.note_list.currentItem().text()
        expr = "@GET(sthpw/task['search_code','%s']['process','%s'].description)" % (self.item['code'], self.task['process'])
        temp = self.server.eval(expr)
        notes = temp[0].split("\n")
        new_notes = []
        
        # the following loop should be a single line, test later
        for task in self.tasks:
            if task.get('process') == self.task['process']:
                sk = task.get('__search_key__')
        for note in notes:
            note_ = note.split("#")[1]
            if selected_note == note_:
                pass
            else:
                new_notes.append(note)
        notes = "\n".join(new_notes)
        data = {'description': notes}

        self.server.update(sk, data)
        self.getNotes()
        self.ui.note.clear()

    def game_type_code_converter(self, game_type_code):
        game_type = ""
        if game_type_code == "GAME_TYPE00002":
            game_type = "casino"
        elif game_type_code == "GAME_TYPE00005":
            game_type = "video_conf"
        elif game_type_code == "GAME_TYPE00007":
            game_type = "training"
        elif game_type_code == "GAME_TYPE00009":
            game_type = "others"
        elif game_type_code == "GAME_TYPE00010":
            game_type = "cf"
        elif game_type_code == "GAME_TYPE00011":
            game_type = "sports"
        elif game_type_code == "GAME_TYPE00012":
            game_type = "lottery"
        elif game_type_code == "GAME_TYPE00014":
            game_type = "IPL"
        elif game_type_code == "GAME_TYPE00021":
            game_type = "database"
        return game_type

    def getProjects(self):
        recent = self.ui.recent_button.isChecked()
        inprogress = self.ui.inprogress_button.isChecked()
        ready = self.ui.ready_button.isChecked()
        complete = self.ui.complete_button.isChecked()

        self.ui.project_list.clear()
        expr = "@UNIQUE(@GET(simpleslot/save_log['timestamp','>','$10_DAY_AGO'].project))"
        recentG = self.server.eval(expr)

        expr = "@SOBJECT(simpleslot/game)"
        self.games = self.server.eval(expr)

        inprogressGames = []
        completeGames = []
        readyGames = []
        recentGames = []

        for game in self.games:
            if game['name'] in recentG:
                recentGames.append(game)
            if game['project_status'] == '.In Progress':
                inprogressGames.append(game)
            elif game['project_status'] == '.Complete':
                completeGames.append(game)
            elif game['project_status'] == '.Ready':
                readyGames.append(game)

        def projectList(games):
            games = sorted(games, key=lambda k: k['name'])
            for game in games:
                self.ui.project_list.addItem(game['name'])

        if inprogress is True:
            projectList(inprogressGames)
        elif ready is True:
            projectList(readyGames)
        elif complete is True:
            projectList(completeGames)
        elif recent is True:
            projectList(recentGames)
        
        self.clearItemFilter()

    def setProjectInfo(self, game):
        name_chn = QtWidgets.QTableWidgetItem(game['name_chn'])
        name_chn.setTextAlignment(QtCore.Qt.AlignHCenter)
        self.ui.project_info.setItem(0, 0, name_chn)

        game_type = QtWidgets.QTableWidgetItem(self.game_type_code_converter(game['game_type_code']))
        game_type.setTextAlignment(QtCore.Qt.AlignHCenter)
        self.ui.project_info.setItem(1, 0, game_type)

        project_coordinator = QtWidgets.QTableWidgetItem(game['project_coordinator'])
        project_coordinator.setTextAlignment(QtCore.Qt.AlignHCenter)
        self.ui.project_info.setItem(2, 0, project_coordinator)

        expr = "@FORMAT(@MIN(simpleslot/game['name','" + game['name'] + "'].sthpw/task.bid_start_date), '12-31-1999')"
        bsd = self.server.eval(expr)[0]
        bid_start_date = QtWidgets.QTableWidgetItem(bsd)
        bid_start_date.setTextAlignment(QtCore.Qt.AlignHCenter)
        self.ui.project_info.setItem(3, 0, bid_start_date)

        expr = "@FORMAT(@MIN(simpleslot/game['name','" + game['name'] + "'].sthpw/task.bid_end_date), '12-31-1999')"
        bed = self.server.eval(expr)[0]
        bid_end_date = QtWidgets.QTableWidgetItem(bed)
        bid_end_date.setTextAlignment(QtCore.Qt.AlignHCenter)
        self.ui.project_info.setItem(4, 0, bid_end_date)

    def clearUI(self):
        self.ui.asset_list.clear()
        self.ui.shot_list.clear()
        self.ui.asset_process_list.clear()
        self.ui.shot_process_list.clear()
        self.ui.file_list.clear()
        self.ui.note_list.clear()

    def getItems(self):
        self.clearUI()
        selected_game = self.ui.project_list.currentItem().text()

        #  find current game sobject
        for game in self.games:
            if selected_game == game['name']:
                self.game = game

        self.setProjectInfo(self.game)

        expr = "@SOBJECT(simpleslot/game['name','" + self.game['name'] + "'].simpleslot/3d)"
        self.casinos = sorted(self.server.eval(expr), key=lambda k: k['name'])
        self.casinos = sorted(self.casinos, key=lambda k: k['3d_type_code'])
        self.updateItemList(self.casinos)

        expr = "@SOBJECT(simpleslot/game['name','" + self.game['name'] + "'].simpleslot/assets)"
        self.assets = sorted(self.server.eval(expr), key=lambda k: k['name'])
        self.assets = sorted(self.assets, key=lambda k: k['asset_type_code'])
        self.updateItemList(self.assets)

        expr = "@SOBJECT(simpleslot/game['name','" + self.game['name'] + "'].simpleslot/shot)"
        self.shots = sorted(self.server.eval(expr), key=lambda k: k['name'])
        for shot in self.shots:
            self.ui.shot_list.addItem(shot['name'])

        # select first in item list if it contains anything
        production_type = self.productionType()
        if production_type == "assets":
            if self.ui.asset_list.count() != 0:
                self.ui.asset_list.setCurrentRow(0)
                self.ui.tabProductionType.setCurrentIndex(0)

        elif production_type == "shot":
            if self.ui.shot_list.count() != 0:
                self.ui.shot_list.setCurrentRow(0)
                self.ui.tabProductionType.setCurrentIndex(1)
        try:
            self.getProcess()
        except:
            pass

    def updateItemList(self, items):
        list_index = 0
        for item in items:
            self.ui.asset_list.addItem(item['name'])
            if '3d_type_code' in item:
                if item['3d_type_code'] == "3D_TYPE00002":
                    self.ui.asset_list.item(list_index).setBackground(QtGui.QColor('#525252'))
                elif item['3d_type_code'] == "3D_TYPE00003":
                    self.ui.asset_list.item(list_index).setBackground(QtGui.QColor('#393939'))
                elif item['3d_type_code'] == "3D_TYPE00004":
                    self.ui.asset_list.item(list_index).setBackground(QtGui.QColor('#424242'))
                elif item['3d_type_code'] == "3D_TYPE00005":
                    self.ui.asset_list.item(list_index).setBackground(QtGui.QColor('#424242'))
                elif item['3d_type_code'] == "3D_TYPE00006":
                    self.ui.asset_list.item(list_index).setBackground(QtGui.QColor('#424242'))
                elif item['3d_type_code'] == "3D_TYPE00007":
                    self.ui.asset_list.item(list_index).setBackground(QtGui.QColor('#424242'))
                elif item['3d_type_code'] == "3D_TYPE00008":
                    self.ui.asset_list.item(list_index).setBackground(QtGui.QColor('#424242'))
                elif item['3d_type_code'] == "3D_TYPE00009":
                    self.ui.asset_list.item(list_index).setBackground(QtGui.QColor('#424242'))
            elif 'asset_type_code' in item:
                if item['asset_type_code'] == "ASSET_TYPE00002":
                    self.ui.asset_list.item(list_index).setBackground(QtGui.QColor('#525252'))
                elif item['asset_type_code'] == "ASSET_TYPE00003":
                    self.ui.asset_list.item(list_index).setBackground(QtGui.QColor('#494949'))
                elif item['asset_type_code'] == "ASSET_TYPE00004":
                    self.ui.asset_list.item(list_index).setBackground(QtGui.QColor('#424242'))
                elif item['asset_type_code'] == "ASSET_TYPE00005":
                    self.ui.asset_list.item(list_index).setBackground(QtGui.QColor('#393939'))
                elif item['asset_type_code'] == "ASSET_TYPE00006":
                    self.ui.asset_list.item(list_index).setBackground(QtGui.QColor('#323232'))
            list_index = list_index + 1

    def productionType(self):
        if self.ui.tabProductionType.currentIndex() == 0:
            production_type = "assets"
        elif self.ui.tabProductionType.currentIndex() == 1:
            production_type = "shot"
        return production_type

    def getProcess(self):
        task_assigned = ""
        bid_start_date = ""
        bid_end_date = ""

        production_type = self.productionType()
        if production_type == "assets":
            selected = self.ui.asset_list.currentItem().text()
            items = self.casinos + self.assets
        elif production_type == "shot":
            selected = self.ui.shot_list.currentItem().text()
            items = self.shots

        self.item = [d for d in items if d['name'] == selected][0]

        expr = "@SOBJECT(sthpw/task['search_code','" + self.item['code'] + "'])"
        self.tasks = self.server.eval(expr)
        self.tasks = self.orderTasksByProcesses(self.tasks)

        if self.ui.asset_process_list.count() != 0:
            self.ui.asset_process_list.clear()
        if self.ui.shot_process_list.count() != 0:
            self.ui.shot_process_list.clear()

        for task in self.tasks:
            # task_assigned = task.get('assigned')
            # bid_start_date = task['bid_start_date'][5:-9]
            # bid_end_date = task['bid_end_date'][5:-9]

            process = task.get('process')
            status = task.get('status')
            if status == '.Not Ready':
                icon = notready_icon
            elif status == '.Ready':
                icon = ready_icon
            elif status == '.In Progress':
                icon = inprogress_icon
            elif status == '.Stand By':
                icon = standby_icon
            elif status == '.Review':
                icon = review_icon
            elif status == '.Complete':
                icon = complete_icon

            qitem = QtWidgets.QListWidgetItem(icon, process)
            self.ui.asset_process_list.addItem(qitem)

            qitem = QtWidgets.QListWidgetItem(icon, process)
            self.ui.shot_process_list.addItem(qitem)

        item_name_chn = self.item['description']

        if self.item.get('asset_type_code') is not None:
            self.item_type_code = self.item.get('asset_type_code')
        elif self.item.get('3d_type_code') is not None:
            self.item_type_code = self.item.get('3d_type_code')

        # get the current process list index from self.task, which is from the future
        selectedProcess = 0
        if hasattr(self, 'task'):
            for i, task in enumerate(self.tasks):
                if task.get('process') == self.task.get('process'):
                    selectedProcess = i
                    break
        else:
            selectedProcess = 0

        # update item info table
        if production_type == "assets":
            self.item_type = self.assetTypeCode(self.item_type_code)

            if self.ui.asset_list.count() != 0:
                self.ui.asset_process_list.setCurrentRow(selectedProcess)     # select first in process list if it contains anything

                widgetItem = QtWidgets.QTableWidgetItem(item_name_chn)
                widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.ui.asset_info.setItem(0, 0, widgetItem)

                widgetItem = QtWidgets.QTableWidgetItem(self.item_type)
                widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.ui.asset_info.setItem(1, 0, widgetItem)

                # widgetItem = QtWidgets.QTableWidgetItem(task_assigned)
                # widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                # self.ui.asset_info.setItem(2, 0, widgetItem)

                # widgetItem = QtWidgets.QTableWidgetItem(bid_start_date)
                # widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                # self.ui.asset_info.setItem(3, 0, widgetItem)

                # widgetItem = QtWidgets.QTableWidgetItem(bid_end_date)
                # widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                # self.ui.asset_info.setItem(4, 0, widgetItem)

        elif production_type == "shot":
            if self.ui.shot_list.count() != 0:
                self.ui.shot_process_list.setCurrentRow(selectedProcess)

                widgetItem = QtWidgets.QTableWidgetItem(item_name_chn)
                widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.ui.shot_info.setItem(0, 0, widgetItem)

                widgetItem = QtWidgets.QTableWidgetItem("None")
                widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.ui.shot_info.setItem(1, 0, widgetItem)



        try:
            self.finalPath()
        except:
            pass

    def orderTasksByProcesses(self, tasks):
        new = []
        production_type = self.productionType()
        if production_type == "shot":
            ordered = ['layout', 'animation', 'lighting', 'effects', 'simulation', 'comp', 'final']
        else:
            ordered = ['rough', 'concept', 'model', 'texture', 'rigging', 'animation', 'lighting', 'effects', 'layout', 'final']
        for order in ordered:
            for task in tasks:
                if task.get('process') == order:
                    new.append(task)
        return new

    # convert casino item type to new asset types
    def assetTypeCode(self, code):
        if code == "ASSET_TYPE00002":
            asset_type = "character"
        elif code == "ASSET_TYPE00003":
            asset_type = "vehicle"
        elif code == "ASSET_TYPE00004":
            asset_type = "set"
        elif code == "ASSET_TYPE00005":
            asset_type = "prop"
        elif code == "ASSET_TYPE00006":
            asset_type = "other"
        elif code == "3D_TYPE00002":
            asset_type = "character"
        elif code == "3D_TYPE00003":
            asset_type = "prop"
        elif code == "3D_TYPE00004":
            asset_type = "set"
        elif code == "3D_TYPE00005":
            asset_type = "set"
        elif code == "3D_TYPE00006":
            asset_type = "set"
        elif code == "3D_TYPE00007":
            asset_type = "set"
        elif code == "3D_TYPE00008":
            asset_type = "set"
        elif code == "3D_TYPE00009":
            asset_type = "set"
        else:
            asset_type = ""
        return asset_type

    def oldAssetTypeCode(self, code):
        if code == "ASSET_TYPE00002":
            asset_type = "character"
        elif code == "ASSET_TYPE00003":
            asset_type = "vehicle"
        elif code == "ASSET_TYPE00004":
            asset_type = "set"
        elif code == "ASSET_TYPE00005":
            asset_type = "prop"
        elif code == "ASSET_TYPE00006":
            asset_type = "other"
        elif code == "3D_TYPE00002":
            asset_type = "character"
        elif code == "3D_TYPE00003":
            asset_type = "symbol"
        elif code == "3D_TYPE00004":
            asset_type = "user_interface"
        elif code == "3D_TYPE00005":
            asset_type = "bonus01"
        elif code == "3D_TYPE00006":
            asset_type = "bonus02"
        elif code == "3D_TYPE00007":
            asset_type = "free_game"
        elif code == "3D_TYPE00008":
            asset_type = "jackpot"
        elif code == "3D_TYPE00009":
            asset_type = "introduction"
        else:
            asset_type = ""
        return asset_type

    def finalPath(self):
        self.old_path = ""
        self.old_base_filename = ""
        self.old_filename = ""

        base_path = "//mcd-server/art_3d_project/"
        login = self.server.login

        project = self.game['name']
        production_type = self.productionType()

        for task in self.tasks:
            if production_type == 'assets':
                if task.get('process') == self.ui.asset_process_list.currentItem().text():
                    self.task = task

                    widgetItem = QtWidgets.QTableWidgetItem(self.task['assigned'])
                    widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                    self.ui.asset_info.setItem(2, 0, widgetItem)

                    year, month, day = self.task['bid_start_date'].split(" ")[0].split("-")
                    widgetItem = QtWidgets.QTableWidgetItem(month + "-" + day + "-" + year)
                    widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                    self.ui.asset_info.setItem(3, 0, widgetItem)

                    year, month, day = self.task['bid_end_date'].split(" ")[0].split("-")
                    widgetItem = QtWidgets.QTableWidgetItem(month + "-" + day + "-" + year)
                    widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                    self.ui.asset_info.setItem(4, 0, widgetItem)                    

            elif production_type == 'shot':
                if task.get('process') == self.ui.shot_process_list.currentItem().text():
                    self.task = task

                    widgetItem = QtWidgets.QTableWidgetItem(self.task['assigned'])
                    widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                    self.ui.shot_info.setItem(2, 0, widgetItem)

                    year, month, day = self.task['bid_start_date'].split(" ")[0].split("-")
                    widgetItem = QtWidgets.QTableWidgetItem(month + "-" + day + "-" + year)
                    widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                    self.ui.shot_info.setItem(3, 0, widgetItem)
                    
                    year, month, day = self.task['bid_end_date'].split(" ")[0].split("-")
                    widgetItem = QtWidgets.QTableWidgetItem(month + "-" + day + "-" + year)
                    widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                    self.ui.shot_info.setItem(4, 0, widgetItem)                    
        self.sk = self.task['__search_key__']


        final_path = ""
        base_filename = ""
        filename = ""

        if appName == "3dsmax":
            ext = ".max"
        elif appName == "maya":
            ext = ".mb"
        elif "Nuke" in appName:
            ext = ".nk"
        elif appName == "python":
            ext = ""

        old_item_type = self.oldAssetTypeCode(self.item_type_code)

        if production_type == 'assets':
            final_path = base_path + project + "/" + production_type + "/" + self.item_type + "/" + self.item['name'] + "/" + self.task['process'] + "/scenes/"
            self.old_path = base_path + project + "/casino/" + old_item_type + "/" + self.item['name'] + "/" + self.task['process'] + "/scenes/"

            base_filename = jc.abbrName(project) + "_" + jc.abbrItemType(self.item_type) + "_" + self.item['name'] + "_" + jc.abbrName(self.task['process'])
            filename = jc.abbrName(project) + "_" + jc.abbrItemType(self.item_type) + "_" + self.item['name'] + "_" + jc.abbrName(self.task['process']) + "_" + jc.maxVersion(final_path, base_filename, "maya") + "_" + login + ext

            #backwards compat
            self.old_base_filename = jc.abbrName(project) + "_" + jc.abbrItemType(old_item_type) + "_" + self.item['name'] + "_" + jc.abbrName(self.task['process'])
            self.old_filename = jc.abbrName(project) + "_" + jc.abbrItemType(old_item_type) + "_" + self.item['name'] + "_" + jc.abbrName(self.task['process']) + "_" + jc.maxVersion(self.old_path, self.old_base_filename, "maya") + "_" + login + ext

        elif production_type == 'shot':
            final_path = base_path + project + "/" + production_type + "/" + self.item['name'] + "/" + self.task['process'] + "/scenes/"
            base_filename = jc.abbrName(project) + "_" + self.item['name'] + "_" + jc.abbrName(self.task['process'])
            filename = jc.abbrName(project) + "_" + self.item['name'] + "_" + jc.abbrName(self.task['process']) + "_" + jc.maxVersion(final_path, base_filename, "maya") + "_" + login + ext

        final_path = final_path.replace(" ", "")

        if production_type == "assets":
            if self.ui.asset_list.count() != 0 and self.ui.asset_process_list.count() != 0:
                self.ui.save_path.setText(final_path)
                self.ui.save_file.setText(filename)
        elif production_type == "shot":
            if self.ui.shot_list.count() != 0 and self.ui.shot_process_list.count() != 0:
                self.ui.save_path.setText(final_path)
                self.ui.save_file.setText(filename)

        self.getFiles(final_path, base_filename)
        self.base_filename = base_filename
        #self.resetLocks()

    def getFiles(self, final_path, base_filename):  # use getfilelist() and update ui
        fileList = []
        self.ui.file_list.clear()

        index = 0
        if os.path.exists(self.old_path) is True:
            oldFiles = os.listdir(self.old_path)
            if len(oldFiles) == 0:
                pass
            else:
                fileList = [x for x in oldFiles if self.old_base_filename in x]
                for filename in fileList:
                    filedate = time.strftime("%m/%d %H:%M", time.localtime(os.path.getmtime(self.old_path + filename)))
                    self.ui.file_list.addItem(filedate + "  " + filename)
                    self.ui.file_list.item(index).setBackground(QtGui.QColor('#725252'))
                    index = index + 1

        if os.path.exists(final_path) is True:
            savedFiles = os.listdir(final_path)
            if len(savedFiles) == 0:
                pass
            else:
                fileList = [x for x in savedFiles if base_filename in x]
                for filename in fileList:
                    filedate = time.strftime("%m/%d %H:%M", time.localtime(os.path.getmtime(final_path + filename)))
                    self.ui.file_list.addItem(filedate + "  " + filename)
                    index = index + 1

        file_list_count = self.ui.file_list.count()

        if file_list_count != 0:
            self.ui.file_list.setCurrentRow(file_list_count - 1)

        self.getNotes()

    def updateStatus(self):
        new = self.orderTasksByProcesses(self.tasks)

        datas = {}
        inprogress = {'status': '.In Progress', 'assigned': self.server.login}
        complete = {'status': '.Complete'}
        now = datetime.datetime.now()

        for i, task in enumerate(new):
            currentTask = self.task
            if task['process'] == currentTask['process']:
                if task['status'] == '.Not Ready' or task['status'] == '.Ready':
                    task_sk = task['__search_key__']
                    datas.update({task_sk: inprogress})

                while i != 0:
                    i -= 1
                    if new[i]['status'] != '.Complete':
                        past_sk = new[i]['__search_key__']
                        datas.update({past_sk: complete})

        self.server.update_multiple(datas, triggers=False)
        self.getProcess()

    def publishMaster(self, arg=None):
        def hasNumbers(inputString):
            return any(char.isdigit() for char in inputString)

        production_type = self.productionType()

        path = self.ui.save_path.text()
        if self.ui.file_list.currentItem().background().color().name() == '#725252':
            path = self.old_path

        filename = self.ui.file_list.currentItem().text().split("  ")[1]

        if production_type == 'assets':
            process = self.ui.asset_process_list.currentItem().text()
        elif production_type == 'shot':
            process = self.ui.shot_process_list.currentItem().text()
        
        base_path = path.split(process)[0]
        process = jc.abbrName(process)

        base, ext = filename.split(".")

        final = base.split(process)[0][:-1]

        master_path = base_path + "master"
        if os.path.exists(master_path) is False:
            os.makedirs(master_path)

        destination = master_path + "/" + final + "_master." + ext
        source = path + filename
        self.saveNotes(filename + u"設為MASTER檔")
        shutil.copy2(source, destination)

    def resetLocks(self):
        expr = "@GET(sthpw/task['search_code','%s']['process','%s'].description)" % (self.item['code'], self.task['process'])
        temp = self.server.eval(expr)[0]
        new_notes = []
        today = datetime.date.today()
        if temp != "":
            for task in self.tasks:
                if task.get('process') == self.task['process']:
                    sk = task.get('__search_key__')

            notes = temp.split("\n")
            for note in notes:
                filename, msg = note.split("#")
                msg_month, msg_day = msg.split(" ")[0].split("/")
                msg_datetime = datetime.date(2016, int(msg_month), int(msg_day))
                if u" 正在使用這個檔案。" in note:
                    if today > msg_datetime:
                        pass
                    else:
                        new_notes.append(note)
                else:
                    new_notes.append(note)
            notes = "\n".join(new_notes)
            if temp == notes:
                pass
            else:
                print 'reseting locks'
                data = {'description': notes}
                self.server.update(sk, data)

    def setLock(self):
        self.saveNotes(self.server.login + u" 正在使用這個檔案。")

    def unlock(self):
        filename = ""
        print 'unlocking'
        if appName == 'maya':
            filename = cmds.file(query=True, sceneName=True).split("/")[-1]
        elif appName == '3dsmax':
            filename = MaxPlus.FileManager.GetFileName()
            print filename
        elif 'Nuke' in appName:
            import nuke
            if nuke.root().name() == 'Root':
                filename = ""
                pass
            else:
                filename = nuke.root().name().split("/")[-1]
                print filename
        expr = "@GET(sthpw/task['search_code','%s']['process','%s'].description)" % (self.item['code'], self.task['process'])
        temp = self.server.eval(expr)
        notes = temp[0].split("\n")

        if filename == "":
            pass
        else:
            for task in self.tasks:
                if task.get('process') == self.task['process']:
                    sk = task.get('__search_key__')

            new_notes = []
            for note in notes:
                if filename in note:
                    note_ = note.split("#")[1]
                    if u" 正在使用這個檔案。" in note:
                        pass
                    else:
                        new_notes.append(note)
                else:
                    new_notes.append(note)

            notes = "\n".join(new_notes)
            data = {'description': notes}

            self.server.update(sk, data)
            self.getNotes()

    def showdialog(self):
       msg = QtWidgets.QMessageBox()
       msg.setIcon(QtWidgets.QMessageBox.Information)

       msg.setText(u"這個檔案有人在使用!")
       #msg.setInformativeText("This is additional information")
       msg.setWindowTitle(u"警告")
       #msg.setDetailedText("The details are as follows:")
       #msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
       #msg.buttonClicked.connect(self.msgbtn)

       retval = msg.exec_()
       #print "value of pressed message box button:", retval



    # checks in note list if the file has been locked
    def checkLock(self):
        self.ui.note_list.count()
        if self.ui.note_list.count() > 0:
            for i in range(self.ui.note_list.count()):
                if u" 正在使用這個檔案。" in self.ui.note_list.item(i).text():
                    locked = True
                else:
                    locked = False
        else:
            locked = False
        return locked

    def tacticLoad(self):
        self.fileOpen()
        # if self.checkLock() is True:
        #     self.showdialog()
        #     pass
        # elif self.checkLock() is False:
        #     self.unlock()
        #     self.fileOpen()
        #     self.setLock()

    def tacticSave(self):
        # if self.checkLock() is True:
        #     self.unlock()
        
        self.fileSave()
        self.updateStatus()
        # self.setLock()

    def fileSave(self, arg=None):
        path = self.ui.save_path.text()
        filename = self.ui.save_file.text()

        if not os.path.exists(path):
            os.makedirs(path)
        final = path + filename

        if appName == "3dsmax":
            import MaxPlus
            jc.maxWorkspaceFileRule(path)
            MaxPlus.FileManager.Save(final)

        elif appName == "maya":
            jc.mayaWorkspaceFileRule(path)
            # cmds.setAttr("defaultRenderGlobals.imageFilePrefix", filename.replace(".mb", ""), type="string")
            cmds.file(rename=final)
            cmds.file(save=True, type='mayaBinary')
        elif "Nuke" in appName:
            import nuke
            nuke.scriptSaveAs(filename=final)
            nuke.root()['project_directory'].setValue(path.replace("scenes/", ""))
            self.setNukeProject()

        print "saved, task status set to in progress"

        production_type = self.productionType()
        if production_type == 'assets':
            self.prev_selection = self.ui.asset_process_list.currentItem().text()
        elif production_type == 'shot':
            self.prev_selection = self.ui.shot_process_list.currentItem().text()

        self.makeThumbnail(path, filename)
        self.finalPath()
        self.getProcess()
        self.saveLog()

    def fileOpen(self, arg=None):
        path = self.ui.save_path.text()
        filename = self.ui.file_list.currentItem().text().split("  ")[1]
        project_path = path.replace("scenes/", "")

        if appName == "3dsmax":
            import MaxPlus
            if self.ui.file_list.currentItem().background().color().name() == '#725252':
                path = self.old_path

            MaxPlus.FileManager.Open(path + filename)
            jc.maxWorkspaceFileRule(path)

        elif appName == "maya":
            import maya.mel as mel
            if self.ui.file_list.currentItem().background().color().name() == '#725252':
                path = self.old_path

            cmds.file(modified=0)
            cmds.file((path + filename), open=True, ignoreVersion=True)

            setrmsproj = 'rman setvar RMSPROJ \"' + path.replace("scenes/","") + '\"'
            try:
                pass
                mel.eval(setrmsproj)
            except:
                "print rman"
                pass
            jc.mayaWorkspaceFileRule(path)

        elif "Nuke" in appName:
            import nuke
            nuke.Root().setModified(False)
            nuke.scriptOpen(path + filename)
            #nuke.root()['project_directory'].setValue(path.replace("scenes/", ""))
            #self.setNukeProject()


    def makeThumbnail(self, path, filename):
        filename = filename.split(".")[0]
        ext = ".tif"        
        if appName == "maya":
            currentFrame = cmds.currentTime(query=True)
           
            cmds.select(cl=True)
            cmds.playblast(st=currentFrame, et=currentFrame, format="image", filename=filename, forceOverwrite=True, sequenceTime=False, clearCache=True, viewer=False, showOrnaments=False, framePadding=4, percent=100, compression="tif", quality=70, width=400, height=400)

            currentFrame = ".%04d" % int(currentFrame)
            thumbPath = self.ui.save_path.text().replace("scenes/","images/") + filename + currentFrame + ext
            destination = self.ui.save_path.text().replace("scenes/","data/others/thumbnails/")
            try:
                os.makedirs(destination)
            except:
                pass
            # remove duplicate thumbnails
            # imageFiles = os.listdir(destination)
            # for imageFile in imageFiles:
            #     if filename in imageFile:
            #         os.remove(thumbPath + imageFile)

            shutil.copy2(thumbPath, destination)
            os.remove(thumbPath)
            self.getThumbnail()

        elif appName == "3dsmax":
            #filename=(MaxPlus.PathManager.GetRenderOutputDir() + "/" + filename + ext)
            thumbPath = self.ui.save_path.text().replace("scenes/","images/") + filename + ext
            destination = self.ui.save_path.text().replace("scenes/","data/others/thumbnails/")
            try:
                os.makedirs(destination)
            except:
                pass

            storage = MaxPlus.Factory.CreateStorage(6)
            
            bmi = storage.GetBitmapInfo()
        
            bmi.SetName(destination + filename + ext)

            bmp = MaxPlus.Factory.CreateBitmap()

            vm = MaxPlus.ViewportManager
            av = vm.GetActiveViewport()
            av.GetDIB(bmi, bmp)

            bmp.OpenOutput(bmi)
            bmp.Write(bmi)
            bmp.Close(bmi)

            self.getThumbnail()


    def getThumbnail(self):
        try:
            selectedFile = self.ui.file_list.currentItem().text().split("  ")[1].split(".")[0]
            thumbPath = self.ui.save_path.text().replace("scenes/","data/others/thumbnails/")
            imageFiles = os.listdir(thumbPath)
            defaultImage = "//Art-1405260002/d/assets/scripts/maya_scripts/icons/default-placeholder.png"
            image = QtWidgets.QImage(defaultImage)
            self.ui.file_thumbnail.setPixmap(QtWidgets.QPixmap.fromImage(image))
            
            for imageFile in imageFiles:
                if selectedFile in imageFile:
                    image = QtWidgets.QImage(thumbPath + imageFile)
                    self.ui.file_thumbnail.setPixmap(QtWidgets.QPixmap.fromImage(image))
                    break
        except:
            defaultImage = "//Art-1405260002/d/assets/scripts/maya_scripts/icons/default-placeholder.png"
            image = QtWidgets.QImage(defaultImage)
            self.ui.file_thumbnail.setPixmap(QtWidgets.QPixmap.fromImage(image))            
         




    def saveLog(self, arg=None):
        data = {'name': self.game['name_chn'], 'project': self.game['name'], 'item': self.item['name'], 'process': self.task['process'], 'item_code': self.item['code'], 'user': self.server.login, 'path': self.ui.save_path.text(), 'filename': self.ui.save_file.text()}
        self.server.insert('simpleslot/save_log', data)

    def setNukeProject(self, arg=None):
        import nuke
        sourceimages_path = nuke.root()['project_directory'].value() + "sourceimages/"
        images_path = nuke.root()['project_directory'].value() + "images/"

        if os.path.exists(images_path) is False:
            os.makedirs(images_path)
        if os.path.exists(sourceimages_path) is False:
            os.makedirs(sourceimages_path)

        nuke.addFavoriteDir('images', images_path)
        nuke.addFavoriteDir('sourceimages', sourceimages_path)

    def openPath(self):
        final_path = self.ui.save_path.text()
        subprocess.check_call(['explorer', final_path.replace("/", "\\")])

    def logOut(self):
        self.close()
        name = self.server.login
        ticket_file = "c:/sthpw/etc/" + name + ".tacticrc"
        os.remove(ticket_file)
        loginProcess()

    def setInProgressFilter(self):
        self.ui.inprogress_button.setChecked(1)
        self.ui.ready_button.setChecked(0)
        self.ui.complete_button.setChecked(0)
        self.ui.recent_button.setChecked(0)
        self.getProjects()

    def setReadyFilter(self):
        self.ui.inprogress_button.setChecked(0)
        self.ui.ready_button.setChecked(1)
        self.ui.complete_button.setChecked(0)
        self.ui.recent_button.setChecked(0)
        self.getProjects()

    def setCompleteFilter(self):
        self.ui.inprogress_button.setChecked(0)
        self.ui.ready_button.setChecked(0)
        self.ui.complete_button.setChecked(1)
        self.ui.recent_button.setChecked(0)
        self.getProjects()

    def setRecentFilter(self):
        self.ui.inprogress_button.setChecked(0)
        self.ui.ready_button.setChecked(0)
        self.ui.complete_button.setChecked(0)
        self.ui.recent_button.setChecked(1)
        self.getProjects()


def qt_tactic_mainMain():
    global widget
    serverok = 0

    try:
        tactic_server_ip = socket.gethostbyname("vg.com")
    except:
        tactic_server_ip = "192.168.163.60"

    try:
        # short test to see if there's a server
        expr = "@GET(sthpw/login.login)"
        temp = server.eval(expr)
        serverok = 1
    except:
        try:
            # try from tacticrc file
            server = TacticServerStub(setup=False)
            ticket_path = "c:/sthpw/etc"
            ticket_files = os.listdir("c:/sthpw/etc/")
            lines = []
            if len(ticket_files) > 0:
                with open(ticket_path + "/" + ticket_files[0], 'r') as f:
                    for line in f:
                        lines.append(line.split("=")[1].replace("\n", ""))

            server.login = lines[0]
            server.set_server(tactic_server_ip)
            server.set_project("simpleslot")
            server.set_ticket(lines[2])
            serverok = 1
        except:
            loginProcess()

    #mainProcess(server=server)
    if serverok == 1:
        try:
            widget.show()
        except:
            print 'not ok'
            mainProcess(server=server)


def loginProcess():
    if appName == "3dsmax":
        import MaxPlus
        MaxPlus.CUI.DisableAccelerators()

    loginWidget = loginWindow(parent=QtWidgets.QApplication.activeWindow())

    if appName == "3dsmax":
        _GCProtector.widgets.append(loginWidget)
        loginWidget.setWindowFlags(loginWidget.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        capsule = loginWidget.effectiveWinId()
        ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
        ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
        ptr = ctypes.pythonapi.PyCObject_AsVoidPtr(capsule)
        #MaxPlus.Win32.Set3dsMaxAsParentWindow(ptr)

    loginWidget.show()


def mainProcess(server=None):
    global widget
    widget = mainWindow(parent=QtWidgets.QApplication.activeWindow())

    try:
        login_name = server.login
        widget.ui.login_name.setText(login_name)
    except:
        pass

    if appName == "3dsmax":
        _GCProtector.widgets.append(widget)
        widget.setWindowFlags(widget.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        capsule = widget.effectiveWinId()
        ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
        ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
        ptr = ctypes.pythonapi.PyCObject_AsVoidPtr(capsule)

    widget.show()
    widget.server = server
    widget.getProjects()
    app.aboutToQuit.connect(widget.unlock)

if __name__ == "__main__":
    qt_tactic_mainMain()

