import jinja2
import os

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
template = templateEnv.get_template(book_template)


path = "//Art-1405260002/d/assets/manga/"
manga = "mushishi"
manga_chn = "蟲師".decode("utf-8")

chapters = [d for d in os.listdir(path + manga) if os.path.isdir(os.path.join(path + manga, d))]            
books = []
number = 0
for book in chapters:
    number += 1
    
    images_path = path + "/" + manga + "/" + book
    images = os.listdir(images_path)
    #image = [x for x in images if x != 'Thumbs.db' and x.split("-")[1][0:3] == '001' and "thumb" not in x][0]
    image = [x for x in images if x != 'Thumbs.db' and x.split("_")[1][0:4] == '0000' and "thumb" not in x][0]


    #convert first image to thumbnail
    temp = image.split(".")
    image_name = temp[0]
    image_ext = temp[1]
    image_network_path = images_path + "/" +  image
    thumb_network_path = images_path + "/" + image_name + "_thumb" + "." + image_ext
  
    if os.path.isfile(thumb_network_path) == True:
        pass
    else:  
        imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" -thumbnail \"800x600^\" -gravity Center -extent 800x600  \"%s\"" % (image_network_path, thumb_network_path)
        subprocess.call(imageMagickCMD)

    thumb_web_path = "http://vg.com/assets/manga/" + manga + "/" + book + "/" + image_name + "_thumb" + "." + image_ext
    chapter_link = ("http://vg.com/assets/manga/" + manga + "/" + book + ".html")
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

#-------------------------------
template = templateEnv.get_template(image_template)
i = 0
for chapter in chapters:
    next_number = i + 1
    prev_number = i - 1
    image_path = path + manga + "/" + chapter

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
    print prev_chapter
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
        "prev_chapter": prev_chapter,
        "next_chapter": next_chapter
            }
    outputText = template.render( data )

    f = open(path + "/" + manga + "/" + chapter + ".html",'w')
    f.write(outputText.encode('utf8')) # python will convert \n to os.linesep
    f.close() 

#-------------------------------
template = templateEnv.get_template(index_template)

temp = [m for m in os.listdir(path)]
mangas = []
for x in temp:
    try:
        if x.split(".")[1] == "html" and x.split(".")[0] != "index":
            mangas.append(x)
    except:
        pass
    
for manga in mangas:
    image_path = path + manga + "/" + chapter

print mangas
for manga in mangas:

    
    



