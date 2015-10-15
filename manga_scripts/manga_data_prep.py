width, height, cover_index, aspect_ratio = 0
path = "//Art-1405260002/d/assets/manga/"

ignore_dir = ["css", "templates", "images", "cover", "Thumbs.db", "desktop.ini"]
mangas = [m for m in os.listdir(path) if m not in ignore_dir if os.path.isdir(os.path.join(path,m))]

mangas = mangas[5:]
for manga in mangas:
    manga_path = path + manga
    print manga
    volumes = [x for x in os.listdir(manga_path) if os.path.isdir(manga_path + "/" + x) and x not in ignore]
    for volume in volumes:
        image = os.listdir(manga_path + "/" + volume)[0]
        image_network_path = manga_path + "/" + volume + "/" + image
        resized_path = manga_path + "/covers/" + volume + ".jpg"
        if os.path.isdir(manga_path + "/covers/") == False:
            os.makedirs(manga_path + "/covers/")
                
        imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (image_network_path, flag, resized_path)            
        subprocess.call(imageMagickCMD)

        imageMagickID = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/identify.exe \"%s\"" % image_network_path
        info = subprocess.Popen(imageMagickID, shell=True, stdout=subprocess.PIPE).communicate()[0]
        info = info.split(" ")
        width, height = [int(s) for s in info[2].split("x")]        
        aspect_ratio = float(width)/float(height)
        manga_index, cover_index = getAR(aspect_ratio)
        
        data = manga, volume, width, height, aspect_ratio, cover_index



out_path = r"d:\output.jpg"
resized_path = r"d:\resized.jpg"

#this one to operate on
flag = "-resize x1000"
imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (image_network_path, flag, resized_path)            
subprocess.call(imageMagickCMD)

#this one analysis
flag = "-resize 350000@"
imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (resized_path, flag, out_path)            
subprocess.call(imageMagickCMD)

imageMagickID = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/identify.exe \"%s\"" % resized_path
info = subprocess.Popen(imageMagickID, shell=True, stdout=subprocess.PIPE).communicate()[0]
info = info.split(" ")
orig_width, orig_height = [int(s) for s in info[2].split("x")]


imageMagickID = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/identify.exe \"%s\"" % out_path
info = subprocess.Popen(imageMagickID, shell=True, stdout=subprocess.PIPE).communicate()[0]
info = info.split(" ")
width, height = [int(s) for s in info[2].split("x")]        
aspect_ratio = float(width)/float(height)
manga_index, cover_index = getAR(aspect_ratio)

im = cv2.imread(out_path)
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY )

edges = []
edges.append(cv2.Canny(im,0,50)) # finds low contrast edges, good for finding creases and edges
edges.append(cv2.Canny(im,200, 400)) #finds highest contrast edges, good for finding empty spacetCreases(manga_path)

crease_positions = findCreasePositions(edges[0]) #high probability this is good
valley_positions = findValleyPositions(edges[1]) # should return (start, end)
crease_final = guessCreaseFromValleys(valley_positions, crease_positions)

def f(x):
    if x != None:
        return x/float(width)*(orig_width) + (1/float(width)/orig_width)
    else:
        pass
    
crease_final_convert = map(f, crease_final)

low_edge = convert1D(edges[0])
high_edge = convert1D(edges[1])

plt.subplot(311)
plt.cla()
plt.tight_layout(pad=1.08, h_pad=None, w_pad=None, rect=None)
test = cv2.cvtColor(edges[0], cv2.COLOR_GRAY2RGB )
for x in range(0, len(crease_final)):
    if crease_final[x] == None:
        pass
    else:
        test[:,crease_final[x]] = [255,0,0]

plt.imshow(test, 'gray')
plt.subplot(312)
plt.imshow(edges[1], 'gray')

plt.subplot(313)
plt.cla()
plt.ylim([0,100])
plt.plot(high_edge)
plt.plot(low_edge)
plt.show()




