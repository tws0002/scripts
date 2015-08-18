var server = TacticServerStub.get();

function isInArray(value, array) {
  return array.indexOf(value) > -1;
}

function unique(arr) {
    var u = {}, a = [];
    for(var i = 0, l = arr.length; i < l; ++i){
        if(!u.hasOwnProperty(arr[i])) {
            a.push(arr[i]);
            u[arr[i]] = 1;
        }
    }
    return a;
}

filetype = "main"
game = "burst_fruit_plate"
exp = "@SOBJECT(simpleslot/game['name','" + game + "'].simpleslot/3d.sthpw/snapshot.sthpw/file['file_name','not like','']['type','" + filetype + "'])";
files = server.eval(exp);

if(files.length != 0) {
    exp = "@SOBJECT(simpleslot/game['name','" + game + "'].simpleslot/package.sthpw/task.sthpw/snapshot.sthpw/file['file_name','not like','']['type','" + filetype + "'])";
    packagefiles = server.eval(exp);
    files = files.concat(packagefiles);
}

else {
    exp = "@SOBJECT(simpleslot/game['name','" + game + "'].simpleslot/assets.sthpw/snapshot.sthpw/file['file_name','not like','']['type','" + filetype + "'])";
    assetfiles = server.eval(exp);
    files = files.concat(assetfiles);
    if(assetfiles.length != 0) {
        exp = "@SOBJECT(simpleslot/game['name','" + game + "'].simpleslot/shot.sthpw/snapshot.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
        shotfiles = server.eval(exp);
        files = files.concat(shotfiles);
        if(shotfiles.legnth != 0) {
            exp = "@SOBJECT(simpleslot/game['name','" + game + "'].simpleslot/package.sthpw/snapshot.sthpw/file['file_name','not like','']['type','" + filetype + "'])"
            packagefiles = server.eval(exp);
            files = files.concat(packagefiles);
        }
    }
}

VIDEO_EXT = ['mp4','webm','swf'];
CONVERT_VIDEO_EXT = ['mov','wmv','mpg','mpeg','m1v','m2v','mp2','mpa','mpe','wma','asf','asx','avi','wax','wm','wvx','ogg', 'mkv','m4v','mxf','f4v'];
IMAGE_EXT = ['jpeg','jpg','png','tif','tiff','gif','dds'];

image_display = "1";
video_display = "1";

if(image_display == "1" && video_display == "0") {
    display_ext = IMAGE_EXT;
}
if(image_display == "0" && video_display == "1") {
    display_ext = VIDEO_EXT;
}
if(image_display == "1" && video_display == "1") {
    display_ext = VIDEO_EXT.concat(IMAGE_EXT);
}
if(image_display == "0" && video_display == "0") {
    display_ext = []
}

snapshot_type = [];
sections = [];

for(i=0; i < files.length; i++) {
    full_filename = files[i].file_name;
    search_type = files[i].search_type;
    filename = full_filename.split(".")[0];
    ext = full_filename.split(".")[1].toLowerCase();
    if(isInArray(ext, display_ext)) {
        relative_dir = files[i].relative_dir;
        timestamp = files[i].timestamp;
        snapshot_code = files[i].snapshot_code;

        exp = "@SOBJECT(sthpw/file['snapshot_code','" + snapshot_code + "'].sthpw/snapshot)";
        snapshot = server.eval(exp)[0];
        
        version = snapshot.version;
        iscurrent = snapshot.is_current;
        login = snapshot.login;
        process = snapshot.process;
        if(isInArray(ext, VIDEO_EXT)){
            snapshot_type = "sequence";
        }
        else {
            snapshot_type = snapshot.snapshot_type;
        }
        
        exp = "@SOBJECT(sthpw/file['snapshot_code','" + snapshot_code + "']['type','main'].parent.parent)";
        task = server.eval(exp)[0];
        
        name = task.name;
        name_chn = task.description;

        std_search_types = ['simpleslot/3d?project=simpleslot','simpleslot/assets?project=simpleslot','simpleslot/shot?project=simpleslot','simpleslot/package?project=simpleslot']

        //chinese name can be ommited in new reveal main page, as its shown already
        /*if(isInArray(search_type, std_search_types)){
            exp = "@GET(sthpw/file['snapshot_code','" + snapshot_code + "']['type','main'].parent.parent.parent.name_chn)";
            game_chn = server.eval(exp);
        }
        else if(search_type == "sthpw/task") {
            exp = "@GET(sthpw/file['snapshot_code','" + snapshot_code + "']['type','main'].parent.parent.parent.parent.name_chn)";
            game_chn = server.eval(exp);
        }
        */

        if(isInArray(ext, IMAGE_EXT)){
            main_url  = (relative_dir + "/" + filename + ".jpg");
            poster_url = "";
        }
        else {
            main_url = (relative_dir + "/" + filename);
            poster_url = (relative_dir + "/" + filename + ".jpg");
        }

        time = timestamp.year + "-" + timestamp.month + "-" + timestamp.day;
        sections.push([main_url,version, time, name_chn, login, process, name, iscurrent,snapshot_type,time,ext, poster_url]);
    }
}

processes = ["final","layout","lighting","animation","rigging","texture","model","concept","rough","publish"];

name_list = [];

for(j=0; j < sections.length; j++){
    name_list.push(sections[j][6]);
}

console.log(name_list)