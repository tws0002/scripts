# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 17:26:19 2015

@author: julio
"""
import os
import shutil
path = "F:/3dbb"
directories = os.listdir(path)
print len(directories)

for directory in directories:
    src = (path + "/" + directory + "/" + directory + ".jpg")
    dst = "%08d.jpg" % int(directory)
    dst = path + "/" + directory + "/" + dst
    shutil.copyfile(src, dst)
    os.remove(src)

for directory in directories:
    dsrc = (path + "/" + directory)
    newname = "%08d" % int(directory)
    ddst = (path + "/" + newname)

    shutil.copytree(dsrc, ddst)
    shutil.rmtree(dsrc)
    #os.rename(dsrc, ddst)
    
