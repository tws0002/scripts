# pyside-uic -o //Art-1405260002/d/assets/scripts/maya_scripts/lib/qt_main_ui.py tactic_3d.ui
import sys
sys.path.append("//Art-1405260002/d/assets/client")
sys.path.append("//Art-1405260002/d/assets/scripts/maya_scripts/lib")
sys.path.append("//Art-1405260002/d/assets/scripts/maya_scripts")
sys.path.append("//Art-1405260002/d/assets/scripts/install")
from PySide import QtCore, QtGui
import time
import qt_muster_ui as qt_muster_ui
import jc_maya_aux_functions as jc
import os
import subprocess
import socket

reload(qt_muster_ui)
reload(jc)

class musterWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(musterWindow, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Tool)
        self.ui = qt_muster_ui.Ui_MusterConnector()
        self.ui.setupUi(self)
        self.ui.server_panel.setFixedSize(396,90)
        #self.ui.submit_panel.setFixedSize(396,65)
        self.ui.nuke_write_table.setColumnWidth(1,335)
        self.ui.nuke_write_table.setColumnWidth(2,20)

minus = QtGui.QIcon()
minus.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/maya_scripts/icons/minus-square-o_c8c8c8_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
plus = QtGui.QIcon()
plus.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/maya_scripts/icons/plus-square-o_c8c8c8_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

nukeopenicon = QtGui.QIcon()
nukeopenicon.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/nuke_scripts/icons/Write.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
nukecloseicon = QtGui.QIcon()
nukecloseicon.name
nukecloseicon.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/nuke_scripts/icons/Write1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

nukecheckicon = QtGui.QIcon()
nukecheckicon.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/nuke_scripts/icons/check_c8c8c8_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#nukecheckicon.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/nuke_scripts/icons/times_c8c8c8_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
nukecrossicon =  QtGui.QIcon()
nukecrossicon.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/nuke_scripts/icons/times_c8c8c8_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

foldericon = QtGui.QIcon()
foldericon.addPixmap(QtGui.QPixmap("//Art-1405260002/d/assets/scripts/maya_scripts/icons/folder-o_c8c8c8_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)


server_panel_status = "show"
frame_range_panel_status = "show"
submit_panel_status = "show"
nuke_panel_status = "show"

app = QtGui.QApplication.instance()
appName = app.objectName()


if not app:
    app = QtGui.QApplication([])
if appName == "maya":
    import maya.mel as mel
    import maya.cmds as cmds
elif "Nuke" in appName:
    import nuke

def getMusterIP():
    import socket
    return socket.gethostbyname('art-render')

def hideServerPanel():
    global server_panel_status
    if server_panel_status == "show":
        widget.ui.server_panel.setVisible(0)
        widget.ui.server_panel_button.setIcon(plus)
        server_panel_status = "hidden"

    elif server_panel_status == "hidden":
        widget.ui.server_panel.setVisible(1)
        widget.ui.server_panel_button.setIcon(minus)
        server_panel_status = "show"


def hideFrameRangePanel():
    global frame_range_panel_status
    if frame_range_panel_status == "show":
        widget.ui.frame_range_panel.setVisible(0)
        widget.ui.frame_range_panel_button.setIcon(plus)
        frame_range_panel_status = "hidden"

    elif frame_range_panel_status == "hidden":
        widget.ui.frame_range_panel.setVisible(1)
        widget.ui.frame_range_panel_button.setIcon(minus)
        frame_range_panel_status = "show"


def hideNukePanel():
    global nuke_panel_status
    if nuke_panel_status == "show":
        widget.ui.nuke_panel.setVisible(0)
        widget.ui.nuke_panel_button.setIcon(nukecloseicon)
        nuke_panel_status = "hidden"

    elif nuke_panel_status == "hidden":
        widget.ui.nuke_panel.setVisible(1)
        widget.ui.nuke_panel_button.setIcon(nukeopenicon)
        nuke_panel_status = "show"
        nukeWriteNodes()


def setMuster():
    global scene_name, proj_path, name
    muster_ip = getMusterIP() 
    name = jc.getNextFileName(1)
    path = name[0]
    base_scenename = name[1]
    full_filename = name[2]
    author = name[3][3]

    file_name_prefix = full_filename
    image_path = path + full_filename + "/"
    proj_path = path.replace("/images/", "")

    widget.ui.job_name.setText(full_filename)
    widget.ui.image_folder.setText(path + full_filename)

    scene_name = base_scenename + "_" + author + ".mb"

    if appName == 'maya':
        cmds.setAttr('defaultRenderGlobals.imageFilePrefix', file_name_prefix, type="string")
        start_frame = cmds.getAttr("defaultRenderGlobals.startFrame")
        end_frame = cmds.getAttr("defaultRenderGlobals.endFrame")
        by_frame = cmds.getAttr("defaultRenderGlobals.byFrameStep")     
        frame_padding = cmds.getAttr("defaultRenderGlobals.extensionPadding")     
        widget.ui.start_frame.setText(str(start_frame))
        widget.ui.end_frame.setText(str(end_frame))
        widget.ui.by_frame.setText(str(by_frame))
        widget.ui.frame_padding.setText(str(frame_padding))
        widget.ui.muster_ip.setText(muster_ip)
    elif appName == "3dsmax":
        pass
    elif "Nuke" in appName:
        scene_name = base_scenename + "_" + author + ".nk"
        widget.ui.start_frame.setText(str(1))
        widget.ui.end_frame.setText(str(1))
        widget.ui.by_frame.setText(str(1))
        widget.ui.frame_padding.setText(str(4))        
    else:
        scene_name = ""

def submitRender(arg=None):
    # Result: -b -s 192.168.201.22 -port 9681 -u "admin" -p "" -sf 1 -ef 10 -bf 1 -attr MAYADIGITS 1 0 -se 1 -st 1 -e 2 -pk 4 -pr 1 -max 0 -v 3
    # -n "aoml_cf_c_character_rig_rig_v01_julio"
    # -f "\\art-render\art_3d_project\adventure_of_mystical_land_cf\assets\character\character_rig\rigging\sourceimages\3dPaintTextures\aoml_cf_c_character_rig_rig_v01_julio.mb"
    # -proj "\\art-render\art_3d_project\adventure_of_mystical_land_cf\assets\character\character_rig\rigging"
    muster_server = widget.ui.muster_ip.text()
    muster_server_port = widget.ui.muster_port.text()
    start_frame = widget.ui.start_frame.text()
    end_frame = widget.ui.end_frame.text()
    by_frame = widget.ui.by_frame.text()
    frame_padding = widget.ui.frame_padding.text()
    priority = widget.ui.priority.text()
    packet_size = widget.ui.packet_size.text()
    #render_pool = widget.ui.render_pool.currentText()
    job_name = widget.ui.job_name.text()
    image_folder = widget.ui.image_folder.text()
    batch_render_filename = proj_path + "/scenes/" + scene_name
    render_pool = getSelectedPools()
    folder_id = str(getParent())
    if appName == 'maya':
        renderer = cmds.getAttr("defaultRenderGlobals.currentRenderer")
        if renderer == "mayaSoftware":
            rendererID = "1"
        if renderer == "mayaHardware":
            rendererID = "3"
        if renderer == "mentalRay":
            rendererID = "2"
        if renderer == "arnold":
            rendererID = "46"
        else:
            rendererID = "2"
        mayaDefaultRenderers = ["mayaSoftware", "mayaHardware", "mayaHardware2"]

        if renderer == "arnold":
            imageFormat = cmds.getAttr("defaultArnoldDriver.aiTranslator")
            #cmds.setAttr("defaultArnoldDriver.aiTranslator", "exr", type="string")
            #cmds.setAttr("defaultArnoldDriver.exrCompression", 3)
            #imageFormat = "exr"
            # imageFormat = cmds.optionMenuGrp("imageMenuMayaSW", q=1, v=1)
        else:
            imageFormatId = cmds.getAttr("defaultRenderGlobals.imageFormat")
            if imageFormatId == 3:
                imageFormat = "tif" # tif
            elif imageFormatId == 4:
                imageFormat = "tif" # tif16
            elif imageFormatId == 51:
                imageFormat = "exr"
            else:
                if renderer in mayaDefaultRenderers:  # set to tif16 if not MR
                    #mel.eval("setAttr \"defaultRenderGlobals.imageFormat\" 3;")
                    cmds.evalDeferred('cmds.setAttr("defaultRenderGlobals.imageFormat", 3)')
                    cmds.evalDeferred('cmds.setAttr("defaultRenderGlobals.imfPluginKey", "tif", type="string")')
                    imageFormat = "tif"
                else:  # set to exr if MR
                    #mel.eval("setAttr \"defaultRenderGlobals.imageFormat\" 51;")  # python can't seem to change imageformat correctly
                    cmds.evalDeferred('cmds.setAttr("defaultRenderGlobals.imageFormat", 51)')
                    cmds.evalDeferred('cmds.setAttr("defaultRenderGlobals.imfPluginKey", "exr", type="string")')
                    cmds.setAttr("mentalrayGlobals.imageCompression", 4) # set to zip comrpession(scanline 16 pack)
                    imageFormat = "exr"

        cmds.setAttr("defaultRenderGlobals.animation", True)
        cmds.setAttr("defaultRenderGlobals.putFrameBeforeExt", True)

        rls = cmds.ls(type="renderLayer")
        renderLayers = []
        for rl in rls:
            if cmds.getAttr(rl + ".renderable") == 1:
                if rl == "defaultRenderLayer":
                    renderLayers.append("masterLayer")
                elif ":" in rl:
                    pass
                else:
                    renderLayers.append(rl)

        cmds.file(save=True, type='mayaBinary')

        width = str(cmds.getAttr("defaultResolution.width"))
        height = str(cmds.getAttr("defaultResolution.height"))
        size = width + "x" + height
        ar = width + ":" + height

        if os.path.isdir(image_folder + "/") is False:
            os.mkdir(image_folder + "/")

        master_bat_file = open(image_folder + "/" + "convert.bat", "w")

        for renderLayer in renderLayers:
            if os.path.isdir(image_folder + "/" + renderLayer + "/") is False:
                os.mkdir(image_folder + "/" + renderLayer + "/")
            sequence_filename = image_folder + "/" + renderLayer + "/" + job_name + ".%%04d" + "." + imageFormat
            delete_filename = image_folder + "/" + renderLayer + "/" + job_name + ".????" + "." + imageFormat
            mp4_filename = image_folder + "/" + job_name + "_" + renderLayer + ".mp4"
            #bat_file = open(image_folder + "/" + renderLayer + "/convert.bat", "w")

            #  FFMpeg does not work with exr, so we need to convert to tif first with imageMagick
            if imageFormat == "exr":
                imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe -colorspace RGB \"%s\" -colorspace sRGB \"%s\""  % (sequence_filename + "[" + start_frame + "-" + end_frame + "]", sequence_filename.replace(".exr",".tif") + "[" + start_frame + "-" + end_frame + "]")
                master_bat_file.writelines(imageMagickCMD + "\n")

            convertCMD = "//Art-1405260002/d/assets/scripts/ffmpeg/bin/ffmpeg -i \"%s\" -c:v libx264 -crf 19 -preset slow -c:a aac -strict experimental -b:a 192k -ac 2 -s %s -aspect %s \"%s\"" % (sequence_filename.replace(".exr",".tif"), size, ar, mp4_filename)
            master_bat_file.writelines(convertCMD + "\n")

            '''This is kind of weird. this is mainly for arnold 
            deleteTIFCMD = "del " + delete_filename.replace(".exr",".tif")
            master_bat_file.writelines(deleteTIFCMD.replace("/", "\\") + "\n")
            '''

            # bat_file.close()
            #master_bat_file.writelines(image_folder + "/" + renderLayer + "/convert.bat" + "\n")

        master_bat_file.close()

        post_job_action = image_folder + "\convert.bat"
        post_job_action = post_job_action.replace("/", "\\")
        # post_job_action = ""

        cmdline = "\"C:\Program Files\Virtual Vertex\Muster 7\Mrtool.exe\" -b -parent " + folder_id + " -s " + muster_server + " -port " + muster_server_port + " -u \"admin\" -p \"\" -sf " + start_frame + " -ef " + end_frame + " -bf " + by_frame + " -attr MAYADIGITS " + frame_padding + " 0 -attr ARNOLDMODE 0 0 -attr ARNOLDLICENSE 1 1 -pool \"" + render_pool + "\" -se 1 -st 1 -e " + rendererID + " -pk " + packet_size + " -pr " + priority + " -max 0 -v 3 -eja \"" + post_job_action + "\" -n \"" + job_name + "\" -dest \"" + image_folder + "\" -f \"" + batch_render_filename + "\" -proj \"" + proj_path + "\""
        subprocess.call(cmdline.replace("/", "\\"))

    if "Nuke" in appName:
        import nuke
        rendererID = "49"
        nuke.scriptSave()
        if os.path.isdir(image_folder + "/") is False:
            os.mkdir(image_folder + "/")
        cmdline = "\"C:\Program Files\Virtual Vertex\Muster 7\Mrtool.exe\" -b -parent " + folder_id + " -s " + muster_server + " -port " + muster_server_port + " -u \"admin\" -p \"\" -sf " + start_frame + " -ef " + end_frame + " -bf " + by_frame + " -pool \"" + render_pool + "\" -e " + rendererID + " -pk " + packet_size + " -pr " + priority + " -max 0 -v 3 -n \"" + job_name + "\" -f \"" + batch_render_filename + "\""
        
        subprocess.call(cmdline.replace("/", "\\"))
    widget.close()


def getPools():

    server = widget.ui.muster_ip.text()
    port = widget.ui.muster_port.text()
    muster_path = "C:/Program Files/Virtual Vertex/Muster 7/"
    os.environ["PATH"] += os.pathsep + muster_path

    try:
        yyy = subprocess.Popen("mrtool -s " + server + " -port 9681 -u \"admin\" -p \"\" -q p -H 0 -S 0 -pf parent", shell=True, stdout=subprocess.PIPE).communicate()[0]
        pool = yyy.split("\r\n")
        myset = set(pool)
        final = []
        for x in myset:
            final.append(x.rstrip())
        final.pop(0)
    except:
        print "asdfsd"
    
        if len(final) == 0:
            final = ['Muster is Down']
    
    widget.ui.render_pool.addItems(final)


def poolModifier():
    modifiers = QtGui.QApplication.keyboardModifiers()
    if modifiers == QtCore.Qt.ControlModifier:
        colorDeSelected()
    else:
        colorSelected()


def colorSelected():
    selected = widget.ui.render_pool.selectedItems()
    for x in selected:
        x.setBackground(QtGui.QColor(215,128,26))
    widget.ui.render_pool.setStyleSheet("""
        QWidget {
            selection-background-color: #d7801a;
            }
        """)

def colorDeSelected():
    selected = widget.ui.render_pool.selectedItems()
    for x in selected:
        x.setBackground(QtGui.QColor(40,40,40))
    widget.ui.render_pool.setStyleSheet("""
        QWidget {
            selection-background-color: #282828;
            }
        """)

def getParent():
    global name
    server = widget.ui.muster_ip.text()
    port = widget.ui.muster_port.text()

    muster_path = "C:/Program Files/Virtual Vertex/Muster 7/"
    os.environ["PATH"] += os.pathsep + muster_path

    temp_array = []
    temp = subprocess.Popen("mrtool -s " + server + " -port " + port + " -u \"admin\" -p \"\" -q j -H 0 -S 0 -jf name,id", shell=True, stdout=subprocess.PIPE).communicate()[0]
    temp_array = temp.split("\r\n")

    muster_jobs = []
    for job in temp_array:
        job_id = job[39:].rstrip()
        job_name = job[:39].rstrip()
        muster_jobs.append([job_name, job_id])
    folder_id = ""
    for n, i in muster_jobs:
        if name[3][0] in n:
            folder_id = i
    if folder_id == "":
        temp = subprocess.Popen("mrtool -s " + server + " -port " + port + " -u \"admin\" -p \"\" -b -folder -n \"" + name[3][0] + "\"", shell=True, stdout=subprocess.PIPE).communicate()[0]
        folder_id = temp.split("ID: ")[1].rstrip()

    return folder_id
    

def getSelectedPools():
    pool = []
    count = widget.ui.render_pool.count()
    for x in range(0,count):
        if widget.ui.render_pool.item(x).background().color().getRgb() == (215,128,26,255):
            pool.append(widget.ui.render_pool.item(x).text())
    pool = ", ".join(pool)
    return pool


def openPath():
    image_folder = widget.ui.image_folder.text()
    if os.path.isdir(image_folder) is False:
        image_folder = proj_path + "/images"

    subprocess.check_call(['explorer', image_folder.replace("/","\\")])

def qt_muster_submitMain():
    global widget
    widget = musterWindow(parent=QtGui.QApplication.activeWindow())
    widget.ui.server_panel_button.clicked.connect(hideServerPanel)
    widget.ui.frame_range_panel_button.clicked.connect(hideFrameRangePanel)
    widget.ui.submit_render_button.clicked.connect(submitRender)
    widget.ui.nuke_panel_button.clicked.connect(hideNukePanel)
    widget.ui.open_path_button.clicked.connect(openPath)
    widget.ui.nuke_write_table.itemClicked.connect(chooseClick)
    widget.ui.render_pool.itemClicked.connect(poolModifier)
    widget.ui.default_selection_button.clicked.connect(defaultSelection)
    widget.ui.clear_selection_button.clicked.connect(clearSelection)
    
    hideFrameRangePanel()
    hideServerPanel()
    hideNukePanel()
    setMuster()

    getPools()
    defaultSelection()

    if "Nuke" in appName:
        nukeWriteNodes()

    widget.show()


def defaultSelection():
    if appName == "maya":
        widget.ui.render_pool.setCurrentItem(widget.ui.render_pool.findItems(u"Pixar",QtCore.Qt.MatchFlags(0))[0])
        colorSelected()
        widget.ui.render_pool.setCurrentItem(widget.ui.render_pool.findItems(u"VanGogh",QtCore.Qt.MatchFlags(0))[0])
        colorSelected()
    elif "Nuke" in appName:
        widget.ui.render_pool.setCurrentItem(widget.ui.render_pool.findItems(u"Pixar",QtCore.Qt.MatchFlags(0))[0])
        colorSelected()

    '''
    widget.ui.render_pool.setCurrentItem(widget.ui.render_pool.findItems("Davinci",0)[0])
    colorSelected()
    widget.ui.render_pool.setCurrentItem(widget.ui.render_pool.findItems("Monet",0)[0])
    colorSelected()
    '''
    
def clearSelection():
    count = widget.ui.render_pool.count()
    for x in range(0, count):
        widget.ui.render_pool.setCurrentRow(x)
        colorDeSelected()
    
    
def renameWriteNode():
    if widget.ui.nuke_write_table.currentColumn() == 0:
        pass
    elif widget.ui.nuke_write_table.currentColumn() == 1:
        if widget.ui.nuke_write_table.currentRow() == currentRow:
            currentName = widget.ui.nuke_write_table.currentItem().text()
            print currentName
            nuke.toNode(previousName)['name'].setValue(currentName)
        nukeWriteNodes()

def chooseClick():
    modifiers = QtGui.QApplication.keyboardModifiers()
    if modifiers == QtCore.Qt.ShiftModifier:
        doubleClick()
    else:
        singleClick()

def singleClick():
    global currentRow
    currentRow = widget.ui.nuke_write_table.currentRow()
    n = widget.ui.nuke_write_table.currentItem()
    nodename = widget.ui.nuke_write_table.item(currentRow,1).text()
    print nodename
    deselect()
    nuke.toNode(nodename)['selected'].setValue(True)
    node = nuke.selectedNode()
    nuke.zoom( 1, [ node.xpos(), node.ypos() ])
    nuke.show(node)

    if widget.ui.nuke_write_table.currentColumn() == 0:
        disable = QtGui.QTableWidgetItem()
        if n.text() == "on":
            disable.setIcon(nukecrossicon)
            disable.setText("off")
            nuke.toNode(nodename)['disable'].setValue(True)

        elif n.text() == "off":
            disable.setIcon(nukecheckicon)
            disable.setText("on")
            nuke.toNode(nodename)['disable'].setValue(False)

        widget.ui.nuke_write_table.setItem(currentRow, 0, disable)

    elif widget.ui.nuke_write_table.currentColumn() == 1:
        global previousName
        previousName = widget.ui.nuke_write_table.currentItem().text()
    elif widget.ui.nuke_write_table.currentColumn() == 2:
        filename = widget.ui.job_name.text()
        pathname = widget.ui.image_folder.text()
        nodepath = pathname + "/" + nodename
        nodepath = nodepath.replace("/","\\")
        if os.path.isdir(nodepath) is False:
            os.makedirs(nodepath)

        #path = pathname + "/" + nodename + "/" + filename + "_" + nodename + ".####.exr"
        #nuke.toNode(nodename)['file'].setValue(path)
def doubleClick():
    if widget.ui.nuke_write_table.currentColumn() == 0:
        row = widget.ui.nuke_write_table.currentRow()
        rows = widget.ui.nuke_write_table.rowCount()
        item = widget.ui.nuke_write_table.currentItem()
        name = widget.ui.nuke_write_table.item(row,1).text()

        nuke.selectAll()
        nodes = nuke.selectedNodes('Write')
        deselect()

        if item.text() == "on":
            for node in nodes:
                node['disable'].setValue(False)
            for x in range(rows):
                disable = QtGui.QTableWidgetItem()
                disable.setIcon(nukecheckicon)
                disable.setText("on")
                widget.ui.nuke_write_table.setItem(x, 0, disable) # change widget icon to X
            disable = QtGui.QTableWidgetItem()
            disable.setIcon(nukecrossicon)
            disable.setText("off")
            widget.ui.nuke_write_table.setItem(row, 0, disable) # change widget icon back to enable
            nuke.toNode(name)['disable'].setValue(True)

        elif item.text() == "off":
            for node in nodes:
                node['disable'].setValue(True) # disable all nuke write nodes
            for x in range(rows):
                disable = QtGui.QTableWidgetItem()
                disable.setIcon(nukecrossicon)
                disable.setText("off")
                widget.ui.nuke_write_table.setItem(x, 0, disable) # change widget icon to X
            disable = QtGui.QTableWidgetItem()
            disable.setIcon(nukecheckicon)
            disable.setText("on")
            widget.ui.nuke_write_table.setItem(row, 0, disable) # change widget icon back to enable
            nuke.toNode(name)['disable'].setValue(False)


def deselect():
    if nuke.selectedNodes():
        for i in nuke.selectedNodes():
            i['selected'].setValue(False)

def selectAllWrite():
    nuke.selectAll()
    nodes = nuke.selectedNodes('Write')
    deselect()
    for n in nodes:
        n['selected'].setValue(True)


def nukeWriteNodes():
    # this finds all the write nodes in the scene and loads them into a table

    widget.ui.nuke_write_table.setRowCount(0)
    widget.ui.nuke_write_table.setColumnWidth(0,23)
    i = 0
    nuke.selectAll()
    for n in nuke.selectedNodes('Write'):
        widget.ui.nuke_write_table.insertRow(i)
        node = QtGui.QTableWidgetItem(n['name'].value())
        #path = QtGui.QTableWidgetItem(n['file'].value())

        nodename = n['name'].value()
        filename = widget.ui.job_name.text()
        pathname = widget.ui.image_folder.text()
        path = pathname + "/" + nodename + "/" + filename + "_" + nodename + ".####.exr"
        print path

        nuke.toNode(nodename)['file'].setValue(path)

        font = QtGui.QFont()
        font.setPointSize(8)

        node.setFont(font)
        #path.setFont(font)

        disable = QtGui.QTableWidgetItem()
        createPath = QtGui.QTableWidgetItem()
        createPath.setIcon(foldericon)
        if n['disable'].value() == 1:
            disable.setIcon(nukecrossicon)
            disable.setText("off")
        elif n['disable'].value() == 0:
            disable.setIcon(nukecheckicon)
            disable.setText("on")
            filename = widget.ui.job_name.text()
            pathname = widget.ui.image_folder.text()
            nodepath = pathname + "/" + nodename
            nodepath = nodepath.replace("/","\\")
            if os.path.isdir(nodepath) is False:
                os.makedirs(nodepath)            

        disable.setTextAlignment(QtCore.Qt.AlignHCenter)

        widget.ui.nuke_write_table.setItem(i, 0, disable)
        widget.ui.nuke_write_table.setItem(i, 1, node)
        widget.ui.nuke_write_table.setItem(i, 2, createPath)

    widget.ui.nuke_write_table.itemChanged.connect(renameWriteNode)

    deselect()
#qt_muster_submitMain()
