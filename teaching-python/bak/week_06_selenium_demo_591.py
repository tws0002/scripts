# -*- coding: utf-8 -*-
from selenium import webdriver
import urllib2
import os
import time
adblockfile = 'c:/Users/julio/Downloads/adblock_plus-2.6.11-sm+tb+fx+an.xpi'
ffprofile = webdriver.FirefoxProfile("C:/Users/julio/AppData/Local/Mozilla/Firefox/Profiles")
ffprofile.add_extension(adblockfile)
driver = webdriver.Firefox(ffprofile)

mainpage = "http://www.591.com.tw"
driver.get(mainpage)


#%% find all cities and their regions

city_button = driver.find_elements_by_xpath("//input[@id='region_id']")[0]
city_button.click()

temp = driver.find_elements_by_xpath("//div[@id='areabox']/div/ul[@class='content clearfix']/li")
cities = []
for city in temp:
    x = city.text
    i = x.index("(")
    x = x[:i]
    cities.append(x)
    
city_link = driver.find_elements_by_xpath("//div[@id='areabox']/div/ul[@class='content clearfix']/li/a")
for link in city_link:
    link = city_link[4]
    link.click()    

temp = driver.find_elements_by_xpath("//div[@id='areabox']/div/ul[@class='content clearfix']/li")
regions = []
for region in temp:
    x = region.text
    i = x.index("(")
    x = x[:i]
    regions.append(x)


#%% taichung north region
path = "http://sale.591.com.tw/house-rentSale-8-102-9-0-0.html"
driver.get(path)

# 1. specify data that needs to be scraped
#           name, 坪size, 坪price, rooms, floors, total price, popularity
# 2. inspect html and 
# 3. determine loops
# 4. find next page button
#%%
all_data = []

num_pages = driver.find_elements_by_xpath("//a[@class='pageNum-form']")
num_pages = num_pages[len(num_pages) - 1]
num_pages = num_pages.text
num_pages = int(num_pages)

#%%
import unicodecsv
filepath = r"c:\591data.csv"
with open(filepath, "w") as fobj:
    for x in range(0,num_pages):
        items = driver.find_elements_by_xpath("//div[@id='shContent']/div[@class='shList']")
        for item in items:
            temp = item.find_elements_by_xpath("./ul/li/div[@class='right']/p")
            name = temp[0].find_element_by_xpath("./a").get_attribute('title')
            address = temp[1].find_element_by_xpath(".").text
            misc = temp[2].find_element_by_xpath(".").text
            item_type, item_ppp, item_rooms, item_floors = misc.split(u"，")
            item_ppp = item_ppp.replace(u"單價：", "").replace(u"萬元","")
            rm_rms = item_rooms[0]
            rm_ld = item_rooms[2]
            rm_bth = item_rooms[4]
            floor, total_floors = item_floors.split(u"/")

            if u"整棟" in floor:
                floor = "all"
            else:
                floor = floor.replace(u"樓層：","")
            
            #all_data.append([name, address, item_type, item_ppp, rm_rms, rm_ld, rm_bth, floor, total_floors])
            csvwriter = unicodecsv.writer(fobj, encoding='utf-8', lineterminator='\n')
            csvwriter.writerow([name, address, item_type, item_ppp, rm_rms, rm_ld, rm_bth, floor, total_floors])
        try:
            page_link = driver.find_element_by_xpath("//a[@class='pageNext']")
        except:
            print "end"
        page_link.click()
        time.sleep(2)



    
