<template>
  <!--========== BRIEF ==========-->
  <div class="bg-color-sky-light" data-auto-height="true">
    <div class="content-lg container">
      <div id="start-test" v-if="showStartButton" class="text-center">
        <h2>Let's analyze and improve your project!</h2>
        <p>Answer 9 simple questions and get first free email consultation right now!</p>
        <button v-if="showStartButton" class="btn-theme btn-theme-sm btn-theme-lg btn-base-bg text-uppercase" @click="showBriefForm=true; showLeadForm=false; showStartButton=false">START</button>
      </div>
      <dmm-create-brief v-if="showBriefForm"></dmm-create-brief>
      <dmm-brief-options v-if="showBriefForm"></dmm-brief-options>
      <div v-if="showLeadForm" class="row">
        <div class="col-sm-6 col-sm-offset-3 sm-margin-b-30">
          <p class="text-center">If you have any other questions, fill out the feedback form below</p>
          <dmm-create-lead></dmm-create-lead>
        </div>
      </div>
    </div>
  </div>
  <!--========== END BRIEF ==========-->
</template>

<script>
import CreateLead from './CreateLead'
import CreateBrief from './CreateBrief'
import BriefOptions from './BriefOptions'

export default {
  name: 'Brief',
  data () {
    return {
      showStartButton: true,
      showBriefForm: false,
      showLeadForm: true
    }
  },
  components: {
    'dmm-create-lead': CreateLead,
    'dmm-create-brief': CreateBrief,
    'dmm-brief-options': BriefOptions
  },
  methods: {
    startBrief: function () {
      this.showBriefForm = true
      this.showLeadForm = false
      this.showStartButton = false
    }
  }
}
</script>
