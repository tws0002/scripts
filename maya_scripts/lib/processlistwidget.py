from PySide import QtCore, QtGui
notready_icon = QtGui.QIcon('//art-1405260002/D/assets/scripts/maya_scripts/icons/proc_list/notready.png')
ready_icon = QtGui.QIcon('//art-1405260002/D/assets/scripts/maya_scripts/icons/proc_list/ready.png')
inprogress_icon = QtGui.QIcon('//art-1405260002/D/assets/scripts/maya_scripts/icons/proc_list/inprogress.png')
standby_icon = QtGui.QIcon('//art-1405260002/D/assets/scripts/maya_scripts/icons/proc_list/standby.png')
review_icon = QtGui.QIcon('//art-1405260002/D/assets/scripts/maya_scripts/icons/proc_list/review.png')
complete_icon = QtGui.QIcon('//art-1405260002/D/assets/scripts/maya_scripts/icons/proc_list/complete.png')

class processListWidget(QtGui.QListWidget):
    def __init__(self, parent= None, mainWindowObj= None):
        QtGui.QListWidget.__init__(self,parent)
        self.mainWindowObj = mainWindowObj

    def contextMenuEvent(self, event):
        menu = QtGui.QMenu(self)
        data = ""
        action1 = menu.addAction(notready_icon, 'Not Ready')
        action2 = menu.addAction(ready_icon, 'Ready')
        action3 = menu.addAction(inprogress_icon, 'In Progress')
        action4 = menu.addAction(standby_icon, 'Stand By')
        action5 = menu.addAction(review_icon, 'Review')        
        action6 = menu.addAction(complete_icon, 'Complete')        
        action = menu.exec_(self.mapToGlobal(event.pos()))
        sk = self.mainWindowObj.sk
        server = self.mainWindowObj.server
        if action == action1:
            data = {'status':'.Not Ready'}
        elif action == action2:
            data = {'status':'.Ready'}            
        elif action == action3:
            data = {'status':'.In Progress'}
        elif action == action4:
            data = {'status':'.Stand By'}
        elif action == action5:
            data = {'status':'.Review'}        
        elif action == action6:
            data = {'status':'.Complete'}

        if data == "":
            pass
        else:
            server.update(sk, data)
            self.mainWindowObj.getProcess()
#reloaded