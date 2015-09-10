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

#flag.append("-thumbnail \"2362x1000^\" -gravity Center -extent 1562x1000 -gravity West -extent 700x1000 ") #blade of the immortal cover
#im_final = "-resize x1000 -gravity center -background white -extent 700x1000 " #base tweek

#air_gear
ag_flag = []
ag_flag.append("-crop 48%x100%+0+0 +repage -gravity East -crop 65%x100%+0+0 +repage ") # Fi F S B Bi
ag_flag.append("-crop 58%x100%+0+0 +repage -gravity East -crop 62.1%x100%+0+0 +repage ") # Fi F S B 
ag_flag.append("") # Fi F S
ag_flag.append("") # Fi F
ag_flag.append("") # F 

#abara
ab_flag = []
ab_flag.append("-crop 60.5%x100%+0+0 +repage -gravity East -crop 59%x100%+0+0 +repage ") # Fi F S B 
ab_flag.append("") # Fi F S
ab_flag.append("") # Fi F S
ab_flag.append("") # Fi F
ab_flag.append("") # F 

#appleseed
as_flag = []
as_flag.append("-crop 48.67%x100%+0+0 +repage -gravity East -crop 73.67%x100%+0+0 +repage ")
ab_flag.append("") # Fi F S
as_flag.append("") # Fi F S
as_flag.append("") # Fi F
as_flag.append("") # F 

flags = [ag_flag, ab_flag, as_flag]


ignore_dir = ["css", "templates", "images"]
mangas = [m for m in os.listdir(path) if m not in ignore_dir if os.path.isdir(os.path.join(path,m))]
mangas = mangas[1:2]

#manga = mangas[0]

#----------------------rename folders
for manga in mangas:
    manga = mangas[0]    
    chapters = [x[1] for x in os.walk((path + manga).decode('utf8'))][0]
    
    try:
        chapters.remove("cover")
    except:
        pass
    
    i = 0
    overwrite = True
    for chapter in chapters:
        chapter = chapters[0]
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
        ar0 = [2.247, 1.858, 1.167, 1.082, 0.694, 0.784] #air_gear
        ar1 = [2.495, 2.009, 1.284, 1.214, 0.725, 0.7969] #abara
        ar2 = [2.344, 2.046, 1.206, 1.141, 0.841, 0.905] #appleseed
        
        #compare current ar to each type and find the closest, returns index 
        crop_type0 = ar0.index(min(ar0, key=lambda x:abs(x-aspect_ratio))) 
        crop_type1 = ar1.index(min(ar1, key=lambda x:abs(x-aspect_ratio)))
        crop_type2 = ar2.index(min(ar2, key=lambda x:abs(x-aspect_ratio)))
    
        ar_temp = [ar0[crop_type0], ar1[crop_type1], ar2[crop_type2]]
        crop_type_temp = ar_temp.index(min(ar_temp, key=lambda x:abs(x-aspect_ratio)))
        if crop_type_temp == 0:
            ar_type = crop_type1
        elif crop_type_temp == 1:
            ar_type = crop_type2
        elif crop_type_temp == 2:
            ar_type = crop_type3    

        flag = flags[ar_type]    
    
        if (int(width) * 0.4867 * 0.7367)/int(height) > 0.83: #.4867 and .7367 are crop percentages, not exact, needs more precision
            im_final = "-resize 700x -gravity center -background white -extent 700x1000 " #base tweek
        else:
            im_final = "-resize x1000 -gravity center -background white -extent 700x1000 " #base tweek        
            
        '''
        thumb_network_path = (image_path + "/" + image_name + "_thumb" + image_ext).encode('utf8')
        thumb_network_path1 = (image_path + "/" + image_name + "_thumb1" + image_ext).encode('utf8')
        flag = "-crop 48.67%x100%+0+0 +repage -gravity East -crop 63.37%x100%+0+0 +repage "
        
        if (int(width) * 0.4867 * 0.7367)/int(height) > 0.83:
            flag = "-resize 700x -gravity center -background white -extent 700x1000 " #base tweek
        else:
            flag = "-resize x1000 -gravity center -background white -extent 700x1000 " #base tweek
        #-gravity center -background white -extent 700x1000 " #base tweek
        imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (image_network_path, flag, thumb_network_path)        
        imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (thumb_network_path, flag, thumb_network_path1)            
        subprocess.call(imageMagickCMD)
        '''
        #custom_flag = "-crop 48.67%x100%+0+0 +repage -gravity East -crop 63%x100%+0+0 +repage " #arms
        #custom_flag = "-crop 48.67%x100%+0+0 +repage -gravity East -crop 66%x100%+0+0 +repage " #attack on titan
        #custom_flag = "-crop 49.29%x100%+0+0 +repage -gravity East -crop 66.3%x100%+0+0 +repage " #azumanga daioh
        #custom_flag = "-crop 91.9%x100%+0+0 +repage -gravity East -crop 65.23%x100%+0+0 +repage " #azumanga daioh
        #custom_flag = "-crop 87.965%x100%+0+0 +repage " #beelzebub
        #custom_flag = "-crop 47.11%x100%+0+0 +repage " #biyaku
        #custom_flag = "-crop 48.11%x100%+0+0 +repage -gravity East -crop 64.54%x100%+0+0 +repage " #azumanga daioh
        #custom_flag = "-crop 50.18%x100%+0+0 +repage -gravity East -crop 87.75%x100%+0+0 +repage " #azumanga daioh
        #custom_flag = "-crop 48.34%x100%+0+0 +repage -gravity East -crop 65.85%x100%+0+0 +repage " #azumanga daioh
        #custom_flag = "-crop 92.69%x100%+0+0 +repage -gravity East -crop 64.09%x100%+0+0 +repage " #azumanga daioh
        #custom_flag = "-crop 92.96%x100%+0+0 +repage -gravity East -crop 65.88%x100%+0+0 +repage "
        #custom_flag = "-crop 48.24%x100%+0+0 +repage -gravity East -crop 65%x100%+0+0 +repage "
        #custom_flag = "-crop 46.58%x100%+0+0 +repage " #biyaku
        #custom_flag = "-crop 48.16%x100%+0+0 +repage -gravity East -crop 65.77%x100%+0+0 +repage "
        #custom_flag = "-crop 56.57%x100%+0+0 +repage -gravity East -crop 66%x100%+0+0 +repage " kumahige
        #ustom_flag = "-gravity East -crop 65.64%x100%+0+0 +repage " #dragon ball
        custom_flag = "-crop 47.88%x100%+0+0 +repage " #dragon quest



        #flag_final = flags[crop_type_temp][ar_type] + im_final
        flag_final = custom_flag + im_final
        if custom_cover == True:
            if overwrite == True:
                createThumb(custom_image_path, flag_final, thumb_network_path)
            else:
                if os.path.isfile(thumb_network_path) == True:
                    pass
                else:
                    createThumb(custom_image_path, flag_final, thumb_network_path)
        elif custom_cover == False:
            if overwrite == True:
                createThumb(image_network_path, flag_final, thumb_network_path)
            else:
                if os.path.isfile(thumb_network_path) == True: 
                    pass
                else:  
                    createThumb(image_network_path, flag_final, thumb_network_path)
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

