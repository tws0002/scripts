# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:19:54 2015

@author: julio
"""

all_data = []

num_pages = driver.find_elements_by_xpath("//a[@class='pageNum-form']")
num_pages = num_pages[len(num_pages) - 1]
num_pages = num_pages.text
num_pages = int(num_pages)

for x in range(0,90):
    items = driver.find_elements_by_xpath("//div[@id='shContent']/div[@class='shList']")
    for item in items:
        item = items[2]
        temp = item.find_elements_by_xpath("./ul/li/div[@class='right']/p")
        name = temp[0].find_element_by_xpath("./a").get_attribute('title')
        address = temp[1].find_element_by_xpath(".").text
        misc = temp[2].find_element_by_xpath(".").text
        item_type, item_ppp, item_rooms, item_floors = misc.split(u"，")
        # clean up data further
        item_ppp = item_ppp.replace(u"單價：", "").replace(u"萬元","")
        item_ppp = float(item_ppp)
        rm_rms = int(item_rooms[0])
        rm_ld = int(item_rooms[2])
        rm_bth = int(item_rooms[4])
        floor, total_floors = item_floors.split(u"/")
        total_floors = int(total_floors)
        if u"整棟" in floor:
            floor = "all"
        else:
            floor = floor.replace(u"樓層：","")
            floor = int(floor)  
    
        all_data.append([name, address, item_type, item_ppp, rm_rms, rm_ld, rm_bth, floor, total_floors])
    try:
        page_link = driver.find_element_by_xpath("//a[@class='pageNext']")
    except:
        print "end"
    page_link.click()