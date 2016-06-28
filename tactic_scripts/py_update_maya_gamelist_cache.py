# -*- coding: utf-8 -*-
#this is a scheduled script that updates the cache the maya, nuke, etc filemanagers uses
#the data are written to simpleslot/plan id 8 for inprogress, 10 for commplte, 11 for ready
#python "//art-1405260002/d/assets/scripts/tactic_scripts/py_update_maya_gamelist_cache.py"

import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
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

#%%
def gamelist(games, game_tasks):
    now = datetime.datetime.now()
    names = ""
    names_chn = ""
    games_type = ""
    assignments = ""
    bsd_string = ""
    bed_string = ""
    depts = []
    for game in games:
        bsd = []
        bed = []
        name = game.get("name")
        name_chn = game.get("name_chn")
        search_code = game.get("code")

        for task in game_tasks:
            if task['search_code'] == search_code:
                depts.append(task)

        game_type = game_type_code_converter(game.get("game_type_code"))


        for dept in depts:
            bsd.append(parser.parse(dept.get("bid_start_date")))
            bed.append(parser.parse(dept.get("bid_end_date")))
        try:
            bsd = min(bsd)
            bsd = bsd.strftime("%m/%d/%y")
        except:
            bsd = ""
        try:
            bed = max(bed)
            bed = bed.strftime("%m/%d/%y")
        except:
            bed = ""
        bsd_string = bsd_string + "__" + (bsd)
        bed_string = bed_string + "__ " + (bed)

        assignment = game.get("project_coordinator")
        assignments = assignments + "__" + assignment
        names = names + "__" + name
        games_type = games_type + "__" + game_type
        names_chn = names_chn + "__" + name_chn
    data = {'name': names, 'description': games_type, 'login': bsd_string, 'keywords': bed_string, 'timestamp': str(now), 'game_name_chn': names_chn, 'process': assignments}
    diff = datetime.datetime.now() - now
    print diff
    return data

def htmlCache():
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
            t = t + " " + "pkg_layout"
        if int(temp[13]) > 0:
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

    def buildHTML(games, html):
        for game in games:
            #game = games[2]
            game_name_chn = game.get("name_chn")
            game_name = game.get("name")
            game_type = "search_" + game_type_code_converter(game.get("game_type_code"))
            elem_filter_codes = game.get("description")
            elem_filter = element_filter_converter(elem_filter_codes)
            file_count = game.get("keywords")

            # this builds the thumbnail
            exp = "@SOBJECT(simpleslot/game['name','" + game_name + "'].sthpw/snapshot['@ORDER_BY','timestamp'].sthpw/file['file_name','not like','']['type','" + filetype + "'])"
            ss_file = server.eval(exp)
            ss_count = len(ss_file)
            if(ss_count > 0):
                ss_count = ss_count - 1
                ss_file = ss_file[ss_count]
                full_filename = ss_file.get("file_name")
                relative_dir = ss_file.get("relative_dir")
                full_path = str(("/assets/" + relative_dir + "/" + full_filename).encode("utf-8"))
            else:
                full_path = "http://vg.com/context/icons/common/no_image.png"

            html.append("<li class='' filters='%s %s'>" % (game_type, elem_filter))
            html.append("<img class= 'loadReveal' src='%s'></img>" % full_path.encode("utf-8"))
            html.append("<h3 class='links'>%s</h3>" % game_name_chn.encode("utf-8"))
            html.append("<span>%s</span>" % str(game_name.encode("utf-8")))
            html.append("<div><table class='gantt_or_reveal'><tr><td><h3 class='loadGantt'>甘特圖</h3><awe class='fa1 fa-tasks fa-3x loadGantt' style='color=#fff' aria-hidden='true'></awe></td><td><h3 class='loadReveal'>多媒體</h3><awe class='fa1 fa-picture-o fa-3x loadReveal' style='color=#fff' aria-hidden='true'></awe></td></tr></table></div>")
            html.append(str("</li>".encode("utf-8")))
        return html

    html = []
    html.append((u"<span><h1>進行中</h1></span>").encode("utf-8"))
    html.append("<ul>")
    buildHTML(inprogress, html)
    html.append("</ul>")
    html.append((u"<span><h1>完成</h1></span>").encode("utf-8"))
    html.append("<ul>")
    buildHTML(complete, html)
    html.append("<ul>")

    htmlstring = ""
    for x in html:
        htmlstring = htmlstring + x
    html = "".join(html)

    data = {'description': html}
    server.update("simpleslot/plan?project=simpleslot&id=809", data)

#%%
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

#%%
def updateRevealFilters():
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
        server.update(sk, data)
#%%
def gameObjectCount(plan_id):
    plan_id = '8'
    cf_type = ['cf','video_conf', 'database']
    expr = "@SOBJECT(simpleslot/plan['id','" + plan_id + "'])"
    projects_data = server.eval(expr)[0]

    names = projects_data.get('name')
    names = names.split("__")

    bsd = projects_data.get('login')
    bsd = bsd.split("__")

    bed = projects_data.get('keywords')
    bed = bed.split("__")

    names_chn = projects_data.get('game_name_chn')
    names_chn = names_chn.split("__")

    games_type = projects_data.get('description')
    games_type = games_type.split("__")

    assigned = projects_data.get('process')
    assigned = assigned.split("__")

    temp = zip(names_chn, games_type, assigned, bsd, bed, names)
    temp.pop(0)
    game_data = []
    for x in temp:
        game_data.append({'name_chn':x[0], 'game_type': x[1], 'assigned':x[2], 'bsd':x[3], 'bed':x[4], 'name':x[5]})

    game_item_count = ""

    for game in game_data:
        items = 0
        if(game['game_type'] == 'casino' or game['game_type'] == 'lottery'):
           expr = "@SOBJECT(simpleslot/game['name','" + game['name'] + "'].simpleslot/3d)"
           items = server.eval(expr)
           #print len(items), game['name']
        elif(game['game_type'] in cf_type):
           expr = "@SOBJECT(simpleslot/game['name','" + game['name'] + "'].simpleslot/assets)"
           assets = server.eval(expr)
           expr = "@SOBJECT(simpleslot/game['name','" + game['name'] + "'].simpleslot/shot)"
           shots = server.eval(expr)
           items = assets + shots

        game_item_count = game_item_count + "__" + str(len(items))
    return game_item_count

def run():

    expr = "@SOBJECT(simpleslot/game.sthpw/task)"
    game_tasks = server.eval(expr)

    expr = "@SOBJECT(simpleslot/game['project_status','.In Progress'])"
    inprogress = server.eval(expr)

    expr = "@SOBJECT(simpleslot/game['project_status','.Ready'])"
    ready = server.eval(expr)

    expr = "@SOBJECT(simpleslot/game['project_status','.Complete'])"
    complete = server.eval(expr)

    data = gamelist(inprogress, game_tasks)
    test1 = server.update("simpleslot/plan?project=simpleslot&id=8", data)
    print "in progress complete"
    data = gamelist(ready, game_tasks)
    test2 = server.update("simpleslot/plan?project=simpleslot&id=10",data)
    print "ready complete"

    data = gamelist(complete, game_tasks)
    test3 = server.update("simpleslot/plan?project=simpleslot&id=11", data)
    print "complete complete"

    updateRevealFilters()
    print "filters"
    htmlCache()
    print "htmlcache"


    inprogress_sk = 'simpleslot/plan?project=simpleslot&code=PLAN00008'
    ready_sk = 'simpleslot/plan?project=simpleslot&code=PLAN00010'
    complete_sk = 'simpleslot/plan?project=simpleslot&code=PLAN00011'
    server.update(inprogress_sk, {'game_code':gameObjectCount('8')})
    server.update(ready_sk, {'game_code':gameObjectCount('10')})
    server.update(complete_sk, {'game_code':gameObjectCount('11')})


if __name__ == "__main__":
    run() # for addCustomShelf, the rule is filename + Main()

