/* eslint-disable prettier/prettier */
import {  ref } from "vue";
import { defineStore } from 'pinia'
import UserService from "../services/user.service"
import { useAuthUserStore } from "../store/auth.module"
import { useRouter } from "vue-router";

export const useGasStore = defineStore('gas', () => {
    const showMenu = ref(false)
    const currentUserData = ref(null)
    const responseError = ref(null)
    const loading = ref(false)
    const authStore = useAuthUserStore()
    const router = useRouter()
    const accountType = ref(null)    

    function changeMenu(values) {
        showMenu.value = values        
    }     

    function getCurrentUser(){
        loading.value = true        
        UserService.getLogedInUser().then(
            (response) => {                
                currentUserData.value = response.data
                loading.value = false                                
                return response.data
            }, 
            (error) => {
                loading.value = false
                responseError.value = error.response.status
                if(error.response.status == 401) {
                    return logoutUser()
                }
            }
        )
    }

    function logoutUser (){
        const log = authStore.logout()
        router.push("/login")
        changeMenu(false)
        return log
    }

    return { 
        showMenu, 
        changeMenu, 
        //changeSignin, 
        //howSignIn,
        //changeSignUp,
        //showSignUp,        
        getCurrentUser,
        currentUserData,
        loading,
        logoutUser,
        accountType              
    }
})