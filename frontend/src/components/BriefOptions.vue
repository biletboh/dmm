<template>
  <div v-if="briefOptions">
    <div class="row">
              <!-- <transition name="slide-fade" mode="out-in"> -->
        <div class="col-sm-12 sm-margin-b-2 wow fadeInLeft animated" :key="titles[position]" data-wow-duration="1.3s">
          <h2 class="text-center"> {{ titles[position] }} </h2>
        </div>
      <!-- </transition> -->
    </div>
    <div  v-if="briefOptions.length == 1">
      <img src="../assets/img/all/Preloader_2.gif" class="img-responsive center-block" alt="loading">
    </div>
    <div class="row options-wrapper">
      <!-- <transition-group appear name="fade" mode="out-in" tag="div"> -->
        <div v-for="(choice, index) in briefOptions[position]['choices']" :key="index" class="col-sm-6 sm-margin-b-2 option" >
          <!-- <transition appear name="fade" mode="out-in" > -->
          <div data-height="height" @click="nextQuestion(), saveBriefData(choice.value)" :id="choice.label" :key="randInt()"
            class="service wow fadeInLeft animated" data-wow-duration="1.3s" :data-wow-delay="countDelay(index+1)" >
            <div class="service-info" :key="choice">
              <h3>{{ choice.display_name }} </h3>
            </div>
          </div>
        <!-- </transition> -->
        </div>
      <!-- </transition-group> -->
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'BriefOptions',
  props: ['data-wow-delay'],
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
    countDelay (delay) {
      return '.' + delay++ + 's'
    },
    randInt () {
      return Math.floor(Math.random() * 100)
    },
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
<style scoped>
.option{
  padding: 1px;
}
.options-wrapper{
  min-height: 440px;
}

.list-enter-active, .list-leave-active {
  transition: all 1s;
}
.list-enter, .list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}
.fade-enter-active, .fade-leave-active {
  transition: opacity .3s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active до версии 2.1.8 */ {
  opacity: 0;
}

</style>
