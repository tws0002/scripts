# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 14:07:43 2015

@author: julio
"""
import shutil
import os
import chardet
import subprocess
manga = mangas[0]
path = "//Art-1405260002/d/assets/manga/"

def createThumb(source, flags, destination):
    imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (source, flags, destination)        
    subprocess.call(imageMagickCMD, shell=True) 



ignore_dir = ["css", "templates", "images"]
mangas = [m for m in os.listdir(path) if m not in ignore_dir if os.path.isdir(os.path.join(path,m))]
mangas = mangas[2:3]

manga = mangas[0]

#----------------------rename folders
chapters = [x[1] for x in os.walk((path + manga).decode('utf8'))][0]

try:
    chapters.remove("cover")
except:
    pass

for x in chapters:
    if chardet.detect(str(x)).get('encoding') == 'ascii':
        folder_rename = False
    else:
        folder_rename = True

if folder_rename == True:
    i = 1
    for chapter in chapters:
        image_path = path + manga + "/" + chapter
        new_path = path + manga + "/Vol_%02d" % i
        os.rename(image_path, new_path )
        print image_path, new_path
        i += 1

#-----------------------------
chapters = [x[1] for x in os.walk((path + manga).decode('utf8'))][0]
try:
    chapters.remove("cover")
except:
    pass

i = 0
overwrite = True

#flag.append("-thumbnail \"2362x1000^\" -gravity Center -extent 1562x1000 -gravity West -extent 700x1000 ") #blade of the immortal cover
im_final = "-resize x1000 -gravity center -background white -extent 700x1000 " #base tweek
ag_flag = []
ag_flag.append("-crop 48%x100%+0+0 +repage -gravity East -crop 65%x100%+0+0 +repage ") # Fi F S B Bi #air_gear
ag_flag.append("-crop 58%x100%+0+0 +repage -gravity East -crop 62.1%x100%+0+0 +repage ") # Fi F S B #air gear

ab_flag = []
ab_flag.append("-crop 60.5%x100%+0+0 +repage -gravity East -crop 59%x100%+0+0 +repage ") # Fi F S B #abara


for chapter in chapters:
    #chapter = chapters[0]
    image_path = path + manga + "/" + chapter
    chapter_index = "http://vg.com/assets/manga/" + "/" + manga +".html"
    images = [x for x in os.listdir(image_path) if x != 'Thumbs.db' and 'thumb' not in x]
    i += 1
    #-------------------------------cover image copy
    image = images[0]
    image_name, image_ext = os.path.splitext(image)
    image_network_path = (image_path + "/" +  image)

    try:
        cover_list = os.listdir(path + manga + "/cover")[i - 1]
        custom_image_ext = os.path.splitext(os.listdir(path + manga + "/cover")[i - 1])[1]
        custom_image_path = (path + manga + "/cover/%02d" + custom_image_ext) % i
        custom_cover = True
    except:
        custom_cover = False

    thumb_network_path = (image_path + "/" + image_name + "_thumb" + image_ext)

    imageMagickID = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/identify.exe \"%s\"" % image_network_path
    info = subprocess.Popen(imageMagickID, shell=True, stdout=subprocess.PIPE).communicate()[0]
    #print info
    info = info.split(" ")
    width, height = info[2].split("x")
    aspect_ratio = float(width)/float(height)
    
    #Fi F S B Bi, Fi F S B, Fi F S, Fi F, F, F S
    ar1 = [2.247, 1.858, 1.167, 1.082, 0.694, 0.784] #air_gear
    ar2 = [2.495, 2.009, 1.284, 1.214, 0.725, 0.7969] #abara

    crop_type = ar1.index(min(ar1, key=lambda x:abs(x-aspect_ratio)))
    
    '''
    thumb_network_path = (image_path + "/" + image_name + "_thumb" + image_ext).encode('utf8')
    test_path = image_path + "/"  + image_name + "test_thumb" + image_ext
    flag = "-crop 48%x100%+0+0 +repage -gravity East -crop 65%x100%+0+0 +repage"
    flag = "-crop 48%x100%+0+0 +repage -gravity East -crop 65%x100%+0+0 +repage"
    imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (image_network_path, flag, test_path)        
    subprocess.call(imageMagickCMD)
    '''
    
    
    flags = ag_flag[crop_type] + im_final
   
    if custom_cover == True:
        if overwrite == True:
            createThumb(custom_image_path, flags, thumb_network_path)
        else:
            if os.path.isfile(thumb_network_path) == True:
                pass
            else:
                createThumb(custom_image_path, flags, thumb_network_path)
    elif custom_cover == False:
        if overwrite == True:
            createThumb(image_network_path, flags, thumb_network_path)
        else:
            if os.path.isfile(thumb_network_path) == True: 
                pass
            else:  
                createThumb(image_network_path, flags, thumb_network_path)
    i += 1



            
#remove thumbnails
chapters = [d for d in os.listdir(path + manga) if os.path.isdir(path + manga + "/" + d)]            
for chapter in chapters:
    image_path = path + manga + "/" + chapter
    images = [x for x in os.listdir(image_path) if 'thumb' in x]
    for image in images:
        image_network_path = image_path + "/" +  image
        print image_network_path
        os.remove(image_network_path)

os.rename(image_path, path + manga + "/test")