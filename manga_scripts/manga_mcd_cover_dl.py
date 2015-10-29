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
mangadb = r"f:/manga_list07.csv"
with open(mangadb,"r") as infile:
    csvreader = unicodecsv.reader(infile, delimiter=",", lineterminator="\n")
    for row in csvreader:
        if row[13] == 'True':
            mid = row[0]
            manga = row[2]
            haspath = os.listdir(r"f:/mcd_covers/")
            if manga in haspath:
                pass
            else:
                print "Getting " + manga + " \n"
                manga_path = base_path + mid
                driver.get(manga_path)        
                volumes = driver.find_elements_by_xpath("//div[@class='col-md-3']")
                count = len(volumes)
                cover_path = "f:/mcd_covers/%s/" % manga
                if os.path.isdir(cover_path) == False:
                    os.mkdir(cover_path)
                
                for volume in range(1,count + 1):
                    small_src = "http://mcd.iosphe.re/t/" + mid + "/" + str(volume) + "/front/a/"
                    med_f_src = "http://mcd.iosphe.re/n/" + mid + "/" + str(volume) + "/front/a/"
                    med_b_src = "http://mcd.iosphe.re/n/" + mid + "/" + str(volume) + "/back/a/"
                    med_s_src= "http://mcd.iosphe.re/n/" + mid + "/" + str(volume) + "/side/a/"
                    lrg_src= "http://mcd.iosphe.re/r/" + mid + "/" + str(volume) + "/front/a/"
                
                    small_dst = r"f:/mcd_covers/%s/vol_%02d_front_sml.jpg" % (manga, volume)
                    med_f_dst = r"f:/mcd_covers/%s/vol_%02d_front_med.jpg" % (manga, volume)
                    med_b_dst = r"f:/mcd_covers/%s/vol_%02d_back_med.jpg" % (manga, volume)
                    med_s_dst = r"f:/mcd_covers/%s/vol_%02d_side_med.jpg" % (manga, volume)
                    lrg_dst = r"f:/mcd_covers/%s/vol_%02d_front_lrg.jpg" % (manga, volume)
                    
                    retrieve = Queue.Queue(maxsize=0)
                    retrieve.put([small_src, small_dst])
                    retrieve.put([med_f_src, med_f_dst])
                    retrieve.put([med_b_src, med_b_dst])
                    retrieve.put([med_s_src, med_s_dst])
                    retrieve.put([lrg_src, lrg_dst])    
                    
                    workers = []
                    for x in range(5):
                        worker = threading.Thread(target=getFiles, args=(retrieve,))
                        worker.setDaemon(True)
                        worker.start()
                        workers.append(worker)
                    
                    for worker in workers:
                        worker.join()

    
#%%




