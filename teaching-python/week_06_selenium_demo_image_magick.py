import os
import subprocess
import csv
import re

os.chdir("c:/")

path = r"f:/cover"
ignore_dir = ["css", "templates", "images", "cover", "Thumbs.db", "desktop.ini"]
mangas = [m for m in os.listdir(path) if m not in ignore_dir if os.path.isdir(os.path.join(path,m))]
#mangas = mangas[0:]
with open(r"f:/cover_data1.csv", "w") as cover_data:
    data_writer = csv.writer(cover_data, delimiter=',', lineterminator='\n')
    #current = cover_data.readlines()
    #endline = len(current)
    #last_manga = current[endline - 1].split(",")[0]
    #print "last manga in db was " + last_manga
    #i = mangas.index(last_manga) - 1
    #mangas = mangas[i:]
    for manga in mangas:
        print manga
        manga_path = path + "/" + manga
        covers = os.listdir(manga_path)
        for cover in covers:
            cover_path = manga_path + "/" + cover
            volume = cover.split(".")[0]
            imageMagickID = r"//Art-1405260002/d/assets/scripts/ImageMagick-6.9.0-6/identify.exe %s" % cover_path
            info = subprocess.Popen(imageMagickID, shell=True, stdout=subprocess.PIPE).communicate()[0]
            info = info.split(" ")
            orig_width, orig_height = [int(s) for s in info[2].split("x")]
            data_writer.writerow([manga, volume, orig_width, orig_height])