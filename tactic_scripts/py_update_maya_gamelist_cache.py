#this is a scheduled script that updates the cache the maya, nuke, etc filemanagers uses 
#the data are written to simpleslot/plan id 8 for inprogress, 10 for commplte, 11 for ready

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



def gamelist(items):
    names = ""
    names_chn = ""
    games_type = ""
    assignments = ""
    bsd_string = ""
    bed_string = ""

    for game in items:
        name = game.get("name")
        name_chn = game.get("name_chn")
        search_code = game.get("code")
        expr = "@SOBJECT(sthpw/task['search_code','" + search_code + "'])"
        depts = server.eval(expr)
    
        expr = "@GET(simpleslot/game['name','" + name + "'].simpleslot/game_type.name)"
        game_type = server.eval(expr)
        for dept in depts:
            dept_name = dept.get("process")
            if dept_name == "3d":
                bsd = dept.get("bid_start_date")
                bsd = parser.parse(bsd)
                bsd = bsd.strftime("%m/%d/%y")
                bed = dept.get("bid_end_date")
                bed = parser.parse(bed)
                bed = bed.strftime("%m/%d/%y")
                bsd_string = bsd_string + "__" + (bsd)
                bed_string = bed_string + "__ " + (bed)
                assignment = dept.get("assigned")
                assignments = assignments + " " + assignment
                names = names + " " + name
                games_type = games_type + " " + game_type[0]
                names_chn = names_chn + "__" + name_chn
    data = {'name': names, 'description': games_type, 'login': bsd_string, 'keywords': bed_string, 'timestamp': str(now), 'game_name_chn': names_chn, 'process': assignments}
    return data

def run():
    expr = "@SOBJECT(simpleslot/game['project_status','.In Progress'])"
    inprogress = server.eval(expr)
    
    expr = "@SOBJECT(simpleslot/game['project_status','.Ready'])"
    ready = server.eval(expr)
    
    expr = "@SOBJECT(simpleslot/game['project_status','.Complete'])"
    complete = server.eval(expr)
    data = gamelist(inprogress)    
    test1 = server.update("simpleslot/plan?project=simpleslot&id=8", data)
    
    data = gamelist(ready)
    test2 = server.update("simpleslot/plan?project=simpleslot&id=10",data)
    
    data = gamelist(complete)
    test3 = server.update("simpleslot/plan?project=simpleslot&id=11", data)
    


