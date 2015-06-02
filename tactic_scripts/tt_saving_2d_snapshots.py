import sys
sys.path.append("//Art-1405260002/d/assets/client")

from tactic_client_lib import TacticServerStub
server = TacticServerStub(setup=False)

import socket
tactic_server_ip = socket.gethostbyname("vg.com")
server.set_server(tactic_server_ip)
server.set_project("simpleslot")
ticket = server.get_ticket("admin", "chicago")
# ticket = "8cc245264e73d48685ded14b6aa431a7" #perpetual ticket?
server.set_ticket(ticket)


game_code = "GAME0070"
expr = "@SOBJECT(simpleslot/package['game_code','" + game_code + "'])"
game = server.eval(expr)
game_pkg_sk = game[0].get("__search_key__")
game_pkg_code = game[0].get("code")

expr = "@SOBJECT(sthpw/task['search_code','" + game_pkg_code + "'])"
tasks = server.eval(expr)

newlist = []
keyorder = ['layout', 'demo', 'output', 'pkg_flash', 'pkg_unity', 'web', 'banner', 'qc']
newlist = sorted(tasks, key=lambda i: keyorder.index(i['process']), reverse=True)


for task in newlist:
    search_type = "simpleslot/package?project=simpleslot"
    search_code = task.get("search_code") # this points to game_package_code
    process = task.get("process")
    search_id = ""
    
    code = task.get("code")
    pipeline_code = task.get("pipeline_code")
    context = task.get("context")

    status = task.get("status")
    bsd = task.get("bid_start_date")
    bed = task.get("bid_end_date")
    assigned = task.get("assigned")
    data = {'search_code':search_code, 'process': process, 'status': status, 'assigned':assigned, 'bid_start_date':bsd, 'bid_end_date':bed, 'search_type':search_type, 'pipeline_code': pipeline_code, 'context': context}
    new_task = server.insert("sthpw/task", data)
    new_task_code = new_task.get("code")

    expr = "@SOBJECT(sthpw/snapshot['search_code','" + code + "'])"
    snapshots = server.eval(expr)

    for snapshot in snapshots:
        print snapshot.get("context")
        snapshot_sk = snapshot.get("__search_key__")
        
        snapshot_data = {'search_code': new_task_code}
        server.update(snapshot_sk, snapshot_data)
    
