import nuke
import sys
sys.path.append("//Art-1405260002/d/assets/scripts/nuke_scripts")
sys.path.append("//Art-1405260002/d/assets/scripts/maya_scripts")

tactic_icon = "//Art-1405260002/d/assets/scripts/nuke_scripts/icons/nk_tactic_icon.png"
pathconvert_icon = "//Art-1405260002/d/assets/scripts/nuke_scripts/icons/nk_pathconvert_icon.png"
renderfarm_icon = "//Art-1405260002/d/assets/scripts/nuke_scripts/icons/nk_renderfarm_icon.png"

sidebar = nuke.menu("Nodes").addMenu("Tactic", icon=tactic_icon)
#sidebar.addCommand("PathConvert", "import qt_pathconvert\nreload(qt_pathconvert)\nqt_pathconvert.qt_pathconvertMain()", icon=pathconvert_icon)
sidebar.addCommand("FileManager", "import qt_tactic_main\nreload(qt_tactic_main)\nqt_tactic_main.qt_tactic_mainMain()", icon=tactic_icon)
#sidebar.addCommand("RenderFarm", "import qt_muster_submit\nreload(qt_muster_submit)\nqt_muster_submit.qt_muster_submitMain()", icon=renderfarm_icon)
