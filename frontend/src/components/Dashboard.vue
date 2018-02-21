<template>

  <body>
    <div class="wrapper">
      <div class="sidebar" data-active-color="blue" data-background-color="black" data-image="../assets/img-material/sidebar-1.jpg">
            <!--
        Tip 1: You can change the color of active element of the sidebar using: data-active-color="purple | blue | green | orange | red | blue"
        Tip 2: you can also add an image using data-image tag
        Tip 3: you can change the color of the sidebar with data-background-color="white | black"
      -->
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
          <img src="../assets/img-material/faces/avatar.jpg" />
        </div>
        <div class="info">
          <a data-toggle="collapse" href="#collapseExample" class="collapsed">
            Admin
            <!--  <b class="caret"></b> -->
          </a>
<!--                 <div class="collapse" id="collapseExample">
                    <ul class="nav">
                        <li>
                            <a href="#">My Profile</a>
                        </li>
                        <li>
                            <a href="#">Edit Profile</a>
                        </li>
                        <li>
                            <a href="#">Settings</a>
                        </li>
                    </ul>
                  </div> -->
                </div>
              </div>
              <ul class="nav">
                <li>
                  <a href="#">
                    <i class="material-icons">dashboard</i>
                    <p>Leads</p>
                  </a>
                </li>
<!--             <li>
                <a data-toggle="collapse" href="#pagesExamples">
                    <i class="material-icons">image</i>
                    <p>Pages
                        <b class="caret"></b>
                    </p>
                </a>
                <div class="collapse" id="pagesExamples">
                    <ul class="nav">
                        <li>
                            <a href="../pages/pricing.html">Pricing</a>
                        </li>
                        <li>
                            <a href="../pages/timeline.html">Timeline</a>
                        </li>
                        <li>
                            <a href="../pages/login.html">Login Page</a>
                        </li>
                        <li>
                            <a href="../pages/register.html">Register Page</a>
                        </li>
                        <li>
                            <a href="../pages/lock.html">Lock Screen Page</a>
                        </li>
                        <li>
                            <a href="../pages/user.html">User Profile</a>
                        </li>
                    </ul>
                </div>
            </li>
            <li>
                <a data-toggle="collapse" href="#componentsExamples">
                    <i class="material-icons">apps</i>
                    <p>Components
                        <b class="caret"></b>
                    </p>
                </a>
                <div class="collapse" id="componentsExamples">
                    <ul class="nav">
                        <li>
                            <a href="../components/buttons.html">Buttons</a>
                        </li>
                        <li>
                            <a href="../components/grid.html">Grid System</a>
                        </li>
                        <li>
                            <a href="../components/panels.html">Panels</a>
                        </li>
                        <li>
                            <a href="../components/sweet-alert.html">Sweet Alert</a>
                        </li>
                        <li>
                            <a href="../components/notifications.html">Notifications</a>
                        </li>
                        <li>
                            <a href="../components/icons.html">Icons</a>
                        </li>
                        <li>
                            <a href="../components/typography.html">Typography</a>
                        </li>
                    </ul>
                </div>
            </li>
            <li>
                <a data-toggle="collapse" href="#formsExamples">
                    <i class="material-icons">content_paste</i>
                    <p>Forms
                        <b class="caret"></b>
                    </p>
                </a>
                <div class="collapse" id="formsExamples">
                    <ul class="nav">
                        <li>
                            <a href="../forms/regular.html">Regular Forms</a>
                        </li>
                        <li>
                            <a href="../forms/extended.html">Extended Forms</a>
                        </li>
                        <li>
                            <a href="../forms/validation.html">Validation Forms</a>
                        </li>
                        <li>
                            <a href="../forms/wizard.html">Wizard</a>
                        </li>
                    </ul>
                </div>
            </li>
            <li class="active">
                <a data-toggle="collapse" href="#tablesExamples" aria-expanded="true">
                    <i class="material-icons">grid_on</i>
                    <p>Tables
                        <b class="caret"></b>
                    </p>
                </a>
                <div class="collapse in" id="tablesExamples">
                    <ul class="nav">
                        <li>
                            <a href="../tables/regular.html">Regular Tables</a>
                        </li>
                        <li class="active">
                            <a href="../tables/extended.html">Extended Tables</a>
                        </li>
                        <li>
                            <a href="../tables/datatables.net.html">DataTables.net</a>
                        </li>
                    </ul>
                </div>
            </li>
            <li>
                <a data-toggle="collapse" href="#mapsExamples">
                    <i class="material-icons">place</i>
                    <p>Maps
                        <b class="caret"></b>
                    </p>
                </a>
                <div class="collapse" id="mapsExamples">
                    <ul class="nav">
                        <li>
                            <a href="../maps/google.html">Google Maps</a>
                        </li>
                        <li>
                            <a href="../maps/fullscreen.html">Full Screen Map</a>
                        </li>
                        <li>
                            <a href="../maps/vector.html">Vector Map</a>
                        </li>
                    </ul>
                </div>
            </li>
            <li>
                <a href="../widgets.html">
                    <i class="material-icons">widgets</i>
                    <p>Widgets</p>
                </a>
            </li>
            <li>
                <a href="../charts.html">
                    <i class="material-icons">timeline</i>
                    <p>Charts</p>
                </a>
            </li>
            <li>
                <a href="../calendar.html">
                    <i class="material-icons">date_range</i>
                    <p>Calendar</p>
                </a>
              </li> -->
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
                <a class="navbar-brand" href="#"> Extended Tables </a>
              </div>
              <div class="collapse navbar-collapse">
                <ul class="nav navbar-nav navbar-right">
<!--                   <li>
                    <a href="#pablo" class="dropdown-toggle" data-toggle="dropdown">
                      <i class="material-icons">dashboard</i>
                      <p class="hidden-lg hidden-md">Dashboard</p>
                    </a>
                  </li>
                  <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                      <i class="material-icons">notifications</i>
                      <span class="notification">5</span>
                      <p class="hidden-lg hidden-md">
                        Notifications
                        <b class="caret"></b>
                      </p>
                    </a>
                    <ul class="dropdown-menu">
                      <li>
                        <a href="#">Mike John responded to your email</a>
                      </li>
                      <li>
                        <a href="#">You have 5 new tasks</a>
                      </li>
                      <li>
                        <a href="#">You're now friend with Andrew</a>
                      </li>
                      <li>
                        <a href="#">Another Notification</a>
                      </li>
                      <li>
                        <a href="#">Another One</a>
                      </li>
                    </ul>
                  </li> -->
                  <li>
                    <a  class="btn btn-white btn-round" @click="logout" >
                      Logout
                    </a>
                  </li>
                  <li class="separator hidden-lg hidden-md"></li>
                </ul>
<!--                 <form class="navbar-form navbar-right" role="search">
                  <div class="form-group form-search is-empty">
                    <input type="text" class="form-control" placeholder="Search">
                    <span class="material-input"></span>
                  </div>
                  <button type="submit" class="btn btn-white btn-round btn-just-icon">
                    <i class="material-icons">search</i>
                    <div class="ripple-container"></div>
                  </button>
                </form> -->
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
                    <h4 class="card-title">Striped Table</h4>
                    <div class="card-content">
                      <div class="table-responsive">
                        <table class="table table-striped">
                          <thead>
                            <tr>
                              <th class="text-center">#</th>
                              <th>Name</th>
                              <th>Email</th>
                              <th>Phone</th>
                              <th>Message</th>
                              <th>Comment</th>
                              <th>Date</th>
                              <th>Brief</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr v-for="(lead, index) in leads" :key="lead.id">
                              <td class="text-center">{{ index }}</td>
                              <td>{{lead.name}}</td>
                              <td>{{lead.email}}</td>
                              <td>{{lead.phone}}</td>
                              <td>{{lead.message}}</td>
                              <td>{{lead.comment}}</td>
                              <td>{{lead.date}}</td>
                              <td>{{lead.brief}}</td>
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
<!--     <footer class="footer">
    <div class="container-fluid">
        <nav class="pull-left">
            <ul>
                <li>
                    <a href="#">
                        Home
                    </a>
                </li>
                <li>
                    <a href="#">
                        Company
                    </a>
                </li>
                <li>
                    <a href="#">
                        Portfolio
                    </a>
                </li>
                <li>
                    <a href="#">
                        Blog
                    </a>
                </li>
            </ul>
        </nav>
        <p class="copyright pull-right">
            &copy;
            <a href="http://www.creative-tim.com">Creative Tim</a>, made with love for a better web
        </p>
    </div>
  </footer> -->
</div>
</div>
</body>
</template>

<script>
/* eslint-disable */
import Vue from 'vue'
import VueSession from 'vue-session'
import VueResource from 'vue-resource'
import { Lead }  from '../api/leads'


Vue.use(VueResource)
Vue.use(VueSession)

export default {
  name: 'Dashboard',
  data () { 
    return {leads: []}
  },
  beforeCreate: function () {
    if (!this.$session.exists()) {
      this.$router.push('/login')
    }
  },
  created(){
    this.showLeads()
  },
  methods: {
    logout: function () {
      const confirmation = confirm("Are you sure?")
      if(confirmation){
        this.$session.destroy()
        this.$router.push('/') 
      }
    },
    showLeads: function(){
      this.leads = Lead.list()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import url(../assets/css/material-dashboard.css);
</style>
