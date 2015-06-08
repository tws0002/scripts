# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver
import urllib2
import os
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


adblockfile = 'c:/Users/julio/Downloads/adblock_plus-2.6.7-sm+tb+fx+an.xpi'
ffprofile = webdriver.FirefoxProfile("c:/Users/julio/Downloads/profilemodel")
#ffprofile = webdrive.FirefoxProfile("C:\Users\julio\AppData\Roaming\Mozilla\Firefox\Profiles\hos6d1mx.default\adblockpluas")
ffprofile.set_preference("extensions.adblockplus.currentVersion", "2.6.7")
ffprofile = webdriver.FirefoxProfile("c:/Users/julio/Downloads/profilemodel")

ffprofile.add_extension(adblockfile)
driver = webdriver.Firefox(ffprofile)

mainpage = "http://www.3d66.com/model.html"

driver.get(mainpage)


sub_types =[]
main_types = driver.find_elements_by_xpath("//div[@class='class_para']")
for main_type in main_types:
    main_type_name = main_type.find_element_by_xpath("./p/a")
    sub_type_names = main_type.find_elements_by_xpath("./span/a")
    for sub_type_name in sub_type_names:
        sub_type_link = sub_type_name.get_attribute('href')
        mt_name = main_type_name.text
        st_name = sub_type_name.text
        sub_types.append([mt_name, st_name, sub_type_link])        

saved = sub_types

for y in range(0,len(saved)): # go to sub_page

driver.get(saved[0][2])

item_pages = driver.find_elements_by_xpath("//div[@class='l_prolist']/dl/dd/p[@class='im']/a")
print len(item_pages)
item_pages.pop(0)
for item_page in item_pages:
    item_link = item_page.get_attribute('href')
    temp = item_page.find_element_by_xpath("./img")
    item_image = temp.get_attribute('src')
    item_name = temp.get_attribute('alt')
    print item_image, item_name, item_link

temp = item_pages[1]
print item_pages[4].text
print item_pages[1].find_element_by_xpath('./img').get_attribute('src')
