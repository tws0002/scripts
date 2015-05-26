import sys
sys.path.append("//Art-1405260002/d/assets/client")
sys.path.append("//Art-1405260002/d/assets/scripts/maya_scripts/lib")
sys.path.append("//Art-1405260002/d/assets/scripts/maya_scripts")
sys.path.append("//Art-1405260002/d/assets/scripts/install")

import os
from tactic_client_lib import TacticServerStub

ticket_path = "c:/sthpw/etc"

if os.path.exists(ticket_path) is False:
    os.makedirs(ticket_path)

#name = self.ui.login.text()
#password = self.ui.password.text()
name = 'julio'
password = '1234'

ticket_files = os.listdir("c:/sthpw/etc/")
ticket_file = "c:/sthpw/etc/" + name + ".tacticrc"

if len(ticket_files) == 0:
    file_object = open(ticket_file, "w")
    ticket_content = "login=" + name + "\n" + "server=192.168.201.10" + "\n" + "project=simpleslot"
    file_object.write(ticket_content)
    file_object.close()

server = TacticServerStub(setup=0)
server.login = name
server.set_server("192.168.201.10")
server.set_project("simpleslot")
ticket = server.get_ticket(name, password)
server.set_ticket(ticket)

file_object = open(ticket_file, "w")
ticket_content = "login=" + name + "\n" + "server=192.168.201.10" + "\n" + "ticket=" + ticket + "\n" + "project=simpleslot"
file_object.write(ticket_content)
file_object.close()
