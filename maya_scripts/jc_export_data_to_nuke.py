import maya.cmds as cmds
import maya.mel as mel
import pickle
import json

def getPasses():
    passes = mel.eval('rmanGetOutputs rmanFinalGlobals')
    renderPasses = []
    for passe in passes:
        output = mel.eval('getAttr("' + passe + '.rman__riopt__Display_mode")')
        compute = bool(mel.eval('getAttr("' + passe + '.rman__torattr___computeBehavior")'))
        data = {'name':output, 'compute':compute}
        renderPasses.append(data)
    return renderPasses


def getRenderLayers():
    renderLayers = cmds.ls(type='renderLayer')
    renderLayerData = []
    for renderLayer in renderLayers:
        renderable = cmds.getAttr(renderLayer + '.renderable')
        if 'defaultRenderLayer' in renderLayer and len(renderLayers) == 1:
            cmds.editRenderLayerGlobals(currentRenderLayer=renderLayer)
            renderPasses = getPasses()
            data = {'name':renderLayer,'renderAble':renderable, 'passes':renderPasses}
            renderLayerData.append(data)                
        elif 'defaultRenderLayer' not in renderLayer:
            cmds.editRenderLayerGlobals(currentRenderLayer=renderLayer)
            renderPasses = getPasses()
            data = {'name':renderLayer,'renderAble':renderable, 'passes':renderPasses}
            renderLayerData.append(data)    
    return renderLayerData

def exportCamera():
    defaultCamera = ['frontShape', 'perspShape', 'sideShape', 'topShape']
    cameras = [cam.replace("Shape","") for cam in cmds.ls(type='camera') if cam not in defaultCamera]
    cmds.select(None)
    for cam in cameras:
        cmds.select(cam, add=True)

    fbxExportPreset = "\"//Art-1405260002/d/assets/scripts/maya_scripts/presets/ExportCamera.fbxexportpreset\""
    mel.eval('FBXLoadExportPresetFile -f ' + fbxExportPreset)
    
    basePath = cmds.workspace( q=True, rd=True )
    cameraPath = basePath + "data/export/cameras.fbx" 
    mel.eval('file -force -options "" -typ "FBX export" -pr -es "' + cameraPath + '"')
    return cameras

def exportData():
    renderLayerData = getRenderLayers()
    startFrame = cmds.getAttr('defaultRenderGlobals.startFrame')
    endFrame = cmds.getAttr('defaultRenderGlobals.endFrame')
    sceneName = cmds.file(q=True, sceneName=True).split("/")[-1].split(".")[0]
    cameras = exportCamera()
    currentPath = cmds.file(q=True, sn=True).replace("/scenes/" + sceneName+".mb","")
    periodInExt = cmds.getAttr('defaultRenderGlobals.periodInExt')
    if periodInExt == 1:
        periodInExt = "."
    else:
        periodInExt = "_"        
    frameBeforeExt = cmds.getAttr('defaultRenderGlobals.putFrameBeforeExt')
    imageFilePrefix = cmds.getAttr('defaultRenderGlobals.imageFilePrefix')        

    renderData = {'name':sceneName, 'currentPath':currentPath, 'start':startFrame, 'end': endFrame, 'renderLayers': renderLayerData, 'cameras': cameras, 'periodInExt': periodInExt, 'frameBeforeExt': frameBeforeExt, 'imageFilePrefix': imageFilePrefix}        

    projectPath = cmds.workspace(q = True, rd=True)
    jsonData = json.dumps(renderData)
    jsonFilePath = "%s/images/%s.json" % (projectPath, sceneName)
    json_file = open(jsonFilePath, 'w')
    json_file.write(jsonData + "\n")
    json_file.close()
    print "----------------------------------------\n\nData Exported to:\n" + jsonFilePath +"\n\n----------------------------------------"
    return jsonData

def jc_export_data_to_nukeMain():
    exportData()

if __name__ == "__main__":
    exportData()

    
