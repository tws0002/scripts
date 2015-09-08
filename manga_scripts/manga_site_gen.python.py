import jinja2
import os
import csv
import uniout
import subprocess
csv_path = "d:/manga_list.csv"

csv_list = []
with open(csv_path, 'rb') as csvfile:
    csv_content = csv.reader(csvfile, delimiter=',')
    for row in csv_content:
        csv_list.append([unicode(row[0], 'Big5'), unicode(row[1], 'Big5'), row[2]])

csv_list = csv_list

templateLoader = jinja2.FileSystemLoader( searchpath="//Art-1405260002/d/assets/manga/templates" )
templateEnv = jinja2.Environment( loader=templateLoader )

book_template = "manga_book.template"
index_template = "manga_index.template"

path = "//Art-1405260002/d/assets/manga/"

#-------------------------------start
#template = templateEnv.get_template(index_template)

ignore_dir = ["css", "templates", "images"]
mangas = [m for m in os.listdir(path) if m not in ignore_dir if os.path.isdir(os.path.join(path,m))]
mangas = mangas[0:1]

#manga = mangas[0]
#-------------------------------chapter index
for manga in mangas:
    manga_author, manga_chn = [(x[0], x[1]) for x in csv_list if x[2] == manga][0]

    chapters = [x[1] for x in os.walk((path + manga).decode('mbcs'))][0]
    try:
        chapters.remove("cover")
    except:
        pass    
    
    chapter_list = [] #same as chapters
    i = 0
    for chapter in chapters:
        next_number = i + 1
        prev_number = i - 1
        print chapter
        image_path = path + manga + "/" + chapter
        chapter_index = "http://vg.com/assets/manga/" + "/" + manga +".html"
        #temp = os.listdir(image_path)
        images = [x for x in os.listdir(image_path) if x != 'Thumbs.db' and 'thumb' not in x]
    
        if prev_number < 0:
            prev_chapter = ""
            next_chapter = "http://vg.com/assets/manga/" + manga + "/" + chapters[next_number] + ".html"
        elif next_number >= len(chapters):
            prev_chapter = "http://vg.com/assets/manga/" + manga + "/" + chapters[prev_number] + ".html"
            next_chapter = ""
        else:
            prev_chapter = "http://vg.com/assets/manga/" + manga + "/" + chapters[prev_number] + ".html"
            next_chapter = "http://vg.com/assets/manga/" + manga + "/" + chapters[next_number] + ".html"
    
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
        
        #-------------------------------cover image conversion
        thumb = [x for x in os.listdir(image_path) if x != 'Thumbs.db' and 'thumb' in x]
        if len(thumb) > 0:
            thumb_web_path = "http://vg.com/assets/manga/" + manga + "/" + chapter + "/" + thumb[0]
        else:
            image = images[0]
            image_name, image_ext = os.path.splitext(image)
            image_network_path = image_path + "/" +  image
            thumb_network_path = image_path + "/" + image_name + "_thumb" + image_ext
        
            overwrite = False
            if overwrite == True:
                imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" -thumbnail \"2362x1000^\" -gravity Center -extent 1562x1000 -gravity West -extent 700x1000  \"%s\"" % (image_network_path, thumb_network_path)        
                subprocess.call(imageMagickCMD)
            else:
                if os.path.isfile(thumb_network_path) == True or os.path.isfile(thumb_network_path.replace("jpg", "png")): 
                    pass
                else:  
                    imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" -thumbnail \"2362x1000^\" -gravity Center -extent 1562x1000 -gravity West -extent 700x1000  \"%s\"" % (image_network_path, thumb_network_path)        
                    subprocess.call(imageMagickCMD)
        
            thumb_web_path = "http://vg.com/assets/manga/" + manga + "/" + chapter + "/" + image_name + "_thumb" + image_ext
    
        chapter_link = ("http://vg.com/assets/manga/" + manga + "/" + chapter + ".html")
        chapter_list.append({'link': chapter_link, 'thumb': thumb_web_path, 'number': 1})
        i += 1
        
    data = {    "title1" : manga_chn[0],
                "title2" : manga_chn[1:],
                "author" : manga_author,
                "chapter_list" : chapter_list
                   }
    
    template = templateEnv.get_template("manga_chapter_list.template")
    outputText = template.render( data )
    t = outputText.encode('utf8')
    f = open(path + manga + ".html",'w')
    f.write(t)
    f.close()
    
