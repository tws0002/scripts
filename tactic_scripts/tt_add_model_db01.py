import sys
sys.path.append("//Art-1405260002/d/assets/client")

import os
import socket
import threading
import Queue


from tactic_client_lib import TacticServerStub

server = TacticServerStub.get()
tactic_server_ip = socket.gethostbyname("vg.com")
server.set_server(tactic_server_ip)
server.set_project("simpleslot")
ticket = server.get_ticket("julio", "1234")
server.set_ticket(ticket)


base_path = "f:/3daa"
model_folders = [d for d in os.listdir(base_path) if 'Thumbs' not in d]

model_folders = model_folders[30840:40000]

for model_folder in model_folders:
    print model_folder
    model_folder_path = base_path + "/" + model_folder
    model_folder_files = []
    model_folder_files = os.listdir(model_folder_path)
    
    rar_file = [f for f in model_folder_files if ".rar" in f][0]
    jpg_file = [g for g in model_folder_files if ".jpg" in g][0]
        
    
    if len(model_folder_files) > 2:
        info_file = model_folder_path + "/info.txt"
        with open(info_file) as file_object:
            content = file_object.read().split(",")

        keywords = content[2] + ", " + content[3] + ", " + content[4] # this is chinese
        description = content[7] + ", " + content[8] + ", " + content[9] # this is english
        name = content[9]
        link = "/assets/simpleslot/model_db01/" + model_folder + "/" + rar_file
        login = "3d66"
        software = content[1]
        
        data = {'name': name, 'description': description, 'link': link, 'login': login, 'software': software, 'keywords': keywords}
    
        if len(content) > 7:
            sobj = server.insert('simpleslot/model_db', data)
            sk = sobj.get('__search_key__')
            snapshot = server.create_snapshot(sk, 'none')
            snapshot_code = snapshot.get('code')
            
            file_path = '/mnt/hgfs/assets/simpleslot/model_db01/' + model_folder + '/' + jpg_file
            ss_sk = server.add_file(snapshot_code, file_path, file_type='web', use_handoff_dir=False, mode='inplace', create_icon=False)
        else:
            print "bad"

       