'''
nuke autocomper using data generated in maya/renderman21, to be used in conjunction with
jc_export_data_to_nuke.py
run this with 64bit python only
'''
import time
import json
import sys
print len(sys.argv)
time.sleep(5)
if len(sys.argv) == 3:

    jsonData = sys.argv[1]
    compPath = sys.argv[2]

import re
import os
import random
import re


scripts_path = "//Art-1405260002/d/assets"
sys.path.append(scripts_path + "/scripts/nuke_scripts")
sys.path.append("c:/Program Files/Nuke10.0v2/lib/site-packages")
os.environ['NUKE_INTERACTIVE'] = "1"
try:
    import nuke
except:
    print 'Nuke Library Not Found'

# renderData is passed using json
class AutoComp(object):
    def __init__(self, jsonData):
        self.renderData = self.jsonToDict(jsonData)

        self.currentPath = self.renderData['currentPath']
        self.fileName = self.renderData['name']

        self.standardShadingStates = ['cpuTime', 'sampleCount', 'p', 'PRadius', 'Nn', 'Ngn', 'Tn', 'Vn', 'VLen', 'curvature', 'incidentRaySpread', 'mpSize', 'u', 'v', 'w', 'du', 'dv', 'dw', 'dPdtime', 'dufp', 'dvfp', 'dwfp', 'id', 'z' ]
        self.integrators = ['__Pworld', '__Nworld', '__depth', '__st', '__Pref', '__Nref', '__WPref', '__WNref']
        self.mattes = ['MatteId01', 'MatteId02', 'MatteId03', 'MatteId04', 'MatteId05', 'MatteId06', 'MatteId07']
        self.aovs = self.standardShadingStates + self.integrators + self.mattes

        #self.passTypes = ['diffuse', 'emission', 'indirectdiffuse', 'indirectspecular', 'reflectioncollection', 'refraction', 'shadowcollector', 'specular', 'subsurface']
        self.passTypes = ['diffuse', 'emission', 'indirectdiffuse', 'indirectspecular', 'reflectioncollection', 'refraction', 'shadowcollector', 'specular']

        self.advanced = False
        self.renderLayers = []
        self.readNodes = []
        self.beautyNodes = []
        self.lastNodes = []
        self.lightGroups = []
        self.copyNodes = []

        self.renderLayers = self.renderLayerData(self.renderData)
        self.autoComp(self.renderLayers)


    def jsonToDict(self, jsonData):
        renderData = json.loads(jsonData)
        return renderData
    # build data structure renderLayer from renderData
    def renderLayerData(self, renderData):
        fileName = renderData['name']
        start = renderData['start']
        end = renderData['end']
        sequenceNumberSeparator = renderData['periodInExt']
        renderLayers = []
        imageFilePrefix = renderData['imageFilePrefix'].split("/")

        for renderLayer in renderData['renderLayers']:
            if renderLayer['renderAble'] == True:
                renderPassData = []
                filenamePrefix = imageFilePrefix[-1].replace("<Scene>",fileName).replace("<RenderLayer>",renderLayer['name'])
                directorySuffix = ("/".join(imageFilePrefix[0:-1])).replace("<Scene>",fileName).replace("<RenderLayer>",renderLayer['name'])

                dirPath = "%s/images/%s" % (self.currentPath, directorySuffix)
                try:
                    files = [x for x in os.listdir(dirPath) if renderLayer['name'] in x]
                except:
                    files = []
                # if len(files) != 0:
                #     sequenceNumberSeparator = re.search('(.+?)(.)([0-9]{4}).exr',files[0]).group(2)
    
                for renderPass in renderLayer['passes']:
                    for passType in self.passTypes:
                        if passType in renderPass['name']:
                            self.advanced = True
                            break

                    renderPassFiles = []
                    if renderPass['compute'] == True:
                        for x,f in enumerate(files):
                            if ((renderLayer['name'] + "_" + renderPass['name'].replace(":","_")).replace("___","_") == f.split(".exr")[0][0:-5]):
                                renderPassFiles.append(f)
                            elif renderPass['name'] == 'rgba' and f.split(".")[0][0:-5] == renderLayer['name']:
                                renderPassFiles.append(f)
                        # try:
                        #     sequenceNumberSeparator = re.search('(.+?)(.)([0-9]{4}).exr',renderPassFiles[0]).group(2)
                        # except:
                        #     pass
                        renderPassData.append({'name':renderPass['name'],'compute':renderPass['compute'],'files':renderPassFiles})
                        renderPassFiles = []
                renderLayerdata = {'name':renderLayer['name'],'renderAble':renderLayer['renderAble'],'passes':renderPassData, 'start':start, 'end':end, 'path':dirPath, 'filenamePrefix': filenamePrefix, 'separator':sequenceNumberSeparator}
                renderLayers.append(renderLayerdata)
        return renderLayers


    def linkNodes(self, readNodes, lightName):
        goodColors = [2287951871, 2287957759, 2136967423, 2136967423, 1601145087, 1602783487, 1602777087, 1736990719, 2139643903, 2289524735]
        count = 0
        ycount = 0
        mergeCount = 0
        
        mergeNodes = []
        dotNodes = []
        group = ""


        for readNode, gradeNode in self.readNodes:
            # if simple skip beauty check, if advanced, need to check and ignore beauty pass
            #if readNode.name() == 'rgba' or 'beauty' in readNode.name():

            beautyLightName = 'lpe:beauty_' + lightName
            print beautyLightName
            if readNode.name() == 'rgba':
                count = count + 1
            elif readNode.name() == beautyLightName and self.advanced == True:
                count = count + 1
            elif readNode.name() in self.aovs or readNode.name() == 'lpe:beauty' :
                pass
            else:
                if len(dotNodes) == 0:
                    dotNode = nuke.nodes.Dot(inputs=[readNodes[count][1]])
                    dotNode.setXpos(gradeNode.xpos() + 35)
                    dotNode.setYpos(gradeNode.ypos() + 75 + 70*(ycount))
                    dotNodes.append(dotNode)

                else:
                    nukeNode = nuke.nodes.Merge(inputs=[dotNodes[mergeCount], readNodes[count][1]])
                    mergeNodes.append(nukeNode)
                    dotNode = nuke.nodes.Dot(inputs=[mergeNodes[mergeCount]])
                    dotNode.setXpos(gradeNode.xpos() + 35)
                    dotNode.setYpos(gradeNode.ypos() + 75 + 70*(ycount))
                    dotNodes.append(dotNode)
                    mergeCount = mergeCount + 1

                    nukeNode.setXpos(gradeNode.xpos())
                    nukeNode.setYpos(gradeNode.ypos() + 70 + 70*(ycount - 1))
                count = count + 1
                ycount = ycount + 1

        if self.advanced == True and len(readNodes) > 1:
            group = nuke.nodes.BackdropNode(name=lightName)
            group.knob("label").setValue("\n" + lightName)
            group.knob("note_font_size").setValue(200)
            group.knob("tile_color").setValue(goodColors[random.randint(0,9)])
            group.setXpos(readNodes[0][0].xpos() - 40)
            group.setYpos(readNodes[0][0].ypos() - 40)
            groupWidth = readNodes[-1][0].xpos() - readNodes[0][0].xpos() + 80*2
            groupHeight = readNodes[-1][0].ypos() - dotNodes[-1].ypos() + 80*2
            group.knob("bdwidth").setValue(groupWidth)
            group.knob("bdheight").setValue(dotNodes[-1].ypos() + 80*2)
        return [group, dotNodes[-1]]
        # elif len(readNodes) == 1:
        #     return [group, readNodes[0][1]]


    # connect light groups
    def linkLights(self, lastNodes):
        count = 0
        ycount = 0
        mergeCount = 0
        
        mergeNodes = []
        dotNodes = []
        #lastNodes[0][0].knob("bdheight").value()
        for group, lastNode in lastNodes:
            if len(dotNodes) == 0:
                dotNode = nuke.nodes.Dot(inputs=[lastNodes[count][1]])
                dotNode.setXpos(lastNode.xpos())
                dotNode.setYpos(lastNode.ypos() + 150 + 100*(ycount))
                dotNodes.append(dotNode)
            else:
                nukeNode = nuke.nodes.Merge(inputs=[dotNodes[mergeCount], lastNodes[count][1]])
                mergeNodes.append(nukeNode)
                dotNode = nuke.nodes.Dot(inputs=[mergeNodes[mergeCount]])
                dotNode.setXpos(lastNode.xpos())
                dotNode.setYpos(lastNode.ypos() + 150 + 100*(ycount))
                dotNodes.append(dotNode)
                mergeCount = mergeCount + 1
        
                nukeNode.setXpos(lastNode.xpos() - 35)
                nukeNode.setYpos(lastNode.ypos() + 150 + 100*(ycount - 1))
            count = count + 1
            ycount = ycount + 1    

    def linkBeauty(self, lastNodes, beautyNodes):
        count = 0
        ycount = 0
        mergeCount = 0

        mergeNodes = []
        dotNodes = []

        for readNode, gradeNode in beautyNodes:
            if len(dotNodes) == 0:
                dotNode = nuke.nodes.Dot(inputs=[beautyNodes[count][1]])

            else:
                nukeNode = nuke.nodes.Merge(inputs=[dotNodes[mergeCount], beautyNodes[count][1]])
                mergeNodes.append(nukeNode)
                dotNode = nuke.nodes.Dot(inputs=[mergeNodes[mergeCount]])

                mergeCount = mergeCount + 1
                nukeNode.setXpos(gradeNode.xpos())
                nukeNode.setYpos(lastNodes[count][1].ypos() + 150 + 100*(ycount))

            dotNode.setXpos(gradeNode.xpos() + 35)
            dotNode.setYpos(lastNodes[count][1].ypos() + 250 + 100*(ycount))
            dotNodes.append(dotNode)
            count = count + 1
            ycount = ycount + 1 

    def createReadNode(self, filePath, name, compute, start, end):
        readNode = nuke.nodes.Read(file=filePath, name=name)
        readNode.knob("first").setValue(int(start))
        readNode.knob("last").setValue(int(end))
        readNode.knob("disable").setValue(not compute)        
        if "subsurface" in readNode.name():
            readNode.knob("tile_color").setValue(2281721087)

        gradeNode = nuke.nodes.Grade(inputs=[readNode])
        gradeNode.setXpos(readNode.xpos())
        gradeNode.setYpos(readNode.ypos() + 150)

        #if name in self.aovs or 'lpe:beauty' in name:
        if 'lpe:beauty' in name:
            self.beautyNodes.append([readNode, gradeNode])

        self.readNodes.append([readNode, gradeNode])


    # build nodes
    def autoComp(self, renderLayers):
        for renderLayer in renderLayers:
            start = renderLayer['start']
            end = renderLayer['end']
            if renderLayer['renderAble'] == True:
                #imagesPath = "%s/images/%s/%s" % (self.currentPath, self.renderData['name'], renderLayer['name'])
                imagesPath = renderLayer['path']
                filenamePrefix = renderLayer['filenamePrefix']
                sequenceNumberSeparator = renderLayer['separator']

                auxs = []
                rgba = []

                for renderPass in renderLayer['passes']:
                    if 'beauty' in renderPass['name']:
                        try:
                            self.lightGroups.append(re.search('(lpe:beauty_)(.+)',renderPass['name']).group(2))
                        except:
                            pass
                    if renderPass['name'] == 'rgba':
                        filePath = "%s/%s%s####.exr" % (imagesPath, filenamePrefix, sequenceNumberSeparator)
                        rgba.append([filePath, renderPass['name'], renderPass['compute']])
                    elif renderPass['name'] in self.integrators or renderPass['name'] in self.standardShadingStates or "lpe:beauty" == renderPass['name']:
                        filePath = "%s/%s_%s%s####.exr" % (imagesPath, filenamePrefix, (renderPass['name'].replace(":","_")).replace("__",""), sequenceNumberSeparator)
                        auxs.append([filePath, renderPass['name'], renderPass['compute']])                        

                # group renderpasses by light names
                self.allLights = []
                for light in self.lightGroups:
                    lightRenderPasses = []
                    for renderPass in renderLayer['passes']:
                        if light in renderPass['name']:
                            lightRenderPasses.append(renderPass)
                        elif renderPass['name'] in self.aovs:
                            pass
                    data = {'name':light,'passes':lightRenderPasses}
                    self.allLights.append(data)

                # create the read nodes
                for light in self.allLights:
                    for renderPass in light['passes']:
                        print renderPass['name']
                        if renderPass['name'] == 'rgba':
                            filePath = "%s/%s%s####.exr" % (imagesPath, filenamePrefix, sequenceNumberSeparator)
                        else:
                            filePath = "%s/%s_%s%s####.exr" % (imagesPath, filenamePrefix, (renderPass['name'].replace(":","_")).replace("__",""), sequenceNumberSeparator)

                        self.createReadNode(filePath, renderPass['name'], renderPass['compute'], start, end)
                    if len(self.readNodes) > 1:
                        lastNode = self.linkNodes(self.readNodes, light['name'])  
                        self.lastNodes.append(lastNode)
                    if self.advanced:
                        self.readNodes = []          

                for aux in auxs:
                    self.createReadNode(aux[0], aux[1], aux[2], start, end)

                for beauty in rgba:
                    self.createReadNode(beauty[0], beauty[1], beauty[2], start, end)
                    #lastNode = self.linkNodes(self.readNodes, "")  
                    #self.lastNodes.append(lastNode)

                if self.advanced and len(self.lastNodes) > 1:   
                    self.linkLights(self.lastNodes)                 
                    self.linkBeauty(self.lastNodes, self.beautyNodes)

    def setCopy(self, copyNode, aov, channels):
        for x in range(0,channels):
            copyNode.knob(self.fromRGBA[x]).setValue('rgba.' + self.RGBA[x])
            copyNode.knob(self.toRGBA[x]).setValue(aov + '.' + self.RGBA[x])

    def linkAov(self, inputB, aov):
        copyNode = nuke.nodes.Copy(inputs=[inputB, self.aovNodes[aov]])
        self.copyNodes.append(copyNode)
        aovChannels = len(self.aovNodes[aov].channels())
        self.setCopy(copyNode, aov, aovChannels)    

    def relightComp(self):
        self.fromRGBA = ['from0', 'from1', 'from2', 'from3']
        self.toRGBA = ['to0', 'to1', 'to2', 'to3']
        self.RGBA = ['red','green','blue','alpha']
        
        self.aovNodes = {}
        # build an aov dictionary
        for readNode, gradeNodes in self.readNodes:
            if 'beauty' in readNode.name():
                self.aovNodes['beauty'] = readNode
            for aov in self.aovs:
                if readNode.name() == aov:
                    self.aovNodes[aov] = readNode
        
        # build the layers and channels
        for aovNode in self.aovNodes:
            channels = len(self.aovNodes[aovNode].channels())
            for x in range(0,channels):
                nuke.Layer(aovNode, [aovNode + "." + self.RGBA[x]])

        ypos = self.lastNodes[-1][1].ypos()
        self.linkAov(self.lastNodes[-1][1], '__Pworld')
        self.linkAov(self.copyNodes[-1], '__Nworld')
        self.linkAov(self.copyNodes[-1], 'z')

        pointCloudNode = nuke.nodes.PositionToPoints2(inputs=[self.copyNodes[-1]])
        pointCloudNode.knob('P_channel').setValue('__Pworld')
        pointCloudNode.knob('N_channel').setValue('__Nworld')
        pointCloudNode.setXpos(self.copyNodes[-1].xpos() + 140)
        pointCloudNode.setYpos(self.copyNodes[-1].ypos())

        defaultCameras = ['Producer Perspective', 'Producer Top', 'Producer Bottom', 'Producer Front', 'Producer Back', 'Producer Right', 'Producer Left']
        cameraPath = "%s/data/export/cameras.fbx" % self.currentPath
        cameraNode = nuke.nodes.Camera2(file=cameraPath, read_from_file=True)
        cameraName = [camera for camera in cameraNode.knob('fbx_node_name').values() if camera not in defaultCameras][0]
        cameraNode.knob('fbx_node_name').setValue(cameraName)
        cameraNode.setXpos(pointCloudNode.xpos() + 140)
        cameraNode.setYpos(pointCloudNode.ypos())

        lightNode = nuke.nodes.Light()
        lightNode.setXpos(cameraNode.xpos() + 140)
        lightNode.setYpos(cameraNode.ypos())
        
        sceneNode = nuke.nodes.Scene(inputs = [cameraNode, pointCloudNode, lightNode])
        sceneNode.setXpos(cameraNode.xpos())
        sceneNode.setYpos(cameraNode.ypos() + 140)
        
        phongNode = nuke.nodes.Phong()
        phongNode.setXpos(sceneNode.xpos())
        phongNode.setYpos(sceneNode.ypos() + 140)
        
        relightNode = nuke.nodes.ReLight()
        
        relightNode.connectInput(0,sceneNode)
        relightNode.connectInput(1,cameraNode)
        relightNode.connectInput(2,self.copyNodes[-1])
        relightNode.connectInput(0,phongNode)
        relightNode.knob('position').value()
        relightNode.knob('point')
        relightNode.knob('normal').setValue('__Nworld')
        relightNode.knob('position').setValue('__Pworld')
        relightNode.setXpos(pointCloudNode.xpos())
        relightNode.setYpos(sceneNode.ypos() + 140)
        
        keyerNode = nuke.nodes.Keyer(inputs=[relightNode])
        keyerNode.setYpos(relightNode.ypos() + 140)
        keyerNode.knob('operation').setValue('luminance key')
        
        colorCorrectNode = nuke.nodes.ColorCorrect(inputs=[self.copyNodes[-1], keyerNode ])
        colorCorrectNode.setXpos(self.copyNodes[-1].xpos())
        colorCorrectNode.setYpos(keyerNode.ypos() + 140)
        colorCorrectNode.knob('gain').setValue(5)

def main():
    comp = AutoComp(jsonData)
    print 'comp ok'
    time.sleep(5)
    try:
        comp.relightComp()
    except:
        print "relighting failed"
    nuke.scriptSave(compPath)
    os.system('complete')    

if __name__ == "__main__":
    main()


