
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
import uniout
import shutil
rarfile.TRY_ENCODINGS = ('utf8', 'utf-16le')
zipfile.TRY_ENCODINGS = ('utf8', 'utf-16le')

manga_path = "d:/manga"
zipped_path = "d:/zipped"
csv_path = "//Art-1405260002/d/assets/scripts/manga_scripts/manga_list.csv"

csv_list = []
with open(csv_path, 'rb') as csvfile:
    csv_content = csv.reader(csvfile, delimiter=',')
    for row in csv_content:
        csv_list.append(row[2])

manga_list = os.listdir(manga_path)
zipped_list = os.listdir(zipped_path)

'''
for x in csv_list:
    if x not in unzipped_list:
        dst = manga_path + "/" + x
        try:
            os.mkdir(dst)
        except:
            pass


for x in zipped_list:
    if x in csv_list:
        pass
    else:
        print x + " not ok"
'''
        
#checks un
        
       
for folder in unzipped_list:
    folder = unzipped_list[170]
    print folder
    path = manga_path + "/" + folder
    try:
        if len(os.listdir(path)) == 0: # if dir is empty
            zip_files = [x[2] for x in os.walk((zipped_path + "/" + folder).decode('utf8'))][0]
            volume = 1
            for zip_file in zip_files:
                zip_file = zip_files[0]
                zip_file_path = (zipped_path +"/" + folder + "/" + zip_file)
                temp_file_path = (zipped_path +"/" + folder + "/temp." + zip_file[-3:])
                #os.path.isfile(temp_file_path)
                if os.path.isfile(zip_file_path) == True: #check for files only
                    shutil.copyfile(zip_file_path, temp_file_path)            
                    if zip_file[-3:] == "rar":
                        rf = rarfile.RarFile(temp_file_path)
                        temp = rf.namelist()
                        if "\\" in temp[1]  or "/" in temp[1]:
                            rf.extractall(path)
                        else:
                            #new_path = path + "/" + zip_file.replace(".rar","")
                            new_path = path + "/Vol_%02d" % volume
                            os.mkdir(new_path)
                            rf.extractall(new_path)
                            
                    elif zip_file[-3:] == "zip":
                        zf = zipfile.ZipFile(temp_file_path)
                        temp = zf.namelist()
                        try:
                            zf.extractall(path)
                        except:
                            #new_path = path + "/" + zip_file.replace(".zip","")
                            new_path = path + "/Vol_%02d" % volume
                            os.mkdir(new_path)
                            zf.extractall(new_path)
                        zf.close()
                else:
                    print "what"
                os.remove(temp_file_path)
                volume += 1
    except:
        print folder + " BAD BAD"

#check manga path for directories with less then 10 files
for x in manga_list:
    path = manga_path + "/" + x
    for dirpath, dirnames, filenames in os.walk(path):
        print dirpath, len(filenames)
        if len(filenames) < 10:
            print dirpath


#check server path with manga path
server_path = "//Art-1405260002/d/assets/manga"
server_list = os.listdir(server_path)
print len(server_list)
print len(unzipped_list)
for folder in server_list:
    if folder in unzipped_list:
        pass
    else:
        print folder
        

#check for empty or sub-subfolder        
for x in server_list:
    if os.path.isdir(server_path + "/" + x) == True:
        if len(os.listdir(server_path + "/" + x)) <= 1:
            print x


#check server path for directories with less then 10 files
server_path = "//Art-1405260002/d/assets/manga"
server_list = os.listdir(server_path)
for x in server_list:
    path = server_path + "/" + x
    for dirpath, dirnames, filenames in os.walk(path):
        #print dirpath, len(filenames)
        if len(filenames) < 10:
            print dirpath, len(filenames)

server_path = r"d:/manga"
server_list = os.listdir(server_path)

for x in 

