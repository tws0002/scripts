import datetime
from dateutil import parser
import time

start_time = time.time()
import sys
sys.path.append("//Art-1405260002/d/assets/client")

from tactic_client_lib import TacticServerStub
server = TacticServerStub()

server.set_server("192.168.201.10")
server.set_project("simpleslot")
ticket = server.get_ticket("julio", "1234")
server.set_ticket(ticket)

import Skype4Py

skype = Skype4Py.Skype()
client = skype.Client
if not client.IsRunning:
    client.Start()
skype.Attach()

expr = "@GET(sthpw/login['begin']['department','sound']['department','producers']['or'].skype)"
names = server.eval(expr)

buddies = skype.Friends

buddylist = [x.Handle for x in buddies]


for name in names:
    if name not in buddylist:
        print name
        
        client.OpenAddContactDialog(name)
        time.sleep(5)

        
    
    
