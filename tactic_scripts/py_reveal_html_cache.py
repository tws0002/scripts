import time
import datetime
from operator import itemgetter
from dateutil import parser
import sys
import socket
sys.path.append("//Art-1405260002/d/assets/client")

from tactic_client_lib import TacticServerStub

server = TacticServerStub.get()

filetype = "main"
exp = "@SOBJECT(simpleslot/game['project_status','NEQ','.Hidden']['keywords','>','0'])"
games = server.eval(exp)

inprogress = []
ready = []
complete = []
notready = []

def getTimeStamp(item):
    return item['timestamp']

# builds filters into html code, jquery will search based on tcn acn, so names has to be unique

def game_type_code_converter(game_type_code):
    game_type = ""
    if game_type_code == "GAME_TYPE00002":
        game_type = "search_casino"
    elif game_type_code == "GAME_TYPE00005":
        game_type = "search_video_conf"
    elif game_type_code == "GAME_TYPE00007":
        game_type = "search_training"
    elif game_type_code == "GAME_TYPE00009":
        game_type = "search_others"
    elif game_type_code == "GAME_TYPE00010":
        game_type = "search_cf"
    elif game_type_code == "GAME_TYPE00011":
        game_type = "search_sports"
    elif game_type_code == "GAME_TYPE00012":
        game_type = "search_lottery"
    elif game_type_code == "GAME_TYPE00014":
        game_type = "search_IPL"
    return game_type    

def element_filter_converter(game_filter):
    temp = [int(x) for x in game_filter.split(",")]
    tcn = ["casino_character", "casino_symbol", "casino_user_interface", "casino_bonus", "casino_free_game", "casino_jackpot", "casino_introduction"]
    acn = ["cf_character", "cf_vehicle", "cf_set", "cf_prop", "cf_misc"]

    t = ""

    if (temp[0]) > 0:
        t = t + " " + tcn[0]
    if int(temp[1]) > 0:
        t = t + " " + tcn[1]    
    if int(temp[2]) > 0:
        t = t + " " + tcn[2]
    if int(temp[3]) > 0:
        t = t + " " + tcn[3]
    if int(temp[4]) > 0:
        t = t + " " + tcn[4]
    if int(temp[5]) > 0:
        t = t + " " + tcn[5]
    if int(temp[6]) > 0:
        t = t + " " + tcn[6]

    if int(temp[7]) > 0:
        t = t + " " + acn[0]
    if int(temp[8]) > 0:
        t = t + " " + acn[1]
    if int(temp[9]) > 0:
        t = t + " " + acn[2]
    if int(temp[10]) > 0:
        t = t + " " + acn[3]
    if int(temp[11]) > 0:
        t = t + " " + tcn[4]
        
    if int(temp[12]) > 0:
        t = t + " " + "cf_shot"
    if int(temp[13]) > 0:
        t = t + " " + "pkg_layout"
    if int(temp[14]) > 0:
        t = t + " " + "pkg_demo"
    t = t[1:]
    return t
#games = sorted(games,key=getTimeStamp,reverse=True)

for game in games:
    name = game.get("name")

    if game.get('project_status') == '.In Progress':
        inprogress.append(game)
    if game.get('project_status') == '.Ready':
        ready.append(game)
    if game.get('project_status') == '.Not Ready':
        notready.append(game)
    if game.get('project_status') == '.Complete':
        complete.append(game)        

inprogress = sorted(inprogress,key=getTimeStamp,reverse=True)
ready = sorted(ready,key=getTimeStamp,reverse=True)
complete = sorted(complete,key=getTimeStamp,reverse=True)
notready = sorted(notready,key=getTimeStamp,reverse=True)

html = []
html.append(("<span><h1>進行中</h1></span>").decode("utf-8"))
html.append("<ul>")
for game in inprogress:
    game_name_chn = game.get("name_chn")    
    game_name = game.get("name")
    game_type = game_type_code_converter(game.get("game_type_code"))
    elem_filter_codes = game.get("description")
    elem_filter = element_filter_converter(elem_filter_codes)
    file_count = game.get("keywords")
    exp = "@SOBJECT(simpleslot/game['name','" + game_name + "'].sthpw/snapshot['@ORDER_BY','timestamp'].sthpw/file['file_name','not like','']['type','" + filetype + "'])"
    try:
        ss_file = server.eval(exp)
        ss_file = sorted(ss_file, key=itemgetter('timestamp')) 
        ss_count = len(ss_file) - 1
        ss_file = ss_file[ss_count]
        full_filename = ss_file.get("file_name")
        relative_dir = ss_file.get("relative_dir")
        full_path = str(("/assets/" + relative_dir + "/" + full_filename).encode("utf-8"))
        html.append("<li class='' filters='%s %s'>" % (game_type, elem_filter))
        html.append("<img class= 'loadReveal' src='%s'></img>" % full_path.decode("utf-8"))
        html.append("<h3 class='links'>%s</h3>" % game_name_chn)
        html.append("<span>%s</span>" % str(game_name.encode("utf-8")))
        html.append(str("</li>".encode("utf-8")))
    except:
        pass
html.append("</ul>")
html.append(("<span><h1>完成</h1></span>").decode("utf-8"))
html.append("<ul>")
for game in complete:
    game_name_chn = game.get("name_chn")    
    game_name = game.get("name")
    game_type = game_type_code_converter(game.get("game_type_code"))
    elem_filter_codes = game.get("description")
    elem_filter = element_filter_converter(elem_filter_codes)
    file_count = game.get("keywords")
    exp = "@SOBJECT(simpleslot/game['name','" + game_name + "'].sthpw/snapshot['@ORDER_BY','timestamp'].sthpw/file['file_name','not like','']['type','" + filetype + "'])"
    try:   
        ss_file = server.eval(exp)
        ss_file = sorted(ss_file, key=itemgetter('timestamp')) 
        ss_count = len(ss_file) - 1
        ss_file = ss_file[ss_count]
        full_filename = ss_file.get("file_name")
        relative_dir = ss_file.get("relative_dir")
        full_path = str(("/assets/" + relative_dir + "/" + full_filename).encode("utf-8"))
        html.append("<li class='' filters='%s %s'>" % (game_type, elem_filter))
        html.append("<img class= 'loadReveal' src='%s'></img>" % full_path.decode("utf-8"))
        html.append("<h3 class='links'>%s</h3>" % game_name_chn)
        html.append("<span>%s</span>" % str(game_name.encode("utf-8")))
        html.append(str("</li>".encode("utf-8")))
    except:
        pass
html.append("</ul>")

html = "".join(html)

test = "<h1>測試</h1>".decode("utf-8")

