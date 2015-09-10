# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 14:32:34 2015

@author: julio
"""

import os
from matplotlib import pyplot as plt
import numpy as np
import cv2
import subprocess

ar_list = [
    [2.247, 1.858, 1.167, 1.082, 0.694, 0.784],     #air gear
    [2.495, 2.009, 1.284, 1.214, 0.725, 0.7969],    #abara
    [2.344, 2.046, 1.206, 1.141, 0.841, 0.905]      #appleseed
    ]
    
def getAR(asepect_ration):
    occurence = []
    for manga_ar in ar_list:
        crop_type = manga_ar.index(min(game_ar, key=lambda x:abs(x-aspect_ratio))) 
        occurence.append(crop_type)
    
    #find most common cover type
    most_common, num = Counter(occurence).most_common()[0] 
    
    ar_temp = []
    for x in range(0,len(ar_list)):
        ar_temp.append(ar_list[x][most_common])
    
    manga_index = ar_temp.index(min(ar_temp, key=lambda x:abs(x-aspect_ratio)))
    return manga_index, most_common

path = r"d:/cover/"
mangas = os.listdir(path)

for manga in mangas:
    manga = mangas[2]
    manga_path = path + manga
    images = os.listdir(manga_path)

image = images[1] #

in_path = manga_path + "/" + image
out_path = r"d:\output.jpg"

flag = "-resize 175000@"
imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (in_path, flag, out_path)            
subprocess.call(imageMagickCMD)

imageMagickID = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/identify.exe \"%s\"" % out_path
info = subprocess.Popen(imageMagickID, shell=True, stdout=subprocess.PIPE).communicate()[0]

info = info.split(" ")
width, height = [int(s) for s in info[2].split("x")]
aspect_ratio = float(width)/float(height)

manga_index, cover_index = getAR(aspect_ratio)


os.path.isfile(out_path)

im = cv2.imread(out_path)
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY )

edges = cv2.Canny(im,0,50)
#edges = cv2.Canny(im,50,200)
imgplot = plt.imshow(edges, 'gray')# numpy array is reversed, use this function
plt.show()

im = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
im_rotate = np.swapaxes(im,0,1)

x_axis = []
for x in im_rotate:
    #x = im_rotate[0]
    rsum = 0
    for y in x:
        rsum += y[1]
    #print rsum/255
    x_axis.append(rsum/255)


s = sorted(x_axis, reverse=True)
s = s[0:10] #get the four folds numbers
s = set(s)
s
positions = []
for line in s:
    #pos = x_axis.index(line) #find indices for the lines
    pos = [i for i, x in enumerate(x_axis) if x == line]
    for p in pos:
        positions.append(p)
      
print sorted(positions)

#find probable locations of creases and calculate widths of elements


fi_width = width * 0.2177
full_width = width + fi_width

crease_bi = int(full_width * 0.8271)
crease_b = int(full_width * 0.5181)
crease_f = int(full_width * 0.4794)
crease_fi = int(full_width * 0.1731)

insert_f_width = crease_fi    
cover_f_width = crease_f - crease_fi
spine_width = crease_b - crease_f
cover_b_width = crease_bi - crease_b
insert_b_width = full_width - crease_bi

#find the line within a range of 2 pixels

def findline(line, r):
    r_min = line - r
    r_max = line + r
    for x in range(r_min, r_max):
        if x in positions:
            return x
        else:
            print "not here"
r = 2            
if cover_index == 1:
    crease_b_fin = findline(crease_b, r)
    crease_f_fin = findline(crease_f, r)
    crease_fi_fin = findline(crease_fi, r)

    #if not found extrapolate
    
        
               
           
           
    
    
    
    