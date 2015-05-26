import sys
sys.path.append("//Art-1405260002/d/assets/client")

import maya.cmds as cmds
import maya.mel as mel
import os
import shutil
import jc_maya_aux_functions as jc


def saveRV():
    username = os.environ.get("USERNAME")
    from tactic_client_lib import TacticServerStub
    server = TacticServerStub()
    #server.set_server("192.168.201.10")
    #server.set_project("simpleslot")
    ticket_files = os.listdir("c:/sthpw/etc/")
    ticket_file = "c:/sthpw/etc/" + username + ".tacticrc"

    if len(ticket_files) == 0:
        file_object = open(ticket_file, "w")
        ticket_content = "login=" + username + "\n" + "server=192.168.201.10" + "\n" + "project=simpleslot"
        file_object.write(ticket_content)
        file_object.close()

    else:
        file_object = open(ticket_file)
        ticket_content = file_object.readlines()
        file_object.close()
        ticket = ticket_content[2].replace("ticket=", "").replace("\n", "")
        server.ticket = ticket
        server.set_server("192.168.201.10")
        server.set_project("simpleslot")     

    rvname = jc.getNextFileName(1)
    rv_path = rvname[0]
    rv_filename = rvname[2]
    # base_scenename = rvname[1].

    project_name = rvname[3][0]
    item_name = rvname[3][1]
    process = rvname[3][2]
    # author = rvname[3][3]
    # reviewVersion = rvname[3][4]
    project_type = rvname[3][5]
    tactic_base_path = "//Art-1405260002/d/assets/simpleslot/"

    if project_type == "casino":
        stype = "3d"
    elif project_type == "assets":
        stype = "assets"
    elif project_type == "shot":     
        stype = "shot"

    src_filename = rv_path + rv_filename
    dst_filename = tactic_base_path + project_name + "/" + project_type + "/" + process + "/" + rv_filename

    if os.path.isdir(tactic_base_path + project_name + "/" + project_type + "/" + process + "/") is False:
        os.makedirs(tactic_base_path + project_name + "/" + project_type + "/" + process + "/")

    if cmds.intScrollBar("scrollBar", q=1, v=1) == -1:
        cmds.renderWindowEditor("renderView", e=1, si=1)
        cmds.intScrollBar("scrollBar", e=1, v=0)

    orig_format = mel.eval('getAttr "defaultRenderGlobals.imageFormat";')
    mel.eval('setAttr "defaultRenderGlobals.imageFormat" 8;')
    cmds.renderWindowEditor("renderView", e=1, wi=src_filename)
    mel.eval('setAttr "defaultRenderGlobals.imageFormat" ' + str(orig_format) + ';')

    shutil.copy2((src_filename + ".jpg"), (dst_filename + ".jpg"))

    expr = "@SOBJECT(simpleslot/game['name','" + project_name + "'].simpleslot/" + stype + "['name','" + item_name + "'].sthpw/task['process','" + process + "'])"
    task = server.eval(expr)

    sk = task[0].get("__search_key__")

    final_filename = "/mnt/hgfs/assets/simpleslot/" + project_name + "/" + project_type + "/" + process + "/" + rv_filename + ".jpg"

    server.simple_checkin(sk, process, final_filename, description="image", mode="inplace")
    print "image uploaded"


#saveRV()