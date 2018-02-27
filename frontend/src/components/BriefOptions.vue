<template>
  <div v-if="briefOptions">
    <transition name="slide-fade" mode="out-in">
    <div class="row">
      <div class="col-sm-12 sm-margin-b-2">
        <h2 class="text-center"> {{ titles[position] }} </h2>
      </div>
    </div>
    </transition>
  <div  v-if="briefOptions.length == 1">
    <img src="../assets/img/loading.gif" class="img-responsive center-block" alt="loading">
  </div>
    <div class="row">
      <div v-for="(choice, index) in briefOptions[position]['choices']" :key="index" class="col-sm-6 sm-margin-b-2">
        <div class="service" data-height="height" @click="nextQuestion(), saveBriefData(choice.value)" :id="choice.label">
          <div class="service-info">
            <h3>{{ choice.display_name }} </h3>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'BriefOptions',
  data () {
    return {
      fields: [
        'industry',
        'experience',
        'aim',
        'stage',
        'strategies',
        'audience',
        'callcenter',
        'marketing',
        'payment'
      ],
      titles: [
        'In which industry do you work / plan to work?',
        'What is your experience in this industry?',
        'What is the main task at this stage of your work?',
        'How can you describe the work of your project at this stage?',
        'Choose the most accurate option that characterizes your project',
        'What is the current / planned coverage of your project?',
        'Do you have a call center?',
        'Is there a marketing department in your company/is it planned in near future?',
        'What is the most convenient way for you to accept payments for services provision?'
      ]
    }
  },
  computed: {
    ...mapGetters({
      briefOptions: 'briefOptions'
    }),
    ...mapGetters({
      briefData: 'briefData'
    }),
    position () {
      return this.$store.state.briefCount
    }
  },
  methods: {
    nextQuestion: function () {
      return this.$store.dispatch('incrementBriefCount')
    },
    saveBriefData (value) {
      var field = this.fields[this.position - 1]
      var briefData = {'field': field, 'value': value}
      this.$store.dispatch('addBriefData', briefData)
    }
  },
  beforeCreate () {
    this.$store.dispatch('optionsBrief')
  }
}
</script>
