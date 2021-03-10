<template>
  <div id="app" class="page-wrapper">
    <HeaderMobile/>
    <MenuSidebar ref="MenuSidebar" @updateDataTable="updateDataTable"/>
    <div class="page-container">
      <HeaderPortal/>
      <MainContent ref="MainContent"/>
    </div>
  </div>
</template>

<script>
import HeaderMobile from './components/HeaderMobile.vue'
import HeaderPortal from './components/HeaderPortal.vue'
import MenuSidebar from './components/MenuSidebar.vue'
import MainContent from './components/MainContent.vue'
import Vue from 'vue';

export default {
  name: 'app',
  components: {
    HeaderMobile,
    MenuSidebar,
    HeaderPortal,
    MainContent
  },
  mounted(){
  },
  computed: {
  },
  methods:{
    updateDataTable(data){
      this.$refs.MainContent.$refs.DataTable.dataList = data;
    }
  }
}
</script>

