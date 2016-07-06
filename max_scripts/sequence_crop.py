# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 14:50:58 2016

@author: julio
"""

import numpy as np
import os
import cv2
from matplotlib import pyplot as plt
import subprocess
import threading
import Queue
import datetime
import logging
import time

x_min = 0
x_max = 0
y_min = 0
y_max = 0

sequencePath = "d:/sequence"
images = [x for x in os.listdir(sequencePath) if 'tga' in x]


q = ""
q = Queue.Queue(maxsize = 0)

len(images)
for image in images:
    q.put(image)


try:
    os.makedirs(sequencePath + "/convert")
    os.makedirs(sequencePath + "/merged")
except:
    pass


#%%
def alphaExtract(q):
    while True:
        image = q.get()
        print image

        in_path = sequencePath + "/" + image
        fileName, fileType = image.split(".")
            
        flag = "-alpha extract -compress zip"
        out_path = sequencePath + "/convert/" + fileName + ".tif"
        imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (in_path, flag, out_path)            
        subprocess.call(imageMagickCMD)
        q.task_done()

#%%
now = datetime.datetime.now()
workers = []
for x in range(16):
    worker = threading.Thread(target=alphaExtract, args=(q,))
    worker.setDaemon(True)
    worker.start()

q.join()
diff = datetime.datetime.now() - now
print diff

# 4 threads at 0:00:21.491000
# 8 threads at 0:00:17.535000
# 16 threads at 0:00:15.606000
#%%
# add all frames together, but too slow
flag = "-evaluate-sequence add"
out_path = r"d:/sequence/merged/merged.tif"
in_path = r"d:/sequence/convert/*.tif"

imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (in_path, flag, out_path)            
subprocess.call(imageMagickCMD)

#%%

#%%
def findMinMax(image):
    im = cv2.imread(image)
    height, width, channels = im.shape
    y_min = findWhite(im)
    im_reverse = im[::-1]
    
    y_max = findWhite(im_reverse)
    y_max = height - y_max
    
    im = np.swapaxes(im,0,1)
    x_min = findWhite(im)
    
    im_reverse = im[::-1]
    x_max = findWhite(im_reverse)
    x_max = width - x_max
    
    x_size = x_max - x_min
    y_size = y_max - y_min
    
    return (x_min, x_max, y_min, y_max)

#%%
sequencePath = "d:/sequence/convert"
images = [x for x in os.listdir(sequencePath) if 'tif' in x]

q = ""
q = Queue.Queue(maxsize = 0)

for image in images:
    q.put(image)

q.qsize()
#%%



workers = []
for x in range(1):
    worker = threading.Thread(target=sequenceMinMax, args=(q,))
    worker.setDaemon(True)
    worker.start()

q.join()



#%%
def sequenceMinMax(q):
    
    global x_min
    global x_max
    global y_min
    global y_max
    while True:
        image = q.get()
        image = sequencePath + "/" + image
        
        a,b,c,d = findMinMax(image)
    
        if a > x_min:
            x_min = a
        if b < x_max:
            x_max = b
        if c > y_min:
            y_min = c
        if d < y_max:
            y_max = d    
        print x_min, x_max, y_min, y_max

#%%
def findWhite(im):
    count = 0
    for count, column in enumerate(im):
        if np.sum(column)/3/255 > 0:
            break
    return count
    
#%%
images = [x for x in os.listdir(sequencePath) if 'tif' in x]
image = r"d:/sequence/merged/merged.tif"
im = cv2.imread(image)
height, width, channels = im.shape

y_min = findWhite(im)
im_reverse = im[::-1]

y_max = findWhite(im_reverse)
y_max = height - y_max

im = np.swapaxes(im,0,1)
x_min = findWhite(im)

im_reverse = im[::-1]
x_max = findWhite(im_reverse)
x_max = width - x_max

x_size = x_max - x_min
y_size = y_max - y_min

#%%        
flag = "-crop %sx%s+%s+%s" % (x_size, y_size, x_min, y_min)

out_path = r"d:/sequence/merged/cropped.tif"
in_path = r"d:/sequence/merged/merged.tif"

imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (in_path, flag, out_path)            
subprocess.call(imageMagickCMD)

#%%



q = ""
q = Queue.Queue(maxsize = 0)
len(images)
for image in images:
    q.put(image)

    

#%%
def cropImage(q):
    while True:
        image = q.get()
        in_path = sequencePath + "/" + image
        out_dir = sequencePath + "/cropped"
        fileName, fileType = image.split(".")
            
        flag = "-compress zip -crop %sx%s+%s+%s" % (x_size, y_size, x_min, y_min)
        if os.path.isdir(out_dir) == False:
            os.makedirs(out_dir)
        out_path = out_dir + "/" + fileName + ".tif"
        
        imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (in_path, flag, out_path)            
        subprocess.call(imageMagickCMD)

#%%
workers = []
for x in range(8):
    worker = threading.Thread(target=cropImage, args=(q,))
    worker.setDaemon(True)
    worker.start()
    workers.append(worker)

for worker in workers:
    worker.join()