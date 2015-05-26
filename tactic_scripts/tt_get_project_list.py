import sys
sys.path.append("//Art-1405260002/d/assets/client")

from tactic_client_lib import TacticServerStub
server = TacticServerStub(setup=False)
server.set_server("192.168.201.10")
#server.set_server("192.168.200.110")
server.set_project("simpleslot")
ticket = server.get_ticket("admin", "chicago")
# ticket = "8cc245264e73d48685ded14b6aa431a7" #perpetual ticket?
server.set_ticket(ticket)

inprogress_filter = "['id','8']"
ready_filter = "['id','10']"
complete_filter = "['id','11']"
        
expr = "@SOBJECT(simpleslot/plan['begin']" + inprogress_filter + ready_filter + complete_filter + "['or'])"
temp = server.eval(expr)
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
