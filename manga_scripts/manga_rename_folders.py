# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 14:07:43 2015

@author: julio
"""
import shutil
import os
import chardet
import subprocess
import re

def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)   

path = "//Art-1405260002/d/assets/manga/"
#path = "d:/manga/"

ignore_dir = ["css", "templates", "images"]
mangas = [m for m in os.listdir(path) if m not in ignore_dir if os.path.isdir(os.path.join(path,m))]

#----------------------move folder up one level

for manga in mangas:
    #manga = "doraaemon"
    #print manga
    chapters = [x[1] for x in os.walk((path + manga).decode('utf8'))][0]
    #chapters = os.listdir(path + manga)
    if len(chapters) < 2: # single folder
        print manga
        for folder in chapters:
            child_folder = path + manga + "/" + folder
            child_folder_contents = os.listdir(child_folder)
            f = child_folder + "/" + child_folder_contents[0] 
            if os.path.isfile(f) == True: # if content is file skip
                pass
            else:
                i = 1
                for x in child_folder_contents:
                    src = child_folder + "/" + x
                    if os.path.isfile(src) == True:
                        pass
                    else:
                        dst = path + manga + "/Vol_%02d" % i
                        print src + " " + dst
                        copytree(src, dst, symlinks=False, ignore=None)
                        shutil.rmtree(src)
                    i += 1


# convert chapter folders to Vol_01 format 
mangas = [m for m in os.listdir(path) if m not in ignore_dir if os.path.isdir(os.path.join(path,m))]

for manga in mangas:
    #manga = "boys_be_2"
    print manga
    
    if len(os.listdir(path + manga)) == 0:
        pass
    else:
        test = os.listdir(path + manga)[0]
        if chardet.detect(test).get('encoding') != 'ascii':
            chapters = [x[1] for x in os.walk((path + manga).decode('utf8'))][0]
        else:
            chapters = os.listdir(path + manga)
        try:
            chapters.remove("covers")
        except:
            pass
        i = 1
        for x in chapters:
            try:
                vol, number = x.split("_")
                if vol == "Vol" and re.search("([0-9])", number).string != None:
                    pass
                elif chardet.detect(str(x)).get('encoding') != 'ascii':
                    raise
                else:
                    raise
            except:
                current = path + manga + "/" + x
                if len(chapters) > 99:
                    new = path + manga + "/Vol_%03d" % i    
                new = path + manga + "/Vol_%02d" % i
                os.rename(current, new)
                i += 1
                print current, new

            
            '''
            
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
            '''