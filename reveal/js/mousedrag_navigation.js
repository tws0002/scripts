    $j(document).mousedown(function(e) { e.preventDefault(); pos=e.pageX; dragging = true })


    $j('.reveal').on('mousedown', function(e) {
        $j(this).data('p0', { x: e.pageX, y: e.pageY });
    }).on('mouseup', function(e) {
        var p0 = $j(this).data('p0'),
            p1 = { x: e.pageX, y: e.pageY },
            d = Math.sqrt(Math.pow(p1.x - p0.x, 2) + Math.pow(p1.y - p0.y, 2));

        x_diff = (p0.x - p1.x);
        y_diff = (p0.y - p1.y);
        console.log(x_diff, y_diff);
        if (x_diff < 6) {
        }
        else if (Math.abs(x_diff) > Math.abs(y_diff)) {
            Reveal.configure({loop: true, transition: "convex", backgroundTransition: "convex"});
            if (x_diff < 0) {
                Reveal.right();    
            }
            if (x_diff > 0) {
                Reveal.left();
            }
        }

        else if (Math.abs(x_diff) < Math.abs(y_diff)) {
            Reveal.configure({loop: true, transition: "zoom", backgroundTransition: "zoom"});
            if (y_diff < 0) {
                Reveal.left();    
            }
            else if (y_diff > 0) {
                Reveal.right();
            }
        }
    })



