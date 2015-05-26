# -*- coding: utf-8 -*-
# global sys, socket, errno, os, six, datetime, parser, TacticServerStub, cmds

import sys
sys.path.append("//Art-1405260002/d/assets/client")

import socket
import errno
import os
import maya.cmds as cmds
import jc_maya_aux_functions as jc
import shutil


username = os.environ.get("USERNAME")
ticket_file = "c:/sthpw/etc/" + username + ".tacticrc"
base = os.path.split(ticket_file)

if os.path.exists(base[0]) is False:
    os.makedirs(base[0])
if os.path.exists(ticket_file) is False:
    file_object = open(ticket_file, "w")
    ticket_content = "login=" + username + "\n"
    ticket_content = ticket_content + "server=192.168.201.10" + "\n"
    ticket_content = ticket_content + "ticket=\n"
    ticket_content = ticket_content + "project=simpleslot"

    file_object.write(ticket_content)
    file_object.close()

from tactic_client_lib import TacticServerStub
server = TacticServerStub()
server.set_server("192.168.201.10")
server.set_project("simpleslot")
asset_item_details = ""
shot_item_details = ""

def login(arg=None):
    try:
        name = cmds.textField("login", q=1, tx=1)
        password = cmds.textField("password", q=1, tx=1)
        ticket = server.get_ticket(name, password)
        server.set_ticket(ticket)
        username = os.environ.get("USERNAME")
        ticket_file = "c:/sthpw/etc/" + username + ".tacticrc"
        file_object = open(ticket_file, "w")
        ticket_content = "login=" + name + "\n" + "server=192.168.201.10" + "\n" + "ticket=" + ticket + "\n" + "project=simpleslot"
        file_object.write(ticket_content)
        file_object.close()
        cmds.deleteUI("login")
        mainUI()
        return True

    except socket.error as error:
        if error.errno == errno.WSAECONNRESET:
            print error.errno
            mainUI()
        else:
            raise
    except:
        windowID = cmds.window("error", sizeable=False)
        cmds.rowColumnLayout()
        cmds.button(label=jc.uniDecode("登入/密碼不對"), c=loginUI)
        cmds.showWindow(windowID)
        return False


def loginUI(arg=None):
    if cmds.window("error", exists=True):
        cmds.deleteUI("error")
    if cmds.window("login", exists=True):
        cmds.deleteUI("login")
    name = server.login
    windowID = cmds.window("login", sizeable=False)
    cmds.rowColumnLayout(nr=2)

    cmds.rowColumnLayout(nc=2, cw=[(1, 50), (2, 120)])
    cmds.text(label="Login")
    cmds.textField("login", tx=name)
    cmds.text(label="Password")
    cmds.textField("password", ec=login)
    cmds.setParent('..')

    cmds.rowColumnLayout(nc=1, cw=[(1, 170)])
    cmds.button(label=jc.uniDecode("登入"), c=login)

    cmds.showWindow(windowID)


def updateFileList(final_path, base_filename): # use getfilelist() and update ui
    fileList = []
    if os.path.exists(final_path) is True:
        savedFiles = os.listdir(final_path)
        if len(savedFiles) == 0:
            pass
        else:
            fileList = [x for x in savedFiles if base_filename in x]
    else:
        pass
    cmds.textScrollList("fileList", edit=1, removeAll=1)
    cmds.textScrollList("fileList", edit=1, append=fileList)


def getUIInfo():
    try:
        project = cmds.textScrollList("projectMenu", q=True, si=True)[0]
    except:
        project = ""
    try:
        assets = cmds.textScrollList("assetsList", q=True, si=True)[0]
    except:
        assets = ""
    try:
        shot = cmds.textScrollList("shotList", q=True, si=True)[0]
    except:
        shot = ""
    try:
        asset_process = cmds.textScrollList("assetsProcessList", q=True, si=True)[0]
    except:
        asset_process = ""
    try:
        shot_process = cmds.textScrollList("shotProcessList", q=True, si=True)[0]
    except:
        shot_process = ""

    project_type = cmds.text("project_type", q=True, label=True)
    selectedTab = cmds.tabLayout("items", q=True, sti=True)

    if selectedTab == 1:
        return project, project_type, selectedTab, assets, asset_process
    elif selectedTab == 2:
        return project, project_type, selectedTab, shot, shot_process


def getNames():
    global projects_list
    expr = "@SOBJECT(simpleslot/plan['id','8'])"
    temp = server.eval(expr)
    projects_list = temp
    names = temp[0].get('name')
    names = names.split(" ")  # list is a space separated string
    names.pop(0)
    names = sorted(names)
    return names


def getItems():
    game = cmds.textScrollList("projectMenu", q=True, si=True)
    game = game[0]

    temp = projects_list

    names = temp[0].get('name')
    names = names.split(" ")

    bsd = temp[0].get('login')
    bsd = bsd.split("__")

    bed = temp[0].get('keywords')
    bed = bed.split("__")

    names_chn = temp[0].get('game_name_chn')
    names_chn = names_chn.split("__")

    games_type = temp[0].get('description')
    games_type = games_type.split(" ")

    assigned = temp[0].get('process')
    assigned = assigned.split(" ")

    temp = zip(names, games_type, bsd, bed, names_chn, assigned)
    temp.pop(0)

    def getNameKey(item):
        return item[0]
    temp = sorted(temp, key=getNameKey, reverse=False)

    cmds.textScrollList("assetsList", edit=True, removeAll=True)
    cmds.textScrollList("shotList", edit=True, removeAll=True)

    for x in range(len(temp)):
        if temp[x][0] == game:  # if selected is in inprogress list
            if temp[x][1] == "casino":  # if selected is casino or shot or assets
                updateList(temp[x][0], "3d", "assets")

            elif temp[x][1] == "sports" or temp[x][1] == "cf":
                updateList(temp[x][0], "assets", "assets")
                updateList(temp[x][0], "shot", "shot")

            cmds.text("project_type", edit=True, label=temp[x][1])
            cmds.text("bsd", edit=True, label=temp[x][2])
            cmds.text("bed", edit=True, label=temp[x][3])
            cmds.text("project_name_chn", edit=True, label=temp[x][4])
            cmds.text("project_supervisor", edit=True, label=temp[x][5])

    selectedTab = cmds.tabLayout("items", q=True, sti=True)
    if selectedTab == 1:
        production_type = "assets"
    elif selectedTab == 2:
        production_type = "shot"

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

    cmds.textScrollList(production_type + "List", edit=True, append=names)
    if cmds.textScrollList(production_type + "List", q=True, ni=1) != 0:
        cmds.textScrollList(production_type + "List", edit=True, sii=1)

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

def getProcess():
    global item_tasks

    production_type = productionType()
    selected = ""
    selected = (cmds.textScrollList(production_type + "List", q=True, sii=1))[0] - 1

    if production_type == "assets":
        item_name_chn = asset_item_details[selected].get('description')

        item_code = asset_item_details[selected].get('code')
        if cmds.text("project_type", q=1, l=1) == "casino":
            stype = "3d"
            item_type = asset_item_details[selected].get('3d_type_code')
            item_type = assetTypeCode(item_type)
        else:
            stype = "assets"
            item_type = asset_item_details[selected].get('asset_type_code')
            item_type = assetTypeCode(item_type)

    elif production_type == "shot":
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

    cmds.textScrollList(production_type + "ProcessList", edit=True, removeAll=True)
    cmds.textScrollList(production_type + "ProcessList", edit=True, append=processes)

    if cmds.textScrollList(production_type + "ProcessList", q=True, sii=1) is None:
        cmds.textScrollList(production_type + "ProcessList", e=True, sii=1)
    else:
        pass

    cmds.text("item_name_chn", e=1, label=item_name_chn)
    cmds.text("item_type", e=1, label=jc.uniDecode(item_type))
    # cmds.text("assigned", e=1, label=processes)
    # updateProcessInfo()
    finalPath()

def productionType():
    selectedTab = cmds.tabLayout("items", q=True, sti=True)
    if selectedTab == 1:
        production_type = "assets"
    elif selectedTab == 2:
        production_type = "shot"
    return production_type


def updateProcessInfo():
    global task_search_key
    production_type = productionType()
    selected_process = (cmds.textScrollList(production_type + "ProcessList", q=True, si=1))[0]
    assigned = ""
    bsd = ""
    bed = ""
    for x in item_tasks:
        if x.get("process") == selected_process:
            task_search_key = x.get("__search_key__")
            assigned = assigned + ", " + x.get("assigned")
            bsd = bsd + ", " + x.get("bid_start_date")[5:-9]
            bed = bed + ", " + x.get("bid_end_date")[5:-9]
    assigned = assigned[2:]
    bsd = bsd[2:]
    bed = bed[2:]

    cmds.text("assigned", e=1, l=assigned)
    cmds.text("item_bsd", e=1, l=bsd)
    cmds.text("item_bed", e=1, l=bed)


def finalPath():
    updateProcessInfo()
    base_path = "//art-render/art_3d_project/"
    name = server.login
    uiinfo = getUIInfo()
    project = uiinfo[0]
    project_type = uiinfo[1]
    selectedTab = uiinfo[2]
    item_name = uiinfo[3]
    item_process = uiinfo[4]
    final_path = ""
    item_type = ""
    if selectedTab == 1:
        if project_type == "cf" or project_type == "sports":
            expr = "@SOBJECT(simpleslot/game['name','" + project + "'].simpleslot/assets['name','" + item_name + "'].simpleslot/asset_type)"
            asset_type = server.eval(expr)
            item_type = asset_type[0].get('name')
            final_path = base_path + project + "/assets/" + item_type + "/" + item_name + "/" + item_process + "/scenes/"
            base_filename = jc.abbrName(project) + "_" + jc.abbrItemType(item_type) + "_" + item_name + "_" + jc.abbrName(item_process)

            filename = jc.abbrName(project) + "_" + jc.abbrItemType(item_type) + "_" + item_name + "_" + jc.abbrName(item_process) + "_" + jc.maxVersion(final_path, base_filename, "maya") + "_" + name + ".mb"
            project_type = "assets"

        elif project_type == "casino":
            expr = "@SOBJECT(simpleslot/game['name','" + project + "'].simpleslot/3d['name','" + item_name + "'].simpleslot/3d_type)"
            asset_type = server.eval(expr)
            item_type = asset_type[0].get('name')
            final_path = base_path + project + "/casino/" + item_type + "/" + item_name + "/" + item_process + "/scenes/"
            base_filename = jc.abbrName(project) + "_" + jc.abbrItemType(item_type) + "_" + item_name + "_" + jc.abbrName(item_process)

            filename = jc.abbrName(project) + "_" + jc.abbrItemType(item_type) + "_" + item_name + "_" + jc.abbrName(item_process) + "_" + jc.maxVersion(final_path, base_filename, "maya") + "_" + name + ".mb"
            project_type = "assets"

    elif selectedTab == 2:
        final_path = base_path + project + "/shot/" + item_name + "/" + item_process + "/scenes/"
        base_filename = jc.abbrName(project) + "_" + item_name + "_" + jc.abbrName(item_process)

        filename = jc.abbrName(project) + "_" + item_name + "_" + jc.abbrName(item_process) + "_" + jc.maxVersion(final_path, base_filename, "maya") + "_" + name + ".mb"
        project_type = "shot"

    final_path = final_path.replace(" ", "")

    cmds.textField("final_path", edit=True, tx=final_path, enterCommand=('cmds.setFocus(\"' + final_path + '\")'))
    cmds.textField("basename", edit=True, tx=filename, enterCommand=('cmds.setFocus(\"' + final_path + '\")'))
    updateFileList(final_path, base_filename)

def assetTypeCode(code):
    if code == "ASSET_TYPE00002":
        asset_type = "角色/Character"
    elif code == "ASSET_TYPE00003":
        asset_type = "車/Vehicles"
    elif code == "ASSET_TYPE00004":
        asset_type = "場景/Sets"
    elif code == "ASSET_TYPE00005":
        asset_type = "道具/Props"
    elif code == "ASSET_TYPE00006":
        asset_type = "其它/Misc"
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


def workspaceFileRule(project_path):
    project_path = project_path.replace("scenes/","")
    cmds.workspace(project_path, o=1)
    garbage = 'garbage'

    cmds.workspace(fileRule=['scene', 'scenes'])
    cmds.workspace(fileRule=['templates', garbage + '/templates'])
    cmds.workspace(fileRule=['images', 'images'])
    cmds.workspace(fileRule=['sourceImages', 'sourceimages'])
    cmds.workspace(fileRule=['renderData', garbage])
    cmds.workspace(fileRule=['clips', garbage])
    cmds.workspace(fileRule=['sound', garbage])
    cmds.workspace(fileRule=['scripts', garbage])
    cmds.workspace(fileRule=['diskCache', garbage + '/data'])
    cmds.workspace(fileRule=['movie', garbage])
    cmds.workspace(fileRule=['translatorData', garbage])
    cmds.workspace(fileRule=['autoSave', garbage])

    cmds.workspace(fileRule=['offlineEdit', garbage])
    cmds.workspace(fileRule=['3dPaintTextures', 'sourceimages/3dPaintTextures'])
    cmds.workspace(fileRule=['depth', garbage + '/depth'])
    cmds.workspace(fileRule=['iprImages', garbage + '/iprImages'])
    cmds.workspace(fileRule=['shaders', garbage + '/shaders'])
    cmds.workspace(fileRule=['furFiles', garbage + '/fur/furFiles'])
    cmds.workspace(fileRule=['furImages', garbage + '/fur/furImages'])
    cmds.workspace(fileRule=['furEqualMap', garbage + '/fur/furEqualMap'])
    cmds.workspace(fileRule=['furAttrMap', garbage + '/fur/furAttrMap'])
    cmds.workspace(fileRule=['furShadowMap', garbage + '/fur/furShadowMap'])
    cmds.workspace(fileRule=['particles', garbage + '/particles'])
    cmds.workspace(fileRule=['fluidCache', garbage + '/nCache/fluid'])
    cmds.workspace(fileRule=['fileCache', garbage + '/nCache'])

    '''
    cmds.workspace(fileRule=['eps', 'data'])
    cmds.workspace(fileRule=['OBJexport', 'data'])
    cmds.workspace(fileRule=['mel', 'scripts'])
    cmds.workspace(fileRule=['STEP_DC', 'data'])
    cmds.workspace(fileRule=['CATIAV5_DC', 'data'])
    cmds.workspace(fileRule=['CATIAV4_DC', 'data'])
    cmds.workspace(fileRule=['IPT_DC', 'data'])
    cmds.workspace(fileRule=['SW_DC', 'test/test/test'])
    cmds.workspace(fileRule=['DAE_FBX export', 'data'])
    cmds.workspace(fileRule=['Autodesk Packet File', 'data'])
    cmds.workspace(fileRule=['DAE_FBX', 'data'])
    cmds.workspace(fileRule=['DXF_DCE', 'data'])
    cmds.workspace(fileRule=['mayaAscii', 'scenes'])
    cmds.workspace(fileRule=['move', 'data'])
    cmds.workspace(fileRule=['mayaBinary', 'scenes'])
    cmds.workspace(fileRule=['DWG_DC', 'data'])
    cmds.workspace(fileRule=['DXF_DC', 'data'])
    cmds.workspace(fileRule=['SPF_DCE', 'data'])
    cmds.workspace(fileRule=['ZPR_DCE', 'data'])
    cmds.workspace(fileRule=['audio', 'sound'])
    cmds.workspace(fileRule=['IV_DC', 'data'])
    cmds.workspace(fileRule=['STL_DCE', 'data'])
    cmds.workspace(fileRule=['FBX export', 'data'])
    cmds.workspace(fileRule=['JT_DC', 'data'])
    cmds.workspace(fileRule=['DWG_DCE', 'data'])
    cmds.workspace(fileRule=['FBX', 'data'])
    cmds.workspace(fileRule=['Alembic', 'data'])
    cmds.workspace(fileRule=['IGES_DC', 'data'])
    cmds.workspace(fileRule=['illustrator', 'data'])
    cmds.workspace(fileRule=['UG_DC', 'data'])
    cmds.workspace(fileRule=['SPF_DC', 'data'])
    cmds.workspace(fileRule=['PTC_DC', 'data'])
    cmds.workspace(fileRule=['OBJ', 'data'])
    cmds.workspace(fileRule=['CSB_DC', 'data'])
    cmds.workspace(fileRule=['STL_DC', 'data'])
    cmds.workspace(fileRule=['IGES_DCE', 'data'])
    cmds.workspace(fileRule=['UG_DCE', 'data'])
    '''


def tacticSave(arg=None):
    if cmds.window("error", exists=True):
        cmds.deleteUI("error")
    path = cmds.textField("final_path", query=True, tx=True)
    filename = cmds.textField("basename", query=True, tx=True)
    if not os.path.exists(path):
        os.makedirs(path)
    final = path + filename
    # project_path = cmds.textField("project_path", q=1, tx=1)

    workspaceFileRule(path)

    cmds.file(rename=final)
    cmds.file(save=True, type='mayaBinary')
    cmds.setAttr("defaultRenderGlobals.imageFilePrefix", filename.replace(".mb", ""), type="string")

    print "saved"
    '''
    game = cmds.textScrollList("projectMenu", q=True, si=True)
    game = game[0]
    project_type = cmds.text("project_type", q=True, label=True)
    if project_type == "casino":
        project_type = "3d"
        process = cmds.textScrollList("assetsProcessList", q=True, si=True)
        process = process[0]
        item = cmds.textScrollList("assetsList", q=True, si=True)

    elif project_type == "sports" or project_type == "cf":
        selectedTab = cmds.tabLayout("items", q=True, sti=True)
        if selectedTab == 1:
            project_type = "assets"
            process = cmds.textScrollList("assetsProcessList", q=True, si=True)
            process = process[0]
            item = cmds.textScrollList("assetsList", q=True, si=True)
        elif selectedTab == 2:
            project_type = "shot"
            process = cmds.textScrollList("shotProcessList", q=True, si=True)
            process = process[0]
            item = cmds.textScrollList("shotList", q=True, si=True)

    expr = "@SOBJECT(simpleslot/game['name','" + game + "'].simpleslot/" + project_type + "['name','" + item[0] + "'].sthpw/task['process','" + process + "'])"
    task = server.eval(expr)
    if len(task) == 0:
        windowID = cmds.window("error", sizeable=False)
        cmds.rowColumnLayout()
        cmds.button(label=jc.uniDecode("TACTIC 上沒有規劃這個物件或流程"), c='cmds.deleteUI("error")')
        cmds.showWindow(windowID)
    else:
        sk = task[0].get('__search_key__')
        # snapshot = server.create_snapshot(sk, (path + filename), "maya binary", "maya file", "None", 0, 0)
        # snapshot_code = snapshot.get('code')
        # server.add_file(snapshot_code, (path + filename), create_icon=True, mode='inplace')
    '''
    finalPath()


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


def tacticLoad(arg=None):
    filename = cmds.textScrollList("fileList", q=True, si=True)
    path = cmds.textField("final_path", q=1, tx=1)
    # project_path = cmds.textField("project_path", q=1, tx=1)
    # project_path = path.replace("scenes/", "")

    if cmds.file(q=True, modified=True) is True:
        if cmds.window("error", exists=True):
            cmds.deleteUI("error")
        errorWindow = cmds.window("error", sizeable=False)
        cmds.rowColumnLayout(nr=4, rs=[(1, 5), (2, 5), (3, 5)])
        cmds.picture(image="//Art-1405260002/d/assets/scripts/font-awesome-4.1.0/png/exclamation-circle_ff0000_128.png", bgc=(1, 1, 1))
        cmds.button(label=jc.uniDecode("存檔 最大版本 + 1?"), c=tacticSave)
        cmds.button(label=jc.uniDecode("存檔?"), c=stdSave)
        cmds.button(label=jc.uniDecode("繼續開檔!"), c=forceLoad)
        cmds.showWindow(errorWindow)
    else:
        pass
        cmds.file((path + filename[0]), open=True)
    workspaceFileRule(path)


def publishMaster(arg=None):
    path = cmds.textField("final_path", query=True, tx=True)
    filename = (cmds.textScrollList("fileList", q=True, si=True))[0]
    temp = filename.split("_")
    final = ""
    for x in temp:
        if x.startswith("v"):
            break
        final = final + "_" + x

    final = final[1:]

    destination = path.replace("scenes/","") + final + "_master.mb"
    
    source = path + filename
    
    print source, destination
    shutil.copy2(source, destination)


def closeWindow(arg=None):
    if cmds.window("TACTIC2MAYA", exists=True):
        cmds.deleteUI("TACTIC2MAYA")


def mainUI():
    if cmds.window("TACTIC2MAYA", exists=True):
        cmds.deleteUI("TACTIC2MAYA")
    names = []
    names = getNames()
    windowID = cmds.window("TACTIC2MAYA", sizeable=False)
    # parent window

    cmds.rowColumnLayout(nr=25, rs=[(1, 10), (2, 10), (3, 10)])  # top panel is project, bottom panel are tabs for shots and assets

    cmds.rowColumnLayout(nc=2, cw=[(1, 200), (2, 350)])

    # panel 1
    cmds.tabLayout("Projects")
    proj_child1 = cmds.rowColumnLayout(nc=1, cw=[(1, 200)])
    cmds.text(label="Projects")
    cmds.textScrollList("projectMenu", append=names, sc=getItems)
    cmds.setParent('..')
    cmds.tabLayout("Projects", edit=True, tabLabel=((proj_child1, 'Projects')))
    cmds.setParent('..')

    # panel 2
    cmds.tabLayout("items")
    child1 = cmds.rowColumnLayout(nc=2, cw=[(1, 250), (2, 100)])
    cmds.text(label="Assets")
    cmds.text(label="Process")
    cmds.textScrollList("assetsList", sc=getProcess)
    cmds.textScrollList("assetsProcessList", append="", sc=finalPath)
    cmds.setParent('..')  # parent row
    child2 = cmds.rowColumnLayout(nc=2, cw=[(1, 250), (2, 100)])
    cmds.text(label="Shots")
    cmds.text(label="Process")
    cmds.textScrollList("shotList", sc=getProcess)
    cmds.textScrollList("shotProcessList", append="", sc=finalPath)
    cmds.setParent('..')
    cmds.tabLayout("items", edit=True, tabLabel=((child1, 'Assets'), (child2, 'Shots')))
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.separator(style="in", h=1)
    cmds.setParent('..')

    cmds.rowColumnLayout("info_panel", nc=3, cw=[(1, 195), (2, 10), (3, 240)])

    # info panel 1 (project info)
    cs1 = [1, 15]
    grey = [.3, .3, .3]

    cmds.rowColumnLayout("project_info", nr=5)
    cmds.rowColumnLayout(nc=2, cw=[(1, 35), (2, 160)], cs=cs1)
    cmds.text(label=jc.uniDecode("專案:"))
    cmds.text("project_name_chn", label="", fn="boldLabelFont", bgc=grey)
    cmds.setParent('..')

    cmds.rowColumnLayout(nc=2, cw=[(1, 35), (2, 160)], cs=cs1)
    cmds.text(label=jc.uniDecode("案型:"))
    cmds.text("project_type", label="")
    cmds.setParent('..')

    cmds.rowColumnLayout(nc=2, cw=[(1, 35), (2, 160)], cs=cs1)
    cmds.text(label=jc.uniDecode("窗口:"))
    cmds.text("project_supervisor", label="", bgc=grey)
    cmds.setParent('..')

    cmds.rowColumnLayout(nc=2, cw=[(1, 35), (2, 160)], cs=cs1)
    cmds.text(label=jc.uniDecode("開始:"))
    cmds.text("bsd", label="", al="center")
    cmds.setParent('..')

    cmds.rowColumnLayout(nc=2, cw=[(1, 35), (2, 160)], cs=cs1)
    cmds.text(label=jc.uniDecode("結束:"))
    cmds.text("bed", label="", al="center", bgc=grey )
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.separator(style="in", hr=0)

    cmds.rowColumnLayout(nr=5)
    cmds.rowColumnLayout(nc=2, cw=[(1, 35), (2, 160)])
    cmds.text(label=jc.uniDecode("物件:"))
    cmds.text("item_name_chn", label="", fn="boldLabelFont", bgc=grey)
    cmds.setParent('..')

    cmds.rowColumnLayout(nc=2, cw=[(1, 35), (2, 160)])
    cmds.text(label=jc.uniDecode("類型:"))
    cmds.text("item_type", label="")
    cmds.setParent('..')

    cmds.rowColumnLayout(nc=2, cw=[(1, 35), (2, 160)])
    cmds.text(label=jc.uniDecode("分配:"))
    cmds.text("assigned", label="", bgc=grey)
    cmds.setParent('..')

    cmds.rowColumnLayout(nc=2, cw=[(1, 35), (2, 160)])
    cmds.text(label=jc.uniDecode("開始:"))
    cmds.text("item_bsd", label="", al="center")
    cmds.setParent('..')

    cmds.rowColumnLayout(nc=2, cw=[(1, 35), (2, 160)])
    cmds.text(label=jc.uniDecode("結束:"))
    cmds.text("item_bed", label="", al="center", bgc=grey)
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.separator(style="in", h=10)
    cmds.setParent('..')
    
    # info panel 2 (item info)
    cmds.rowColumnLayout(nc=2, cw=[(1, 100), (2, 450)])

    cmds.text(label=jc.uniDecode("存檔案路徑"), ann=jc.uniDecode("專案路徑 + /scenes"))
    cmds.textField("final_path")
    cmds.text(label=jc.uniDecode("存檔案名"), ann=jc.uniDecode("檔案名 + 最後版本 + 1"))
    cmds.textField("basename")
    cmds.setParent('..')

    cmds.rowColumnLayout(nc=1, cal=(1, "center"), cw=(1, 550))
    cmds.button(label="Save", rs=True, c=tacticSave)
    cmds.setParent('..')

    cmds.separator(style="in", h=15)
    cmds.setParent('..')

    cmds.rowColumnLayout(nc=1, cw=[(1, 550)])
    cmds.text(label="Files")
    cmds.textScrollList("fileList", dcc=tacticLoad)
    cmds.button("loadFile", label="OPEN", c=tacticLoad)
    cmds.separator(style="in", h=15)
    cmds.button("publishFile", label="PUBLISH", c=publishMaster)

    cmds.setParent('..')


    cmds.separator(style="in", h=15)
    cmds.button(label="CLOSE", c=closeWindow)

    cmds.setParent('..')
    cmds.showWindow(windowID)


def start():
    try:
        expr = "@GET(sthpw/login.login)"
        temp = server.eval(expr)
        if len(temp) == 0:
            loginUI()
        else:
            mainUI()
    except:
        loginUI()

start()
