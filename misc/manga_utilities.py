
# -*- encoding: utf-8 -*-
"""
Created on Tue Sep 01 13:11:59 2015

@author: julio
"""

import os
import csv
import rarfile
import zipfile
import chardet
rarfile.TRY_ENCODINGS = ('utf8', 'utf-16le')
zipfile.TRY_ENCODINGS = ('utf8', 'utf-16le')

manga_path = "d:/manga"
zipped_path = "d:/zipped"
csv_path = "d:/manga_list.csv"

csv_list = []
with open(csv_path, 'rb') as csvfile:
    csv_content = csv.reader(csvfile, delimiter=',')
    for row in csv_content:
        csv_list.append(row[2])

unzipped_list = os.listdir(manga_path)
zipped_list = os.listdir(zipped_path)

#compare zipped folder to csv
for x in csv_list:
    if x in zipped_list:
        pass
    else:
        print x
        dst = (zipped_path + "/" + x)
        print dst
        os.mkdir(dst)
        
#compare manga folder to zipped folder
missing = []
for x in zipped_list:
    if x in unzipped_list:
        pass
    else:
        missing.append(x)
        print x

print missing
#add directories to unzipped folder
for x in missing:
    dst = (manga_path + "/" + x)
    try:    
        os.mkdir(dst)
    except:
        print "dir already exists"
        
#checks un
for folder in unzipped_list:
    path = manga_path + "/" + folder
    if len(os.listdir(path)) == 1: # if dir is empty
        print folder
        #folder = "biyaku_cafe"
        zip_files = [x for x in os.listdir(zipped_path + "/" + folder)] #go look for filess in the respective zip dir
        for zip_file in zip_files:
            zip_file_uni = unicode(zip_file, 'Big5')
            os.path.isfile(zipped_path + "/" + folder + "/" + zip_file_uni)
            if os.path.isfile(zipped_path + "/" + folder + "/" + zip_file_uni) == True: #check for files only
                if zip_file_uni[-3:] == "rar":
                    rf = rarfile.RarFile(zipped_path +"/" + folder + "/" + zip_file)
                    temp = rf.namelist()
                    if "\\" in temp[0]  or "/" in temp[0]:
                        rf.extractall(path)
                    else:
                        new_path = path + "/" + zip_file_uni.replace(".zip","")
                        os.mkdir(new_path)
                        rf.extractall(new_path)
                        
                elif zip_file_uni[-3:] == "zip":
                    zf = zipfile.ZipFile(zipped_path +"/" + folder + "/" + zip_file)
                    temp = zf.namelist()
                    if  "\\" in temp[0] or "/" in temp[0]:
                        zf.extractall(path)
                    else:
                        new_path = path + "/" + zip_file_uni.replace(".zip","")
                        os.mkdir(new_path)
                        zf.extractall(new_path)
            else:
                print "what"


#check server path with manga path
server_path = "//Art-1405260002/d/assets/manga"
server_list = os.listdir(server_path)
for folder in unzipped_list:
    if folder in os.listdir(server_path):
        pass
    else:
        print folder
        
#check server path with csv
server_list = os.listdir(server_path)
for x in csv_list:
    if x in server_list:
        pass
    else:
        print x

#check for empty or sub-subfolder        
for x in server_list:
    if os.path.isdir(server_path + "/" + x) == True:
        if len(os.listdir(server_path + "/" + x)) <= 1:
            print x






