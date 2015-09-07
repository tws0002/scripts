import jinja2
import os
import csv
import uniout
csv_path = "d:/manga_list.csv"

csv_list = []
with open(csv_path, 'rb') as csvfile:
    csv_content = csv.reader(csvfile, delimiter=',')
    for row in csv_content:
        csv_list.append([unicode(row[0], 'Big5'), unicode(row[1], 'Big5'), row[2]])

for x in csv_list:
    print x[1]
    print unicode(x[1],'Big5')

csv_list = csv_list[0:10]    
print csv_list
# In this case, we will load templates off the filesystem.
# This means we must construct a FileSystemLoader object.
# 
# The search path can be used to make finding templates by
#   relative paths much easier.  In this case, we are using
#   absolute paths and thus set it to the filesystem root.
templateLoader = jinja2.FileSystemLoader( searchpath="//Art-1405260002/d/assets/manga/templates" )

# An environment provides the data necessary to read and
#   parse our templates.  We pass in the loader object here.
templateEnv = jinja2.Environment( loader=templateLoader )

# This constant string specifies the template file we will use.
book_template = "manga_book.template"
image_template = "manga_image.template"
index_template = "manga_index.template"

# Read the template file using the environment object.
# This also constructs our Template object.
path = "//Art-1405260002/d/assets/manga/"

manga = "blade_of_the_immortal"
manga_chn = "無限住人".decode("utf-8")

#-------------------------------main index
template = templateEnv.get_template(index_template)

ignore_dir = ["css", "templates", "images"]
mangas = [m for m in os.listdir(path) if m not in ignore_dir if os.path.isdir(os.path.join(path,m))]


for manga in mangas:
    chapters = [d for d in os.listdir(path + manga) if os.path.isdir(path + manga + "/" + d)]
    for chapter in chapters:
        images_path = path + manga + "/" + chapter
        #images = os.listdir(images_path)
        image = os.listdir(images_path)[0]

        if "-" in image:
            temp = image.split("-")
        elif "_" in image:
            temp = image.split("_")


        image = [x for x in temp if "." in x and x != 'Thumbs.db'][0].split(".")[0]
        print image
        


        image = [x for x in images if x != 'Thumbs.db' and x.split("-")[1][0:3] == '001' and "thumb" not in x][0]
        image = [x for x in images if x != 'Thumbs.db' and x.split(".")[0][:-3]]
        
        image.split("_")
        numbers = [s for s in image if s.isdigit()] 
        print numbers
        image = images[10]



#-------------------------------chapter index
template = templateEnv.get_template(book_template)

chapters = [d for d in os.listdir(path + manga) if os.path.isdir(path + manga + "/" + d)]            

books = []
number = 0
for chapter in chapters:
    number += 1
    images_path = path + manga + "/" + chapter

    image = [x for x in os.listdir(images_path) if x != 'Thumbs.db' and 'thumb' not in x][0]

    #convert first image to thumbnail
    temp = image.split(".")
    image_name = temp[0]
    image_ext = temp[1]
    image_network_path = images_path + "/" +  image
    thumb_network_path = images_path + "/" + image_name + "_thumb" + "." + image_ext
  
    if os.path.isfile(thumb_network_path) == True:
        pass
    else:  
        imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" -thumbnail \"2362x1000^\" -gravity Center -extent 1562x1000 -gravity West -extent 700x1000  \"%s\"" % (image_network_path, thumb_network_path)        
        subprocess.call(imageMagickCMD)

    thumb_web_path = "http://vg.com/assets/manga/" + manga + "/" + chapter + "/" + image_name + "_thumb" + "." + image_ext
    chapter_link = ("http://vg.com/assets/manga/" + manga + "/" + chapter + ".html")
    books.append({'link': chapter_link, 'thumb': thumb_web_path, 'number': number})
    
data = {    "title1" : manga_chn[0],
            "title2" : manga_chn[1:],
            "books" : books
               }
               
outputText = template.render( data )
print outputText
t = outputText.encode('utf8')
f = open(path + manga + ".html",'w')
f.write(t) # python will convert \n to os.linesep
f.close() 

#-------------------------------image index
template = templateEnv.get_template(image_template)
i = 0
for chapter in chapters:
    next_number = i + 1
    prev_number = i - 1
    image_path = path + manga + "/" + chapter
    chapter_index = "http://vg.com/assets/manga/" + "/" + manga +".html"
    temp = os.listdir(image_path)
    if prev_number < 0:
        prev_chapter = ""
        next_chapter = "http://vg.com/assets/manga/" + manga + "/" + chapters[next_number] + ".html"
    elif next_number >= len(chapters):
        prev_chapter = "http://vg.com/assets/manga/" + manga + "/" + chapters[prev_number] + ".html"
        next_chapter = ""
    else:
        prev_chapter = "http://vg.com/assets/manga/" + manga + "/" + chapters[prev_number] + ".html"
        next_chapter = "http://vg.com/assets/manga/" + manga + "/" + chapters[next_number] + ".html"
    i += 1

    images = []
    for image in temp:
        if image == "Thumbs.db" :
            pass
        elif "thumb" in image:
            pass
        else:
            final_path = "http://vg.com/assets/manga/" + manga + "/" + chapter + "/" + image
            images.append({'link': final_path})

    data = {
        "images" : images,
        "chapter_index": chapter_index,
        "prev_chapter": prev_chapter,
        "next_chapter": next_chapter
            }
    outputText = template.render( data )
    f = open(path + "/" + manga + "/" + chapter + ".html",'w')
    f.write(outputText.encode('utf8')) # python will convert \n to os.linesep
    f.close() 



    
    



