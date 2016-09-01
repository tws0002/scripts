var current = app.activeDocument;
var currentName = current.name;
var currentPath = current.path;
var current_bits = current.bitsPerChannel;

newFile = File(currentPath + "/" + currentName);

current.close();

var doc1 = open(newFile);

var curLayers = doc1.layers;



for (i = 0; i < curLayers.length; i++) {
    activeDocument = doc1;
    layerName = curLayers[i].name;
    $.writeln(curLayers[i].name);
    $.writeln(curLayers[i].bounds);

    curMinX = app.activeDocument.activeLayer.bounds[0].value;
    curMinY = app.activeDocument.activeLayer.bounds[1].value;
    curMaxX = app.activeDocument.activeLayer.bounds[2].value;
    curMaxY = app.activeDocument.activeLayer.bounds[3].value;    
    curWidth = curMaxX - curMinX;
    curHeight = curMaxY - curMinY;

    $.writeln(curWidth);
    $.writeln(curHeight);

    curLayers.getByName(layerName).copy(false);
    $.sleep(500);
    app.documents.add(curWidth, curHeight, 72, layerName, NewDocumentMode.RGB,DocumentFill.TRANSPARENT,1,current_bits);
    app.activeDocument.paste();

}
/*current.selection.selectAll();
current.selection.copy(true);
app.documents.add(img_w, img_h, 72, 'copied', NewDocumentMode.RGB,DocumentFill.WHITE,1,current_bits);
app.activeDocument.paste();
app.activeDocument.bitsPerChannel = BitsPerChannelType.EIGHT;
app.activeDocument.resizeImage(final_w);
app.activeDocument.selection.selectAll();

$.writeln(current.layers.length);*/

