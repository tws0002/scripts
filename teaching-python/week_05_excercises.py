# -*- coding: utf-8 -*-
import sys
import socket
import os
sys.path.append("//Art-1405260002/d/assets/client")
#sys.path.append("//art-render/art_3d_project/client")
ticket_path = "c:/sthpw/etc"
tactic_server_ip = socket.gethostbyname("vg.com")

name = "julio"
password = "1234"

if os.path.exists(ticket_path) is False:
    os.makedirs(ticket_path)

ticket_file = "c:/sthpw/etc/" + name + ".tacticrc"

if os.path.isfile(ticket_file) is False:
    with open(ticket_file, 'w') as file_object:
        ticket_content = "login=" + name + "\n" + "server=" + tactic_server_ip + "\n" + "project=simpleslot"
        file_object.write(ticket_content)

from tactic_client_lib import TacticServerStub
server = TacticServerStub(setup=False)

server.set_server(tactic_server_ip)
server.set_project("simpleslot")
ticket = server.get_ticket(name, password)
server.set_ticket(ticket)

expr= "@SOBJECT(sthpw/login)"
logins = server.eval(expr)

expr = "@GET(sthpw/login.login)"
names = server.eval(expr)

filepath = "c:\loginList.txt"

with open(filepath,"w") as datafile:
    for x in logins:
        datafile.write(str(x) + "\n")
        
with open(filepath, "wb") as datafile:
    pickle.dump(logins, datafile, pickle.HIGHEST_PROTOCOL)
        



#-----------------------------------------------------------------------

# 1. logins 資料類型是? 若有子資料類型，請也列出來

# 2. names 資料類型是? 若有子資料類型，請也列出來

# 3. 請把你的資料從 logins 裡找出來 
# 請寫成 function, return dictionary
def findYourself():
	# 寫這裡	

# 4. 請從 logins 裡找出大家的分機號碼(ext), 做成一個新的list
# 請寫成 function, return list
def allExt():
	# 寫這裡	

# 5. 請從 logins 裡找出大家的分機號碼(ext), 做成一個新的dictionary list, 
# 裡面有 login 跟 ext
# 請寫成 function, return dictionary list
def allExtDict():
	# 寫這裡	

def main():
	findYourself()
	allExt()
	allExtDict()

if __name__ == '__main__':
	main()	 





