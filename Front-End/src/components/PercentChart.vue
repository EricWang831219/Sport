<template>
  <div class="col-lg-6">
    <div class="au-card chart-percent-card">
      <div class="au-card-inner">
        <h3 class="title-2 tm-b-5">Totals char by %</h3>
        <div class="row no-gutters">
          <div class="col-xl-6">
            <div class="chart-note-wrap">
              <div class="chart-note mr-0 d-block">
                <span class="dot dot--red"></span>
                <span>Over</span>
              </div>
              <div class="chart-note mr-0 d-block">
                <span class="dot dot--blue"></span>
                <span>Under</span>
              </div>
            </div>
          </div>
          <div class="col-xl-6">
            <div class="percent-chart">
              <CanvasImg :percent="OverPercent" :majorColor="majorColor" 
              :minorColor="minorColor" :majorLabel="majorLabel" :minorLabel="minorLabel" :id="canvasId" :index="index" />
              <!--<canvas id="percent-chart" ref="percent-chart"></canvas>-->
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CanvasImg from "./Canvas.vue"
export default {
  name: "PercentChart",
  components:{
      CanvasImg
  },
  data() {
    return {
      OverPercent: 0,
      majorColor: "#fa4251",
      minorColor: "#00b5e9",
      majorLabel: "Over",
      minorLabel: "Under",
      canvasId: "canvasI",
      index: 0
    };
  },
  mounted() {
    axios.get("http://127.0.0.1:5000/getPercent").then(response => {
      let res = response.data.OverPercent;
      this.OverPercent = res;
      this.index++;
    });
  }
};
</script>
