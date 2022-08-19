/* eslint-disable prettier/prettier */
import { createRouter, createWebHistory } from 'vue-router'
import WelcomePage from '../views/WelcomePage.vue'
import UsersDashboard from '../views/UsersDashboard.vue'
import CompleteRegistration from '../components/CompleteRegistration.vue'
import RegistrationComplete from '../components/RegistrationComplete.vue'
import UserDashBoard from '../components/userDashArea/UserDashBoard.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: WelcomePage
    },    

    {
      path: '/dashboard',
      name: 'user-dashboard',
      component: UsersDashboard,
      children: [
          {
            path: 'complete-registration',
            component: CompleteRegistration,
          }, {
            path: 'registration-complete',
            component: RegistrationComplete,
          }, {
            path: 'summary',
            component: UserDashBoard,
          }
      ]
    }
  ]
})

export default router
