//
//圖層座標，群組座標輸出版
//
//不會輸出隱藏之圖層

psdname = "";
CR = String.fromCharCode(13);
var indent = 2;
var icnt = 0;

//全圖層匯出
function searchLayer( layObj, indent )
{
	var i,k;
	var idt = "■";
	var n = layObj.artLayers.length;

		for ( i=0;  i<n; i++)	{
			if( layObj.artLayers[i].visible == true ){
				var x1 = parseFloat( layObj.artLayers[i].bounds[0] );
				var y1 = parseInt( layObj.artLayers[i].bounds[1] );
				var width = parseInt(layObj.artLayers[i].bounds[2])-parseInt(layObj.artLayers[i].bounds[0]);
    			var height = parseInt(layObj.artLayers[i].bounds[3])-parseInt(layObj.artLayers[i].bounds[1]);
    			
				layName = layObj.artLayers[i].name;
				
				str = layName + "," + x1 + "," + y1 + "," + width + "," + height + CR ;
				fileObj.write( str );
			}
		}

	var ns = layObj.layerSets.length;
	for ( i=0; i<ns; i++)	{
		if( layObj.layerSets[i].visible == true ){	    
		    fileObj.write( idt + layObj.layerSets[i].name + CR );
		    icnt += 1;
		    searchLayer( layObj.layerSets[i], icnt )
		}
	}
	icnt -= 1;
}

savename = File.saveDialog("請輸入要保存的檔案名稱 ");
if (savename)
{
	fileObj = new File(savename);
	flag = fileObj.open("w");

	if (flag == true)
	{
			str =  "圖層名稱," + "X," + "Y," + "寬," + "高," + CR  + CR;
			fileObj.write( str );
			searchLayer( activeDocument );
			fileObj.close();
			alert("輸出完成");
    }else{
		alert("無法開啟檔案");
	}

}