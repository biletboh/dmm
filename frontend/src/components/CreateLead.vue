<template>
  <form  v-on:submit="submitForm">
    <input v-model="name" type="text" class="form-control footer-input margin-b-20" placeholder="Name" required>
    <input v-model="email" type="email" class="form-control footer-input margin-b-20" placeholder="Email" required>
    <input v-model="phone" type="text" class="form-control footer-input margin-b-20" placeholder="Phone" required>
    <textarea v-model="message" class="form-control footer-input margin-b-30" rows="6" placeholder="Message" required></textarea>
    <button type="submit" class="btn-theme btn-theme-sm btn-base-bg text-uppercase">Submit</button>
  </form>
</template>

<script>
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
  methods: {
    submitForm (event) {
      this.createLead()

      this.name = ''
      this.email = ''
      this.phone = ''
      this.message = ''

      event.preventDefault()
    },
    createLead () {
      this.$store.dispatch('createLead', { name: this.name, email: this.email, phone: this.phone, message: this.message })
    }
  }
}
</script>
