import os
import os.path
import subprocess

path = "//Art-1405260002/d/assets/manga/"

book = "wuxianzhuren"
book_chinese = "無限住人"
chapters = [d for d in os.listdir(path + book) if os.path.isdir(os.path.join(path + book, d))]
index_link = ("http://vg.com/assets/manga/%s.html") % book

#------------------------------------------pages

head = []
foot = []
head.append('<!doctype html><html lang=\"en\"><head>')
head.append('<meta charset=\"utf-8\"><meta http-equiv=\"cache-control\" content=\"max-age=0\" /><meta http-equiv=\"cache-control\" content=\"no-cache\"\n />')
head.append('<meta http-equiv=\"expires\" content=\"0\" /><meta http-equiv=\"expires\" content=\"Tue, 01 Jan 1980 1:00:00 GMT\" /><meta http-equiv=\"pragma\" content=\"no-cache\"\n />')
head.append('<link rel=\"stylesheet\" href=\"http://vg.com/assets/scripts/sly/css/horizontal.css?version=1\">)
head.append('<script src=\"http://vg.com/assets/scripts/jquery-2.1.1.min.js\"></script>\n')
head.append('<link rel=\"stylesheet\" href=\"../../scripts/font-awesome-4.1.0/css/font-awesome.min.css\">\n')
head.append('</head>\n\n')

head.append('<body class=\"bg\" style=\"background-image: url(\"http://vg.com/assets/manga/big-video-background.jpg\");\">')
head.append('<div class=\"wrap\"><h2>%s<small> - %s</small></h2>' %s book_chinese, book_english)
head.append('<div class=\"scrollbar\"><div class=\"handle\" style=\"transform: translateZ(0px) translateX(114px); width: 190px;\">')
head.append('<div class=\"mousearea\"></div></div></div>')
head.append('<div class=\"frame\" id=\"basic\" style=\"overflow: hidden;\">')
head.append('<ul class=\"\" style=\"transform: translateZ(0px) translateX(-684px); width: 26840px;\">')


foot.append('</div></div><a href=\"%s\" class=\"cancel cancel_button fa fa-times fa-3x\"></a><script src=\"http://vg.com/assets/scripts/reveal/lib/js/head.min.js\"></script>' % index_link)
foot.append('<script src=\"http://vg.com/assets/scripts/reveal/js/reveal.js\"></script>')
foot.append('<script>Reveal.initialize({controls: true, progress: true, history: true, overview: true, center: true, transition: \"slide\", dependencies: [{ src: \"http://vg.com/assets/scripts/reveal/plugin/zoom-js/zoom.js\", async: true }]});')
foot.append('Reveal.configure({minScale: 1, maxScale: 5, slideNumber: true, mouseWheel: true, transitionSpeed: \"slow\", loop: \"false\", embedded: \"true\", viewDistance: 5, transition: \"fade\", backgroundTransition: \"default\"});</script></body></html>')
purple_bliss = "radial-gradient(ellipse at center, #0b8793 10%, #360033 90%)"
for chapter in chapters:
    image_path = path + "/" + book + "/" + chapter
    images = os.listdir(image_path)
    section = []
    for image in images:
        if image == "Thumbs.db" :
            pass
        elif "thumb" in image:
            pass
        else:
            final_path = "http://vg.com/assets/manga/" + book + "/" + chapter + "/" + image
            section.append("     <section data-background=\'%s\'><img data-src=\'%s\'></img></section>\n" % (purple_bliss, final_path))
    html = "".join(head) + "".join(section) + "".join(foot)
    

    f = open(path + "/" + book + "/" + chapter + ".html",'w')
    f.write(html) # python will convert \n to os.linesep
    f.close() 
    



#------------------------------------------books
html = []
html.append('<!doctype html><html lang=\"en\"><head>')
html.append('<meta charset=\"utf-8\"><meta http-equiv=\"cache-control\" content=\"max-age=0\" /><meta http-equiv=\"cache-control\" content=\"no-cache\" />')
html.append('<meta http-equiv=\"expires\" content=\"0\" /><meta http-equiv=\"expires\" content=\"Tue, 01 Jan 1980 1:00:00 GMT\" /><meta http-equiv=\"pragma\" content=\"no-cache\" />')

html.append('<link id=\"pagestyle\" rel=\"stylesheet\" href=\"http://vg.com/assets/manga/main.css\"></head><body class=\"revealmp\">')

head.append('<body class=\"bg\" style=\"background-image: url(\"http://vg.com/assets/manga/big-video-background.jpg\");\">')
head.append('<div class=\"wrap\"><h2>%s<small> - %s</small></h2>' %s book_chinese, book_english)
head.append('<div class=\"scrollbar\"><div class=\"handle\" style=\"transform: translateZ(0px) translateX(114px); width: 190px;\">')
head.append('<div class=\"mousearea\"></div></div></div>')
head.append('<div class=\"frame\" id=\"basic\" style=\"overflow: hidden;\">')
head.append('<ul class=\"\" style=\"transform: translateZ(0px) translateX(-684px); width: 26840px;\">')


html.append("<span><h1>%s</h1></span>" % book_chinese)
html.append("<ul>")
for chapter in chapters:
    images_path = path + "/" + book + "/" + chapter
    images = os.listdir(images_path)
    image = [x for x in images if x != 'Thumbs.db' and x.split("-")[1][0:3] == '001' and "thumb" not in x][0]
    #image = [x for x in images if x != 'Thumbs.db' and x.split("_")[1][0:4] == '0000' and "thumb" not in x][0]


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
    
    thumb_web_path = "http://vg.com/assets/manga/" + book + "/" + chapter + "/" + image_name + "_thumb" + "." + image_ext
    html.append("<li>")
    chapter_link = ("http://vg.com/assets/manga/" + book + "/" + chapter + ".html")
    html.append("<a href='%s'><img class= 'loadReveal' src='%s'></img></a>" % (chapter_link, thumb_web_path))
    html.append("<h3 class='links'>%s</h3>" % chapter)
    html.append("<span>%s</span>" % "")
    html.append("</li>")
html.append("</ul>")
html.append("</body></html>")

html = "".join(html)   
f = open(path + "/" + book + ".html",'w')
f.write(html) # python will convert \n to os.linesep
f.close()  
print html

