/* eslint-disable prettier/prettier */
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './index.css'
import './assets/main.css'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { 
        faEllipsisVertical, faHouse, faCircleInfo,
        faMagnifyingGlassLocation, faUserPlus, faCircleXmark,
        faBell, faCircleUser, faPenToSquare
    } 
    from '@fortawesome/free-solid-svg-icons'
import { createPinia } from 'pinia'


library.add(faEllipsisVertical, faHouse,
    faCircleInfo, faMagnifyingGlassLocation, 
    faUserPlus, faCircleXmark, faBell, faCircleUser, faPenToSquare)

const pinia = createPinia()
const app = createApp(App)

app.use(router)
app.use(pinia)
app.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app')
