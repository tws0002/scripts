import MaxPlus
import sys
sys.path.append("//Art-1405260002/d/assets/client")
sys.path.append("//Art-1405260002/d/assets/scripts/maya_scripts/lib")
sys.path.append("//Art-1405260002/d/assets/scripts/maya_scripts")
sys.path.append("//Art-1405260002/d/assets/scripts/install")

import qt_tactic_main

action1 = MaxPlus.ActionFactory.Create('Do something', 'TACTIC', qt_tactic_main.qt_tactic_mainMain)

MenuName = "TACTIC"
mb = MaxPlus.MenuBuilder(MenuName)
mb.AddItem(action1)
mb.AddSeparator()
menu = mb.Create(MaxPlus.MenuManager.GetMainMenu())
