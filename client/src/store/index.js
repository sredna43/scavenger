import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const state = {
  isAuthenticated: false
}

export const mutations = {
  authenticate: (state) => {
    state.isAuthenticated = true;
  },
  deauthenticate: (state) => {
    state.isAuthenticated = false;
  }
}

export const actions = {
  auth: ({commit}) => {
    commit('authenticate');
  }
}

export const getters = {
  isAuthenticated: state => state.isAuthenticated
}

export const store = new Vuex.Store({
  state,
  mutations,
  actions,
  getters
});
