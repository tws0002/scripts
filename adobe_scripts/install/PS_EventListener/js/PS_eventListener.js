(function () {
    'use strict';
 
    var csInterface = new CSInterface();   
 
    function Register(inOn) {
 
        if (inOn) {
            var event = new CSEvent("com.adobe.PhotoshopRegisterEvent", "APPLICATION");
        } else {
            var event = new CSEvent("com.adobe.PhotoshopUnRegisterEvent", "APPLICATION");
        }
        event.extensionId = "com.example.psevents";
 
        // some events:
        // 1668247673 = charIDToTypeID( "copy" ) = copy
        // 1885434740 = charIDToTypeID( "past" ) = paste
        // 1668641824 = charIDToTypeID( "cut " ) = cut
        event.data = "1668247673, 1885434740, 1668641824";
        csInterface.dispatchEvent(event);
    }
 
    function init() {
 
       // Switch onChange callback
        $('#registerEvent').change(function() {
            Register( $(this).is(':checked') ); // true or false
        });
    }
 
    function PSCallback(csEvent) {
        var dataArray = csEvent.data.split(",");
        // send to JSX to convert typeIDs to stringIDs
        csInterface.evalScript('convertTypeID(' + JSON.stringify(dataArray[0]) + ')', function(res) {
            $('#result').val(res.toString());
        });
    }
 
    init();
    csInterface.addEventListener("PhotoshopCallback", PSCallback);
 
}());