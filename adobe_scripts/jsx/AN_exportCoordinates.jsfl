// Assigns the layers array to the variable "theLayers". 
var theLayers = fl.getDocumentDOM().getTimeline().layers; 

//fl.trace(theLayers.length)
for(i=0;i<theLayers.length;i++){
	frameLength = theLayers[i].frames.length;
	layerName = theLayers[i].name;
	//fl.trace(layerName);
	if(frameLength == 0){}
	else{
		layerElements = theLayers[i].frames[0].elements;
		if(layerElements.length == 0){}
		else{
			for(j=0;j<layerElements.length;j++){
				curX = layerElements[j].x;
				curY = layerElements[j].y;
				fl.trace("layer name = " + layerName + " elementX= " + curX + " elementY= " + curY);
				
			}
		}

	}
}
	


//fl.trace(theLayers[10].frames[0].elements[0].transformX)

var layers = fl.getDocumentDOM().getTimeline().layers;
// include 'var' it's good taste
var timeline = fl.getDocumentDOM().getTimeline();

for(i=0;i<layers.length;i++){
//fl.trace(layers[i].name);
}


current = fl.getDocumentDOM();
//current.selectAll()

fl.trace(current.selection[0].constructor); 
//var getClassOf = Function.prototype.call.bind(Object.prototype.toString);
fl.trace(fl.getDocumentDOM().library.items[10].sourceLibraryName);
getQualifiedClassName(current.selection[0]);