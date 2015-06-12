# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:51:40 2015

@author: julio
"""

import os

path = "f:/test"
item_folders = os.listdir(path)

for folder in item_folders:
    info_file = path + "/" + folder + "/info.txt"
    with open(info_file) as file:
        data = file.read()
        link = data.split(",")[-1]

    