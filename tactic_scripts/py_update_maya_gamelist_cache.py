#this is a scheduled script that updates the cache the maya, nuke, etc filemanagers uses
#the data are written to simpleslot/plan id 8 for inprogress, 10 for commplte, 11 for ready

import time
from operator import itemgetter
import sys
import socket
sys.path.append("/home/apache/tactic/src/client")
sys.path.append("/mnt/hgfs/assets/scripts/python-dateutil-2.3")
sys.path.append("/mnt/hgfs/assets/scripts/six-1.8.0")
sys.path.append("//Art-1405260002/d/assets/client")
sys.path.append("//Art-1405260002/d/assets/scripts/python-dateutil-2.3")
sys.path.append("//Art-1405260002/d/assets/scripts/six-1.8.0")

from tactic_client_lib import TacticServerStub
server = TacticServerStub.get()
tactic_server_ip = socket.gethostbyname("vg.com")
server.set_server(tactic_server_ip)
server.set_project("simpleslot")
ticket = server.get_ticket("julio", "1234")
server.set_ticket(ticket)


import six
import datetime
now = datetime.datetime.now()
from dateutil import parser
#%%
def gamelist(items):
    now = datetime.datetime.now()
    names = ""
    names_chn = ""
    games_type = ""
    assignments = ""
    bsd_string = ""
    bed_string = ""

    for game in items:
        bsd = []
        bed = []
        name = game.get("name")
        name_chn = game.get("name_chn")
        search_code = game.get("code")
        expr = "@SOBJECT(sthpw/task['search_code','" + search_code + "'])"
        depts = server.eval(expr)

        expr = "@GET(simpleslot/game['name','" + name + "'].simpleslot/game_type.name)"
        game_type = server.eval(expr)
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
        games_type = games_type + "__" + game_type[0]
        names_chn = names_chn + "__" + name_chn
    data = {'name': names, 'description': games_type, 'login': bsd_string, 'keywords': bed_string, 'timestamp': str(now), 'game_name_chn': names_chn, 'process': assignments}
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
    data = {'description': html}
    server.update("simpleslot/plan?project=simpleslot&id=809", data)
    return html
    print "html cache generated"

#%%
def pkgtypecount(items):
    layout = demo = 0
    for item in items:
        code = item.get('code')
        exp = "@SOBJECT(sthpw/file['code','" + code + "'].parent.parent)"
        obj = server.eval(exp)[0]
        temp = str(obj.get('process'))
        if temp == 'layout':
            layout = layout + 1
        elif temp == 'demo':
            demo = demo + 1
    return[layout, demo]

def asttypecount(items):
    ast_char = ast_vehicle = ast_set = ast_prop = ast_other = 0
    for item in items:
        code = item.get('code')
        exp = "@SOBJECT(sthpw/file['code','" + code + "'].parent.parent.parent)"
        try:    
            obj = server.eval(exp)[0]
            temp = str(obj.get('asset_type_code'))
    
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
        code = item.get('code')
        exp = "@SOBJECT(sthpw/file['code','" + code + "'].parent.parent.parent)"
        try:    
            obj = server.eval(exp)[0]
            temp = str(obj.get('3d_type_code'))
    
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

def updateRevealFilters():
    filetype = "main"
    exp = "@SOBJECT(simpleslot/game['project_status','NEQ','.Hidden']['project_status','NEQ','.Complete']['project_status','NEQ','.Not Ready']['project_status','NEQ','.Ready'])"
    games = server.eval(exp)
    
    inprogress = []
    ready = []
    complete = []
    notready = []
    
    items = []
    typecodenames = ["character", "symbol", "user_interface", "bonus01", "bonus02", "free_game", "jackpot", "introduction"]
    typecodes = ["3D_TYPE00002", "3D_TYPE00003", "3D_TYPE00004", "3D_TYPE00005", "3D_TYPE00006", "3D_TYPE00007", "3D_TYPE00008", "3D_TYPE00009"]
    assetcodenames = ["character", "vehicle", "set", "prop", "other"]
    assetcodes = ["ASSET_TYPE00002","ASSET_TYPE00003", "ASSET_TYPE00004", "ASSET_TYPE00005", "ASSET_TYPE00006"]
    
    for game in games:
        sk = game.get("__search_key__")
        name = game.get("name")
        keyword = game.get("keywords")
        #print name
    
        exp = "@SOBJECT(simpleslot/game['name','" + name + "'].simpleslot/3d.sthpw/task.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
        threedfiles = server.eval(exp)
        items = threedfiles
    
        #if len(threedfiles) == 0: #if theres something in 3d, then there's nothing in asset or shot, proceed to 2d
        exp = "@SOBJECT(simpleslot/game['name','" + name + "'].simpleslot/assets.sthpw/snapshot.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
        assetfiles = server.eval(exp)
        filter_asset = asttypecount(assetfiles)
        items = items + assetfiles
    
        exp = "@SOBJECT(simpleslot/game['name','" + name + "'].simpleslot/shot.sthpw/task.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
        shotfiles = server.eval(exp)
        items = items + shotfiles
    
        filter_asset.append(len(shotfiles))
        filter_3d = typecount(threedfiles)
    
        exp = "@SOBJECT(simpleslot/game['name','" + name + "'].simpleslot/package.sthpw/task.sthpw/snapshot.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
        packagefiles = server.eval(exp)
        filter_package = pkgtypecount(packagefiles)
        items = items + packagefiles
    
        ff = ""
        for ch in filter_3d:
            ff = ff + "," + str(ch)
        for ch in filter_asset:
            ff = ff + "," + str(ch)
        for ch in filter_package:
            ff = ff + "," + str(ch)        
        #ff = ff + "," + str(len(packagefiles))
    
        if len(items) > 0:
            data = {'keywords': len(items), 'description': ff[1:]}
        else:
            data = {'keywords': 0, 'description': 0}
        #print data
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

#%%

def run():
    expr = "@SOBJECT(simpleslot/game['project_status','.In Progress'])"
    inprogress = server.eval(expr)

    expr = "@SOBJECT(simpleslot/game['project_status','.Ready'])"
    ready = server.eval(expr)

    expr = "@SOBJECT(simpleslot/game['project_status','.Complete'])"
    complete = server.eval(expr)

    data = gamelist(inprogress)
    test1 = server.update("simpleslot/plan?project=simpleslot&id=8", data)
    print "in progress complete"
    data = gamelist(ready)
    test2 = server.update("simpleslot/plan?project=simpleslot&id=10",data)
    print "ready complete"

    data = gamelist(complete)
    test3 = server.update("simpleslot/plan?project=simpleslot&id=11", data)
    print "complete complete"

    updateRevealFilters()
    htmlCache()

    inprogress_sk = 'simpleslot/plan?project=simpleslot&code=PLAN00008'
    ready_sk = 'simpleslot/plan?project=simpleslot&code=PLAN00010'
    complete_sk = 'simpleslot/plan?project=simpleslot&code=PLAN00011'
    server.update(inprogress_sk, {'game_code':gameObjectCount('8')})
    server.update(ready_sk, {'game_code':gameObjectCount('10')})
    server.update(complete_sk, {'game_code':gameObjectCount('11')})


if __name__ == "__main__":
    run() # for addCustomShelf, the rule is filename + Main()

