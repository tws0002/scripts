# -*- coding: utf-8 -*-

from selenium import webdriver
import urllib
import os
import threading
import Queue
import unicodecsv

def getFiles(retrieve):
    while len(retrieve.queue) != 0:
        cur = retrieve.get()
        urllib.urlretrieve(cur[0], cur[1])
        
base_path = r'http://mcd.iosphe.re/manga/'

driver = webdriver.Firefox()

#%%
covers_path = r"f:/mcd_covers"
mcd_covers = os.listdir(covers_path)
print mcd_covers


#%%
mangadb = r"f:/manga_list08.csv"
with open(mangadb,"r") as infile:
    csvreader = unicodecsv.reader(infile, delimiter=",", lineterminator="\n")
    retrieve = Queue.Queue(maxsize=0)
    for row in csvreader:
        if row[13] == 'True' and row[2] not in mcd_covers:
            mid = row[0]
            manga = row[2]
            haspath = os.listdir(r"f:/mcd_covers/")
            if manga in haspath:
                pass
            else:
                print "Getting " + manga + " \n"
                manga_path = base_path + mid
                driver.get(manga_path)        
                volumes = driver.find_elements_by_xpath("//div[@class='col-md-3']/div/div/a")
                vol_range = []
                for x in volumes:
                    vol_range.append(x.get_attribute('href').split("/")[5])
                
                #count = len(volumes)
                cover_path = "f:/mcd_covers/%s/" % manga
                if os.path.isdir(cover_path) == False:
                    os.mkdir(cover_path)
                
                #for volume in range(1,count + 1):
                for volume in vol_range:
                    small_src = "http://mcd.iosphe.re/t/" + mid + "/" + str(volume) + "/front/a/"
                    med_f_src = "http://mcd.iosphe.re/n/" + mid + "/" + str(volume) + "/front/a/"
                    med_b_src = "http://mcd.iosphe.re/n/" + mid + "/" + str(volume) + "/back/a/"
                    med_s_src= "http://mcd.iosphe.re/n/" + mid + "/" + str(volume) + "/side/a/"
                    lrg_src= "http://mcd.iosphe.re/r/" + mid + "/" + str(volume) + "/front/a/"
                
                    small_dst = r"f:/mcd_covers/%s/vol_%02d_front_sml.jpg" % (manga, int(volume))
                    med_f_dst = r"f:/mcd_covers/%s/vol_%02d_front_med.jpg" % (manga, int(volume))
                    med_b_dst = r"f:/mcd_covers/%s/vol_%02d_back_med.jpg" % (manga, int(volume))
                    med_s_dst = r"f:/mcd_covers/%s/vol_%02d_side_med.jpg" % (manga, int(volume))
                    lrg_dst = r"f:/mcd_covers/%s/vol_%02d_front_lrg.jpg" % (manga, int(volume))
                    
                    retrieve.put([small_src, small_dst])
                    retrieve.put([med_f_src, med_f_dst])
                    retrieve.put([med_b_src, med_b_dst])
                    retrieve.put([med_s_src, med_s_dst])
                    retrieve.put([lrg_src, lrg_dst])  
#%%                    
backup = retrieve
len(retrieve.queue)                    

#%%                    
while len(retrieve.queue) != 0:
    workers = []
    for x in range(15):
        worker = threading.Thread(target=getFiles, args=(retrieve,))
        worker.setDaemon(True)
        worker.start()
        workers.append(worker)
    
    for worker in workers:
        worker.join()

    
#%%
mangadb = r"f:/manga_list08.csv"
with open(mangadb,"r") as infile:
    csvreader = unicodecsv.reader(infile, delimiter=",", lineterminator="\n", encoding='utf-8-sig')
    retrieve = Queue.Queue(maxsize=0)
    for row in csvreader:
        if row[2] == 'yotsuba':
            mid = int(row[0])
            mid = str(mid)
            manga = row[2]
            haspath = os.listdir(r"f:/mcd_covers/")
            if manga in haspath:
                pass
            else:
                print "Getting " + manga + " \n"
                manga_path = base_path + mid
                driver.get(manga_path)        
                volumes = driver.find_elements_by_xpath("//div[@class='col-md-3']/div/div/a")
                vol_range = []
                for x in volumes:
                    vol_range.append(x.get_attribute('href').split("/")[5])
                
                #count = len(volumes)
                cover_path = "f:/mcd_covers/%s/" % manga
                if os.path.isdir(cover_path) == False:
                    os.mkdir(cover_path)
                
                #for volume in range(1,count + 1):
                for volume in vol_range:
                    small_src = "http://mcd.iosphe.re/t/" + mid + "/" + str(volume) + "/front/a/"
                    med_f_src = "http://mcd.iosphe.re/n/" + mid + "/" + str(volume) + "/front/a/"
                    med_b_src = "http://mcd.iosphe.re/n/" + mid + "/" + str(volume) + "/back/a/"
                    med_s_src= "http://mcd.iosphe.re/n/" + mid + "/" + str(volume) + "/side/a/"
                    lrg_src= "http://mcd.iosphe.re/r/" + mid + "/" + str(volume) + "/front/a/"
                
                    small_dst = r"f:/mcd_covers/%s/vol_%02d_front_sml.jpg" % (manga, int(volume))
                    med_f_dst = r"f:/mcd_covers/%s/vol_%02d_front_med.jpg" % (manga, int(volume))
                    med_b_dst = r"f:/mcd_covers/%s/vol_%02d_back_med.jpg" % (manga, int(volume))
                    med_s_dst = r"f:/mcd_covers/%s/vol_%02d_side_med.jpg" % (manga, int(volume))
                    lrg_dst = r"f:/mcd_covers/%s/vol_%02d_front_lrg.jpg" % (manga, int(volume))
                    
                    retrieve.put([small_src, small_dst])
                    retrieve.put([med_f_src, med_f_dst])
                    retrieve.put([med_b_src, med_b_dst])
                    retrieve.put([med_s_src, med_s_dst])
                    retrieve.put([lrg_src, lrg_dst])  
#%%    
for x in retrieve.queue:
    print x
    
    
