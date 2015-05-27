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


driver.get("https://www.mixamo.com/3d-characters")
characters = driver.find_elements_by_xpath("//div[@class='pure-u-1-4']/a")

for character in characters:
    details = character.text
    name = character.text.split("\n")[0].replace(" ","_").replace("/","_").replace(",","_").replace(".","").replace("-","_").lower().encode('utf-8')
    if len(name.split("_")) == 3:
        if len(name.split("_")[1]) == 1:
            name = name.split("_")[0]
    if "by" in name:
        name = name.split("_by_")[0]

    name = name.replace("_j_j_ong","").replace("_j_nordstrom","")

    tags = character.text.split("\n")[1].encode('utf-8')
    link = character.get_attribute('href')

    base_path = "d:\\mixamo_models"
    item_path = base_path + "\\" + name
    if not os.path.exists(item_path):
        os.makedirs(item_path)
        info_file = item_path + "\info.txt"
        file_object = open(info_file, "w")
        info_content = "name=" + name + "\ntags=" + tags + "\nlink="+ link
        file_object.write(info_content)
        file_object.close()
    
    #dst = item_path + "\\" + (name + ".gif")
    #src = character.find_element_by_xpath("./figure/img").get_attribute('src').split("?")[0].replace("-first","")
    #urllib.urlretrieve(src, dst)

base_path = "d:\\mixamo_models"
item_path = base_path + "\\" + name

content = []
characters = os.listdir(base_path)

newlist = []
for character in characters:
    temp = base_path + "\\"  + character
    files = os.listdir(temp)
    if len(files) < 3:
        newlist.append(character)
        
characters = newlist
print characters

#-------------------------------------------------------
for character in characters:
    temp = base_path + "\\" + character

    files = os.listdir(temp)
    for f in files:
        if "txt" in f:
            info_file = base_path + "\\" + character + "\\" + f
        elif "gif" in f:
            gif_file = base_path + "\\" + character + "\\" + f

    file_object = open(info_file, "r")
    content = file_object.readlines()
    file_object.close()

    name = content[0].replace("name=", "").replace("\n", "")
    tags = content[1].replace("tags=", "")
    link = content[2].replace("link", "")

    driver.get(link)
    driver.execute_script("window.onbeforeunload = function(e){};")

    temp = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "md-overlay")))

    driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)

    download_button = driver.find_element_by_id("downloadButton")
    download_button.click()

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
    try:
        download_noskin.select_by_visible_text("T-Pose")
    except:
        download_noskin.select_by_visible_text("Include Skin")
    download_options = Select(driver.find_element_by_id("mini_formatselectbox"))
    download_options.select_by_visible_text("FBX (.fbx)")


    download_final = driver.find_element_by_xpath("//input[@id='miniDownloadSubmit']")
    name1 = driver.find_element_by_xpath("//strong[@class='p_name']").text.replace(" ","_") + ".fbx"

    fname = name1.split(".")[0].split("_")
    fname.pop(len(fname) - 1)
    ffname = ""
    for z in fname:
        ffname = ffname + "_" + z
    ffname = ffname[1:] + ".fbx"

    if "/" in name1 or "," in name1:
        source = "C:\\Users\\julio\\Downloads\\" + name1.replace("/", "_").replace(",", "_")
        destination = "d:\\mixamo_models\\" + character + "\\" + ffname.replace("/", "").replace(",", "")
    else:
        source = "C:\\Users\\julio\\Downloads\\" + name1
        destination = "d:\\mixamo_models\\" + character + "\\" + name + ".fbx"

    download_final.click()

    for x in range(0, 20):
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
