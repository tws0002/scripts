# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 13:55:34 2015

@author: julio
"""
import os
import shutil

path = r"f:/manga/"
ignore_dir = ["css", "templates", "images", "cover", "Thumbs.db", "desktop.ini"]
mangas = [m for m in os.listdir(path) if m not in ignore_dir if os.path.isdir(os.path.join(path,m))]

#mangas = mangas[mangas.index("tsukidate_no_satsujin"):]
#mangas = mangas[0:1]
# copy image to covers
mangas = ['donmai_princess']
#%%
for manga in mangas:
    #chapters = [x[1] for x in os.walk((path + manga).decode('utf8'))][0]
    chapters = [x for x in os.listdir(path + manga) if "html" not in x and x not in ignore_dir]
    i = 0
    cover_test_path = ("f:/cover/" + manga)
    try:
        if os.path.isdir(cover_test_path) == True:
            if len(os.listdir(cover_test_path)) != 0:
                pass
            else:
                raise
        else:
            raise
        print manga
    except:
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
#%%       
# find folders within folder
for manga in mangas:
    chapters = os.listdir(path + manga)
    for chapter in chapters:
        chapter_path = path + manga + "/" + chapter
        chapter_content = os.listdir(chapter_path)
        f = chapter_path + "/" + chapter_content[0] 
        if os.path.isfile(f) == True: # if content is file skip
            pass
        else:
            i = 1
            for x in chapter_content:
                isfolder = chapter_path + "/" + x
                dst = path + manga + "/Vol_%02d" % i
                print src + " " + dst

                copytree(src, dst, symlinks=False, ignore=None)
                shutil.rmtree(src)
                i += 1

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

# folder in folder
mangas = [m for m in os.listdir(path) if m not in ignore_dir if os.path.isdir(os.path.join(path,m))]

#mangas = mangas[mangas.index("your_lie_in_april"):]
for manga in mangas:
    print manga
    unicode_chapter_content_path  = None
    chapters = os.listdir(path + manga)
    i = 1
    for chapter in chapters:
        #chapter = chapters[1]
        chapter_path = path + manga + "/" + chapter
        chapter_content = os.listdir(chapter_path)
        src = chapter_path + "/" + chapter_content[0]

        #for x in os.listdir(chapter_path):
        #    x_path = unicode(os.path.join(chapter_path, x))
        #    if os.path.isfile(x_path) == True and (x_path.split(".")[1] == "db" or x_path.split(".")[1] == "txt") :
        #        print x_path
        #        os.remove(x_path)

        if chardet.detect(chapter_content[0]).get('encoding') != 'ascii': # if content directory is not ascii
            unicode_chapter_content = [x[2] for x in os.walk((chapter_path).decode('utf8'))][0] # these are files 
            unicode_chapter_content_path = [x[1] for x in os.walk((chapter_path).decode('utf8'))][0] # these are files 
            page= 1
            for x in unicode_chapter_content: # rename files to standard format
                #x = chapter_content[0]
                ext = x.split(".")[1]
                src = chapter_path + "/" + x
                page_number = "%03d" % page
                page_number = page_number + "." + ext
                dst = chapter_path + "/" + page_number
                print src, dst
                os.rename(src, dst)
                page += 1
            
        if len(chapter_content) == 1: # if chapter folder has another folder
            src = chapter_path + "/" + chapter_content[0]
            print src
            if unicode_chapter_content_path:
                src = chapter_path + "/" + unicode_chapter_content_path[0]
            if os.path.isfile(f) == True: # if content is file skip
                pass
            else:
                dst = path + manga + "/Vol_%02d" % i
                print src, dst
                copytree(src, dst, symlinks=False, ignore=None)
                shutil.rmtree(src)
                #os.rmdir(src)
        i += 1

#%% this part copyies covers not in mcd to network
import os
import unicodecsv
import subprocess
import shutil
csv_path = r"f:/manga_list08.csv"

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
#%%
csv_list = []
with open(csv_path, 'r') as csvfile:
    csv_content = unicodecsv.reader(csvfile, delimiter=',', lineterminator='\n')
    for row in csv_content:
        csv_list.append(row)

#%%
for x in csv_list:
    if x[13] == 'False':
        src = r"f:/cover/%s/" % x[2]
        dst = r"//art-1405260002/d/assets/manga/covers/%s/" % x[2]
        if os.path.isdir(dst) == True:
            print "exists"
        else:
            print x[2]
            copytree(src, dst)

