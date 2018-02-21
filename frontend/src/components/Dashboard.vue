<template>
    <div>
    <h2>I am Dashboard</h2>
    <button @click="logout">LOGOUT</button>
    </div>
</template>

<script>
/* eslint-disable */
import Vue from 'vue'
import VueSession from 'vue-session'
import VueResource from 'vue-resource'


Vue.use(VueResource)
Vue.use(VueSession)

export default {
  name: 'Dashboard',
  data () { 
    return {test: true}
},
beforeCreate: function () {
    if (!this.$session.exists()) {
        this.$router.push('/login')
    }
},
methods: {
    logout: function () {
        this.$session.destroy()
        this.$router.push('/') 
    }
}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
