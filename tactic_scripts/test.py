# -*- coding: utf-8 -*-
#this is a scheduled script that updates the cache the maya, nuke, etc filemanagers uses
#the data are written to simpleslot/plan id 8 for inprogress, 10 for commplte, 11 for ready
#python "//art-1405260002/d/assets/scripts/tactic_scripts/py_update_maya_gamelist_cache.py"

import time
import sys
import socket
sys.path.append("/home/apache/tactic/src/client")
sys.path.append("/mnt/hgfs/assets/scripts/python-dateutil-2.3")
sys.path.append("/mnt/hgfs/assets/scripts/six-1.8.0")
sys.path.append("//Art-1405260002/d/assets/client")
sys.path.append("//Art-1405260002/d/assets/scripts/python-dateutil-2.3")
sys.path.append("//Art-1405260002/d/assets/scripts/six-1.8.0")

from tactic_client_lib import TacticServerStub
server = TacticServerStub.get(setup=False)
tactic_server_ip = socket.gethostbyname("vg.com")
server.set_server(tactic_server_ip)
server.set_project("simpleslot")
ticket = server.get_ticket("julio", "1234")
server.set_ticket(ticket)
import operator
import six
import datetime
now = datetime.datetime.now()
from dateutil import parser

typecodenames = ["character", "symbol", "user_interface", "bonus01", "bonus02", "free_game", "jackpot", "introduction"]
typecodes = ["3D_TYPE00002", "3D_TYPE00003", "3D_TYPE00004", "3D_TYPE00005", "3D_TYPE00006", "3D_TYPE00007", "3D_TYPE00008", "3D_TYPE00009"]
assetcodenames = ["character", "vehicle", "set", "prop", "other"]
assetcodes = ["ASSET_TYPE00002","ASSET_TYPE00003", "ASSET_TYPE00004", "ASSET_TYPE00005", "ASSET_TYPE00006"]
def pkgtypecount(items):
    layout = demo = 0
    for item in items:
        try:
            temp = item['process']
            if temp == 'layout':
                layout = layout + 1
            elif temp == 'demo':
                demo = demo + 1
        except:
            continue
    return [layout, demo]

def asttypecount(items):
    ast_char = ast_vehicle = ast_set = ast_prop = ast_other = 0
    for item in items:
        try:
            temp = item['asset_type_code']
            if temp == assetcodes[0]:
                ast_char = char + 1
            elif temp == assetcodes[1]:
                ast_vehicle = ast_vehicle + 1
            elif temp == assetcodes[2]:
                ast_set = ast_set + 1
            elif temp == assetcodes[3]:
                ast_prop = ast_prop + 1
            elif temp == assetcodes[5]:
                ast_other = ast_other + 1
        except:
            continue
    return [ast_char, ast_vehicle, ast_set, ast_prop, ast_other]

def typecount(items):
    char = symbol = ui = bonus = free_game = jackpot = intro = 0
    for item in items:
        try:
            temp = item['3d_type_code']
            if temp == typecodes[0]:
                char = char + 1
            elif temp == typecodes[1]:
                symbol = symbol + 1
            elif temp == typecodes[2]:
                ui = ui + 1
            elif temp == typecodes[3]:
                bonus = bonus + 1
            elif temp == typecodes[4]:
                bonus = bonus + 1
            elif temp == typecodes[5]:
                free_game = free_game + 1
            elif temp == typecodes[6]:
                jackpot = jackpot + 1
            elif temp == typecodes[7]:
                intro = intro + 1
        except:
            continue
    return [char, symbol, ui, bonus, free_game, jackpot, intro]

def game_type_code_converter(game_type_code):
    game_type = ""
    if game_type_code == "GAME_TYPE00002":
        game_type = "casino"
    elif game_type_code == "GAME_TYPE00005":
        game_type = "video_conf"
    elif game_type_code == "GAME_TYPE00007":
        game_type = "training"
    elif game_type_code == "GAME_TYPE00009":
        game_type = "others"
    elif game_type_code == "GAME_TYPE00010":
        game_type = "cf"
    elif game_type_code == "GAME_TYPE00011":
        game_type = "sports"
    elif game_type_code == "GAME_TYPE00012":
        game_type = "lottery"
    elif game_type_code == "GAME_TYPE00014":
        game_type = "IPL"
    elif game_type_code == "GAME_TYPE00021":
        game_type = "database"
    return game_type

filetype = "main"
status_filter = "['project_status','NEQ','.Hidden']['project_status','NEQ','.Complete']['project_status','NEQ','.Not Ready']['project_status','NEQ','.Ready']"
stypes = ['3d', 'assets', 'package']

items = []
tasks = []
snapshots= []
files = []

games_exp = "@SOBJECT(simpleslot/game" + status_filter + ")"
games = server.eval(games_exp)

for stype in stypes:
    items_exp = "@SOBJECT(simpleslot/game" + status_filter + ".simpleslot/" + stype + ")"
    tasks_exp = "@SOBJECT(simpleslot/game" + status_filter + ".simpleslot/" + stype + ".sthpw/task)"
    snapshots_exp = "@SOBJECT(simpleslot/game" + status_filter + ".simpleslot/" + stype + ".sthpw/task.sthpw/snapshot)"
    files_exp = "@SOBJECT(simpleslot/game" + status_filter + ".simpleslot/" + stype + ".sthpw/task.sthpw/snapshot.sthpw/file['file_name','not like','']['type','" + filetype + "'])"

    if(stype == '3d'):
        casino_items = server.eval(items_exp)
        casino_tasks = server.eval(tasks_exp)
        casino_files = server.eval(files_exp)
    elif(stype == 'assets'):
        asset_items = server.eval(items_exp)
        asset_tasks = server.eval(tasks_exp)
        asset_files = server.eval(files_exp)
    elif(stype == 'package'):
        package_items = server.eval(items_exp)
        package_tasks = server.eval(tasks_exp)
        package_files = server.eval(files_exp)

for game in games:
    game_type_code = game['game_type_code']
    game_type = game_type_code_converter(game_type_code)

    sk = game.get("__search_key__")

    name = game.get("name")
    game_code = game["code"]

    item_codes = []
    task_codes = []
    snapshot_codes = []

    filtered_items = []
    filtered_tasks = []
    filtered_snapshots = []
    filtered_files = []

    if(game_type == "casino" or game_type == "lottery"):
        items = casino_items + package_items
        tasks = casino_tasks + package_tasks
        #snapshots = casino_snapshots
        files = casino_files
    elif(game_type == "cf" or game_type == "database"):
        items = asset_items
        tasks = asset_tasks
        #snapshots = asset_snapshots
        files = asset_files
    elif(game_type == "video_conf"):
        items = package_items
        tasks = package_tasks
        #snapshots = package_snapshots
        files = package_files

    for item in items:
        if item['game_code'] == game_code:
            item_codes.append(item['code'])
            filtered_items.append(item)
    for task in tasks:
        if task['search_code'] in item_codes:
            task_codes.append(task['code'])
            filtered_tasks.append(task)
    for file in files:
        if file['search_code'] in task_codes:
            filtered_files.append(file)

    casino_typecount = typecount(filtered_items)
    asset_typecount = asttypecount(filtered_items)
    package_typecount = pkgtypecount(filtered_tasks)

    print casino_typecount

    ff = ""
    for ch in casino_typecount:
        ff = ff + "," + str(ch)
    for ch in asset_typecount:
        ff = ff + "," + str(ch)
    for ch in package_typecount:
        ff = ff + "," + str(ch)

    if len(filtered_files) > 0:
        data = {'keywords': len(filtered_files), 'description': ff[1:]}
    else:
        data = {'keywords': 0, 'description': 0}
    print name, data
    server.update(sk, data)