def getCreases(manga_path):
    global width, height, cover_index, aspect_ratio, crease_positions
    ignore = [".html","covers", "cover"]
    manga_path = path + manga
    volumes = [x for x in os.listdir(manga_path) if os.path.isdir(manga_path + "/" + x) and x not in ignore]
    for volume in volumes:
        volume = volumes[0]
        image = os.listdir(manga_path + "/" + volume)[0]
        image_network_path = manga_path + "/" + volume + "/" + image
        
        imageMagickID = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/identify.exe \"%s\"" % image_network_path
        info = subprocess.Popen(imageMagickID, shell=True, stdout=subprocess.PIPE).communicate()[0]
        info = info.split(" ")
        orig_width, orig_height = [int(s) for s in info[2].split("x")]        
        aspect_ratio = float(orig_width)/float(orig_height)
        manga_index, cover_index = getAR(aspect_ratio)

        out_path = r"d:\output.jpg"
       
        flag = "-resize 175000@"
        imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (image_network_path, flag, out_path)            
        subprocess.call(imageMagickCMD)
        
        imageMagickID = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/identify.exe \"%s\"" % out_path
        info = subprocess.Popen(imageMagickID, shell=True, stdout=subprocess.PIPE).communicate()[0]
        
        info = info.split(" ")
        width, height = [int(s) for s in info[2].split("x")]
        aspect_ratio = float(width)/float(height)
        
        manga_index, cover_index = getAR(aspect_ratio)
       
        im = cv2.imread(out_path)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        
        edges = []
        edges.append(cv2.Canny(im,0,50)) # finds low contrast edges, good for finding creases and edges
        edges.append(cv2.Canny(im,200, 400)) #finds highest contrast edges, good for finding empty space
        
        crease_positions = findCreasePositions(edges[0]) #high probability this is good
        valley_positions = findValleyPositions(edges[1]) # should return (start, end)
        crease_final = guessCreaseFromValleys(valley_positions)
        
        t = []
        for x in crease_final:
            try:
                t.append(x/float(width)*orig_width)
            except:
                pass
        crease_final = t
        
        if os.path.isdir(manga_path + "/covers/") == False:
            os.makedirs(manga_path + "/covers/")

        crop_width = int(crease_final[1]) - int(crease_final[0])
        crop_offset = int(crease_final[0])
        thumb_network_path = manga_path + "/covers/" + volume + ".jpg"
        flags = "-crop %sx%s+%s+0" % (crop_width, orig_height, crop_offset)
        createThumb(image_network_path, flags, thumb_network_path)
   
def getCreases(manga_path):
    global width, height, cover_index, aspect_ratio
    ignore = [".html","cover"]
    volumes = [x for x in os.listdir(manga_path) if os.path.isdir(manga_path + "/" + x)]
    images = []
    for volume in volumes[:4]:
        image = os.listdir(manga_path + "/" + volume)[0]
        images.append(manga_path + "/" + volume + "/" + image)
    crease_all = []
    for image in images:
        out_path = r"d:\output.jpg"
        imageMagickID = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/identify.exe \"%s\"" % image
        info = subprocess.Popen(imageMagickID, shell=True, stdout=subprocess.PIPE).communicate()[0]
        info = info.split(" ")
        orig_width, orig_height = [int(s) for s in info[2].split("x")]
        
        flag = "-resize 175000@"
        imageMagickCMD = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/convert.exe \"%s\" %s \"%s\"" % (image, flag, out_path)            
        subprocess.call(imageMagickCMD)
        
        imageMagickID = "//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/identify.exe \"%s\"" % out_path
        info = subprocess.Popen(imageMagickID, shell=True, stdout=subprocess.PIPE).communicate()[0]
        
        info = info.split(" ")
        width, height = [int(s) for s in info[2].split("x")]
        aspect_ratio = float(width)/float(height)
        
        manga_index, cover_index = getAR(aspect_ratio)
        #fi_min, fi_max, f_min, f_max, b_min, b_max, bi_min, bi_max = creaseMinMaxRange(cover_index)
        
        im = cv2.imread(out_path)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY )
        
        edges = []
        edges.append(cv2.Canny(im,0,50)) # finds low contrast edges, good for finding creases and edges
        edges.append(cv2.Canny(im,200, 400)) #finds highest contrast edges, good for finding empty space
        
        global crease_positions
        crease_positions = findCreasePositions(edges[0]) #high probability this is good
        valley_positions = findValleyPositions(edges[1]) # should return (start, end)
        crease_final = guessCreaseFromValleys(valley_positions)
        crease_all.append(crease_final)
    
    crease_all = np.array(crease_all)
    crease_all = np.swapaxes(crease_all, 0, 1)
    
    temp = []
    for z in range(0, len(crease_all)):
        nandsum = 0
        count = 0
        for x in crease_all[z]:
            if x is not None:
                nandsum += x
                count += 1
        try:
            temp.append(int(nandsum/count/float(width)*orig_width))
        except:
            temp.append(None)
    
    # crease_final expressed in percentages
    crease_final = temp
    return crease_final, orig_width, orig_height