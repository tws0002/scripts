function deleteBG(){
    for(var i=0;i<activeDocument.artLayers.length;i++){
        if(activeDocument.artLayers[i].name == 'Background'){
            activeDocument.artLayers[i].allLocked = false;
                    activeDocument.artLayers[i].remove();
            }
        }
    }

   var elementPath = "/";
var currentFolder;
var allFolder;
var count = 0;
var folderList = [];
//var inputFolder = "~/Documents/ps"
var inputFolder = Folder.selectDialog("Select a folder of documents to process");
var data = "";

function allLayers(obj){
    var i,j;
    var layersLength ;
    var elemendData;

    //skip loop if its artlayer
    if(obj.typename == 'ArtLayer'){
        layersLength = 0;
        }
    else {
        layersLength = obj.layers.length;
        }
    
    for(j=0; j<layersLength;j++){
        count++;
        if(obj.layers[j].visible == true ){     
            if(obj.layers[j].typename == 'ArtLayer'){
                currentFilename = obj.layers[j].name;
                boundary = exportLayer(obj.layers[j], folderList);
                elementData = folderList.join("/") + "," + boundary[0]+ "," + boundary[1] + "," + boundary[2] + "," + boundary[3] + "," + boundary[4] + "," + boundary[5] + "" + boundary[6] + "|linebreak|";
                data = data + elementData;                
                }
            else{
                currentFolder = obj.layers[j].name;        
                folderList.push(obj.layers[j].name);
                }
            }

        allLayers(obj.layers[j]);
        count--;
        if(folderList.length > count){
            folderList.pop(0);
            }
        }
    }

function exportLayer(layer, layerPath){
    var filename = layer.name;
    filename= filename.replace(/[|&;$%@"<>()+,]/g, "");
    var folderPath = layerPath.join("/");
    var curMinX = layer.bounds[0].value;
    var curMinY = layer.bounds[1].value;
    var curMaxX = layer.bounds[2].value;
    var curMaxY = layer.bounds[3].value;
    var curWidth = curMaxX - curMinX;
    var curHeight = curMaxY - curMinY;
    var current_bits = activeDocument.bitsPerChannel;
    var savePath = inputFolder + "/" + folderPath + "/" +  filename + ".png";
    
    layer.copy(false);
    if(curWidth % 2 != 0){
        curWidth = curWidth + 1;
    }

    if(curHeight % 2 != 0){
        curHeight = curHeight + 1;
    }
    
    if(exportPNG == true){
        app.documents.add(curWidth, curHeight, 72, 'copied', NewDocumentMode.RGB,DocumentFill.TRANSPARENT,1,current_bits);
        app.activeDocument.paste();
        app.activeDocument.bitsPerChannel = BitsPerChannelType.EIGHT;
        deleteBG();
        
        var pngSaveOptions=new PNGSaveOptions;

        folderObj = new Folder(inputFolder + "/" + folderPath);
        folderObj.create(inputFolder + "/" + folderPath);
        app.activeDocument.saveAs(File(savePath), pngSaveOptions, false);
        app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);
    }
    return [filename, curMinX, curMinY, curMaxX, curMaxY, curWidth, curHeight]
}

function td(inner){
    return "<td>" + inner + "</td>"
}    

function image(src){
    return "<img src=\'" + src + "\'/>"
}
var CR = String.fromCharCode(13);
var rows;
var table;
var csvout;
var htmlPath;
var csvPath;
var exportPNG;

function exportCoordinates(option){
    exportPNG = option;
    allLayers(app.activeDocument);

    table = "\ufeff" + "<table><tr><td>資料夾</td><td>檔名</td><td>X</td><td>Y</td><td>圖寬</td><td>圖高</td><td>圖片路徑</td></tr>";
    csvout = "\ufeff" + "資料夾, 檔名, X, Y, 圖寬, 圖高, 圖片路徑" + CR;

    rows = data.split("|linebreak|");
    rows.pop();
    for (var i = 0; i < rows.length; i++) {
        cols = rows[i].split(",");
        folderPath = cols[0];
        filename = cols[1];
        curX = cols[2];
        curY = cols[3];
        width = cols[4];
        height = cols[5];
        
         imagePath = "./" + folderPath + "/" + filename + ".png";
         fullImagePath = inputFolder + "/" + folderPath + "/" + filename + ".png";

         imageHtml = image(imagePath);
         tableRow = "<tr>" + td(filename) + td(folderPath) + td(curX) + td(curY) + td(width) + td(height) + td(imageHtml) + "</tr>";
         table = table + tableRow;

         csvRow = filename + "," + folderPath + "," + curX + "," + curY + "," + width + "," + height + "," + fullImagePath;
         csvout = csvout + csvRow + CR;
    }
     table = table + "</table>"
     htmlPath = inputFolder + "/index.html";
     htmlFile = new File(htmlPath);
     htmlFile.encoding = "UTF8";
     htmlFile.open("e", "TEXT", "????");
     htmlFile.writeln(table);
     htmlFile.close();
     $.writeln(table);

     csvPath = inputFolder + "/output.csv";
    csvFile = new File(csvPath);
    csvFile.encoding = "UTF8";
    csvFile.open("e", "TEXT", "????");
    csvFile.writeln(csvout);
    csvFile.close();
}

//exportCoordinates()