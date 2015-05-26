# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os
import jc_maya_aux_functions as jc
import subprocess
import sys
import shutil


sys.path.append("//Art-1405260002/d/assets/client")

#username = os.environ.get("USERNAME")
from tactic_client_lib import TacticServerStub
server = TacticServerStub()
server.set_server("192.168.201.10")
server.set_project("simpleslot")

def getRange():
    minTime = cmds.playbackOptions(q=1, minTime=1)
    maxTime = cmds.playbackOptions(q=1, maxTime=1)
    return minTime, maxTime


def setTimeRange():
    cmds.textField("mintime", edit=1, tx=int(getRange()[0]))
    cmds.textField("maxtime", edit=1, tx=int(getRange()[1]))


def exportType(arg=None):
    if cmds.radioButtonGrp("exportType", q=1, sl=1) == 1:
        exportType = 0
    else:
        exportType = 1
    cmds.rowColumnLayout("playbackrange", edit=1, en=exportType)
    setTimeRange()


def fileType():
    if cmds.radioButtonGrp("exportType", q=1, sl=1) == 1:
        filetype = "jpg"
    else:
        filetype = "avi"
    return filetype


def getDimensions():
    fileDimensions = cmds.radioButtonGrp("fileDimensions", q=1, sl=1)
    if fileDimensions == 1:
        dimensions = [1920, 1080]
    elif fileDimensions == 2:
        dimensions = [1280, 720]
    elif fileDimensions == 3:
        dimensions = [480, 360]
    elif fileDimensions == 4:
        dimensions = [720, 720]
    return dimensions


def pbList(base_scenename):
    scene_path = cmds.file(q=1, sn=1)
    scene_path = os.path.split(scene_path)
    pb_path = scene_path[0].replace("/scenes", "") + "/images/"
    savedFiles = []
    if os.path.exists(pb_path) is True:
        savedFiles = os.listdir(pb_path)
        currentSceneReviewList = [x for x in savedFiles if base_scenename[:-5] in x]
    cmds.textScrollList("playblastList", e=1, removeAll=1)
    cmds.textScrollList("playblastList", e=1, append=currentSceneReviewList)


def screenCap(arg=None):
    pbname = jc.getNextFileName(1)
    pb_path = pbname[0]
    pb_filename = pbname[2]
    base_scenename = pbname[1]
    currentFrame = cmds.currentTime(query=True)
    st = cmds.textField("mintime", q=1, tx=1)
    et = cmds.textField("maxtime", q=1, tx=1)

    if fileType() == "jpg":
        fileFormat = "image"
        compression = "jpg"
        cmds.playblast(fr=currentFrame, p=100, widthHeight=getDimensions(), format=fileFormat, viewer=0, cf=(pbname[2] + ".jpg"), compression=compression)

    else:
        fileFormat = "avi"
        compression = "none"
        avi_filename = cmds.playblast(st=st, et=et, p=100, widthHeight=getDimensions(), format=fileFormat, viewer=0, f=("c:/sthpw/" + pbname[2] + ".avi"))

        mp4_filename = (pb_path + pb_filename + ".mp4")
        convertCMD = "//Art-1405260002/d/assets/scripts/ffmpeg/bin/ffmpeg -i \"%s\" -c:v libx264 -crf 19 -preset slow -c:a aac -strict experimental -b:a 192k -ac 2 \"%s\"" % (avi_filename, mp4_filename)

        os.system(convertCMD)
        os.remove(avi_filename)
    pbList(base_scenename)

def previewImages(arg=None):
    temp = jc.getNextFileName(1)
    image_folder = temp[0]
    filename = cmds.textScrollList("playblastList", q=1, si=1)[0]
    path = image_folder + filename
    if filename.endswith(".mp4") is False:
        cmds.renderWindowEditor("renderView", e=1, li=path)
    else:
        pass



def openFile(arg=None):
    temp = jc.getNextFileName(1)
    image_folder = temp[0]
    filename = cmds.textScrollList("playblastList", q=1, si=1)[0]
    path = image_folder + filename
    open_cmd = "C:\Program Files (x86)\Pdplayer\pdplayer.exe " + "\"" + path + "\""
    subprocess.call(open_cmd)


def tacticPublish(arg=None):
    temp = jc.getNextFileName(1)
    path = temp[0]
    project_name = temp[3][0]
    item_name = temp[3][1]
    process = temp[3][2]   
    filename = (cmds.textScrollList("playblastList", q=1, si=1))[0]
    tactic_base_path = "//Art-1405260002/d/assets/simpleslot/"

    src_filename = path + filename
    dst_filename = tactic_base_path + project_name + "/review/" + filename
    # dst_thumbname = tactic_base_path + project_name + "/review/" + filename.replace("mp4","jpg")
    # thumbCMD = "//Art-1405260002/d/assets/scripts/ffmpeg/bin/ffmpeg -i \"%s\" -vf \"thumbnail\" -frames:v 5 -vsync vfr \"%s\"" % (src_filename, dst_thumbname)    
    # os.system(thumbCMD)

    if os.path.isdir(tactic_base_path + project_name + "/review/") is False:
        os.mkdir(tactic_base_path + project_name + "/review/")

    shutil.copy2((src_filename), (dst_filename))
    final_filename = "/mnt/hgfs/assets/simpleslot/" + project_name + "/review/" + filename

    expr = "@SOBJECT(sthpw/snapshot['description','" + final_filename + "'])"
    check = server.eval(expr)
    if len(check) > 0:
        print "exists"
        pass
    else:
        expr = "@SOBJECT(simpleslot/game['name','" + project_name + "'].simpleslot/assets['name','" + item_name + "'].sthpw/task['process','" + process + "'])"
        task = server.eval(expr)
        sk = task[0].get("__search_key__")
        server.simple_checkin(sk, process, final_filename, description=final_filename, mode="inplace")
        print "uploaded to tactic"



def playblast2tacticMain():
    if cmds.window("playblast2tactic", exists=True):
        cmds.deleteUI("playblast2tactic")
    windowID = cmds.window("playblast2tactic", sizeable=False)

    getTime = getRange()

    rowWidth1 = 100
    rowWidth2 = 200
    rowSpacing = 3

    cmds.rowColumnLayout(nr=5, rs=[(1, rowSpacing), (2, rowSpacing), (3, rowSpacing), (4, rowSpacing), (5, 20)])  # top panel is project, bottom panel are tabs for shots and assets

    cmds.rowColumnLayout(nc=2, cw=[(1, rowWidth1), (2, rowWidth2)], cal=[(1, "center"), (2, "center")])
    cmds.text(jc.uniDecode("出圖類型"))
    cmds.radioButtonGrp("exportType", sl=1, cw=[(1, 80), (2, 80)], labelArray2=[jc.uniDecode('單張'), jc.uniDecode('影片')], numberOfRadioButtons=2, cc=exportType)
    cmds.setParent('..')

    cmds.rowColumnLayout(nc=2, cw=[(1, rowWidth1), (2, rowWidth2)], cal=[(1, "center"), (2, "center")])
    cmds.text(jc.uniDecode("出圖大小"))
    cmds.radioButtonGrp("fileDimensions", sl=2, cw=[(1, 45), (2, 45), (3, 45), (4, 45)], labelArray4=['1080P', '720P', '480P', '720square'], numberOfRadioButtons=4, cc=exportType)
    cmds.setParent('..')

    cmds.rowColumnLayout(nc=2, cw=[(1, rowWidth1), (2, rowWidth2)], cal=[(1, "center"), (2, "center")])
    cmds.text(jc.uniDecode("時間範圍"))

    cmds.rowColumnLayout("playbackrange", nc=4, cs=[(1, 0), (2, 5), (3, 20), (4, 5)], cw=[(1, 30), (2, 30), (3, 30), (4, 30)])
    cmds.text(jc.uniDecode("開始:"))
    cmds.textField("mintime", tx=int(getTime[0]))
    cmds.text(jc.uniDecode("結束:"))
    cmds.textField("maxtime", tx=int(getTime[1]))
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.rowColumnLayout(nc=1, cal=[1, "center"], cw=(1, 300))
    cmds.button(l="playblast", c=screenCap)
    cmds.separator(style="in", h=15)
    cmds.setParent('..')

    cmds.rowColumnLayout(nc=1, cal=[1, "center"], cw=(1, 300))
    cmds.text(jc.uniDecode("圖/影片"))
    cmds.textScrollList("playblastList", append="", sc=previewImages)

    cmds.rowColumnLayout(nc=2, cal=[1, "center"], cw=[(1, 150), (2, 150)])
    cmds.button(l=jc.uniDecode("開啟"), c=openFile)

    cmds.button(l=jc.uniDecode("上傳 TACTIC"), c=tacticPublish)
    cmds.setParent('..')

    cmds.showWindow(windowID)
    exportType()
    # pbname = getName()
    pbname = jc.getNextFileName(1)
    base_scenename = pbname[1]
    pbList(base_scenename)


#playblast2tactic()
# project_name, project_type, item_type, item_name, process, maya_scenes, filename
# project_abbr, item_type_abbr, item_name, process_abbr, version, author.mb
