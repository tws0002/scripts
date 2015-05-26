import sys
sys.path.append("//Art-1405260002/d/assets/client")

from tactic_client_lib import TacticServerStub
server = TacticServerStub(setup=False)
server.set_server("192.168.201.10")
server.set_project("simpleslot")
ticket = server.get_ticket("julio", "1234")
# ticket = "8cc245264e73d48685ded14b6aa431a7" #perpetual ticket?
server.set_ticket(ticket)

expr = "@SOBJECT(simpleslot/game['name','burst_fruit_plate'].simpleslot/3d)"
items = server.eval(expr)

for item in items:
    sk = item.get("__search_key__")
    name = item.get("name").lower()
    data = {'name': name}
    server.update(sk, data)            
    

'''
names = ""
names_chn = ""
games_type = ""
assignments = ""
bsd_string = ""
bed_string = ""
for game in games:
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


test = server.update("simpleslot/plan?project=simpleslot&id=8", {'name': names, 'description': games_type, 'login': bsd_string, 'keywords': bed_string, 'timestamp': str(now), 'game_name_chn': names_chn, 'process': assignments})
print test
'''
