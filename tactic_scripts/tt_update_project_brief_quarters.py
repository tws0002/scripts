import sys
sys.path.append("//Art-1405260002/d/assets/client")
import datetime
from dateutil import parser

from tactic_client_lib import TacticServerStub
server = TacticServerStub(setup=False)
import socket
tactic_server_ip = socket.gethostbyname("vg.com")
server.set_server(tactic_server_ip)
server.set_project("simpleslot")
ticket = server.get_ticket("admin", "chicago")
server.set_ticket(ticket)

#['name','combine_cf']
expr = "@SOBJECT(simpleslot/game)"
games = server.eval(expr)

test = []
for game in games:
    sk = game.get("__search_key__")
    code = game.get("code")
    name = game.get("name")
    print name

    expr = "@MAX(simpleslot/game['code','" + code + "'].sthpw/task.bid_end_date)"
    try:
        bed = server.eval(expr)
        bed = parser.parse(bed)
        
   
        if bed.month >= 1 and bed.month <= 3:
            quarter = 'Q1'
        elif bed.month >= 4 and bed.month <= 6:
            quarter = 'Q2'
        elif bed.month >= 7 and bed.month <= 9:
            quarter = 'Q3'
        elif bed.month >= 10 and bed.month <= 12:
            quarter = 'Q4'

        quarter_data = {'brief_quarter': quarter}
        year_data = {'brief_year': bed.year}

        server.update(sk, quarter_data)
        print year_data
    except:
        print "probably no tasks"
        

