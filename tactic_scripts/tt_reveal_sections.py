import time
import datetime
from dateutil import parser
import sys
import socket
sys.path.append("//Art-1405260002/d/assets/client")

from tactic_client_lib import TacticServerStub
server = TacticServerStub.get()
tactic_server_ip = socket.gethostbyname("vg.com")
server.set_server(tactic_server_ip)
server.set_project("simpleslot")
ticket = server.get_ticket("julio", "1234")
server.set_ticket(ticket)


import datetime
from dateutil import parser
from operator import itemgetter
import os

game = code[0]
game_chn = code[1]
background = code[2]

game = "the_last_samurai"

title = ""
for x in game.lower().split("_"):
    title = title + " " + x.capitalize()

title = title[1:]


filetype = "main"
items = ""
exp = "@SOBJECT(simpleslot/game['name','" + game + "'].simpleslot/3d.sthpw/task.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
threedfiles = server.eval(exp)
items = threedfiles

if len(threedfiles) != 0: #if theres something in 3d, then there's nothing in asset or shot, proceed to 2d
    exp = "@SOBJECT(simpleslot/game['name','" + game + "'].simpleslot/package.sthpw/task.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
    packagefiles = server.eval(exp)
    items = items + packagefiles
else:
    exp = "@SOBJECT(simpleslot/game['name','" + game + "'].simpleslot/assets.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
    assetfiles = server.eval(exp)
    items = items + assetfiles

    if len(assetfiles) != 0: #if theres somthing in assets, check shot
        exp = "@SOBJECT(simpleslot/game['name','" + game + "'].simpleslot/shot.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
        shotfiles = server.eval(exp)
        items = items + shotfiles
        if len(shotfiles) != 0: #if theres something in shot, check 2d
            exp = "@SOBJECT(simpleslot/game['name','" + game + "'].simpleslot/package.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
            packagefiles = server.eval(exp)
            items = items + packagefiles

VIDEO_EXT = ['mp4','webm','swf']
CONVERT_VIDEO_EXT = ['mov','wmv','mpg','mpeg','m1v','m2v','mp2','mpa','mpe','wma','asf','asx','avi','wax','wm','wvx','ogg', 'mkv','m4v','mxf','f4v']
IMAGE_EXT = ['jpeg','jpg','png','tif','tiff','gif','dds']


display_ext = []

image_display = "1" #_____________rememder to redact this_____________________________________________________
video_display = "1" #_____________rememder to redact this_____________________________________________________
#display_ext gets input from UI on whether to display only images
if image_display == "1" and video_display == "0":
    display_ext = IMAGE_EXT
if image_display == "0" and video_display == "1":
    display_ext = VIDEO_EXT
if image_display == "1" and video_display == "1":
    display_ext = VIDEO_EXT + IMAGE_EXT
if image_display == "0" and video_display == "0":
    display_ext = []

snapshot_type = []
sections = []
for item in items:
    full_filename = item.get("file_name")
    search_type = item.get("search_type")
    filename = full_filename.split(".")[0]
    ext = full_filename.split(".")[1].lower()
    
    #display images or videos, both, or none    
    if ext in display_ext:
        relative_dir = item.get("relative_dir")
        timestamp = item.get("timestamp")
        timestamp = parser.parse(timestamp)
        snapshot_code = item.get('snapshot_code')

        #go up one level to snapshot
        exp = "@SOBJECT(sthpw/file['snapshot_code','" + snapshot_code + "'].sthpw/snapshot)"
        snapshot = server.eval(exp)[0]
        
        version = snapshot.get('version')
        iscurrent = snapshot.get('is_current')
        login = snapshot.get('login')
        process = snapshot.get('process')

        if ext in VIDEO_EXT:
            snapshot_type = "sequence"
        else:
            snapshot_type = snapshot.get('snapshot_type')

        #go up two level to the TASK level
        exp = "@SOBJECT(sthpw/file['snapshot_code','" + snapshot_code + "']['type','main'].parent.parent)"
        task = server.eval(exp)[0]

        pipeline = task.get('process')

        exp = "@SOBJECT(sthpw/file['snapshot_code','" + snapshot_code + "']['type','main'].parent.parent.parent)"
        meta = server.eval(exp)[0]        
        try:        
            name = meta.get('name')
            print name
        except:
            pass
        if name == None:
            name = "package " + pipeline

        '''
        std_search_types = ['simpleslot/3d?project=simpleslot','simpleslot/assets?project=simpleslot','simpleslot/shot?project=simpleslot','simpleslot/package?project=simpleslot']

        #snapshot parents could be sthpw/task or in std_search_types
        #be very aware where the users are putting their files
        if search_type in std_search_types:
            exp = "@GET(sthpw/file['snapshot_code','" + snapshot_code + "']['type','main'].parent.parent.parent.name_chn)"
            game_chn = server.eval(exp)
        elif search_type == "sthpw/task":
            exp = "@GET(sthpw/file['snapshot_code','" + snapshot_code + "']['type','main'].parent.parent.parent.parent.name_chn)"
            game_chn = server.eval(exp)
        '''
        
        #building thumbnails? 
        if ext in IMAGE_EXT:
            #filename = str(name_ext[0].encode("utf-8").replace("_publish","_icon_publish")) + ".png"
            #temp = (str(relative_dir.encode("utf-8")) + "/" + filename)
            main_url  = (str(relative_dir.encode("utf-8")) + "/" + filename + "." + ext)
            poster_url = ""
        else:
            main_url = (str(relative_dir.encode("utf-8")) + "/" + str(filename.encode("utf-8")) + "." + ext)
            poster_url = (str(relative_dir.encode("utf-8")) + "/" + str(filename.encode("utf-8")) + ".jpg")

        time = ("%s-%s-%s" % (timestamp.year, timestamp.month, timestamp.day))
        sections.append([main_url,version, time, name_chn, login, process, name, iscurrent,snapshot_type,time,ext, poster_url])

processes = ["final","layout","lighting","animation","rigging","texture","model","concept","rough","publish"]

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

sections = sorted(sections,key=getTimeStamp,reverse=True)

name_list = []
for x in sections:
    name_list.append(x[6])
name_list = uniquelist(name_list)


images = []
#images.append("     <section data-background='%s'><h2>%s</h2>\n" % (str(background.encode('utf-8')), str(game_chn.encode('utf-8'))))
#images.append("     <h3>%s</h3></section>\n" % title)

images.append("     <section data-background='%s'>" % str(background.encode('utf-8')))
images.append("     <div id='search-bg' style=\"background-image: url('%s')\"></div>" % (str(background.encode('utf-8'))))
images.append("		<div id='search'>")
images.append("		<h2 class='title'>%s</h2>\n" % str(game_chn.encode('utf-8')))
images.append("     <h3>%s</h3>\n" % title)	
images.append("	</div></section>")
for name in name_list:
    images.append("<section class='section_top'>\n")     #per item section
    images.append("     <section><h2>%s</h2></section>\n" % str(name.encode('utf-8')))
    for x in sections:
        if x[6] == name:
            if x[8] == "sequence":
                if x[10] == "swf":
                    images.append("     <section><div id='section_correction'><object class='shockwave' data='/assets/%s'></object></div></section>\n" % (str(x[0].encode("utf-8"))))
                else:
                    images.append("     <section><div id='section_correction'><video controls loop autoplay><source type='video/%s' data-src='/assets/%s'></video></div></section>\n" % (str(x[10]), str(x[0].encode("utf-8"))))
            else:
                images.append("     <section><div id='section_correction'><img data-src = '/assets/%s' /></div></section>\n" % (str(x[0].encode('utf-8'))))
    '''
            
            images.append("<div class='close'><table><tr style='height: 15px;'><td id='game-data'>%s</td><td id='item-data'>%s</td><td id='process-data'>%s</td><td id='versioning-data'>%s</td><td id='author-data'>%s</td><td id='date-data'>%s</td><td id='close-data'>%s</td></tr><tr>" % (new_labels[0],new_labels[1],new_labels[2],new_labels[3],new_labels[4],new_labels[5],new_labels[6]))
            images.append("<td id='game'>%s</td>\n" % (game_chn[0]))
            images.append("<td id='item'>%s</td>\n" % (x[3]))
            images.append("<td id='process'>%s</td>\n" % (x[5]))
            images.append("<td id='versioning'>%s</td>\n" % (x[1]))
            images.append("<td id='author'>%s</td>\n" % (x[4]))
            images.append("<td id='date'>%s</td>\n" % (x[2]))
            images.append("<td id='close'></td>\n")
            images.append("</tr></tbody></table></div>")
            
            images.append("</section>\n")
    '''
    images.append("</section>\n\n")    

images = "".join(images)
return images