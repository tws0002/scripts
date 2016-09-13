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
    var wh = [0,0];
    instx = [];
    for(i=0;i<layers.length;i++){
        layerName = layers[i].name;
        frames = layers[i].frames;
        for(j=0;j<frames.length;j++){
            if(frames[j].duration > 1){
                j = j + (frames[j].duration -1); //go to end frame last longer then 1 frame
            }
            elements = frames[j].elements;
            for(k=0;k<elements.length;k++){
                symbolType = elements[k].symbolType;
                elementType = elements[k].elementType;
                curX = elements[k].x;
                curY = elements[k].y;
                if(elementType == 'text'){
                    instanceName = '請轉成Symbol';
                    wh = [0,0];
                }
                if(symbolType == 'movie clip'){
                    instanceName = elements[k].libraryItem.name;
                    //fl.trace(i + "  " + layerName + "   " + (j + 1) + "/" + frames.length + "   " + (k + 1) + "/" + elements.length + " " + elements[k].libraryItem.name);
                    libStage = elements[k].libraryItem.timeline;
                    libLayers = libStage.layers;
                    for(l=0;l<libLayers.length;l++){
                        libFrames = libLayers[l].frames;
                        tweenObj = libFrames[0].tweenObj;
/*                        if(tweenObj){
                            fl.trace('tween obj detected, skipping');
                            wh = libraryExport(instanceName);
                        }*/
                        if(libFrames.length == 1 && !tweenObj ){
                            fl.trace('single frame, skipping');
                            wh = libraryExport(instanceName);
                            
                        }
                        else if(instx.indexOf(instanceName) > -1){
                            fl.trace('already exported');

                        }
                        else{
                            for(m=0;m<libFrames.length;m++){
                                libElements = libFrames[m].elements;
                                for(n=0;n<libElements.length;n++){
                                    if(libElements[n].elementType == 'text'){
                                        wh =libraryExport(instanceName);
                                    }
                                    if(libElements[n].symbolType == 'movie clip'){
                                        libInstanceName = libElements[n].libraryItem.name;
                                            wh = libraryExport(libInstanceName);

                                            //fl.trace((l + 1) + "/" + libLayers.length + "    " + (m + 1) + "/" + libFrames.length + "    " + (n + 1) + "/" + libElements.length + "  " + libElements[n].libraryItem.name);        
                                            //fl.trace(libElements[n].libraryItem.name);
                                            instanceName = libInstanceName;
                                            x = x + 1; 
                                    }
                                }
                            }
                        }
                    }
                    instx.push(instanceName);
                }
                elementData = i + "," + layerName + "," + j + "," + k + "," + instanceName + "," + Math.round(curX) + "," + Math.round(curY) + "," + wh[0] + "," + wh[1] + "," + folderURI + "|linebreak|";
                data = data + elementData;            
                fl.trace(elementData);
            }
        }
    } 
    fl.trace("Number of Layers = " + layers.length);    
    fl.trace('total loops = ' + x);
    fl.closeDocument(newDoc, false);  
    return data
    
    function libraryExport(instanceName){
        libIndex = parseInt(library.findItemIndex(instanceName));

        if (libIndices.indexOf(libIndex) > -1){}
        else{
            width = 0;
            height = 0;
            libIndices.push(libIndex);
            item = library.items[libIndex];
            var itemName = item.name.split('.')[0];
            var exportPath = folderURI + "/" + itemName + ".png";
            newDoc.addItem({x:0.0, y:0.0}, item);
            FLfile.createFolder(exportPath.substring(0, exportPath.lastIndexOf("/")));

            dimensions = newDoc.getTimeline().getBounds(1,true);
            width = Math.abs(dimensions.right) + Math.abs(dimensions.left);
            height = Math.abs(dimensions.top) + Math.abs(dimensions.bottom);


            //fl.trace("name: " + instanceName + "    width:  " + width + "   height: " + height);
            
            widthScaleFactor = 1;
            heightScaleFactor = 1;

            if(Math.round(width) % 2 == 1){
                widthScaleFactor = (width+1)/width;
            }
            
            if(Math.round(height) % 2 == 1){
                heightScaleFactor = (height+1)/height;
            }
            
            newDom.library.selectItem(item.name, false);            
            newDoc.scaleSelection(widthScaleFactor, heightScaleFactor);

            dimensions = newDoc.getTimeline().getBounds(1,true);
            width = Math.abs(dimensions.right) + Math.abs(dimensions.left);
            height = Math.abs(dimensions.top) + Math.abs(dimensions.bottom);


            //fl.trace("name: " + instanceName + "    width:  " + Math.round(width) + "   height: " + Math.round(height));
            
            if(item.itemType == "movie clip"){
                newDoc.exportInstanceToPNGSequence(exportPath);
            }
            else{
                newDoc.exportPNG(exportPath, true, false);
            }
            newDoc.deleteSelection();

        } 
        return [width, height]
    }
}

//exportCoordinates();