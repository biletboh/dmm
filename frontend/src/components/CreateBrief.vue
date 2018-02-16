<template>
  <transition name="slide-fade" mode="out-in">
  <div class="row">
    <div class="col-sm-12 sm-margin-b-2">
      <h2 class="text-center"> {{ titles[position] }} </h2>
    </div>
  </div>
  </transition>
</template>

<script>
export default {
  name: 'CreateBrief',
  data () {
    return {
      position: 0,
      titles: [
        'In which industry do you work / plan to work?',
        'What is your experience in this industry?',
        'What is the main task at this stage of your work?',
        'How can you describe the work of your project at this stage?',
        'Choose the most accurate option that characterizes your project',
        'What is the current / planned coverage of your project?',
        'Do you have a call center?',
        'Is there a marketing department in your company/is it planned in near future?',
        'What is the most convenient way for you to accept payments for services provision?',
        'What is the indicator that shows the state of overbought or oversold market?'
      ]
    }
  },
  methods: {
    submitForm (event) {
      this.createBrief()

      event.preventDefault()
    },
    createBrief () {
      console.log('send data to store')
      // this.$store.dispatch('createBrief', { industry: this.industry })
    },
    nextQuestion: function () {
    }
  }
}
</script>
