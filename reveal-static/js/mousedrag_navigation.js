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
    var mview_url = $j('section.present').children('section.present.mview').attr('url');
    var mp3_url = $j('section.present').children('section.present.mp3').attr('url');
    if(mview_url == null && mp3_url == null){
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

function playButton(){
    var current_slide = $j('section.present').children('section.present');
    var play_button = $j(current_slide).find('div.center-button#play-button');
    if($j(play_button).hasClass('on')){
        $j(play_button).removeClass('on').addClass('off');
        $j(play_button).children('awe.fa-play').removeClass('fa-play').addClass('fa-pause');
    } else if($j(play_button).hasClass('off')) {
        $j(play_button).removeClass('off').addClass('on');
        $j(play_button).children('awe.fa-pause').removeClass('fa-pause').addClass('fa-play');
    }
}

function loopButton(){
    var current_slide = $j('section.present').children('section.present');
    var loop_button = $j(current_slide).find('div.center-button#loop-button');
    var repeat = $j(loop_button).hasClass('on');
    if(repeat == true){
        $j(loop_button).removeClass('on').addClass('off');
        $j(loop_button).find('awe.btn_off').removeClass('btn_off').addClass('btn_on');
    } else if(repeat == false){
        $j(loop_button).removeClass('off').addClass('on');
        $j(loop_button).find('awe.btn_on').removeClass('btn_on').addClass('btn_off');
    }
}

function stopButton(){
    var current_slide = $j('section.present').children('section.present');
    var play_button = $j(current_slide).find('div.center-button#play-button');
    if($j(play_button).hasClass('on')){
        $j(play_button).removeClass('off').addClass('on');
        $j(play_button).children('awe.fa-pause').removeClass('fa-pause').addClass('fa-play');
    }
}

function resetWaveSurfer(){
    wavesurfer.un('finish');
    wavesurfer.un('ready');
    wavesurfer.unAll();
    wavesurfer.destroy();
}

function formatTime(time){
    time = Math.round(time);
    var minutes = Math.floor(time / 60),
        seconds = time - minutes * 60;
    seconds = seconds < 10 ? '0' + seconds : seconds;
    return minutes + ":" + seconds;
}

var wavesurfer;
function loadMp3() {
    if (wavesurfer){
        resetWaveSurfer();
    }
    var timer = 0;
    var current_slide = $j('section.present').children('section.present');
    var mp3_url = $j('section.present').children('section.present.mp3').attr('url');
    if(mp3_url){
        var current_container = $j(current_slide).find('#waveform');
        wavesurfer = WaveSurfer.create({
            container: current_container[0],
            cursorColor: '#6BC19E',
            cursorWidth: 2,
            height: 75,
            waveColor: '#547992',
            progressColor: '#579E81',
            interact: true,
            splitChannels: true
        });
        wavesurfer.load(mp3_url);

        var play_button = $j(current_slide).find('div.center-button#play-button');
        var loop_button = $j(current_slide).find('div.center-button#loop-button');

        wavesurfer.on('finish', function () {
            var repeat = $j(loop_button).hasClass('on');
            if (repeat == false) {
                $j(play_button).removeClass('off').addClass('on');
                $j(play_button).children('awe.fa-pause').removeClass('fa-pause').addClass('fa-play');
                wavesurfer.stop();
            }
            else if (repeat == true) {
                wavesurfer.play();
            }
        });

        wavesurfer.on('ready', function () {
            var duration = wavesurfer.getDuration();
            $j(current_slide).find('span#current').text('0:00');
            $j(current_slide).find('span#total').text(formatTime(duration));

            clearInterval(timer);
            timer = setInterval(function() {
                $j(current_slide).find('#current').text(formatTime(wavesurfer.getCurrentTime()));
            }, 1000);
        });
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
    if($j('section.present.mview').length == 0 || $j('section.present.mp3').length == 0){
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

;window.Modernizr=function(a,b,c){function x(a){j.cssText=a}function y(a,b){return x(prefixes.join(a+";")+(b||""))}function z(a,b){return typeof a===b}function A(a,b){return!!~(""+a).indexOf(b)}function B(a,b){for(var d in a){var e=a[d];if(!A(e,"-")&&j[e]!==c)return b=="pfx"?e:!0}return!1}function C(a,b,d){for(var e in a){var f=b[a[e]];if(f!==c)return d===!1?a[e]:z(f,"function")?f.bind(d||b):f}return!1}function D(a,b,c){var d=a.charAt(0).toUpperCase()+a.slice(1),e=(a+" "+n.join(d+" ")+d).split(" ");return z(b,"string")||z(b,"undefined")?B(e,b):(e=(a+" "+o.join(d+" ")+d).split(" "),C(e,b,c))}var d="2.6.2",e={},f=!0,g=b.documentElement,h="modernizr",i=b.createElement(h),j=i.style,k,l={}.toString,m="Webkit Moz O ms",n=m.split(" "),o=m.toLowerCase().split(" "),p={},q={},r={},s=[],t=s.slice,u,v={}.hasOwnProperty,w;!z(v,"undefined")&&!z(v.call,"undefined")?w=function(a,b){return v.call(a,b)}:w=function(a,b){return b in a&&z(a.constructor.prototype[b],"undefined")},Function.prototype.bind||(Function.prototype.bind=function(b){var c=this;if(typeof c!="function")throw new TypeError;var d=t.call(arguments,1),e=function(){if(this instanceof e){var a=function(){};a.prototype=c.prototype;var f=new a,g=c.apply(f,d.concat(t.call(arguments)));return Object(g)===g?g:f}return c.apply(b,d.concat(t.call(arguments)))};return e}),p.csstransitions=function(){return D("transition")};for(var E in p)w(p,E)&&(u=E.toLowerCase(),e[u]=p[E](),s.push((e[u]?"":"no-")+u));return e.addTest=function(a,b){if(typeof a=="object")for(var d in a)w(a,d)&&e.addTest(d,a[d]);else{a=a.toLowerCase();if(e[a]!==c)return e;b=typeof b=="function"?b():b,typeof f!="undefined"&&f&&(g.className+=" "+(b?"":"no-")+a),e[a]=b}return e},x(""),i=k=null,function(a,b){function k(a,b){var c=a.createElement("p"),d=a.getElementsByTagName("head")[0]||a.documentElement;return c.innerHTML="x<style>"+b+"</style>",d.insertBefore(c.lastChild,d.firstChild)}function l(){var a=r.elements;return typeof a=="string"?a.split(" "):a}function m(a){var b=i[a[g]];return b||(b={},h++,a[g]=h,i[h]=b),b}function n(a,c,f){c||(c=b);if(j)return c.createElement(a);f||(f=m(c));var g;return f.cache[a]?g=f.cache[a].cloneNode():e.test(a)?g=(f.cache[a]=f.createElem(a)).cloneNode():g=f.createElem(a),g.canHaveChildren&&!d.test(a)?f.frag.appendChild(g):g}function o(a,c){a||(a=b);if(j)return a.createDocumentFragment();c=c||m(a);var d=c.frag.cloneNode(),e=0,f=l(),g=f.length;for(;e<g;e++)d.createElement(f[e]);return d}function p(a,b){b.cache||(b.cache={},b.createElem=a.createElement,b.createFrag=a.createDocumentFragment,b.frag=b.createFrag()),a.createElement=function(c){return r.shivMethods?n(c,a,b):b.createElem(c)},a.createDocumentFragment=Function("h,f","return function(){var n=f.cloneNode(),c=n.createElement;h.shivMethods&&("+l().join().replace(/\w+/g,function(a){return b.createElem(a),b.frag.createElement(a),'c("'+a+'")'})+");return n}")(r,b.frag)}function q(a){a||(a=b);var c=m(a);return r.shivCSS&&!f&&!c.hasCSS&&(c.hasCSS=!!k(a,"article,aside,figcaption,figure,footer,header,hgroup,nav,section{display:block}mark{background:#FF0;color:#000}")),j||p(a,c),a}var c=a.html5||{},d=/^<|^(?:button|map|select|textarea|object|iframe|option|optgroup)$/i,e=/^(?:a|b|code|div|fieldset|h1|h2|h3|h4|h5|h6|i|label|li|ol|p|q|span|strong|style|table|tbody|td|th|tr|ul)$/i,f,g="_html5shiv",h=0,i={},j;(function(){try{var a=b.createElement("a");a.innerHTML="<xyz></xyz>",f="hidden"in a,j=a.childNodes.length==1||function(){b.createElement("a");var a=b.createDocumentFragment();return typeof a.cloneNode=="undefined"||typeof a.createDocumentFragment=="undefined"||typeof a.createElement=="undefined"}()}catch(c){f=!0,j=!0}})();var r={elements:c.elements||"abbr article aside audio bdi canvas data datalist details figcaption figure footer header hgroup mark meter nav output progress section summary time video",shivCSS:c.shivCSS!==!1,supportsUnknownElements:j,shivMethods:c.shivMethods!==!1,type:"default",shivDocument:q,createElement:n,createDocumentFragment:o};a.html5=r,q(b)}(this,b),e._version=d,e._domPrefixes=o,e._cssomPrefixes=n,e.testProp=function(a){return B([a])},e.testAllProps=D,g.className=g.className.replace(/(^|\s)no-js(\s|$)/,"$1$2")+(f?" js "+s.join(" "):""),e}(this,this.document),function(a,b,c){function d(a){return"[object Function]"==o.call(a)}function e(a){return"string"==typeof a}function f(){}function g(a){return!a||"loaded"==a||"complete"==a||"uninitialized"==a}function h(){var a=p.shift();q=1,a?a.t?m(function(){("c"==a.t?B.injectCss:B.injectJs)(a.s,0,a.a,a.x,a.e,1)},0):(a(),h()):q=0}function i(a,c,d,e,f,i,j){function k(b){if(!o&&g(l.readyState)&&(u.r=o=1,!q&&h(),l.onload=l.onreadystatechange=null,b)){"img"!=a&&m(function(){t.removeChild(l)},50);for(var d in y[c])y[c].hasOwnProperty(d)&&y[c][d].onload()}}var j=j||B.errorTimeout,l=b.createElement(a),o=0,r=0,u={t:d,s:c,e:f,a:i,x:j};1===y[c]&&(r=1,y[c]=[]),"object"==a?l.data=c:(l.src=c,l.type=a),l.width=l.height="0",l.onerror=l.onload=l.onreadystatechange=function(){k.call(this,r)},p.splice(e,0,u),"img"!=a&&(r||2===y[c]?(t.insertBefore(l,s?null:n),m(k,j)):y[c].push(l))}function j(a,b,c,d,f){return q=0,b=b||"j",e(a)?i("c"==b?v:u,a,b,this.i++,c,d,f):(p.splice(this.i++,0,a),1==p.length&&h()),this}function k(){var a=B;return a.loader={load:j,i:0},a}var l=b.documentElement,m=a.setTimeout,n=b.getElementsByTagName("script")[0],o={}.toString,p=[],q=0,r="MozAppearance"in l.style,s=r&&!!b.createRange().compareNode,t=s?l:n.parentNode,l=a.opera&&"[object Opera]"==o.call(a.opera),l=!!b.attachEvent&&!l,u=r?"object":l?"script":"img",v=l?"script":u,w=Array.isArray||function(a){return"[object Array]"==o.call(a)},x=[],y={},z={timeout:function(a,b){return b.length&&(a.timeout=b[0]),a}},A,B;B=function(a){function b(a){var a=a.split("!"),b=x.length,c=a.pop(),d=a.length,c={url:c,origUrl:c,prefixes:a},e,f,g;for(f=0;f<d;f++)g=a[f].split("="),(e=z[g.shift()])&&(c=e(c,g));for(f=0;f<b;f++)c=x[f](c);return c}function g(a,e,f,g,h){var i=b(a),j=i.autoCallback;i.url.split(".").pop().split("?").shift(),i.bypass||(e&&(e=d(e)?e:e[a]||e[g]||e[a.split("/").pop().split("?")[0]]),i.instead?i.instead(a,e,f,g,h):(y[i.url]?i.noexec=!0:y[i.url]=1,f.load(i.url,i.forceCSS||!i.forceJS&&"css"==i.url.split(".").pop().split("?").shift()?"c":c,i.noexec,i.attrs,i.timeout),(d(e)||d(j))&&f.load(function(){k(),e&&e(i.origUrl,h,g),j&&j(i.origUrl,h,g),y[i.url]=2})))}function h(a,b){function c(a,c){if(a){if(e(a))c||(j=function(){var a=[].slice.call(arguments);k.apply(this,a),l()}),g(a,j,b,0,h);else if(Object(a)===a)for(n in m=function(){var b=0,c;for(c in a)a.hasOwnProperty(c)&&b++;return b}(),a)a.hasOwnProperty(n)&&(!c&&!--m&&(d(j)?j=function(){var a=[].slice.call(arguments);k.apply(this,a),l()}:j[n]=function(a){return function(){var b=[].slice.call(arguments);a&&a.apply(this,b),l()}}(k[n])),g(a[n],j,b,n,h))}else!c&&l()}var h=!!a.test,i=a.load||a.both,j=a.callback||f,k=j,l=a.complete||f,m,n;c(h?a.yep:a.nope,!!i),i&&c(i)}var i,j,l=this.yepnope.loader;if(e(a))g(a,0,l,0);else if(w(a))for(i=0;i<a.length;i++)j=a[i],e(j)?g(j,0,l,0):w(j)?B(j):Object(j)===j&&h(j,l);else Object(a)===a&&h(a,l)},B.addPrefix=function(a,b){z[a]=b},B.addFilter=function(a){x.push(a)},B.errorTimeout=1e4,null==b.readyState&&b.addEventListener&&(b.readyState="loading",b.addEventListener("DOMContentLoaded",A=function(){b.removeEventListener("DOMContentLoaded",A,0),b.readyState="complete"},0)),a.yepnope=k(),a.yepnope.executeStack=h,a.yepnope.injectJs=function(a,c,d,e,i,j){var k=b.createElement("script"),l,o,e=e||B.errorTimeout;k.src=a;for(o in d)k.setAttribute(o,d[o]);c=j?h:c||f,k.onreadystatechange=k.onload=function(){!l&&g(k.readyState)&&(l=1,c(),k.onload=k.onreadystatechange=null)},m(function(){l||(l=1,c(1))},e),i?k.onload():n.parentNode.insertBefore(k,n)},a.yepnope.injectCss=function(a,c,d,e,g,i){var e=b.createElement("link"),j,c=i?h:c||f;e.href=a,e.rel="stylesheet",e.type="text/css";for(j in d)e.setAttribute(j,d[j]);g||(n.parentNode.insertBefore(e,n),m(c,0))}}(this,document),Modernizr.load=function(){yepnope.apply(window,[].slice.call(arguments,0))};

/**
 * jquery.hoverdir.js v1.1.0
 * http://www.codrops.com
 *
 * Licensed under the MIT license.
 * http://www.opensource.org/licenses/mit-license.php
 *
 * Copyright 2012, Codrops
 * http://www.codrops.com
 */
;( function( $, window, undefined ) {

    'use strict';

    $.HoverDir = function( options, element ) {

        this.$el = $( element );
        this._init( options );

    };

    // the options
    $.HoverDir.defaults = {
        speed : 300,
        easing : 'ease',
        hoverDelay : 0,
        inverse : false
    };

    $.HoverDir.prototype = {

        _init : function( options ) {

            // options
            this.options = $.extend( true, {}, $.HoverDir.defaults, options );
            // transition properties
            this.transitionProp = 'all ' + this.options.speed + 'ms ' + this.options.easing;
            // support for CSS transitions
            this.support = Modernizr.csstransitions;
            // load the events
            this._loadEvents();

        },
        _loadEvents : function() {

            var self = this;

            this.$el.on( 'mouseenter.hoverdir, mouseleave.hoverdir', function( event ) {

                var $el = $( this ),
                    $hoverElem = $el.find( 'div' ),
                    direction = self._getDir( $el, { x : event.pageX, y : event.pageY } ),
                    styleCSS = self._getStyle( direction );

                if( event.type === 'mouseenter' ) {

                    $hoverElem.hide().css( styleCSS.from );
                    clearTimeout( self.tmhover );

                    self.tmhover = setTimeout( function() {

                        $hoverElem.show( 0, function() {

                            var $el = $( this );
                            if( self.support ) {
                                $el.css( 'transition', self.transitionProp );
                            }
                            self._applyAnimation( $el, styleCSS.to, self.options.speed );

                        } );


                    }, self.options.hoverDelay );

                }
                else {

                    if( self.support ) {
                        $hoverElem.css( 'transition', self.transitionProp );
                    }
                    clearTimeout( self.tmhover );
                    self._applyAnimation( $hoverElem, styleCSS.from, self.options.speed );

                }

            } );

        },
        // credits : http://stackoverflow.com/a/3647634
        _getDir : function( $el, coordinates ) {

            // the width and height of the current div
            var w = $el.width(),
                h = $el.height(),


                // calculate the x and y to get an angle to the center of the div from that x and y.
                // gets the x value relative to the center of the DIV and "normalize" it
                x = ( coordinates.x - $el.offset().left - ( w/2 )) * ( w > h ? ( h/w ) : 1 ),
                y = ( coordinates.y - $el.offset().top  - ( h/2 )) * ( h > w ? ( w/h ) : 1 ),

                // the angle and the direction from where the mouse came in/went out clockwise (TRBL=0123);
                // first calculate the angle of the point,
                // add 180 deg to get rid of the negative values
                // divide by 90 to get the quadrant
                // add 3 and do a modulo by 4  to shift the quadrants to a proper clockwise TRBL (top/right/bottom/left) **/
                direction = Math.round( ( ( ( Math.atan2(y, x) * (180 / Math.PI) ) + 180 ) / 90 ) + 3 ) % 4;
            return direction;

        },
        _getStyle : function( direction ) {

            var fromStyle, toStyle,
                slideFromTop = { left : '0px', top : '-100%' },
                slideFromBottom = { left : '0px', top : '100%' },
                slideFromLeft = { left : '-100%', top : '0px' },
                slideFromRight = { left : '100%', top : '0px' },
                slideTop = { top : '0px' },
                slideLeft = { left : '0px' };

            switch( direction ) {
                case 0:
                    // from top
                    fromStyle = !this.options.inverse ? slideFromTop : slideFromBottom;
                    toStyle = slideTop;
                    break;
                case 1:
                    // from right
                    fromStyle = !this.options.inverse ? slideFromRight : slideFromLeft;
                    toStyle = slideLeft;
                    break;
                case 2:
                    // from bottom
                    fromStyle = !this.options.inverse ? slideFromBottom : slideFromTop;
                    toStyle = slideTop;
                    break;
                case 3:
                    // from left
                    fromStyle = !this.options.inverse ? slideFromLeft : slideFromRight;
                    toStyle = slideLeft;
                    break;
            };

            return { from : fromStyle, to : toStyle };

        },
        // apply a transition or fallback to jquery animate based on Modernizr.csstransitions support
        _applyAnimation : function( el, styleCSS, speed ) {

            $.fn.applyStyle = this.support ? $.fn.css : $.fn.animate;
            el.stop().applyStyle( styleCSS, $.extend( true, [], { duration : speed + 'ms' } ) );

        },

    };

    var logError = function( message ) {

        if ( window.console ) {

            window.console.error( message );

        }

    };

    $.fn.hoverdir = function( options ) {

        var instance = $.data( this, 'hoverdir' );

        if ( typeof options === 'string' ) {

            var args = Array.prototype.slice.call( arguments, 1 );

            this.each(function() {

                if ( !instance ) {

                    logError( "cannot call methods on hoverdir prior to initialization; " +
                    "attempted to call method '" + options + "'" );
                    return;

                }

                if ( !$.isFunction( instance[options] ) || options.charAt(0) === "_" ) {

                    logError( "no such method '" + options + "' for hoverdir instance" );
                    return;

                }

                instance[ options ].apply( instance, args );

            });

        }
        else {

            this.each(function() {

                if ( instance ) {

                    instance._init();

                }
                else {

                    instance = $.data( this, 'hoverdir', new $.HoverDir( options, this ) );

                }

            });

        }

        return instance;

    };

} )( jQuery, window );

//gantt chart functions
        function zoom_tasks(node){
            switch(node.value){
                case "week":
                    gantt.config.scale_unit = "day";
                    gantt.config.date_scale = "%d %M";

                    gantt.config.scale_height = 60;
                    gantt.config.min_column_width = 30;
                    gantt.config.subscales = [
                                {unit:"hour", step:1, date:"%H"}
                    ];
                break;
                case "trplweek":
                    gantt.config.min_column_width = 70;
                    gantt.config.scale_unit = "day";
                    gantt.config.date_scale = "%d %M";
                    gantt.config.subscales = [ ];
                    gantt.config.scale_height = 35;
                break;
                case "month":
                    gantt.config.min_column_width = 25;
                    gantt.config.scale_unit = "week";
                    gantt.config.date_scale = "第%W週";
                    gantt.config.subscales = [
                                {unit:"day", step:1, date:"%D"}
                    ];
                    gantt.config.scale_height = 60;
                break;
                case "year":
                    gantt.config.min_column_width = 25;
                    gantt.config.scale_unit = "month";
                    gantt.config.date_scale = "%M";
                    gantt.config.scale_height = 60;
                    gantt.config.subscales = [
                                {unit:"week", step:1, date:"第%W週"}
                    ];
                break;
            }
            gantt.render();
            colorStatus();
        }

        function game_type_code_converter(game_type_code){
            game_type = "";
            if(game_type_code == "GAME_TYPE00002"){
                game_type = "casino"
            }
            else if(game_type_code == "GAME_TYPE00005"){
                game_type = "video_conf"
            }
            else if(game_type_code == "GAME_TYPE00007"){
                game_type = "training"
            }
            else if(game_type_code == "GAME_TYPE00009"){
                game_type = "others"
            }
            else if(game_type_code == "GAME_TYPE00010"){
                game_type = "cf"
            }
            else if(game_type_code == "GAME_TYPE00011"){
                game_type = "sports"
            }
            else if(game_type_code == "GAME_TYPE00012"){
                game_type = "lottery"
            }
            else if(game_type_code == "GAME_TYPE00014"){
                game_type = "IPL"
            }
            else if(game_type_code == "GAME_TYPE00021"){
                game_type = "database"
            }
            return game_type
        }

        function reorderTasks(tasks){
            new_tasks = [];
            processes = ['rough','concept','model','texture','rigging','animation','lighting','effects','layout','final'];
            for(x=0;x<processes.length;x++){
                for(i=0;i<tasks.length;i++){
                    if(tasks[i]['process'] == processes[x]){
                        new_tasks.push(tasks[i]);
                    }
                }
            }
            return new_tasks;
        }

        function mydiff(date1,date2,interval) {
            var second=1000, minute=second*60, hour=minute*60, day=hour*24, week=day*7;
            date1 = new Date(date1);
            date2 = new Date(date2);
            var timediff = date2 - date1;
            if (isNaN(timediff)) return NaN;
            switch (interval) {
                case "years": return date2.getFullYear() - date1.getFullYear();
                case "months": return (
                    ( date2.getFullYear() * 12 + date2.getMonth() )
                    -
                    ( date1.getFullYear() * 12 + date1.getMonth() )
                );
                case "weeks"  : return Math.floor(timediff / week);
                case "days"   : return Math.floor(timediff / day);
                case "hours"  : return Math.floor(timediff / hour);
                case "minutes": return Math.floor(timediff / minute);
                case "seconds": return Math.floor(timediff / second);
                default: return undefined;
            }
        }

        function colorStatus(){
            $j("div.gantt_tree_content:contains('.Complete')").parent().addClass("complete");
            $j("div.gantt_tree_content:contains('.In Progress')").parent().addClass("inprogress");
            $j("div.gantt_tree_content:contains('.Ready')").parent().addClass("ready");
            $j("div.gantt_tree_content:contains('.Not Ready')").parent().addClass("notready");
        }