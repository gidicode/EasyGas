/* eslint-disable prettier/prettier */
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './index.css'
import './assets/main.css'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import vue3StarRatings from "vue3-star-ratings"
import { 
        faBars, faHouse, faCircleInfo, faMagnifyingGlass,
        faMagnifyingGlassLocation, faUserPlus, faCircleXmark,
        faBell, faCircleUser, faPenToSquare, faCircleCheck,
        faArrowLeft, faHeartCircleCheck
    } 
    from '@fortawesome/free-solid-svg-icons'
import { createPinia } from 'pinia'


library.add(
        faBars, faHouse, faCircleCheck, faMagnifyingGlass,
        faCircleInfo, faMagnifyingGlassLocation, faArrowLeft,
        faUserPlus, faCircleXmark, faBell, faCircleUser, 
        faPenToSquare, faHeartCircleCheck,
    )

const pinia = createPinia()
const app = createApp(App)

app.use(router)
app.use(pinia)
app.component('font-awesome-icon', FontAwesomeIcon)
app.component("vue3-star-ratings", vue3StarRatings);

app.mount('#app')
