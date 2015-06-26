# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:51:40 2015

@author: julio
"""
import os
from selenium import webdriver
import time
import urllib2
from functools import wraps
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import threading
    
path = "f:/3daa"
item_folders = os.listdir(path)
adblockfile = 'c:/Users/julio/Downloads/adblock_plus-2.6.7-sm+tb+fx+an.xpi'
ffprofile1 = webdriver.FirefoxProfile("c:/Users/julio/Downloads/profilemodel")
ffprofile1.set_preference("extensions.adblockplus.currentVersion", "2.6.7")
ffprofile1 = webdriver.FirefoxProfile("c:/Users/julio/Downloads/profilemodel")
ffprofile1.add_extension(adblockfile)

ffprofile2 = webdriver.FirefoxProfile("c:/Users/julio/Downloads/profilemodel")
ffprofile2.set_preference("extensions.adblockplus.currentVersion", "2.6.7")
ffprofile2 = webdriver.FirefoxProfile("c:/Users/julio/Downloads/profilemodel")
ffprofile2.add_extension(adblockfile)

driver1 = webdriver.Firefox(ffprofile1)
driver2 = webdriver.Firefox(ffprofile2)

rar_link_file = "f:/rarlink.txt"
start = 6284
end = 10000
def getFiles(driver, start, end):
    for id in range(start,end):
        folder = item_folders[id]
        folder = str(folder)
        info_file = path + "/" + folder + "/info.txt"
        
        try:
            with open(info_file) as file:
                data = file.read()
        except:
            print "nothing in folder"
            
        print folder
        if len(os.listdir(path + "/" + folder)) == 0:
            print "nothing in folder"
            pass
        elif len(data.split(",")) > 6:
            pass
        else:
            filename = [x for x in os.listdir(path + "/" + folder) if x.split(".")[-1] == "rar"]
        
            if filename != []:
                if os.path.getsize(path + "/" + folder + "/" + filename[0]) == 0:
                    os.remove(path + "/" + folder + "/" + filename[0])
                    print  filename[0] + " is zero length, removing"
                    filename = []
            
            if filename == []:
                link = data.split(",")[5]
                def getlink(link):
                    driver.get(link)
                for retryno in range(0,10):
                    try:
                        getlink(link)
                        break
                    except:
                        print "connection lost"
                    
                rar_link = driver.find_element_by_xpath("//span[@class='bt_down_rar']/a").get_attribute("href")
                def getrarlink(rar_link)                :
                    driver.get(rar_link)
                for retryno in range(0,10):
                    try:
                        getrarlink(rar_link)
                        break
                    except:
                        print "connection lost"
                driver.get(rar_link)
                src = driver.find_element_by_xpath("//li[@class='bd']/a").get_attribute("href")
                dst_filename = src.split("/")[-1]
                dest = path + "/" + folder + "/" + dst_filename
                # write back into info.text
                
                # only append the rar link to unaltered info.txt                
                if len(data.split(",")) == 6:
                    with open(info_file, "a") as file:
                        file.write("," + src)

                with open(rar_link_file, "a") as file:
                    file.write(src + "\n")

import threading
import thread
from thread import start_new_thread

start_new_thread(getFiles, (driver1, 7095, 7100,))
start_new_thread(getFiles, (driver2, 7100, 7200,))

'''
for retryno in range(0,100):
    print retryno
    
threads = []
for work in range(0,2):
    t = threading.Thread(target=getFiles, args=(work))
    t.append(getFiles(driver1,7075,7100)
    getFiles(driver2, 7100, 7200)
except:
    print "some error"    
'''
                