# -*- coding: utf-8 -*-
global sys, socket, errno, os, six, datetime, parser, TacticServerStub, cmds

import sys
# sys.path.append("c:/client")
sys.path.append("//Art-1405260002/d/assets/client")
# sys.path.append("c:/Python27/python-dateutil-2.3")
# sys.path.append("c:/Python27/six-1.8.0")
import socket
import errno
import os
# import six
# from datetime import datetime
# from dateutil import parser

import maya.cmds as cmds

username = os.environ.get("USERNAME")
ticket_file = "c:/sthpw/etc/" + username + ".tacticrc"
base = os.path.split(ticket_file)

if os.path.exists(base[0]) == False:
    os.makedirs(base[0])
if os.path.exists(ticket_file) == False:
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
    cmds.button(label=str("登入").decode('utf-8'), c=login)

    cmds.showWindow(windowID)


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
        cmds.button(label="登入/密碼不對", c=loginUI)
        cmds.showWindow(windowID)
        return False


def abbrName(name):
    def hasNumbers(inputString):
        return any(char.isdigit() for char in inputString)

    conjunction = ['and', 'the', 'or', 'of']
    name = name.lower()
    name = name.replace(" ", "")
    words = name.split("_")
    final = ""
    if len(words) < 2:
        if len(words[0]) < 5:
            final = words[0]
        else:
            final = words[0][:3]
    else:
        for word in words:
            if word[0] == "v" and hasNumbers(word[1]) and hasNumbers(word[2]):
                char = "_" + word
            elif word == "cf":
                char = "_cf"
            else:
                if words[1][0] == "v":
                    char = word[:3]
                elif len(word) < 3 and (word not in conjunction):
                    char = word
                else:
                    char = word[0]
            final = final+char
    return final


def abbrItemType(name):
    name = name.lower()
    name = name.replace(" ", "")
    words = name.split("_")
    final = ""
    for word in words:
        char = word[0]
        final = final+char
    return final


def maxVersion(final_path, filename):
    savedFiles = []
    versions = []
    if os.path.exists(final_path) is True:
        savedFiles = os.listdir(final_path)
        if len(savedFiles) == 0:
            maxversion = "v01"
            pass
        else:
            for savedFile in savedFiles:
                if os.path.isdir(final_path + savedFile) is True:
                    pass
                else:
                    savedFile = savedFile.replace(filename, "").replace(".mb", "")
                    savedFile = savedFile.split("_")
                    savedFile.pop(0)
                    version = savedFile.pop(0)
                    '''
                    if len(savedFile) > 1:
                        user = savedFile[0] + "_" + savedFile[1]
                    else:
                        user = savedFile[0]
                    '''
                    version = version.replace("v", "")
                    versions.append(int(version))
            maxversion = "v" + str("%02d" % (max(versions) + 1))
    else:
        maxversion = "v01"
    return maxversion


def finalPath():
    base_path = "//art-render/art_3d_project/"
    game = cmds.textScrollList("projectMenu", q=True, si=True)
    name = server.login
    try:
        assets = cmds.textScrollList("assetList", q=True, si=True)
    except:
        assets = ""
    try:
        shot = cmds.textScrollList("shotList", q=True, si=True)
    except:
        shot = ""
    try:
        asset_process = cmds.textScrollList("assetProcessList", q=True, si=True)
    except:
        asset_process = ""
    try:
        shot_process = cmds.textScrollList("shotProcessList", q=True, si=True)
    except:
        shot_process = ""

    project_type = cmds.text("project_type", q=True, label=True)

    try:
        selectedTab = cmds.tabLayout("items", q=True, sti=True)
        if selectedTab == 1:
            if project_type == "cf" or project_type == "sports":
                expr = "@SOBJECT(simpleslot/game['name','" + game[0] + "'].simpleslot/assets['name','" + assets[0] + "'].simpleslot/asset_type)"
                asset_type = server.eval(expr)
                item_type = asset_type[0].get('name')
                final_path = base_path + game[0] + "/assets/" + item_type + "/" + assets[0] + "/" + asset_process[0] + "/scenes/"
                filename = abbrName(game[0]) + "_" + abbrItemType(item_type) + "_" + assets[0] + "_" + abbrName(asset_process[0])

                filename = abbrName(game[0]) + "_" + abbrItemType(item_type) + "_" + assets[0] + "_" + abbrName(asset_process[0]) + "_" + maxVersion(final_path, filename) + "_" + name + ".mb"

            elif project_type == "casino":
                expr = "@SOBJECT(simpleslot/game['name','" + game[0] + "'].simpleslot/3d['name','" + assets[0] + "'].simpleslot/3d_type)"
                asset_type = server.eval(expr)
                item_type = asset_type[0].get('name')
                final_path = base_path + game[0] + "/casino/" + item_type + "/" + assets[0] + "/" + asset_process[0] + "/scenes/"
                filename = abbrName(game[0]) + "_" + abbrItemType(item_type) + "_" + assets[0] + "_" + abbrName(asset_process[0])

                filename = abbrName(game[0]) + "_" + abbrItemType(item_type) + "_" + assets[0] + "_" + abbrName(asset_process[0]) + "_" + maxVersion(final_path, filename) + "_" + name + ".mb"

        elif selectedTab == 2:
            final_path = base_path + game[0] + "/shot/" + shot[0] + "/" + shot_process[0] + "/scenes/"
            filename = abbrName(game[0]) + "_" + shot[0] + "_" + abbrName(shot_process[0])

            filename = abbrName(game[0]) + "_" + shot[0] + "_" + abbrName(shot_process[0]) + "_" + maxVersion(final_path, filename) + "_" + name + ".mb"

        final_path = final_path.replace(" ", "")

        # project_path = final_path.replace("scenes/", "")
        # cmds.textField("project_path", edit=True, tx=project_path, enterCommand=('cmds.setFocus(\"' + final_path + '\")'))
        cmds.textField("final_path", edit=True, tx=final_path, enterCommand=('cmds.setFocus(\"' + final_path + '\")'))
        cmds.textField("basename", edit=True, tx=filename, enterCommand=('cmds.setFocus(\"' + final_path + '\")'))
        getFiles()
    except:
        pass


def getFiles():
    savedFileList = []
    final_path = cmds.textField("final_path", q=True, tx=1)
    if os.path.exists(final_path) is True:
        savedFiles = os.listdir(final_path)
        if len(savedFiles) == 0:
            pass
        for savedFile in savedFiles:
            if os.path.isdir(final_path + savedFile) is True:
                pass
            else:
                savedFileList.append(savedFile)
    cmds.textScrollList("fileList", edit=1, removeAll=1)
    cmds.textScrollList("fileList", edit=1, append=savedFileList)


def updateList(name, stype, production_type):
    if stype == "3d":
        processes = ["model", "texture", "rigging", "animation", "lighting", "layout", "final"]
    elif stype == "assets":
        processes = ["model", "texture", "rigging"]
    elif stype == "shot":
        processes = ["animation", "lighting", "layout", "final"]

    expr = "@SOBJECT(simpleslot/game['name','" + name + "'].simpleslot/" + stype + ")"
    items = server.eval(expr)
    items = [y['name'] for y in items]

    items = sorted(items)
    cmds.textScrollList(production_type + "ProcessList", edit=True, removeAll=True)

    cmds.textScrollList(production_type + "List", edit=True, append=items)
    cmds.textScrollList(production_type + "ProcessList", edit=True, append=processes)

    cmds.textScrollList(production_type + "List", edit=True, sii=1)
    cmds.textScrollList(production_type + "ProcessList", edit=True, sii=1)


def getItems():
    game = cmds.textScrollList("projectMenu", q=True, si=True)
    game = game[0]
    expr = "@SOBJECT(simpleslot/plan['id','8'])"
    temp = server.eval(expr)

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

    temp = zip(names, games_type, bsd, bed, names_chn)
    temp.pop(0)

    def getNameKey(item):
        return item[0]
    temp = sorted(temp, key=getNameKey, reverse=False)

    cmds.textScrollList("assetList", edit=True, removeAll=True)

    cmds.textScrollList("shotList", edit=True, removeAll=True)

    for x in range(len(temp)):
        if temp[x][0] == game:  # if selected is in inprogress list
            if temp[x][1] == "casino":  # if selected is casino or shot or assets
                updateList(temp[x][0], "3d", "asset")

            elif temp[x][1] == "sports" or temp[x][1] == "cf":
                updateList(temp[x][0], "assets", "asset")
                updateList(temp[x][0], "shot", "shot")

            cmds.text("project_type", edit=True, label=temp[x][1])
            cmds.text("bsd", edit=True, label=temp[x][2])
            cmds.text("bed", edit=True, label=temp[x][3])
            cmds.text("project_name_chn", edit=True, label=temp[x][4])
    finalPath()


def getNames():
    expr = "@SOBJECT(simpleslot/plan['id','8'])"
    temp = server.eval(expr)
    names = temp[0].get('name')
    names = names.split(" ")  # list is a space separated string
    names.pop(0)
    names = sorted(names)
    return names


def workspaceFileRule(project_path):
    cmds.workspace(project_path, o=1)
    cmds.workspace(fileRule=['scene', 'scenes'])
    cmds.workspace(fileRule=['3dPaintTextures', 'sourceimages/3dPaintTextures'])
    cmds.workspace(fileRule=['eps', 'data'])
    cmds.workspace(fileRule=['OBJexport', 'data'])
    cmds.workspace(fileRule=['mel', 'scripts'])
    cmds.workspace(fileRule=['particles', 'cache/particles'])
    cmds.workspace(fileRule=['STEP_DC', 'data'])
    cmds.workspace(fileRule=['CATIAV5_DC', 'data'])
    cmds.workspace(fileRule=['sound', 'sound'])
    cmds.workspace(fileRule=['furFiles', 'renderData/fur/furFiles'])
    cmds.workspace(fileRule=['depth', 'renderData/depth'])
    cmds.workspace(fileRule=['CATIAV4_DC', 'data'])
    cmds.workspace(fileRule=['autoSave', 'autosave'])
    cmds.workspace(fileRule=['diskCache', 'data'])
    cmds.workspace(fileRule=['fileCache', 'cache/nCache'])
    cmds.workspace(fileRule=['IPT_DC', 'data'])
    cmds.workspace(fileRule=['SW_DC', 'data'])
    cmds.workspace(fileRule=['DAE_FBX export', 'data'])
    cmds.workspace(fileRule=['Autodesk Packet File', 'data'])
    cmds.workspace(fileRule=['DAE_FBX', 'data'])
    cmds.workspace(fileRule=['DXF_DCE', 'data'])
    cmds.workspace(fileRule=['mayaAscii', 'scenes'])
    cmds.workspace(fileRule=['iprImages', 'renderData/iprImages'])
    cmds.workspace(fileRule=['move', 'data'])
    cmds.workspace(fileRule=['mayaBinary', 'scenes'])
    cmds.workspace(fileRule=['fluidCache', 'cache/nCache/fluid'])
    cmds.workspace(fileRule=['clips', 'clips'])
    cmds.workspace(fileRule=['templates', 'assets'])
    cmds.workspace(fileRule=['DWG_DC', 'data'])
    cmds.workspace(fileRule=['offlineEdit', 'scenes/edits'])
    cmds.workspace(fileRule=['translatorData', 'data'])
    cmds.workspace(fileRule=['DXF_DC', 'data'])
    cmds.workspace(fileRule=['renderData', 'renderData'])
    cmds.workspace(fileRule=['SPF_DCE', 'data'])
    cmds.workspace(fileRule=['ZPR_DCE', 'data'])
    cmds.workspace(fileRule=['furShadowMap', 'renderData/fur/furShadowMap'])
    cmds.workspace(fileRule=['audio', 'sound'])
    cmds.workspace(fileRule=['IV_DC', 'data'])
    cmds.workspace(fileRule=['scripts', 'scripts'])
    cmds.workspace(fileRule=['STL_DCE', 'data'])
    cmds.workspace(fileRule=['furAttrMap', 'renderData/fur/furAttrMap'])
    cmds.workspace(fileRule=['FBX export', 'data'])
    cmds.workspace(fileRule=['JT_DC', 'data'])
    cmds.workspace(fileRule=['sourceImages', 'sourceimages'])
    cmds.workspace(fileRule=['DWG_DCE', 'data'])
    cmds.workspace(fileRule=['FBX', 'data'])
    cmds.workspace(fileRule=['movie', 'movies'])
    cmds.workspace(fileRule=['Alembic', 'data'])
    cmds.workspace(fileRule=['furImages', 'renderData/fur/furImages'])
    cmds.workspace(fileRule=['IGES_DC', 'data'])
    cmds.workspace(fileRule=['illustrator', 'data'])
    cmds.workspace(fileRule=['furEqualMap', 'renderData/fur/furEqualMap'])
    cmds.workspace(fileRule=['UG_DC', 'data'])
    cmds.workspace(fileRule=['images', 'images'])
    cmds.workspace(fileRule=['SPF_DC', 'data'])
    cmds.workspace(fileRule=['PTC_DC', 'data'])
    cmds.workspace(fileRule=['OBJ', 'data'])
    cmds.workspace(fileRule=['CSB_DC', 'data'])
    cmds.workspace(fileRule=['STL_DC', 'data'])
    cmds.workspace(fileRule=['IGES_DCE', 'data'])
    cmds.workspace(fileRule=['shaders', 'renderData/shaders'])
    cmds.workspace(fileRule=['UG_DCE', 'data'])


def tacticSave(arg=None):
    path = cmds.textField("final_path", query=True, tx=True)
    filename = cmds.textField("basename", query=True, tx=True)
    if not os.path.exists(path):
        os.makedirs(path)
    final = path + filename
    project_path = path.replace("scenes/", "")

    workspaceFileRule(project_path)

    cmds.file(rename=final)
    cmds.file(save=True, type='mayaBinary')
    print "saved"

    game = cmds.textScrollList("projectMenu", q=True, si=True)
    game = game[0]
    project_type = cmds.text("project_type", q=True, label=True)
    if project_type == "casino":
        project_type = "3d"
        process = cmds.textScrollList("assetProcessList", q=True, si=True)
        process = process[0]
        item = cmds.textScrollList("assetList", q=True, si=True)

    elif project_type == "sports" or project_type == "cf":
        selectedTab = cmds.tabLayout("items", q=True, sti=True)
        if selectedTab == 1:
            project_type = "assets"
            process = cmds.textScrollList("assetProcessList", q=True, si=True)
            process = process[0]
            item = cmds.textScrollList("assetList", q=True, si=True)
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
        cmds.button(label="TACTIC 上沒有規劃這個物件或流程", c='cmds.deleteUI("error")')
        cmds.showWindow(windowID)
    else:
        sk = task[0].get('__search_key__')
        # snapshot = server.create_snapshot(sk, (path + filename), "maya binary", "maya file", "None", 0, 0)
        # snapshot_code = snapshot.get('code')
        # server.add_file(snapshot_code, (path + filename), create_icon=True, mode='inplace')
    finalPath()


def tacticLoad(arg=None):
    filename = cmds.textScrollList("fileList", q=True, si=True)
    path = cmds.textField("final_path", q=1, tx=1)
    project_path = path.replace("scenes/", "")
    cmds.file((path + filename[0]), open=True)
    workspaceFileRule(project_path)


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


def uniDecode(chinese):
    return str(chinese).decode('utf-8')


def mainUI():
    if cmds.window("fileNaming", exists=True):
        cmds.deleteUI("fileNaming")
    names = []
    names = getNames()
    windowID = cmds.window("fileNaming", sizeable=False)
    # parent window
    cmds.rowColumnLayout(nr=3, rs=[(1, 10), (2, 10), (3, 10)])  # top panel is project, bottom panel are tabs for shots and assets

    cmds.rowColumnLayout(nc=4)

    # panel 1
    cmds.rowColumnLayout(nc=2, rs=[(1, 30), (2, 10), (3, 10)], cs=[1, 10], cw=[(1, 50), (2, 100)])
    cmds.text(label=uniDecode("專案中"))
    cmds.text("project_name_chn", label="XXXXXXXX")
    cmds.text(label=uniDecode("案型"))
    cmds.text("project_type", label="casino")
    cmds.text(label=uniDecode("3D開始"))
    cmds.text("bsd", label="XXXXXXXX")
    cmds.text(label=uniDecode("3D結束"))
    cmds.text("bed", label="XXXXXXXX")
    cmds.setParent('..')

    # panel 2
    cmds.tabLayout("Projects")
    proj_child1 = cmds.rowColumnLayout(nc=1, cw=[(1, 200)])
    cmds.text(label="Projects")
    cmds.textScrollList("projectMenu", append=names, sc=getItems)
    cmds.setParent('..')
    cmds.tabLayout("Projects", edit=True, tabLabel=((proj_child1, 'Projects')))
    cmds.setParent('..')

    # panel 3
    cmds.tabLayout("items")
    child1 = cmds.rowColumnLayout(nc=2, cw=[(1, 250), (2, 100)])
    cmds.text(label="Assets")
    cmds.text(label="Process")
    cmds.textScrollList("assetList", sc=finalPath)
    cmds.textScrollList("assetProcessList", append="", sc=finalPath)
    cmds.setParent('..')  # parent row
    child2 = cmds.rowColumnLayout(nc=2, cw=[(1, 250), (2, 80)])
    cmds.text(label="Shots")
    cmds.text(label="Process")
    cmds.textScrollList("shotList", sc=finalPath)
    cmds.textScrollList("shotProcessList", append="", sc=finalPath)
    cmds.setParent('..')
    cmds.tabLayout("items", edit=True, tabLabel=((child1, 'Assets'), (child2, 'Shots')))
    cmds.setParent('..')

    # panel 4
    cmds.tabLayout("load")
    proj_child2 = cmds.rowColumnLayout(nc=1, cw=[(1, 400)])
    cmds.text(label="Files")
    cmds.textScrollList("fileList")
    cmds.button("loadFile", label="OPEN", c=tacticLoad)
    cmds.setParent('..')
    cmds.tabLayout("load", edit=True, tabLabel=((proj_child2, 'Files')))
    cmds.setParent('..')

    cmds.setParent('..')

    cmds.rowColumnLayout(nc=2, cw=[(1, 100), (2, 625)])
    # cmds.text(label="Project Path")
    # cmds.textField("project_path")
    cmds.text(label=uniDecode("檔案路徑"), ann="專案路徑 + /scenes")
    cmds.textField("final_path")
    cmds.text(label=uniDecode("檔案名"), ann=uniDecode("檔案名 + 最後版本 + 1"))
    cmds.textField("basename")
    cmds.setParent('..')

    cmds.rowColumnLayout(nc=1, cw=[(1, 725)])
    cmds.button(label="Save", rs=True, c=tacticSave)
    cmds.showWindow(windowID)


start()
