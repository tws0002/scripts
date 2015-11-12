import jinja2
import os
import unicodecsv
import subprocess
csv_path = r"f:/manga_list08.csv"

#%%
csv_list = []
with open(csv_path, 'r') as csvfile:
    csv_content = unicodecsv.reader(csvfile, delimiter=',', lineterminator='\n')
    for row in csv_content:
        csv_list.append(row)

#%%
templateLoader = jinja2.FileSystemLoader( searchpath="//Art-1405260002/d/assets/scripts/manga_scripts/templates" )
templateEnv = jinja2.Environment(loader=templateLoader)

book_template = "manga_book.template"
index_template = "manga_index.template"

path = "//Art-1405260002/d/assets/manga/"

#%%
#template = templateEnv.get_template(index_template)

ignore_dir = ["css", "templates", "images", "covers", "mcd_covers"]
mangas = [m for m in os.listdir(path) if m not in ignore_dir if os.path.isdir(os.path.join(path,m))]
#mangas.index("appleseed")
#mangas = mangas[30:31]
#mangas = ['sidooh']

#%%
count = []
for x in csv_list:
    if x[13] == 'False':
        count.append(x[2])

count.sort()
for x in count:
    print x
#%%
for manga in mangas:
    print manga
    manga = '3x3eyes'
    html_path = "//art-1405260002/d/assets/manga/%s/index.html" % (manga)
    csv_manga = [x[2] for x in csv_list]
    if os.path.isfile(html_path) == True:
        pass
    elif manga not in csv_manga:
        pass
    else:
        #manga_author, manga_chn = [(x[0], x[1]) for x in csv_list if x[2] == manga][0]
        title, title_chn, author, author_chn, description, cover_type = [(x[2], x[3], x[7], x[6], x[12], x[13]) for x in csv_list if x[2] == manga][0]
        ignore_words = ['a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on', 'at', 'to', 'from', 'by', 'of']    
        title = title.replace("_", " ").upper()
        char_count = len(title)
        title_font_size = char_count
        description = description.replace("**",",")
        
        chapters = [x[1] for x in os.walk((path + manga).decode('mbcs'))][0]
        try:
            chapters.remove("cover")
        except:
            pass    
            
        chapter_list = [] #same as chapters
        i = 1
        for chapter in chapters:
            #print chapters
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
            #print prev_number, next_number
       
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
            chapter_num = int(chapter.split("_")[1])
            if cover_type == 'True':        
                cover_link = "http://vg.com/assets/manga/mcd_covers/%s/vol_%02d_front_med.jpg" % (manga, chapter_num)
            elif cover_type == 'False':
                cover_path = "//art-1405260002/d/assets/manga/covers/%s/" % (manga)
                ext = os.listdir(cover_path)[0].split(".")[1]
                cover_link = "http://vg.com/assets/manga/covers/%s/Vol_%02d.%s" % (manga, chapter_num, ext)
                
    
            chapter_list.append({'link': chapter_link, 'number': i, 'cover':cover_link})
            i += 1
        if len(title_chn) == 0:
            manga_chn = ['  ']
        title_chn_ar = []
        author_chn_ar = []
        for x in title_chn:
            title_chn_ar.append(x)
        for x in author_chn:
            author_chn_ar.append(x)
    
        data = {    "title" : title,
                    "author" : author,
                    "title_chn" : title_chn_ar,
                    "author_chn" : author_chn_ar,
                    "chapter_list" : chapter_list,
                    "description" : description
                       }
        
        template = templateEnv.get_template("manga_chapter_list.template")
        outputText = template.render( data )
        t = outputText.encode('utf8')
        f = open(path + manga + "/index.html",'w')
        f.write(t)
        f.close()
        
