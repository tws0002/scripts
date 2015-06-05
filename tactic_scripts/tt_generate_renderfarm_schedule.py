import sys
import socket
sys.path.append("//Art-1405260002/d/assets/client")
sys.path.append("c:/python27/lib/site-packages/pytz-2015.4-py2.7.egg")
sys.path.append("c:/python27/lib/site-packages/six-1.9.0-py2.7.egg")
sys.path.append("c:/python27/scripts/python-dateutil-2.4.2")
sys.path.append("c:/python27/lib/site-packages/")
import datetime
import six
from dateutil import parser
import time
start_time = time.time()

from tactic_client_lib import TacticServerStub
server = TacticServerStub()

tactic_server_ip = socket.gethostbyname("vg.com")

server.set_server(tactic_server_ip)
server.set_project("simpleslot")
ticket = server.get_ticket("julio", "1234")
server.set_ticket(ticket)

expr = "@GET(simpleslot/game['project_status','.In Progress'].name)"
games = server.eval(expr)

for game in games:
    expr = "@MAX(simpleslot/game['name','" + game + "'].simpleslot/3d.sthpw/task['process','lighting'].bid_end_date)"
    bed = server.eval(expr)
    
    expr = "@MIN(simpleslot/game['name','" + game + "'].simpleslot/3d.sthpw/task['process','lighting'].bid_start_date)"
    bsd = server.eval(expr)
    print game, bsd, bed
