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


name = "burst_fruit_plate"
stype = "3d"
expr = "@SOBJECT(simpleslot/game['name','" + name + "'].simpleslot/" + stype + ")"
game = server.eval(expr)

print len(game)
