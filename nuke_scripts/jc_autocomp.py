# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 16:10:54 2016

@author: julio
"""

#import SCRIPTSPATH
import sys
renderData = sys.argv[1]
basePath = sys.argv[2]  
fileName = sys.argv[3]
compPath = sys.argv[4]

scripts_path = "//Art-1405260002/d/assets"
sys.path.append(scripts_path + "/scripts/nuke_scripts")


import os
os.environ['NUKE_INTERACTIVE'] = "1"
import nuke
import jc_nk_autocomp
reload(jc_nk_autocomp)
comp = jc_nk_autocomp.AutoComp(renderData, basePath, fileName)
comp.relightComp()
nuke.scriptSave(compPath)

