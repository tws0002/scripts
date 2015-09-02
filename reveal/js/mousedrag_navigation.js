(function ( $ ) {
    $(document).mousedown(function(e) { e.preventDefault(); pos=e.pageX; dragging = true })

    $('.reveal').on('mousedown', function(e) {
        $(this).data('p0', { x: e.pageX, y: e.pageY});
    }).on('mouseup', function(e) {
        if(e.which == 1) {
            var p0 = $(this).data('p0'),
                p1 = { x: e.pageX, y: e.pageY },
                d = Math.sqrt(Math.pow(p1.x - p0.x, 2) + Math.pow(p1.y - p0.y, 2));

            x_diff = (p0.x - p1.x);
            y_diff = (p0.y - p1.y);
        
            if (Math.abs(x_diff) > Math.abs(y_diff) && Math.abs(x_diff) > 6) {
                console.log(x_diff);
                if (x_diff < 0) {
                    Reveal.left();    
                }
                else if (x_diff > 0) {
                    Reveal.right();
                }
            }
        }
    });

    // leftIsDragging   = false;
    // middleIsDragging = false;
    // rightIsDragging  = false;  
    // p0 = 0;
    // $(document).bind('mousedown', function(event) {
    //     if(event.which == 1) {
    //         leftIsDragging   = true;
    //         p0 = event.pageY;

    //     }
    // });

    // $(document).bind('mouseup', function(event) {
    //     if(event.which == 1) {
    //         leftIsDragging   = false;
    //     }
    // });

    // $(document).bind('mousemove', function(event) {
    //     if (leftIsDragging) 
    //     {
    //         doc_w = $(document).width();
    //         doc_h = window.innerHeight;

    //         img_w = $('section.present').children("img").prop('naturalWidth');
    //         img_h = $('section.present').children("img").prop('naturalHeight');
            
    //         var default_ratio;
    //         if((img_w/img_h) < (doc_w/doc_h)) {
    //             default_ratio = doc_h / img_h;    
    //         }
    //         else if((img_w/img_h) > (doc_w/doc_h)) {
    //             default_ratio = doc_w / img_w;
    //         }        
    //         p1 = event.pageY;
    //         diff = (p0 - p1);
    //         temp = $('section.present').children("img").panzoom("getTransform");
    //         ratio = parseFloat(temp.match(/\(([^)]+)\)/)[1].split(",")[0])
    //         zoomOut = Math.max(ratio + diff/50000, default_ratio/1.1);
    //         $('section.present').children("img").panzoom('zoom', zoomOut, { silent: true });   
    //     }
    // });
}( jQuery ));