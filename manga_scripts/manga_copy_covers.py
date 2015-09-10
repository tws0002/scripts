# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 13:55:34 2015

@author: julio
"""
import os
import shutil

path = r"d:/manga/"
ignore_dir = ["css", "templates", "images", "cover", "Thumbs.db", "desktop.ini"]
mangas = [m for m in os.listdir(path) if m not in ignore_dir if os.path.isdir(os.path.join(path,m))]
last_pos = mangas.index("one_punch_man") + 1
mangas = mangas[last_pos:]
for manga in mangas:
    #chapters = [x[1] for x in os.walk((path + manga).decode('utf8'))][0]
    chapters = [x for x in os.listdir(path + manga) if "html" not in x and x not in ignore_dir]
    print manga
    i = 0
    cover_test_path = ("d:/cover/" + manga)
    try:        
        os.mkdir(cover_test_path)
    except:
        pass    
    
    for chapter in chapters:
        image_path = path + manga + "/" + chapter
        images = [x for x in os.listdir(image_path) if x != 'Thumbs.db' and 'thumb' not in x]
        i += 1
        image = images[0] #first is cover
        image_name, image_ext = os.path.splitext(image)
        image_network_path = (image_path + "/" +  image)
        cover_local = cover_test_path + "/" + chapter + image_ext
        if os.path.isfile(cover_local) == True:
            pass
        else:
            shutil.copy2(image_network_path, cover_local)        
   
