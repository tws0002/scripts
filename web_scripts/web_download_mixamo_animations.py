import sys
sys.path.append("C:\Python27\Lib\site-packages\selenium-2.45.0-py2.7.egg")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import shutil
import urllib # to download stuff
import time
import os


driver = webdriver.Firefox()
driver.get("https://www.mixamo.com/motions")

login_form = driver.find_element_by_xpath("//a[@class='md-trigger']")
login_form.click()
email_input = driver.find_element_by_xpath("//input[@name='user_session[login]']")
email_input.send_keys("")
password_input = driver.find_element_by_xpath("//input[@name='user_session[password]']")
password_input.send_keys("")
login_submit = driver.find_element_by_xpath("//input[@class='primary-button'][@value='Log In']")
login_submit.click()
#----------------------end log in

# get all motions on page, download all gifs, gather all information and write to text file
# build directory structure


motionlink = []
# page loop


for x in range(1,4):
    driver.get("https://www.mixamo.com/motions?page=" + str(x) + "&order=relevance&character=2,3,4,5,6,9")
    #driver.get("https://www.mixamo.com/motions?page=" + str(x) + "&order=relevance") # load page
    #time.sleep(2) # wait 
    #temp = driver.find_elements_by_xpath("//div[@class='listOfMotions pure-g small-sides small-bottom wide']/div[@class='mini-motion-section motion-character-type-human pure-u-1-6']/a") # get all the motion divs
    temp = driver.find_elements_by_xpath("//div[@class='listOfMotions pure-g small-sides small-bottom wide']/div/a") # get all the motion divs
    driver.execute_script("test = document.getElementsByClassName('motions-tooltip');for(i=0;i<test.length;i++){test[i].style.visibility = 'visible';}") # unhide the hidden divs
    link_file = "d:\\mixamo\\animal_link.%03d.txt" % x
    link_file_object = open(link_file, "w")

    # item loop

    for y in range(0, len(temp)):


        db = []
        db = temp[y].find_elements_by_xpath("./div/div/div/p/strong") # get the hidden divs
        name = temp[y].find_element_by_xpath("./div/div/div[@class='name']/p").text.encode('utf-8')

        description = db[0].text.encode('utf-8')
        duration = db[1].text.encode('utf-8')
        id = db[2].text.encode('utf-8')
        base_path = "d:\\mixamo"
        item_path = base_path + "\\" + str(id)
        if not os.path.exists(item_path):
            os.makedirs(item_path)
            info_file = item_path + "\info.txt"
            file_object = open(info_file, "w")
            info_content = "name=" + name + "\ndescription=" + description + "\nduration=" + duration + "\nid=" + id + "\n"
            file_object.write(info_content)
            file_object.close()


        dst = item_path + "\\" + (id + ".gif")
        src = temp[y].find_element_by_xpath("../div/a/img").get_attribute('src')
        urllib.urlretrieve(src, dst)

        link = temp[y].get_attribute('href') + "\n"
        link_file_object.write(link)

    driver.execute_script("test = document.getElementsByClassName('motions-tooltip');for(i=0;i<test.length;i++){test[i].style.visibility = 'hidden';}")
    link_file_object.close()
   




#------------------
#build a single list of all links
content = []
temp = []
temp = [x for x in os.listdir("d:\mixamo") if ".txt" in x]

for x in range(1, len(temp) + 1):
    link_file = "d:\mixamo\link.%03d.txt" % x
    with open(link_file) as file_object:
        content = content + file_object.readlines()

content = set(content)
content = list(content)
#-------------------------
#download fbx



#-----------------

x = 1410
#for x in range(2015, len(content)):
for x in range(0, len(newlist)):
    link = newlist[x].replace("\n","")
    
    id = link.split("/")[len(link.split("/")) - 1]
    driver.get(link)
                    
    driver.execute_script("window.onbeforeunload = function(e){};")
    temp = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "md-overlay")))
        
    driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
        
    download_button = driver.find_element_by_id("downloadButton")
    download_button.click()
    
    #downloadclip = driver.find_element_by_id("bottomDownloaderMinMaxIcon")
    #downloadclip.click()
        
    def getclips():    
        temp = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "miniPurchasedClips")))

    tries = 0
    try:
        getclips()
    except:
        time.sleep(1)
        tries = tries + 1
        if tries > 10:
            pass
        else:
            getclips()
    download_list = driver.find_elements_by_xpath("//div[@id='miniPurchasedClips']/div")
    
    driver.execute_script("listobject = document.getElementById(\"miniPurchasedClips\");purchasedlist = listobject.getElementsByClassName(\"item\");purchasedlist[0].className += \" item-selected\";")
    
    
    download_noskin = Select(download_list[0].find_element_by_name("request[skin]"))
    download_noskin.select_by_visible_text("Skeleton Only")
    
    download_options = Select(driver.find_element_by_id("mini_formatselectbox"))
    download_options.select_by_visible_text("FBX (.fbx)")
    
    
    download_final = driver.find_element_by_xpath("//input[@id='miniDownloadSubmit']")
    name = driver.find_element_by_xpath("//strong[@class='p_name']").text.replace(" ","_") + ".fbx"
    
    
    fname = name.split(".")[0].split("_")
    fname.pop(len(fname) - 1)
    ffname = ""
    for z in fname:
        ffname = ffname + "_" + z
    ffname = ffname[1:] + ".fbx"
    
    
    
    if "/" in name or "," in name:
        source = "C:\\Users\\julio\\Downloads\\" + name.replace("/","_").replace(",","_")
        destination = "d:\\mixamo\\" + str(id).replace("\n","") + "\\" + ffname.replace("/","").replace(",","")
    else:
        source = "C:\\Users\\julio\\Downloads\\" + name
        destination = "d:\\mixamo\\" + str(id).replace("\n","") + "\\" + ffname
    
    download_final.click()
    
    for x in range (0,20):
        if os.path.isfile(source):
            size = os.stat(source).st_size
            if size == 0:
                time.sleep(1)
            else:
                new_size = os.stat(source).st_size
                if new_size == size:
                    shutil.copy2(source, destination)
                    break
                else:
                    time.sleep(1)
                    pass
        else:
            time.sleep(1)
            if x == 19:
                print x + " timed out"

    driver.execute_script("window.onbeforeunload = function(e){};")
   



    

#------------------------------------

mixamo = "d:\\mixamo\\"
temp = [d for d in os.listdir(mixamo) if 'txt' not in d]

def destinationName(name):
    fname = name.split(".")[0].split("_")
    fname.pop(len(fname) - 1)
    ffname = ""
    for z in fname:
        ffname = ffname + "_" + z
    ffname = ffname[1:] + ".fbx"
    return ffname

dl_folder = "C:\\Users\\julio\\Downloads\\"
dl_files = [d for d in os.listdir(dl_folder) if 'fbx' in d]


for x in temp:
    folder = "d:\\mixamo\\" + str(x)
    files = os.listdir(folder)
    for file in files:
        if ".fbx" in file:
            name_filter = file.replace(".fbx","")
      
            for dl_file in dl_files:
                if name_filter in dl_file:
                    source = "C:\\Users\\julio\\Downloads\\" + dl_file
                    ffname = destinationName(source).replace("C:\\Users\\julio\\Downloads\\","")
                    destination = "d:\\mixamo\\" + str(x) + "\\" + ffname
                    shutil.copy2(source, destination)
                    
                    #print source + "\n" + destination
code = []
for x in temp:
    folder = "d:\\mixamo\\" + str(x)
    files = os.listdir(folder)
    if len(files) < 3:
        code.append(x)


newlist = []
for x in content:
    for y in code:
        if ("new/" + y + "\n") in x:
            newlist.append(x)
        else:
            pass
print len(newlist)
print len(code)
print code
print newlist

print content[y]

print content[2029]

print len(content)

2235-2029






