# pyside-uic -o //Art-1405260002/d/assets/scripts/maya_scripts/lib/qt_main_ui.py //Art-1405260002/d/assets/scripts/maya_scripts/ui/qt_main_ui.ui
#C:\Python27\Lib\site-packages\PySide>
#pyside-rcc.exe -py2 //Art-1405260002/d/assets/scripts/maya_scripts/icons/icons.qrc > //Art-1405260002/d/assets/scripts/maya_scripts/ui/icons_rc.py

import sys
sys.path.append("//Art-1405260002/d/assets/client")
sys.path.append("//Art-1405260002/d/assets/scripts/maya_scripts/lib")
sys.path.append("//Art-1405260002/d/assets/scripts/maya_scripts/ui")
sys.path.append("//Art-1405260002/d/assets/scripts/maya_scripts")
sys.path.append("//Art-1405260002/d/assets/scripts/install")
sys.path.append("//Art-1405260002/d/assets/scripts/python-dateutil-2.3")
sys.path.append("//Art-1405260002/d/assets/scripts/six-1.8.0")
import datetime
import time
#global widget, recent_file, loginWidget
global server

from PySide import QtCore, QtGui
from tactic_client_lib import TacticServerStub
#server = TacticServerStub()

import ctypes
import qt_main_ui as qt_main_ui
import qt_login_ui
import os, shutil
import subprocess
import socket
import jc_maya_aux_functions as jc
from dateutil import parser

tactic_server_ip = socket.gethostbyname("vg.com")

reload(qt_main_ui)
reload(qt_login_ui)
reload(jc)


asset_item_details = ""
shot_item_details = ""

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
            sshFile = "//Art-1405260002/d/assets/scripts/maya_scripts/lib/darkorange.stylesheet"
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
    assigned = None
    bsd = None
    bed = None  
    
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Tool)
        self.ui = qt_main_ui.Ui_main_window()
        self.ui.setupUi(self)

        self.ui.project_list.itemClicked.connect(self.getItems)

        self.ui.tabProductionType.currentChanged.connect(self.getItems)
        self.ui.asset_list.itemClicked.connect(self.getProcess)
        self.ui.shot_list.itemClicked.connect(self.getProcess)

        self.ui.asset_process_list.itemClicked.connect(self.finalPath)
        self.ui.shot_process_list.itemClicked.connect(self.finalPath)

        self.ui.save_button.clicked.connect(self.tacticSave)
        self.ui.open_button.clicked.connect(self.tacticLoad)
        self.ui.open_path_button.clicked.connect(self.openPath)
        self.ui.logout_button.clicked.connect(self.logOut)

        self.ui.inprogress_button.clicked.connect(self.setInProgressFilter)
        self.ui.ready_button.clicked.connect(self.setReadyFilter)
        self.ui.complete_button.clicked.connect(self.setCompleteFilter)

        #self.ui.publish_button.clicked.connect(publishMaster)
        self.ui.update_cache.clicked.connect(self.updateCache)

        #self.ui.inprogress_button.clicked.connect(getProjects)
        #self.ui.ready_button.clicked.connect(getProjects)
        #self.ui.complete_button.clicked.connect(getProjects)

        if "Nuke" in appName:
            pass
        else:
            sshFile = "//Art-1405260002/d/assets/scripts/maya_scripts/lib/darkorange.stylesheet"
            with open(sshFile, "r") as fh:
                self.setStyleSheet(fh.read())

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

        #time.sleep(0.05)
    
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
        recent_file = ''

        if recent_file == "":
            production_type = self.productionType()
            if production_type == "assets":
                if self.ui.asset_list.count() != 0:
                    self.ui.asset_list.setCurrentRow(0)
                    self.ui.tabProductionType.setCurrentIndex(0)
    
                    self.getProcess()
    
            elif production_type == "shot":
                if self.ui.shot_list.count() != 0:
                    self.ui.shot_list.setCurrentRow(0)
                    self.ui.tabProductionType.setCurrentIndex(1)
    
                    self.getProcess()
        else:
            if recent_file[3][5] == "assets":
                if self.ui.asset_list.count() != 0:
                    self.ui.tabProductionType.setCurrentIndex(0)
                    self.ui.asset_list.setCurrentItem(self.ui.asset_list.findItems(recent_file[3][1], QtCore.Qt.MatchExactly)[0])
                    self.ui.asset_list.scrollToItem(self.ui.asset_list.findItems(recent_file[3][1], QtCore.Qt.MatchExactly)[0], QtGui.QAbstractItemView.EnsureVisible)
                    self.getProcess()
    
            elif recent_file[3][5] == "shot":
                if self.ui.shot_list.count() != 0:
                    self.ui.tabProductionType.setCurrentIndex(1)
                    self.ui.shot_list.setCurrentItem(self.ui.shot_list.findItems(recent_file[3][1], QtCore.Qt.MatchExactly)[0])
                    self.ui.shot_list.scrollToItem(self.ui.shot_list.findItems(recent_file[3][1], QtCore.Qt.MatchExactly)[0], QtGui.QAbstractItemView.EnsureVisible)
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
        if self.ui.asset_process_list.count() != 0:
            self.ui.asset_process_list.clear()
        if self.ui.shot_process_list.count() != 0:        
            self.ui.shot_process_list.clear()
        
        production_type = self.productionType()

        selected = ""
        if production_type == "assets":
            selected = self.ui.asset_list.currentRow()
            self.item_name = self.ui.asset_list.currentItem().text()
            self.item_name_chn = self.asset_item_details[selected].get('description')
            item_code = self.asset_item_details[selected].get('code')
            if self.ui.project_info.item(1,0).text() == "casino":
                stype = "3d"
                self.item_type = self.asset_item_details[selected].get('3d_type_code')
                #item_type = assetTypeCode(item_type)
            else:
                stype = "assets"
                self.item_type = self.asset_item_details[selected].get('asset_type_code')
                #item_type = assetTypeCode(item_type)
    
        elif production_type == "shot":
            selected = self.ui.shot_list.currentRow()
            self.item_name = self.ui.shot_list.currentItem().text()
            self.item_name_chn = self.shot_item_details[selected].get('description')
            self.item_type = "None"
            item_code = self.shot_item_details[selected].get('code')
            stype = "shot"
    
        expr = "@SOBJECT(simpleslot/" + stype + "['code','" + item_code + "'].sthpw/task)"
        self.item_tasks = self.server.eval(expr)
    
        bad = []
        bad.append("assets")
        processes = [y['process'] for y in self.item_tasks]
    
        processes = [y for y in processes if y not in bad]
        processes = set(processes)
        processes = list(processes)
        processes = self.orderProcesses(processes)
        recent_file = ""
    
        for process in processes:
            if production_type == "assets" and self.ui.asset_list.count() != 0:
                self.ui.asset_process_list.addItem(process)
            elif production_type == "shot" and self.ui.shot_list.count() != 0:
                self.ui.shot_process_list.addItem(process)


        if production_type == "assets":
            if self.ui.asset_list.count() != 0:
                if recent_file == "":
                    self.ui.asset_process_list.setCurrentRow(0)     # select first in process list if it contains anything
                else:
                    self.ui.asset_process_list.setCurrentItem(self.ui.asset_process_list.findItems(recent_file[3][2], QtCore.Qt.MatchExactly)[0])
    
                widgetItem = QtGui.QTableWidgetItem(self.item_name_chn)
                widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.ui.asset_info.setItem(0,0,widgetItem)
    
                widgetItem = QtGui.QTableWidgetItem(self.item_type)
                widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.ui.asset_info.setItem(1,0,widgetItem)
                self.finalPath()

        elif production_type == "shot":
            if self.ui.shot_list.count() != 0:
                if recent_file == "":
                    self.ui.shot_process_list.setCurrentRow(0)
                else:
                    self.ui.shot_process_list.setCurrentItem(self.ui.shot_process_list.findItems(recent_file[3][2], QtCore.Qt.MatchExactly)[0])
    
                widgetItem = QtGui.QTableWidgetItem(self.item_name_chn)
                widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.ui.shot_info.setItem(0,0,widgetItem)
    
                widgetItem = QtGui.QTableWidgetItem(self.item_type)
                widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.ui.shot_info.setItem(1,0,widgetItem)
                self.finalPath()

        recent_file = ""  # set to none, this is so locating recent file will only run once, when the widget is initialized.        

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
            self.item_process = self.ui.asset_process_list.currentItem().text()
        elif production_type == "shot":
            self.item_process = self.ui.shot_process_list.currentItem().text()            

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
                expr = "@SOBJECT(simpleslot/game['name','" + project + "'].simpleslot/assets['name','" + self.item_name + "'].simpleslot/asset_type)"
                asset_type = self.server.eval(expr)
                item_type = asset_type[0].get('name')
                final_path = base_path + project + "/assets/" + item_type + "/" + self.item_name + "/" + self.item_process + "/scenes/"
                base_filename = jc.abbrName(project) + "_" + jc.abbrItemType(item_type) + "_" + self.item_name + "_" + jc.abbrName(self.item_process)

                filename = jc.abbrName(project) + "_" + jc.abbrItemType(item_type) + "_" + self.item_name + "_" + jc.abbrName(self.item_process) + "_" + jc.maxVersion(final_path, base_filename, "maya") + "_" + name + ext
                project_type = "assets"

            elif project_type == "casino":
                expr = "@SOBJECT(simpleslot/game['name','" + project + "'].simpleslot/3d['name','" + self.item_name + "'].simpleslot/3d_type)"
                asset_type = self.server.eval(expr)
                item_type = asset_type[0].get('name')
                final_path = base_path + project + "/casino/" + item_type + "/" + self.item_name + "/" + self.item_process + "/scenes/"
                base_filename = jc.abbrName(project) + "_" + jc.abbrItemType(item_type) + "_" + self.item_name + "_" + jc.abbrName(self.item_process)

                #filename = jc.abbrName(project) + "_" + jc.abbrItemType(item_type) + "_" + self.item_name + "_" + jc.abbrName(self.item_process) + "_" + jc.maxVersion(final_path, base_filename, "maya") + "_" + name + ext
                filename = jc.abbrName(project) + "_"  + jc.abbrItemType(item_type) + "_" + self.item_name + "_" + jc.abbrName(self.item_process) + "_" + jc.maxVersion(final_path, base_filename, "maya") + "_" + name + ext
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
        recent_file = ""
                
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
            self.ui.file_list.addItem(filename)           

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

        print "saved"
        self.finalPath()    

    def tacticLoad(self, arg=None):
        path = self.ui.save_path.text()
        filename = self.ui.file_list.currentItem().text()
        project_path = path.replace("scenes/", "")

        if appName == "3dsmax":
            import MaxPlus
            MaxPlus.FileManager.Open(path + filename)
            jc.maxWorkspaceFileRule(path)

        elif appName == "maya":
            import maya.cmds as cmds
            print path + filename
            cmds.file(modified=0)
            cmds.file((path + filename), open=True)
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
         
    def updateCache(self):
        expr = "@SOBJECT(simpleslot/game['project_status','.In Progress'])"
        inprogress = self.server.eval(expr)
        
        expr = "@SOBJECT(simpleslot/game['project_status','.Ready'])"
        ready = self.server.eval(expr)
        
        expr = "@SOBJECT(simpleslot/game['project_status','.Complete'])"
        complete = self.server.eval(expr)
        data = gamelist(inprogress)    
        test1 = self.server.update("simpleslot/plan?project=simpleslot&id=8", data)
        
        data = gamelist(ready)
        test2 = self.server.update("simpleslot/plan?project=simpleslot&id=10",data)
        
        data = gamelist(complete)
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
            server = TacticServerStub()
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

    if serverok == 1:
        try:
            widget.show()
        except:
            mainProcess(server=server)


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

qt_tactic_mainMain() # for addCustomShelf, the rule is filename + Main() 