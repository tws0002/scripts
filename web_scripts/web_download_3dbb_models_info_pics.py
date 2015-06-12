# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
sys.path.append("//Art-1405260002/d/assets/scripts/web_scripts")
from selenium import webdriver
import urllib
import urllib2
import errno
import os
import time
import jianfan
import keypress
import shutil
import ctypes
au_path = r"C:\Program Files (x86)\AutoIt3\AutoItX\AutoItX3.dll"
autoit = ctypes.windll.LoadLibrary(au_path)

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def retrying_urlopen(retries, *args, **kwargs):
    for i in range(retries):
        try:
            return urllib2.urlopen(*args, **kwargs)
        except URLError as e:
            if e.reason.errno == errno.EINPROGRESS:
                continue
            raise

print "sdfsf"
    

adblockfile = 'c:/Users/julio/Downloads/adblock_plus-2.6.7-sm+tb+fx+an.xpi'
ffprofile = webdriver.FirefoxProfile("c:/Users/julio/Downloads/profilemodel")
#ffprofile = webdrive.FirefoxProfile("C:\Users\julio\AppData\Roaming\Mozilla\Firefox\Profiles\hos6d1mx.default\adblockpluas")
ffprofile.set_preference("extensions.adblockplus.currentVersion", "2.6.7")
ffprofile = webdriver.FirefoxProfile("c:/Users/julio/Downloads/profilemodel")

ffprofile.add_extension(adblockfile)
driver = webdriver.Firefox(ffprofile)

mainpage = "http://www.3d66.com/model.html"

driver.get(mainpage)

# Main page
sub_types =[]
main_types = driver.find_elements_by_xpath("//div[@class='class_para']")
#info_file = "f:/3dbb_links.txt"
#file_object = open(info_file, "w")
for main_type in main_types:
    main_type_name = main_type.find_element_by_xpath("./p/a")
    sub_type_names = main_type.find_elements_by_xpath("./span/a")
    for sub_type_name in sub_type_names:
        sub_type_link = sub_type_name.get_attribute('href')
        mt_name = jianfan.jtof(main_type_name.text).replace(u'3d模型','')
        st_name = jianfan.jtof(sub_type_name.text)
        sub_types.append([mt_name, st_name, sub_type_link])        
        #info_content = (mt_name + "," + st_name + "," + sub_type_link + "\n").encode('utf-8')
        #file_object.write(info_content)
#file_object.close()

saved = sub_types
'''
x = 0
for save in saved:
    x = x + 1
    print save[1], x
'''
# main type, sub type, link

    driver.get(saved[44][2])

for y in range(44,61): # go to sub category
    driver.get(saved[y][2])
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "softpagenav")))

    links = []
    maxpage = driver.find_elements_by_xpath("//div[@id='softpagenav']/ul/li")[-1].text.split("/")[1]
    subcatid = saved[y][2].replace(".html","").split("_")[2]
    maxpage = int(str(maxpage))
    base = "http://www.3d66.com/"
    for p in range(1,(maxpage + 1)):
        link = base + "model_" + str(p) + "_" + str(subcatid) + ".html"
        links.append(link)
    print links

    if y == 39:
        pp = 2
    else:
        pp = 0
    for z in range(pp, len(links)):    
        driver.get(links[z])
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "King_Chance_Layer_Content")))
        page_title = driver.title
    
        item_pages = driver.find_elements_by_xpath("//div[@class='l_prolist']/dl/dd/p[@class='im']/a")
        item_pages.pop(0)
    
        def savePage():
            saveas = ActionChains(driver).key_down(Keys.CONTROL).send_keys('s').key_up(Keys.CONTROL)
            saveas.perform()
            autoit.AU3_WinActivate(u'Save As', u'')
            keypress.save_as()
            time.sleep(3)

        def pressEnter():
            autoit.AU3_WinActivate(u'Save As', u'')
            keypress.save_as()
            time.sleep(3)

        savePage()
            
        for i in range(0,10): #retry loop
       
            if os.path.exists("c:/users/julio/Downloads/" + page_title + "_files") is False:
                autoit.AU3_WinActivate(u'Save As', u'')
                pressEnter()
            else:
                break
    
        
        for item_page in item_pages:
            item_sw = item_page.find_elements_by_xpath("../../ul/li")[0].text.replace(u"模型版本 ","")
            item_id = item_page.find_elements_by_xpath("../../ul/li")[1].text.replace("ID ", "")
            folder_name = "f:/3daa/" + str(item_id)
            
            if os.path.exists(folder_name) is True:
                pass
    
            elif os.path.exists(folder_name) is False:
                os.makedirs(folder_name)
                item_link = item_page.get_attribute('href')
                item_image_src  = item_page.find_element_by_xpath("./img").get_attribute('src').split("/")[-1].encode('utf-8')
                item_image_src = urllib.unquote(item_image_src).decode('utf-8')
                src_path = "c:/users/julio/Downloads/" + page_title + "_files/" + item_image_src
                dst_path = folder_name + "/" + item_image_src
    
                shutil.copy(src_path, dst_path)
    
                item_name = item_page.find_element_by_xpath("./img").get_attribute('alt')
    
                info_file = folder_name + "\info.txt"
                file_object = open(info_file, "w")
                info_content = (item_id.encode('utf-8') + "," + item_sw.encode('utf-8') + "," + saved[y][0].encode('utf-8') + "," + saved[y][1].encode('utf-8') +"," + jianfan.jtof(item_name).encode('utf-8') + "," + item_link.encode('utf-8'))
                file_object.write(info_content)
                file_object.close()
        
        shutil.rmtree("c:/users/julio/Downloads/" + page_title + "_files")
        os.remove("c:/users/julio/Downloads/" + page_title + ".htm")



