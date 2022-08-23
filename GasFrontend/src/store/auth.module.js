/* eslint-disable prettier/prettier */
import AuthService from "../services/auth.service";
import { defineStore } from 'pinia'
import {  ref } from "vue";

const user = JSON.parse(localStorage.getItem('user'))

export const useAuthUserStore = defineStore("auth/user", () => {
    const state = ref(user 
        ? {status: {loggedIn: true}, user} : 
        {status: {loggedIn: false}, user: null})
    
    function login(user) {
        return  AuthService.login(user).then(
            user => {
                state.value.status.loggedIn = true
                state.value.user = user
                return Promise.resolve(user)
            }, 
            error => {
                state.value.status.loggedIn = false
                state.value.user = null
                return Promise.reject(error)
            }
        )
    }

    function logout() {
        AuthService.logout()
        state.value.status.loggedIn = false
        state.value.user = null
    }

    function register(user) {
        return AuthService.register(user).then(
            response => {
                state.value.status.loggedIn = false                
                return Promise.resolve(response.data)
            },
            error => {
                state.value.status.loggedIn = false
                return Promise.reject(error)
            }
        )
    }

    return {login, logout,register, state}
})
