<template>
  <div class="component-wrapper">
    <!--========== PARALLAX ==========-->
    <div class="parallax-window" >
      <img src="../assets/img/1920x1080/01.jpg" v-parallax="0.4" class="parallax-img" alt="">
      <div class="parallax-content container">
        <h1 class="carousel-title">TAKE PART IN A SHORT SURVEY!</h1>
      </div>
    </div>
    <!--========== BRIEF ==========-->
    <div class="bg-color-sky-light" data-auto-height="true">
      <div class="content-lg container">
        <div v-if="showBriefStart" id="start-test" class="text-center">
          <h2>Let's analyze and improve your project!</h2>
          <p>Answer 9 simple questions and get first free email consultation right now!</p>
          <button v-if="showBriefStart" class="btn-theme btn-theme-sm btn-theme-lg btn-base-bg text-uppercase" @click="showBriefForm=true; showLeadForm=false; showBriefStart=false">START</button>
          <div class="row">
            <div class="col-sm-6 col-sm-offset-3 sm-margin-b-30 lead-form">
              <p class="text-center">If you have any other questions, fill out the feedback form below</p>
              <dmm-create-lead></dmm-create-lead>
            </div>
          </div>
        </div>
        <dmm-brief-options v-if="showBriefForm"></dmm-brief-options>
        <div v-if="showBriefCompleted" id="complete-test" class="text-center">
          <h2>You have successfully completed!</h2>
          <div class="row">
            <div class="col-sm-6 col-sm-offset-3 sm-margin-b-30 lead-form">
              <p class="text-center">Please leave your contact information to get the most advantageous offer from DMM based on the received answers.</p>
              <dmm-create-lead></dmm-create-lead>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--========== END BRIEF ==========-->
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import CreateLead from './CreateLead'
import BriefOptions from './BriefOptions'

export default {
  name: 'Brief',
  data () {
    return {
      showBriefStart: true,
      showBriefForm: false
    }
  },
  computed: {
    ...mapGetters({
      briefCount: 'briefCount'
    }),
    ...mapGetters({
      leads: 'leads'
    }),
    ...mapGetters({
      briefData: 'briefData'
    }),
    ...mapGetters({
      isBriefSent: 'isBriefSent'
    }),
    showBriefCompleted () {
      if (this.briefIsReady) {
        return true
      } else {
        return false
      }
    },
    briefIsReady () {
      if (this.briefCount === 9) {
        this.$store.dispatch('clearLeads')
        this.createBrief()
        return true
      }
      return false
    }
  },
  methods: {
    createBrief () {
      this.showBriefForm = false
      this.showBriefStart = false
      if (this.leads.length === 1 && this.isBriefSent === false) {
        this.briefData['lead'] = this.leads[0].email
        this.$store.dispatch('createBrief', this.briefData)
        this.$store.dispatch('markBriefSent', true)
        this.$router.push('/thanks')
        return true
      }
    }
  },
  components: {
    'dmm-create-lead': CreateLead,
    'dmm-brief-options': BriefOptions
  }
}
</script>

<style scoped>
.parallax-img{
  top: -70%;
}
.lead-form >>> input,
.lead-form >>> textarea {
  background-color: #fff;
  border: 1px solid #ccc;
}
</style>
