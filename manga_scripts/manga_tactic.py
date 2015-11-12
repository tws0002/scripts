import sys
import unicodecsv
sys.path.append("//Art-1405260002/d/assets/client")

import os
from tactic_client_lib import TacticServerStub
server = TacticServerStub.get()
server.set_server("192.168.163.60")
server.set_project("simpleslot")
ticket = server.get_ticket("julio", "1234")
server.set_ticket(ticket)

#%%
csv_path = r"f:/manga_list08.csv"
csv_list = []
with open(csv_path, 'r') as csvfile:
    csv_content = unicodecsv.reader(csvfile, delimiter=',', lineterminator='\n')
    for row in csv_content:
        csv_list.append(row)

path = "//Art-1405260002/d/assets/manga/"

ignore_dir = ["css", "templates", "images", "covers", "mcd_covers"]
mangas = [m for m in os.listdir(path) if m not in ignore_dir if os.path.isdir(os.path.join(path,m))]


expr = "@GET(simpleslot/mangas.folder_name)"
tactic_mangas = server.eval(expr)

#%%
for manga in mangas:
    print manga
    
    html_path = "http://vg.com/assets/manga/%s/index.html" % (manga)
    csv_manga = [x[2] for x in csv_list]
    if manga not in csv_manga or manga in tactic_mangas:
        pass
    else:
        muid, title, folder_name, name_chn, alternate_names, tags, author_chn, artist, author, year, volumes, status, description, mcd_covers = [(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13]) for x in csv_list if x[2] == manga][0]
        description = description.replace("**",",")
        tags = tags.replace(r"[","").replace(r"]","").replace(r"'","")
        
        data = {
            'muid':muid,
            'name':title,
            'folder_name': folder_name,
            'name_chn': name_chn,
            'alternate_names': alternate_names,
            'tags': tags,
            'author_chn': author_chn,
            'artist': artist,
            'author': author,
            'year': year,
            'volumes': volumes,
            'status': status,
            'description': description,
            'mcd_covers': mcd_covers,
            'link': html_path
        }
        sobj = server.insert('simpleslot/mangas', data)

        sk = sobj.get('__search_key__')
        snapshot = server.create_snapshot(sk, 'none')
        snapshot_code = snapshot.get('code')
        
        if mcd_covers == 'True':        
            cover_link = "/mnt/hgfs/assets/manga/mcd_covers/%s/vol_01_front_med.jpg" % (manga)
            server.add_file(snapshot_code, cover_link, file_type='web', use_handoff_dir=False, mode='inplace', create_icon=False)        
        elif mcd_covers == 'False':
            cover_path = "/mnt/hgfs/assets/manga/covers/%s" % (manga)
            nfs_path = "//art-1405260002/d/assets/manga/covers/%s" % manga
            try:
                ext = os.listdir(nfs_path)[0].split(".")[1]
                cover_link = "/mnt/hgfs/assets/manga/covers/%s/Vol_01.%s" % (manga, ext)
                server.add_file(snapshot_code, cover_link, file_type='web', use_handoff_dir=False, mode='inplace', create_icon=False)        
            except:
                pass







