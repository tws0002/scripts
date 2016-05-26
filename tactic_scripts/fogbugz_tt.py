import sys
sys.path.append("//Art-1405260002/d/assets/client")

try:
    tactic_server_ip = socket.gethostbyname("vg.com")
except:
    tactic_server_ip = "192.168.163.60"

from tactic_client_lib import TacticServerStub
server = TacticServerStub(setup=False)
server.set_server(tactic_server_ip)
server.set_project("simpleslot")
ticket = server.get_ticket("admin", "chicago")

server.set_ticket(ticket)
#%%
     
expr = "@SOBJECT(sthpw/task['assigned','steve_ho'])"
temp = server.eval(expr)


#%%

print len(temp)

for x in temp:
    print x['bid_start_date']
#%%
names = ""
bsd = ""
bed = names_chn = games_type = assigned = ""
for x in temp: #range(0,len(temp)):
    names = names + x.get('name')
    bsd = bsd + x.get('login')
    bed = bed + x.get('keywords')
    names_chn = names_chn + x.get('game_name_chn')
    games_type = games_type + x.get('description')
    assigned = assigned + x.get('process')

projects_list = {'name': names, 'login': bsd, 'keywords': bed, 'game_name_chn': names_chn, 'description': games_type, 'process': assigned}
print projects_list.get('name')

