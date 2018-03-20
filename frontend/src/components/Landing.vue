<template>
  <div>
    <dmm-header></dmm-header>
    <router-view name="sublanding"></router-view>
    <dmm-footer></dmm-footer>

    <!-- Back To Top -->
    <a href="javascript:void(0);" class="js-back-to-top back-to-top">Top</a>

  </div>
</template>

<script>
/* eslint-disable */
import Header from './Header'
import Footer from './Footer'

export default {
  name: 'Landing',
  components: {
    'dmm-header': Header,
    'dmm-footer': Footer,
  },
  methods: {
    initAnimations: function(){
      new WOW().init();
    },
    backToTopButton: function(){
        // browser window scroll (in pixels) after which the "back to top" link is shown
        var offset = 300,
        //browser window scroll (in pixels) after which the "back to top" link opacity is reduced
        offset_opacity = 1200,
        //duration of the top scrolling animation (in ms)
        scroll_top_duration = 700,
        //grab the "back to top" link
        $back_to_top = $('.js-back-to-top');

    //hide or show the "back to top" link
    $(window).scroll(function(){
        ( $(this).scrollTop() > offset ) ? $back_to_top.addClass('back-to-top-is-visible') : $back_to_top.removeClass('back-to-top-is-visible back-to-top-fade-out');
        if( $(this).scrollTop() > offset_opacity ) {
            $back_to_top.addClass('back-to-top-fade-out');
        }
    });

    //smooth scroll to top
    $back_to_top.on('click', function(event){
        event.preventDefault();
        $('body,html').animate({
            scrollTop: 0 ,
            }, scroll_top_duration
        );
    });
    }
  },
  mounted(){
    this.initAnimations();
    this.backToTopButton();
  }
}
</script>

<style></style>
