<behavior class="chart_load" event="load">
    spt.dom.load_js( ['assets/scripts/Highcharts-4.0.3/js/highcharts.js'], function(){});
</behavior>


<behavior class="chart_content" event="load">
Highcharts.createElement('link', {
    href: '//fonts.googleapis.com/css?family=Unica+One',
    rel: 'stylesheet',
    type: 'text/css'
}, null, document.getElementsByTagName('head')[0]);

Highcharts.theme = {
    colors: ["#2b908f", "#90ee7e", "#f45b5b", "#7798BF", "#aaeeee", "#ff0066", "#eeaaee",
        "#55BF3B", "#DF5353", "#7798BF", "#aaeeee"],
    chart: {
        backgroundColor: {
            linearGradient: { x1: 0, y1: 0, x2: 1, y2: 1 },
            stops: [
                [0, '#2a2a2b'],
                [1, '#3e3e40']
            ]
        },
        style: {
            fontFamily: "'Unica One', sans-serif"
        },
        plotBorderColor: '#606063'
    },
    title: {
        style: {
            color: '#E0E0E3',
            textTransform: 'uppercase',
            fontSize: '20px'
        }
    },
    subtitle: {
        style: {
            color: '#E0E0E3',
            textTransform: 'uppercase'
        }
    },
    xAxis: {
        gridLineColor: '#707073',
        labels: {
            style: {
                color: '#E0E0E3'
            }
        },
        lineColor: '#707073',
        minorGridLineColor: '#505053',
        tickColor: '#707073',
        title: {
            style: {
                color: '#A0A0A3'

            }
        }
    },
    yAxis: {
        gridLineColor: '#707073',
        labels: {
            style: {
                color: '#E0E0E3'
            }
        },
        lineColor: '#707073',
        minorGridLineColor: '#505053',
        tickColor: '#707073',
        tickWidth: 1,
        title: {
            style: {
                color: '#A0A0A3'
            }
        }
    },
    tooltip: {
        backgroundColor: 'rgba(0, 0, 0, 0.85)',
        style: {
            color: '#F0F0F0'
        }
    },
    plotOptions: {
        series: {
            dataLabels: {
                color: '#B0B0B3'
            },
            marker: {
                lineColor: '#333'
            }
        },
        boxplot: {
            fillColor: '#505053'
        },
        candlestick: {
            lineColor: 'white'
        },
        errorbar: {
            color: 'white'
        }
    },
    legend: {
        itemStyle: {
            color: '#E0E0E3'
        },
        itemHoverStyle: {
            color: '#FFF'
        },
        itemHiddenStyle: {
            color: '#606063'
        }
    },
    credits: {
        style: {
            color: '#666'
        }
    },
    labels: {
        style: {
            color: '#707073'
        }
    },

    drilldown: {
        activeAxisLabelStyle: {
            color: '#F0F0F3'
        },
        activeDataLabelStyle: {
            color: '#F0F0F3'
        }
    },

    navigation: {
        buttonOptions: {
            symbolStroke: '#DDDDDD',
            theme: {
                fill: '#505053'
            }
        }
    },

    // scroll charts
    rangeSelector: {
        buttonTheme: {
            fill: '#505053',
            stroke: '#000000',
            style: {
                color: '#CCC'
            },
            states: {
                hover: {
                    fill: '#707073',
                    stroke: '#000000',
                    style: {
                        color: 'white'
                    }
                },
                select: {
                    fill: '#000003',
                    stroke: '#000000',
                    style: {
                        color: 'white'
                    }
                }
            }
        },
        inputBoxBorderColor: '#505053',
        inputStyle: {
            backgroundColor: '#333',
            color: 'silver'
        },
        labelStyle: {
            color: 'silver'
        }
    },

    navigator: {
        handles: {
            backgroundColor: '#666',
            borderColor: '#AAA'
        },
        outlineColor: '#CCC',
        maskFill: 'rgba(255,255,255,0.1)',
        series: {
            color: '#7798BF',
            lineColor: '#A6C7ED'
        },
        xAxis: {
            gridLineColor: '#505053'
        }
    },

    scrollbar: {
        barBackgroundColor: '#808083',
        barBorderColor: '#808083',
        buttonArrowColor: '#CCC',
        buttonBackgroundColor: '#606063',
        buttonBorderColor: '#606063',
        rifleColor: '#FFF',
        trackBackgroundColor: '#404043',
        trackBorderColor: '#404043'
    },

    // special colors for some of the
    legendBackgroundColor: 'rgba(0, 0, 0, 0.5)',
    background2: '#505053',
    dataLabelsColor: '#B0B0B3',
    textColor: '#C0C0C0',
    contrastTextColor: '#F0F0F3',
    maskColor: 'rgba(255,255,255,0.3)'
};

// Apply the theme
Highcharts.setOptions(Highcharts.theme);

var server = TacticServerStub.get();

function returnUTC(temp) {
    temp = Date.parse(temp);
    year = temp.getFullYear();
    month = temp.getMonth();
    day = temp.getDate();
    hour = temp.getHours();

    return(Date.UTC(year,month,day,hour));
}

Number.prototype.round = function(places) {
  return +(Math.round(this + "e+" + places)  + "e-" + places);
}

farm_dates = [];
expr = "@SOBJECT(simpleslot/renderfarm_performance)";
renderfarm = server.eval(expr);

davinci_data = [];
ilm_data = [];
pixar_data = [];
vangogh_data = [];
picasso_data = [];

for(k=0;k<renderfarm.length;k++){
    name = renderfarm[k].name;
    usage = renderfarm[k].usage;
    usage = usage * .01;
    usage = usage / 4;
    usage = usage.round(2);
    time = renderfarm[k].time;
    time = returnUTC(time);
    if(name == 'Davinci_Cluster'){
        davinci_data.push([time, usage]);          
    }
    if(name == 'ILM_Cluster'){
        ilm_data.push([time, usage]);
    }
    if(name == 'Pixar_Cluster'){
        pixar_data.push([time, usage]); 
    }
    if(name == 'VanGogh_Cluster'){
        vangogh_data.push([time, usage]);        
    }
    if(name == 'Picasso_Cluster'){
        usage = usage * 4;
        picasso_data.push([time, usage]);        
    }

}


$j(function () {
    $j('#performance_container').highcharts({
        credits: {
            text: 'by: julio'
        },       
        chart: {
            type: 'area',
            zoomType: 'x'
        },
        title: {
            text: '刀鋒使用率(百分比)'
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            tickInterval: 24 * 3600 * 1000, // one week
            tickWidth: 2,
            gridLineWidth: 1,
            minorTickInterval: 7 * 24 * 3600 * 1000,
            minorTickWidth: 2,
            minorGridLineWidth: 0,            
            type: 'datetime',
            dateTimeLabelFormats: { // don't display the dummy year
                month: '%e. %b',
                year: '%b'
            },
            title: {
                text: '日期/時間'
            }
        },
        yAxis: {
            title: {
                text: '使用率 %'
            },
            min: 0,
            max: 100
        },
        tooltip: {
            headerFormat: '<b>{series.name}</b><br>',
            pointFormat: '{point.x:%e. %b}: {point.y} %'
        },

        plotOptions: {
            area: {
                stacking: 'normal',
                lineColor: '#dddddd',
                lineWidth: 1,
                marker: {
                    enabled: false,
                    lineWidth: 1,
                    lineColor: '#ffffff'
                }
            }
        },

        series: [{
            name: "台北,遊戲組,模型組", //Davinci Cluster: 
            data: davinci_data,
        },{
            name: "特效模擬,測試", //ILM_Cluster:
            data: ilm_data,
        },{
            name: "動畫組 算圖",  //Pixar_Cluster: 
            data: pixar_data,
        },{
            name: "動畫組算圖 製程管理組算圖", //VanGogh_Cluster:
            data: vangogh_data,
        }
        ]
    });
});

$j(function () {
    $j('#picasso_container').highcharts({
        credits: {
            text: 'by: julio'
        },
        chart: {
            type: 'area',
            zoomType: 'x'
        },
        title: {
            text: 'PICASSO使用率(百分比)'
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            tickInterval: 24 * 3600 * 1000, // one week
            tickWidth: 2,
            gridLineWidth: 1,
            minorTickInterval: 7 * 24 * 3600 * 1000,
            minorTickWidth: 2,
            minorGridLineWidth: 0,            
            type: 'datetime',
            dateTimeLabelFormats: { // don't display the dummy year
                month: '%e. %b',
                year: '%b'
            },
            title: {
                text: '日期/時間'
            }
        },
        yAxis: {
            title: {
                text: '使用率 %'
            },
            min: 0,
            max: 100
        },
        tooltip: {
            headerFormat: '<b>{series.name}</b><br>',
            pointFormat: '{point.x:%e. %b}: {point.y} %'
        },

        plotOptions: {
            area: {
                stacking: 'normal',
                lineColor: '#dddddd',
                lineWidth: 1,
                marker: {
                    enabled: false,
                    lineWidth: 1,
                    lineColor: '#ffffff'
                }
            }
        },

        series: [{
            name: "遊戲組,模型組", 
            data: picasso_data,
        }
        ]
    });
});
</behavior>
