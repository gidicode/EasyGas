/* eslint-disable prettier/prettier */
import {  ref } from "vue";
import { defineStore } from 'pinia'
import UserService from "../services/user.service"
import { useAuthUserStore } from "../store/auth.module"
import { useRouter } from "vue-router";

export const useGasStore = defineStore('gas', () => {
    const showMenu = ref(false)
    const showSignIn = ref(false)
    const showSignUp = ref(false) 
    const currentUserData = ref(null)
    const responseError = ref(null)
    const loading = ref(false)
    const authStore = useAuthUserStore()
    const router = useRouter()

    function changeMenu(values) {
        showMenu.value = values        
    }

    function changeSignin() {
        showSignIn.value = !showSignIn.value        
    }

    function changeSignUp() {
        return showSignUp.value = !showSignUp.value
    }    

    function getCurrentUser(){
        loading.value = true
        UserService.getLogedInUser().then(
            (response) => {                
                currentUserData.value = response.data
                loading.value = false                
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
        changeSignin, 
        showSignIn,
        changeSignUp,
        showSignUp,
        getCurrentUser,
        currentUserData,
        loading,
        logoutUser              
    }
})