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
global widget, server, recent_file, loginWidget


from PySide import QtCore, QtGui
from tactic_client_lib import TacticServerStub
server = TacticServerStub()

import ctypes
import qt_main_ui as qt_main_ui
import qt_login_ui
import os, shutil
import subprocess
import socket
import jc_maya_aux_functions as jc
from dateutil import parser

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
        global server
        from tactic_client_lib import TacticServerStub

        ticket_path = "c:/sthpw/etc"

        if os.path.exists(ticket_path) is False:
            os.makedirs(ticket_path)

        name = self.ui.login.text()
        password = self.ui.password.text()

        ticket_files = os.listdir("c:/sthpw/etc/")
        ticket_file = "c:/sthpw/etc/" + name + ".tacticrc"

        tactic_server_ip = socket.gethostbyname("vg.com")

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

        mainProcess()


class mainWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Tool)
        self.ui = qt_main_ui.Ui_main_window()
        self.ui.setupUi(self)

        self.ui.project_list.itemClicked.connect(getItems)
        # self.ui.tabProductionType.currentChanged.connect(getItems)
        self.ui.asset_list.itemClicked.connect(getProcess)
        self.ui.shot_list.itemClicked.connect(getProcess)

        self.ui.asset_process_list.itemClicked.connect(finalPath)
        self.ui.shot_process_list.itemClicked.connect(finalPath)
        self.ui.save_button.clicked.connect(tacticSave)
        self.ui.open_button.clicked.connect(tacticLoad)
        self.ui.open_path_button.clicked.connect(openPath)
        self.ui.logout_button.clicked.connect(logOut)

        self.ui.inprogress_button.clicked.connect(setInProgressFilter)
        self.ui.ready_button.clicked.connect(setReadyFilter)
        self.ui.complete_button.clicked.connect(setCompleteFilter)

        self.ui.publish_button.clicked.connect(publishMaster)
        self.ui.update_cache.clicked.connect(updateCache)

        #self.ui.inprogress_button.clicked.connect(getProjects)
        #self.ui.ready_button.clicked.connect(getProjects)
        #self.ui.complete_button.clicked.connect(getProjects)
        if "Nuke" in appName:
            pass
        else:
            sshFile = "//Art-1405260002/d/assets/scripts/maya_scripts/lib/darkorange.stylesheet"
            with open(sshFile, "r") as fh:
                self.setStyleSheet(fh.read())


def openPath():
    final_path = widget.ui.save_path.text()
    subprocess.check_call(['explorer', final_path.replace("/", "\\")])


def logOut():
    widget.close()
    name = server.login
    ticket_file = "c:/sthpw/etc/" + name + ".tacticrc"
    os.remove(ticket_file)
    loginProcess()


def setInProgressFilter():
    widget.ui.inprogress_button.setChecked(1)
    widget.ui.ready_button.setChecked(0)
    widget.ui.complete_button.setChecked(0)
    getProjects()

def setReadyFilter():
    widget.ui.inprogress_button.setChecked(0)
    widget.ui.ready_button.setChecked(1)
    widget.ui.complete_button.setChecked(0)
    getProjects()

def setCompleteFilter():
    widget.ui.inprogress_button.setChecked(0)
    widget.ui.ready_button.setChecked(0)
    widget.ui.complete_button.setChecked(1)
    getProjects()

def getProjects():
    openRecent()

    global projects_list
    inprogress = widget.ui.inprogress_button.isChecked()
    ready = widget.ui.ready_button.isChecked()
    complete = widget.ui.complete_button.isChecked()

    widget.ui.project_list.clear()

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
    temp = server.eval(expr)

    if inprogress == ready == complete == False:
        temp = ""

    names = bsd = bed = names_chn = games_type = assigned = ""

    for x in temp:
        names = names + x.get('name')
        bsd = bsd + x.get('login')
        bed = bed + x.get('keywords')
        names_chn = names_chn + x.get('game_name_chn')
        games_type = games_type + x.get('description')
        assigned = assigned + x.get('process')

    projects_list = {'name': names, 'login': bsd, 'keywords': bed, 'game_name_chn': names_chn, 'description': games_type, 'process': assigned}

    names = projects_list.get('name')
    names = names.split(" ")  # list is a space separated string
    names.pop(0)
    names = sorted(names)

    for name in names:
        widget.ui.project_list.addItem(name)

    if recent_file == "":
        clearAll()
    else:
        if recent_file[3][0] not in names:
            pass
        else:
            widget.ui.project_list.setCurrentItem(widget.ui.project_list.findItems(recent_file[3][0], QtCore.Qt.MatchExactly)[0])
            widget.ui.project_list.scrollToItem(widget.ui.project_list.findItems(recent_file[3][0], QtCore.Qt.MatchExactly)[0], QtGui.QAbstractItemView.EnsureVisible)
            getItems()

    return names


def clearAll():
    widget.ui.asset_list.clear()
    widget.ui.shot_list.clear()
    widget.ui.asset_process_list.clear()
    widget.ui.shot_process_list.clear()
    widget.ui.save_path.clear()
    widget.ui.save_file.clear()
    widget.ui.asset_info.clearContents()
    widget.ui.shot_info.clearContents()


def getItems():
    clearAll()

    game = widget.ui.project_list.currentItem().text()

    temp = projects_list

    names = temp.get('name')
    names = names.split(" ")

    bsd = temp.get('login')
    bsd = bsd.split("__")

    bed = temp.get('keywords')
    bed = bed.split("__")

    names_chn = temp.get('game_name_chn')
    names_chn = names_chn.split("__")

    games_type = temp.get('description')
    games_type = games_type.split(" ")

    assigned = temp.get('process')
    assigned = assigned.split(" ")

    temp = zip(names_chn, games_type, assigned, bsd, bed, names)
    temp.pop(0)

    def getNameKey(item):
        return item[0]

    temp = sorted(temp, key=getNameKey, reverse=False)

    for x in range(len(temp)):
        #if temp[x][5] in game:  # if selected is in inprogress list
        # make sure game is an exact match to temp[x][5], otherwise projects with _app or _cf suffix will aggregate
        if game == temp[x][5]:
            if temp[x][1] == "casino":  # if selected is casino or shot or assets
                updateList(temp[x][5], "3d", "assets")

            elif temp[x][1] == "sports" or temp[x][1] == "cf" or temp[x][1] == "video_conf":
                updateList(temp[x][5], "assets", "assets")
                updateList(temp[x][5], "shot", "shot")

            for z in range(len(temp[x])):
                widgetItem = QtGui.QTableWidgetItem(temp[x][z])
                widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
                widget.ui.project_info.setItem(z,0,widgetItem)

    # select first in item list if it contains anything

    if recent_file == "":
        production_type = productionType()
        if production_type == "assets":
            if widget.ui.asset_list.count() != 0:
                widget.ui.asset_list.setCurrentRow(0)
                widget.ui.tabProductionType.setCurrentIndex(0)

                getProcess()

        elif production_type == "shot":
            if widget.ui.shot_list.count() != 0:
                widget.ui.shot_list.setCurrentRow(0)
                widget.ui.tabProductionType.setCurrentIndex(1)

                getProcess()
    else:
        if recent_file[3][5] == "assets":
            if widget.ui.asset_list.count() != 0:
                widget.ui.tabProductionType.setCurrentIndex(0)
                widget.ui.asset_list.setCurrentItem(widget.ui.asset_list.findItems(recent_file[3][1], QtCore.Qt.MatchExactly)[0])
                widget.ui.asset_list.scrollToItem(widget.ui.asset_list.findItems(recent_file[3][1], QtCore.Qt.MatchExactly)[0], QtGui.QAbstractItemView.EnsureVisible)
                getProcess()

        elif recent_file[3][5] == "shot":
            if widget.ui.shot_list.count() != 0:
                widget.ui.tabProductionType.setCurrentIndex(1)
                widget.ui.shot_list.setCurrentItem(widget.ui.shot_list.findItems(recent_file[3][1], QtCore.Qt.MatchExactly)[0])
                widget.ui.shot_list.scrollToItem(widget.ui.shot_list.findItems(recent_file[3][1], QtCore.Qt.MatchExactly)[0], QtGui.QAbstractItemView.EnsureVisible)
                getProcess()


def updateList(name, stype, production_type):
    global asset_item_details
    global shot_item_details

    expr = "@SOBJECT(simpleslot/game['name','" + name + "'].simpleslot/" + stype + ")"
    temp = server.eval(expr)

    items = sorted(temp, key=lambda k: k['name'])

    if stype == "3d" or stype == "assets":
        asset_item_details = items
        names = [y['name'] for y in asset_item_details]

    else:
        shot_item_details = items
        names = [y['name'] for y in shot_item_details]

    for name in names:
        if production_type == "assets":
            widget.ui.asset_list.addItem(name)
        else:
            widget.ui.shot_list.addItem(name)


def orderProcesses(processes):
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


def productionType():
    if widget.ui.tabProductionType.currentIndex() == 0:
        production_type = "assets"
    elif widget.ui.tabProductionType.currentIndex() == 1:
        production_type = "shot"
    return production_type


def getProcess():
    global item_tasks
    global recent_file
    production_type = productionType()

    widget.ui.asset_process_list.clear()
    widget.ui.shot_process_list.clear()
    widget.ui.save_path.clear()
    widget.ui.save_file.clear()
    widget.ui.asset_info.clearContents()
    widget.ui.shot_info.clearContents()

    if production_type == "assets":
        selected = ""
        selected = widget.ui.asset_list.currentRow()
        item_name_chn = asset_item_details[selected].get('description')
        item_code = asset_item_details[selected].get('code')
        if widget.ui.project_info.item(1,0).text() == "casino":
            stype = "3d"
            item_type = asset_item_details[selected].get('3d_type_code')
            item_type = assetTypeCode(item_type)
        else:
            stype = "assets"
            item_type = asset_item_details[selected].get('asset_type_code')
            item_type = assetTypeCode(item_type)

    elif production_type == "shot":
        selected = ""
        selected = widget.ui.shot_list.currentRow()
        item_name_chn = shot_item_details[selected].get('description')
        item_type = "None"
        item_code = shot_item_details[selected].get('code')
        stype = "shot"

    expr = "@SOBJECT(simpleslot/" + stype + "['code','" + item_code + "'].sthpw/task)"
    item_tasks = server.eval(expr)

    bad = []
    bad.append("assets")
    processes = [y['process'] for y in item_tasks]

    processes = [y for y in processes if y not in bad]
    processes = set(processes)
    processes = list(processes)
    processes = orderProcesses(processes)

    for process in processes:
        if production_type == "assets" and widget.ui.asset_list.count() != 0:
            widget.ui.asset_process_list.addItem(process)
        elif production_type == "shot" and widget.ui.shot_list.count() != 0:
            widget.ui.shot_process_list.addItem(process)

    if production_type == "assets":
        if widget.ui.asset_list.count() != 0:
            if recent_file == "":
                widget.ui.asset_process_list.setCurrentRow(0)     # select first in process list if it contains anything
            else:
                widget.ui.asset_process_list.setCurrentItem(widget.ui.asset_process_list.findItems(recent_file[3][2], QtCore.Qt.MatchExactly)[0])

            widgetItem = QtGui.QTableWidgetItem(item_name_chn)
            widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
            widget.ui.asset_info.setItem(0,0,widgetItem)

            widgetItem = QtGui.QTableWidgetItem(item_type)
            widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
            widget.ui.asset_info.setItem(1,0,widgetItem)
            if widget.ui.asset_process_list.count() != 0:
                updateProcessInfo(production_type)
            finalPath()

    elif production_type == "shot":
        if widget.ui.shot_list.count() != 0:
            if recent_file == "":
                widget.ui.shot_process_list.setCurrentRow(0)
            else:
                widget.ui.shot_process_list.setCurrentItem(widget.ui.shot_process_list.findItems(recent_file[3][2], QtCore.Qt.MatchExactly)[0])

            widgetItem = QtGui.QTableWidgetItem(item_name_chn)
            widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
            widget.ui.shot_info.setItem(0,0,widgetItem)

            widgetItem = QtGui.QTableWidgetItem(item_type)
            widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
            widget.ui.shot_info.setItem(1,0,widgetItem)
            if widget.ui.shot_process_list.count() != 0:
                updateProcessInfo(production_type)
            finalPath()
    recent_file = ""  # set to none, this is so locating recent file will only run once, when the widget is initialized.


def updateProcessInfo(production_type):
    selected_process = ""
    if production_type == "assets":
        if widget.ui.asset_process_list.count() != 0:
            selected_process = widget.ui.asset_process_list.currentItem().text()
    elif production_type == "shot":
        if widget.ui.shot_process_list.count() != 0:
            selected_process = widget.ui.shot_process_list.currentItem().text()

    assigned = ""
    bsd = ""
    bed = ""
    for x in item_tasks:
        if x.get("process") == selected_process:
            # task_search_key = x.get("__search_key__")
            assigned = assigned + ", " + x.get("assigned")
            bsd = bsd + ", " + x.get("bid_start_date")[5:-9]
            bed = bed + ", " + x.get("bid_end_date")[5:-9]
    assigned = assigned[2:]
    bsd = bsd[2:]
    bed = bed[2:]

    process_infos = [assigned, bsd, bed]

    for x in range(0, len(process_infos)):
        index = 2 + x
        widgetItem = QtGui.QTableWidgetItem(process_infos[x])
        widgetItem.setTextAlignment(QtCore.Qt.AlignHCenter)
        if production_type is "assets":
            widget.ui.asset_info.setItem(index, 0, widgetItem)
        if production_type is "shot":
            widget.ui.shot_info.setItem(index, 0, widgetItem)


def assetTypeCode(code):
    if code == "ASSET_TYPE00002":
        asset_type = "Character"
    elif code == "ASSET_TYPE00003":
        asset_type = "Vehicles"
    elif code == "ASSET_TYPE00004":
        asset_type = "Sets"
    elif code == "ASSET_TYPE00005":
        asset_type = "Props"
    elif code == "ASSET_TYPE00006":
        asset_type = "Misc"
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

def getUIInfo():
    try:
        project = widget.ui.project_list.currentItem().text()
    except:
        project = ""
    try:
        assets = widget.ui.asset_list.currentItem().text()
    except:
        assets = ""
    try:
        shot = widget.ui.shot_list.currentItem().text()
    except:
        shot = ""
    try:
        asset_process = widget.ui.asset_process_list.currentItem().text()
    except:
        asset_process = ""
    try:
        shot_process = widget.ui.shot_process_list.currentItem().text()
    except:
        shot_process = ""

    project_type = widget.ui.project_info.item(1,0).text()
    production_type = productionType()

    if production_type == "assets":
        return project, project_type, production_type, assets, asset_process
    elif production_type == "shot":
        return project, project_type, production_type, shot, shot_process


def updateFileList(final_path, base_filename): # use getfilelist() and update ui
    fileList = []
    widget.ui.file_list.clear()

    if os.path.exists(final_path) is True:
        savedFiles = os.listdir(final_path)
        if len(savedFiles) == 0:
            pass
        else:
            fileList = [x for x in savedFiles if base_filename in x]
    else:
        pass

    for filename in fileList:
        widget.ui.file_list.addItem(filename)


def tacticSave(arg=None):
    path = widget.ui.save_path.text()
    filename = widget.ui.save_file.text()

    if not os.path.exists(path):
        os.makedirs(path)
    final = path + filename

    if appName == "3dsmax":
        import MaxPlus
        jc.maxWorkspaceFileRule(path)
        #MaxPlus.PathManager.SetSceneDir(path)
        MaxPlus.FileManager.Save(final)
        #MaxPlus.PathManager.SetProjectFolderDir(path)

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
    finalPath()

'''
def forceLoad(arg=None):
    filename = cmds.textScrollList("fileList", q=True, si=True)[0]
    path = cmds.textField("final_path", q=1, tx=1)
    cmds.file(modified=0)
    cmds.file((path + filename), open=1)
    if cmds.window("error", exists=True):
        cmds.deleteUI("error")


def stdSave(arg=None):
    filename = cmds.textScrollList("fileList", q=True, si=True)[0]
    # path = cmds.textField("final_path", q=1, tx=1)
    cmds.file(save=1, type='mayaBinary')
    cmds.setAttr("defaultRenderGlobals.imageFilePrefix", filename, type="string")
    if cmds.window("error", exists=True):
        cmds.deleteUI("error")
'''

def tacticLoad(arg=None):
    path = widget.ui.save_path.text()
    filename = widget.ui.file_list.currentItem().text()
    project_path = path.replace("scenes/", "")
    #app = QtGui.QApplication.instance()
    #appName = app.objectName()

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


def publishMaster(arg=None):
    path = widget.ui.save_path.text()
    filename = widget.ui.file_list.currentItem().text()

    master = filename.split("_")
    ext = master.pop(len(master) - 1)
    master.pop(len(master) - 1)

    ext = ext.split(".")[1]

    final = ""
    for x in master:
        final = final + "_" + x

    final = final[1:]

    destination = path.replace("scenes/","") + final + "_master." + ext

    source = path + filename

    print source, destination
    shutil.copy2(source, destination)


def finalPath():
    base_path = "//art-render/art_3d_project/"
    name = server.login

    uiinfo = getUIInfo()

    project = uiinfo[0]
    project_type = uiinfo[1]
    selectedTab = uiinfo[2]
    updateProcessInfo(selectedTab)
    item_name = uiinfo[3]
    item_process = uiinfo[4]
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

    if selectedTab == "assets":
        if project_type == "cf" or project_type == "sports" or project_type == "video_conf":
            expr = "@SOBJECT(simpleslot/game['name','" + project + "'].simpleslot/assets['name','" + item_name + "'].simpleslot/asset_type)"
            asset_type = server.eval(expr)
            item_type = asset_type[0].get('name')
            final_path = base_path + project + "/assets/" + item_type + "/" + item_name + "/" + item_process + "/scenes/"
            base_filename = jc.abbrName(project) + "_" + jc.abbrItemType(item_type) + "_" + item_name + "_" + jc.abbrName(item_process)

            filename = jc.abbrName(project) + "_" + jc.abbrItemType(item_type) + "_" + item_name + "_" + jc.abbrName(item_process) + "_" + jc.maxVersion(final_path, base_filename, "maya") + "_" + name + ext
            project_type = "assets"

        elif project_type == "casino":
            expr = "@SOBJECT(simpleslot/game['name','" + project + "'].simpleslot/3d['name','" + item_name + "'].simpleslot/3d_type)"
            asset_type = server.eval(expr)
            item_type = asset_type[0].get('name')
            final_path = base_path + project + "/casino/" + item_type + "/" + item_name + "/" + item_process + "/scenes/"
            base_filename = jc.abbrName(project) + "_" + jc.abbrItemType(item_type) + "_" + item_name + "_" + jc.abbrName(item_process)

            #filename = jc.abbrName(project) + "_" + jc.abbrItemType(item_type) + "_" + item_name + "_" + jc.abbrName(item_process) + "_" + jc.maxVersion(final_path, base_filename, "maya") + "_" + name + ext
            filename = jc.abbrName(project) + "_"  + jc.abbrItemType(item_type) + "_" + item_name + "_" + jc.abbrName(item_process) + "_" + jc.maxVersion(final_path, base_filename, "maya") + "_" + name + ext
            project_type = "assets"

    elif selectedTab == "shot":
        final_path = base_path + project + "/shot/" + item_name + "/" + item_process + "/scenes/"
        base_filename = jc.abbrName(project) + "_" + item_name + "_" + jc.abbrName(item_process)

        filename = jc.abbrName(project) + "_" + item_name + "_" + jc.abbrName(item_process) + "_" + jc.maxVersion(final_path, base_filename, "maya") + "_" + name + ext
        project_type = "shot"

    final_path = final_path.replace(" ", "")

    if selectedTab == "assets":
        if widget.ui.asset_list.count() != 0 and widget.ui.asset_process_list.count() != 0:
            widget.ui.save_path.setText(final_path)
            widget.ui.save_file.setText(filename)
    elif selectedTab == "shot":
        if widget.ui.shot_list.count() != 0 and widget.ui.shot_process_list.count() != 0:
            widget.ui.save_path.setText(final_path)
            widget.ui.save_file.setText(filename)


    print final_path
    try:
        updateFileList(final_path, base_filename)
    except:
        print "updateFilelist failed"
    recent_file = ""

def loginProcess():
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

def openRecent():
    global recent_file
    recent_file = ""
    if widget.ui.inprogress_button.isChecked() == False:
            recent_file = ""
    else:
        try:
            recent_file = jc.getNextFileName(0)
        except:
            recent_file = ""
        '''
    project_path = recent_file[0]
    project_filename = recent_file[2]
    base_scenename = recent_file[1]

    project_name = recent_file[3][0]
    item_name = recent_file[3][1]
    process = recent_file[3][2]
    author = recent_file[3][3]
    reviewVersion = recent_file[3][4]
    project_type = recent_file[3][5]
    if project_type != "shot":
        item_type = recent_file[3][6]

    widget.ui.project_list.setCurrentItem(widget.ui.project_list.findItems(project_name, QtCore.Qt.MatchExactly)[0])
    '''

def mainProcess():
    global widget
    global loginWidget
    global server
    login_name = server.login
    widget = mainWindow(parent=QtGui.QApplication.activeWindow())
    widget.ui.login_name.setText(login_name)

    getProjects()

    if appName == "3dsmax":
        _GCProtector.widgets.append(widget)
        widget.setWindowFlags(widget.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        capsule = widget.effectiveWinId()
        ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
        ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
        ptr = ctypes.pythonapi.PyCObject_AsVoidPtr(capsule)

    try:
        loginWidget.close()
    except:
        pass

    widget.show()

    '''
    try:
        MaxPlus.Win32.Set3dsMaxAsParentWindow(ptr)
    except:
        pass
        '''

def qt_tactic_mainMain():
    global server
    try:
        expr = "@GET(sthpw/login.login)"
        temp = server.eval(expr)
        serverok = 1
    except:
        print "servernotok"
        try:
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
            print "notok"
            loginProcess()

    if serverok == 1:
        try:
            widget.show()
        except:
            mainProcess()

def gamelist(items):
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
        depts = server.eval(expr)
    
        expr = "@GET(simpleslot/game['name','" + name + "'].simpleslot/game_type.name)"
        game_type = server.eval(expr)
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
                assignments = assignments + " " + assignment
                names = names + " " + name
                games_type = games_type + " " + game_type[0]
                names_chn = names_chn + "__" + name_chn
    data = {'name': names, 'description': games_type, 'login': bsd_string, 'keywords': bed_string, 'timestamp': str(now), 'game_name_chn': names_chn, 'process': assignments}
    return data

def updateCache():
    expr = "@SOBJECT(simpleslot/game['project_status','.In Progress'])"
    inprogress = server.eval(expr)
    
    expr = "@SOBJECT(simpleslot/game['project_status','.Ready'])"
    ready = server.eval(expr)
    
    expr = "@SOBJECT(simpleslot/game['project_status','.Complete'])"
    complete = server.eval(expr)
    data = gamelist(inprogress)    
    test1 = server.update("simpleslot/plan?project=simpleslot&id=8", data)
    
    data = gamelist(ready)
    test2 = server.update("simpleslot/plan?project=simpleslot&id=10",data)
    
    data = gamelist(complete)
    test3 = server.update("simpleslot/plan?project=simpleslot&id=11", data)
    return "update complete"
#%%
if __name__ == "__main__":
    qt_tactic_mainMain() # for addCustomShelf, the rule is filename + Main()
