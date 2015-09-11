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
from collections import Counter
ar_list = [
    [2.247, 1.858, 1.167, 1.082, 0.694, 0.784],     #air gear
    [2.495, 2.009, 1.284, 1.214, 0.725, 0.7969],    #abara
    [2.344, 2.046, 1.206, 1.141, 0.841, 0.905]      #appleseed
    ]
    
def getAR(asepect_ration):
    occurence = []
    for manga_ar in ar_list:
        crop_type = manga_ar.index(min(manga_ar, key=lambda x:abs(x-aspect_ratio))) 
        occurence.append(crop_type)
    
    #find most common cover type
    most_common, num = Counter(occurence).most_common()[0] 
    
    ar_temp = []
    for x in range(0,len(ar_list)):
        ar_temp.append(ar_list[x][most_common])
    
    manga_index = ar_temp.index(min(ar_temp, key=lambda x:abs(x-aspect_ratio)))
    return manga_index, most_common

def findCreasePositions(edges):
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
    
    positions = []
    for line in s:
        #pos = x_axis.index(line) #find indices for the lines
        pos = [i for i, x in enumerate(x_axis) if x == line]
        for p in pos:
            positions.append(p)
          
    return sorted(positions)


path = r"d:/cover/"
mangas = os.listdir(path)

for manga in mangas:
manga = mangas[18]
manga_path = path + manga
images = os.listdir(manga_path)

image = images[0] #

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

edges = []
edges.append(cv2.Canny(im,0,50)) # finds low contrast edges
edges.append(cv2.Canny(im,200, 400)) #finds highest contrast edges, good for finding empty space

x_axis_values = findFeaturePositions(edges[1])

plt.subplot(311)
plt.imshow(edges[0], 'gray')
plt.subplot(312)
plt.imshow(edges[1], 'gray')
plt.subplot(313)
plt.plot(x_axis_values)

plt.subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=1.0)
#plt.imshow(edges[3], 'gray')

#imgplot = plt.imshow(edge[4, 'gray')
plt.show()

#returns highest 10 positions of creases


positions = findCreasePositions(edges[0])
feature_positions = findFeaturePositions(edges[2])
#find probable locations of creases and calculate widths of elements

fi_width = width * 0.2177
full_width = width + fi_width

#general location for the creases in pixels
#this is going to be off for each manga...

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
# match line with positions generated above. 
def findline(guessed_positions, r, detected_positions):
    r_min = guessed_positions - r
    r_max = guessed_positions + r
    for x in range(r_min, r_max):
        if x in detected_positions:
            return x
        else:
            pass

r = 3
if cover_index == 1:
    crease_b_fin = findline(crease_b, r, positions)
    crease_f_fin = findline(crease_f, r, positions)
    crease_fi_fin = findline(crease_fi, r, positions)
    
    # if not found extrapolate using best method
    # 1. retry canny with next set of min max
    # 2. look at history or future of same manga
    # 3. try similar manga
    # 4. use others to calculate width
    
    if crease_fi_fin is None:
        r = 20 # increase search width as features also have margins
        crease_fi_fin = findline(crease_fi, r, feature_positions)
        

        

    
    
    
        
               
           
           
    
    
    
    