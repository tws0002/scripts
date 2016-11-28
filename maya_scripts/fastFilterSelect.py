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
        self.setWindowTitle('Fast Filter Select'+' v1.0'+u' by 小黑')
        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setModal(False)
        self.resize(600,480)
        self.setLayout(qg.QVBoxLayout())
        self.layout().setAlignment(qc.Qt.AlignTop)

        #定義上方UI
        top_button_layout = qg.QHBoxLayout()
        top_button_layout.setContentsMargins(0,0,0,0)
        get_type_but = qg.QPushButton('show the type of the selected obj')
        get_type_but.clicked.connect(self.showType)
        self.found_type_edit=qg.QLineEdit()
        top_button_layout.addWidget(get_type_but)
        top_button_layout.addWidget(self.found_type_edit)
        self.layout().addLayout(top_button_layout)

        line=qg.QFrame()
        line.setFrameStyle(qg.QFrame.HLine)
        self.layout().addWidget(line)

        #定義中間文字
        setting_text_layout = qg.QHBoxLayout()
        setting_text_layout.setAlignment(qc.Qt.AlignCenter)
        setting_text_label=qg.QLabel('Condition Settings  : ')
        setting_text_layout.addWidget(setting_text_label)
        self.layout().addLayout(setting_text_layout)

        #定義輸入欄位
        edit_conditions_layout = qg.QHBoxLayout()
        type_label=qg.QLabel('type : ')
        self.type_edit=qg.QLineEdit()
        prefix_label=qg.QLabel('prefix : ')
        self.prefix_edit=qg.QLineEdit()
        name_label=qg.QLabel('name : ')
        self.name_edit=qg.QLineEdit()
        suffix_label=qg.QLabel('suffix : ')
        self.suffix_edit=qg.QLineEdit()
        edit_conditions_layout.addWidget(type_label)
        edit_conditions_layout.addWidget(self.type_edit)
        edit_conditions_layout.addWidget(prefix_label)
        edit_conditions_layout.addWidget(self.prefix_edit)
        edit_conditions_layout.addWidget(name_label)
        edit_conditions_layout.addWidget(self.name_edit)
        edit_conditions_layout.addWidget(suffix_label)
        edit_conditions_layout.addWidget(self.suffix_edit)
        self.layout().addLayout(edit_conditions_layout)


        #定案按鈕
        search_button_layout = qg.QHBoxLayout()
        search_but = qg.QPushButton('search object')
        search_button_layout.addWidget(search_but)
        search_but.clicked.connect(self.searchObj)
        self.layout().addLayout(search_button_layout)


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
        set_all_on_but = qg.QPushButton('Set all on')
        set_all_on_but.clicked.connect(self.setAllOn)
        set_all_off_but = qg.QPushButton('Set all off')
        set_all_off_but.clicked.connect(self.setAllOff)
        sel_obj_but = qg.QPushButton('Seletct Node')
        sel_obj_but.clicked.connect(self.selectNode)

        buttonLayout.addWidget(set_all_on_but)
        buttonLayout.addWidget(set_all_off_but)
        buttonLayout.addWidget(sel_obj_but)
        self.layout().addWidget(buttonWidget)

#---------------------------------------------------------------------------------------------------#
    def showType(self):
        object_selected=cmds.ls( selection=True, tail=1,dag=True)
        if len(object_selected) >0:
            if cmds.nodeType(object_selected[0])=='transform':
                obj_shape=cmds.listRelatives(object_selected[0], shapes=True)
                obj_type=cmds.nodeType(obj_shape[0])
                self.found_type_edit.setText(obj_shape[0]+' type is '+obj_type)
            else:
                obj_type=cmds.nodeType(object_selected[0])
                self.found_type_edit.setText(object_selected[0]+' type is '+obj_type)

        else:
            self.found_type_edit.setText('selected : None')

    def filterPrefix(self,obj_list):
        filter_obj=[]
        get_prefix=self.prefix_edit.text()
        if get_prefix!='':
            for i in obj_list:
                if i[0:len(get_prefix)] == get_prefix:
                    filter_obj.append(i)
            return filter_obj
        else:
            return obj_list


    def filterName(self,obj_list):
        filter_obj=[]
        get_name=self.name_edit.text()
        if get_name!='':
            for i in obj_list:
                if get_name in i:
                    filter_obj.append(i)
            return filter_obj
        else:
            return obj_list


    def filterSuffix(self,obj_list):
        filter_obj=[]
        get_suffix=self.suffix_edit.text()
        if get_suffix!='':
            for i in obj_list:
                if i[len(i)-len(get_suffix):len(i)] == get_suffix:
                    filter_obj.append(i)
            return filter_obj
        else:
            return obj_list




    def filterType(self,obj_list):
        filter_obj=[]
        get_type=self.type_edit.text()
        if get_type!='':
            for i in obj_list:
                if cmds.nodeType(i)==get_type:
                    filter_obj.append(i)
            return filter_obj
        else:
            return obj_list



    def selectNode(self):
        u'''點擊選擇按鈕觸發'''
        pm.select(self.check_obj_list)


    def setAllOn(self):
        u'''點擊設定全部按鈕觸發'''
        for i in self.obj_list_widget.children():
            if type(i) == nodeList_wid_class:
                i.obj_founded_CB.setChecked(True)

    def setAllOff(self):
        u'''點擊設定全部取消按鈕觸發'''
        for i in self.obj_list_widget.children():
            if type(i) == nodeList_wid_class:
                i.obj_founded_CB.setChecked(False)


    def creatList(self):
        u'''找出符合條件的物件'''
        all_object=cmds.ls()
        filter_obj=self.filterType(all_object)
        filter_obj=self.filterPrefix(filter_obj)
        filter_obj=self.filterName(filter_obj)
        filter_obj=self.filterSuffix(filter_obj)
        filter_obj.sort()
        return filter_obj


    def searchObj(self):
        self.check_obj_list=[]
        chek_condition=True
        if self.type_edit.text()=='' and self.prefix_edit.text()=='' and self.name_edit.text()=='' and self.suffix_edit.text()=='':
            chek_condition=False


        #刪除列表
        for i in self.obj_list_widget.children():
            if type(i) == nodeList_wid_class or type(i)==qg.QLabel:
                i.deleteLater()
        if chek_condition==True:
            filter_obj=self.creatList()
            obj_node_num=len(filter_obj)
            text_label=qg.QLabel('Total '+ str(obj_node_num) +' object(s) are founded')
            self.obj_list_layout.addWidget(text_label)

            for i in filter_obj:
                nodeList_wid_class_add = nodeList_wid_class(i)
                self.obj_list_layout.addWidget(nodeList_wid_class_add)
        else:
            text_label=qg.QLabel('Please input conditions and try again.')
            self.obj_list_layout.addWidget(text_label)








#---------------------------------------------------------------------------------------------------#
class nodeList_wid_class(qg.QWidget):
    def __init__(self,objNode):
        self.objNode=objNode
        #定義UI
        qg.QWidget.__init__(self)
        self.OutsideLayout=qg.QVBoxLayout()
        self.setLayout(self.OutsideLayout)
        self.layout().setAlignment(qc.Qt.AlignTop)
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setSpacing(0)

        #定義路徑欄UI
        self.obj_founded_CB = qg.QCheckBox(self.objNode)
        self.layout().addWidget(self.obj_founded_CB)
        self.obj_founded_CB.stateChanged.connect(self.node_hit)

    def node_hit(self,state):
        u'''點擊按鈕觸發'''
        if state == qc.Qt.Checked:
            if self.objNode not in dialog.check_obj_list:
                dialog.check_obj_list.append(self.objNode)
            pm.select(self.objNode)

        else:
            if self.objNode in dialog.check_obj_list:
                dialog.check_obj_list.remove(self.objNode)
            pass

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


def fastFilterSelectMain():
    global dialog
    if dialog is None:
        dialog =Black_UI()
    dialog.show()