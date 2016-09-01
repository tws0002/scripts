global SMTD_TilesRendering

plugin simpleManipulator DLTileManipulator
    name:"TileManip"
    classID:#(0x7c427c83, 0xc28852e)
    category:"Manipulators"
	invisible:true
(
    local greenColor =  colorMan.getColor #manipulatorsActive
    local redColor =    colorMan.getColor #manipulatorsSelected
    local yellowColor = colorMan.getColor #manipulatorsInactive

    parameters main rollout:paramRollout
    ( 
		tilesX type:#integer animatable:false ui:spn_tilesX default:2
		tilesY type:#integer animatable:false ui:spn_tilesY default:2
    )

    rollout paramRollout "Tiles"
    (
        Spinner  spn_tilesX   "TilesX:"       range:[1,1000,2]  type:#integer
        Spinner  spn_tilesY   "TilesY:"       range:[1,1000,2]  type:#integer
    )

    on canManipulate target  return (classOf target) == DLTileManipulator

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
        if (target != undefined) then 
        (
           this.tilesX = target.tilesX 
           this.tilesY = target.tilesY
           unselColor  = greenColor
        ) 
        else
        (
           unselColor  = yellowColor
        )

        -- These flags are used for all the gizmos
        local flags = (gizmoUseScreenSpace + gizmoActiveViewportOnly + gizmoDontHitTest)

--		this.addGizmoMarker #diamond [gw.getWinSizeX()*0.5,0.5*gw.getWinSizeY(),0.0] flags unselColor redColor
		
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

		local XFactor = (xSize as float /tilesX ) 
		local YFactor = (ySize as float /tilesY ) 
		for x = xDiff to xSize+xDiff by XFactor  do
		(
	        local giz = manip.makeGizmoShape()
			giz.AddPoint [x,yDiff,0]
	        giz.AddPoint [x,ySize+yDiff ,0]
	        this.addGizmoShape giz flags unselColor redColor
		)		
		for y = yDiff to ySize+yDiff by YFactor do
		(
	        local giz = manip.makeGizmoShape()
			giz.AddPoint [xDiff,y,0]
	        giz.AddPoint [xSize+xDiff ,y,0]
	        this.addGizmoShape giz flags unselColor redColor
		)		
        -- return an empty string so no tool tip is displayed
        return ""
    )

    -- mouseMove is called on every mouse move when dragging the manip
    -- It needs to convert the mouse position 'm' into a new value for the slider
    on mouseMove m which do
    (

    )

    on mouseDown m which do
    (
      -- Toggle the value of the "Hide" state
      --if (which == 1) then target.hide = not hide 
    )
)
