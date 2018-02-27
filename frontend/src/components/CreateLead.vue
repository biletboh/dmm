<template>
  <form  v-on:submit="submitForm">

    <p :class="{ 'control': true }">
      <input v-validate="'required|alpha_spaces'" :class="{'input': true, 'has-error': errors.has('name') }" class="form-control footer-input margin-b-20" v-model="name" name="name" type="text" placeholder="Name">
      <span v-show="errors.has('name')" class="help has-error">{{ errors.first('name') }}</span>
    </p>

    <p :class="{ 'control': true }">
      <input v-validate="'required|email'" :class="{'input': true, 'has-error': errors.has('email') }" class="form-control footer-input margin-b-20" v-model="email" name="email" type="text" placeholder="Email">
      <span v-show="errors.has('email')" class="help has-error">{{ errors.first('email') }}</span>
    </p>

    <p :class="{ 'control': true }">
      <input v-validate="'required|phonenumbercheck'" :class="{'input': true, 'has-error': errors.has('phone') }" class="form-control footer-input margin-b-20" v-model="phone" name="phone" type="text" placeholder="Phone">
      <span v-show="errors.has('phone')" class="help has-error">{{ errors.first('phone') }}</span>
    </p>

    <p :class="{ 'control': true }">
      <textarea v-validate="'required'" :class="{'textarea': true, 'has-error': errors.has('message') }" class="form-control footer-input margin-b-20" v-model="message" name="message" type="text" placeholder="Message" rows="6"></textarea>
      <span v-show="errors.has('message')" class="help has-error">{{ errors.first('message') }}</span>
    </p>

    <!-- <input v-model="name" type="text" class="form-control footer-input margin-b-20" placeholder="Name" required> -->
    <!-- <input v-model="email" type="email" class="form-control footer-input margin-b-20" placeholder="Email" required> -->
    <!-- <input v-model="phone" type="text" class="form-control footer-input margin-b-20" placeholder="Phone" required> -->
    <!-- <textarea v-model="message" class="form-control footer-input margin-b-30" rows="6" placeholder="Message" required></textarea> -->
    <button type="submit" :disabled="!isFormComplete || errors.any() " class="btn-theme btn-theme-sm btn-base-bg text-uppercase">Submit</button>
  </form>
</template>

<script>
/* eslint-disable */

import Vue from 'vue'
import VeeValidate from 'vee-validate'

var PhoneNumber = require('awesome-phonenumber')

Vue.use(VeeValidate)

VeeValidate.Validator.extend('phonenumbercheck', {
  getMessage: field => 'Sorry, wrong phone number.',
  validate: value => {

    let plusregex = new RegExp('^[\+]')
    if (!plusregex.test(value)) {
      value = '+' + value
    } 

    let testNumber = new PhoneNumber(value)
    if(testNumber.isValid()){
     return true
   }
   return false
 }
});

export default {
  name: 'create-lead',
  data () {
    return {
      'name': '',
      'email': '',
      'phone': '',
      'message': ''
    }
  },
  computed: {
    isFormComplete () {
      return this.name && this.phone && this.email && this.message;
    }
  },
  methods: {
    submitForm (event) {

      this.phone = this.checkPlusNumber(this.phone)
      event.preventDefault()

      this.createLead()
      this.$router.push('/thanks')

      // this.name = ''
      // this.email = ''
      // this.phone = ''
      // this.message = ''
    },
    createLead () {
      this.$store.dispatch('createLead', { name: this.name, email: this.email, phone: this.phone, message: this.message })
    },
    checkPlusNumber(phone_number) {
      let plus_regex = new RegExp('^[\+]')
      if (!plus_regex.test(phone_number)) {
        phone_number = '+' + phone_number
      }
      return phone_number
    }
  }
}
</script>
<style scoped>
.has-error{
  border: 1px solid rgba(220, 53, 69, 0.8) !important;
}

span.has-error{
  color: red;
  font-size: 0.7em !important;
  border: none !important;
}
</style>
