# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 14:07:43 2015

@author: julio
"""
import shutil
import os
import chardet
import subprocess

path = "//Art-1405260002/d/assets/manga/"
path = "d:/manga/"

ignore_dir = ["css", "templates", "images"]
mangas = [m for m in os.listdir(path) if m not in ignore_dir if os.path.isdir(os.path.join(path,m))]

#----------------------rename folders
for manga in mangas:
    chapters = [x[1] for x in os.walk((path + manga).decode('utf8'))][0]
    
    try:
        chapters.remove("cover")
    except:
        pass
    
    for x in chapters:
        try:
            if chardet.detect(str(x)).get('encoding') == 'ascii':
                folder_rename = False
            elif " " in x:
                folder_rename = True
            else:
                folder_rename = True
        except:
            folder_rename = True
    
    if folder_rename == True:
        i = 1
        for chapter in chapters:
            image_path = path + manga + "/" + chapter
            new_path = path + manga + "/Vol_%02d" % i
            os.rename(image_path, new_path )
            print manga, chapter, image_path, new_path
            i += 1