<template>
    <!-- MENU SIDEBAR-->
        <aside class="menu-sidebar d-none d-lg-block">
            <div class="logo">
                <router-link to="/">
                    <img src="./../assets/images/icon/logo-mini.png"/> &nbsp;&nbsp;&nbsp;SportAnalyze
                </router-link>              
            </div>
            <div class="menu-sidebar__content js-scrollbar1">
                <nav class="navbar-sidebar">
                    <ul class="list-unstyled navbar__list">
                        <li class="active has-sub">
                            <a class="js-arrow" href="#">
                                <i class="fas fa-tachometer-alt"></i>Dashboard</a>
                        </li>
                        <li class="has-sub">
                            <a class="js-arrow" href="#">
                                <i class="fas fa-table"></i>Eastern Teams</a>
                            <ul class="list-unstyled navbar__sub-list js-sub-list">
                                <li v-for='data in initData.eastern' :key="data.name">
                                   <a href="#" @click="getDataTableData(data.name)"><img :src="data.img" width="20%" height="20%"/>&nbsp;&nbsp;{{data.name}}</a>
                                </li>
                            </ul>
                        </li>
                        <li class="has-sub">
                            <a class="js-arrow" href="#">
                                <i class="fas fa-table"></i>Western Teams</a>
                            <ul class="list-unstyled navbar__sub-list js-sub-list">
                                <li v-for='data in initData.western' :key="data.team">
                                   <a href="#" @click="getDataTableData(data.name)"><img :src="data.img" width="20%" height="20%"/>&nbsp;&nbsp;{{data.name}}</a>
                                </li>
                            </ul>
                        </li>
                        <li>
                            <a href="#">
                                <i class="fas fa-chart-bar"></i>Charts</a>
                        </li>
                    </ul>
                </nav>
            </div>
        </aside>
        <!-- END MENU SIDEBAR-->
</template>

<script>
import axios from "axios";
import dataTable from "./DataTable.vue";
export default {
  name: 'MenuSidebar',
  data() {
    return {
      initData: []
    };
  },
  mounted(){
    // init team menu
    try {
        var arrow = $('.js-arrow');
        arrow.each(function () {
        var that = $(this);
        that.on('click', function (e) {
            e.preventDefault();
            that.find(".arrow").toggleClass("up");
            that.toggleClass("open");
            that.parent().find('.js-sub-list').slideToggle();
        });
        });
    } catch (error) {
        console.log(error);
    }

    this.getInitData();
    this.getDataTableData('L.A. Lakers');
  },
  methods:{
      getInitData(){
        axios.get("/static/config/data/teamData.json").then(response => {
            this.initData = response.data.teamData;
        });
      },
      getDataTableData(team){  
        axios.get("http://127.0.0.1:5000/getTeamData?team=" + team).then(response => {
            this.$emit('updateDataTable', response.data);
        });
      }
  }
}
</script>