# -*- coding: utf-8 -*-
import PySide.QtCore as qc
import PySide.QtGui as qg
import pymel.core as pm
import os
import maya.cmds as mc
global ui

dialog=None

#---------------------------------------------------------------------------------------------------#

class Black_UI(qg.QDialog):
    def __init__(self):
        qg.QDialog.__init__(self)
        self.setWindowTitle('pxrTexManager'+' v1.0'+u' by 小黑')
        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setModal(False)
        self.resize(600,480)
        self.setLayout(qg.QVBoxLayout())

        #定義上方UI
        analyseButton = qg.QPushButton('Analyse scence File Textures')
        analyseButton.clicked.connect(self.pathFinalCheck)
        self.layout().addWidget(analyseButton)
        SelectLabel=qg.QLabel('Select file you want to manager.<Multi-Selectable>')
        SelectLabel.setAlignment(qc.Qt.AlignCenter)
        self.layout().addWidget(SelectLabel)

        #定義拉霸欄UI
        self.pathListWidget = qg.QWidget()
        self.pathListLayout = qg.QVBoxLayout()
        self.pathListLayout.setAlignment(qc.Qt.AlignTop)
        self.pathListWidget.setLayout(self.pathListLayout)
        pathListScrollArea = qg.QScrollArea()
        pathListScrollArea.setWidgetResizable(True)
        pathListScrollArea.setWidget(self.pathListWidget)
        self.layout().addWidget(pathListScrollArea)

        #當前專案目錄顯示
        current_workspace_Layout = qg.QHBoxLayout()
        current_workspace=mc.workspace( q=True, rd=True )
        current_workspace_Label=qg.QLabel('Current Project : ')
        current_workspace_Edit=qg.QLineEdit(current_workspace+'sourceimages')
        current_workspace_Layout.addWidget(current_workspace_Label)
        current_workspace_Layout.addWidget(current_workspace_Edit)
        self.layout().addLayout(current_workspace_Layout)

        #定義路徑替換UI
        substitueLabel=qg.QLabel('Substitue path root')
        self.layout().addWidget(substitueLabel)
        replacePathFormLayout=qg.QFormLayout()
        self.oldRoot=qg.QLineEdit()
        self.newRoot=qg.QLineEdit()
        replacePathFormLayout.addRow('Old Root',self.oldRoot)
        replacePathFormLayout.addRow('New Root',self.newRoot)
        self.layout().addLayout(replacePathFormLayout)
        substituteButton = qg.QPushButton('substitute')
        substituteButton.clicked.connect(self.substitutePath)
        self.layout().addWidget(substituteButton)




    def listDirs(self):
        u'''搜索所有PxrTextureNode與使用中的路徑'''
        pxrNodes = pm.ls(type='PxrTexture')
        allFilePath = []
        for node in pxrNodes:
            allFilePath.append(node.filename.get())
        return allFilePath, pxrNodes


    def fixDirs(self,path):
        u'''去除檔名,只留下路徑'''
        pathDirs=[]
        for i in path:
            if os.path.dirname(i) not in pathDirs:
                pathDirs.append(os.path.dirname(i))
        return pathDirs

    def checkExists(self,path):
        u'''確認貼圖是否存在'''
        if '_MAPID_' in path:
            path=path.replace('_MAPID_','1001')
        currentProj = mc.workspace(q=True, rd=True)
        if path[0:12]=='sourceimages':
            path=currentProj+path
        path=path.replace('/','\\')
        return os.path.exists(path)



    def grpDirs(self):
        u'''整理成一個List'''
        pathGrp=[]
        allFilePath,pxrNodes=self.listDirs()
        fixDirsR=self.fixDirs(allFilePath)
        for c,fPath in enumerate(fixDirsR):
            pathGrp.append({})
            pathGrp[c]['path']=str(fPath)
            pathGrp[c]['used']=[]
            pathGrp[c]['exists']=[]
            pathGrp[c]['notExists']=[]
            for c2,aPath in enumerate(allFilePath):
                if os.path.dirname(aPath)==fPath:
                    pathGrp[c]['used'].append(pxrNodes[c2].name())
                    if self.checkExists(aPath):
                        pathGrp[c]['exists'].append(pxrNodes[c2].name())
                    else:
                        pathGrp[c]['notExists'].append(pxrNodes[c2].name())
        return pathGrp


    def pathFinalCheck(self):
        u'''創建內嵌式列表'''
        #刪除列表
        for i in self.pathListWidget.children():
            if type(i) == pathList_wid_class or type(i)==qg.QLabel:
                i.deleteLater()
        self.substituteNode=[]

        #創建資訊列
        allFilePath,pxrNodes=self.listDirs()
        pxrNodesNum=len(pxrNodes)
        pathGrp=self.grpDirs()
        pathGrpNum=len(pathGrp)
        allPath_Label=qg.QLabel('Total '+ str(pxrNodesNum) +' file textures point to '+str(pathGrpNum)+' (difference) path(s)')
        self.pathListLayout.addWidget(allPath_Label)

        #創建列表
        for path in pathGrp:
            pathList_wid_add = pathList_wid_class(path['path'], path['used'], path['exists'],path['notExists'])
            self.pathListLayout.addWidget(pathList_wid_add)

    def substitutePath(self):
        u'''點擊轉換按鈕觸發'''
        pm.undoInfo(ock=True)
        for i in self.substituteNode:
            path=mc.getAttr(i+'.filename')
            pathChanged=self.replace(path)
            mc.setAttr(i+'.filename',str(pathChanged),type='string')
        pm.undoInfo(cck=True)


    def replace(self,path):
        u'''路徑替換'''
        oldPath=self.oldRoot.text()
        newPath=self.newRoot.text()
        newPath=newPath.replace('\\','/')
        pathChanged=path.replace(oldPath,newPath)
        return pathChanged

#---------------------------------------------------------------------------------------------------#
class pathList_wid_class(qg.QWidget):
    def __init__(self, path, used, exists, notExists):
        self.path=path
        self.used=used
        self.exists=exists
        self.notExists=notExists
        #定義UI
        qg.QWidget.__init__(self)
        self.OutsideLayout=qg.QVBoxLayout()
        self.setLayout(self.OutsideLayout)
        self.layout().setAlignment(qc.Qt.AlignTop)
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setSpacing(0)

        #定義路徑欄UI
        pathNameListLayout = qg.QHBoxLayout()
        self.layout().addLayout(pathNameListLayout)
        self.usedNum=len(used)
        self.pathCB = qg.QCheckBox(str(self.usedNum)+' texture(s) point to '+self.path)
        pathNameListLayout.addWidget(self.pathCB)
        self.pathCB.stateChanged.connect(self.path_uesd_hit)

        #定義貼圖存在欄UI
        self.existsListLayout = qg.QHBoxLayout()
        self.layout().addLayout(self.existsListLayout)
        exitsNum=len(self.exists)
        self.exitsNumCB = qg.QCheckBox(str(exitsNum)+' of them exist(s).')
        existsSpacerItem = qg.QSpacerItem(30, 10, qg.QSizePolicy.Fixed)
        self.existsListLayout.addItem(existsSpacerItem)
        self.existsListLayout.addWidget(self.exitsNumCB)
        self.exitsNumCB.stateChanged.connect(self.exists_hit)

        #定義貼圖不存在欄UI
        self.notExistsListLayout = qg.QHBoxLayout()
        self.layout().addLayout(self.notExistsListLayout)
        notExistsNum=len(self.notExists)
        self.notExistsNumCB = qg.QCheckBox(str(notExistsNum)+' of them NOT exist(s).')
        if notExistsNum>0:
            self.notExistsNumCB.setStyleSheet("font: bold;color: rgb(255, 0, 0);")
        notExistsSpacerItem = qg.QSpacerItem(30, 10, qg.QSizePolicy.Fixed)
        self.notExistsListLayout.addItem(notExistsSpacerItem)
        self.notExistsListLayout.addWidget(self.notExistsNumCB)
        self.notExistsNumCB.stateChanged.connect(self.notExists_hit)



    def path_uesd_hit(self, state):
        u'''點擊路徑按鈕觸發'''
        if state == qc.Qt.Checked:
            self.exitsNumCB.setChecked(False)
            self.notExistsNumCB.setChecked(False)
            self.clearLayout(self.existsListLayout)
            self.clearLayout(self.notExistsListLayout)

            for i in self.used:
                if i not in dialog.substituteNode:
                    dialog.substituteNode.append(i)
            pm.select(self.used)
        else:
            exitsNum=len(self.exists)
            self.exitsNumCB = qg.QCheckBox(str(exitsNum)+' of them exist(s).')
            existsSpacerItem = qg.QSpacerItem(30, 10, qg.QSizePolicy.Fixed)
            self.existsListLayout.addItem(existsSpacerItem)
            self.existsListLayout.addWidget(self.exitsNumCB)
            self.exitsNumCB.stateChanged.connect(self.exists_hit)



            notExistsNum=len(self.notExists)
            self.notExistsNumCB = qg.QCheckBox(str(notExistsNum)+' of them NOT exist(s).')
            #如果貼圖不存在,字樣變紅色
            if notExistsNum>0:
                self.notExistsNumCB.setStyleSheet("font: bold;color: rgb(255, 0, 0);")
            notExistsSpacerItem = qg.QSpacerItem(30, 10, qg.QSizePolicy.Fixed)
            self.notExistsListLayout.addItem(notExistsSpacerItem)
            self.notExistsListLayout.addWidget(self.notExistsNumCB)
            self.notExistsNumCB.stateChanged.connect(self.notExists_hit)

            for i in self.used:
                if i in dialog.substituteNode:
                    dialog.substituteNode.remove(i)

            pass

    def exists_hit(self,state):
        u'''點擊存在按鈕觸發'''
        if state == qc.Qt.Checked:
            self.pathCB.setChecked(False)
            self.notExistsNumCB.setChecked(False)

            for i in self.exists:
                if i not in dialog.substituteNode:
                    dialog.substituteNode.append(i)
            pm.select(self.exists)

        else:
            for i in self.exists:
                if i in dialog.substituteNode:
                    dialog.substituteNode.remove(i)
            pass

    def notExists_hit(self,state):
        u'''點擊不存在按鈕觸發'''
        if state == qc.Qt.Checked:
            self.pathCB.setChecked(False)
            self.exitsNumCB.setChecked(False)

            for i in self.notExists:
                if i not in dialog.substituteNode:
                    dialog.substituteNode.append(i)
            pm.select(self.notExists)
        else:
            for i in self.notExists:
                if i in dialog.substituteNode:
                    dialog.substituteNode.remove(i)
            pass

    def clearLayout(self,layout):
        u'''清除layout底下所有物件'''
        while layout.count() > 0:
            item = layout.takeAt(0)
            if not item:
                continue
            w = item.widget()
            if w:
                w.deleteLater()







#---------------------------------------------------------------------------------------------------#
def create():
    global dialog
    if dialog is None:
        dialog =Black_UI()
    dialog.show()

def delete():
    global dialog
    if dialog is None:
        return
    dialog.deleteLater()
    dialog =None



def pxrManagerMain():
    global dialog
    if dialog is None:
        dialog =Black_UI()
    dialog.show()