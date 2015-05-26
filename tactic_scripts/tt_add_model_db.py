import sys
sys.path.append("//Art-1405260002/d/assets/client")

import os
from tactic_client_lib import TacticServerStub
server = TacticServerStub.get()
server.set_server("192.168.201.10")
server.set_project("simpleslot")
ticket = server.get_ticket("julio", "1234")
server.set_ticket(ticket)

#mixamo = "d:\\mixamo\\"
mixamo = "//Art-1405260002/d/assets/simpleslot/model_db/"
model_list = [d for d in os.listdir(mixamo) if 'Thumbs' not in d]

#not_yet = []
for model in model_list:
    #model = temp[0]
    model_dir = mixamo + model
    content = []
    files = os.listdir(model_dir)
    fbx_file = [f for f in files if "fbx" in f]
    
    if len(files) > 2:
        info_file = model_dir + "/info.txt"
        with open(info_file) as file_object:
            content = file_object.read().splitlines()
            name = content[0].replace("name=","")
            description = content[1].replace("tags=","")
            link = "/assets/simpleslot/model_db/" + model + "/" + fbx_file[0]
            login = "mixamo"
            data = {'name': name, 'description': description, 'link': link, 'login': login}
    sobj = server.insert('simpleslot/model_db', data)
    
    
    sk = sobj.get('__search_key__')
    snapshot = server.create_snapshot(sk, 'none')
    snapshot_code = snapshot.get('code')
    
    file_path = '/mnt/hgfs/assets/simpleslot/model_db/' + model + '/' + model + '.gif'
    server.add_file(snapshot_code, file_path, file_type='web', use_handoff_dir=False, mode='inplace', create_icon=False)
