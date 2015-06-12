import socket
import sys
sys.path.append("/home/apache/tactic/src/client")
sys.path.append("/mnt/hgfs/assets/scripts/python-dateutil-2.3")
sys.path.append("/mnt/hgfs/assets/scripts/six-1.8.0")


from tactic_client_lib import TacticServerStub
server = TacticServerStub(setup=False)


tactic_server_ip = socket.gethostbyname(socket.gethostname())

server.set_server(tactic_server_ip)
server.set_project("simpleslot")
ticket = server.get_ticket("julio", "1234")
server.set_ticket(ticket)

import datetime
import calendar
import dateutil.parser
from datetime import timedelta
from dateutil import relativedelta

expr = "@SOBJECT(simpleslot/game['begin']['project_status','.In Progress']['project_status','.Complete']['or'])"
#expr = "@SOBJECT(simpleslot/game['project_status','.In Progress'])"
games = server.eval(expr)

expr = "@SOBJECT(simpleslot/task_combine)"
task_combine = server.eval(expr)

task_combine_sk = "simpleslot/task_combine"

data = {}
inlist = []
casino_processes = ["rough","concept","model","texture","effects","rigging","animation","lighting","layout","final"]
asset_processes = ["concept","model","texture","rigging"]
shot_processes = ["layout","animation","effects","lighting","final"]
temp_min = []
temp_max = []


for game in games:
    game_name = game.get("name")
    game_code = game.get("code")
    expr = "@GET(simpleslot/game['code','" + game_code + "'].simpleslot/game_type.name)"
    game_type = server.eval(expr)
    data = {}
    data['game_code'] = game_code

    if game_type[0] == "cf" or game_type[0] == "sports":
        for asset_process in asset_processes:
            expr = "@MIN(simpleslot/game['name','" + game_name + "'].simpleslot/assets.sthpw/task['process','" + asset_process + "'].bid_start_date)"
            temp_min = server.eval(expr)

            expr = "@MAX(simpleslot/game['name','" + game_name + "'].simpleslot/assets.sthpw/task['process','" + asset_process + "'].bid_end_date)"        
            temp_max = server.eval(expr)

            
            if temp_min != None or temp_max != None:
                data["threed_" + asset_process + "_min"] = temp_min
                data["threed_" + asset_process + "_max"] = temp_max            
            
        for shot_process in shot_processes:
            expr = "@MIN(simpleslot/game['name','" + game_name + "'].simpleslot/shot.sthpw/task['process','" + shot_process + "'].bid_start_date)"
            temp_min = server.eval(expr)
            
            expr = "@MAX(simpleslot/game['name','" + game_name + "'].simpleslot/shot.sthpw/task['process','" + shot_process + "'].bid_end_date)"        
            temp_max = server.eval(expr)            

            if temp_min != None or temp_max != None:
                data["threed_" + shot_process + "_min"] = temp_min
                data["threed_" + shot_process + "_max"] = temp_max
        
    if game_type[0] == "casino" or game_type[0] == "video_conf":
    #if game_name == "cf_king_of_hidden_weapons":        
        for casino_process in casino_processes:
            expr = "@MIN(simpleslot/game['name','" + game_name + "'].simpleslot/3d.sthpw/task['process','" + casino_process + "'].bid_start_date)"
            temp_min = server.eval(expr)
            
            expr = "@MAX(simpleslot/game['name','" + game_name + "'].simpleslot/3d.sthpw/task['process','" + casino_process + "'].bid_end_date)"        
            temp_max = server.eval(expr)

            if temp_min != None or temp_max != None:
                data["threed_" + casino_process + "_min"] = temp_min
                data["threed_" + casino_process + "_max"] = temp_max             
    insert = 1
    
    for game_in_combine in task_combine: #match combine list names to master list, if match, only update. 
        code = game_in_combine.get("game_code")
        sk = game_in_combine.get("__search_key__")
        if code == game_code:
            inlist.append(data)
            
            server.update(sk,data)
            insert = 0
            break
            
    if insert == 1: #if game not in combine list, insert
        server.insert(task_combine_sk,data)
        inlist.append(data)
            


#return inlist


