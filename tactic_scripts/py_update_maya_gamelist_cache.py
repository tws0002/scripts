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
    
if __name__ == "__main__":
    run() # for addCustomShelf, the rule is filename + Main()

