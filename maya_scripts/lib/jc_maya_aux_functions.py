import os
from PySide import QtGui
app = QtGui.QApplication.instance()
try:
    appName = app.objectName()
except:
    appName = "StandAlone"

if appName == "maya":
    import maya.cmds as cmds
elif appName == "3dsmax":
    import MaxPlus


def uniDecode(chinese):
    return chinese.decode("utf-8")


def maxVersion(final_path, filename, mode):
    savedFiles = []
    versions = []
    if os.path.exists(final_path) is True:
        savedFiles = os.listdir(final_path)
        currentSceneReviewList = [x for x in savedFiles if filename in x]
        if len(currentSceneReviewList) == 0:
            maxversion = "v001"
        else:
            for savedFile in currentSceneReviewList:
                savedFile = savedFile.replace((filename + "_"), "")
                if mode == "maya":
                    version = savedFile.split(".")[0].split("_")[0]
                elif mode == "images":
                    version = savedFile.split(".")[0].split("_")[1]
                else:
                    version = savedFile.split(".")[0].split("_")[1]
                version = version.replace("v", "")
                versions.append(int(version))

                maxversion = "v" + str("%03d" % (max(versions) + 1))
    else:
        maxversion = "v001"
    return maxversion


def abbrName(name):
    def hasNumbers(inputString):
        return any(char.isdigit() for char in inputString)

    conjunction = ['and', 'the', 'or', 'of']
    name = name.lower()
    name = name.replace(" ", "")
    words = name.split("_")
    final = ""
    if len(words) < 2:
        if len(words[0]) < 5:
            final = words[0]
        else:
            final = words[0][:3]

    elif len(words) < 3 and words[1] == "cf":
        if len(words[0]) < 5:
            final = words[0] + "_cf"
        elif len(words[0]) > 4:
            final = words[0][:3] + "_cf"

    else:
        for word in words:
            if word[0] == "v" and hasNumbers(word[1]) and hasNumbers(word[2]):
                char = "_" + word
            elif word == "cf":
                char = "_cf"
            else:
                if words[1][0] == "v":
                    char = word[:3]
                elif len(word) < 3 and (word not in conjunction):
                    char = word
                else:
                    char = word[0]
            final = final+char
    return final


def abbrItemType(name):
    name = name.lower()
    name = name.replace(" ", "")
    words = name.split("_")
    final = ""
    for word in words:
        char = word[0]
        final = final+char
    return final
# git tests

# This looks at the scene path, splits the information packed in the scene path and scene name and returns it as an array.
# Alternately, it looks at a text file containing recent files and returns the same set of information


def getNextFileName(current):
    app = QtGui.QApplication.instance()
    base_path = "//art-render/art_3d_project/"
    appName = app.objectName()
    recent_files = []
    if current == 1:  # get from api
        if appName == "maya":
            import maya.cmds as cmds
            scene_path = cmds.file(q=1, sn=1)
        elif appName == "3dsmax":
            import MaxPlus
            scene_path = MaxPlus.FileManager.GetFileNameAndPath()
            scene_path = scene_path.replace("\\", "/")
        elif "Nuke" in appName:
            import nuke
            scene_path = nuke.root().name()
    elif current == 0:  # get from recent file
        if appName == "maya":
            import maya.cmds as cmds
            scene_path = cmds.optionVar(q='RecentFilesList')[0]

        elif appName == "3dsmax":
            import xml.etree.ElementTree as ET
            login = os.environ['HOME'].replace("C:/Users/", "").replace("/Documents", "").replace("C:\Users\\", "")
            file_path = "c:/Users/" + login + "/AppData/Local/Autodesk/3dsMax/2015 - 64bit/ENU/RecentDocuments.xml"
            file_object = open(file_path)

            tree = ET.parse(file_object)
            root = tree.getroot()
            recent_files = []
            for x in root.iter('FilePath'):
                recent_files.append(x.text)

            scene_path = recent_files[0]
            file_object.close()
        elif "Nuke" in appName:
            login = os.environ['HOME'].replace("C:\Users\\", "")
            file_path = "c:/Users/" + login + "/.nuke/recent_files"
            file_object = open(file_path, "r")
            recent_files = file_object.readlines()
            file_object.close()
            scene_path = recent_files[0]
    else:
        scene_path = ""

    if scene_path is not "":
        scene_path = scene_path.replace("//art-render/art_3d_project/", "")

        if "(" in scene_path and ")" in scene_path:  # remove everything inside brackets
            start = scene_path.find('(')
            end = scene_path.find(')')
            length = len(scene_path)
            if start != -1 and end != -1:
                    # render_type = scene_path[start+1:end]
                    scene_path = scene_path[0:start] + scene_path[end + 1:length]

        project_details = scene_path.split("/")
        project_name = project_details[0]

        project_type = project_details[1]

        if project_type == "shot":
            item_name = project_details[2]
            process = project_details[3]
            filename = project_details[5]
        else:
            item_type = project_details[2]
            item_name = project_details[3]
            process = project_details[4]
            filename = project_details[6]

            item_type_abbr = abbrItemType(item_type)    # c

        if appName == "maya":
            filename = filename.replace(".mb", "")
        if appName == "3dsmax":
            filename = filename.replace(".max", "")
        if "Nuke" in appName:
            filename = filename.replace(".nk", "")

        # Building filename filters to get correct author name, since users with underscore will mess up the index using split
        project_name_filter = (abbrName(project_name) + "_")
        item_type_filter = (abbrItemType(item_type) + "_")
        item_name_filter = item_name + "_"
        process_filter = (abbrName(process) + "_")


        filename_details = filename.split("_")
        project_name_abbr = abbrName(project_name)  # aoml
        process_abbr = abbrName(process)            # rig

        temp = filename.replace(project_name_filter,"").replace(item_type_filter,"").replace(item_name_filter,"").replace(process_filter,"").replace(".mb","")
        author = temp[5:]
        version = temp.replace("_" + author,"")

        if project_type == "shot":
            reviewPath = base_path + project_name + "/" + project_type + "/" + item_name + "/" + process + "/images/"
            if os.path.exists(reviewPath) is False:
                os.mkdir(reviewPath)

            name_filter = project_name_abbr + "_" + item_name + "_" + process_abbr + "_" + version
            reviewVersion = maxVersion(reviewPath, name_filter, "images")
            reviewFileName = project_name_abbr + "_" + item_name + "_" + process_abbr + "_" + version + "_" + author.replace("\n", "") + "_" + reviewVersion
            reviewBaseFileName = project_name_abbr + "_" + item_name + "_" + process_abbr + "_" + version
            expression_variables = [project_name, item_name, process, author, reviewVersion, project_type]

        # project type is casino or assets
        else:
            reviewPath = base_path + project_name + "/" + project_type + "/" + item_type + "/" + item_name + "/" + process + "/images/"

            if os.path.exists(reviewPath) is False:
                os.mkdir(reviewPath)

            name_filter = project_name_abbr + "_" + item_type_abbr + "_" + item_name + "_" + process_abbr + "_" + version

            reviewVersion = maxVersion(reviewPath, name_filter, "images")

            reviewFileName = project_name_abbr + "_" + item_type_abbr + "_" + item_name + "_" + process_abbr + "_" + version + "_" + author + "_" + reviewVersion
            reviewBaseFileName = project_name_abbr + "_" + item_type_abbr + "_" + item_name + "_" + process_abbr + "_" + version
            expression_variables = [project_name, item_name, process, author, reviewVersion, project_type, item_type]

        return reviewPath, reviewBaseFileName, reviewFileName, expression_variables

    else:
        pass
    # snapshot = server.create_snapshot(task_search_key, (path + filename), "maya binary", "maya file", "None", 0, 0)
    # snapshot_code = snapshot.get('code')
    # server.add_file(snapshot_code, (path + filename), create_icon=True, mode='inplace')


def maxWorkspaceFileRule(project_path):
    project_path = project_path.replace("scenes/", "")
    cmd = "pathConfig.setCurrentProjectFolder(\"" + project_path + "\")"
    MaxPlus.Core.EvalMAXScript(cmd)

    MaxPlus.PathManager.SetAnimationDir(".\\data\\others")
    MaxPlus.PathManager.SetArchivesDir(".\\data\\others")
    MaxPlus.PathManager.SetAutobackDir(".\\data\\others")
    MaxPlus.PathManager.SetProxiesDir(".\\data\\others")
    MaxPlus.PathManager.SetDownloadDir(".\\data\\others")
    MaxPlus.PathManager.SetExportDir(".\\data\\export")
    MaxPlus.PathManager.SetExpressionDir(".\\data\\others")
    MaxPlus.PathManager.SetImageDir(".\\images")
    MaxPlus.PathManager.SetImportDir(".\\data\\others")
    MaxPlus.PathManager.SetMatlibDir(".\\data\\others")
    MaxPlus.PathManager.SetMaxstartDir(".\\scenes")
    MaxPlus.PathManager.SetPhotometricDir(".\\data\\others")
    MaxPlus.PathManager.SetPreviewDir(".\\images")
    MaxPlus.PathManager.SetRenderAssetsDir(".\\data\\renderData")
    MaxPlus.PathManager.SetRenderOutputDir(".\\images")
    MaxPlus.PathManager.SetRenderPresetsDir(".\\data\\others")
    MaxPlus.PathManager.SetSceneDir(".\\scenes")
    MaxPlus.PathManager.SetSoundDir(".\\data\\others")
    MaxPlus.PathManager.SetVpostDir(".\\data\\others")

    paths = ['scenes', 'images', 'sourceimages', 'sourceimages/3dPaintTextures', 'data/others', 'data/renderData', 'data/iprImages', 'data/fur/furFiles', 'data/fur/furImages', 'data/fur/furEqualMap', 'data/fur/furAttrMap', 'data/fur/furShadowMap', 'data/particles', 'data/nCache', 'data/nCache/fluid', 'data/cache', 'data/export']

    for path in paths:
        if not os.path.exists(project_path + path):
            os.makedirs(project_path + path)
        else:
            pass
    print "dir created"


def mayaWorkspaceFileRule(project_path):
    project_path = project_path.replace("scenes/", "")
    cmds.workspace(project_path, o=1)
    data = 'data'

    cmds.workspace(fileRule=['scene', 'scenes'])
    cmds.workspace(fileRule=['images', 'images'])
    cmds.workspace(fileRule=['sourceImages', 'sourceimages'])

    cmds.workspace(fileRule=['clips', data + '/others'])
    cmds.workspace(fileRule=['sound', data + '/others'])
    cmds.workspace(fileRule=['scripts', data + '/others'])
    cmds.workspace(fileRule=['movie', data + '/others'])
    cmds.workspace(fileRule=['translatorData', data + '/others'])
    cmds.workspace(fileRule=['autoSave', data + '/others'])
    cmds.workspace(fileRule=['templates', data + '/others'])
    cmds.workspace(fileRule=['offlineEdit', data + '/others'])
    cmds.workspace(fileRule=['depth', data + '/others'])

    cmds.workspace(fileRule=['3dPaintTextures', 'sourceimages/3dPaintTextures'])
    cmds.workspace(fileRule=['renderData', data + '/renderData'])
    cmds.workspace(fileRule=['iprImages', data + '/iprImages'])

    cmds.workspace(fileRule=['furFiles', data + '/fur/furFiles'])
    cmds.workspace(fileRule=['furImages', data + '/fur/furImages'])
    cmds.workspace(fileRule=['furEqualMap', data + '/fur/furEqualMap'])
    cmds.workspace(fileRule=['furAttrMap', data + '/fur/furAttrMap'])
    cmds.workspace(fileRule=['furShadowMap', data + '/fur/furShadowMap'])

    cmds.workspace(fileRule=['particles', data + '/particles'])
    cmds.workspace(fileRule=['fluidCache', data + '/nCache/fluid'])
    cmds.workspace(fileRule=['fileCache', data + '/nCache'])
    cmds.workspace(fileRule=['diskCache', data + '/cache'])
    cmds.workspace(fileRule=['OBJ', data + '/export'])
    cmds.workspace(fileRule=['OBJexport', data + '/export'])
    cmds.workspace(fileRule=['Alembic', data + '/export'])
    cmds.workspace(fileRule=['shaders', data + '/export'])

    paths = ['scenes', 'images', 'sourceimages', 'sourceimages/3dPaintTextures', 'data/others', 'data/renderData', 'data/iprImages', 'data/fur/furFiles', 'data/fur/furImages', 'data/fur/furEqualMap', 'data/fur/furAttrMap', 'data/fur/furShadowMap', 'data/particles', 'data/nCache', 'data/nCache/fluid', 'data/cache', 'data/export']

    for path in paths:
        if not os.path.exists(project_path + path):
            os.makedirs(project_path + path)
        else:
            pass

    '''
    cmds.workspace(fileRule=['eps', 'data'])
    cmds.workspace(fileRule=['mel', 'scripts'])
    cmds.workspace(fileRule=['STEP_DC', 'data'])
    cmds.workspace(fileRule=['CATIAV5_DC', 'data'])
    cmds.workspace(fileRule=['CATIAV4_DC', 'data'])
    cmds.workspace(fileRule=['IPT_DC', 'data'])
    cmds.workspace(fileRule=['SW_DC', 'test/test/test'])
    cmds.workspace(fileRule=['DAE_FBX export', 'data'])
    cmds.workspace(fileRule=['Autodesk Packet File', 'data'])
    cmds.workspace(fileRule=['DAE_FBX', 'data'])
    cmds.workspace(fileRule=['DXF_DCE', 'data'])
    cmds.workspace(fileRule=['mayaAscii', 'scenes'])
    cmds.workspace(fileRule=['move', 'data'])
    cmds.workspace(fileRule=['mayaBinary', 'scenes'])
    cmds.workspace(fileRule=['DWG_DC', 'data'])
    cmds.workspace(fileRule=['DXF_DC', 'data'])
    cmds.workspace(fileRule=['SPF_DCE', 'data'])
    cmds.workspace(fileRule=['ZPR_DCE', 'data'])
    cmds.workspace(fileRule=['audio', 'sound'])
    cmds.workspace(fileRule=['IV_DC', 'data'])
    cmds.workspace(fileRule=['STL_DCE', 'data'])
    cmds.workspace(fileRule=['FBX export', 'data'])
    cmds.workspace(fileRule=['JT_DC', 'data'])
    cmds.workspace(fileRule=['DWG_DCE', 'data'])
    cmds.workspace(fileRule=['FBX', 'data'])
    cmds.workspace(fileRule=['IGES_DC', 'data'])
    cmds.workspace(fileRule=['illustrator', 'data'])
    cmds.workspace(fileRule=['UG_DC', 'data'])
    cmds.workspace(fileRule=['SPF_DC', 'data'])
    cmds.workspace(fileRule=['PTC_DC', 'data'])

    cmds.workspace(fileRule=['CSB_DC', 'data'])
    cmds.workspace(fileRule=['STL_DC', 'data'])
    cmds.workspace(fileRule=['IGES_DCE', 'data'])
    cmds.workspace(fileRule=['UG_DCE', 'data'])
    '''
