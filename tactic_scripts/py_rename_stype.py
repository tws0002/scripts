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

'''
expr = "@SOBJECT(simpleslot/package)"
items = server.eval(expr)

test = []

for item in items:
    sk = item.get("__search_key__")
    code = item.get("code")
    pipeline_code = item.get("pipeline_code")
    code = code.replace("2D","PACKAGE")
    pipeline_code = pipeline_code.replace("2d", "package")
    test.append(sk)
    data = {'code': code}
    server.update(sk, data)
print testexpr = "@SOBJECT(sthpw/task['search_type','simpleslot/2d?project=simpleslot'])"
tasks = server.eval(expr)

test = []
for task in tasks:
    sk = task.get("__search_key__")
    search_code = task.get("search_code")
    search_type = "simpleslot/package?project=simpleslot"
    if search_code[:2] == "2D":
        search_code = search_code.replace("2D","PACKAGE")
        data = {'search_code': search_code, 'search_type': search_type}
        test.append(search_type)
        server.update(sk, data)

expr = "@SOBJECT(sthpw/task['process','package'])"
tasks = server.eval(expr)
test = []
for task in tasks:
    sk = task.get("__search_key__")
    process = "pkg_flash"
    data = {'process': process}
    server.update(sk, data)
print test
expr = "@SOBJECT(sthpw/note['search_type','simpleslot/package?project=simpleslot'])"
notes = server.eval(expr)
test = []
for note in notes:
    sk = note.get("__search_key__")
    search_code = note.get("search_code")
    search_code = search_code.replace("2D","PACKAGE")
    data = {'search_code': search_code}
    server.update(sk, data)
'''
expr = "@SOBJECT(sthpw/file['search_type','simpleslot/package?project=simpleslot'])"
snapshots = server.eval(expr)
test = []
for snapshot in snapshots:
    sk = snapshot.get("__search_key__")
    search_code = snapshot.get("search_code")
    if search_code[:2] == "2D":
        search_code = search_code.replace("2D","PACKAGE")
        test.append(search_code)
        data = {'search_code': search_code}
        server.update(sk, data)
print test
