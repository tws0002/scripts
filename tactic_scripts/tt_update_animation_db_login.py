import sys
sys.path.append("//Art-1405260002/d/assets/client")

import os
from tactic_client_lib import TacticServerStub
server = TacticServerStub.get()
import socket
tactic_server_ip = socket.gethostbyname("vg.com")
server.set_server(tactic_server_ip)
server.set_project("simpleslot")
ticket = server.get_ticket("julio", "1234")
server.set_ticket(ticket)

expr = "@SOBJECT(simpleslot/animation_db)"
animations = server.eval(expr)


for anim in animations:
    sk = anim.get("__search_key__")
    
    snapshot = server.get_snapshot(sk, context='none', include_files=True)
    snapshot_sk = snapshot.get("__search_key__")
    
    snapshot_file = server.get_all_children(snapshot_sk, 'sthpw/file')
    snapshot_file_sk = snapshot_file[0].get("__search_key__")
    
    server.delete_sobject(snapshot_file_sk)
    server.delete_sobject(snapshot_sk)
    server.delete_sobject(sk)