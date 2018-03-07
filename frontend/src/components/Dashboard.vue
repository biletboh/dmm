<template>
  <div class="wrapper">
    <div class="sidebar" data-active-color="blue" data-background-color="black" data-image="../assets/img-material/sidebar-1.jpg">
      <div class="logo">
        <a class="simple-text">
          DMM SOLUTIONS
        </a>
      </div>
      <div class="logo logo-mini">
        <a class="simple-text">
          DMM
        </a>
      </div>
      <div class="sidebar-wrapper">
        <div class="user">
          <div class="photo">
            <img src="../assets/img-material/default-avatar.png" />
          </div>
          <div class="info">
            <a data-toggle="collapse" href="#collapseExample" class="collapsed">
              Hi, Admin
            </a>
          </div>
        </div>
        <ul class="nav">
          <li>
            <a href="#">
              <i class="material-icons">dashboard</i>
              <p>Leads</p>
            </a>
          </li>
        </ul>
      </div>
    </div>
    <div class="main-panel">
      <nav class="navbar navbar-transparent navbar-absolute">
        <div class="container-fluid">
          <div class="navbar-minimize">
            <button id="minimizeSidebar" class="btn btn-round btn-white btn-fill btn-just-icon">
              <i class="material-icons visible-on-sidebar-regular">more_vert</i>
              <i class="material-icons visible-on-sidebar-mini">view_list</i>
            </button>
          </div>
          <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse">
              <span class="sr-only">Toggle navigation</span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
          </div>
          <div class="collapse navbar-collapse">
            <ul class="nav navbar-nav navbar-right">
              <li>
                <a  class="btn btn-round btn-info btn-fill btn-just-icon" @click="logout" >
                  <i class="material-icons">power_settings_new</i>
                </a>
              </li>
              <li class="separator hidden-lg hidden-md"></li>
            </ul>
          </div>
        </div>
      </nav>
      <div class="content">
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-12">
              <div class="card">
                <div class="card-header card-header-icon" data-background-color="blue">
                  <i class="material-icons">assignment</i>
                </div>
                <br><br>
                <div class="card-content">
                  <div class="table-responsive">
                    <table class="table table-striped" >
                      <thead>
                        <tr>
                          <th>Name</th>
                          <th>Email</th>
                          <th>Phone</th>
                          <th>Date</th>
                          <th>Message</th>
                          <th>Comment</th>
                          <th class="text-center">Brief</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr
                        v-for="lead in leads"
                        :key="lead.id"
                        >
                        <td>{{ lead.name }}</td>
                        <td>{{ lead.email }}</td>
                        <td>{{ lead.phone }}</td>
                        <td>{{ lead.date }}</td>
                        <td >
                         <span v-if="lead.messages.length > 0" v-on:click="showModalMessage(lead)"
                          class=" tag label label-success">
                        {{lead.messages.length}}</span>
                        <span v-else  class="tag label label-default disabled">
                        {{lead.messages.length}}</span>
                        {{ lead.message }}
                      </td>

                      <td>
                        <div class="form-group">
                          <input class="form-control" @keyup.enter="updateComment(lead.id, lead.comment, $event)"  @focusout="updateComment(lead.id, lead.comment, $event)"  :key="lead.id" v-model="lead.comment" name="comment" type="text" >
                          <span class="text-danger"></span>
                          <!-- <span class="text-success"></span> -->
                        </div>
                      </td>

                      <td class=" text-center" v-if="lead.brief">
                       <button
                       v-on:click="showModal(lead)"
                       class="btn btn-success btn-round btn-sm"
                       >
                       Brief
                     </button>
                   </td>
                   <td class="text-center" v-else>
                     <span class="btn btn-defaut btn-round btn-sm disabled">No Brief</span>
                   </td>
                 </tr>
               </tbody>
             </table>
           </div>
         </div>
       </div>
     </div>
   </div>
 </div>
</div>
</div>
<modal name="hello-world" height="auto" :scrollable="true" :draggable="true" width="50%">
  <div class="modal-header">
    <div class="row">
      <div class="col-md-10">
        <h5>
          {{ modalLead.name }}<br>
          {{ modalLead.email }}<br>
        {{ modalLead.phone }}</h5>
      </div>
      <div class="col-md-2">
        <p class="text-right">
          <i @click="$modal.hide('hello-world')" id="close-btn" class="material-icons">close</i>
        </p>
      </div>
    </div>
  </div>
  <div class="modal-body">
    <div class="row" v-for="(answer, label) in modalLead.brief" :key="label">
      <div class="col-md-2"><span class="modal-label">{{ label | capitalize }}</span></div>
      <div class="col-md-10"><p class="answer">{{ answer }}</p></div>
    </div>
  </div>
</modal>
<modal name="message" height="auto" :scrollable="true" :draggable="true" width="50%">
  <div class="modal-header">
    <div class="row">
      <div class="col-md-10">
        <h5>
          {{ modalLead.name }}<br>
          {{ modalLead.email }}<br>
        {{ modalLead.phone }}</h5>
      </div>
      <div class="col-md-2">
        <p class="text-right">
          <i @click="$modal.hide('message')" id="close-btn" class="material-icons">close</i>
        </p>
      </div>
    </div>
  </div>
  <div class="modal-body">
    <div class="row" v-for="message in modalLead.messages"  :key="message.id">
      <div class="col-md-4"><span class="modal-label">{{ message.date }}</span></div>
      <div class="col-md-8"><p class="answer">{{ message.message }}</p></div>
    </div>
  </div>
</modal>
</div>
</template>

<script>
/* eslint-disable */
import Vue from 'vue'
import VueSession from 'vue-session'
import VueResource from 'vue-resource'
import { mapGetters } from 'vuex'
import VModal from 'vue-js-modal'
import Vue2Filters from 'vue2-filters'
import { Comment }  from '../api/comment'

Vue.use(VueResource)
Vue.use(VueSession)
Vue.use(VModal)
Vue.use(Vue2Filters)

import Bootstrap from '../assets/vendor/material/bootstrap.min.js';
import Tagsinput from '../assets/vendor/material/jquery.tagsinput.js';
import Material from '../assets/vendor/material/material.min.js';
import MaterialDashboard from '../assets/vendor/material/material-dashboard.js';

export default {
  name: 'Dashboard',
  data () {
    return {
      'modalLead': {}
    }
  },
  computed: mapGetters(['leads']),
  methods: {
    logout: function () {
      const confirmation = confirm("Are you sure?")
      if(confirmation){
        this.$session.destroy()
        this.$router.push('/') 
      }
    },
    showModal (lead) {
      this.modalLead = lead
      this.$modal.show('hello-world')
    },
    hideModal () {
      this.$modal.hide('hello-world')
    },
    showModalMessage (lead) {
      this.modalLead = lead
      this.$modal.show('message')
    },
    hideModalMessage () {
      this.$modal.hide('message')
    },
    updateComment(id, data, event){
      // let el_suc = $(event.target).parent().find('span.text-success')
      let el_err = $(event.target).parent().find('span.text-danger')

      Comment.update(id, {"comment": data}, this.$session.get('Token'))
      .then(response => {
        // el_suc.html("Comment was successfully saved")
        // setTimeout(function(){
        //   el_suc.html("")
        // },5000)
      })
      .catch( err => {
        el_err.html("Comment wasn\'t saved: " + err.message)
        setTimeout(function(){
          el_err.html("")
        },5000)
      })
    }
  },
  beforeCreate: function () {
    if (!this.$session.exists()) {
      this.$router.push('/login')
    }
  },
  beforeMount () {
    if (this.$session.exists()) {
      this.$store.dispatch('getLeads', this.$session.get('Token'))
    }
  }
}
</script>

<style scoped>
@import url(../assets/css/material-dashboard.css);
.sidebar-mini .wrapper{
  min-height: 100vh !important;
}
.main-panel {
  overflow: auto;
}
.modal-footer {
  text-align: center;
}
.modal-label {
  font-size: 18px;
}
.btn {
  font-weight: 700;
}
.label {
  font-size: 11px;
}
.wrapper {
  background: #EEEEEE;
}
td{
  font-weight: 200;
  padding: 0 !important;
}
.answer{
  color: #515769;
}
h5{
  font-weight: 600;
  line-height: 30px;
  margin-bottom: 0;
}
#close-btn{
  cursor: pointer;
  font-size: 30px;
}
span.tag{
  cursor: pointer !important;  
}
button.btn-success{
  padding-left:   30px !important;
  padding-right:  30px !important;
}
</style>
