<template>
  <!--========== BRIEF ==========-->
  <div class="bg-color-sky-light" data-auto-height="true">
    <div class="content-lg container">
      <div v-if="showBriefStart" id="start-test" class="text-center">
        <h2>Let's analyze and improve your project!</h2>
        <p>Answer 9 simple questions and get first free email consultation right now!</p>
        <button v-if="showBriefStart" class="btn-theme btn-theme-sm btn-theme-lg btn-base-bg text-uppercase" @click="showBriefForm=true; showLeadForm=false; showBriefStart=false">START</button>
      </div>
      <div v-if="showBriefCompleted" id="complete-test" class="text-center">
        <h2>You have successfully completed!</h2>
      </div>
      <dmm-brief-options v-if="showBriefForm"></dmm-brief-options>
      <div v-if="showLeadForm" class="row">
        <div class="col-sm-6 col-sm-offset-3 sm-margin-b-30">
          <p class="text-center">If you have any other questions, fill out the feedback form below</p>
          <dmm-create-lead></dmm-create-lead>
        </div>
      </div>
      <div v-if="showBriefCompleted" class="row">
        <div class="col-sm-6 col-sm-offset-3 sm-margin-b-30">
          <p class="text-center">Please leave your contact information to get the most advantageous offer from DMM based on the received answers. We will contact you as soon as possible.</p>
          <dmm-create-lead></dmm-create-lead>
        </div>
      </div>
    </div>
  </div>
  <!--========== END BRIEF ==========-->
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
      showLeadForm: true,
      showBriefForm: false
    }
  },
  computed: {
    ...mapGetters({
      briefCount: 'briefCount'
    }),
    showBriefCompleted () {
      if (this.briefCount > 8) {
        return true
      } else {
        return false
      }
    }
  },
  components: {
    'dmm-create-lead': CreateLead,
    'dmm-brief-options': BriefOptions
  }
}
</script>
