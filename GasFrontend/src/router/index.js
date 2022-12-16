/* eslint-disable prettier/prettier */
import { createRouter, createWebHistory } from 'vue-router'
import WelcomePage from '../views/WelcomePage.vue'
import UsersDashboard from '../views/UsersDashboard.vue'
import UserCompleteReg from '../components/UserCompleteReg.vue'
import VendorCompleteReg from '../components/VendorCompleteReg.vue'
import RegistrationComplete from '../components/RegistrationComplete.vue'
import UserDashBoard from '../components/userDashArea/UserDashBoard.vue'
import UserProfile from '../components/userDashArea/UserProfile.vue'
import Signin from '../components/SignIn.vue'
import SignUp from "../components/SignUp.vue"
import VendorsNearMe from "../components/userDashArea/VendorsNearMe.vue"
import SearchForFriend from "../components/userDashArea/SearchForFriend.vue"
import VendorDetails from "../components/userDashArea/VendorDetails.vue"
import GasRequest from "../components/userDashArea/GasRequest.vue"
import VendorsList from "../components/userDashArea/VendorsList.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: WelcomePage
    },    

    {
      path: '/login',
      name: 'login',
      component: Signin
    },
    {
      path: '/signUp',
      name: 'signUp',
      component: SignUp
    },
    {
      path: '/dashboard',
      name: 'user-dashboard',
      component: UsersDashboard,
      children: [
          {
            path: 'user-complete-registration',
            component: UserCompleteReg,
          }, {
            path: 'vendor-complete-registration',
            component: VendorCompleteReg,
          }, {
            path: 'registration-complete',
            component: RegistrationComplete,
          }, {
            path: 'summary',
            component: UserDashBoard,
          }, {
            path: 'user-profile',
            component: UserProfile
          }, {
            path: 'vendors-nearme',
            component: VendorsNearMe
          }, {
            path: 'search-forfriend',
            component: SearchForFriend
          }, {
            path: "vendor-details",
            component: VendorDetails
          }, {
            path: "gas-request",
            component: GasRequest
          },
          {
            path:"vendors-list",
            component: VendorsList
          }
      ]
    }
  ]
})

export default router
