<template>
  <div class="chart-info">
    <div class="chart-info__left">
      <div class="chart-note">
        <span class="dot dot--green"></span>
        <span>Win</span>
      </div>
      <div class="chart-note mr-0">
        <span class="dot dot--red"></span>
        <span>Loss</span>
      </div>
    </div>
    <div class="chart-info__right">
      <div class="chart-statis mr-0">
        <span class="index decre">
          <i class="zmdi"></i>{{totals}}
        </span>
        <span class="label">totals</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PredictionResult",
  props:['totals'],
  data() {
    return {
    };
  },
};
</script>