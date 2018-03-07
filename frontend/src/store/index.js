/* eslint-disable */
import Vue from 'vue'
import Vuex from 'vuex'
import { Lead } from '../api/leads'
import { Brief } from '../api/briefs'
import {
  ADD_LEAD,
  SET_LEADS,
  ACCESS_BRIEFS_OPTIONS,
  ADD_BRIEF_DATA,
  INCREMENT_BRIEF,
  LEAD_SENT,
  BRIEF_SENT
} from './mutation-types.js'

Vue.use(Vuex)

const state = {
  leads: [],
  briefOptions: [{'choices': []}],
  briefData: {},
  briefCount: 0,
  isLeadSent: false,
  isBriefSent: false
}

const getters = {
  leads: state => state.leads,
  briefOptions: state => state.briefOptions,
  briefData: state => state.briefData,
  briefCount: state => state.briefCount,
  isLeadSent: state => state.isLeadSent,
  isBriefSent: state => state.isBriefSent,

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
  },
  [LEAD_SENT] (state, mark) {
    state.isLeadSent = mark
  },
  [BRIEF_SENT] (state, mark) {
    state.isBriefSent = mark
  }
}

const actions = {
  createLead ({ commit }, leadData) {
    return new Promise((resolve, reject)=>{
      Lead.create(leadData)
      .then(
        lead => {
        commit(ADD_LEAD, lead)
        resolve(lead)
      })
      .catch(
        err => {
        reject(err)
      })
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
  markLeadSent({ commit}, mark){
    commit(LEAD_SENT, mark)
  },
  markBriefSent({ commit}, mark){
    commit(BRIEF_SENT, mark)
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
