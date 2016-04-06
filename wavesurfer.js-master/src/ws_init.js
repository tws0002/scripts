var wavesurfer = [];

var $j = jQuery.noConflict();
$j('.wavesurfer-block').each(function(i) {

    var selector = '#wavesurfer-player-' + i;

    var container = $j(this).children(container);

    container.attr("id", "wavesurfer-player-" + i);

    var wave_color = container.attr('data-wave-color');
  var progress_color = container.attr('data-progress-color');
  var cursor_color = container.attr('data-cursor-color');
  var file_url = container.attr('data-url');
  var split = container.attr('data-split-channels');
  if (split == "true") {
    split = true;
  } else {
    split = false;
  }

    var options = {
    container: selector,
    splitChannels: split,
    waveColor: wave_color,
    progressColor: progress_color,
    cursorColor: cursor_color
  };

    wavesurfer[i] = WaveSurfer.create(options);

    wavesurfer[i].load(file_url);

    $j(window).resize(function() {
    wavesurfer[i].drawer.containerWidth = wavesurfer[i].drawer.container.clientWidth;
    wavesurfer[i].drawBuffer();
  });

});

$j('.wavesurfer-block').each(function(i) {

  var timeblock = $j(this).find('.wavesurfer-time');
  var duration = $j(this).find('.wavesurfer-duration');

  var buttonPlay = $j(this).find('button.wavesurfer-play');
  var buttonStop = $j(this).find('button.wavesurfer-stop');
  var buttonMute = $j(this).find('button.wavesurfer-mute');
  var buttonDownload = $j(this).find('button.wavesurfer-download');
  var buttonLoop = $j(this).find('button.wavesurfer-loop');
  var debugBlock = $j(this).find('.debug');
  var progressBar = $j(this).find('progress');

  wavesurfer[i].on('loading', function(percent) {
    progressBar.attr('value', percent);
  });
  wavesurfer[i].on('error', function() {
    progressBar.hide();
  });

    wavesurfer[i].on('ready', function() {
    progressBar.hide();
    var audio_duration = wavesurfer[i].getDuration();
    duration.html(secondsTimeSpanToMS(audio_duration));
    var current_time = wavesurfer[i].getCurrentTime();
    timeblock.html(secondsTimeSpanToMS(current_time));
  });

    wavesurfer[i].on('audioprocess', function() {
    var current_time = wavesurfer[i].getCurrentTime();
    timeblock.html(secondsTimeSpanToMS(current_time));
  });

    wavesurfer[i].on('seek', function() {
    var current_time = wavesurfer[i].getCurrentTime();
    timeblock.html(secondsTimeSpanToMS(current_time));
  });

    buttonStop.addClass('wavesurfer-active-button');

    buttonPlay.click(function() {
    wavesurfer[i].playPause();

        if ($j(this).hasClass('wavesurfer-active-button')) {
      $j(this).removeClass('wavesurfer-active-button');

      $j(this).addClass('wavesurfer-paused-button');

      $j(this).parent().children('button.wavesurfer-play').removeClass('wavesurfer-active-button');
      $j(this).parent().children('button.wavesurfer-stop').removeClass('wavesurfer-active-button');

          } else {
      $j(this).addClass('wavesurfer-active-button');

            $j(this).addClass('wavesurfer-active-button');

            $j(this).parent().children('button.wavesurfer-play').removeClass('wavesurfer-paused-button');
      $j(this).parent().children('button.wavesurfer-stop').removeClass('wavesurfer-active-button');
    };

  });
  buttonStop.click(function() {
    wavesurfer[i].stop();

    $j(this).addClass('wavesurfer-active-button');
    $j(this).parent().children('button.wavesurfer-play').removeClass('wavesurfer-active-button');
    $j(this).parent().children('button.wavesurfer-play').removeClass('wavesurfer-paused-button');
    var current_time = wavesurfer[i].getCurrentTime();
    timeblock.html(secondsTimeSpanToMS(current_time));
  });

    buttonMute.click(function() {
    wavesurfer[i].toggleMute();

        if ($j(this).hasClass('wavesurfer-active-button')) {
      $j(this).removeClass('wavesurfer-active-button');
    } else {
      $j(this).addClass('wavesurfer-active-button');
    };

  });

    buttonDownload.click(function() {
    var audio = $j(this).parent().parent('.wavesurfer-block').children('.wavesurfer-player');

    var download_url = audio.attr('data-url');
        var index = download_url.lastIndexOf("/") + 1;
    var file_name = download_url.substr(index);
    $j(this).children('a').attr('href', download_url);
    $j(this).children('a').attr('download', file_name);

        download(download_url);
  });

    wavesurfer[i].on('finish', function() {
    if (buttonLoop.hasClass('wavesurfer-active-button') == false) {
      buttonPlay.removeClass('wavesurfer-active-button');
      buttonStop.addClass('wavesurfer-active-button');
    };
  });

    buttonLoop.click(function() {
        if ($j(this).hasClass('wavesurfer-active-button')) {
      $j(this).removeClass('wavesurfer-active-button');
      wavesurfer[i].on('finish', function() {
        wavesurfer[i].pause();
      });
    } else {
      $j(this).addClass('wavesurfer-active-button');
      wavesurfer[i].on('finish', function() {
        wavesurfer[i].play();
      });
    };
  });

    if ($j(this).hasClass('wavesurfer-playlist')) {
        var tracks = $j(this).find('.wavesurfer-list-group li');
    var current = 0;
    tracks.eq(current).addClass('wavesurfer-active-track');

        tracks.click(function() {
      if ($j(this).hasClass('wavesurfer-active-track') == false) {

        tracks.each(function() {
          $j(this).removeClass('wavesurfer-active-track');
        });
        var url = $j(this).attr('data-url');
        current = $j(this).index();
        wavesurfer[i].load(url);
        progressBar.attr('value', '0');
        progressBar.show();

                wavesurfer[i].on('loading', function(percent) {
          progressBar.attr('value', percent);
        });
        wavesurfer[i].on('ready', function() {
          progressBar.hide();
          wavesurfer[i].play();
        });
        $j(this).addClass('wavesurfer-active-track');
        buttonPlay.addClass('wavesurfer-active-button');

                buttonPlay.addClass('wavesurfer-active-button');

                buttonPlay.parent().children('button.wavesurfer-play').removeClass('wavesurfer-paused-button');
        buttonPlay.parent().children('button.wavesurfer-stop').removeClass('wavesurfer-active-button');

        buttonDownload.parent().parent('.wavesurfer-block').children('.wavesurfer-player').attr('data-url', url);
      };     });

    wavesurfer[i].on('finish', function() {
            current++;

            var url = '';
      url = tracks.eq(current).attr('data-url');
            if (url != undefined) {
        wavesurfer[i].load(url);
        progressBar.attr('value', '0');
        progressBar.show();

                wavesurfer[i].on('loading', function(percent) {
          progressBar.attr('value', percent);
        });

        tracks.eq(current - 1).removeClass('wavesurfer-active-track');
        tracks.eq(current).addClass('wavesurfer-active-track');

        buttonDownload.parent().parent('.wavesurfer-block').children('.wavesurfer-player').attr('data-url', url);
                
                wavesurfer[i].on('ready', function() {
          wavesurfer[i].play();

        });
      };
    });
  };
});

function secondsTimeSpanToMS(s) {
  var m = Math.floor(s / 60);   s -= m * 60;
  s = Math.floor(s);
  return (m < 10 ? '0' + m : m) + ":" + (s < 10 ? '0' + s : s); } 