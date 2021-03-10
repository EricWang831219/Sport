<template>
  <canvas :id="id"></canvas>
</template>

<script>
export default {
  name: "canvasImg",
  props: ['percent','majorColor','minorColor','majorLabel','minorLabel','id','index'],
  data() {
    return {};
  },
  computed:{
      getPercent(){
        return this.index
      }
  },
  watch: {
      getPercent(newV, oldV){
      let vm = this;
      const ctx = document.getElementById(vm.id);
      if (ctx) {
        ctx.height = 280;
        const myChart = new Chart(ctx, {
          type: "doughnut",
          data: {
            datasets: [
              {
                label: "My First dataset",
                data: [vm.percent, 100 - vm.percent],
                backgroundColor: [vm.majorColor, vm.minorColor],
                hoverBackgroundColor: [vm.majorColor, vm.minorColor],
                borderWidth: [0, 0],
                hoverBorderColor: ["transparent", "transparent"]
              }
            ],
            labels: [vm.majorLabel, vm.minorLabel]
          },
          options: {
            maintainAspectRatio: false,
            responsive: true,
            cutoutPercentage: 55,
            animation: {
              animateScale: true,
              animateRotate: true
            },
            legend: {
              display: false
            },
            tooltips: {
              titleFontFamily: "Poppins",
              xPadding: 15,
              yPadding: 10,
              caretPadding: 0,
              bodyFontSize: 16
            }
          }
        });
      }
    }
     
  }
};
</script>