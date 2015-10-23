# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 13:51:11 2015

@author: julio
"""

import json

mcdjson = r"f:/mcdatabase.txt"

with open(mcdjson) as fileobj:
    data = fileobj.read()

jsondata = json.loads(data)

    
#%%

import unicodecsv    
import re
#mangas = r"\\art-1405260002\D\assets\scripts\manga_scripts\manga_list.csv"
mangas = r"f:/manga_list01.csv"
data = []
with open(mangas, "rU") as fileobj:
    sheets = fileobj.read()
    
    csvreader = unicodecsv.reader(fileobj, encoding='utf8')
    for row in csvreader:
        print row

#%%
not_ok = []
found = []
new = []

for manga in mangas:
    manga = manga.decode('big5').encode('utf8')    
    source_name = manga.split(",")[2]
    source_name_chn = manga.split(",")[1].replace("?","")
    source_name = source_name.replace("_", " ")
    ok = 0
    t_names = ""
    for target_id, target_names in jsondata.items():
        for target in target_names:
            count = 0            
            target = target.lower().replace("-","")
            if re.search(source_name, target) or re.search(source_name_chn, target.encode('utf8')):
                t_names = "|".join(target_names)
                ok = 1
                break
        if ok == 1:
            break
    if ok == 1:
        found.append(source_name)
        new.append([manga.split(",")[0],manga.split(",")[1],manga.split(",")[2],target_id, t_names])
    else:
        not_ok.append(manga.split(",")[2])
        new.append([manga.split(",")[0],manga.split(",")[1],manga.split(",")[2],"", ""])
#%%        

import xlrd
mangas = r"f:/manga_list01.xls"

xls = xlrd.open_workbook(mangas)
print xls.sheet_names

sheet = xls.sheet_by_name('manga_list01')
print sheet.row(0)

