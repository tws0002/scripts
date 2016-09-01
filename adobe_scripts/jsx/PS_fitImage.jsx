var bpfile = File('//art-1405260002/D/assets/scripts/adobe_scripts/plate/backplate.psd');
var current = app.activeDocument;
var current_name = current.name;
var current_bits = current.bitsPerChannel;

app.preferences.rulerUnits = Units.PIXELS
app.preferences.typeUnits = TypeUnits.PIXELS
app.displayDialogs = DialogModes.NO

doc_w = 2000;
doc_h = 1042;

img_w = current.width;
img_h = current.height;

var ratio;
if((img_w/img_h) < (doc_w/doc_h)) {
    ratio = doc_h / img_h;    
}
else if((img_w/img_h) > (doc_w/doc_h)) {
    ratio = doc_w / img_w;
}

offset_h = img_h/2 - doc_h/2;
if(img_w < doc_w) {
    offset_w = 0;
}
else {
    offset_w = img_w/2 - doc_w/2;
}

final_w = img_w * ratio;
final_h = img_h * ratio;

$.writeln(final_w);
$.writeln(final_h);

current.selection.selectAll();
current.selection.copy(true);
app.documents.add(img_w, img_h, 72, 'copied', NewDocumentMode.RGB,DocumentFill.WHITE,1,current_bits);
app.activeDocument.paste();
app.activeDocument.bitsPerChannel = BitsPerChannelType.EIGHT;
app.activeDocument.resizeImage(final_w);
app.activeDocument.selection.selectAll();
if(app.activeDocument.activeLayer.isBackgroundLayer) app.activeDocument.activeLayer.isBackgroundLayer = false;  
if(app.activeDocument.activeLayer.allLocked) app.activeDocument.activeLayer.allLocked = false; 
app.activeDocument.selection.copy(true);
app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);

app.open(bpfile);
app.activeDocument.paste();
app.activeDocument.artLayers[0].translate(0,-41);
app.activeDocument.flatten();
if(app.activeDocument.activeLayer.isBackgroundLayer) app.activeDocument.activeLayer.isBackgroundLayer = false;  
if(app.activeDocument.activeLayer.allLocked) app.activeDocument.activeLayer.allLocked = false; 
//app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);


