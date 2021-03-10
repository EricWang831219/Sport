<template>
  <div class="col-lg-6">
    <div class="au-card recent-report">
      <div class="au-card-inner">
        <h3 class="title-2">Prediction Report</h3>
        <div v-if='!isActive'>
          <div class="form-group">
            <label for="Trends" class="control-label mb-1">Trends:</label>
            <input
              id="Trends"
              name="Trends"
              type="text"
              class="form-control"
              aria-required="true"
              aria-invalid="false"
              v-model="Trends"
            >
          </div>
          <div class="form-group">
            <label for="Odds" class="control-label mb-1">Odds:</label>
            <input
              id="Odds"
              name="Odds"
              type="text"
              class="form-control"
              aria-required="true"
              aria-invalid="false"
              v-model="Odds"
            >
          </div>
          <div class="form-group">
            <label for="Handicap" class="control-label mb-1">Handicap:</label>
            <input
              id="Handicap"
              name="Handicap"
              type="text"
              class="form-control"
              aria-required="true"
              aria-invalid="false"
              v-model="Handicap"
            >
          </div>
          <div class="form-group">
            <label for="Category" class="control-label mb-1">Category:</label>
            <select class="form-control" v-model="Category">
              <option v-for="(item, key) in options" :key = key>
                {{item}}
              </option>
            </select>
          </div>
          <button @click="submit()"  class="btn btn-lg btn-info btn-block">
            <span v-if='!isSending' id="prediction">Prediction</span>
            <span v-else id="sending">Sending…</span>
          </button>
          </div>
          <PredictionResult v-else :totals="totals" />
          <div v-show='isActive'>
          <div class="recent-report__chart" style="padding-bottom:5%">
            <!-- <canvas id="recent-rep-chart"></canvas> -->
            <CanvasImg v-show='isActive' :percent="winRate" :majorColor="majorColor" 
              :minorColor="minorColor" :majorLabel="majorLabel" :minorLabel="minorLabel" :id="canvasId" :index="index"/> 
          </div>
          <button  @click="back()"  class="btn btn-lg btn-info btn-block">
            <span id="back">Back</span>
          </button>
          </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import Chart from "chart.js";
import PredictionResult from './PredictionResult.vue' ;
import CanvasImg from './Canvas.vue';
export default {
  name: "PredictionForm",
    components:{
      PredictionResult,
      CanvasImg
  },
  data() {
    return {
      options: ['NBA','MLB'],
      Trends: [],
      Odds: [],
      Handicap: [],
      Category: null,
      isActive : false,
      isSending : false,
      totals : null,
      majorColor: "#00ad5f",
      minorColor: "#fa4251",
      majorLabel: "WinRate",
      minorLabel: "LossRate",
      canvasId: "canvasII",
      winRate: null,
      index: 0
    };
  },
  methods:{
    submit(){
      this.isSending = true
      axios.get("http://127.0.0.1:5000/getPrediction?data=" + this.Trends + '|' + this.Odds + '|' + this.Handicap + '&category=' + this.Category).then(response => {
       this.totals = response.data.totals
       this.winRate = response.data.winRate
       this.isSending = false
       this.isActive = true
       this.index++;
       //this.getCanvas(response.data.winRate)
      });
    },
    back(){
      this.isActive = false
    }
  }
};
</script>