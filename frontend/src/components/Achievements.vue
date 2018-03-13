<template>
  <div class="content-lg container">
    <div id="for_script"></div>
    <div class="row margin-b-40">
      <div class="col-lg-12 title-achievements">
        <h2 class="text-center">Our achievements</h2>
        <p class="text-center">Over the years, we have successfully taken the leading positions in the field of our key directions</p>
      </div>
      <div class="col-lg-9">
        <div class="mapСontainer">
          <h3>We serve customers in 7 different countries</h3>
          <div class="map">Alternative content</div>
        </div>
      </div>
      <div class="col-lg-3">
        <div class="col-lg-12">
          <h3 class="text-center">Our audience</h3>
          <div title="16.2 million views" class="outer circle shapeborder">
            <div title="79 thousand leads per day" class="inner circle shapeborder element-animation">&nbsp;</div>
          </div>
          <div class="lc">
            <div class="legend legend-1"></div><span> - 16.2 million views</span><br>
            <div class="legend legend-2"></div><span> - 79 thousand leads per day</span>
          </div>
        </div>
        <div class="col-lg-12">
          <h3 class="text-center">Our projects</h3>
          <div class="chart-container">
            <canvas id="myChart" width="300" height="300"></canvas>
          </div>
          <div class="lc">
            <div class="legend legend-1"></div><span> - 112 successful projects</span><br>
            <div class="legend legend-2"></div><span> - 37 regular customers</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import 'jquery-mapael';
import world_countries from '../assets/vendor/world_countries.js';
export default {
  name: 'Achievements',
  methods: {
    fillCharts: function (){
      var ctx = document.getElementById('myChart').getContext('2d');
      var data = {
        datasets: [{
          data: [37, 75],
          backgroundColor: ["rgba(0, 162, 244, 1)", "rgba(0, 162, 244, 0.5)"]
        }],
        labels: [
        ['Regular', 'customers'],
        ['Successful', 'projects']
        ]
      };
      var myPieChart = new Chart(ctx, {
        type: 'pie',
        data: data,
        options: {
          legend: {
            display: false
          },
          tooltips: {
            callbacks: {
              title: function(tooltipItem, data) {
                return data['labels'][tooltipItem[0]['index']];
              },
              label: function(tooltipItem, data) {
                return false;
              }
            },
            caretSize: 0,
            mode: 'single',
            position: 'average',
            backgroundColor: '#FFF',
            titleFontSize: 14,
            titleFontColor: '#000',
            titleFontStyle: 'normal',
            bodyFontColor: '#000',
            bodyFontSize: 14,
            displayColors: false,
            cornerRadius: 0
          }
        }
      });
    },
    fillMap: function(){
      $(".mapСontainer").mapael({
        map: {
          name: "world_countries",
          defaultArea: {
            attrs: {
              fill: "rgba(0, 162, 244, 0.5)",
              stroke: "#ffffff"
            },
            attrsHover: {
              fill: "rgba(0, 162, 244, 1)"
            },
            text: {
              attrs: {
                fill: "#505444"
              },
              attrsHover: {
                fill: "#000"
              }
            }
          }
        },
        plots: {
        // Image plot
        'Kiev': {
          type: "image",
          url: "http://email-list.org/marker.png",
          width: 12,
          height: 40,
          latitude: 50.43,
          longitude: 30.52,
          tooltip: {
            content: "<span style=\"font-weight:bold;\">Kiev, Ukraine</span>"
          },
          attrs: {
            opacity: 1
          },
          attrsHover: {
            transform: "s1.5"
          }
        },
        'Minsk': {
          type: "image",
          url: "http://email-list.org/marker.png",
          width: 12,
          height: 40,
          latitude: 53.89,
          longitude: 27.56,
          tooltip: {
            content: "<span style=\"font-weight:bold;\">Minsk, Belarus</span>"
          },
          attrs: {
            opacity: 1
          },
          attrsHover: {
            transform: "s1.5"
          }
        },
        'Limassol': {
          type: "image",
          url: "http://email-list.org/marker.png",
          width: 12,
          height: 40,
          latitude: 34.70,
          longitude: 33.02,
          tooltip: {
            content: "<span style=\"font-weight:bold;\">Limassol, Cyprus</span>"
          },
          attrs: {
            opacity: 1
          },
          attrsHover: {
            transform: "s1.5"
          }
        },
        'NewDelhi': {
          type: "image",
          url: "http://email-list.org/marker.png",
          width: 12,
          height: 40,
          latitude: 28.64,
          longitude: 77.21,
          tooltip: {
            content: "<span style=\"font-weight:bold;\">New Delphi, India</span>"
          },
          attrs: {
            opacity: 1
          },
          attrsHover: {
            transform: "s1.5"
          }
        },
        'Nairobi': {
          type: "image",
          url: "http://email-list.org/marker.png",
          width: 12,
          height: 40,
          latitude: -1.36,
          longitude: 36.83,
          tooltip: {
            content: "<span style=\"font-weight:bold;\">Nairobi, Kenya</span>"
          },
          attrs: {
            opacity: 1
          },
          attrsHover: {
            transform: "s1.5"
          }
        },
        'Tbilisi': {
          type: "image",
          url: "http://email-list.org/marker.png",
          width: 12,
          height: 40,
          latitude: 41.71,
          longitude: 44.78,
          tooltip: {
            content: "<span style=\"font-weight:bold;\">Tbilisi, Georgia</span>"
          },
          attrs: {
            opacity: 1
          },
          attrsHover: {
            transform: "s1.5"
          }
        },
        'Dubai': {
          type: "image",
          url: "http://email-list.org/marker.png",
          width: 12,
          height: 40,
          latitude: 25.27,
          longitude: 55.29,
          tooltip: {
            content: "<span style=\"font-weight:bold;\">Dubai, United Arab Emirates</span>"
          },
          attrs: {
            opacity: 1
          },
          attrsHover: {
            transform: "s1.5"
          }
        }
      }

    });
    },
    changeSVG: function(){
      if ($(window).width() >= 768) {
        $('.map').find('svg')[0].setAttribute("height", "500");
        $('.map').find('svg')[0].setAttribute("preserveAspectRatio", "none");
        $('.map').find('svg')[0].setAttribute("viewBox", "400 0 600 360");
      }
    }
  },
  mounted () {
    this.fillCharts();
    this.fillMap();
    this.changeSVG();
  }
}
</script>

<style scoped>
.title-achievements{
  margin-bottom: 30px;
}
</style>
