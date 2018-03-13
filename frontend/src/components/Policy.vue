<template>
  <div class="component-wrapper">
    <!--========== PARALLAX ==========-->
    <div class="parallax-window" >
      <img src="../assets/img/1920x1080/01.jpg" v-parallax="0.4" class="parallax-img" alt="">
      <div class="parallax-content container">
        <h1 class="carousel-title">Privacy Policy</h1>
      </div>
    </div>
    <!--========== PARALLAX ==========-->
    <!--========== PAGE LAYOUT ==========-->
    <!-- Our Exceptional Solutions -->
    <div class="content-lg container">
      <div class="row margin-b-40">
        <div class="col-sm-12">
          <p class="privacy-text">DMM understands that your privacy is important. DMM is committed to protecting your privacy and personal information you provide as you access and use materials on DMM Site, including the Site subscription pages. In addition, information that
            you submit to DMM in response to an email request for information or other outreach from DMM, or through DMM’s employment application processes, will be treated in accordance with appointment.<br><br> We respect your privacy. If you provide
            information on our website, we'll only use your information within the context of how you shared it. We do not sell information provided on our site to third party sources for marketing purposes. Please be aware that our website does use analytical
            systems to track how users use the site. We use this information for insight into how useful and effective our content is for our web audiences. If you have questions about the information we collect and how it's used, please contact us.<br><br>          SECURITY DMM has implemented generally accepted standards of technology and operational security in order to protect personally identifiable data and information from loss, misuse, alteration or destruction. However, despite DMM best efforts,
            security cannot be absolutely guaranteed against all threats. To the best of DMM ability, DMM ensures that all appropriate confidentiality obligations and technical and organisational security measures are in place to prevent any unauthorised
            or unlawful disclosure or processing of such information and data, and the accidental loss or destruction of or damage to such information and data. Only authorised personnel are provided access to such information and these employees have agreed
            to ensure confidentiality of this information.<br><br> DATA RETENTION Personal data submitted to us will only be retained for as long as is required for the purposes for which it was collected or as required by law. For example, contact information
            about DMM website visitors (such as information generated though registration for access to areas on the site) will be kept as long as the information is required to completely service the contact request or until a user requests that DMM deletes
            that information.<br><br> MARKETING From time to time, we may send you information regarding services, publications, products and events that we perceive may be of interest to you or your business. You may receive this information by hard copy
            mailing or email. If, at any time, you prefer not to receive further communications from us in any or all forms (except in connection with information, products, publications, events or services that you specifically request), you will have
            the ability to unsubscribe from such communications by means of a link provided in every email that is sent to you by us.
          </p>
        </div>
      </div>
      <!--// end row -->
    </div>
    <!--========== END PAGE LAYOUT ==========-->
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'Policy'
}
</script>

<style scoped>
.parallax-img{
  top: -90%;
}
</style>
