import jinja2
import os
import csv
import uniout
import subprocess
csv_path = "//Art-1405260002/d/assets/scripts/manga_scripts/manga_list.csv"
#csv_path = "//Art-1405260002/d/assets/scripts/manga_scripts/test.csv"
csv_list = []
with open(csv_path, 'rb') as csvfile:
    csv_content = csv.reader(csvfile, delimiter=',')
    for row in csv_content:
        csv_list.append([unicode(row[0], 'Big5'), unicode(row[1], 'Big5'), row[2]])

templateLoader = jinja2.FileSystemLoader( searchpath="//Art-1405260002/d/assets/scripts/manga_scripts/templates" )
templateEnv = jinja2.Environment( loader=templateLoader )

book_template = "manga_book.template"
index_template = "manga_index.template"

path = "//Art-1405260002/d/assets/manga/"

#-------------------------------start
#template = templateEnv.get_template(index_template)

ignore_dir = ["css", "templates", "images"]
mangas = [m for m in os.listdir(path) if m not in ignore_dir if os.path.isdir(os.path.join(path,m))]
mangas.index("sidooh")
mangas = mangas[562:]
#-------------------------------chapter index
len(csv_list)
for x in csv_list:
    if "gunnm" in x[2]:
        print x
    

#%%
for manga in mangas:
    manga_author, manga_chn = [(x[0], x[1]) for x in csv_list if x[2] == manga][0]
    
    print manga
    chapters = [x[1] for x in os.walk((path + manga).decode('mbcs'))][0]
    try:
        chapters.remove("cover")
    except:
        pass    
    
    chapter_list = [] #same as chapters

    i = 1
    for chapter in chapters:
        next_number = prev_number = None
        if len(chapters) == 1:
            pass
        elif i == 1:
            next_number = i + 1
        elif i > 1 and i < len(chapters) + 1:
            next_number = i + 1
            prev_number = i - 1
        elif i == len(chapters): # 
            prev_number = i - 1            
        print prev_number, next_number
   
        image_path = path + manga + "/" + chapter
        chapter_index = "http://vg.com/assets/manga/" + manga +"/index.html"
        #temp = os.listdir(image_path)
        images = [x for x in os.listdir(image_path) if x != 'Thumbs.db' and 'thumb' not in x]

        prev_chapter = ""
        next_chapter = ""    
        if len(chapters) == 1:
            pass
        elif prev_number < 1:
            prev_chapter = ""
            next_chapter = "http://vg.com/assets/manga/" + manga + "/" + chapters[next_number - 1] + ".html"
        elif next_number >= len(chapters):
            prev_chapter = "http://vg.com/assets/manga/" + manga + "/" + chapters[prev_number - 1] + ".html"
            next_chapter = ""
        else:
            prev_chapter = "http://vg.com/assets/manga/" + manga + "/" + chapters[prev_number - 1] + ".html"
            next_chapter = "http://vg.com/assets/manga/" + manga + "/" + chapters[next_number - 1] + ".html"

        image_links = []
        for image in images:
            final_path = "http://vg.com/assets/manga/" + manga + "/" + chapter + "/" + image
            image_links.append({'link': final_path})
    
        data = {
            "images" : image_links,
            "chapter_index": chapter_index,
            "prev_chapter": prev_chapter,
            "next_chapter": next_chapter
                }
    
        template = templateEnv.get_template("manga_image.template")
        outputText = template.render( data )
        f = open(path + "/" + manga + "/" + chapter + ".html",'w')
        f.write(outputText.encode('utf8')) # python will convert \n to os.linesep
        f.close() 
        
        chapter_link = ("http://vg.com/assets/manga/" + manga + "/" + chapter + ".html")
        chapter_list.append({'link': chapter_link, 'number': i})
        i += 1
    if len(manga_chn) == 0:
        manga_chn = ['  ']
    data = {    "title1" : manga_chn[0],
                "title2" : manga_chn[1:],
                "author" : manga_author,
                "chapter_list" : chapter_list
                   }
    
    template = templateEnv.get_template("manga_chapter_list.template")
    outputText = template.render( data )
    t = outputText.encode('utf8')
    f = open(path + manga + "/index.html",'w')
    f.write(t)
    f.close()
    
