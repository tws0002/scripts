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

def retry(ExceptionToCheck, tries=4, delay=3, backoff=2, logger=None):
    """Retry calling the decorated function using an exponential backoff.

    http://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
    original from: http://wiki.python.org/moin/PythonDecoratorLibrary#Retry

    :param ExceptionToCheck: the exception to check. may be a tuple of
        exceptions to check
    :type ExceptionToCheck: Exception or tuple
    :param tries: number of times to try (not retry) before giving up
    :type tries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param backoff: backoff multiplier e.g. value of 2 will double the delay
        each retry
    :type backoff: int
    :param logger: logger to use. If None, print
    :type logger: logging.Logger instance
    """
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck, e:
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        print msg
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)

        return f_retry  # true decorator

    return deco_retry
    
path = "f:/3daa"
item_folders = os.listdir(path)
adblockfile = 'c:/Users/julio/Downloads/adblock_plus-2.6.7-sm+tb+fx+an.xpi'
ffprofile = webdriver.FirefoxProfile("c:/Users/julio/Downloads/profilemodel")
ffprofile.set_preference("extensions.adblockplus.currentVersion", "2.6.7")
ffprofile = webdriver.FirefoxProfile("c:/Users/julio/Downloads/profilemodel")
ffprofile.add_extension(adblockfile)
driver = webdriver.Firefox(ffprofile)
start = 5000
end = 6000
def getFiles(start, end):
    for id in range(start,end):
        folder = item_folders[id]
        folder = str(folder)
        print folder
        if len(os.listdir(path + "/" + folder)) == 0:
            print "nothing in folder"
            pass
        else:
            info_file = path + "/" + folder + "/info.txt"
        
            filename = [x for x in os.listdir(path + "/" + folder) if x.split(".")[-1] == "rar"]
        
            if filename != []:
                if os.path.getsize(path + "/" + folder + "/" + filename[0]) == 0:
                    os.remove(path + "/" + folder + "/" + filename[0])
                    print  filename[0] + " is zero length, removing"
                    filename = []
        
            
            if filename == []:
                with open(info_file) as file:
                    data = file.read()
                    link = data.split(",")[-1]
        
                driver.get(link)
                rar_link = driver.find_element_by_xpath("//span[@class='bt_down_rar']/a").get_attribute("href")
                driver.get(rar_link)
                src = driver.find_element_by_xpath("//li[@class='bd']/a").get_attribute("href")
                dst_filename = src.split("/")[-1]
                dest = path + "/" + folder + "/" + dst_filename
        
                @retry(urllib2.URLError, tries=4, delay=3, backoff=2)
                def urlopen_with_retry(src1):
                    return urllib2.urlopen(src1, timeout=30)
        
                u = urlopen_with_retry(src)
                h = u.info()
                totalSize = int(h["Content-Length"])
                src_size = long(h.values()[0])
        
                dest_file = open(dest, 'wb')
        
                timeout = time.time() + 60 * 5   # 5 minutes from now
                blockSize = 8192
                count = 0
                try:
                    while True:
                        fileData = u.read(blockSize)
                        if not fileData or time.time() > timeout:
                            break
                        dest_file.write(fileData)
                        count += 1
                        if totalSize > 0:
                            percent = int(count * blockSize * 100 / totalSize)
                            if percent > 100: percent = 100
                            print "%2d%%" % percent,
                            if percent < 100:
                                print "\b\b\b\b\b",  # Erase "NN% "
                            else:
                                print "Done."
                    dest_file.flush()
                    dest_file.close()                
                except:
                    dest_file.flush()
                    dest_file.close()
        
                dst_size = os.path.getsize(path + "/" + folder + "/" + dst_filename)
            
                if dst_size == src_size:
                    print "file ok"
                else:
                    os.remove(path + "/" + folder + "/" + dst_filename)
                    print "file size not match " + dst_filename + " deleted"

for retryno in range(0,40000):
    print retryno
    try: 
        getFiles(start,end)
    except:
        print "some error"
        