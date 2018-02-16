import Vue from 'vue'
import Vuex from 'vuex'
import { Lead } from '../api/leads'
import {
  ADD_LEAD,
  SET_LEADS
} from './mutation-types.js'

Vue.use(Vuex)

const state = {
  leads: [] // list of leads
}

const getters = {
  leads: state => state.leads // get a list from a state
}

const mutations = {
  [ADD_LEAD] (state, lead) {
    state.leads = [lead, ...state.leads]
  },
  [SET_LEADS] (state, { leads }) {
    state.leads = leads
  }
}

// Actions
const actions = {
  createLead ({ commit }, leadData) {
    Lead.create(leadData).then(lead => {
      commit(ADD_LEAD, lead)
    })
  },
  getLead ({ commit }) {
    Lead.list().then(leads => {
      commit(SET_LEADS, { leads })
    })
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
