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
import Queue


drivers = []
user = os.getenv('USERNAME')
def profs():
    adblockfile = '//art-cs005520513/julio/adblock_plus-2.6.7-sm+tb+fx+an.xpi'
    ffprofile = webdriver.FirefoxProfile("c:/Users/" + user + "/Downloads/profilemodel")
    ffprofile.set_preference("extensions.adblockplus.currentVersion", "2.6.7")
    ffprofile = webdriver.FirefoxProfile("c:/Users/" + user + "/Downloads/profilemodel")
    ffprofile.add_extension(adblockfile)
    return ffprofile
number_of_drivers = 8
for i in range(number_of_drivers):
    drivers.append(webdriver.Firefox(profs()))





#path = "//art-cs005520513/julio/3daa"
path = "f:/3daa"
item_folders = os.listdir(path)
#rar_link_file = "//art-cs005520513/julio/rarlink02.txt"
rar_link_file = "f:/rarlink04.txt"

q = Queue.Queue(maxsize=0)
start = 35000
end = 40000
for i in range(start, end):
    q.put(i)

print len(q.queue)
def getFiles(driver, q):
    while True:
        cur = q.get()
        folder = item_folders[cur]
        folder = str(folder)
        info_file = path + "/" + folder + "/info.txt"
        print folder

        try:
            with open(info_file) as file:
                data = file.read()
        except:
            print "nothing in folder"

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
                def getLink():
                    driver.get(link)
                    return driver.find_element_by_xpath("//span[@class='bt_down_rar']/a").get_attribute("href")

                for tries in range(0,30):
                    try:
                        rar_link = getLink()
                        break
                    except:
                        print "retrying"

                def getRarLink():
                    driver.get(rar_link)
                    return driver.find_element_by_xpath("//li[@class='bd']/a").get_attribute("href")

                for tries in range(0,30):
                    try:
                        src = getRarLink()
                        break
                    except:
                        print "retrying"

                dst_filename = src.split("/")[-1]
                dest = path + "/" + folder + "/" + dst_filename
                # write back into info.text

                # only append the rar link to unaltered info.txt
                if len(data.split(",")) == 6:
                    with open(info_file, "a") as file:
                        file.write("," + src)

                    with open(rar_link_file, "a") as file:
                        file.write(src + "\n")
                        q.task_done()


workers = []
for x in range(number_of_drivers):
    worker = threading.Thread(target=getFiles, args=(drivers[x],q,))
    worker.setDaemon(True)
    worker.start()
    workers.append(worker)

for worker in workers:
    worker.join()

print threading.active_count()


print dir(worker)
print "sadfsdf"
