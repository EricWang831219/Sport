<template>
  <div class="row">
    <div class="col-lg-12">
      <h2 class="title-1 m-b-25">Results of the past 10 games in home</h2>
      <div class="table-responsive table--no-card m-b-40">
        <table class="table table-borderless table-striped table-earning">
          <thead>
            <tr>
              <th>Date</th>
              <th>MatchUp</th>
              <th>PK</th>
              <th class="text-right">PointSpreads</th>
              <th class="text-right">Totals</th>
              <th class="text-right">Score</th>
            </tr>
          </thead>
          <tbody v-for='(data, i) in dataList' :key="i + data.matchUP">
            <tr>
              <td>{{data.gameTime}}</td>
              <td>{{data.matchUP}}</td>
              <td v-if='data.PK == 1'><i class="fa fa-check" style="color:green"></i></td>
              <td v-else><i class="fa fa-close" style="color:red"></i></td>
              <td class="text-right" v-if='data.pointSpreads == 1'><i class="fa fa-check" style="color:green"></i></td>
              <td class="text-right" v-else><i class="fa fa-close" style="color:red"></i></td>
              <td class="text-right" v-if='data.totals == 1'><i class="fa fa-check" style="color:green"></i></td>
              <td class="text-right" v-else><i class="fa fa-close" style="color:red"></i></td>
              <td class="text-right">{{data.score}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: 'DataTable',
    data() {
    return {
      dataList: []
    };
  },
  mounted() {
  },
  methods:{
  }

}
</script>