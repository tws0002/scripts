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
        self.setWindowTitle('pxrFastRender'+' v1.0'+u' by 小黑')
        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setModal(False)
        self.resize(600,480)
        self.setLayout(qg.QVBoxLayout())
        self.layout().setAlignment(qc.Qt.AlignTop)
        self.evnSet_lb=qg.QLabel('select light set : ')

        #參數定義
        cmds.loadPlugin('RenderMan_for_Maya',qt=True)
        self.nameSpace='lightHdrSys'
        self.nameSpaceFull=self.nameSpace+':'
        self.img_fold = r"\\ART-RENDER\art_3d_project\maya_asset_globle\casino\introduction\light_hdr\concept\sourceimages\shaderLookDev\HDRI"
        self.key_light_dic={'name':'key light','transform':'look_dev_key','shape':'look_dev_keyShape'}
        self.fill_light_dic={'name':'fill light','transform':'look_dev_fill','shape':'look_dev_fillShape'}
        self.back_light_dic={'name':'back light','transform':'look_dev_back','shape':'look_dev_backShape'}
        self.env_light_dic={'name':'env light','transform':'look_dev_env','shape':'look_dev_envShape'}
        self.mbFile=r'\\art-render\art_3d_project\maya_asset_globle\casino\introduction\light_hdr\concept\scenes\mag_i_light_hdr_master.mb'

        #定義上方按鈕UI
        top_button_layout = qg.QHBoxLayout()
        create_light_button = qg.QPushButton('Create HDR')
        create_light_button.clicked.connect(self.lightFinalCheck)
        delete_node_button = qg.QPushButton('Delete HDR')
        delete_node_button.clicked.connect(self.deleteHdrNode)
        select_node_button = qg.QPushButton('Select Camera')
        select_node_button.clicked.connect(self.selectCamNode)
        top_button_layout.addWidget(create_light_button)
        top_button_layout.addWidget(delete_node_button)
        top_button_layout.addWidget(select_node_button)

        self.layout().addLayout(top_button_layout)

        #分隔線
        line=qg.QFrame()
        line.setFrameStyle(qg.QFrame.HLine)
        self.layout().addWidget(line)

        #定義燈光列表框
        self.lightListWidget = qg.QWidget()
        self.lightListWidget.setLayout(qg.QVBoxLayout())
        self.lightListWidget.layout().setAlignment(qc.Qt.AlignTop)
        self.lightListWidget.layout().setContentsMargins(0,0,0,0)
        self.lightListWidget.layout().setSpacing(0)
        self.layout().addWidget(self.lightListWidget)


    def selectCamNode(self):
        cmds.select(self.nameSpaceFull+'look_dev_cam')

    def deleteHdrNode(self):
        if cmds.namespace(exists=self.nameSpace)==True:
            nodeList=cmds.ls( self.nameSpaceFull+'*')
            for node in nodeList:
                try:
                    cmds.delete(node)
                except:
                    pass

        if cmds.namespace(exists=self.nameSpace):
            cmds.namespace(rm=self.nameSpace)


        self.mainWidget.deleteLater()

    def lightFinalCheck(self):
        u'''創建內嵌式列表'''

        if cmds.namespace(exists=self.nameSpace)==False:
            self.nameSpaceFull=''
        try:
            self.mainWidget.deleteLater()
        except:
            pass

        if cmds.objExists(self.nameSpaceFull+'look_dev_grp')==False:
            cmds.file( self.mbFile,i=1,ra=True,ns=self.nameSpace,mnc=True)
            self.nameSpaceFull=self.nameSpace+':'


        #資訊欄總介面
        self.mainWidget = qg.QWidget()
        self.mainWidget.setLayout(qg.QVBoxLayout())
        self.mainWidget.layout().setAlignment(qc.Qt.AlignCenter)
        self.mainWidget.layout().setContentsMargins(0,0,0,0)
        #HDR滑動介面
        self.pathListWidget = qg.QWidget()
        self.pathListLayout = qg.QHBoxLayout()
        self.pathListLayout.setContentsMargins(0,0,0,0)
        self.pathListLayout.setAlignment(qc.Qt.AlignTop)
        self.pathListWidget.setLayout(self.pathListLayout)
        pathListScrollArea = qg.QScrollArea()
        pathListScrollArea.setWidgetResizable(True)
        pathListScrollArea.setWidget(self.pathListWidget)
        self.mainWidget.layout().addWidget(pathListScrollArea)
        for img in os.listdir(self.img_fold):
            img_ext=os.path.splitext(img)[1]
            img_path = os.path.join(self.img_fold, img)
            if img_ext=='.jpg':
                self.pathListLayout.addWidget(hdrImages(img_path,self.img_fold,self.env_light_dic['shape']))
            else:
                pass
        self.lightListWidget.layout().addWidget(self.mainWidget)

        #顯示開關介面
        self.vis_widget = qg.QWidget()
        self.vis_widget.setLayout(qg.QHBoxLayout())
        self.vis_widget.layout().setContentsMargins(0,0,0,0)
        self.vis_widget.layout().setAlignment(qc.Qt.AlignTop)
        #self.vis_widget.layout().setSpacing(0)
        self.vis_widget.layout().addWidget(vis_CB_class('Ground','swatch_backdrop.visibility'))
        #地板格線
        ground_gird_combo=qg.QComboBox()
        ground_gird_combo.addItem('no gird')
        ground_gird_combo.addItem('gird')
        ground_gird_value=cmds.getAttr(self.nameSpaceFull+'grund_grid_PxrLMLayer.layerMask')
        if ground_gird_value==0:
            ground_gird_combo.setCurrentIndex(0)
        else:
            ground_gird_combo.setCurrentIndex(1)
        ground_gird_combo.currentIndexChanged.connect(self.set_grid)
        self.vis_widget.layout().addWidget(ground_gird_combo)

        self.vis_widget.layout().addWidget(vis_CB_class('Teapot','Teapot_grp.visibility'))
        self.vis_widget.layout().addWidget(vis_CB_class('relfBall','lookDevSphereChrome.visibility'))
        self.vis_widget.layout().addWidget(vis_CB_class('whiteBall','lookDevSphereMatte.visibility'))
        self.vis_widget.layout().addWidget(vis_CB_class('colorCard','colorCard_mesh.visibility'))
        self.vis_widget.layout().addWidget(vis_CB_class('envPrimary','look_dev_envShape.rman__LightPrimaryVisibility'))
        self.mainWidget.layout().addWidget(self.vis_widget)

        self.renderSet_widget = qg.QWidget()
        self.renderSet_widget.setLayout(qg.QHBoxLayout())
        self.renderSet_widget.layout().setContentsMargins(0,0,0,0)
        self.renderSet_widget.layout().setAlignment(qc.Qt.AlignTop)

        #Render Size
        renderSize_lb=qg.QLabel('Render Size W*H:')
        self.renderSet_widget.layout().addWidget(renderSize_lb)
        resWidth_edit=attr_edit_class('defaultResolution.width')
        resWidth_edit.textEdited.connect(self.setDevice_Aspect_Ratio)
        resHeight_edit=attr_edit_class('defaultResolution.height')
        resHeight_edit.textEdited.connect(self.setDevice_Aspect_Ratio)
        self.renderSet_widget.layout().addWidget(resWidth_edit)
        self.renderSet_widget.layout().addWidget(resHeight_edit)

        #SetLookDecCam
        setCamRen_button = qg.QPushButton('Set LookDevCam')
        setCamRen_button.clicked.connect(self.setRenderCam)
        self.renderSet_widget.layout().addWidget(setCamRen_button)

        #Render Resolution
        render_res_lb=qg.QLabel('Test Resolution :')
        render_res_combo=qg.QComboBox()
        render_res_combo.addItem('100%')
        render_res_combo.addItem('75%')
        render_res_combo.addItem('50%')
        render_res_combo.addItem('25%')
        render_res_combo.addItem('10%')
        render_res_combo.currentIndexChanged.connect(self.set_resolusion)
        currentRes=pm.mel.eval('optionVar -q renderViewTestResolution')
        if currentRes==1:
            render_res_combo.setCurrentIndex(0)
        elif currentRes==5:
            render_res_combo.setCurrentIndex(1)
        elif currentRes==4:
            render_res_combo.setCurrentIndex(2)
        elif currentRes==3:
            render_res_combo.setCurrentIndex(3)
        elif currentRes==2:
            render_res_combo.setCurrentIndex(4)
        self.renderSet_widget.layout().addWidget(render_res_lb)
        self.renderSet_widget.layout().addWidget(render_res_combo)
        self.mainWidget.layout().addWidget(self.renderSet_widget)




        #全局控制介面
        self.global_ctrl_widget = qg.QWidget()
        self.global_ctrl_widget.setLayout(qg.QGridLayout())
        self.global_ctrl_widget.layout().setAlignment(qc.Qt.AlignTop)
        self.global_ctrl_widget.layout().setContentsMargins(0,0,0,0)

        y_rotate_lb=qg.QLabel('Rotate Y')
        y_rotate_slider_widget = qg.QWidget()
        y_rotate_slider_widget.setLayout(qg.QHBoxLayout())
        y_rotate_slider_widget.layout().setAlignment(qc.Qt.AlignCenter)
        y_rotate_slider_widget.layout().setContentsMargins(0,0,0,0)
        y_rotate_slider_widget.layout().setSpacing(0)

        self.y_rotate_slider = qg.QSlider()
        self.y_rotate_slider.setOrientation(qc.Qt.Horizontal)
        self.y_rotate_slider.setRange(0, 360)
        self.y_rotate_spin = qg.QSpinBox()
        self.y_rotate_spin.setRange(0, 360)
        y_rotate_slider_widget.layout().addWidget(self.y_rotate_slider)
        y_rotate_slider_widget.layout().addWidget(self.y_rotate_spin)

        self.y_rotate_slider.valueChanged.connect(self.y_rotate_spin.setValue)
        self.y_rotate_spin.valueChanged.connect(self.y_rotate_slider.setValue)
        angle = cmds.getAttr(self.nameSpaceFull+self.env_light_dic['transform']+'.rotateY')
        self.y_rotate_spin.setValue(angle)
        self.y_rotate_spin.valueChanged.connect(self.set_y_rotate)
        self.global_ctrl_widget.layout().addWidget(y_rotate_lb,0,0)
        self.global_ctrl_widget.layout().addWidget(y_rotate_slider_widget,0,1)


        globals_scale_lb=qg.QLabel('Globals Scale')
        self.global_ctrl_widget.layout().addWidget(globals_scale_lb,1,0)
        globals_scale_slider=float_slider_class('look_dev_grp.scale',1,10,10,100)
        globals_scale_slider.spin.valueChanged.connect(self.set_light_intensity)
        self.global_ctrl_widget.layout().addWidget(globals_scale_slider,1,1)

        self.mainWidget.layout().addWidget(self.global_ctrl_widget)
        line=qg.QFrame()
        line.setFrameStyle(qg.QFrame.HLine)
        self.mainWidget.layout().addWidget(line)


        #燈光個別控制介面
        self.light_ctrl_widget = qg.QWidget()
        self.light_ctrl_widget.setLayout(qg.QGridLayout())
        self.light_ctrl_widget.layout().setAlignment(qc.Qt.AlignTop)
        self.light_ctrl_widget.layout().setContentsMargins(0,0,0,0)
        light_lb = qg.QLabel('Light Name')
        diffuse_lb = qg.QLabel('Diffuse Weight')
        diffuse_lb.setAlignment(qc.Qt.AlignCenter)
        specular_lb  = qg.QLabel('Specular Weight')
        specular_lb.setAlignment(qc.Qt.AlignCenter)

        key_light_lb = lightName_label(self.key_light_dic['name'],self.key_light_dic['transform'])
        fill_light_lb = lightName_label(self.fill_light_dic['name'],self.fill_light_dic['transform'])
        back_light_lb  = lightName_label(self.back_light_dic['name'],self.back_light_dic['transform'])
        env_light_lb  = lightName_label(self.env_light_dic['name'],self.env_light_dic['transform'])

        self.light_ctrl_widget.layout().addWidget(light_lb,   0, 0)
        self.light_ctrl_widget.layout().addWidget(diffuse_lb,   0, 1)
        self.light_ctrl_widget.layout().addWidget(specular_lb,   0, 2)
        self.light_ctrl_widget.layout().addWidget(key_light_lb,   1, 0)
        self.light_ctrl_widget.layout().addWidget(fill_light_lb,   2, 0)
        self.light_ctrl_widget.layout().addWidget(back_light_lb,   3, 0)
        self.light_ctrl_widget.layout().addWidget(env_light_lb,   4, 0)

        self.light_ctrl_widget.layout().addWidget(float_slider_class(self.key_light_dic['shape']+'.diffAmount',0,1,0,100),1,1)
        self.light_ctrl_widget.layout().addWidget(float_slider_class(self.key_light_dic['shape']+'.specAmount',0,1,0,100),1,2)
        self.light_ctrl_widget.layout().addWidget(float_slider_class(self.fill_light_dic['shape']+'.diffAmount',0,1,0,100),2,1)
        self.light_ctrl_widget.layout().addWidget(float_slider_class(self.fill_light_dic['shape']+'.specAmount',0,1,0,100),2,2)
        self.light_ctrl_widget.layout().addWidget(float_slider_class(self.back_light_dic['shape']+'.diffAmount',0,1,0,100),3,1)
        self.light_ctrl_widget.layout().addWidget(float_slider_class(self.back_light_dic['shape']+'.specAmount',0,1,0,100),3,2)
        self.light_ctrl_widget.layout().addWidget(float_slider_class(self.env_light_dic['shape']+'.diffAmount',0,1,0,100),4,1)
        self.light_ctrl_widget.layout().addWidget(float_slider_class(self.env_light_dic['shape']+'.specAmount',0,1,0,100),4,2)
        self.mainWidget.layout().addWidget(self.light_ctrl_widget)


    def set_y_rotate(self,value):
        cmds.setAttr(self.nameSpaceFull+self.env_light_dic['transform']+'.rotateY', value )

    def set_light_intensity(self,value):
        scale_intensity=value*value
        cmds.setAttr( self.nameSpaceFull+'scale_keyLight_multiplyDivide.input2',scale_intensity, scale_intensity, scale_intensity,type="double3")
        cmds.setAttr( self.nameSpaceFull+'scale_fillLight_multiplyDivide.input2',scale_intensity, scale_intensity, scale_intensity,type="double3")
        cmds.setAttr( self.nameSpaceFull+'scale_backLight_multiplyDivide.input2',scale_intensity, scale_intensity, scale_intensity,type="double3")
        cameraFar=value*100
        cmds.setAttr( self.nameSpaceFull+'look_dev_camShape.farClipPlane',cameraFar)
    def setRenderCam(self):
        cameraList=cmds.ls(type='camera')
        for camera in cameraList:
            cmds.setAttr( camera+'.renderable',0)
        cmds.setAttr( dialog.nameSpaceFull+'look_dev_camShape'+'.renderable',1)
    def setDevice_Aspect_Ratio(self):
        width=cmds.getAttr('defaultResolution.width')
        height=cmds.getAttr('defaultResolution.height')
        cmds.setAttr('defaultResolution.deviceAspectRatio',float(width)/float(height))
        cmds.setAttr('defaultResolution.deviceAspectRatio',float(width)/float(height))

    def set_resolusion(self,index):
        if index==0:
            pm.mel.eval('setTestResolutionVar(1)')
        elif index==1:
            pm.mel.eval('setTestResolutionVar(5)')
        elif index==2:
            pm.mel.eval('setTestResolutionVar(4)')
        elif index==3:
            pm.mel.eval('setTestResolutionVar(3)')
        elif index==4:
            pm.mel.eval('setTestResolutionVar(2)')

    def set_grid(self,index):
        if index==0:
            cmds.setAttr(self.nameSpaceFull+'grund_grid_PxrLMLayer.layerMask',0)
        else:
            cmds.setAttr(self.nameSpaceFull+'grund_grid_PxrLMLayer.layerMask',1)






#---------------------------------------------------------------------------------------------------#

class hdrImages(qg.QWidget):
    def __init__(self,jpg_path,img_fold,shape):
        '''建立HDR縮圖'''
        self.jpg_path=jpg_path
        self.img_fold=img_fold
        self.shape=shape
        qg.QWidget.__init__(self)
        self.setLayout(qg.QVBoxLayout())
        self.layout().setAlignment(qc.Qt.AlignCenter)
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setSpacing(0)
        pixmap = qg.QPixmap(self.jpg_path)
        lbl = qg.QLabel()
        lbl.setPixmap(pixmap)
        self.layout().addWidget(lbl)
        lbl.mousePressEvent = self.clickedEvent
        img_name=os.path.basename(self.jpg_path).replace('_preview','')
        self.img_name_fix=os.path.splitext(img_name)[0]
        img_name_lb = qg.QLabel(self.img_name_fix)
        img_name_lb.setAlignment(qc.Qt.AlignCenter)
        self.layout().addWidget(img_name_lb)


    def clickedEvent(self,event):
        '''點擊觸發'''
        img_exr_name=self.img_name_fix+'.hdr'
        exr_path=os.path.join(self.img_fold, img_exr_name)
        cmds.setAttr( dialog.nameSpaceFull+self.shape+'.rman__EnvMap', exr_path,type="string" )

class vis_CB_class(qg.QCheckBox):
    def __init__(self,name,attr):
        self.name=name
        self.attr=attr
        qg.QCheckBox.__init__(self)
        self.setText(self.name)
        vis = cmds.getAttr(dialog.nameSpaceFull+self.attr)
        if vis==True:
            self.setChecked(True)
        else:
            self.setChecked(False)
        self.stateChanged.connect(self.CB_hit)
    def CB_hit(self,state):
        '''狀態變更觸發'''
        if state == qc.Qt.Checked:
            cmds.setAttr( dialog.nameSpaceFull+self.attr, True )
        else:
            cmds.setAttr( dialog.nameSpaceFull+self.attr, False )







class lightName_label(qg.QLabel):
    def __init__(self,name,lightShape):
        '''建立有滑鼠觸發功能的label'''
        self.name=name
        self.lightShape=lightShape
        qg.QLabel.__init__(self)
        self.setText(self.name)
    def mousePressEvent(self,e):
        cmds.select(dialog.nameSpaceFull+self.lightShape)
    def leaveEvent(self,e):
        self.setStyleSheet("font:;color: rgb(255, 255, 255);")
    def enterEvent(self,e):
        self.setStyleSheet("font: bold;color: rgb(0, 255, 0);")


class float_slider_class(qg.QWidget):
    def __init__(self,lightAttr,spinMin,spinMax,sliderMin,sliderMax):
        '''可以使用小數點的拉霸'''
        self.lightAttr=lightAttr
        self.spinMin=spinMin
        self.spinMax=spinMax
        self.spinGap=spinMax-spinMin
        self.sliderMin=sliderMin
        self.sliderMax=sliderMax
        self.sliderGap=self.sliderMax-self.sliderMin
        qg.QWidget.__init__(self)
        self.setLayout(qg.QHBoxLayout())
        self.layout().setAlignment(qc.Qt.AlignCenter)
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setSpacing(0)

        self.slider = qg.QSlider()
        self.slider.setOrientation(qc.Qt.Horizontal)
        self.slider.setRange(self.sliderMin,self.sliderMax)
        self.spin = qg.QDoubleSpinBox()
        self.spin.setRange(self.spinMin,self.spinMax)
        self.spin.setSingleStep(0.1)

        self.slider.valueChanged.connect(self.convertSpin)
        self.spin.valueChanged.connect(self.convertSlider)
        self.spin.valueChanged.connect(self.setContribution)
        ShapeValue = cmds.getAttr(dialog.nameSpaceFull+self.lightAttr)
        self.spin.setValue(ShapeValue[0][0])

        self.layout().addWidget(self.slider)
        self.layout().addWidget(self.spin)

    def convertSpin(self,value):
        num=float(value-self.sliderMin)/self.sliderGap*self.spinGap+self.spinMin
        self.spin.setValue(num)

    def convertSlider(self,value):
        num=int((value-self.spinMin)/self.spinGap*self.sliderGap+self.sliderMin)
        self.slider.setValue(num)

    def setContribution(self,value):
        cmds.setAttr( dialog.nameSpaceFull+self.lightAttr,value, value, value,type="double3" )


class attr_edit_class(qg.QLineEdit):
    def __init__(self,attrEdit):
        self.attrEdit=attrEdit
        qg.QLineEdit.__init__(self)
        currentAttr=cmds.getAttr(self.attrEdit)
        self.setText(str(currentAttr))
        self.reg_ex=qc.QRegExp("[0-9]+")
        self.text_validator=qg.QRegExpValidator(self.reg_ex,self)
        self.setValidator(self.text_validator)
        self.textEdited.connect(self.text_hit)
    def text_hit(self):
        newText=self.text()
        cmds.setAttr(self.attrEdit, int(newText) )


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

def pxrFastRenderMain():
    global dialog
    if dialog is None:
        dialog =Black_UI()
    dialog.show()


