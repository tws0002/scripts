import sys
sys.path.append("//Art-1405260002/d/assets/scripts/nuke_scripts/lib")
import nuke
import qt_pathconvert_ui
reload(qt_pathconvert_ui)
from PySide import QtCore, QtGui

class pathConvertWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(pathConvertWindow, self).__init__(parent)
        self.setFocus()
        self.setWindowFlags(QtCore.Qt.Tool)
        self.ui = qt_pathconvert_ui.Ui_pathConvert()
        self.ui.setupUi(self)
        self.ui.convert_all_button.clicked.connect(convertAll)
        self.ui.refresh_button.clicked.connect(getReadNodes)


def qt_pathconvertMain():
    global pathConvertWidget
    try:
        if pathConvertWidget:
            pathConvertWidget.show()
    except:
        pathConvertWidget = pathConvertWindow(parent=QtGui.QApplication.activeWindow())
        pathConvertWidget.show()
    getReadNodes()

def getReadNodes():
    global readNodes
    pathConvertWidget.ui.tableWidget.setRowCount(0)
    i = 0
    nuke.selectAll()
    readNodes = []
    for n in nuke.selectedNodes('Read'):
        pathConvertWidget.ui.tableWidget.insertRow(i)
        readNodes.append(n['name'].value())
        node = QtGui.QTableWidgetItem(n['name'].value())
        path = QtGui.QTableWidgetItem(n['file'].value())
        pathConvertWidget.ui.tableWidget.setItem(i, 0, node)
        pathConvertWidget.ui.tableWidget.setItem(i, 1, path)
        i = i + 1

    deselect()

def deselect():
    if nuke.selectedNodes():
        for i in nuke.selectedNodes():
            i['selected'].setValue(False)


def convertAll():
    search_text = pathConvertWidget.ui.search.text()
    replace_text = pathConvertWidget.ui.replace.text()

    for readNode in readNodes:
        m = nuke.toNode(readNode)
        #m['selected'].setValue(True)
        filepath = m['file'].value()
        if search_text in filepath:
            filepath = filepath.replace(search_text,replace_text)
        m['file'].setValue(filepath)
    getReadNodes()

    qt_pathconvertMain()
