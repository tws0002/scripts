import sys
sys.path.append("//Art-1405260002/d/assets/client")

from tactic_client_lib import TacticServerStub
server = TacticServerStub(setup=False)
server.set_server("192.168.201.10")
#server.set_server("192.168.200.110")
server.set_project("simpleslot")
ticket = server.get_ticket("admin", "chicago")
server.set_ticket(ticket)

expr = "@SOBJECT(sthpw/login)"
logins = server.eval(expr)
#logins = ['fish_hung', 'alpha']
#6965 = shot
#6270 = asset
#6264 = casino

widget_template_id = 6264

expr = "@SOBJECT(sthpw/wdg_settings['id','" + str(widget_template_id) + "'])"
widget_template = server.eval(expr)[0]

wkey = widget_template.get("key")
wlogin = widget_template.get("login")
wdata = widget_template.get("data")
wproject_code = widget_template.get("project_code")

expr = "@GET(sthpw/wdg_settings['key','" + wkey + "'].login)"
existing_login = server.eval(expr)

for login in logins:
    name = login.get("login")
    if name not in existing_login:
        data = {'key': wkey, 'login': name, 'data': wdata, 'project_code': wproject_code}
        server.insert("sthpw/wdg_settings", data)



