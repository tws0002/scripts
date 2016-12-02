# -*- coding: utf-8 -*-
'''
import subprocess
import fileinput
input = "//Art-1405260002/d/assets/scripts/web_scripts/ui/web_123rf_download.ui"
output = "//Art-1405260002/d/assets/scripts/web_scripts/ui/web_123rf_download.py"
subprocess.call("C:/Python27/scripts/pyside-uic -o %s %s" % (output, input))
with open(output, 'r') as data:
    filedata = data.read()
header = "# -*- coding: utf-8 -*-\n"
header = header + "import sys\nsys.path.append(\"//Art-1405260002/d/assets/scripts/maya_scripts/lib\")\n"
filedata = header + filedata
with open(output, 'w') as data:
    data.write(filedata)

pyinstaller --onefile --icon=\\Art-1405260002\d\assets\scripts\web_scripts\icons\123rf.ico //Art-1405260002/d/assets/scripts/web_scripts/web_download_123rf.py
python //art-1405260002/d/assets/scripts/web_scripts/web_download_123rf.py
'''
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys
import os, sys, time, subprocess, csv, pickle
import multiprocessing
import Queue

sys.path.append("//Art-1405260002/d/assets/scripts/web_scripts/ui")

from PySide import QtCore, QtGui
import web_123rf_download as downloadUi
reload(downloadUi)
# initialized selenium firefox
#%%
class MainWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = downloadUi.Ui_Form()
        self.ui.setupUi(self)
        sshFile = "//Art-1405260002/d/assets/scripts/maya_scripts/lib/darkorange.stylesheet"
        with open(sshFile, "r") as fh:
            self.setStyleSheet(fh.read())

        self.ui.search_button.clicked.connect(self.search)
        self.quota = self.ui.quota_lineEdit.text()
        self.image_links = []
       
    def start(self):
        self.searchThread = searchThread()
        #self.listenerThread = listenerThread()
       
    def search(self):
        keyword = self.ui.search_lineEdit.text()

        quota = self.ui.quota_lineEdit.text()
        quota = int(quota)
        
        self.searchThread.search(keyword, quota)
        self.ui.download_button.setEnabled(True)        
        self.ui.download_button.clicked.connect(self.searchThread.multiprocess_download)
        self.searchThread.signal.finished.connect(self.finished)
        
    def finished(self, data):
        if data == True:
            self.close()
        


class MySignal(QtCore.QObject):
    finished = QtCore.Signal(bool)


class searchThread(QtCore.QThread):
    global outputQueue
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.start()
        self.downloaded_id = []
        self.image_links = []
        self.signal = MySignal()    

 
    def start(self):
        ffprofile = webdriver.FirefoxProfile("//Art-1405260002/d/assets/scripts/donotupload/zkIiCA3d.default")
        ffprofile.set_preference("browser.download.folderList",2)
        ffprofile.set_preference("browser.download.manager.showWhenStarting",0)
        ffprofile.set_preference("browser.download.dir","c:\\downloads")
        ffprofile.set_preference("browser.helperApps.neverAsk.saveToDisk","image/jpeg");

        self.driver = webdriver.Firefox(ffprofile) 
        mainpage = "http://www.123rf.com"
        
        self.driver.get(mainpage)

        import pw
        username = pw.username
        password = pw.password
        
        loginButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "signin_panel_btn")))
        loginButton.click()
        
        loginFrame = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "cboxIframe")))
        self.driver.switch_to_frame(loginFrame)
        
        userField = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, "panel_field_uid")))
        userField.send_keys(username)
        
        passField = self.driver.find_element_by_id("panel_field_password")
        passField.send_keys(password)
        
        loginButton2 = self.driver.find_element_by_id("panel_login_submit")
        loginButton2.click()  

        pickle.dump( self.driver.get_cookies() , open("cookies.pkl","wb"))
        
        download_dir = "c:/downloads"
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
#        if not os.path.exists(download_dir + "/l"):            
#            os.makedirs(download_dir + "/l")
#        if not os.path.exists(download_dir + "/xl"):            
#            os.makedirs(download_dir + "/xl")            
#        if not os.path.exists(download_dir + "/xxl"):            
#            os.makedirs(download_dir + "/xxl")
#            
        


    def getLinks(self):
        items = self.driver.find_elements_by_xpath("//div[@id='main_container_mosaic']/div")
        if len(items) < self.quota: # if search result is less then quota, reset quota
            self.quota = len(items)

        for item in items:
            image_id = item.get_attribute('onmouseout').replace("hideMosaicContainer('","").replace("');","")    
            if image_id not in self.downloaded_id and self.quota_count != 0:
                self.downloaded_id.append(image_id)
                self.image_links.append(item.find_element_by_xpath(".//a[@class='pdetail']").get_attribute('href'))
                self.quota_count = self.quota_count - 1        
        if(self.quota_count != 0):
            self.nextPage()

    def nextPage(self):
        nextPageButton = self.driver.find_elements_by_xpath("//button[@id='gosubmit']")
        if(len(nextPageButton) == 1):
            nextPageButton[0].click()        
        else:
            nextPageButton[1].click()
    
    def search(self, keyword, quota):
        self.downloaded_id = []        
        with open('//art-1405260002/d/assets/scripts/web_scripts/data/downloaded.csv') as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            for row in data:
                self.downloaded_id.append(row[0])  
                
        self.quota = int(quota)
        self.quota_count = int(quota)

        
        searchBox = self.driver.find_element_by_id("searchtext")
        searchBox.clear()
        searchBox.send_keys(keyword)
        searchButton = self.driver.find_element_by_id("gosubmit2")
        
        searchButton.click()

        while self.quota_count > 0:
            self.getLinks()

        self.q = multiprocessing.Queue()
        for link in self.image_links:
            self.q.put(link)
        self.q.put("STOP")
    
    def multiprocess_download(self):
        worker_args = [self.q,outputQueue]
        cpuCount = 4
        jobs = []
        for x in range(cpuCount):
            try:
                self.worker = multiprocessing.Process(target=worker_download_links, args=worker_args)
                self.worker.daemon = True
                jobs.append(self.worker)
                self.worker.start()
            except EOFError:
                break
            except:
                pass
        for job in jobs:
            job.join()

        outputList = []
        while True:
            try:
                x = outputQueue.get()
                if x == "STOP":
                    print x
                    break
                else:
                    outputList.append(x)
            except Queue.Empty:
                print 'break'
                break
            
        csvfile = open('//art-1405260002/d/assets/scripts/web_scripts/data/downloaded.csv', 'a')
        for y in outputList:
            csvfile.write(y + "\n")
        csvfile.close()
        
        self.driver.close()
        self.signal.finished.emit(True)
    
def login(driver):
    username = "cy919"
    password = "chungyo36f"
    
    loginButton = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "signin_panel_btn")))
    loginButton.click()
    
    loginFrame = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "cboxIframe")))
    driver.switch_to_frame(loginFrame)
    
    userField = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "panel_field_uid")))
    userField.send_keys(username)
    
    passField = driver.find_element_by_id("panel_field_password")
    passField.send_keys(password)
    
    loginButton2 = driver.find_element_by_id("panel_login_submit")
    loginButton2.click()          
    
def worker_download_links(q, outputQueue):
    def download(image_id, size):
        try:
            downloadButton = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "downloadlinknew")))
            #downloadButton = driver.find_element_by_xpath("//a[@id='downloadlinknew']")
            downloadButton.click()
            
            savepath = "c:/downloads/" + image_id + "_" + size + ".jpg"
            os.path.isfile(savepath)
            while os.path.isfile(savepath) != True or os.path.isfile(savepath + ".part") == True:
                time.sleep(1)
            print (image_id + " success")
            basket = driver.find_element_by_id("details_download_basket")
            driver.execute_script("jQuery(arguments[0]).hide();", basket)  
            
            overlay = driver.find_element_by_id("details_download_overlay_comp")
            driver.execute_script("jQuery(arguments[0]).hide();", overlay) 
            return True
        except:
            return False

    def getSizes():
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "font11px")))
        sizes = driver.find_elements_by_xpath("//div[@class='font11px']/div")
        selSize = ''
        sz = ''
        for size in sizes:
            try:            
                data = size.get_attribute('onclick')
                if "JPG" in data and "hiweb" in data:
                    selSize = size
                    sz = 'ml'
                elif "JPG" in data and "med" in data:
                    selSize = size
                    sz = 'l'
                elif "JPG" in data and "high" in data:
                    selSize = size
                    sz = 'xxl'
                elif "JPG" in data and "mega" in data:
                    selSize = size
                    sz = 'xxl'
            except:
                pass    
        selSize.click()
        return sz
        
        
        
        #close_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "details_download_exit_comp")))
        #close_button.click()
        
    cookies = pickle.load(open("cookies.pkl", "rb"))
    ffprofile = webdriver.FirefoxProfile("//Art-1405260002/d/assets/scripts/donotupload/zkIiCA3d.default")
    ffprofile.set_preference("browser.download.folderList",2)
    ffprofile.set_preference("browser.download.manager.showWhenStarting",0)
    ffprofile.set_preference("browser.download.dir","c:\\downloads")
    ffprofile.set_preference("browser.helperApps.neverAsk.saveToDisk","image/jpeg");

    driver = webdriver.Firefox(ffprofile) 
    driver.get("http://www.123rf.com/privacy.php")
    
    for cookie in cookies:
        try:
            driver.add_cookie(cookie)
        except:
            pass

    while True:
        try:
            link = q.get(block=True, timeout=0.1)
            if link == "STOP":
                outputQueue.put("STOP")
                break            
            driver.get(link)

            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "kw_list")))
            kw_list = driver.find_elements_by_xpath("//div [@id='kw_list']/a")
            keywords = []
            for kw in kw_list:
                keywords.append(kw.text.replace(","," "))
            keywords = "|".join(keywords)
            title = driver.find_element_by_xpath("//a[@id='compImg_link']").get_attribute('title').replace(","," ")
            image_id = driver.find_element_by_xpath("//span[@itemprop='productID']").text.replace(","," ")
            image_type = driver.find_elements_by_xpath("//div[@class='imginfo']/span")[1].text.replace(","," ")
            output = "%s,%s,%s,%s" % (image_id, title, image_type, keywords)
            outputQueue.put(output)                


            dok = False
            first_run = True
            while dok == False:  
                try:
                    if first_run == False:
                        driver.get(link)
                    sz = getSizes()
                    dok = download(image_id, sz)                
                    first_run = False
                except:
                    dok = False
                    first_run = False

            time.sleep(1.5)

        except Queue.Empty:
            break
    driver.close()
        #%%
if __name__=='__main__':
    multiprocessing.freeze_support()
    try:
        if sys.platform.startswith('win'):
            import multiprocessing.popen_spawn_win32 as forking
        else:
            import multiprocessing.popen_fork as forking
    except ImportError:
        import multiprocessing.forking as forking

    if sys.platform.startswith('win'):
        class _Popen(forking.Popen):
            def __init__(self, *args, **kw):
                if hasattr(sys, 'frozen'):
                    os.putenv('_MEIPASS2', sys._MEIPASS)
                try:
                    super(_Popen, self).__init__(*args, **kw)
                finally:
                    if hasattr(sys, 'frozen'):
                        if hasattr(os, 'unsetenv'):
                            os.unsetenv('_MEIPASS2')
                        else:
                            os.putenv('_MEIPASS2', '')
        forking.Popen = _Popen    
    outputQueue = multiprocessing.Queue()
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.start()
    sys.exit(app.exec_())

#%%


