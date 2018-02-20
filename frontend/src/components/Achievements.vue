<template>
  <div class="content-lg container">
    <div class="row margin-b-40">
      <div class="col-lg-12">
        <h2 class="text-center">Our achievements</h2>
        <p>Over the years, we have successfully taken the leading positions in the field of our key directions</p>
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
export default {
  name: 'Achievements',
  methods: {
    fillCharts: function (){
      var ctx = document.getElementById('myChart').getContext('2d');
      var data = {
        datasets: [{
          data: [37, 75],
          backgroundColor: ["rgba(0, 204, 204, 1)", "rgba(0, 204, 204, 0.5)"]
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
    }
  },
  mounted () {
    this.fillCharts();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
