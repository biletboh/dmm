<template>
  <body>
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
            <div class="collapse navbar-collapse">
              <ul class="nav navbar-nav navbar-right">
                <li>
                  <router-link to="/"   class="btn btn-white btn-round"  >
                    Home
                  </router-link>
                </li>
                <li>
                  <a  class="btn btn-white btn-round" @click="logout" >
                    Logout
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
                  <h4 class="card-title">Leads</h4>
                  <div class="card-content">
                    <div class="table-responsive">
                      <table class="table table-striped">
                        <thead>
                          <tr>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Phone</th>
                            <th>Date</th>
                            <th>Message</th>
                            <th>Comment</th>
                            <th>Brief</th>
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
                             <td>{{ lead.message }}</td>
                             <td>{{ lead.comment }}</td>
                             <td v-if="lead.brief">
                               <button
                                 v-on:click="showModal(lead)"
                                 class="btn btn-success btn-round btn-sm"
                                >
                                Brief
                               </button>
                             </td>
                             <td v-else>
                               <span class="btn btn-warning btn-round btn-sm disabled">No Brief</span>
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
    </div>
    <modal name="hello-world" height="auto" :pivotX="0.9">
    <div class="modal-header">
      <h3>Brief Answers</h3>
    </div>
    <div class="modal-body">
      <ul class="list-unstyled">
        <li
          v-for="(answer, label) in modalLead.brief"
          :key="label"
          >
          <p><span class="modal-label">{{ label | capitalize }}:</span> {{ answer }}</p>
        </li>
      </ul>
    </div>
    <div
      class="modal-footer"
    >
      <h3><small>{{ modalLead.name }} <span class="muted">{{ modalLead.email }} {{ modalLead.phone }}</span></small></h3>
    </div>
    </modal>
  </body>
</template>

<script>
/* eslint-disable */
import Vue from 'vue'
import VueSession from 'vue-session'
import VueResource from 'vue-resource'
import { mapGetters } from 'vuex'
import VueMaterial from 'vue-material'
import VModal from 'vue-js-modal'
import Vue2Filters from 'vue2-filters'
 
Vue.use(VueResource)
Vue.use(VueSession)
Vue.use(VueMaterial)
Vue.use(VModal)
Vue.use(Vue2Filters)

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
    }
  },
  beforeCreate: function () {
    if (!this.$session.exists()) {
      this.$router.push('/login')
    }
  },
  beforeMount () {
    this.$store.dispatch('getLeads', this.$session.get('Token'))
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import url(../assets/css/material-dashboard.css);
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
</style>
