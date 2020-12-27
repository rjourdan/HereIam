import Vue from 'vue'
import Router from 'vue-router'
import HereMap from '@/components/HereMap'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HereMap',
      component: HereMap
    }
  ]
})
