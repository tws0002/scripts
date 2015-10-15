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
import matplotlib.ticker as mtick
import itertools
from itertools import groupby
from operator import itemgetter

#%%
ar_list = [
    [2.247, 1.858, 1.167, 1.082, 0.694, 0.784],     #air gear
    [2.495, 2.009, 1.284, 1.214, 0.725, 0.7969],    #abara
    [2.344, 2.046, 1.206, 1.141, 0.841, 0.905]      #appleseed
    ]

   
def getAR(aspect_ratio):
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

# crease positions 
def findCreasePositions(edge_image):
    fi_min, fi_max, f_min, f_max, b_min, b_max, bi_min, bi_max = creaseMinMaxRange(cover_index)    
    im = cv2.cvtColor(edge_image, cv2.COLOR_GRAY2RGB)
    im_rotate = np.swapaxes(im,0,1)
    
    x_axis = []
    x_axis_max = []
    new = []
    new1 = []
    count = 0
    for x in im_rotate:
        rsum = 0
        for y in x:
            rsum += y[1] # y[1][r,g,b]
        x_axis.append(rsum/255) # count of all white pixels per column
        if (rsum/255)*100/height > 40: # any column with values greater then 40% this should be based on mean
            x_axis_max.append(rsum/255)
            new.append([count, rsum/255])
        count += 1
    #maximum = max(x_axis) * 100/height
    #average = (sum(x_axis)*100/height/len(x_axis))
    #average = sum(x_axis)/len(x_axis)       
    maximum = max(x_axis) * .50
    positions = []

    try:    
        positions, value = zip(*new)
    except:
        pass
    # get an average to filter, but only if more then 10 peaks    
    if len(new) < 10:
        pass
    else:
        for x in new:
            if x[1] < maximum:
                pass
            else:
                new1.append(x)
        positions, value = zip(*new1)        

    t = sorted(new1, key=itemgetter(1))
    fi_crease = f_crease = b_crease = bi_crease = None
    for x in positions:
        if x > fi_min and x < fi_max:
            if fi_crease: # if multiple lines in range, choose leftest
                if x_axis[x] > x_axis[fi_crease]:
                    pass
            else:
                fi_crease = x
        if x > f_min and x < f_max:
            if f_crease: # if multiple lines in range, choose rightest
                if x_axis[x] > x_axis[f_crease]:
                    pass
            else:
                f_crease = x            
        if x > b_min and x < b_max:
                b_crease = x
        if x > bi_min and x < bi_max:
            bi_crease = x            

    # if f_crease is None and b_crease is None: leave this and check valley
    return fi_crease, f_crease, b_crease, bi_crease    



def findValleyPositions(imgarray):
    im = cv2.cvtColor(imgarray, cv2.COLOR_GRAY2RGB)
    im_rotate = np.swapaxes(im,0,1)
    
    x_axis = []
    x_axis_min = []
    x_pos = 0
    for x in im_rotate:
        rsum = 0
        for y in x:
            rsum += y[1]
        x_axis.append(rsum/255)
        if (rsum/255)*100/height < 1.8: # any column with values less then 2% 
            x_axis_min.append(x_pos)
        x_pos += 1 
    
    valleys = []
    for k, g in itertools.groupby(enumerate(x_axis_min), lambda (i,x):i-x):
        valleys.append(map(itemgetter(1), g))
    return valleys

#find probable ranges expressed in pixels
#spine is 50% +- 2.5%
#fi and bi is 15% to 20%
# base type search parameter

def guessCreaseFromValleys(valley_positions, crease_positions):
    fi_min, fi_max, f_min, f_max, b_min, b_max, bi_min, bi_max = creaseMinMaxRange(cover_index)    
    fi_valley = f_valley = b_valley = bi_valley = 0
    for x in valley_positions:
        # valley should be in range, but either start or end might be outside...
        if  x[0] > fi_min and x[len(x)-1] < fi_max:
            if  len(x) < 3:
                pass
            else:
                fi_valley = [x[0], x[len(x)-1]]
        if x[0] > f_min and x[len(x)-1] < f_max:
            if  len(x) < 3:
                pass
            else:            
                f_valley = [x[0], x[len(x)-1]]
        if x[0] > b_min and x[len(x)-1] < b_max:
            if  len(x) < 3:
                pass
            else:            
                b_valley = [x[0], x[len(x)-1]]
        if x[0] > bi_min and x[len(x)-1] < bi_max:
            if  len(x) < 3:
                pass
            else:            
                bi_valley = [x[0], x[len(x)-1]]

    # find the middle point of valleys and use as crease
    # last resort
    fi_crease = f_crease = b_crease = bi_crease = None
    if fi_valley != 0:
        fi_crease = (fi_valley[1] - fi_valley[0]) / 2 + fi_valley[0]
    if f_valley != 0:        
        f_crease = (f_valley[1] - f_valley[0]) / 2 + f_valley[0]
    if b_valley != 0:        
        b_crease = (b_valley[1] - b_valley[0]) / 2 + b_valley[0]
    if bi_valley != 0:        
        bi_crease = (bi_valley[1] - bi_valley[0]) / 2 + bi_valley[0]

    # use crease positions if availble
    if crease_positions[0]:
        fi_crease = crease_positions[0]
    if crease_positions[1]:
        f_crease = crease_positions[1]
    if crease_positions[2]:
        b_crease = crease_positions[2]
    if crease_positions[3]:
        bi_crease = crease_positions[3]      

    # best guess unknown creases
    if bi_crease and fi_crease is None:
        fi_crease = width - bi_crease
    
    if f_crease is None and fi_crease and b_crease and (cover_index == 0 or cover_index == 2):
        f_crease = width - b_crease    
    
    if crease_positions[0] == None and f_crease and b_crease and cover_index == 1:
        cover_width = width - b_crease
        spine_width = b_crease - f_crease
        fi_crease = width - (cover_width * 2) - spine_width
        
    return [fi_crease, f_crease, b_crease, bi_crease]
    
def creaseMinMaxRange(cover_index):
    #----------min max of probable crease positions
    # these parameters needs tweaking
    fi_min = fi_max = f_min = f_max = b_min = b_max = bi_min = bi_max = 0        
    # fi f s b bi
    if cover_index == 0: 
        fi_min = width * 0.125
        fi_max = width * 0.225
        
        f_min = (width / 2) - (width * 0.05)
        f_max = (width / 2)
    
        b_min = (width / 2)
        b_max = (width / 2) + (width * 0.05)
        
        bi_min = width * 0.775
        bi_max = width * 0.875
    
    # fi f s b
    elif cover_index == 1:
        fi_min = width * 0.197
        fi_max = width * 0.297
        
        f_min = width * 0.54
        f_max = width * 0.64
        
        b_min = width * 0.59
        b_max = width * 0.69 
    
    # fi f
    elif cover_index == 2:
        f_min = width * 0.42
        f_max = width * 0.52
        b_min = width * 0.48
        b_max = width * 0.58
    
    # fi f s
    elif cover_index == 3:
        fi_min = width * 0.2766
        fi_max = width * 0.3766
        f_min = width * 0.8678
        f_max = width * 0.9678
        #fi_min = 0
        #fi_max = width / 2
        #f_min = width /2
        #f_max = width
    
    # f
    elif cover_index == 4:
        pass
    
    # f s
    elif cover_index == 5:
        f_min = width * 0.83
        f_max = width * 0.93
    return fi_min, fi_max, f_min, f_max, b_min, b_max, bi_min, bi_max
    
# converts images to usable arrays
def convert1D(imgarray):
    im = cv2.cvtColor(imgarray, cv2.COLOR_GRAY2RGB)
    im_rotate = np.swapaxes(im,0,1)
    x_axis = []
    x_axis_values = []
    for x in im_rotate:
        rsum = 0
        for y in x:
            rsum += y[1]
        x_axis_values.append(((rsum/255)*100)/height)
    return x_axis_values
    
# smooth values in a list, r is range
def smoothList(edges):
    smoothed_x_axis = []
    for x in range(0, len(edges)):
        r = 2   
        try:
            add_x = edges[x-2] + edges[x-1] + edges[x] + edges[x+1] + edges[x+2]
            add_x = add_x/5
            smoothed_x_axis.append(add_x)
        except:
            pass
    return smoothed_x_axis

def smoothListGaussian(edges,strippedXs=True,degree=2):  
    window=degree*2-1
    weight=np.array([1.0]*window)  
    weightGauss=[]  
    for i in range(window):  
        i=i-degree+1  
        frac=i/float(window)  
        gauss=1/(np.exp((4*(frac))**2))  
        weightGauss.append(gauss)  
    weight=np.array(weightGauss)*weight  
    smoothed=[0.0]*(len(edges)-window)  
    for i in range(len(smoothed)):  
        smoothed[i]=sum(np.array(edges[i:i+window])*weight)/sum(weight)  
    return smoothed  


# input the manga path, it will find the cover images, analyze the 10 of them, return average crease loactions

def getCreases(manga_path):
    global width, height, cover_index, aspect_ratio
    ignore = [".html","covers", "cover"]
    crease_all = []
    crease_final = []
    if "coverss" in os.listdir(manga_path):
        pass
    else:
        volumes = [x for x in os.listdir(manga_path) if os.path.isdir(manga_path + "/" + x) and x not in ignore]
        #volumes = volumes[:19]
        for volume in volumes:
            volume = volumes[2]
            image = os.listdir(manga_path + "/" + volume)[0]
            image_network_path = manga_path + "/" + volume + "/" + image
            print volume
            out_path = r"d:\output.jpg"
            resized_path = r"d:\\" + volume + ".jpg"
            
            #this one to operate on
            flag = "-resize x1000"
            imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (image_network_path, flag, resized_path)            
            subprocess.call(imageMagickCMD)

            imageMagickID = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/identify.exe \"%s\"" % resized_path
            info = subprocess.Popen(imageMagickID, shell=True, stdout=subprocess.PIPE).communicate()[0]
            info = info.split(" ")
            try:
                orig_width, orig_height = [int(s) for s in info[2].split("x")]        
            except:
                orig_width, orig_height = [int(s) for s in info[3].split("x")]        
            aspect_ratio = float(orig_width)/float(orig_height)
            manga_index, cover_index = getAR(aspect_ratio)            
           
            #flag = "-resize 175000@"
            flag = "-resize 350000@"
            imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (resized_path, flag, out_path)            
            subprocess.call(imageMagickCMD)
            
            imageMagickID = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/identify.exe \"%s\"" % out_path
            info = subprocess.Popen(imageMagickID, shell=True, stdout=subprocess.PIPE).communicate()[0]
            
            info = info.split(" ")
            width, height = [int(s) for s in info[2].split("x")]
            aspect_ratio = float(width)/float(height)
            
            manga_index, cover_index = getAR(aspect_ratio)
           
            im = cv2.imread(out_path)
            im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            
            edges = []
            edges.append(cv2.Canny(im,0,50)) # finds low contrast edges, good for finding creases and edges
            edges.append(cv2.Canny(im,200, 400)) #finds highest contrast edges, good for finding empty space
            
            crease_positions = findCreasePositions(edges[0]) #high probability this is good
            #valley_positions = findValleyPositions(edges[1]) # should return (start, end)
            valley_positions = []
            crease_final = guessCreaseFromValleys(valley_positions, crease_positions)
            crease_all.append(crease_final)

        crease_all1 = crease_all
        crease_all1 = np.array(crease_all1)
        crease_all1 = np.swapaxes(crease_all1, 0, 1)

        temp = []
        for z in range(0, len(crease_all1)):
            nandsum = 0
            count = 0
            for x in crease_all1[z]:
                if x is not None:
                    nandsum += x
                    count += 1
            try:
                temp.append(int(nandsum/count/float(width)*orig_width))
            except:
                temp.append(None)
        crease_average = temp # average 
        #return crease_all

        for x in range(0, len(volumes)):
            resized_path = r"d:\\" + volumes[x] + ".jpg"

            image = os.listdir(manga_path + "/" + volumes[x])[0]
            image_network_path = manga_path + "/" + volumes[x] + "/" + image
            if os.path.isdir(manga_path + "/covers/") == False:
                os.makedirs(manga_path + "/covers/")
            try:
                f = crease_all[x][1]/float(width)*orig_width
                fi = crease_all[x][0]/float(width)*orig_width
            except:
                pass
            pixel_offset = int(1/(float(width)/orig_width)) # pixel scaling offset
            if f == None or f == "":
                print "using average"
                f = crease_average[0]/width*orig_width + pixel_offset
            if fi == None or f == "":
                print "using average"
                fi = crease_average[1]/width*orig_width + pixel_offset
            #print f, fi
            try:
                crop_width = int(f) - int(fi)
                crop_offset = int(fi)
                
                thumb_network_path = manga_path + "/covers/" + volumes[x] + ".jpg"
    
                if (int(width) * 0.4867 * 0.7367)/int(height) > 0.83: #.4867 and .7367 are crop percentages, not exact, needs more precision
                    flags = "-crop %sx%s+%s+0 +repage -resize 700x -gravity center -background white -extent 700x1000" % (crop_width, orig_height, crop_offset)
                else:
                    flags = "-crop %sx%s+%s+0 +repage -resize x1000 -gravity center -background white -extent 700x1000" % (crop_width, orig_height, crop_offset)
                #flags = "-crop %sx%s+%s+0" % (crop_width, orig_height, crop_offset)
                createThumb(resized_path, flags, thumb_network_path)
            except:
                print "not enough data"

    
def createThumb(source, flags, destination):
    imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (source, flags, destination)        
    subprocess.call(imageMagickCMD, shell=True) 

#%%
path = "//Art-1405260002/d/assets/manga/"
ignore_dir = ["css", "templates", "images", "cover", "Thumbs.db", "desktop.ini"]
mangas = [m for m in os.listdir(path) if m not in ignore_dir if os.path.isdir(os.path.join(path,m))]
mangas = mangas[11:12]

for manga in mangas:
    manga_path = path + manga
    getCreases(manga_path)


# visualizing
#creases = crease_final
width, height, cover_index, aspect_ratio = 0
path = "//Art-1405260002/d/assets/manga/"
ignore_dir = ["css", "templates", "images", "cover", "Thumbs.db", "desktop.ini"]
mangas = [m for m in os.listdir(path) if m not in ignore_dir if os.path.isdir(os.path.join(path,m))]
manga = mangas[24]
manga_path = path + manga

volume = "Vol_01"
image = os.listdir(manga_path + "/" + volume)[0]
image_network_path = manga_path + "/" + volume + "/" + image
out_path = r"d:\output.jpg"
resized_path = r"d:\resized.jpg"

#this one to operate on
flag = "-resize x1000"
imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (image_network_path, flag, resized_path)            
subprocess.call(imageMagickCMD)

#this one analysis
flag = "-resize 350000@"
imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (resized_path, flag, out_path)            
subprocess.call(imageMagickCMD)

imageMagickID = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/identify.exe \"%s\"" % resized_path
info = subprocess.Popen(imageMagickID, shell=True, stdout=subprocess.PIPE).communicate()[0]
info = info.split(" ")
orig_width, orig_height = [int(s) for s in info[2].split("x")]


imageMagickID = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/identify.exe \"%s\"" % out_path
info = subprocess.Popen(imageMagickID, shell=True, stdout=subprocess.PIPE).communicate()[0]
info = info.split(" ")
width, height = [int(s) for s in info[2].split("x")]        
aspect_ratio = float(width)/float(height)
manga_index, cover_index = getAR(aspect_ratio)

im = cv2.imread(out_path)
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY )

edges = []
edges.append(cv2.Canny(im,0,50)) # finds low contrast edges, good for finding creases and edges
edges.append(cv2.Canny(im,200, 400)) #finds highest contrast edges, good for finding empty spacetCreases(manga_path)

crease_positions = findCreasePositions(edges[0]) #high probability this is good
valley_positions = findValleyPositions(edges[1]) # should return (start, end)
crease_final = guessCreaseFromValleys(valley_positions, crease_positions)

def f(x):
    if x != None:
        return x/float(width)*(orig_width) + (1/float(width)/orig_width)
    else:
        pass
    
crease_final_convert = map(f, crease_final)

low_edge = convert1D(edges[0])
high_edge = convert1D(edges[1])

plt.subplot(311)
plt.cla()
plt.tight_layout(pad=1.08, h_pad=None, w_pad=None, rect=None)
test = cv2.cvtColor(edges[0], cv2.COLOR_GRAY2RGB )
for x in range(0, len(crease_final)):
    if crease_final[x] == None:
        pass
    else:
        test[:,crease_final[x]] = [255,0,0]

plt.imshow(test, 'gray')
plt.subplot(312)
plt.imshow(edges[1], 'gray')

plt.subplot(313)
plt.cla()
plt.ylim([0,100])
plt.plot(high_edge)
plt.plot(low_edge)
plt.show()




