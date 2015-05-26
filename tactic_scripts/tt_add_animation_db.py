# -*- coding: utf-8 -*-
"""
Created on Thu May 07 16:02:50 2015

@author: julio
"""

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
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
        
mixamo = "//Art-1405260002/d/assets/simpleslot/animation_db/"
animations = [d for d in os.listdir(mixamo) if RepresentsInt(d)]

#not_yet = []

for x in animations:
    anim_dir = mixamo + str(x)
    content = []
    files = os.listdir(anim_dir)
    fbx_file = [f for f in files if "fbx" in f]
    
    if len(files) > 2:
        info_file = anim_dir + "/info.txt"
        with open(info_file) as file_object:
            content = file_object.read().splitlines()
            name = content[0].replace("name=","")
            description = content[1].replace("description=","")
            temp = content[2].replace("duration=","")
            duration = temp.split(" ")[0]
            frames = temp.split(" ")[2].replace("(","")
            link = "/assets/simpleslot/animation_db/" + str(x) + "/" + fbx_file[0]
            data = {'name': name, 'description': description, 'duration': duration, 'frames': frames, 'link': link, 'login': 'mixamo'}
    
    sobj = server.insert('simpleslot/animation_db', data)
    
    sk = sobj.get('__search_key__')
    snapshot = server.create_snapshot(sk, 'none')
    snapshot_code = snapshot.get('code')
    
    file_path = '/mnt/hgfs/assets/simpleslot/animation_db/' + str(x) + '/' + str(x) + '.gif'
    server.add_file(snapshot_code, file_path, file_type='web', use_handoff_dir=False, mode='inplace', create_icon=False)
