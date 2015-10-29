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
#manga_list = r"\\art-1405260002\D\assets\scripts\manga_scripts\manga_list.csv"
manga_list = r"f:/manga_list02.csv"
mangas = []
with open(manga_list, "r") as fileobj:
    mangas = fileobj.readlines()


#%%
not_ok = []
found = []
new = []

for manga in mangas:
    manga = manga.decode('big5').encode('utf8')    
    manga_id = manga.split(",")[3]
    source_name = manga.split(",")[2]
    source_name_chn = manga.split(",")[1].replace("?","")
    source_name = source_name.replace("_", " ")
    if manga_id != "":
        pass
    else:
        ok = 0
        t_names = ""
        for target_id, target_names in jsondata.items():
            for target in target_names:
                count = 0            
                target = target.lower().replace("-","")
                if len(source_name.split(" ")) == 1: # single word source needs exact match
                    if source_name == target:
                        t_names = "|".join(target_names)
                        ok = 1
                        break
                elif re.search(source_name, target) or re.search(source_name_chn, target.encode('utf8')): # source string in targets
                    t_names = "|".join(target_names)
                    ok = 1
                    break
            if ok == 1:
                break
        if ok == 1:
            print source_name, target, target_id

#%%            
        if ok == 1:
            found.append(source_name)
            new.append([manga.split(",")[0],manga.split(",")[1],manga.split(",")[2],target_id, t_names])
        else:
            not_ok.append(manga.split(",")[2])
            new.append([manga.split(",")[0],manga.split(",")[1],manga.split(",")[2],"", ""])
#%%        

print len(found)
print len(not_ok)
for x in found:
    print x

#%%
import xlrd
mangas = r"f:/manga_list01.xls"

xls = xlrd.open_workbook(mangas)
print xls.sheet_names

sheet = xls.sheet_by_name('manga_list01')
print sheet.nrows()

#%%
from selenium import webdriver
adblockfile = 'c:/Users/julio/Downloads/adblock_plus-2.6.11-sm+tb+fx+an.xpi'
ffprofile = webdriver.FirefoxProfile("C:/Users/julio/AppData/Local/Mozilla/Firefox/Profiles")
ffprofile.add_extension(adblockfile)
driver = webdriver.Firefox(ffprofile)

mainpage = "https://www.mangaupdates.com/series.html"
driver.get(mainpage)

search_bar = driver.find_element_by_xpath("//td[@class='textbold search_bar']/form/input[@class='loginbox']")
search_bar = driver.find_element_by_xpath("//td/input[@name='search']")

search_bar.send_keys("gimmick")
search_button = driver.find_elements_by_xpath("//td/input[@name='search']/../input")[1]
search_button.click()



