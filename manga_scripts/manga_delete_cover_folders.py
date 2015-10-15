# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 12:17:19 2015

@author: julio
"""
import shutil
ignore_dir = ["css", "templates", "images", "cover", "Thumbs.db", "desktop.ini"]
mangas = [m for m in os.listdir(path) if m not in ignore_dir if os.path.isdir(os.path.join(path,m))]

mangas = mangas[1:10]
for manga in mangas:
    print manga
    manga_path = path + mangaPIRA
    cover = [x for x in os.listdir(manga_path) if os.path.isdir(manga_path + "/" + x) and "covers" in x]
    shutil.rmtree(manga_path + "/covers", ignore_errors=True)
