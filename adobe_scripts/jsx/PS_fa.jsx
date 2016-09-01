//Tim Down Stackoverflow
function hexToRgb(hex) {
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null;
}

function getBounds(curLayer){
    minX = curLayer.bounds[0].value;
    minY = curLayer.bounds[1].value;
    maxX = curLayer.bounds[2].value;
    maxY = curLayer.bounds[3].value;    
    width = maxX - minX;
    height = maxY - minY;
    return {
        minX: parseInt(minX),
        minY: parseInt(minY),
        maxX: parseInt(maxX),
        maxY: parseInt(maxY),
        width: parseInt(width),
        height: parseInt(height)
    }
}

function strokeFill(strokeColor, fillColor){
var idsetd = charIDToTypeID( "setd" );
    var desc187 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
        var ref138 = new ActionReference();
        var idPrpr = charIDToTypeID( "Prpr" );
        var idLefx = charIDToTypeID( "Lefx" );
        ref138.putProperty( idPrpr, idLefx );
        var idLyr = charIDToTypeID( "Lyr " );
        var idOrdn = charIDToTypeID( "Ordn" );
        var idTrgt = charIDToTypeID( "Trgt" );
        ref138.putEnumerated( idLyr, idOrdn, idTrgt );
    desc187.putReference( idnull, ref138 );
    var idT = charIDToTypeID( "T   " );
        var desc188 = new ActionDescriptor();
        var idScl = charIDToTypeID( "Scl " );
        var idPrc = charIDToTypeID( "#Prc" );
        desc188.putUnitDouble( idScl, idPrc, 100.000000 );
        var idSoFi = charIDToTypeID( "SoFi" );
            var desc189 = new ActionDescriptor();
            var idenab = charIDToTypeID( "enab" );
            desc189.putBoolean( idenab, true );
            var idpresent = stringIDToTypeID( "present" );
            desc189.putBoolean( idpresent, true );
            var idshowInDialog = stringIDToTypeID( "showInDialog" );
            desc189.putBoolean( idshowInDialog, true );
            var idMd = charIDToTypeID( "Md  " );
            var idBlnM = charIDToTypeID( "BlnM" );
            var idNrml = charIDToTypeID( "Nrml" );
            desc189.putEnumerated( idMd, idBlnM, idNrml );
            var idClr = charIDToTypeID( "Clr " );
                var desc190 = new ActionDescriptor();
                var idRd = charIDToTypeID( "Rd  " );
                desc190.putDouble( idRd, fillColor.r );
                var idGrn = charIDToTypeID( "Grn " );
                desc190.putDouble( idGrn, fillColor.g );
                var idBl = charIDToTypeID( "Bl  " );
                desc190.putDouble( idBl, fillColor.b );
            var idRGBC = charIDToTypeID( "RGBC" );
            desc189.putObject( idClr, idRGBC, desc190 );
            var idOpct = charIDToTypeID( "Opct" );
            var idPrc = charIDToTypeID( "#Prc" );
            desc189.putUnitDouble( idOpct, idPrc, 100.000000 );
        var idSoFi = charIDToTypeID( "SoFi" );
        desc188.putObject( idSoFi, idSoFi, desc189 );
        var idFrFX = charIDToTypeID( "FrFX" );
            var desc191 = new ActionDescriptor();
            var idenab = charIDToTypeID( "enab" );
            desc191.putBoolean( idenab, true );
            var idpresent = stringIDToTypeID( "present" );
            desc191.putBoolean( idpresent, true );
            var idshowInDialog = stringIDToTypeID( "showInDialog" );
            desc191.putBoolean( idshowInDialog, true );
            var idStyl = charIDToTypeID( "Styl" );
            var idFStl = charIDToTypeID( "FStl" );
            var idInsF = charIDToTypeID( "InsF" );
            desc191.putEnumerated( idStyl, idFStl, idInsF );
            var idPntT = charIDToTypeID( "PntT" );
            var idFrFl = charIDToTypeID( "FrFl" );
            var idSClr = charIDToTypeID( "SClr" );
            desc191.putEnumerated( idPntT, idFrFl, idSClr );
            var idMd = charIDToTypeID( "Md  " );
            var idBlnM = charIDToTypeID( "BlnM" );
            var idNrml = charIDToTypeID( "Nrml" );
            desc191.putEnumerated( idMd, idBlnM, idNrml );
            var idOpct = charIDToTypeID( "Opct" );
            var idPrc = charIDToTypeID( "#Prc" );
            desc191.putUnitDouble( idOpct, idPrc, 100.000000 );
            var idSz = charIDToTypeID( "Sz  " );
            var idPxl = charIDToTypeID( "#Pxl" );
            desc191.putUnitDouble( idSz, idPxl, 1.000000 );
            var idClr = charIDToTypeID( "Clr " );
                var desc192 = new ActionDescriptor();
                var idRd = charIDToTypeID( "Rd  " );
                desc192.putDouble( idRd, strokeColor.r );
                var idGrn = charIDToTypeID( "Grn " );
                desc192.putDouble( idGrn, strokeColor.g);
                var idBl = charIDToTypeID( "Bl  " );
                desc192.putDouble( idBl, strokeColor.b );
            var idRGBC = charIDToTypeID( "RGBC" );
            desc191.putObject( idClr, idRGBC, desc192 );
            var idoverprint = stringIDToTypeID( "overprint" );
            desc191.putBoolean( idoverprint, false );
        var idFrFX = charIDToTypeID( "FrFX" );
        desc188.putObject( idFrFX, idFrFX, desc191 );
    var idLefx = charIDToTypeID( "Lefx" );
    desc187.putObject( idT, idLefx, desc188 );
executeAction( idsetd, desc187, DialogModes.NO );
    }

function raterizeLayerStyle(){
    var idrasterizeLayer = stringIDToTypeID( "rasterizeLayer" );
    var desc5 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
        var ref4 = new ActionReference();
        var idLyr = charIDToTypeID( "Lyr " );
        var idOrdn = charIDToTypeID( "Ordn" );
        var idTrgt = charIDToTypeID( "Trgt" );
        ref4.putEnumerated( idLyr, idOrdn, idTrgt );
    desc5.putReference( idnull, ref4 );
    var idWhat = charIDToTypeID( "What" );
    var idrasterizeItem = stringIDToTypeID( "rasterizeItem" );
    var idlayerStyle = stringIDToTypeID( "layerStyle" );
    desc5.putEnumerated( idWhat, idrasterizeItem, idlayerStyle );
    executeAction( idrasterizeLayer, desc5, DialogModes.NO );
}

var current = app.activeDocument;
//current.resizeImage(64,64,72);

//var currentName = current.name;
//var currentPath = current.path;
imageWidth = current.width.value;
imageHeight= current.height.value;
circle = false;
curBounds= getBounds(current.activeLayer);
$.writeln(curBounds.width + "  " + curBounds.height);
$.writeln(typeof(curBounds.width));

if((curBounds.width > curBounds.height && curBounds.width <= curBounds.height + 2)){
    margin = 0.213;
    }
else if((curBounds.height > curBounds.width) && (curBounds.height <= curBounds.width+ 2)){
    margin = 0.213;
    }
else {
    margin = 0.0625;
    }

if(circle){
    margin = 0.0625;
    }

targetWidth= Math.round(imageWidth - (imageWidth * margin));
maxDimension = Math.max(curBounds.width, curBounds.height);

while(maxDimension != targetWidth){
    curBounds = getBounds(current.activeLayer);
    maxDimension = Math.max(curBounds.width, curBounds.height);
    ratio = (targetWidth / maxDimension) * 100;
    current.activeLayer.resize(ratio, ratio);
    }

midX = curBounds.width /2;
midY = curBounds.height /2;

deltaX = 32 - (curBounds.minX + midX);
deltaY = 32 - (curBounds.minY + midY);
current.activeLayer.translate(deltaX, deltaY);

strokeColor = hexToRgb('323232');
fillColor = hexToRgb('21d5fa');

strokeFill(strokeColor, fillColor);

raterizeLayerStyle();
current.resizeImage(24,24,72);




