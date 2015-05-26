# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel
import jc_maya_aux_functions as jc
import os
import subprocess

#  Result: -b -s 192.168.201.22 -port 9681 -u "admin" -p "" -sf 1 -ef 10 -bf 1 -attr MAYADIGITS 1 0 -se 1 -st 1 -e 2 -pk 4 -pr 1 -max 0 -v 3 -n "aoml_cf_c_character_rig_rig_v01_julio" -f "\\art-render\art_3d_project\adventure_of_mystical_land_cf\assets\character\character_rig\rigging\sourceimages\3dPaintTextures\aoml_cf_c_character_rig_rig_v01_julio.mb" -proj "\\art-render\art_3d_project\adventure_of_mystical_land_cf\assets\character\character_rig\rigging" //


def setMuster():
    name = jc.getNextFileName()
    path = name[0]
    base_scenename = name[1]
    full_filename = name[2]
    author = name[3][3]

    file_name_prefix = full_filename
    image_path = path + full_filename + "/"
    proj_path = path.replace("/images/", "")

    cmds.textFieldGrp("scene_name", e=1, tx=(base_scenename + "_" + author + ".mb"))
    cmds.textFieldGrp("job_name", e=1, tx=full_filename)
    cmds.textFieldGrp("image_folder", e=1, tx=path + full_filename)
    cmds.textFieldGrp("proj_folder", e=1, tx=proj_path)
    cmds.setAttr('defaultRenderGlobals.imageFilePrefix', file_name_prefix, type="string")

    start_frame = cmds.getAttr("defaultRenderGlobals.startFrame")
    end_frame = cmds.getAttr("defaultRenderGlobals.endFrame")
    cmds.intFieldGrp("start_frame", e=1, v1=start_frame)
    cmds.intFieldGrp("end_frame", e=1, v1=end_frame)
    # cmds.optionMenuGrp()


def mainUI():
    if cmds.window("MAYA2MUSTER2TACTIC", exists=True):
        cmds.deleteUI("MAYA2MUSTER2TACTIC")

    windowID = cmds.window("MAYA2MUSTER2TACTIC", sizeable=False)
    # parent window

    cmds.rowColumnLayout(nr=6, rs=[(1, 10)])  # top panel is project, bottom panel are tabs for shots and assets

    cw2 = [80, 300]
    framewidth = 400
    muster_server = "192.168.200.27"
    cmds.frameLayout(label="Server", width=framewidth, cll=1, cl=1)
    cmds.columnLayout(w=380, cal="center", rs=4)
    cmds.textFieldGrp("muster_server", l="Muster Server", cw=([2, 100]), tx=muster_server, en=1, cw2=cw2, cl2=["right", "left"])
    cmds.textFieldGrp("muster_server_port", l="Muster Port", cw=([2, 50]), tx="9681", en=1, cw2=cw2, cl2=["right", "left"])
    cmds.intFieldGrp("priority", l="Priority", en=1, cw2=cw2, cw=([2, 50]), v1=100, cl2=["right", "left"])
    cmds.intFieldGrp("packet_size", l="Packet Size", en=1, cw=([2, 50]), cw2=cw2, v1=4, cl2=["right", "left"])
    '''
    cmds.optionMenuGrp("renderers", l="Renderers", en=1, cw2=[120,50],cc=setRenderer)
    cmds.menuItem( label='mayaSoftware' )
    cmds.menuItem( label='mayaHardware' )
    cmds.menuItem( label='mayaHardware2' )
    cmds.menuItem( label='mentalRay' )
    cmds.menuItem( label='arnold' )
    '''
    cmds.setParent("..")
    cmds.setParent("..")


    cmds.frameLayout(label="Frame Ranges", width=framewidth, cll=1, cl=1)
    cmds.columnLayout(w=380, cal="center", rs=4)
    cmds.intFieldGrp("start_frame", cw=([2, 50]), l="Start Frame", v1=1, en=1, cw2=cw2, cl2=("right", "left"))
    cmds.intFieldGrp("end_frame", cw=([2, 50]), l="End Frame", v1=1, en=1,  cw2=cw2, cl2=("right", "left"))
    cmds.intFieldGrp("by_frame", cw=([2, 50]), l="By Frame", v1=1, en=1,  cw2=cw2, cl2=("right", "left"))
    cmds.intFieldGrp("frame_padding", cw=([2, 50]), l="Frame Padding", v1=4, en=1, cw2=cw2, cl2=("right", "left"))
    cmds.setParent("..")
    cmds.setParent("..")

    cmds.frameLayout(label="Submit", width=framewidth, cll=1, cl=0)
    cmds.columnLayout(w=380, cal="center", rs=4)
    cmds.textFieldGrp("scene_name", l="Scene Name", vis=0, tx="", en=1, cw2=cw2, cl2=["right", "left"])
    cmds.textFieldGrp("job_name", l="Job Name", tx="", en=1, cw2=cw2, cl2=["right", "left"])
    cmds.textFieldGrp("image_folder", l="Image Folder", vis=1, tx="", en=1, cw2=cw2, cl2=["right", "left"])
    cmds.textFieldGrp("proj_folder", l="Project Folder", vis=0, tx="", en=1, cw2=cw2, cl2=["right", "left"])
    cmds.textFieldGrp("cmdline", l="Command Line", tx="", vis=0, en=1, cw2=cw2, cl2=["right", "left"])
    cmds.optionMenuGrp("render_pool", l="Render Pool", en=1, cw2=cw2, cl2=["right", "left"])
    cmds.setParent("..")
    cmds.rowColumnLayout(nc=2, cw=([1, 80], [2, 220]))
    cmds.text("")
    cmds.button("Save + Submit", c=submitRender)
    cmds.setParent("..")
    cmds.setParent("..")

    cmds.showWindow(windowID)
    getPools()
    setMuster()


def submitRender(arg=None):
    # Result: -b -s 192.168.201.22 -port 9681 -u "admin" -p "" -sf 1 -ef 10 -bf 1 -attr MAYADIGITS 1 0 -se 1 -st 1 -e 2 -pk 4 -pr 1 -max 0 -v 3
    # -n "aoml_cf_c_character_rig_rig_v01_julio"
    # -f "\\art-render\art_3d_project\adventure_of_mystical_land_cf\assets\character\character_rig\rigging\sourceimages\3dPaintTextures\aoml_cf_c_character_rig_rig_v01_julio.mb"
    # -proj "\\art-render\art_3d_project\adventure_of_mystical_land_cf\assets\character\character_rig\rigging"

    muster_server = cmds.textFieldGrp("muster_server", q=1, tx=1)
    muster_server_port = cmds.textFieldGrp("muster_server_port", q=1, tx=1)
    start_frame = str(cmds.intFieldGrp("start_frame", q=1, v1=1))
    end_frame = str(cmds.intFieldGrp("end_frame", q=1, v1=1))
    by_frame = str(cmds.intFieldGrp("by_frame", q=1, v1=1))
    frame_padding = str(cmds.intFieldGrp("frame_padding", q=1, v1=1))
    priority = str(cmds.intFieldGrp("priority", q=1, v1=1))
    packet_size = str(cmds.intFieldGrp("packet_size", q=1, v1=1))
    render_pool = cmds.optionMenuGrp("render_pool", q=1, v=1)
    scene_name = cmds.textFieldGrp("scene_name", q=1, tx=1)
    job_name = cmds.textFieldGrp("job_name", q=1, tx=1)
    image_folder = cmds.textFieldGrp("image_folder", q=1, tx=1)
    proj_folder = cmds.textFieldGrp("proj_folder", q=1, tx=1)

    batch_render_filename = proj_folder + "/scenes/" + scene_name
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
        cmds.setAttr("defaultArnoldDriver.aiTranslator", "exr", type="string")
        cmds.setAttr("defaultArnoldDriver.exrCompression", 3)
        imageFormat = "exr"
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
            if renderer in mayaDefaultRenderers:
                cmds.setAttr("defaultRenderGlobals.imageFormat", 4)
                imageFormat = "tif"
            else:
                cmds.setAttr("defaultRenderGlobals.imageFormat", 51)
                imageFormat = "exr"

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
        
        if imageFormat == "exr":
            imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe -colorspace RGB \"%s\" -colorspace sRGB \"%s\""  % (sequence_filename + "[" + start_frame + "-" + end_frame + "]", sequence_filename.replace(".exr",".tif") + "[" + start_frame + "-" + end_frame + "]")
            master_bat_file.writelines(imageMagickCMD + "\n")
        
        convertCMD = "//Art-1405260002/d/assets/scripts/ffmpeg/bin/ffmpeg -i \"%s\" -c:v libx264 -crf 19 -preset slow -c:a aac -strict experimental -b:a 192k -ac 2 -s %s -aspect %s \"%s\"" % (sequence_filename.replace(".exr",".tif"), size, ar, mp4_filename)
        master_bat_file.writelines(convertCMD + "\n")

        deleteTIFCMD = "del " + delete_filename.replace(".exr",".tif")
        master_bat_file.writelines(deleteTIFCMD.replace("/", "\\") + "\n")
        # bat_file.close()
        #master_bat_file.writelines(image_folder + "/" + renderLayer + "/convert.bat" + "\n")

    master_bat_file.close()

    post_job_action = image_folder + "\convert.bat"
    post_job_action = post_job_action.replace("/", "\\")
    # post_job_action = ""

    cmdline = "\"C:\Program Files\Virtual Vertex\Muster 7\Mrtool.exe\" -b -s " + muster_server + " -port " + muster_server_port + " -u \"admin\" -p \"\" -sf " + start_frame + " -ef " + end_frame + " -bf " + by_frame + " -attr MAYADIGITS " + frame_padding + " 0 -attr ARNOLDMODE 0 0 -attr ARNOLDLICENSE 1 1 -pool \"" + render_pool + "\" -se 1 -st 1 -e " + rendererID + " -pk " + packet_size + " -pr " + priority + " -max 0 -v 3 -eja \"" + post_job_action + "\" -n \"" + job_name + "\" -dest \"" + image_folder + "\" -f \"" + batch_render_filename + "\" -proj \"" + proj_folder + "\""

    cmds.textFieldGrp("cmdline", e=1, tx=cmdline.replace("/", "\\"))

    subprocess.call(cmdline.replace("/", "\\"))
    

def getPools():
    server = cmds.textFieldGrp("muster_server", q=1, tx=1)
    port = cmds.textFieldGrp("muster_server_port", q=1, tx=1)

    muster_path = "C:/Program Files/Virtual Vertex/Muster 7/"
    os.environ["PATH"] += os.pathsep + muster_path
    yyy = subprocess.Popen("mrtool -s 192.168.200.27 -port 9681 -u \"admin\" -p \"\" -q p -H 0 -S 0 -pf parent", shell=True, stdout=subprocess.PIPE).communicate()[0]
    pool = yyy.split("\r\n")
    myset = set(pool)
    final = []
    for x in myset:
        final.append(x.rstrip())
    final.pop(0)
    cmds.optionMenuGrp("render_pool", e=1, )
    for x in final:
        cmds.menuItem(label=x)
    #return final

mainUI()
