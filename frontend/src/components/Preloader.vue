<template>
  <!--========== PRELOADER ==========-->
  <div id="preloader" >
    <div id="status">&nbsp;</div>
  </div>
  <!--========== END PRELOADER ==========-->
</template>

<script>
/* eslint-disable */
export default {
  name: 'Preloader',
  methods:{
    initPreloader: function(){
      jQuery('#preloader').show().delay(1000).fadeOut('slow');
    }
  },
  watch: {
    '$route': function(){
      this.initPreloader();
    }
  },
  mounted (){
    this.initPreloader();
  }
}
</script>

<style scoped>

</style>
