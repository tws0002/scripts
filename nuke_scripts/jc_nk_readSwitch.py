# -*- coding: utf-8 -*-
import sys
import nuke
sys.path.append("//Art-1405260002/d/assets/scripts/nuke_scripts")
sys.path.append("//Art-1405260002/d/assets/scripts/image_scripts")

from PySide import QtCore, QtGui

import json, re, os

class RotatedHeaderView(QtGui.QHeaderView):
    def __init__(self, parent=None):
        super(RotatedHeaderView, self).__init__(QtCore.Qt.Horizontal, parent)
        self.setMinimumSectionSize(8)
        self.setDefaultSectionSize(30)


    def paintSection(self, painter, rect, logicalIndex ):
        painter.save()
        # translate the painter such that rotate will rotate around the correct point
        painter.translate(rect.x(), rect.y() + rect.height())
        painter.rotate(-90)
        
        # and have parent code paint at this location
        newrect = QtCore.QRect(0,0,rect.height(),rect.width())
        super(RotatedHeaderView, self).paintSection(painter, newrect, logicalIndex)
        painter.restore()

    def minimumSizeHint(self):
        size = super(RotatedHeaderView, self).minimumSizeHint()
        size.transpose()
        return size

    def sectionSizeFromContents(self, logicalIndex):
        size = super(RotatedHeaderView, self).sectionSizeFromContents(logicalIndex)
        size.transpose()
        return size

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.verticalLayout_2 = QtGui.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtGui.QTableWidget(self)
        self.tableWidget.setObjectName("tableWidget")
        self.dirStructure = []
        self.newStructure = []
        self.count = 0

        nuke.selectAll()
        self.readNodes = []
        for n in nuke.selectedNodes('Read'):
            self.readNodes.append(n)        

        sceneFullPath = nuke.root().name()
        basePath, baseName = sceneFullPath.split("/comp/scenes")

        baseName = baseName[1:-3] 
        baseName = re.search('(.+?)(_v[0-9]{3})', baseName).group(1)
        baseName = baseName.replace("comp","lig")        

        imagesPath = "%s/lighting/images" % basePath
        self.existingDirs = [x for x in os.listdir(imagesPath) if "." not in x]

        self.verticalLayout_2.addWidget(self.tableWidget)
        self.getAll(imagesPath, "")
        self.reorderStructure()
        self.updateUI()

    
    def reorderStructure(self):
        for x, data in enumerate(self.dirStructure):
            if data['count'] == 1 and len(data['passes']) > 0:
                self.newStructure.append(data)
        
            passes = ""
            if len(self.dirStructure[x]['passes']) == 0:
                passes = self.forward(x)
                ndata = {'count':1, 'path': self.dirStructure[x]['dir'], 'passes':passes}
                self.newStructure.append(ndata)

    def forward(self, current_index):  
        next_index = current_index + 1
        t = []
        if next_index < len(self.dirStructure):
            if self.dirStructure[next_index]['count'] == 2:
                t = t + self.dirStructure[next_index]['passes']
                self.forward(next_index)
        return t

    def clearTableWidget(self):
        self.tableWidget.clear()

    def updateUI(self):
        self.tableWidget.clear()

        columnCount = len(self.readNodes)
        rowCount = len(self.existingDirs)
        self.tableWidget.setColumnCount(columnCount)
        self.tableWidget.setRowCount(rowCount)

        items = []
        horizontalLabels = []
        verticalLabels = []

        for readNode in self.readNodes:
            horizontalLabels.append(readNode.name())

        for existingDir in self.existingDirs:
            verticalLabels.append(existingDir)

      
        self.tableWidget.setHorizontalHeader(RotatedHeaderView(self.tableWidget))
        self.tableWidget.setHorizontalHeaderLabels(horizontalLabels)
        self.tableWidget.setVerticalHeaderLabels(verticalLabels)


        for xcount, existingDir in enumerate(self.newStructure):
            if existingDir['count'] == 1:
                for ycount, readNode in enumerate(self.readNodes):
                    readNodeBaseName = readNode.knob('file').value().split("/")[-1]
                    readNodeBaseName  = re.search('(.+?)(.%04d)', readNodeBaseName).group(1)
                    if readNodeBaseName in existingDir['passes']:
                        item = QtGui.QTableWidgetItem()
                        item.setText('V')
                        self.tableWidget.setItem(xcount, ycount, item)


        # for xcount, existingDir in enumerate(self.sceneData):
        #     for ycount, renderLayer in enumerate(existingDir['data']):
        #         item = QtGui.QTableWidgetItem()
        #         item.setText(str(renderLayer['number']))
        #         item.setTextAlignment(QtCore.Qt.AlignHCenter)

        #         if renderLayer['rl_dir'] == True:
        #             item.setBackground(QtGui.QColor(self.rl_dir_true))
        #         elif renderLayer['rl_dir'] == False:
        #             item.setBackground(QtGui.QColor(self.rl_dir_false))
        #         if existingDir['name'] == 'master':
        #             item.setBackground(QtGui.QColor(self.master_color))
        #         self.tableWidget.setItem(xcount, ycount, item)

        # # label delete buttons
        # for row in range(0, rowCount - 1):
        #     item = QtGui.QTableWidgetItem()
        #     item.setTextAlignment(QtCore.Qt.AlignHCenter)
        #     self.tableWidget.setItem(row, (columnCount - 1), item)
        #     item.setText("Delete")

        # # label move buttons
        # for col in range(0, columnCount - 1):
        #     item = QtGui.QTableWidgetItem()
        #     item.setTextAlignment(QtCore.Qt.AlignHCenter)
        #     self.tableWidget.setItem((rowCount -1), col, item)
        #     item.setText("Move")

        # vHeaderWidth = self.tableWidget.verticalHeader().width()
        # hHeaderHeight = self.tableWidget.horizontalHeader().height()
        # self.tableWidget.horizontalHeader().height()
        # colWidth = self.tableWidget.columnWidth(0)
        # rowHeight = self.tableWidget.rowHeight(0)
        # w = (colWidth * (columnCount + 2)) + vHeaderWidth + columnCount*2
        # h = ((rowCount + 2) * rowHeight) + hHeaderHeight
        # self.setMinimumSize(w,h)
        # self.setMaximumSize(w,h)


    def getAll(self, path, directory, count=0):
        subpath = os.path.join(path, directory)
        contents = os.listdir(subpath)
        files = [x for x in contents if "." in x]
        directories = [x for x in contents if "." not in x]
        baseName = ""
        passes = []
        if count == 1:
            passes = []
        for image in files:
            try:
                baseName = re.search('(.+?)([0-9]{4})', image).group(1)[:-1]
            except:
                pass
            if baseName not in passes:
                passes.append(baseName)
        
        self.dirStructure.append({'dir': directory, 'passes':passes, 'count':count})

        if len(directories) > 0:
            for directory in directories:
                count = count + 1
                self.getAll(subpath, directory, count=count)
                count = count - 1


win = Window()
win.show()

