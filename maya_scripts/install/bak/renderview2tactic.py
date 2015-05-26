import maya.cmds as cmds
import maya.mel as mel
import os
import sys
import shutil
sys.path.append("//Art-1405260002/d/assets/client")

username = os.environ.get("USERNAME")
from tactic_client_lib import TacticServerStub
server = TacticServerStub()
server.set_server("192.168.201.10")
server.set_project("simpleslot")

'''
maxVersion will look at the final_path and list all the files with a prefix
of filename. From this list, it will find the largest version number and
return this number plus 1
'''


def maxVersion(final_path, filename):
    savedFiles = []
    versions = []
    if os.path.exists(final_path) is True:
        savedFiles = os.listdir(final_path)
        currentSceneReviewList = [x for x in savedFiles if filename in x]
        if len(currentSceneReviewList) == 0:
            maxversion = "v01"
        elif currentSceneReviewList[0] == "Thumbs.db":
            maxversion = "v01"
        else:
            for savedFile in currentSceneReviewList:
                if os.path.isdir(final_path + savedFile) is True:  # if its a directory, skip
                    pass
                elif savedFile == "Thumbs.db":
                    pass
                else:
                    savedFile = savedFile.replace((filename + "_"), "")
                    version = savedFile.split(".")[0]
                    version = version.replace("v", "")
                    versions.append(int(version))

            maxversion = "v" + str("%02d" % (max(versions) + 1))
    else:
        maxversion = "v01"
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


'''
getReviewFileName will find the current scene path and filename,
build the image path,
add the correct version using maxversion, add user name,
return the path and filename
'''


def getReviewFileName():
    base_path = "//art-render/art_3d_project/"

    scene_path = cmds.file(q=1, sn=1)
    scene_path = scene_path.replace("//art-render/art_3d_project/", "")

    project_details = scene_path.split("/")

    project_name = project_details[0]
    project_type = project_details[1]
    item_type = project_details[2]
    item_name = project_details[3]
    process = project_details[4]
    filename = project_details[6]

    filename = filename.replace(".mb", "")

    filename_details = filename.split("_")

    project_name_abbr = abbrName(project_name)
    item_type_abbr = abbrName(item_type)
    process_abbr = abbrName(process)

    authorIndex = len(filename_details) - 1
    versionIndex = authorIndex - 1

    version = filename_details[versionIndex]
    author = filename_details[authorIndex]

    expression_variables = [project_name, item_name, process, author]
    reviewPath = base_path + project_name + "/" + project_type + "/" + item_type + "/" + item_name + "/" + process + "/images/"

    if os.path.exists(reviewPath) is False:
        os.mkdir(reviewPath)

    temp = project_name_abbr + "_" + item_type_abbr + "_" + item_name + "_" + process_abbr + "_" + version + "_" + author

    reviewVersion = maxVersion(reviewPath, temp)

    reviewFileName = project_name_abbr + "_" + item_type_abbr + "_" + item_name + "_" + process_abbr + "_" + version + "_" + author + "_" + reviewVersion

    return reviewPath, reviewFileName, expression_variables


def saveRV():
    temp = getReviewFileName()
    path = temp[0]
    filename = (temp[1] + ".jpg")
    network_base_path = "//Art-1405260002/d/assets/simpleslot/"

    src_filename = path + filename
    if os.path.isdir(network_base_path + temp[2][0] + "/review/") is False:
        os.mkdir(network_base_path + temp[2][0] + "/review/")

    dst_filename = network_base_path + temp[2][0] + "/review/" + filename

    if cmds.intScrollBar("scrollBar", q=1, v=1) == -1:
        cmds.renderWindowEditor("renderView", e=1, si=1)
        cmds.intScrollBar("scrollBar", e=1, v=0)

    orig_format = mel.eval('getAttr "defaultRenderGlobals.imageFormat";')
    mel.eval('setAttr "defaultRenderGlobals.imageFormat" 8;')
    cmds.renderWindowEditor("renderView", e=1, wi=src_filename)
    mel.eval('setAttr "defaultRenderGlobals.imageFormat" ' + str(orig_format) + ';')

    shutil.copy2(src_filename, dst_filename)
    expr = "@SOBJECT(simpleslot/game['name','" + temp[2][0] + "'].simpleslot/assets['name','" + temp[2][1] + "'].sthpw/task['process','" + temp[2][2] + "'])"

    task = server.eval(expr)
    sk = task[0].get("__search_key__")

    final_filename = "/mnt/hgfs/assets/simpleslot/" + temp[2][0] + "/review/" + filename
    server.simple_checkin(sk, temp[2][2], final_filename, description="image", mode="inplace")
