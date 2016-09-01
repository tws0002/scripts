
//$.writeln(app.activeDocument.selection.bounds);

//$.writeln(app.activeDocument.activeLayer.bounds);
function offsetLayer(obj){
    inputPosX = obj['inputPosX'];
    inputPosY = obj['inputPosY'];

    curMinX = app.activeDocument.activeLayer.bounds[0].value;
    curMinY = app.activeDocument.activeLayer.bounds[1].value;
    curMaxX = app.activeDocument.activeLayer.bounds[2].value;
    curMaxY = app.activeDocument.activeLayer.bounds[3].value;

    translateX = inputPosX - curMinX;
    translateY = inputPosY - curMinY;
    app.activeDocument.activeLayer.translate(translateX,translateY);
}

function resizeLayer(obj){
    inputSizeX = obj['inputSizeX'];
    inputSizeY = obj['inputSizeY'];
    lock = obj['lock'];
    dimension = obj['dimension'];

    curMinX = app.activeDocument.activeLayer.bounds[0].value;
    curMinY = app.activeDocument.activeLayer.bounds[1].value;
    curMaxX = app.activeDocument.activeLayer.bounds[2].value;
    curMaxY = app.activeDocument.activeLayer.bounds[3].value;

    curWidth = curMaxX - curMinX;
    curHeight = curMaxY - curMinY;
    if(lock == true){
        if(dimension == 'w'){
            ratio = curWidth / curHeight;
            resizeX = ((inputSizeX - curMinX) / curWidth) * 100;
            resizeY = resizeX;
        }
        else if(dimension == 'h'){
            resizeY = ((inputSizeY - curMinY) / curHeight) * 100;
            resizeX = resizeY;
        }
    }    
    else if(lock != true){
        resizeX = ((inputSizeX - curMinX) / curWidth) * 100;
        resizeY = ((inputSizeY - curMinY) / curHeight) * 100;
    }
 
    app.activeDocument.activeLayer.resize(resizeX, resizeY, AnchorPosition.TOPLEFT);
}

function getTransform() {    
    curMinX = app.activeDocument.activeLayer.bounds[0].value;
    curMinY = app.activeDocument.activeLayer.bounds[1].value;
    curMaxX = app.activeDocument.activeLayer.bounds[2].value;
    curMaxY = app.activeDocument.activeLayer.bounds[3].value;
    //curWidth = curMaxX - curMinX;
    //curHeight = curMaxY - curMinY;    
    return [curMinX, curMinY, curMaxX, curMaxY].join(",");
}