import sys
sys.path.append("//Art-1405260002/d/assets/client")

import MaxPlus
import os
import shutil
import jc_maya_aux_functions as jc
import subprocess

def saveVrayVFB():
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
    item_type = rvname[3][6]

    if project_type == "casino":
        stype = "3d"
    elif project_type == "assets":
        stype = "assets"
    elif project_type == "shot":     
        stype = "shot"

    tactic_base_path = "//Art-1405260002/d/assets/simpleslot/"

    src_filename = rv_path + rv_filename
    dst_filename = tactic_base_path + project_name + "/" + project_type + "/" + process + "/" + rv_filename

    if os.path.isdir(tactic_base_path + project_name + "/" + project_type + "/" + process + "/") is False:
        os.makedirs(tactic_base_path + project_name + "/" + project_type + "/" + process + "/")

    cmd = "vfbControl #saveImage \"" + src_filename + ".exr\""
    MaxPlus.Core.EvalMAXScript(cmd)

    imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe -quality 100 -colorspace RGB \"%s\" -colorspace sRGB \"%s\"" % (src_filename + ".exr", src_filename + ".jpg")
    subprocess.call(imageMagickCMD)

    # deleteEXRCMD = "del \"" + src_filename + ".exr\""
    # deleteEXRCMD = deleteEXRCMD.replace("/","\\")
    # subprocess.call(deleteEXRCMD)
    os.remove(src_filename + ".exr")

    shutil.copy2((src_filename + ".jpg"), (dst_filename + ".jpg"))

    expr = "@SOBJECT(simpleslot/game['name','" + project_name + "'].simpleslot/" + stype + "['name','" + item_name + "'].sthpw/task['process','" + process + "'])"
    task = server.eval(expr)

    sk = task[0].get("__search_key__")

    final_filename = "/mnt/hgfs/assets/simpleslot/" + project_name + "/" + project_type + "/" + process + "/" + rv_filename + ".jpg"

    server.simple_checkin(sk, process, final_filename, description="VRAY", mode="inplace")
    print "image uploaded"


#saveVrayVFB()
