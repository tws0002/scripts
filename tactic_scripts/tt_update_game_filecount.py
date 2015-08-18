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

#-----------------------------------------------

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
    

