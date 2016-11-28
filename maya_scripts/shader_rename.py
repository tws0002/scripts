# -*- coding: utf-8 -*-
import PySide.QtCore as qc
import PySide.QtGui as qg
import pymel.core as pm
import os
import maya.cmds as cmds
global ui

dialog=None

#---------------------------------------------------------------------------------------------------#

class Black_UI(qg.QDialog):
    def __init__(self):
        qg.QDialog.__init__(self)
        self.setWindowTitle('Rename Shader'+' v0.5'+u' by 小黑')
        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setModal(False)
        self.resize(600,480)
        self.setLayout(qg.QVBoxLayout())
        self.layout().setAlignment(qc.Qt.AlignTop)

        #定義上方UI
        top_button_layout = qg.QHBoxLayout()
        top_button_layout.setContentsMargins(0,0,0,0)
        selected_node_but = qg.QPushButton('Get the selected node')
        selected_node_but.clicked.connect(self.getSelectedNode)
        rename_label=qg.QLabel('rename  : ')
        self.rename_edit=qg.QLineEdit()
        preview_but = qg.QPushButton('Preview')
        preview_but.clicked.connect(self.previewRename)
        top_button_layout.addWidget(selected_node_but)
        top_button_layout.addWidget(rename_label)
        top_button_layout.addWidget(self.rename_edit)
        top_button_layout.addWidget(preview_but)
        self.layout().addLayout(top_button_layout)

        line=qg.QFrame()
        line.setFrameStyle(qg.QFrame.HLine)
        self.layout().addWidget(line)

        self.obj_list_widget = qg.QWidget()
        self.obj_list_layout = qg.QVBoxLayout()
        self.obj_list_layout.setAlignment(qc.Qt.AlignTop)
        self.obj_list_widget.setLayout(self.obj_list_layout)
        obj_list_scroll_Area = qg.QScrollArea()
        obj_list_scroll_Area.setWidgetResizable(True)
        obj_list_scroll_Area.setWidget(self.obj_list_widget)
        self.layout().addWidget(obj_list_scroll_Area)


        buttonWidget = qg.QWidget()
        buttonLayout=qg.QHBoxLayout()
        buttonLayout.setContentsMargins(0,0,0,0)
        buttonWidget.setLayout(buttonLayout)
        rename_but = qg.QPushButton('rename')
        rename_but.clicked.connect(self.renameAll)
        buttonLayout.addWidget(rename_but)
        self.layout().addWidget(buttonWidget)
        self.node_list=[]



#---------------------------------------------------------------------------------------------------#
    def getSelectedNode(self):
        #刪除列表
        for i in self.obj_list_widget.children():
            if type(i) == nodeList_wid_class or type(i)==qg.QLabel or type(i)==preview_nodeList_wid_class:
                i.deleteLater()

        self.node_list=cmds.ls( selection=True,ap=True )
        self.node_list.sort()
        obj_node_num=len(self.node_list)
        text_label=qg.QLabel('Total '+ str(obj_node_num) +' node(s) are selected')
        self.obj_list_layout.addWidget(text_label)

        for i in self.node_list:
            nodeList_wid_class_add = nodeList_wid_class(i)
            self.obj_list_layout.addWidget(nodeList_wid_class_add)



    def previewRename(self):
        get_name=self.rename_edit.text()
        for i in self.obj_list_widget.children():
            if type(i) == nodeList_wid_class or type(i)==qg.QLabel or type(i)==preview_nodeList_wid_class:
                i.deleteLater()

        obj_node_num=len(self.node_list)
        text_label=qg.QLabel('Total '+ str(obj_node_num) +' node(s) are selected')
        self.obj_list_layout.addWidget(text_label)

        for i in self.node_list:
            nodeList_wid_class_add = preview_nodeList_wid_class(i,get_name)
            self.obj_list_layout.addWidget(nodeList_wid_class_add)


    def renameAll(self):
        get_name=self.rename_edit.text()
        for i in self.node_list:
            node_type=cmds.nodeType(i)
            cmds.rename(i, get_name+'_'+node_type)








#---------------------------------------------------------------------------------------------------#
class nodeList_wid_class(qg.QWidget):
    def __init__(self,objNode):
        self.objNode=objNode
        #定義UI
        qg.QWidget.__init__(self)
        self.OutsideLayout=qg.QHBoxLayout()
        self.setLayout(self.OutsideLayout)
        self.layout().setAlignment(qc.Qt.AlignTop)
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setSpacing(0)

        #定義路徑欄UI
        node_type=cmds.nodeType(self.objNode)
        self.obj_founded_label = qg.QLabel(str(self.objNode)+'  ('+node_type+')')
        self.layout().addWidget(self.obj_founded_label)


class preview_nodeList_wid_class(qg.QWidget):
    def __init__(self,objNode,name):
        self.objNode=objNode
        self.name=name
        #定義UI
        qg.QWidget.__init__(self)
        self.OutsideLayout=qg.QHBoxLayout()
        self.setLayout(self.OutsideLayout)
        self.layout().setAlignment(qc.Qt.AlignTop)
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setSpacing(0)

        #定義路徑欄UI
        node_type=cmds.nodeType(self.objNode)
        self.obj_founded_label = qg.QLabel(str(self.objNode)+'  ('+node_type+')')
        self.obj_rename_label = qg.QLabel('----> '+str(self.name)+'_'+node_type)
        self.layout().addWidget(self.obj_founded_label)
        self.layout().addWidget(self.obj_rename_label)

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


def shader_renameMain():
    global dialog
    if dialog is None:
        dialog =Black_UI()
    dialog.show()