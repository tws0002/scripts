from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#adblockfile = 'c:/Users/julio/Downloads/adblock_plus-2.6.11-sm+tb+fx+an.xpi'
#ffprofile = webdriver.FirefoxProfile("C:/Users/julio/AppData/Local/Mozilla/Firefox/Profiles")
#ffprofile.add_extension(adblockfile)
def getInfo(webObject, manga, mid=''):
    genrelist = ['action', 'adult', 'adventure', 'comedy', 'doujinshi', 'drama', 'ecchi', 'fantasy', 'gender bender', 'harem', 'hentai', 'historical', 'horror', 'josei', 'lolicon', 'martial arts', 'mature', 'mecha', 'mystery', 'psychological', 'romance', 'school life', 'sci-fi', 'seinen', 'shotacon', 'shoujo', 'shoujo-ai', 'shounen', 'shounen-ai', 'slice of life', 'smut', 'sports', 'supernatural', 'tragedy', 'yaoi', 'yuri']        
    driver = webObject
    data =  driver.find_elements_by_xpath("//div[@class='sContainer']/div[@class='sMember']/div")
    title = driver.find_element_by_xpath("//span[@class='releasestitle tabletitle']").text
    description = data[1].text.replace(",","**")
    assoc_names = data[7].text.split("\n")
    assoc_names = "|".join(assoc_names)
    volumes = data[13].text.split(" ")[0]
    
    if "Complete" in data[13].text:
        status = 'complete'
    elif "Ongoing" in data[13].text:
        status = 'ongoing'
    else:
        status = ''

    genre = data[29].text.lower().split("\n")[0]
    genre = [g for g in genrelist if g in genre]    
    author = data[37].text
    artist = data[39].text
    year = data[41].text
    #data = {'description': description, 'title': title, 'assoc_names':assoc_names, 'volumes': volumes, 'genre': genre, 'author':author, 'artist': artist, 'year': year}

    author_chn = manga.split(",")[0]
    name_chn = manga.split(",")[1]
    name = manga.split(",")[2]

    data = [mid, title, name, name_chn, assoc_names, genre, author_chn, author, artist, year, volumes, status, description]
    return data    

def sendSearch(source_name, webObject):
    driver = webObject
    search_bar = driver.find_element_by_xpath("//td/input[@name='search']")
    search_bar.clear()
    search_bar.send_keys(source_name)
    search_button = driver.find_elements_by_xpath("//td/input[@name='search']/../input")[1]
    search_button.click()
    return driver

def userInput(source_name, driver):
    wait_cmd = ""
    mainpage = "https://www.mangaupdates.com/series.html"
    driver.get(mainpage) 
    driver = sendSearch(source_name, driver)
    #WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "right_content")))
    mlist = driver.find_elements_by_xpath("//table[@class='text series_rows_table']/tbody/tr/td/a[@alt='Series Info']")
    if len(mlist) == 0:
        wait_cmd = 's'
        data = []
    else:
        print "\nSearching for \"%s\"...\n" % source_name
        for index, m in enumerate(mlist):
            print str(index + 1) + " " + m.text
        print "\n"
        #print "%s " % mlist[0].text   
        while wait_cmd == "":
            wait_cmd = raw_input('n to input number, s to skip, t to search again with chinese')
            if wait_cmd.isdigit() == True:
                series = int(wait_cmd)
                mid = mlist[series - 1].get_attribute('href').split('=')[1]
                mlist[series - 1].click()
                data = getInfo(driver, manga, mid=mid)
            elif wait_cmd == 's':
                data = [manga_id, "", manga.split(",")[2], manga.split(",")[1], "", "", manga.split(",")[0], "", "", "", "", "", ""]
            elif wait_cmd == 't':
                data = []
    return wait_cmd, data
#%%    
import unicodecsv    
driver = webdriver.Firefox()
#%% this part search for mangas on mangaupdates to gather information
manga_list = r"f:/manga_list02.csv"
new_list = r"f:/manga_list03.csv"
with open(manga_list, "r") as infile, open(new_list, "a+") as outfile:
    csvwriter = unicodecsv.writer(outfile, delimiter=",", lineterminator="\n")
    csvreader = unicodecsv.reader(outfile, delimiter=",", lineterminator="\n")
    mangas = infile.readlines()
    finish = ''
    exist_names = []
    for e in csvreader:
        try:
            exist_names.append(e[2].replace("_"," "))
        except:
            pass
    for manga in mangas:
        manga = manga.decode('big5').encode('utf8')    
        manga_id = manga.split(",")[3]
        if manga_id == "\n":
            manga_id = ""
        source_name = manga.split(",")[2]
        source_name_chn = manga.split(",")[1].replace("?","")
        source_name = source_name.replace("_", " ")
        if manga_id != "" or source_name in exist_names:
            pass
        else:
            w, data = userInput(source_name, driver)
            if w == 't':
                w, data = userInput(source_name_chn.decode('utf8'), driver)
            csvwriter.writerow(data)
#%% this part fills in mangas already with ids
manga_list = r"f:/manga_missing.txt"
new_list = r"f:/manga_list_06.csv"
with open(manga_list, "r") as infile, open(new_list, "a+") as outfile:
    csvwriter = unicodecsv.writer(outfile, delimiter=",", lineterminator="\n")
    csvreader = unicodecsv.reader(outfile, delimiter=",", lineterminator="\n")
    mangas = infile.readlines()
    finish = ''
    exist_names = []
    for e in csvreader:
        try:
            exist_names.append(e[2].replace("_"," "))
        except:
            pass
    for manga in mangas:
        #manga = manga.decode('big5').encode('utf8')    
        manga_id = manga.split(",")[3]
        if manga_id == "\n":
            manga_id = ""
        source_name = manga.split(",")[2]
        source_name_chn = manga.split(",")[1].replace("?","")
        source_name = source_name.replace("_", " ")
        if source_name in exist_names:
            pass
        elif manga_id != "":
            link = "https://www.mangaupdates.com/series.html?id=" + manga_id
            driver.get(link)
            data = getInfo(driver, manga, mid=manga_id)
            csvwriter.writerow(data)
#%% this part compares final db with mcd db
# if match, new column
import json
mcdjson = r"f:/mcdatabase.txt"
with open(mcdjson) as fileobj:
    data = fileobj.read()

jsondata = json.loads(data)        
mcd_ids = [] #len is 8954 as of Nov 2015
for x, y in jsondata.items():
    mcd_ids.append(x)

#%%
mangadb = r"f:/manga_list06.csv"
new_list = r"f:/manga_list07.csv"

with open(mangadb,"r") as infile, open(new_list,"w") as outfile:
    csvreader = unicodecsv.reader(infile, delimiter=",", lineterminator="\n")
    csvwriter = unicodecsv.writer(outfile, delimiter=",", lineterminator="\n")
    for row in csvreader:
        if row[0] in mcd_ids:
            row.append('True')            
        else:
            row.append('False')
        csvwriter.writerow(row)

#%% start pulling 




