# -*- coding: utf-8 -*-
from selenium import webdriver
import urllib2
import os
import time
adblockfile = 'c:/Users/julio/Downloads/adblock_plus-2.6.11-sm+tb+fx+an.xpi'
ffprofile = webdriver.FirefoxProfile("C:/Users/julio/AppData/Local/Mozilla/Firefox/Profiles")
ffprofile.add_extension(adblockfile)
driver = webdriver.Firefox(ffprofile)

mainpage = "http://en.dm5.com/manhua-yiquanchaoren/"
base = "http://en.dm5.com"
driver.get(mainpage)

#%%
chapters = driver.find_elements_by_xpath("//ul[@id='cbc_3']/li/a")
chapter_links = []
for chapter in chapters:
    chapter_links.append(chapter.get_attribute('href'))

#len(chapter_links)
#chapter_links = chapter_links[0:2]
#%%
for chapter_link in chapter_links:
    driver.get(chapter_link)
    driver.execute_script( "window.onbeforeunload = function(e){};" ) # turn off all js
    title = driver.find_element_by_xpath("//div[@class='view_bt']/h1").text
    chapter_id = title.replace(u"一拳超人","").replace(u"原作版","").replace(u"话","")
    pages = driver.find_elements_by_xpath("//select[@id='pagelist']/option")
    option_value = pages[0].get_attribute('value').replace("-p1/","")
    for x in range(1, len(pages) + 1):
        current_page = "%02d" % x
        link = base + option_value + "-p" + str(x) + "/"
        if x == 1:
            pass
        else:
            driver.get(link)
        src = driver.find_element_by_xpath("//img[@id='cp_image']").get_attribute('src')
        dest_path = "c:/Users/julio/Downloads/OPM/%03d/" % int(chapter_id)
        if os.path.isdir(dest_path) is False:
            os.makedirs(dest_path)
        dest = dest_path + str(current_page) + ".jpg"
        headers = { 'User-Agent' : 'Mozilla/5.0', 'Referer': link }
        imgRequest = urllib2.Request(src, headers=headers)
        imgData = urllib2.urlopen(imgRequest).read()
        output = open(dest,'wb')
        output.write(imgData)
        output.close()

    time.sleep(.5)
