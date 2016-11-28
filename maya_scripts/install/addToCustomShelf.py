# -*- coding: utf-8 -*-
# this script will search for a script directory and append them to the custom shelf
# existing scripts will not be affected


import os
import maya.cmds as cmds
import maya.mel as mel
homepath = os.environ.get("HOMEPATH")
homedrive = os.environ.get("HOMEDRIVE")
tactic_shelf_2014 = homedrive + homepath + "\\Documents\maya\\2014-x64\prefs\shelves\\shelf_TACTIC.mel"
tactic_shelf_2015 = homedrive + homepath + "\\Documents\maya\\2015-x64\prefs\shelves\\shelf_TACTIC.mel"

if cmds.shelfLayout("TACTIC", q=1, ex=1) == True:
    if cmds.about(version=1) == "2014 x64":
        os.remove(tactic_shelf_2014)
    elif cmds.about(version=1) == "2015 x64":
            os.remove(tactic_shelf_2015)
    else:
        pass
else:
    mel.eval('addNewShelfTab "TACTIC";')

tempList = []
tempList = cmds.shelfLayout('TACTIC', q=1, ca=1)
buttonList = []

if tempList > 0:
    for button in tempList:
        buttonList.append(cmds.shelfButton(button, q=1, l=1))
        
scripts_path = "//Art-1405260002/d/assets/scripts/maya_scripts/"
scriptList = []
scripts = os.listdir(scripts_path)

#ignore = []
ignore = ["config.py", "getEnvironmet.py", "qt_tactic_dev.py"]

tempList = []
tempList = cmds.shelfLayout('TACTIC', q=1, ca=1)

if tempList == None:
    pass
else:
    for button in tempList:
        cmds.deleteUI(button)
    
try:
    for script in scripts:  # find scripts in directory
        if os.path.isdir(scripts_path + script) is True:
            pass
        else:
            if script.split(".")[1] != "py":
                pass
            elif script in ignore:
                pass
            else:
                scriptList.append(script)

       
    for script in scriptList:
        name = script.split(".")[0]
        source_type = script.split(".")[1]
        if source_type == "py":
            command = "import " + name + "\n" + "reload(" + name + ")" + "\n" + name + "." + name + "Main()"
            source_type = "python"
        elif source_type == "mel":
            command = "source \"" + scripts_path + script + "\";" + "\n" + name + "();"
        image = scripts_path + "icons/" + name + ".png"
        cmds.shelfButton(p='TACTIC', l=name, i=image, c=command, rpt=1, stp=source_type)
            # print command
except:
    pass
