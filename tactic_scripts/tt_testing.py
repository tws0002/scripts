import sys
sys.path.append("//Art-1405260002/d/assets/client")

from tactic_client_lib import TacticServerStub
server = TacticServerStub(setup=False)
server.set_server("192.168.200.60")
server.set_project("simpleslot")
ticket = server.get_ticket("admin", "chicago")

server.set_ticket(ticket)


a = ['key', 'duke', 'samurai', 'joey_chen', 'una_wang', 'alpha', 'chihjung']
b = ['xeno_lee','dave', 'ison_lee', 'kenny_hou', 'mask_chang', 'michael922', 'tong', 'yi_lun']
c = a + b


for x in c:
    filters = filters +  "[\'login\',\'" + x + "\']"

expr = "@SOBJECT(sthpw/login['begin']['login','julio']['login','alpha']['or'])"
expr =  "@SOBJECT(sthpw/login['begin']" + filters + "['or'])"
test = server.eval(expr)

@SOBJECT(sthpw/login['begin']['login','yi_lun']['login','key']['login','duke']['login','samurai']['login','joey_chen']['login','una_wang']['login','alpha']['login','chihjung']['login','xeno_lee']['login','dave']['login','ison_lee']['login','kenny_hou']['login','mask_chang']['login','michael922']['login','tong']['login','yi_lun']['login','key']['login','duke']['login','samurai']['login','joey_chen']['login','una_wang']['login','alpha']['login','chihjung']['login','xeno_lee']['login','dave']['login','ison_lee']['login','kenny_hou']['login','mask_chang']['login','michael922']['login','tong']['login','yi_lun']['or'])