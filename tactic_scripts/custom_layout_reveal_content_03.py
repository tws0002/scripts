import datetime
from dateutil import parser
from operator import itemgetter
import os

main_url = []
time = []
version = []
name = []
uploader = []
process = []
name_chn = []
game_chn = []
iscurrent = []
process_count = []
snapshot_type = []
time1 = []
extension = []
test = []
labels = []
new_labels = []
poster_url = []

exp = "@GET(simpleslot/completion.description)"
labels = server.eval(exp)
for label in labels:
    new_labels.append(label)

exp = "@SOBJECT(simpleslot/plan['id','2'])"
temp = server.eval(exp)
game = temp[0].get('name')
image_display = temp[0].get('login')
video_display = temp[0].get('keywords')

#game = "circus"
filetype = "main"

#get the files
exp = "@SOBJECT(simpleslot/game['name','" + game + "'].simpleslot/3d.sthpw/snapshot.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
threedfiles = server.eval(exp)
items = threedfiles

if len(threedfiles) != 0: #if theres something in 3d, then there's nothing in asset or shot, proceed to 2d
    exp = "@SOBJECT(simpleslot/game['name','" + game + "'].simpleslot/package.sthpw/task.sthpw/snapshot.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
    packagefiles = server.eval(exp)
    items = items + packagefiles
else:
    exp = "@SOBJECT(simpleslot/game['name','" + game + "'].simpleslot/assets.sthpw/snapshot.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
    assetfiles = server.eval(exp)
    items = items + assetfiles

    if len(temp) != 0: #if theres somthing in assets, check shot
        exp = "@SOBJECT(simpleslot/game['name','" + game + "'].simpleslot/shot.sthpw/snapshot.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
        shotfiles = server.eval(exp)
        items = items + shotfiles
        if len(temp) != 0: #if theres something in shot, check 2d
            exp = "@SOBJECT(simpleslot/game['name','" + game + "'].simpleslot/package.sthpw/snapshot.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
            packagefiles = server.eval(exp)
            items = items + packagefiles


VIDEO_EXT = ['mp4','webm','swf']
CONVERT_VIDEO_EXT = ['mov','wmv','mpg','mpeg','m1v','m2v','mp2','mpa','mpe','wma','asf','asx','avi','wax','wm','wvx','ogg', 'mkv','m4v','mxf','f4v']
IMAGE_EXT = ['jpeg','jpg','png','tif','tiff','gif','dds']


display_ext = []

#display_ext gets input from UI on whether to display only images
if image_display == "1" and video_display == "0":
    display_ext = IMAGE_EXT
if image_display == "0" and video_display == "1":
    display_ext = VIDEO_EXT
if image_display == "1" and video_display == "1":
    display_ext = VIDEO_EXT + IMAGE_EXT
if image_display == "0" and video_display == "0":
    display_ext = []

display_ext = VIDEO_EXT + IMAGE_EXT
snapshot_type = []
for item in items:
    #item = items[0] #_____________rememder to redact this_____________________________________________________
    filename = item.get("file_name")
    search_type = item.get("search_type")

    name_ext = os.path.splitext(filename)
    ext = name_ext[1]
    ext = ext.lstrip(".")
    ext = ext.lower()

    if ext in display_ext:
        extension.append(ext)
        relative_dir = item.get("relative_dir")
        timestamp = item.get("timestamp")
        timestamp = parser.parse(timestamp)


        snapshot_code = item.get('snapshot_code')


        exp = "@SOBJECT(sthpw/file['snapshot_code','" + snapshot_code + "'].sthpw/snapshot)"
        temp = server.eval(exp)
        version.append(temp[0].get('version'))
        iscurrent.append(temp[0].get('is_current'))
        uploader.append(temp[0].get('login'))
        process.append(temp[0].get('process'))

        if ext in VIDEO_EXT:
            snapshot_type.append("sequence")
        else:
            snapshot_type.append(temp[0].get('snapshot_type'))


        exp = "@SOBJECT(sthpw/file['snapshot_code','" + snapshot_code + "']['type','main'].parent.parent)"
        temp = server.eval(exp)
        name.append(temp[0].get('name'))
        name_chn.append(temp[0].get('description'))
        std_search_types = ['simpleslot/3d?project=simpleslot','simpleslot/assets?project=simpleslot','simpleslot/shot?project=simpleslot','simpleslot/package?project=simpleslot']

        #snapshot parents could be sthpw/task or in std_search_types
        if search_type in std_search_types:
            exp = "@GET(sthpw/file['snapshot_code','" + snapshot_code + "']['type','main'].parent.parent.parent.name_chn)"
            game_chn = server.eval(exp)
        elif search_type == "sthpw/task":
            exp = "@GET(sthpw/file['snapshot_code','" + snapshot_code + "']['type','main'].parent.parent.parent.parent.name_chn)"
            game_chn = server.eval(exp)

        if ext in IMAGE_EXT:
            #filename = str(name_ext[0].encode("utf-8").replace("_publish","_icon_publish")) + ".png"
            filename = str(name_ext[0].encode("utf-8")+ ".jpg")
            temp = (str(relative_dir.encode("utf-8")) + "/" + filename)
            if os.path.isfile(temp):
                pass
            else:
                temp.replace(".jpg",".png")
            temp1 = ""
        else:
            temp = (str(relative_dir.encode("utf-8")) + "/" + str(filename.encode("utf-8")))
            temp1 = (str(relative_dir.encode("utf-8")) + "/" + str(name_ext[0].encode("utf-8")) + ".jpg")
        main_url.append(temp)
        poster_url.append(temp1)

        #time.append(timestamp)
        time.append("%s-%s-%s" % (timestamp.year, timestamp.month, timestamp.day))
        time1.append(timestamp)


list = zip(main_url,version, time, name_chn, uploader, process, name, iscurrent,snapshot_type,time1,extension, poster_url)
processes = ["final","layout","lighting","animation","rigging","texture","model","concept","rough","publish"]

name_list = []

for x in list:
    name_list.append(x[6])

def getName(item):
    return item[6]

def getVersion(item):
    return item[1]

def getTime(item):
    return item[2]

def getProcess(item):
    return item[5]

def getTimeStamp(item):
    return item[9]

def uniquelist(seq):
    checked = []
    for e in seq:
        if e not in checked:
            checked.append(e)
    return checked

#list = sorted(list,key=getTime, reverse=True)
#list = sorted(list,key=getVersion,reverse=True)
list = sorted(list,key=getTimeStamp,reverse=True)
new_list = []


for process in processes:
    for item in list:
        if item[5] == process:
            new_list.append(item)


#new_list = sorted(new_list, key=getName)

name_list = uniquelist(name_list)



images = []

images.append("<section>%s" % (game_chn[0]))
images.append("%s</section>\n\n" % (game))

count = 0

for name in name_list:
    images.append("<section>\n")
    for x in new_list:
        if x[6] == name:
            if x[8] == "sequence":
                images.append("    <section>\n")
                images.append("        <video width='800' height='448' controls loop autoplay><source type='video/webm' src='/assets/%s'></video>\n" % (x[0].decode("utf-8")))
            else:
                images.append("    <section>\n")
                images.append("        <img src = '/assets/%s'/>\n" % (x[0].decode("utf-8")))
                images.append("        <div class='close'>\n")
                images.append("            <table>\n")
                images.append("                <tr style='height: 15px;'>\n")
                images.append("                    <td id='game-data'>%s</td>\n" % new_labels[0])
                images.append("                    <td id='item-data'>%s</td>\n" % new_labels[1])
                images.append("                    <td id='process-data'>%s</td>\n" % new_labels[2])
                images.append("                    <td id='versioning-data'>%s</td>\n" % new_labels[3])
                images.append("                    <td id='author-data'>%s</td>\n" % new_labels[4])
                images.append("                    <td id='date-data'>%s</td>\n" % new_labels[5])
                images.append("                    <td id='close-data'>%s</td>\n" % new_labels[6])
                images.append("                </tr>\n")
                images.append("                <tr>\n")
                images.append("                    <td id='game'>%s</td>\n" % (game_chn[0]))
                images.append("                    <td id='item'>%s</td>\n" % (x[3]))
                images.append("                    <td id='process'>%s</td>\n" % (x[5]))
                images.append("                    <td id='versioning'>%s</td>\n" % (x[1]))
                images.append("                    <td id='author'>%s</td>\n" % (x[4]))
                images.append("                    <td id='date'>%s</td>\n" % (x[2]))
                images.append("                    <td id='close'></td>\n")
                images.append("               </tr>\n")
                images.append("            </table>\n")
                images.append("        </div>\n")
            images.append("    </section>\n")
    images.append("</section>\n")

    count = count + 1


images = "".join(images)

