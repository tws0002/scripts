# -*- coding: utf-8 -*-

import time
import datetime
from dateutil import parser
import sys
import socket
sys.path.append("//Art-1405260002/d/assets/client")

from tactic_client_lib import TacticServerStub

server = TacticServerStub.get()
tactic_server_ip = socket.gethostbyname("vg.com")
server.set_server(tactic_server_ip)
server.set_project("simpleslot")
ticket = server.get_ticket("julio", "1234")
server.set_ticket(ticket)

import datetime
from dateutil import parser
from operator import itemgetter
import os

filetype = "main"
exp = "@SOBJECT(simpleslot/game['project_status','NEQ','.Hidden'])"
games = server.eval(exp)

inprogress = []
ready = []
complete = []
notready = []

def getTimeStamp(item):
    return item['timestamp']
    
#games = sorted(games,key=getTimeStamp,reverse=True)

for game in games:
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
    exp = "@SOBJECT(simpleslot/game['name','" + game_name + "'].sthpw/snapshot.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
    try:   
        ss_file = server.eval(exp)[0]
        full_filename = ss_file.get("file_name")
        relative_dir = ss_file.get("relative_dir")
        full_path = str(("/assets/" + relative_dir + "/" + full_filename).encode("utf-8"))
        html.append("<li>")
        html.append("<a href='' onclick=''><img src='%s'></img></a>" % full_path.decode("utf-8"))
        html.append("<h3><a href='' onclick=''>%s</a></h3>" % game_name_chn)
        html.append("<span>%s</span>" % str(game_name.encode("utf-8")))
        html.append(str("</li>".encode("utf-8")))
    except:
        pass
html.append("</ul>")

html.append(("<span><h1>準備中</h1></span>").decode("utf-8"))
html.append("<ul>")
for game in ready:
    game_name_chn = game.get("name_chn")    
    game_name = game.get("name")
    exp = "@SOBJECT(simpleslot/game['name','" + game_name + "'].sthpw/snapshot.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
    try:   
        ss_file = server.eval(exp)[0]
        full_filename = ss_file.get("file_name")
        relative_dir = ss_file.get("relative_dir")
        full_path = str(("/assets/" + relative_dir + "/" + full_filename).encode("utf-8"))
        html.append("<li>")
        html.append("<a href='' onclick=''><img src='%s'></img></a>" % full_path.decode("utf-8"))
        html.append("<h3><a href='' onclick=''>%s</a></h3>" % game_name_chn)
        html.append("<span>%s</span>" % str(game_name.encode("utf-8")))
        html.append(str("</li>".encode("utf-8")))
    except:
        pass
html.append("</ul>")

html.append(("<span><h1>待命</h1></span>").decode("utf-8"))
html.append("<ul>")
for game in ready:
    game_name_chn = game.get("name_chn")    
    game_name = game.get("name")
    exp = "@SOBJECT(simpleslot/game['name','" + game_name + "'].sthpw/snapshot.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
    try:   
        ss_file = server.eval(exp)[0]
        full_filename = ss_file.get("file_name")
        relative_dir = ss_file.get("relative_dir")
        full_path = str(("/assets/" + relative_dir + "/" + full_filename).encode("utf-8"))
        html.append("<li>")
        html.append("<a href='' onclick=''><img src='%s'></img></a>" % full_path.decode("utf-8"))
        html.append("<h3><a href='' onclick=''>%s</a></h3>" % game_name_chn)
        html.append("<span>%s</span>" % str(game_name.encode("utf-8")))
        html.append(str("</li>".encode("utf-8")))
    except:
        pass
html.append("</ul>")

html.append(("<span><h1></h1></span>").decode("utf-8"))
html.append("<ul>")
for game in ready:
    game_name_chn = game.get("name_chn")    
    game_name = game.get("name")
    exp = "@SOBJECT(simpleslot/game['name','" + game_name + "'].sthpw/snapshot.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
    try:   
        ss_file = server.eval(exp)[0]
        full_filename = ss_file.get("file_name")
        relative_dir = ss_file.get("relative_dir")
        full_path = str(("/assets/" + relative_dir + "/" + full_filename).encode("utf-8"))
        html.append("<li>")
        html.append("<a href='' onclick=''><img src='%s'></img></a>" % full_path.decode("utf-8"))
        html.append("<h3><a href='' onclick=''>%s</a></h3>" % game_name_chn)
        html.append("<span>%s</span>" % str(game_name.encode("utf-8")))
        html.append(str("</li>".encode("utf-8")))
    except:
        pass
html.append("</ul>")


html = "".join(html)




