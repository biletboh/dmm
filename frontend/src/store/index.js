import Vue from 'vue'
import Vuex from 'vuex'
import { Lead } from '../api/leads'
import { Brief } from '../api/briefs'
import {
  ADD_LEAD,
  SET_LEADS,
  ACCESS_BRIEFS_OPTIONS,
  ADD_BRIEF_DATA,
  INCREMENT_BRIEF
} from './mutation-types.js'

Vue.use(Vuex)

const state = {
  leads: [],
  briefOptions: [{'choices': []}],
  briefData: {},
  briefCount: 0
}

const getters = {
  leads: state => state.leads,
  briefOptions: state => state.briefOptions,
  briefData: state => state.briefData,
  briefCount: state => state.briefCount
}

const mutations = {
  [ADD_LEAD] (state, lead) {
    state.leads = [lead, ...state.leads]
  },
  [SET_LEADS] (state, { leads }) {
    state.leads = leads
  },
  [ADD_BRIEF_DATA] (state, data) {
    state.briefData[data.briefData.field] = data.briefData.value
  },
  [ACCESS_BRIEFS_OPTIONS] (state, { briefOptions }) {
    state.briefOptions = Object.values(briefOptions.actions.POST)
  },
  [INCREMENT_BRIEF] (state) {
    state.briefCount++
  }
}

// Actions
const actions = {
  createLead ({ commit }, leadData) {
    Lead.create(leadData).then(lead => {
      commit(ADD_LEAD, lead)
    })
  },
  getLeads ({ commit }, token) {
    Lead.list(token).then(leads => {
      commit(SET_LEADS, { leads })
    })
  },
  optionsBrief ({ commit }) {
    Brief.options().then(briefOptions => {
      commit(ACCESS_BRIEFS_OPTIONS, { briefOptions })
    })
  },
  addBriefData ({ commit }, briefData) {
    commit(ADD_BRIEF_DATA, { briefData })
  },
  createBrief ({ commit }, briefData) {
    Brief.create(briefData)
  },
  incrementBriefCount ({ commit }) {
    commit(INCREMENT_BRIEF)
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
