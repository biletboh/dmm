<template>
  <div class="component-wrapper">
    <!--========== PARALLAX ==========-->

    <div class="parallax-window" >
      <img src="../assets/img/1920x1080/01.jpg" v-parallax="0.4" class="parallax-img" alt="">
      <div class="parallax-content container">
        <h1 class="carousel-title">Login</h1>
      </div>
    </div>
    <!--========== PARALLAX ==========-->

    <!--========== PAGE LAYOUT ==========-->
    <!-- Our Exceptional Solutions -->
    <div class="content-lg container">
      <div class="row margin-b-40">
        <div class="col-sm-4 col-sm-offset-4 login-form">
          <form  v-on:submit="submitForm" >
            <input v-model="login" type="text" class="form-control footer-input margin-b-20" placeholder="Login" required>
            <input v-model="password" type="password" class="form-control footer-input margin-b-20" placeholder="Password" required>
            <button type="submit" class="btn-theme btn-theme-sm btn-base-bg text-uppercase">Submit</button>
          </form>

        </div>
      </div>
      <!--// end row -->
    </div>
    <!--========== END PAGE LAYOUT ==========-->
  </div>
</template>

<script>
/* eslint-disable */
import Vue from 'vue'
import { User }  from '../api/user'
// import { HTTP } from '../api/common'
import VueSession from 'vue-session'
import VueResource from 'vue-resource'


Vue.use(VueResource)
Vue.use(VueSession)

export default {
  name: 'Login',
  data () {
    return {
      'login': '',
      'password': ''
    }
  },
  methods: {
    submitForm (event) {
      event.preventDefault()
      this.userLogin();

      this.login = ''
      this.password = ''
    },
    userLogin () {
      User.login( { username: this.login, password: this.password } ).then( response => {
        if (response.status === 200) {
          this.$session.start();
          this.$session.set('Token', response.data.token);
          Vue.http.headers.common['Authorization'] = 'Token ' + response.data.token;
          this.$router.push('/dashboard');
        }else{
          alert('Wrong login or password');
        }
      }
      )
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.parallax-img{
  top: -90%;
}
.login-form >>> input{
  background-color: #fff;
  border: 1px solid #ccc;
}
</style>
