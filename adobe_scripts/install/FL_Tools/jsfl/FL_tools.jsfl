function exportCoordinates(){ 
    fl.showIdleMessage(false);
    var doc = fl.getDocumentDOM();
    var newDoc = fl.createDocument();
    var newDom = fl.getDocumentDOM();
    var folderURI = fl.browseForFolderURL('Select output folder');

    var library = doc.library;
    var layers = doc.getTimeline().layers;
    var x = 0;

    var libIndices = [];    
    var data = "";
    instx = [];
    for(i=0;i<layers.length;i++){
        layerName = layers[i].name;
        frames = layers[i].frames;
        for(j=0;j<frames.length;j++){
            elements = frames[j].elements;
            for(k=0;k<elements.length;k++){
                //fl.trace("k" + k + "/" + elements.length);
                symbolType = elements[k].symbolType;
                curX = elements[k].x;
                curY = elements[k].y;
                if(symbolType == 'movie clip'){
                    instanceName = elements[k].libraryItem.name;
                    //fl.trace(i + "  " + layerName + "   " + (j + 1) + "/" + frames.length + "   " + (k + 1) + "/" + elements.length + " " + elements[k].libraryItem.name);
                    libStage = elements[k].libraryItem.timeline;
                    libLayers = libStage.layers;
                    for(l=0;l<libLayers.length;l++){
                        libFrames = libLayers[l].frames;
                        tweenObj = libFrames[0].tweenObj;
                        if(tweenObj && instx.indexOf(instanceName) == -1){
                            //fl.trace('tween obj detected, skipping');
                            libraryExport(instanceName);
                            instx.push(instanceName);
                            elementData = layerName + "," + instanceName + "," + curX + "," + curY + "," + folderURI + "|linebreak|";
                            data = data + elementData;                                
                        }
                        else if(libFrames.length == 1 && instx.indexOf(instanceName) == -1){
                            //fl.trace('single frame, skipping');
                            libraryExport(instanceName);
                            instx.push(instanceName);
                            elementData = layerName + "," + instanceName + "," + curX + "," + curY + "," + folderURI + "|linebreak|";
                            data = data + elementData;                                
                        }
                        else if(instx.indexOf(instanceName) == -1){
                            libraryExport(instanceName);
                            instx.push(instanceName); 
                            elementData = layerName + "," + instanceName + "," + curX + "," + curY + "," + folderURI + "|linebreak|";
                            data = data + elementData;    
                        }
                        else{
                            for(m=0;m<libFrames.length;m++){
                                libElements = libFrames[m].elements;
                                for(n=0;n<libElements.length;n++){
                                    if(libElements[n].symbolType == 'movie clip'){
                                        libInstanceName = libElements[n].libraryItem.name;
                                        libraryExport(libInstanceName);
                                        //fl.trace((l + 1) + "/" + libLayers.length + "    " + (m + 1) + "/" + libFrames.length + "    " + (n + 1) + "/" + libElements.length + "  " + libElements[n].libraryItem.name);        
                                        //fl.trace(libElements[n].libraryItem.name);
                                        x = x + 1; 
                                    }
                                }
                            }
                        }
                    }
                }
        
                fl.trace(elementData);
            }
        }
    } 
    fl.trace(instx.length);
    fl.trace("Number of Layers = " + layers.length);    
    fl.trace('total loops = ' + x);
    fl.closeDocument(newDoc, false);  
    return data
    
    function libraryExport(instanceName){
        libIndex = parseInt(library.findItemIndex(instanceName));

        if (libIndices.indexOf(libIndex) > -1){}
        else{
            libIndices.push(libIndex);
            item = library.items[libIndex];
            var itemName = item.name.split('.')[0];
            var exportPath = folderURI + "/" + itemName + ".png";
            newDoc.addItem({x:0.0, y:0.0}, item);
            FLfile.createFolder(exportPath.substring(0, exportPath.lastIndexOf("/")));
            if(item.itemType == "movie clip"){
                newDoc.exportInstanceToPNGSequence(exportPath);
            }
            else{
                newDoc.exportPNG(exportPath, true, false);
            }
            newDoc.deleteSelection();
        } 
    }
}

//exportCoordinates();