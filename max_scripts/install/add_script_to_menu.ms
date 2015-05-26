mainMenuBar = menuMan.getMainMenuBar()
tacticMenu = menuMan.findMenu "TACTIC"
if (tacticMenu != undefined) do (
	menuMan.unRegisterMenu tacticMenu
)

python.ExecuteFile "//Art-1405260002/d/assets/scripts/max_scripts/tactic_mainmenu.py"
