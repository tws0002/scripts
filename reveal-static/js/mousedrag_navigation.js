var myviewer;

function zoomin() {
    temp = $j('section.present').children("img").panzoom("getTransform");
    ratio = parseFloat(temp.match(/\(([^)]+)\)/)[1].split(",")[0])
    z_in = ratio + 0.15;
    $j('section.present').children("img").panzoom('zoom', z_in);
}

function zoomout() {
    temp = $j('section.present').children("img").panzoom("getTransform");
    ratio = parseFloat(temp.match(/\(([^)]+)\)/)[1].split(",")[0])
    z_out = ratio - 0.15;
    $j('section.present').children("img").panzoom('zoom', z_out);
}

function contrast(){
    if($j('section').children("img").hasClass("contrast") == true){
        $j('section').children("img").removeClass("contrast");    
    }
    else {
        $j('section').children("img").addClass("contrast");
    }
}


function fitImage() {
    mview_url = $j('section.present').children('section.present.mview').attr('url');
    if(mview_url == null){    
        doc_w = $j(document).width();
        doc_h = window.innerHeight;
        img = vid = [];
        img = $j('section.present').children('img');
        vid = $j('section.present').children('video');
        if(img.length != 0) {
            element = img;
            img_w = element.prop('naturalWidth');
            img_h = element.prop('naturalHeight');
        } else {
            img = []
        }
        if(vid.length != 0) {
            element = vid;
            img_w = element.innerWidth();
            img_h = element.innerHeight();
            doc_h = doc_h - 100;
        } else {
            vid = []
        }
        
        var ratio;
        if((img_w/img_h) < (doc_w/doc_h)) {
            ratio = doc_h / img_h;    
        }
        else if((img_w/img_h) > (doc_w/doc_h)) {
            ratio = doc_w / img_w;
        }

        offset_h = img_h/2 - doc_h/2;
        if(img_w < doc_w) {
            offset_w = 0;
        }
        else {
            offset_w = img_w/2 - doc_w/2;
        }


        element.panzoom({
            minScale: 0,
        });

        element.panzoom('zoom', ratio);
        element.panzoom('pan', -offset_w, -offset_h);
        element.on('mousewheel.focal', function(e) {
            e.preventDefault();
            var delta = e.delta || e.originalEvent.wheelDelta;
            var zoomOut = delta ? delta < 0 : e.originalEvent.deltaY > 0;
            element.panzoom('zoom', zoomOut, {
              increment: 0.05,
              animate: false,
              focal: e,
            });
        });     
       $j(".present").css("overflow", "visible");
   }
}

function updateInfo() {
    project_name = $j('h3.title').text();
    project_name_chn = $j('h2.title').text();
    item_name = $j('section.present').children('div.item_title').text();
    item_name_chn = $j('section.present').children('div.item_title_chn').text();
    author = $j('section.present').children('section.present').children('div.item_author').text();
    date = $j('section.present').children('section.present').children('div.item_date').text();
    $j('div.info_project').text('');
    $j('div.info_project_chn').text('');
    $j('div.info_item').text('');
    $j('div.info_item_chn').text('');
    $j('div.info_author').text('');
    $j('div.info_date').text('');
    $j('div.info_project').append(project_name);
    $j('div.info_project_chn').append(project_name_chn);
    $j('div.info_item').append(item_name);
    $j('div.info_item_chn').append(item_name_chn);
    $j('div.info_author').append(author);
    $j('div.info_date').append(date);
}

function loadMarmoset() {
    mview_url = $j('section.present').children('section.present.mview').attr('url');
    if(mview_url != null){
        doc_w = $j(document).width();
        doc_h = window.innerHeight;
        setTimeout( function () {
            $j('section.present').children('section.mview').children('div.marmoset').empty();        
            
            mview_url = "/assets/" + mview_url;
            
            var myviewer = new marmoset.WebViewer( doc_w, doc_h, mview_url);
            $j('section.present.mview').children('div.marmoset').append(myviewer.domRoot);   
            $j('div.marmoset').children('div').children('canvas').css("left", 0);   
            myviewer.loadScene();

            $j('div#marmosetUI').children('text').css('bottom',65);
            logo = $j('div#marmosetUI').children('div')[5];
            controls = $j('div#marmosetUI').children('div')[6];
            $j(controls).css('right',35).css('top',125);
            $j(logo).remove();
            
        }, 0 );


        /*myviewer.onLoad = function() {console.log(mview_url);};*/


        //remove past or future mview, too heavy
        if ($j('section.past').children('section.mview').children('div.marmoset').children().length > 0){
            $j('section.past').children('section.mview').children('div.marmoset').empty();
        }

        else if ($j('section.future').children('section.mview').children('div.marmoset').children().length > 0){
            $j('section.future').children('section.mview').children('div.marmoset').empty();
        }    
    }
}

function updateCursor() {
    current = $j('div.slides').children('section.future').length;
    item_count = $j('div.slides').children('.section_top').length;
    child_count = $j('section.present').children('section').length - 1;
    cur_item_child_future_count = $j('section.present').children('section.future').length;
    right = left = up = down = 0;

    if(current == item_count){
        right = 1; //right
    } 

    else if(current == 0) {
        left = 1; //left
    }

    else {
        left = right = 1; //left + right
    }

    if(child_count == 0) { //no up down
    }
    else if(child_count > 0) {
        if(cur_item_child_future_count == 0) {
            up = 1; //up
        }
        else if(cur_item_child_future_count == child_count) {
            down = 1; //down
        }
        else {
            up = down = 1; //up + down
        }
    }

    if(left == 0 && right == 1 && up == 0 && down == 0) {
        $j('.navHint').children('img').attr('src','/assets/scripts/reveal-static/icons/right.png');
    }
    if(left == 1 && right == 0 && up == 0 && down == 0) {
        $j('.navHint').children('img').attr('src','/assets/scripts/reveal-static/icons/left.png');
    }
    if(left == 1 && right == 1 && up == 0 && down == 0) {
        $j('.navHint').children('img').attr('src','/assets/scripts/reveal-static/icons/left-right.png');
    }
    if(left == 1 && right == 1 && up == 1 && down == 0) {
        $j('.navHint').children('img').attr('src','/assets/scripts/reveal-static/icons/left-right-up.png');
    }
    if(left == 1 && right == 1 && up == 0 && down == 1) {
        $j('.navHint').children('img').attr('src','/assets/scripts/reveal-static/icons/left-right-down.png');
    }
    if(left == 1 && right == 0 && up == 1 && down == 0) {
        $j('.navHint').children('img').attr('src','/assets/scripts/reveal-static/icons/left-up.png');
    }
    if(left == 1 && right == 0 && up == 0 && down == 1) {
        $j('.navHint').children('img').attr('src','/assets/scripts/reveal-static/icons/left-down.png');
    }
    if(left == 1 && right == 1 && up == 1 && down == 1) {
        $j('.navHint').children('img').attr('src','/assets/scripts/reveal-static/icons/all.png');
    }
    if(left == 1 && right == 0 && up == 1 && down == 1) {
        $j('.navHint').children('img').attr('src','/assets/scripts/reveal-static/icons/left-up-down.png');
    }        
}

function touchControl() {
   $j(document).mousedown(function(e) { e.preventDefault(); pos=e.pageX; dragging = true })
    if($j('section.present.mview').length == 0){
        $j('.reveal').on('mousedown', function(e) {
            $j(this).data('p0', { x: e.pageX, y: e.pageY});
        }).on('mouseup', function(e) {
            if(e.which == 1) {
                var p0 = $j(this).data('p0'),
                    p1 = { x: e.pageX, y: e.pageY },
                    d = Math.sqrt(Math.pow(p1.x - p0.x, 2) + Math.pow(p1.y - p0.y, 2));

                x_diff = (p0.x - p1.x);
                y_diff = (p0.y - p1.y);
            
                if (Math.abs(x_diff) > Math.abs(y_diff) && Math.abs(x_diff) > 6) {
                    if (x_diff < 0) {
                        Reveal.left();    
                    }
                    else if (x_diff > 0) {
                        Reveal.right();
                    }
                }

                else if (Math.abs(y_diff) > Math.abs(x_diff) && Math.abs(y_diff) > 6) {
                    if (y_diff < 0) {
                        Reveal.up();    
                    }
                    else if (y_diff > 0) {
                        Reveal.down();
                    }
                }            
            }
        });
    }
    else{
        $j('.reveal').unbind();
    }
}

