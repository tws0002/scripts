import sys
sys.path.append("//Art-1405260002/d/assets/scripts/nuke_scripts")
sys.path.append("//Art-1405260002/d/assets/scripts/maya_scripts")
sys.path.append("//Art-1405260002/d/assets/scripts/nuke_scripts/install")

import nuke

import qt_pathconvert
#reload(qt_pathconvert)

#import qt_tactic_main
#reload(qt_tactic_main)


def test():
	print "what"
#nuke.menu("Nodes").addMenu("TT", icon="nk_tactic_icon.png").addCommand("PathConvert", "")
sidebar = nuke.menu("Nodes").addMenu("Tactic", icon="//Art-1405260002/d/assets/scripts/nuke_scripts/icons/nk_tactic_icon.png")
sidebar.addCommand("PathConvert", "test()", icon="//Art-1405260002/d/assets/scripts/nuke_scripts/icons/nk_pathconvert_icon.png")
#sidebar.addCommand("FileManager", "reload(qt_tactic_main)", icon="//Art-1405260002/d/assets/scripts/nuke_scripts/icons/nk_pathconvert_icon.png")
