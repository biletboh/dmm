/* eslint-disable */
import { HTTP }  from './common'
// import Vue from 'vue'
// import VueSession from 'vue-session'
// import VueResource from 'vue-resource'


// Vue.use(VueResource)
// Vue.use(VueSession)

export const User = {
  login (config) {
    return HTTP.post('/auth/', config)
    .then( response => {
        return response
  })
    .catch( err => {
        return err
    })
}
}