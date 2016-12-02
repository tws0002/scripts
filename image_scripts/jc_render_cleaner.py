# -*- coding: utf-8 -*-
'''
import subprocess
import fileinput
input = "//Art-1405260002/d/assets/scripts/image_scripts/ui/clean_sequence.ui"
output = "//Art-1405260002/d/assets/scripts/image_scripts/ui/clean_sequence.py"
subprocess.call("C:/Python27/scripts/pyside-uic -o %s %s" % (output, input))
with open(output, 'r') as data:
    filedata = data.read()
header = "# -*- coding: utf-8 -*-\n"
header = header + "import sys\nsys.path.append(\"//Art-1405260002/d/assets/scripts/maya_scripts/lib\")\n"
filedata = filedata.replace(':/Art-1405260002', '//Art-1405260002')
filedata = filedata.replace('import icons_rc', '')
filedata = header + filedata
with open(output, 'w') as data:
    data.write(filedata)


'''
#%%
import sys
sys.path.append("//Art-1405260002/d/assets/scripts/nuke_scripts")
sys.path.append("//Art-1405260002/d/assets/scripts/image_scripts")

from PySide import QtCore, QtGui
from threading import Thread

import json, re, os, shutil
import os

try:
    O_BINARY = os.O_BINARY
except:
    O_BINARY = 0
READ_FLAGS = os.O_RDONLY | O_BINARY
WRITE_FLAGS = os.O_WRONLY | os.O_CREAT | os.O_TRUNC | O_BINARY
BUFFER_SIZE = 128*1024

class CTError(Exception):
    def __init__(self, errors):
        self.errors = errors

class copyThreadSignals(QtCore.QObject):
    maxLength = QtCore.Signal(int)
    count = QtCore.Signal(int)

class osThread(QtCore.QThread):
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.src = ""
        self.dst = ""
        self.files = [] 
        self.count = 0
        self.maxLength = 1
        self.signal = copyThreadSignals()

    def copyfiles(self, src, files):
        self.maxLength = len(files)
        self.signal.maxLength.emit(self.maxLength)
        self.count = 0
        if not os.path.exists(self.dst):
            os.makedirs(self.dst)
        for f in files:
            src = os.path.join(self.src, f)
            dst = os.path.join(self.dst, f)
            self.copyfile(src, dst)
            self.count = self.count + 1
            self.signal.count.emit(self.count)     

    def copyfile(self, src, dst):
        try:
            fin = os.open(src, READ_FLAGS)
            stat = os.fstat(fin)
            fout = os.open(dst, WRITE_FLAGS, stat.st_mode)
            for x in iter(lambda: os.read(fin, BUFFER_SIZE), ""):
                os.write(fout, x)
        finally:
            try: os.close(fin)
            except: pass
            try: os.close(fout)
            except: pass

    def copytree(self, src, dst, symlinks=False, ignore=[]):
        names = os.listdir(src)
        length = len(names)
        if not os.path.exists(dst):
            os.makedirs(dst)
        errors = []
        self.count = 0
        self.maxLength = length
        self.signal.maxLength.emit(self.maxLength)
        for name in names:
            if name in ignore:
                continue
            srcname = os.path.join(src, name)
            dstname = os.path.join(dst, name)
            try:
                if symlinks and os.path.islink(srcname):
                    linkto = os.readlink(srcname)
                    os.symlink(linkto, dstname)
                elif os.path.isdir(srcname):
                    self.copytree(srcname, dstname, symlinks, ignore)
                else:
                    self.copyfile(srcname, dstname)
                self.count = self.count + 1
                self.signal.count.emit(self.count)                    
            except (IOError, os.error), why:
                errors.append((srcname, dstname, str(why)))
            except CTError, err:
                errors.extend(err.errors)
        if errors:
            raise CTError(errors)

    def rmtree(self, path, ignore_errors=False, onerror=None):
        if ignore_errors:
             def onerror(*args):
                  pass
        elif onerror is None:
             def onerror(*args):
                  raise
        try:
             if os.path.islink(path):
                  # symlinks to directories are forbidden, see bug #1669
                  raise OSError("Cannot call rmtree on a symbolic link")
        except OSError:
             onerror(os.path.islink, path, sys.exc_info())
             # can't continue even if onerror hook returns
             return
        names = []
        try:
             names = os.listdir(path)
        except os.error, err:
             onerror(os.listdir, path, sys.exc_info())
        for name in names:
             fullname = os.path.join(path, name)
             try:
                  mode = os.lstat(fullname).st_mode
             except os.error:
                  mode = 0
             if stat.S_ISDIR(mode):
                  rmtree(fullname, ignore_errors, onerror)
             else:
                 try:
                     os.remove(fullname)
                 except os.error, err:
                     onerror(os.remove, fullname, sys.exc_info())
        try:
             os.rmdir(path)
        except os.error:
             onerror(os.rmdir, path, sys.exc_info())                 

    def run(self):
        if self.rl_dir == True:
            self.copytree(self.src, self.dst)
        elif self.rl_dir == False:
            self.copyfiles(self.src, self.files)



#--------------------------------
class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.verticalLayout_2 = QtGui.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtGui.QTableWidget(self)
        self.tableWidget.setObjectName("tableWidget")
        # get renderlayers here
        base = r"\\mcd-server\art_3d_project\fish_battle_cf\shot\shot_07\lighting\images"
        jsonPath = base.replace("\\","/") + "/fb_cf_shot_07_lig_v016_chihjung.json"

        #base = r"\\mcd-server\art_3d_project\fish_battle_cf\shot\shot_01\lighting\images"
        #jsonPath = base.replace("\\","/") + "/fb_cf_shot_01_lig_v029_sandy_yu.json"

        jsonData = file.read(open(jsonPath,"r"))
        self.renderData = json.loads(jsonData)
        self.baseName = re.search('(.+?)(_v[0-9]{3})', self.renderData['name']).group(1)

        self.progress_bar = QtGui.QProgressBar(self)
        self.progress_bar.setEnabled(True)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.verticalLayout_2.addWidget(self.progress_bar)

        self.verticalLayout_2.addWidget(self.tableWidget)
        self.tableWidget.cellClicked.connect(self.action)

        self.rl_dir_true = '#ffe11b'
        self.rl_dir_false = '#bedb39'
        self.master_color = '#fd7400'
        self.updateUI()

    def clearTableWidget(self):
        self.tableWidget.clear()

    def updateUI(self):
        self.tableWidget.clear()

        self.renderLayers = [x['name'] for x in self.renderData['renderLayers']]

        self.currentPath = self.renderData['currentPath']
        self.sceneData, self.existingDirs = self.getSceneData()

        columnCount = len(self.renderLayers) + 1
        rowCount = len(self.existingDirs) + 1
        self.tableWidget.setColumnCount(columnCount)
        self.tableWidget.setRowCount(rowCount)

        items = []
        horizontalLabels = []
        verticalLabels = []

        for count, renderLayer in enumerate(self.renderLayers):
            horizontalLabels.append(renderLayer)

        for existingDir in self.existingDirs:
            verticalLabels.append(existingDir)
        horizontalLabels.append("Delete")
        verticalLabels.append("Copy to Master")
        self.tableWidget.setHorizontalHeaderLabels(horizontalLabels)
        self.tableWidget.setVerticalHeaderLabels(verticalLabels)

        for xcount, existingDir in enumerate(self.sceneData):
            for ycount, renderLayer in enumerate(existingDir['data']):
                item = QtGui.QTableWidgetItem()
                item.setText(str(renderLayer['number']))
                item.setTextAlignment(QtCore.Qt.AlignHCenter)

                if renderLayer['rl_dir'] == True:
                    item.setBackground(QtGui.QColor(self.rl_dir_true))
                elif renderLayer['rl_dir'] == False:
                    item.setBackground(QtGui.QColor(self.rl_dir_false))
                if existingDir['name'] == 'master':
                    item.setBackground(QtGui.QColor(self.master_color))
                self.tableWidget.setItem(xcount, ycount, item)

        # label delete buttons
        for row in range(0, rowCount - 1):
            item = QtGui.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem(row, (columnCount - 1), item)
            item.setText("Delete")

        # label move buttons
        for col in range(0, columnCount - 1):
            item = QtGui.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem((rowCount -1), col, item)
            item.setText("Move")

        vHeaderWidth = self.tableWidget.verticalHeader().width()
        hHeaderHeight = self.tableWidget.horizontalHeader().height()
        self.tableWidget.horizontalHeader().height()
        colWidth = self.tableWidget.columnWidth(0)
        rowHeight = self.tableWidget.rowHeight(0)
        w = (colWidth * (columnCount + 2)) + vHeaderWidth + columnCount*2
        h = ((rowCount + 2) * rowHeight) + hHeaderHeight
        self.setMinimumSize(w,h)
        self.setMaximumSize(w,h)

    def progressBarCount(self,data):
        self.progress_bar.setValue(data)
    
    def progressBarMax(self, data):
        self.progress_bar.setMaximum(data)


    # logic to determin if pressing individual cells or "delete" or "move to master"
    def action(self, row, column):
        renderLayer = self.tableWidget.horizontalHeaderItem(column).text()
        sceneName = self.tableWidget.verticalHeaderItem(row).text()
        item = self.tableWidget.item(row, column)
        if renderLayer == "Delete":
            self.deleteAllImages(renderLayer, sceneName)
            self.updateUI()
        elif sceneName == "Copy to Master":
            latestRow = self.getLatest(renderLayer)
            self.deleteMasterRl(renderLayer)
            self.moveToMaster(renderLayer, latestRow, column)
            self.updateUI()
        else:
            self.deleteMasterRl(renderLayer)
            self.moveToMaster(renderLayer, row, column)
            self.updateUI()
    
    def makeMasterFolder(self, masterPath):
        master = os.path.isdir(masterPath)
        if master == False:
            os.mkdir(masterPath)
        else:
            pass

    def moveToMaster(self, renderLayer, row, column):
        masterPath = "%s/images/master" % self.currentPath
        self.makeMasterFolder(masterPath)
        sceneName = self.tableWidget.verticalHeaderItem(row).text()
        color = self.tableWidget.item(row, column).background().color().name()
        self.osThread = osThread()

        if color == self.rl_dir_false: # move files with renderlayer in name to master folder
            src = "%s/images/%s" % (self.currentPath, sceneName)
            dst = "%s/%s" % (masterPath, renderLayer)
            files = [x for x in os.listdir(src) if renderLayer in x]
            self.osThread.rl_dir = False
            self.osThread.files = files

        elif color == self.rl_dir_true: # move folders
            src = "%s/images/%s/%s" % (self.currentPath, sceneName, renderLayer)
            dst = "%s/%s" % (masterPath, renderLayer)
            self.osThread.rl_dir = True

        self.osThread.src = src
        self.osThread.dst = dst
        self.osThread.signal.count.connect(self.progressBarCount)
        self.osThread.signal.maxLength.connect(self.progressBarMax)
        self.osThread.start()

    def getLatest(self, renderLayer):
        currentCol = self.tableWidget.currentColumn()
        rowCount = self.tableWidget.rowCount()
        latestRows = []
        for row in range(0, rowCount - 2):
            cellText = self.tableWidget.item(row, currentCol).text()
            if cellText != '0':
                latestRows.append(row)
        return latestRows[-1]

    def deleteMasterRl(self, renderLayer):
        dirPath = "%s/images/master/%s" % (self.currentPath, renderLayer)
        if os.path.isdir(dirPath):
            print dirPath
            message = "Replace Master Render Layer folder with cuurent selection?"
            result = QtGui.QMessageBox.question(self, 'Warning', message, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if result == QtGui.QMessageBox.Yes:
                print 'Yes.'
                shutil.rmtree(dirPath)
            else:
                print 'No.'        
        else:
            pass


    def deleteAllImages(self, renderLayer, sceneName):
        #print "Deleting all images from %s" % sceneName  
        dirPath = "%s/images/%s" % (self.currentPath, sceneName)
        message = "Delete folder %s" % dirPath
        result = QtGui.QMessageBox.question(self, 'Warning', message, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if result == QtGui.QMessageBox.Yes:
            print 'Yes.'
            shutil.rmtree(dirPath)
        else:
            print 'No.'        

    # 
    def getSceneData(self):
        imagesPath = self.currentPath + "/images"
        existingDirs = [x for x in os.listdir(imagesPath) if os.path.isdir(os.path.join(imagesPath, x)) if self.baseName in x]
        sceneData = []
        for existingDir in existingDirs:
            # get those files using <scene>/<renderLayer>
            dirPath1 = "%s/%s" % (imagesPath,existingDir)
            files = os.listdir(dirPath1)
            versionData = []
            if len(files) != 0 and files[0] in self.renderLayers: # files in rl directories
                for renderLayer in self.renderLayers:
                    files = []
                    dirPath = "%s/%s/%s" % (imagesPath,existingDir, renderLayer)
                    try:
                        files = os.listdir(dirPath)
                    except:
                        files = []

                    data = {'layer':renderLayer, 'number':len(files), 'rl_dir':True, 'files':[]}
                    versionData.append(data)

            else: # files and passes all in same dir
                for renderLayer in self.renderLayers:
                    # cross check files with renderLayers
                    temp = []
                    for imageFile in files:
                        if renderLayer in imageFile:
                            temp.append(imageFile)
                    data = {'layer':renderLayer,'number':len(temp), 'rl_dir':False, 'files':temp}
                    versionData.append(data)

            sceneData.append({'name':existingDir, 'data':versionData})
        return [sceneData, existingDirs]

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())




