'''
import subprocess
import fileinput

input = "//Art-1405260002/d/assets/scripts/maya_scripts/ui/qt_main_ui.ui"
output = "//Art-1405260002/d/assets/scripts/maya_scripts/lib/qt_main_ui.py"
subprocess.call("C:/Python27/scripts/pyside-uic -o %s %s" % (output, input))

with open(output, 'r') as data:
    filedata = data.read()

header = "# -*- coding: utf-8 -*-\n" 
header = header + "import sys\nsys.path.append(\"//Art-1405260002/d/assets/scripts/maya_scripts/lib\")\n"

filedata = filedata.replace('../', '//Art-1405260002/d/assets/scripts/maya_scripts/')
filedata = filedata.replace("self.asset_process_list = processListWidget(self.assets_tab)", "self.asset_process_list = processListWidget(self.assets_tab, mainWindowObj=main_window)")
filedata = filedata.replace("self.shot_process_list = processListWidget(self.shots_tab)", "self.shot_process_list = processListWidget(self.shots_tab, mainWindowObj=main_window)")
filedata = filedata.replace("from processlistwidget import processListWidget", "import processlistwidget\nfrom processlistwidget import processListWidget\nreload(processlistwidget)")

filedata = header + filedata
with open(output, 'w') as data:
    data.write(filedata)

'''    
scripts_path = "//Art-1405260002/d/assets"
import sys
tactic_client_path = scripts_path + "/client"
sys.path.append(scripts_path + "/client")
sys.path.append(scripts_path + "/scripts/maya_scripts/lib")
sys.path.append(scripts_path + "/scripts/maya_scripts/ui")
sys.path.append(scripts_path + "/scripts/maya_scripts")
sys.path.append(scripts_path + "/scripts/install")
sys.path.append(scripts_path + "/scripts/python-dateutil-2.3")
sys.path.append(scripts_path + "/scripts/six-1.8.0")
import datetime
import time
global server, widget

from PySide import QtCore, QtGui
from tactic_client_lib import TacticServerStub

import ctypes
import qt_main_ui as qt_main_ui
import qt_login_ui
import os, shutil
import subprocess
import socket
import jc_maya_aux_functions as jc
from dateutil import parser

try:
    tactic_server_ip = socket.gethostbyname("vg.com")
except:
    tactic_server_ip = "192.168.163.60"

reload(qt_main_ui)
reload(qt_login_ui)
reload(jc)

asset_item_details = ""
shot_item_details = ""
notready_icon = QtGui.QIcon('//art-1405260002/D/assets/scripts/maya_scripts/icons/proc_list/notready.png')
ready_icon = QtGui.QIcon('//art-1405260002/D/assets/scripts/maya_scripts/icons/proc_list/ready.png')
inprogress_icon = QtGui.QIcon('//art-1405260002/D/assets/scripts/maya_scripts/icons/proc_list/inprogress.png')
standby_icon = QtGui.QIcon('//art-1405260002/D/assets/scripts/maya_scripts/icons/proc_list/standby.png')
review_icon = QtGui.QIcon('//art-1405260002/D/assets/scripts/maya_scripts/icons/proc_list/review.png')
complete_icon = QtGui.QIcon('//art-1405260002/D/assets/scripts/maya_scripts/icons/proc_list/complete.png')

app = QtGui.QApplication.instance()
if not app:
    app = QtGui.QApplication([])

appName = app.objectName()

class _GCProtector(object):
    widgets = []

class loginWindow(QtGui.QDialog):
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
#%%

class mainWindow(QtGui.QDialog):
    asset_item_details = None
    shot_item_details = None
    server = None
    item_tasks = None

    game = None
    projects_data = None
    #projects_data = {'name': names, 'login': bsd, 'keywords': bed, 'game_name_chn': names_chn, 'description': game_type, 'process': assigned}
    project_info = []

    item_name = None
    item_name_chn = None
    item_type = None
    item_process = None
    item_code = None
    assigned = None
    bsd = None
    bed = None
    sk = None
    processes = None

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
        self.ui.logout_button.clicked.connect(self.logOut)

        self.ui.inprogress_button.clicked.connect(self.setInProgressFilter)
        self.ui.ready_button.clicked.connect(self.setReadyFilter)
        self.ui.complete_button.clicked.connect(self.setCompleteFilter)

        self.ui.file_list.itemClicked.connect(self.getNotes)
        #self.ui.save_note.clicked.connect(self.saveNotes)
        self.ui.note_list.itemDoubleClicked.connect(self.delNotes)
        self.ui.note.returnPressed.connect(self.saveNotes)
        self.ui.note.setStyleSheet("""
            background-color: rgb(170,170,170);
            color: black;
        """)
        self.ui.update_cache.clicked.connect(self.updateCache)

        if "Nuke" in appName:
            pass
        else:
            sshFile = scripts_path + "/scripts/maya_scripts/lib/darkorange.stylesheet"
            with open(sshFile, "r") as fh:
                self.setStyleSheet(fh.read())

    def getNotes(self):
        self.ui.note_list.clear()
        expr = "@GET(sthpw/task['search_code','%s']['process','%s'].description)" % (self.item_code, self.item_process)
        temp = self.server.eval(expr)[0]

        if temp != "":
            notes = temp.split("\n")
            for note in notes:
                filename = note.split("#")[0]
                note = note.split("#")[1]
                if filename == self.ui.file_list.currentItem().text().split("  ")[1]:
                    self.ui.note_list.addItem(note)
                    self.ui.note_list.scrollToItem(self.ui.note_list.item(self.ui.note_list.count() - 1))

    def saveNotes(self):
        note = self.ui.note.text().replace("\n","")
        now = datetime.datetime.now()
        name = self.server.login

        if note != "":
            expr = "@GET(sthpw/task['search_code','%s']['process','%s'].description)" % (self.item_code, self.item_process)
            temp = self.server.eval(expr)
            if temp != []:
                notes = temp[0].split("\n")
            if notes[0] == "":
                notes.pop(0)
            for task in self.item_tasks:
                if task.get('process') == self.item_process:
                    sk = task.get('__search_key__')

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
        expr = "@GET(sthpw/task['search_code','%s']['process','%s'].description)" % (self.item_code, self.item_process)
        temp = self.server.eval(expr)
        notes = temp[0].split("\n")
        new_notes = []
        for task in self.item_tasks:
            if task.get('process') == self.item_process:
                sk = task.get('__search_key__')
        for note in notes:
            filename = note.split("#")[0]
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

    def getProjects(self):
        #openRecent()
        inprogress = self.ui.inprogress_button.isChecked()
        ready = self.ui.ready_button.isChecked()
        complete = self.ui.complete_button.isChecked()

        self.ui.project_list.clear()

        if inprogress == True:
            inprogress_filter = "['id','8']"
        else:
            inprogress_filter = ""
        if ready == True:
            ready_filter = "['id','10']"
        else:
            ready_filter = ""
        if complete == True:
            complete_filter = "['id','11']"
        else:
            complete_filter = ""

        expr = "@SOBJECT(simpleslot/plan['begin']" + inprogress_filter + ready_filter + complete_filter + "['or'])"
        temp = self.server.eval(expr)

        if inprogress == ready == complete == False:
            temp = ""

        names = bsd = bed = names_chn = game_type = assigned = ""

        for x in temp:
            names = names + x.get('name')
            bsd = bsd + x.get('login')
            bed = bed + x.get('keywords')
            names_chn = names_chn + x.get('game_name_chn')
            game_type = game_type + x.get('description')
            assigned = assigned + x.get('process')

        self.projects_data = {'name': names, 'login': bsd, 'keywords': bed, 'game_name_chn': names_chn, 'description': game_type, 'process': assigned}

        names = self.projects_data.get('name')
        names = names.split("__")  # list is a space separated string
        names.pop(0)
        names = sorted(names)

        for name in names:
            self.ui.project_list.addItem(name)


    def getItems(self):
        self.ui.asset_list.clear()
        self.ui.shot_list.clear()

        self.game = self.ui.project_list.currentItem().text()

        names = self.projects_data.get('name')
        names = names.split("__")

        bsd = self.projects_data.get('login')
        bsd = bsd.split("__")

        bed = self.projects_data.get('keywords')
        bed = bed.split("__")

        names_chn = self.projects_data.get('game_name_chn')
        names_chn = names_chn.split("__")

        games_type = self.projects_data.get('description')
        games_type = games_type.split("__")

        assigned = self.projects_data.get('process')
        assigned = assigned.split("__")

        temp = zip(names_chn, games_type, assigned, bsd, bed, names)
        temp.pop(0)

        def getNameKey(item):
            return item[0]

        temp = sorted(temp, key=getNameKey, reverse=False)
        self.project_info = []
        for x in range(len(temp)):
            #if temp[x][5] in game:  # if selected is in inprogress list
            # make sure game is an exact match to temp[x][5], otherwise projects with _app or _cf suffix will aggregate
            if self.game == temp[x][5]:
                if temp[x][1] == "casino":  # if selected is casino or shot or assets
                    self.updateList(name=temp[x][5], stype="3d", production_type="assets")

                elif temp[x][1] == "sports" or temp[x][1] == "cf" or temp[x][1] == "video_conf" or temp[x][1] == "database":
                    self.updateList(name=temp[x][5], stype="assets", production_type="assets")
                    self.updateList(name=temp[x][5], stype="shot", production_type="shot")

                for z in range(len(temp[x])):
                    self.project_info.append(temp[x][z])
                    widgetItem = QtGui.QTableWidgetItem(temp[x][z])
                    widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                    self.ui.project_info.setItem(z,0,widgetItem)

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

        self.getProcess()

    def updateList(self, name=None, stype=None, production_type=None):
        expr = "@SOBJECT(simpleslot/game['name','" + name + "'].simpleslot/" + stype + ")"
        temp = self.server.eval(expr)

        items = sorted(temp, key=lambda k: k['name'])

        if stype == "3d" or stype == "assets":
            self.asset_item_details = items
            names = [y['name'] for y in self.asset_item_details]

        else:
            self.shot_item_details = items
            names = [y['name'] for y in self.shot_item_details]

        for name in names:
            if production_type == "assets":
                self.ui.asset_list.addItem(name)
            else:
                self.ui.shot_list.addItem(name)

    def productionType(self):
        if self.ui.tabProductionType.currentIndex() == 0:
            production_type = "assets"
        elif self.ui.tabProductionType.currentIndex() == 1:
            production_type = "shot"
        return production_type

    def getProcess(self):
        production_type = self.productionType()

        selected = ""

        if production_type == "assets":
            selected = self.ui.asset_list.currentRow()
            self.item_name = self.ui.asset_list.currentItem().text()
            self.item_name_chn = self.asset_item_details[selected].get('description')
            self.item_code = self.asset_item_details[selected].get('code')
            if self.project_info[1] == "casino":
                stype = "3d"
                self.item_type = self.asset_item_details[selected].get('3d_type_code')
            else:
                stype = "assets"
                self.item_type = self.asset_item_details[selected].get('asset_type_code')

            # item_type is retrieved here instead of in final path
            self.item_type = self.assetTypeCode(self.item_type)

        elif production_type == "shot":
            if self.ui.shot_list.count() != 0:            
                selected = self.ui.shot_list.currentRow()
                self.item_name = self.ui.shot_list.currentItem().text()
                self.item_name_chn = self.shot_item_details[selected].get('description')
                self.item_type = "None"
                self.item_code = self.shot_item_details[selected].get('code')
            stype = "shot"

        expr = "@SOBJECT(simpleslot/" + stype + "['code','" + self.item_code + "'].sthpw/task)"
        tasks = self.server.eval(expr)

        self.item_tasks = self.orderTasksByProcesses(tasks)

        self.updateProcessList()
        selectedProcess = 0
        for i, task in enumerate(self.item_tasks):
            if task.get('status') == ".In Progress":
                selectedProcess = i

        if production_type == "assets":
            if self.ui.asset_list.count() != 0:
                self.ui.asset_process_list.setCurrentRow(selectedProcess)     # select first in process list if it contains anything

                widgetItem = QtGui.QTableWidgetItem(self.item_name_chn)
                widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.ui.asset_info.setItem(0,0,widgetItem)

                widgetItem = QtGui.QTableWidgetItem(self.item_type)
                widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.ui.asset_info.setItem(1,0,widgetItem)

        elif production_type == "shot":
            if self.ui.shot_list.count() != 0:
                self.ui.shot_process_list.setCurrentRow(selectedProcess)

                widgetItem = QtGui.QTableWidgetItem(self.item_name_chn)
                widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.ui.shot_info.setItem(0,0,widgetItem)

                widgetItem = QtGui.QTableWidgetItem(self.item_type)
                widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.ui.shot_info.setItem(1,0,widgetItem)
        self.finalPath()

    '''
    def orderProcesses(self, processes):
        length = len(processes) - 1
        new = []
        for x in range(0, len(processes)):
            new.append("")

        if "final" in processes:
            new[length] = "final"
            length = length - 1
        if "layout" in processes:
            new[length] = "layout"
            length = length - 1
        if "effects" in processes:
            new[length] = "effects"
            length = length - 1
        if "lighting" in processes:
            new[length] = "lighting"
            length = length - 1
        if "animation" in processes:
            new[length] = "animation"
            length = length - 1
        if "rigging" in processes:
            new[length] = "rigging"
            length = length - 1
        if "texture" in processes:
            new[length] = "texture"
            length = length - 1
        if "model" in processes:
            new[length] = "model"
            length = length - 1
        if "concept" in processes:
            new[length] = "concept"
            length = length - 1
        if "rough" in processes:
            new[length] = "rough"
            length = length - 1
        return new
    '''

    def orderTasksByProcesses(self, tasks):
        new = []
        production_type = self.productionType()
        if production_type == "shot":
            ordered = ['layout','animation','lighting','effects','final']
        else:
            ordered = ['rough', 'concept', 'model','texture','rigging','animation','lighting','effects','layout','final']
        for order in ordered:
            for task in tasks:
                if task.get('process') == order:
                    new.append(task)
        return new

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

    def updateProcessInfo(self):
        production_type = self.productionType()
        selected_process = ""
        if production_type == "assets":
            if self.ui.asset_process_list.count() != 0:
                selected_process = self.ui.asset_process_list.currentItem().text()
        elif production_type == "shot":
            if self.ui.shot_process_list.count() != 0:
                selected_process = self.ui.shot_process_list.currentItem().text()

        self.assigned = ""
        self.bsd = ""
        self.bed = ""
        for x in self.item_tasks:
            if x.get("process") == selected_process:
                # task_search_key = x.get("__search_key__")
                self.assigned = self.assigned + ", " + x.get("assigned")
                self.bsd = self.bsd + ", " + x.get("bid_start_date")[5:-9]
                self.bed = self.bed + ", " + x.get("bid_end_date")[5:-9]
                self.sk = x.get('__search_key__')

        self.assigned = self.assigned[2:]
        self.bsd = self.bsd[2:]
        self.bed = self.bed[2:]

        process_infos = [self.assigned, self.bsd, self.bed]

        for x in range(0, len(process_infos)):
            index = 2 + x
            widgetItem = QtGui.QTableWidgetItem(process_infos[x])
            widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
            if production_type is "assets":
                self.ui.asset_info.setItem(index, 0, widgetItem)
            if production_type is "shot":
                self.ui.shot_info.setItem(index, 0, widgetItem)

    def finalPath(self):
        base_path = "//art-render/art_3d_project/"
        name = self.server.login

        project = self.project_info[5]
        project_type = self.project_info[1]

        production_type = self.productionType()

        self.updateProcessInfo()

        if production_type == "assets":
            try:
                self.item_process = self.ui.asset_process_list.currentItem().text()
            except:
                pass
        elif production_type == "shot":
            try:
                self.item_process = self.ui.shot_process_list.currentItem().text()
            except:
                pass

        #print project, production_type, item_name, item_process
        final_path = ""
        base_filename = ""
        item_type = ""
        filename = ""

        if appName == "3dsmax":
            ext = ".max"
        elif appName == "maya":
            ext = ".mb"
        elif "Nuke" in appName:
            ext = ".nk"
        elif appName == "python":
            ext = ""

        if production_type == "assets":
            if project_type == "cf" or project_type == "sports" or project_type == "video_conf" or project_type == "database":
                final_path = base_path + project + "/assets/" + self.item_type + "/" + self.item_name + "/" + self.item_process + "/scenes/"
                base_filename = jc.abbrName(project) + "_" + jc.abbrItemType(self.item_type) + "_" + self.item_name + "_" + jc.abbrName(self.item_process)

                filename = jc.abbrName(project) + "_" + jc.abbrItemType(self.item_type) + "_" + self.item_name + "_" + jc.abbrName(self.item_process) + "_" + jc.maxVersion(final_path, base_filename, "maya") + "_" + name + ext
                project_type = "assets"

            elif project_type == "casino":
                final_path = base_path + project + "/casino/" + self.item_type + "/" + self.item_name + "/" + self.item_process + "/scenes/"
                base_filename = jc.abbrName(project) + "_" + jc.abbrItemType(self.item_type) + "_" + self.item_name + "_" + jc.abbrName(self.item_process)

                filename = jc.abbrName(project) + "_"  + jc.abbrItemType(self.item_type) + "_" + self.item_name + "_" + jc.abbrName(self.item_process) + "_" + jc.maxVersion(final_path, base_filename, "maya") + "_" + name + ext
                project_type = "assets"

        elif production_type == "shot":
            final_path = base_path + project + "/shot/" + self.item_name + "/" + self.item_process + "/scenes/"
            base_filename = jc.abbrName(project) + "_" + self.item_name + "_" + jc.abbrName(self.item_process)

            filename = jc.abbrName(project) + "_" + self.item_name + "_" + jc.abbrName(self.item_process) + "_" + jc.maxVersion(final_path, base_filename, "maya") + "_" + name + ext
            project_type = "shot"

        final_path = final_path.replace(" ", "")

        if production_type == "assets":
            if self.ui.asset_list.count() != 0 and self.ui.asset_process_list.count() != 0:
                self.ui.save_path.setText(final_path)
                self.ui.save_file.setText(filename)
        elif production_type == "shot":
            if self.ui.shot_list.count() != 0 and self.ui.shot_process_list.count() != 0:
                self.ui.save_path.setText(final_path)
                self.ui.save_file.setText(filename)

        try:
            self.updateFileList(final_path, base_filename)
        except:
            print "updateFilelist failed"
        #recent_file = ""

    def updateFileList(self, final_path, base_filename): # use getfilelist() and update ui
        fileList = []
        self.ui.file_list.clear()

        if os.path.exists(final_path) is True:
            savedFiles = os.listdir(final_path)
            if len(savedFiles) == 0:
                pass
            else:
                fileList = [x for x in savedFiles if base_filename in x]
        else:
            pass

        for filename in fileList:
            filedate = time.strftime("%m/%d %H:%M", time.localtime(os.path.getmtime(final_path + filename)))
            self.ui.file_list.addItem(filedate + "  " + filename)

        file_list_count = self.ui.file_list.count()

        if file_list_count != 0:
            self.ui.file_list.setCurrentRow(file_list_count - 1)

        self.getNotes()

    def updateProcessList(self):
        production_type = self.productionType()

        if self.ui.asset_process_list.count() != 0:
            self.ui.asset_process_list.clear()
        if self.ui.shot_process_list.count() != 0:
            self.ui.shot_process_list.clear()

        for task in self.item_tasks:
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
               
            if production_type == "assets" and self.ui.asset_list.count() != 0:
                item = QtGui.QListWidgetItem(icon, process)
                self.ui.asset_process_list.addItem(item)
            elif production_type == "shot" and self.ui.shot_list.count() != 0:
                item = QtGui.QListWidgetItem(icon, process)
                self.ui.shot_process_list.addItem(item)

    def updateStatus(self):
        tasks = self.item_tasks
        new = self.orderTasksByProcesses(tasks)

        datas = {}
        inprogress = {'status':'.In Progress'}
        complete = {'status':'.Complete'}

        for i, task in enumerate(new):
            process = self.item_process
            # print i, task.get('process'), process
            if task.get('process') == process:
                if task.get('status') == '.Not Ready' or task.get('status') == '.Ready':
                    task_sk = task.get('__search_key__')
                    datas.update({task_sk:inprogress})
                while i != 0:
                    i-=1
                    if new[i].get('status') != '.Complete':
                        past_sk = new[i].get('__search_key__')
                        datas.update({past_sk:complete})
        self.server.update_multiple(datas, triggers=False)

    def tacticSave(self, arg=None):
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
            import maya.cmds as cmds
            jc.mayaWorkspaceFileRule(path)
            cmds.setAttr("defaultRenderGlobals.imageFilePrefix", filename.replace(".mb", ""), type="string")
            cmds.file(rename=final)
            cmds.file(save=True, type='mayaBinary')
        elif "Nuke" in appName:
            import nuke
            nuke.scriptSaveAs(filename=final)

        print "saved, task status set to in progress"

        self.finalPath()
        self.updateStatus()
        self.getProcess()

    def tacticLoad(self, arg=None):
        path = self.ui.save_path.text()
        filename = self.ui.file_list.currentItem().text().split("  ")[1]
        project_path = path.replace("scenes/", "")

        if appName == "3dsmax":
            import MaxPlus
            MaxPlus.FileManager.Open(path + filename)
            jc.maxWorkspaceFileRule(path)

        elif appName == "maya":
            import maya.cmds as cmds
            print path + filename
            cmds.file(modified=0)
            cmds.file((path + filename), open=True, ignoreVersion=True)
            jc.mayaWorkspaceFileRule(path)

        elif "Nuke" in appName:
            import nuke
            nuke.scriptOpen(path + filename)

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
        self.getProjects()

    def setReadyFilter(self):
        self.ui.inprogress_button.setChecked(0)
        self.ui.ready_button.setChecked(1)
        self.ui.complete_button.setChecked(0)
        self.getProjects()

    def setCompleteFilter(self):
        self.ui.inprogress_button.setChecked(0)
        self.ui.ready_button.setChecked(0)
        self.ui.complete_button.setChecked(1)
        self.getProjects()

    def gamelist(self, items):
        now = datetime.datetime.now()
        names = ""
        names_chn = ""
        games_type = ""
        assignments = ""
        bsd_string = ""
        bed_string = ""

        for game in items:
            name = game.get("name")
            name_chn = game.get("name_chn")
            search_code = game.get("code")
            expr = "@SOBJECT(sthpw/task['search_code','" + search_code + "'])"
            depts = self.server.eval(expr)

            expr = "@GET(simpleslot/game['name','" + name + "'].simpleslot/game_type.name)"
            game_type = self.server.eval(expr)
            for dept in depts:
                dept_name = dept.get("process")
                if dept_name == "3d":
                    bsd = dept.get("bid_start_date")
                    bsd = parser.parse(bsd)
                    bsd = bsd.strftime("%m/%d/%y")
                    bed = dept.get("bid_end_date")
                    bed = parser.parse(bed)
                    bed = bed.strftime("%m/%d/%y")
                    bsd_string = bsd_string + "__" + (bsd)
                    bed_string = bed_string + "__ " + (bed)
                    assignment = dept.get("assigned")
                    assignments = assignments + "__" + assignment
                    names = names + "__" + name
                    games_type = games_type + "__" + game_type[0]
                    names_chn = names_chn + "__" + name_chn
        data = {'name': names, 'description': games_type, 'login': bsd_string, 'keywords': bed_string, 'timestamp': str(now), 'game_name_chn': names_chn, 'process': assignments}
        return data

    def updateCache(self):
        expr = "@SOBJECT(simpleslot/game['project_status','.In Progress'])"
        inprogress = self.server.eval(expr)

        expr = "@SOBJECT(simpleslot/game['project_status','.Ready'])"
        ready = self.server.eval(expr)

        expr = "@SOBJECT(simpleslot/game['project_status','.Complete'])"
        complete = self.server.eval(expr)

        data = self.gamelist(inprogress)
        test1 = self.server.update("simpleslot/plan?project=simpleslot&id=8", data)

        data = self.gamelist(ready)
        test2 = self.server.update("simpleslot/plan?project=simpleslot&id=10",data)

        data = self.gamelist(complete)
        test3 = self.server.update("simpleslot/plan?project=simpleslot&id=11", data)
        print "update complete"

#%%
def qt_tactic_mainMain():
    serverok = 0
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
                        lines.append(line.split("=")[1].replace("\n",""))

            server.login = lines[0]
            server.set_server(tactic_server_ip)
            server.set_project("simpleslot")
            server.set_ticket(lines[2])
            serverok = 1
        except:
            loginProcess()

    #mainProcess(server=server)
    #'''
    if serverok == 1:
        try:
            widget.show()
        except:
            mainProcess(server=server)
    #'''

#%%
def loginProcess():
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

#%%
def mainProcess(server=None):
    global widget
    widget = mainWindow(parent=QtGui.QApplication.activeWindow())
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

#%%
if __name__ == "__main__":
    qt_tactic_mainMain() # for addCustomShelf, the rule is filename + Main()