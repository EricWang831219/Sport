<template>
    <!-- MAIN CONTENT-->
            <div class="main-content">
                <div class="section__content section__content--p30">
                    <div class="container-fluid">
                        <div class="row">
                            <predictionForm/>
                            <PercentChart/>
                        </div>
                        <DataTable ref="DataTable"/>
                        <div class="row">
                            <div class="col-md-12">
                                <div class="copyright">
                                    <p>Copyright © 2018 Colorlib. All rights reserved. Template by <a href="https://colorlib.com">Colorlib</a>.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- END MAIN CONTENT-->
</template>
<script>
import PercentChart from './PercentChart.vue'
import DataTable from './DataTable.vue'
import PredictionForm from './PredictionForm.vue' 
export default {
  name: 'MainContent',
  components:{
      PercentChart,
      DataTable,
      PredictionForm
  }
}
</script>
