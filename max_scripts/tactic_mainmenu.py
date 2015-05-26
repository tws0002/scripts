import MaxPlus
import sys
sys.path.append("//Art-1405260002/d/assets/client")
sys.path.append("//Art-1405260002/d/assets/scripts/maya_scripts/lib")
sys.path.append("//Art-1405260002/d/assets/scripts/maya_scripts")
sys.path.append("//Art-1405260002/d/assets/scripts/install")


import qt_tactic_main
import vray2tactic


action1 = MaxPlus.ActionFactory.Create('Do something', 'FileManager', qt_tactic_main.qt_tactic_mainMain)
action2 = MaxPlus.ActionFactory.Create('Do something', 'VRAY2TACTIC', vray2tactic.saveVrayVFB)

MenuName = "TACTIC"
mb = MaxPlus.MenuBuilder(MenuName)
mb.AddItem(action1)
mb.AddItem(action2)
mb.AddSeparator()
menu = mb.Create(MaxPlus.MenuManager.GetMainMenu())
#action.Execute()
'''

print MaxPlus.PathManager.GetUserStartupscriptsDir()
#MaxPlus.PathManager.SetUserStartupscriptsDir()

'''