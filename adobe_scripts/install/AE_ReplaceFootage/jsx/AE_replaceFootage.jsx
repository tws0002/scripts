function replaceFootage(o) {
    targetName = o['targetName'];

    var folder = app.project.activeItem;
    var  folderCount = folder.numItems;

    var sourceName =  folder.name;
    //var targetName = o;
    var sourceItems = [];
    var re = new RegExp(sourceName,"g");

    for (i = 1; i < folderCount + 1; i++) {
        folderName = folder.item(i).name;
        if(folder.item(i).typeName == "Footage"){
            newPath = folder.item(i).file.path.replace(re, targetName) ;
            $.writeln(newPath);
            var targetFolder = new Folder(newPath);
            var targetFiles = targetFolder.getFiles();
            newName = folder.item(i).file.name.replace(re, targetName) ;
            var f = new File(newPath + "/" + newName);
            if(folderName.match(/[[]\d\d\d\d[-]\d\d\d\d[\]]/)){
                folder.item(i).replaceWithSequence(f, false);
            }
            else {
                folder.item(i).replace(f);
            }
        }
    };
    folder.name = targetName;      
}

