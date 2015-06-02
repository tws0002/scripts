import sys
sys.path.append("/home/apache/tactic/src/client")
sys.path.append("/mnt/hgfs/assets/scripts/python-dateutil-2.3")
sys.path.append("/mnt/hgfs/assets/scripts/six-1.8.0")
sys.path.append("//Art-1405260002/d/assets/client")
import six
import datetime
now = datetime.datetime.now()
from dateutil import parser

from tactic_client_lib import TacticServerStub
server = TacticServerStub(setup=False)
import socket
tactic_server_ip = socket.gethostbyname("vg.com")
server.set_server(tactic_server_ip)server.set_project("simpleslot")
ticket = server.get_ticket("julio", "1234")
# ticket = "8cc245264e73d48685ded14b6aa431a7" #perpetual ticket?
server.set_ticket(ticket)

expr = "@SOBJECT(simpleslot/game['project_status','.In Progress'])"
inprogress = server.eval(expr)

expr = "@SOBJECT(simpleslot/game['project_status','.Ready'])"
ready = server.eval(expr)

expr = "@SOBJECT(simpleslot/game['project_status','.Complete'])"
complete = server.eval(expr)

names = ""
names_chn = ""
games_type = ""
assignments = ""
bsd_string = ""
bed_string = ""
for game in inprogress:
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


test1 = server.update("simpleslot/plan?project=simpleslot&id=8", {'name': names, 'description': games_type, 'login': bsd_string, 'keywords': bed_string, 'timestamp': str(now), 'game_name_chn': names_chn, 'process': assignments})
print test1
names = ""
names_chn = ""
games_type = ""
assignments = ""
bsd_string = ""
bed_string = ""
for game in ready:
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

test2 = server.update("simpleslot/plan?project=simpleslot&id=10", {'name': names, 'description': games_type, 'login': bsd_string, 'keywords': bed_string, 'timestamp': str(now), 'game_name_chn': names_chn, 'process': assignments})
print test2
names = ""
names_chn = ""
games_type = ""
assignments = ""
bsd_string = ""
bed_string = ""
for game in complete:
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

test3 = server.update("simpleslot/plan?project=simpleslot&id=11", {'name': names, 'description': games_type, 'login': bsd_string, 'keywords': bed_string, 'timestamp': str(now), 'game_name_chn': names_chn, 'process': assignments})
print test3
