global SMTDSettings
global SMTD_RegionRendering
global SMTD_MultiRegionRendering

plugin simpleManipulator DLRegionManipulator
	name:"RegionManip"
	classID:#(0x7c427c83, 0xc28852d)
	category:"Manipulators"
	invisible:true
(
	local greenColor =  colorMan.getColor #manipulatorsActive
	local redColor =    colorMan.getColor #manipulatorsSelected
	local yellowColor = colorMan.getColor #manipulatorsInactive
	local orangeColor = [1.0,0.65,0.45]
	local offTileColor = [0.6,0.5,0.5]
	local tileColor = [0.8,0.65,0.65]

	parameters main rollout:paramRollout
	( 
		cornerX type:#float animatable:false ui:spn_cornerX default:0.0
		cornerY type:#float animatable:false ui:spn_cornerY default:0.0
		cornerX2 type:#float animatable:false ui:spn_cornerX2 default:1.0
		cornerY2 type:#float animatable:false ui:spn_cornerY2 default:1.0
		tilesX type:#integer animatable:false ui:spn_tilesX default:1
		tilesY type:#integer animatable:false ui:spn_tilesY default:1
	)
	
	rollout paramRollout "Region"
	(
		Spinner  spn_cornerX "X:"	range:[0,1,0]  type:#float
		Spinner  spn_cornerY "Y:"	range:[0,1,0]  type:#float
		Spinner  spn_cornerX2 "X2:"	range:[0,1,0]  type:#float
		Spinner  spn_cornerY2 "Y2:"	range:[0,1,0]  type:#float
		Spinner  spn_tilesX "X2:"	range:[1,10,1]  type:#integer
		Spinner  spn_tilesY "Y2:"	range:[1,10,1]  type:#integer
	)	

	on canManipulate target  return (classOf target) == DLRegionManipulator
	tool create
	(
		on mousePoint click do
		   case click of
		   (
			  1: #stop 
		   )
	)

	on updateGizmos do
	(
		this.clearGizmos()
		if SMTD_MultiRegionRendering.lastSelectedLines[1] == undefined or SMTDSettings.MultiRegionData.count == 0 do return ""
		local isLocked = try(SMTDSettings.MultiRegionData[SMTD_MultiRegionRendering.lastSelectedLines[1]][11] == true)catch(false)
		
		if (target != undefined) then 
		(
		   this.cornerX= target.cornerX
		   this.cornerY= target.cornerY
		   this.cornerX2= target.cornerX2
		   this.cornerY2= target.cornerY2
			if isLocked then
			(
				selColor = unselColor  = greenColor*0.85
			)
			else
			(
				selColor = redColor
				unselColor  = greenColor
			)
		) 
		else
		(
		   selColor = unselColor  = yellowColor
		)
		
		-- These flags are used for all the gizmos
		local flags = (gizmoUseScreenSpace + gizmoActiveViewportOnly)
		local flags2 = (gizmoUseScreenSpace + gizmoActiveViewportOnly + gizmoDontHitTest)

		local xSize = gw.getWinSizeX()-1
		local ySize = gw.getWinSizeY()-1
		
		local vpAspect = gw.getWinSizeX() as float / gw.getWinSizeY() as float
		local rAspect = RenderWidth as float / RenderHeight * renderPixelAspect
		
		if rAspect > vpAspect then
		(
			ySize = gw.getWinSizeX() / rAspect
			xDiff = 0
			yDiff = (gw.getWinSizeY() - ySize)/2
		)	
		else
		(
			xSize = gw.getWinSizeY() * rAspect
			xDiff = 0.5*(gw.getWinSizeX() - xSize)
			yDiff = 0
		)	
		
		local corner1 = [cornerX*xSize+xDiff,cornerY*ySize+yDiff,0]
		local corner2 = [cornerX2*xSize+xDiff,cornerY*ySize+yDiff ,0]
		local corner3 = [cornerX2*xSize+xDiff,cornerY2*ySize+yDiff ,0]
		local corner4 = [cornerX*xSize+xDiff,cornerY2*ySize+yDiff ,0]
		
		theWinX = gw.getWinSizeX()-1
		theWinY = gw.getWinSizeY()-1
		local drawCorner1 = copy corner1
		local drawCorner2 = copy corner2
		local drawCorner3 = copy corner3
		local drawCorner4 = copy corner4
		
		if drawCorner1.x < 0 do drawCorner4.x = drawCorner1.x = 0
		if drawCorner2.x >= theWinX do drawCorner2.x = drawCorner3.x = theWinX
		if drawCorner1.y < 0 do drawCorner2.y = drawCorner1.y = 0
		if drawCorner3.y >= theWinY do drawCorner3.y = drawCorner4.y = theWinY
		
		local offset = 6
		if isLocked do offset = 0
		-- Create a polyline gizmo 0 Top Line
		local giz = manip.makeGizmoShape()
		giz.AddPoint (drawCorner1+[offset,0,0])
		giz.AddPoint (drawcorner2-[offset,0,0])
		this.addGizmoShape giz flags unselColor selColor

		-- Create a polyline gizmo 1 Right Line
		local giz = manip.makeGizmoShape()
		giz.AddPoint (drawcorner2+[0,offset,0])
		giz.AddPoint (drawcorner3-[0,offset,0])
		this.addGizmoShape giz flags unselColor selColor

		-- Create a polyline gizmo 2 Bottom Line
		local giz = manip.makeGizmoShape()
		giz.AddPoint (drawcorner3-[offset,0,0])
		giz.AddPoint (drawcorner4+[offset,0,0])
		this.addGizmoShape giz flags unselColor selColor

		-- Create a polyline gizmo 3 Left Line
		local giz = manip.makeGizmoShape()
		giz.AddPoint (drawcorner4-[0,offset,0])
		giz.AddPoint (drawcorner1+[0,offset,0])
		this.addGizmoShape giz flags unselColor selColor

		--Gizmo 4		Center
		if SMTD_MultiRegionRendering.lastSelectedLines[1] != undefined and SMTDSettings.MultiRegionData[SMTD_MultiRegionRendering.lastSelectedLines[1]][11] == true then
			this.addGizmoMarker #xMarker [((cornerX+cornerX2)/2)*xSize+xDiff,((cornerY+cornerY2)/2)*ySize+yDiff,0] flags unselColor selColor --4
		else
			this.addGizmoMarker #circle [((cornerX+cornerX2)/2)*xSize+xDiff,((cornerY+cornerY2)/2)*ySize+yDiff,0] flags unselColor selColor --4
		if not isLocked do
		(
			this.addGizmoMarker #bigBox corner1 flags unselColor selColor --5 Upper Left
			this.addGizmoMarker #bigBox corner2 flags unselColor selColor --6 Upper Right
			this.addGizmoMarker #bigBox corner3 flags unselColor selColor --7 Bottom Right
			this.addGizmoMarker #bigBox corner4 flags unselColor selColor --8 Bottom Left
		)
		
		local theStep = ((corner2.x-corner1.x)/tilesX)
		if theStep > 0 do
		(
			for x = corner1.x to corner2.x by theStep do
			(
				if x != corner1.x and x != corner2.x do
				(
					local giz = manip.makeGizmoShape()
					giz.AddPoint [x,drawcorner1.y,0]
					giz.AddPoint [x,drawcorner4.y,0]
					this.addGizmoShape giz flags2 tileColor tileColor
				)
			)		
		)
		theStep = ((corner4.y-corner1.y)/tilesY) 
		if theStep != 0 do 
		(
			for y = corner1.y to corner4.y by theStep do
			(
				if y != corner1.y and y != corner4.y do
				(			
					local giz = manip.makeGizmoShape()
					giz.AddPoint [drawcorner1.x,y,0]
					giz.AddPoint [drawcorner2.x,y,0]
					this.addGizmoShape giz flags2 tileColor tileColor
				)
			)		
		)
		-- return an empty string so no tool tip is displayed
		return ""
	)

	-- mouseMove is called on every mouse move when dragging the manip
	-- It needs to convert the mouse position 'm' into a new value for the slider
	on mouseMove m which do
	(
		if SMTDSettings.MultiRegionData[SMTD_MultiRegionRendering.lastSelectedLines[1]][11] == true do return false
		
		local xSize = gw.getWinSizeX()-1
		local ySize = gw.getWinSizeY()-1
		
		local vpAspect = gw.getWinSizeX() as float / gw.getWinSizeY() as float
		local rAspect = RenderWidth as float / RenderHeight * renderPixelAspect
		
		if rAspect > vpAspect then
		(
			ySize = gw.getWinSizeX() / rAspect
			yDiff = 0.5 * (gw.getWinSizeY() - ySize)
			xDiff = 0
		)	
		else
		(
			xSize = gw.getWinSizeY() * rAspect
			xDiff = 0.5 * (gw.getWinSizeX() - xSize)
			yDiff = 0
		)	

		local notBlowup = true --try(SMTD_RegionRendering.ddl_regionType.selected != "Blowup" )catch(true)
		
		local regX = SMTDSettings.MultiRegionData[SMTD_MultiRegionRendering.lastSelectedLines[1]][2]
		local regY = SMTDSettings.MultiRegionData[SMTD_MultiRegionRendering.lastSelectedLines[1]][3]
		local regW = SMTDSettings.MultiRegionData[SMTD_MultiRegionRendering.lastSelectedLines[1]][4]
		local regH = SMTDSettings.MultiRegionData[SMTD_MultiRegionRendering.lastSelectedLines[1]][5]
		local cx = regX+ regW/2 --center X
		local cy = regY+ regH/2 --center Y
		
		local currentW = regW/1.9
		local currentH = regH/1.9
		
		local theSnapY = #(0.0,1.0)
		for i = 1 to SMTDSettings.MultiRegionData.count where i != SMTD_MultiRegionRendering.lastSelectedLines[1] and (theX = (m.x-xDiff)/xSize; theX >= SMTDSettings.MultiRegionData[i][2]-currentW and theX <= SMTDSettings.MultiRegionData[i][2]+SMTDSettings.MultiRegionData[i][4]+currentW) do join theSnapY #(SMTDSettings.MultiRegionData[i][3],SMTDSettings.MultiRegionData[i][3]+SMTDSettings.MultiRegionData[i][5])
		local theSnapX = #(0.0,1.0)
		for i = 1 to SMTDSettings.MultiRegionData.count where i != SMTD_MultiRegionRendering.lastSelectedLines[1] and (theY = (m.y-yDiff)/ySize; theY >= SMTDSettings.MultiRegionData[i][3]-currentH and theY <= SMTDSettings.MultiRegionData[i][3]+SMTDSettings.MultiRegionData[i][5]+currentH) do join theSnapX #(SMTDSettings.MultiRegionData[i][2], SMTDSettings.MultiRegionData[i][2]+SMTDSettings.MultiRegionData[i][4])
		
		local theSnapThreshold = 0.01
		case which of
		(
			0: --top line
			(
				local y = (m.y-yDiff) / ySize
				if y < 0 do y = 0
				if y > cornerY2 do y = cornerY2
				if not keyboard.controlpressed do for i in theSnapY where abs (i-y) < theSnapThreshold do y = i
				target.cornerY = y
				if keyboard.shiftPressed do target.cornerY2 = 2*cy-y
			)
			1: --right line
			(
				local x = (m.x-xDiff) / xSize
				if x > 1.0 do x = 1.0
				if x < cornerX do x = cornerX
				if not keyboard.controlpressed do for i in theSnapX where abs (i-x) < theSnapThreshold do x = i
				target.cornerX2 = x
				if keyboard.shiftPressed do target.cornerX = 2*cx-x
			)	 
			2: --bottom line
			(
				local y = (m.y-yDiff) / ySize
				if y > 1.0 do y = 1.0
				if y < cornerY do y = cornerY
				if not keyboard.controlpressed do for i in theSnapY where abs (i-y) < theSnapThreshold do y = i
				target.cornerY2 = y
				if keyboard.shiftPressed do target.cornerY = 2*cy-y
			)		
			3: --left line
			(
				local x = (m.x-xDiff) / xSize
				if x < 0 do x = 0
				if x > cornerX2 do x = cornerX2
				if not keyboard.controlpressed do for i in theSnapX where abs (i-x) < theSnapThreshold do x = i
				target.cornerX = x
				if keyboard.shiftPressed do target.cornerX2 = 2*cx-x
			)		
			4:  --central O handle
			(
				local width = cornerX2 - cornerX
				local height = cornerY2 - cornerY
				local x = (m.x-xDiff) / xSize
				local y = (m.y-yDiff) / ySize
				
				if not keyboard.controlpressed do for i in theSnapX where abs (i-(x+width/2)) < theSnapThreshold do x = i - width/2
				if not keyboard.controlpressed do for i in theSnapY where abs (i-(y+height/2)) < theSnapThreshold do y = i - height/2
				if not keyboard.controlpressed do for i in theSnapX where abs (i-(x-width/2)) < theSnapThreshold do x = i + width/2
				if not keyboard.controlpressed do for i in theSnapY where abs (i-(y-height/2)) < theSnapThreshold do y = i + height/2
				
				target.cornerX = x-width/2
				target.cornerX2 = x+width/2
				target.cornerY = y-height /2
				target.cornerY2 = y+height /2
			)		
			5: --corner 1
			(
				local x = (m.x-xDiff) / xSize
				local y = (m.y-yDiff) / ySize
				
				if x < 0 do x = 0
				if y < 0 do y = 0
				if x > cornerX2 do x = cornerX2
				if y > cornerY2 do y = cornerY2

				if not keyboard.controlpressed do 
				(
					for i in theSnapY where abs (i-y) < theSnapThreshold do y = i
					for i in theSnapX where abs (i-x) < theSnapThreshold do x = i
				)
				target.cornerX = x
				target.cornerY = y
				if keyboard.shiftPressed do 
				(
					target.cornerY2 = 2*cy-y		
					target.cornerX2 = 2*cx-x					
				)
			)
			6: --corner 2
			(
				local x = (m.x-xDiff) / xSize
				local y = (m.y-yDiff) / ySize
				
				if x > 1.0 do x = 1.0
				if y < 0 do y = 0
				if x < cornerX do x = cornerX
				if y > cornerY2 do y = cornerY2

				if not keyboard.controlpressed do 
				(
					for i in theSnapY where abs (i-y) < theSnapThreshold do y = i
					for i in theSnapX where abs (i-x) < theSnapThreshold do x = i
				)
				target.cornerX2 = x
				target.cornerY = y
				if keyboard.shiftPressed do 
				(
					target.cornerY2 = 2*cy-y		
					target.cornerX = 2*cx-x					
				)				
			)	
			7: --corner 3
			(
				local x = (m.x-xDiff) / xSize
				local y = (m.y-yDiff) / ySize
				
				if x > 1.0 do x = 1.0
				if y > 1.0 do y = 1.0
				if x < cornerX do x = cornerX
				if y < cornerY do y = cornerY

				if not keyboard.controlpressed do 
				(
					for i in theSnapY where abs (i-y) < theSnapThreshold do y = i
					for i in theSnapX where abs (i-x) < theSnapThreshold do x = i
				)
				target.cornerX2 = x
				target.cornerY2 = y
				if keyboard.shiftPressed do 
				(
					target.cornerY = 2*cy-y
					target.cornerX = 2*cx-x					
				)				
				
			)	
			8: --corner 4
			(
				local x = (m.x-xDiff) / xSize
				local y = (m.y-yDiff) / ySize
				
				if x < 0 do x = 0
				if y > 1.0 do y = 1.0
				if x > cornerX2 do x = cornerX2
				if y < cornerY do y = cornerY
					
				if not keyboard.controlpressed do 
				(
					for i in theSnapY where abs (i-y) < theSnapThreshold do y = i
					for i in theSnapX where abs (i-x) < theSnapThreshold do x = i
				)
				target.cornerX = x
				target.cornerY2 = y
				if keyboard.shiftPressed do 
				(
					target.cornerY = 2*cy-y		
					target.cornerX2 = 2*cx-x					
				)				
			)	
		)
		try
		(
			--SMTD_RegionRendering.updateFromRegionGizmo()
			SMTD_MultiRegionRendering.updateFromRegionGizmo()
--			SMTD_RegionRendering.spn_regionLeft.changed (SMTD_RegionRendering.spn_regionLeft.value = ceil (target.cornerX*RenderWidth) )
--			SMTD_RegionRendering.spn_regionTop.changed (SMTD_RegionRendering.spn_regionTop.value = ceil (target.cornerY*RenderHeight))
--			SMTD_RegionRendering.spn_regionWidth.changed (SMTD_RegionRendering.spn_regionWidth.value = ceil ((target.cornerX2-target.cornerX)*RenderWidth))
--			SMTD_RegionRendering.spn_regionHeight.changed (SMTD_RegionRendering.spn_regionHeight.value = ceil ((target.cornerY2-target.cornerY)*RenderHeight))
		)catch()
		
	)
)

plugin simpleManipulator DLMultiRegionManipulator
    name:"MultiRegionManip"
    classID:#(0x7c427c77, 0xc288568)
    category:"Manipulators"
	invisible:true
(
    local greenColor =  colorMan.getColor #manipulatorsActive
    local redColor =    colorMan.getColor #manipulatorsSelected
    local yellowColor = colorMan.getColor #manipulatorsInactive
	local offColor = yellowColor * 0.75
	local offTileColor = [0.6,0.5,0.5]
	local tileColor = [0.8,0.65,0.65]
	local cyanColor = [0.5,0.8,1.0]
	local orangeColor = [0.85,0.65,0.45]
	
	local gizmoMap = #()

    on canManipulate target  return (classOf target) == DLMultiRegionManipulator

    -- Creation mouse procedure
    tool create
    (
        on mousePoint click do
           case click of
           (
              1: 
              (
                #stop 
              )
           )

    )

    on updateGizmos do
    (
        this.clearGizmos()
		
        -- These flags are used for all the gizmos
        local flags = (gizmoUseScreenSpace + gizmoActiveViewportOnly + gizmoDontHitTest)
        local flags2 = (gizmoUseScreenSpace + gizmoActiveViewportOnly)

--		this.addGizmoMarker #diamond [gw.getWinSizeX()*0.5,0.5*gw.getWinSizeY(),0.0] flags yellowColor redColor
		
		local xSize = gw.getWinSizeX() - 1
		local ySize = gw.getWinSizeY() - 1

		local vpAspect = gw.getWinSizeX() as float / gw.getWinSizeY() as float
		local rAspect = RenderWidth as float / RenderHeight * renderPixelAspect

		if rAspect > vpAspect then
		(
			ySize = gw.getWinSizeX() / rAspect
			xDiff = 0
			yDiff = (gw.getWinSizeY() - ySize)/2
		)	
		else
		(
			xSize = gw.getWinSizeY() * rAspect
			xDiff = 0.5*(gw.getWinSizeX() - xSize)
			yDiff = 0
		)	
		
		gizmoMap = #()
		local cnt = 0
		local gizmocount = 0
		local theSel = SMTD_MultiRegionRendering.getListViewSelection()
		for i = 1 to ::SMTDSettings.MultiRegionData.count do
		(
			local aRegion = SMTDSettings.MultiRegionData[i]
			cnt += 1
			theX1 = aRegion[2]*xSize + xDiff
			theY1 = aRegion[3]*ySize + yDiff
			theX2 = theX1 + aRegion[4]*xSize
			theY2 = theY1 + aRegion[5]*ySize
			
			theDrawX1 = copy theX1
			theDrawX2 = copy theX2
			theDrawY1 = copy theY1
			theDrawY2 = copy theY2
			
			if theDrawX1 < 0 do theDrawX1 = 0
			if theDrawX2 < 0 do theDrawX2 = 0
			if theDrawY1 < 0 do theDrawY1 = 0
			if theDrawY2 < 0 do theDrawY2 = 0

			if theDrawX1 > xSize+xDiff+xDiff do theDrawX1 = xSize+xDiff+xDiff
			if theDrawX2 > xSize+xDiff+xDiff do theDrawX2 = xSize+xDiff+xDiff
			if theDrawY1 > ySize+yDiff+yDiff do theDrawY1 = ySize+yDiff+yDiff
			if theDrawY2 > ySize+yDiff+yDiff do theDrawY2 = ySize+yDiff+yDiff

			local mainColor = (if SMTDSettings.MultiRegionData[i][1] == True then yellowColor else offColor )
			if findItem theSel i > 0 do mainColor = (if SMTDSettings.MultiRegionData[i][1] == True then cyanColor else cyanColor*0.75)
			local gridColor = (if SMTDSettings.MultiRegionData[i][1] == True then tileColor else offTileColor )
			if (SMTD_MultiRegionRendering.lastSelectedLines.count != 1 or findItem SMTD_MultiRegionRendering.lastSelectedLines i == 0) do
			(
				theStep = ((theX2-theX1)/aRegion[6]) 
				if theStep > 0 do
				(	
					for x = theX1 to theX2 by theStep do
					(
						local giz = manip.makeGizmoShape()
						giz.AddPoint [x,theDrawY1,0]
						giz.AddPoint [x,theDrawY2,0]
						this.addGizmoShape giz flags gridColor redColor
						gizmocount += 1			
						--gizmoMap[gizmocount] = cnt
					)		
				)
				theStep = ((theY2-theY1)/aRegion[7]) 
				if theStep > 0 do
				(
					for y = theY1 to theY2 by theStep do
					(
						local giz = manip.makeGizmoShape()
						giz.AddPoint [theDrawX1,y,0]
						giz.AddPoint [theDrawX2,y,0]
						this.addGizmoShape giz flags gridColor redColor
						gizmocount += 1			
						--gizmoMap[gizmocount] = cnt						
					)
				)				
				
				local giz = manip.makeGizmoShape()
				giz.AddPoint [theDrawX1,theDrawY1,0]
				giz.AddPoint [theDrawX2,theDrawY1,0]
				giz.AddPoint [theDrawX2,theDrawY2,0]
				giz.AddPoint [theDrawX1,theDrawY2,0]
				giz.AddPoint [theDrawX1,theDrawY1,0]
				
				this.addGizmoShape giz flags mainColor redColor
				gizmocount += 1
				--gizmoMap[gizmocount] = cnt

			)
			
			XTextOffset = 7 + ((cnt as string).count)*7
			YTextOffset = 5
			
			/*
			this.addGizmoText (cnt as string)  [theX1+15,theY2-YTextOffset,0] flags mainColor mainColor
			gizmocount += 1

			this.addGizmoText (cnt as string)  [theX2-XTextOffset,theY2-YTextOffset,0] flags mainColor mainColor
			gizmocount += 1

			this.addGizmoText (cnt as string)  [theX1+15,theY1+15+YTextOffset,0] flags mainColor mainColor
			gizmocount += 1
			
			this.addGizmoText (cnt as string)  [theX2-XTextOffset,theY1+15+YTextOffset,0] flags mainColor mainColor
			gizmocount += 1
			*/
			
			this.addGizmoText (cnt as string)  [theX1+(theX2-theX1)/2-XTextOffset/2+4,theY1+(theY2-theY1)/2-6,0] flags mainColor mainColor
			gizmocount += 1			
			
			if (SMTD_MultiRegionRendering.lastSelectedLines.count != 1 or findItem SMTD_MultiRegionRendering.lastSelectedLines i == 0) do
			(
				local theMarker = (if SMTDSettings.MultiRegionData[i][11] == true then #xMarker else #plussign)
				this.addGizmoMarker theMarker [theX1+(theX2-theX1)/2,theY1+(theY2-theY1)/2,0] (if (SMTD_MultiRegionRendering.lastSelectedLines.count != 1 or findItem SMTD_MultiRegionRendering.lastSelectedLines i == 0) then flags2 else flags) greencolor redColor 
				gizmocount += 1
				gizmoMap[gizmocount] = cnt
			)
			
		)		
        -- return an empty string so no tool tip is displayed
        return ""
    )
	
	on mouseDown m which do
	(
		if gizmoMap[which+1] != undefined do 
		(
			theSel = if keyboard.controlPressed then
				SMTD_MultiRegionRendering.getListViewSelection()
			else
				#()
			if (theIndex = findItem theSel gizmoMap[which+1]) == 0 then 
				append theSel gizmoMap[which+1]
			else
				deleteItem theSel theIndex
			SMTD_MultiRegionRendering.setListViewSelection theSel
			SMTD_MultiRegionRendering.lastSelectedLines = theSel
			SMTD_MultiRegionRendering.updateSpinners()
			this.clearGizmos()
			SMTD_MultiRegionRendering.createRegionGizmo (theSel.count == 1)
			if theSel.count == 1 do SMTD_MultiRegionRendering.updateToRegionGizmo()
			max views redraw
			redrawViews()
			try(select (getNodeByName "DLMultiRegionManipulator"))catch()
		)
	)
	/*	
    on mouseMove m which do
    (
		print m
		print which
		format "%\n" gizmoMap
		print gizmoMap[which+1]
		if gizmoMap[which+1] != undefined do SMTD_MultiRegionRendering.setListViewSelection #(gizmoMap[which+1])
		
    )
	*/
)




plugin simpleManipulator DLMaxRegionManipulator
	name:"MaxRegionManip"
	classID:#(0x2e40d5c2, 0x15145736)
	category:"Manipulators"
	invisible:true
(
	local greenColor =  colorMan.getColor #manipulatorsActive
	local redColor =    colorMan.getColor #manipulatorsSelected
	local yellowColor = colorMan.getColor #manipulatorsInactive

	parameters main rollout:paramRollout
	( 
		cornerX type:#float animatable:false ui:spn_cornerX default:0.0
		cornerY type:#float animatable:false ui:spn_cornerY default:0.0
		cornerX2 type:#float animatable:false ui:spn_cornerX2 default:0.0
		cornerY2 type:#float animatable:false ui:spn_cornerY2 default:0.0
	)

	rollout paramRollout "Region"
	(
		Spinner  spn_cornerX "X:"	range:[0,1,0]  type:#float
		Spinner  spn_cornerY "Y:"	range:[0,1,0]  type:#float
		Spinner  spn_cornerX2 "X2:"	range:[0,1,0]  type:#float
		Spinner  spn_cornerY2 "Y2:"	range:[0,1,0]  type:#float
	)

	on canManipulate target  return (classOf target) == DLMaxRegionManipulator
	tool create
	(
		on mousePoint click do
		   case click of
		   (
			  1: #stop 
		   )
	)

	on updateGizmos do
	(
		this.clearGizmos()
		if (target != undefined) then 
		(
		   this.cornerX= target.cornerX
		   this.cornerY= target.cornerY
		   this.cornerX2= target.cornerX2
		   this.cornerY2= target.cornerY2
		   unselColor  = greenColor
		) 
		else
		(
		   unselColor  = yellowColor
		)

		-- These flags are used for all the gizmos
		local flags = (gizmoUseScreenSpace + gizmoActiveViewportOnly)

		local xSize = gw.getWinSizeX()-1
		local ySize = gw.getWinSizeY()-1
		
		local vpAspect = gw.getWinSizeX() as float / gw.getWinSizeY() as float
		local rAspect = RenderWidth as float / RenderHeight * renderPixelAspect
		
		if rAspect > vpAspect then
		(
			ySize = gw.getWinSizeX() / rAspect
			xDiff = 0
			yDiff = (gw.getWinSizeY() - ySize)/2
		)	
		else
		(
			xSize = gw.getWinSizeY() * rAspect
			xDiff = 0.5*(gw.getWinSizeX() - xSize)
			yDiff = 0
		)	
		
		local corner1 = [cornerX*xSize+xDiff,cornerY*ySize+yDiff,0]
		local corner2 = [cornerX2*xSize+xDiff,cornerY*ySize+yDiff ,0]
		local corner3 = [cornerX2*xSize+xDiff,cornerY2*ySize+yDiff ,0]
		local corner4 = [cornerX*xSize+xDiff,cornerY2*ySize+yDiff ,0]
		
		-- Create a polyline gizmo 0
		local giz = manip.makeGizmoShape()
		giz.AddPoint corner1
		giz.AddPoint corner2
		this.addGizmoShape giz flags unselColor redColor

		-- Create a polyline gizmo 1
		local giz = manip.makeGizmoShape()
		giz.AddPoint corner2
		giz.AddPoint corner3
		this.addGizmoShape giz flags unselColor redColor

		-- Create a polyline gizmo 2
		local giz = manip.makeGizmoShape()
		giz.AddPoint corner3
		giz.AddPoint corner4
		this.addGizmoShape giz flags unselColor redColor

		-- Create a polyline gizmo 3
		local giz = manip.makeGizmoShape()
		giz.AddPoint corner4
		giz.AddPoint corner1
		this.addGizmoShape giz flags unselColor redColor

		--Gizmo 4		
		this.addGizmoMarker #circle [((cornerX+cornerX2)/2)*xSize+xDiff,((cornerY+cornerY2)/2)*ySize+yDiff,0] flags unselColor redColor --4
		
--		local theMesh = manip.makeBox [((cornerX+cornerX2)/2)*xSize+xDiff,((cornerY+cornerY2)/2)*ySize+yDiff,0] (cornerX2-cornerX) (cornerY2-cornerY) 0 3 3 1 
--		this.addGizmoMesh theMesh flags unselColor redColor
--		delete theMesh
		
		this.addGizmoMarker #bigBox corner1 flags unselColor redColor --5
		this.addGizmoMarker #bigBox corner2 flags unselColor redColor --6
		this.addGizmoMarker #bigBox corner3 flags unselColor redColor --7
		this.addGizmoMarker #bigBox corner4 flags unselColor redColor --8
		
		-- return an empty string so no tool tip is displayed
		return ""
	)

	-- mouseMove is called on every mouse move when dragging the manip
	-- It needs to convert the mouse position 'm' into a new value for the slider
	on mouseMove m which do
	(
		local xSize = gw.getWinSizeX()-1
		local ySize = gw.getWinSizeY()-1
		
		local vpAspect = gw.getWinSizeX() as float / gw.getWinSizeY() as float
		local rAspect = RenderWidth as float / RenderHeight * renderPixelAspect
		
		if rAspect > vpAspect then
		(
			ySize = gw.getWinSizeX() / rAspect
			yDiff = 0.5 * (gw.getWinSizeY() - ySize)
			xDiff = 0
		)	
		else
		(
			xSize = gw.getWinSizeY() * rAspect
			xDiff = 0.5 * (gw.getWinSizeX() - xSize)
			yDiff = 0
		)		
		
		local notBlowup = SMTDSettings.regionType != 3
		
		case which of
		(
			0:
			(
				local y = (m.y-yDiff) / ySize
				if notBlowup then
				(
					if y < 0 do y = 0
					if y > cornerY2 do y = cornerY2
				)
				else
				(
					local centerX = target.cornerX + ((target.cornerX2-target.cornerX)/2)
					local halfsize = (target.cornerY2-y)/2.0
					target.cornerX = centerX - halfsize
					target.cornerX2 = centerX + halfsize
				)
				target.cornerY = y
			)
			1:
			(
				local x = (m.x-xDiff) / xSize
				if notBlowup then
				(
					if x > 1.0 do x = 1.0
					if x < cornerX do x = cornerX
				)
				else
				(
					local centerY = target.cornerY + ((target.cornerY2-target.cornerY)/2)
					local halfsize = (x-target.cornerX)/2.0
					target.cornerY = centerY - halfsize
					target.cornerY2 = centerY + halfsize
				)				
				target.cornerX2 = x
			)	
			2:
			(
				local y = (m.y-yDiff) / ySize
				if notBlowup then
				(
					if y > 1.0 do y = 1.0
					if y < cornerY do y = cornerY
				)
				else
				(
					local centerX = target.cornerX + ((target.cornerX2-target.cornerX)/2)
					local halfsize = (y-target.cornerY)/2.0
					target.cornerX = centerX - halfsize
					target.cornerX2 = centerX + halfsize
				)				
				target.cornerY2 = y
			)		
			3:
			(
				local x = (m.x-xDiff) / xSize
				if notBlowup then
				(
					if x < 0 do x = 0
					if x > cornerX2 do x = cornerX2
				)
				else
				(
					local centerY = target.cornerY + ((target.cornerY2-target.cornerY)/2)
					local halfsize = (target.cornerX2-x)/2.0
					target.cornerY = centerY - halfsize
					target.cornerY2 = centerY + halfsize
				)						
				target.cornerX = x
			)		
			4:
			(
				local width = cornerX2 - cornerX
				local height = cornerY2 - cornerY
				local x = (m.x-xDiff) / xSize
				local y = (m.y-yDiff) / ySize
				
				if notBlowup then
				(
					if x + width/2 > 1.0 do x = 1.0 - width/2
					if y + height/2 > 1.0 do y = 1.0 - height/2
					if x - width/2 < 0.0 do x = width/2
					if y - height/2 < 0.0 do y = height/2
				)
				
				target.cornerX = x-width/2
				target.cornerX2 = x+width/2
				target.cornerY = y-height /2
				target.cornerY2 = y+height /2
			)		
			5:
			(
				local x = (m.x-xDiff) / xSize
				local y = (m.y-yDiff) / ySize
				
				if notBlowup then
				(
					if x < 0 do x = 0
					if y < 0 do y = 0
					if x > cornerX2 do x = cornerX2
					if y > cornerY2 do y = cornerY2
				)
                else
                (
                    local width = cornerX2 - x
                    local height = cornerY2 - y
                    if width>height then
                    (
                        x = cornerX2 - height
                    )
                    else
                    (
                        y = cornerY2 - width
                    )
                )
				
				target.cornerX = x
				target.cornerY = y
			)
			6:
			(
				local x = (m.x-xDiff) / xSize
				local y = (m.y-yDiff) / ySize
				
				if notBlowup then
				(
					if x > 1.0 do x = 1.0
					if y < 0 do y = 0
					if x < cornerX do x = cornerX
					if y > cornerY2 do y = cornerY2
				)
				else
                (
                    local width = x- cornerX
                    local height = cornerY2 - y
                    if width>height then
                    (
                        x = cornerX + height
                    )
                    else
                    (
                        y = cornerY2 - width
                    )
                )
				target.cornerX2 = x
				target.cornerY = y
			)	
			7:
			(
				local x = (m.x-xDiff) / xSize
				local y = (m.y-yDiff) / ySize
				
				if notBlowup then
				(
					if x > 1.0 do x = 1.0
					if y > 1.0 do y = 1.0
					if x < cornerX do x = cornerX
					if y < cornerY do y = cornerY
				)
                else
                (
                    local width = x - cornerX
                    local height = y - cornerY
                    if width>height then
                    (
                        x = cornerX + height
                    )
                    else
                    (
                        y = cornerY + width
                    )
                )
				
				target.cornerX2 = x
				target.cornerY2 = y
			)	
			8:
			(
				local x = (m.x-xDiff) / xSize
				local y = (m.y-yDiff) / ySize
				
				if notBlowup then
				(
					if x < 0 do x = 0
					if y > 1.0 do y = 1.0
					if x > cornerX2 do x = cornerX2
					if y < cornerY do y = cornerY
				)
                else
                (
                    local width = cornerX2 - x 
                    local height = y - cornerY
                    if width>height then
                    (
                        x = cornerX2 - height
                    )
                    else
                    (
                        y = cornerY + width
                    )
                )
				
				target.cornerX = x
				target.cornerY2 = y
			)	
		)
		try
		(
			SMTD_RegionRendering.updateFromRegionGizmo()
		)catch()
		
	)
)
