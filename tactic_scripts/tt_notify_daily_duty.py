import datetime
import time
import sys
sys.path.append("//Art-1405260002/d/assets/client")
import socket
from tactic_client_lib import TacticServerStub
import Skype4Py

start_time = time.time()

server = TacticServerStub(setup=False)

tactic_server_ip = socket.gethostbyname("vg.com")

server.set_server(tactic_server_ip)
server.set_project("simpleslot")
ticket = server.get_ticket("julio", "1234")
server.set_ticket(ticket)


skype = Skype4Py.Skype()
client = skype.Client
if not client.IsRunning:
    client.Start()
skype = Skype4Py.Skype()
skype.Attach()

now = datetime.datetime.now()
today_string = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
expr = "@SOBJECT(simpleslot/daily_duty_schedule['day','" + today_string + "'])"
duty = server.eval(expr)


for d in duty:
    worker1 = d.get("name").split(",")[1].replace(" ", "")
    worker2 = d.get("name1").split(",")[1].replace(" ", "")
    expr = "@SOBJECT(sthpw/login['begin']['login','" + worker1 + "']['login','" + worker2 + "']['or'])"
    logins = server.eval(expr)

    for login in logins:
        name = login.get('login')
        if name == 'julio':
            pass
        else:
            skypename = login.get('skype')
            final = today_string + "\n" + worker1 + "跟".decode('utf-8') + worker2 + "是今天值日生，請:".decode('utf-8') + "\n" + "1.冰箱整潔維護與微波爐旁邊檯面整潔。".decode('utf-8') + "\n" + "2.便當桌整潔。".decode('utf-8') + "\n" + "3.公共區域地板整潔。".decode('utf-8') + "\n"

            skype.SendMessage(skypename, final)
            print skypename


#end_time = time.time()
#diff = start_time - end_time
#print("--- %s seconds ---" % diff)
