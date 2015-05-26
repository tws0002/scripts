Render View Extension 1.99


Render View button modifications and extended functionality: 

- Both "Render Frame" and "IPR Render" buttons are modified to have a camera selection popup menu when clicking with the right mouse button.
- The scene preparation and render time is displayed at the bottom of the renderView After rendering a frame.
- A new Snapshot button added, with the usual right button camera selection menu.
- Render Diagnostics button is removed since it is in the upper menu and it's a rarely used tool. (And we need space for panel mode. :)
- Color button is extended with a right click menu for all the available display types. (Color/Alpha/R/G/B/Luminance)
- Alpha button removed. Now left clicking the Color button toggles color and alpha channel display.
- Right clicking on the Render Globals button brings up a menu to set things without opening the clumsy Render Globals Window:
	Raytracing on/off
	Render All / Selected only (+ an option for automatic selection for rendering)
	Render Quality (Containing user presets)
	Motion Blur (off/2d/3d)
	Render options (Use Default Light on/off, Depth-Map Shadows,  Composite (No premultiply), Paint Effects render,  Oversample Paint Effects
	Turn All Image Planes on/off (either at once or only at render time)
	Select Active (renderable) Camera and set Output Channels (Color/Alpha/Depth)
	Image Format (including user defined image formats if there is any defined in the userImageFormats.mel)
    + in case of Mental Ray:
	Final Gathering, Global Illumination, Caustics, Displacement, Shadows on/off
	
	Approximation editing: create, assign and edit approximations from the render view. 
	(Works with any number and any type of selected objects)
	Image based lighting node cration and selection
	Custom text creation and manipulation
	Translation Verbosity
	When choosing a different MR render quality preset switches like raytracing and FG remain the same (only the values change).

- Framestore button:
	Set Render-info display - GUI to set what kind of information should be displayed in the bottom of the RenderView
	Open the mayaImageTool Window - GUI to modify image names, check and compare rendered data, save images, add comments.
	Auto-open the mayaImageTool window - Checkbox to automatically open the mIT window after every render.

	Add note to rendered image - Renders user defined information on the bottom of the image.
	(Date is added as Year/Month/Day)
	Save kept images to disk - Option box lets you define a specific filename instead of the current image name set in the render globals.)
	Load previously saved images from disk
	Delete previously saved images from disk
	Remove all images from RenderView 

- Preview Resolution button to quickly display and modify the test resoluion.
- Ray Tracing On/Off button that displays the current state of raytracing.
  Right clicking this button brings up a new marking menu to set Mental Ray sampling parameters directly, like
  easily multiply/divide all the sampling contrast values together.

- The Renderer selection menu has new menuitems to load the currently unloaded renderers.

- Exposure slider. Right click menu allows setting the default value.

Render Utilites (a new menu in the renderView):

- "Render Multiple Frames" lets you render any number of different images (or image region) 
into the Render View or directly to disk. You can generate sequences based on start frame/end frame/step count 
or add frames manually and assign a new camera to any frame. 
(This camera will be used until you define a new one in the list.)
You can easily render many frames using different cameras for preview, check animation key positions
or render a whole animation within Maya. (This is slower than batch mode but it can fix render 
problems that are known to happen sometimes while using mayabatch. :)
Read button annotations for further details.

- "Display Mental Ray Tesselation" renders the wireframe image of the selected object(s). This feature displays 
the effect of the currently assigned approximations. The render uses the current resolution with min=max=0 sampling,
and the basic mental ray contour calculation method to avoid installing custom shaders.


How to use the scripts:
	- Copy the mayaversion/renderWindowPanel.mel, /mayaPreviewRender.mel, /mentalrayPreviewRender.mel and 
	sz_renderView.mel script files into a script directory before starting Maya. The list of the current script directories 
	can be queried using the following mel command: getenv "MAYA_SCRIPT_PATH";
	(I don't recommend overwriting the original files that you find in the "Maya/scripts/others directory".)
	
	If you encounter an error of only the script editor appearing after installing the script and starting Maya, you 
	probably put the sz_renderview.mel file into the wrong place.
	
	- Copy the icon files from the Icons directory to a Maya Icon folder (the default is "user dir/my documents/maya/version/prefs/icons")
	The list of the current icon directories can be queried using the following mel command: getenv XBMLANGPATH;
	(Linux and OSX requires xpm files to work properly.)

	- Starting with Maya 2011 icon files will are cross platform, using the PNG image format.


Modifications:

1.99 - News:
		- Maya 2013, 2014, 2015 support.
		- Beware: Maya 2014 and 2015 support is quite experimental, I haven't used the script a lot with these releases.
1.98 - News:
		- Maya 2011 compatibility (2010 is skipped since its simply 2009 repackaged).
		- Exposure slider for Maya 2011.
		- Icons converted to png for Maya 2011.
1.9 - News:
		- Maya 2009 compatibility and slight changes in the render globals and render quality popup menus.
1.8 - News:
		- Maya 2008 compatibility (and dropped support for Maya versions 6.0 and 6.5. Time flies.)
		- New items in the mental ray render quality marking menu: rasterizer parameters and adaptive sampling presets.
		- Ability to flip between two images from the MIT window for easier image comparison.
		- Rasterizer sampling settings (samples collect and shading quality) are stored in the image info instead of min/max.
		- Custom text creation GUI changes.
		- Render verbosity change (from the render globals right click menu) works again with 8.5 and above.
		- Menuitem to match the current frame to the displayed image of the renderView from the `right click on image` popup menu.
		- Renders now store the mental ray render log into a file that is avaible from the right-click menu of the image,
		and the render log display window has some useful filtering options to simplify issue tracking and analysis.
		Stored render logs are also kept and managed when keeping and removing an image from the stack.
		Because of an obscure maya bug this feature makes the mr output disappear from the output window. For the moment you 
		have to choose between using a cool window with search capabilities or the old school but permanent output window...
		(To use the logging feature with standalone rendering redirect the standard error output of the ray executable into a file
		named mentalray.log in the user temp directory.)
	Bugfix:
		- There was an issue with image removal with Maya 8.5 (two images were removed not just the selected one).
		- Preview resolution icon was incorrectly initialized and reported a different size at startup.
		- When nothing was selected in the render info window the script did not display the original Maya information.
1.7 - News:
	  - Maya 8.5 compatibility.
	  - Mental ray approximation GUI changes:
	  	- Approximation connected to the selected object is displayed bold.
	  	- New approximation can be automatically assigned to selection by using the option box.
	  	- Objects connected to an approximation can be easily selected.
		- A type of approximation can be removed from all selected objects.
1.6 - News:
	  - Maya 8 compatibility.
	  - New MR related features: 
		- Custom text creation / connect / disconnect / select / delete.
	  	- IBL node creation / selection.
	  	- "Use rapid scanline for motion blur" switch to automatically enable rapid mode when motion blur mode is changed.
	  	- Show all approximation node (for the selected type) in Attribute SpreadSheet for easier modification.
	  	- Scanline mode setting in the MR quality marking menu (right click on the raytrace icon).
	  	- The "Add note" feature now uses the current render info data by default.
	  	- Icon changes! After 4 years gotta have to streamline the look! :)
	  - mrLiquid IPR options from the right-click menu: standard / progressive mode, pause / continue.
	  Bugfix:
	  - Some internal script changes, optimizations. Hope I did not break anything... :)
	  - Preview resolution menu was fooled by fractional pixel values and sometimes did not mark the current size correctly.
1.5 - News:
	  - Finally Maya 7 compatible. It was really annoying to get it working since Maya 7 had some of the script's
	  functionality, usually implemented in a completely different way. Maya 7 requires a modified version of Alias'
	  mayaPreviewRender.mel that handles the multi-layer render commands. (The file is in the same directory as renderWindowPanel.mel)
	  - The current render layer is also added to the stored render data list.
	  - A new option box for "Render selected" lets you define objects that are selected automatically when "Render selected objects only"
	  is enabled. (The original selection is reset after rendering.)
	  - Gonzalo Garramuno's mrLiquid plugin is treated as the mentalRay plugin by the script. You never know... :) 
	 Bugfix:
	  - The Render Globals window was put offscreen when opening the Maya software globals 
	  menu to avoid window popping. This turned out to work really badly so it is now removed.
	  - The "Display Mental Ray Tesselation" feature was modified to use a simpler solution.
1.4 - News:
      - Every render stores some information about the render process and image quality: filename, frame, camera,
      date&time, resolution, renderer, rendertime, sampling (min, max, contrast), filter (type, width, height),
      for both Maya Software and Mental Ray renders. (Maya Hardware has limited support.)
      - The user can choose the data that is to be displayed for the images using the "Set render-info display"
      menuitem in the framestore menu.
      - The mayaImageTool window is a new GUI to compare rendered data and images. And user comments can be added
      to the data that is displayed at the bottom of the renderView.
      - The script now works with linux (and hopefully OSX) and has XPM icons too. Many thanks to Mike Eheler to test the OS-related features.
1.3 - News:
      - The IPR button has a new "Enable / Disable raytracing" option when using Mental Ray.
      - Custom render quality presets are now added to the quality list.
      - "Dispay Mental Ray Tesselation" utility to render the wireframe of selected objects. Read details above.
      - The button that used to turn raytracing on/off is extended with a right click marking menu to quickly change
      Mental Ray sampling parameters (Min/Max/Contrast threshold, Time Contrast) and Final Gather ray count.
      - "Add note" now works with images already stored in the framestore. (The selected image is put to the first place, without overwriting
      the current unsaved image.)
      - The framestore load and delete functions open a submenu to display the currently available files on disk.
      Bugfix:
      - "Add note" now surely deletes shading groups too (not just the shader), and works before the HyperShade is opened first.
      - "Render multiple frames" now handles fractional frame values properly; display the frames' progression
      and is interruptible by hitting the ESC button.
      - The render buttons now work with all of the default renderers in 5.0 and 6.0 too.
      - MR quality nodes are created before the menuitems are displayed.
      - The Utilities menu is now displayed in the right-click popup menu too.
      - MayaMan features dropped. If anyone requests it I get it working again.
1.2 - News:
      - "Add note to rendered image" lets you write information about the picture directly onto the image.
      - Both the Famestore menu and the Preview Resolution menu changed from left click to right click, to be
      more consistent with the basic maya workflow. 
      - Preview Resolution menu marks the current resolution.      
      Many Maya 5.0 related bugfixes:
      - Render region, render time, camera change, image format change with mr, mr quality.
      - Using auto-render region displays render time properly.
      - The camera popup menu's checkboxes mark the current camera (in the renderView) and not the one set to renderable.
1.1 - News:
      - New Render Utilities menu with "Smooth at Rendertime" and "Render Multiple Frames" utilities.
      Bugfix:
      - The popup camera list now works ok with lights parented to cameras, small additions and changes.
1.0 - First normal release
0.5 - Test release



Advices, comments, bug-fixes and great new ideas are welcome.
Use script at your own risk, as always.


Horvátth Szabolcs
szabolcs@impresszio.hu | www.impresszio.hu/szabolcs
2014.12.01