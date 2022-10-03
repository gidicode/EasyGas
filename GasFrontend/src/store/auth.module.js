/* eslint-disable prettier/prettier */
import AuthService from "../services/auth.service";
import { defineStore } from 'pinia'
import jwt_decode from "jwt-decode";

export const useAuthUserStore = defineStore("auth/user", () => {
    const user = JSON.parse(localStorage.getItem('user'))            
    const state = user
        ? {status: {loggedIn: true}, user}: 
        {status: {loggedIn: false}, user: null}
    
    function login(user) {
        return  AuthService.login(user).then(
            response => {                
                state.status.loggedIn = true
                const decodeRes = jwt_decode(response.access)                
                state.user = decodeRes
                return Promise.resolve(user)
            }, 
            error => {
                state.status.loggedIn = false
                state.user = null
                return Promise.reject(error)
            }
        )
    }

    function logout() {
        AuthService.logout()
        state.status.loggedIn = false
        state.user = null
    }

    function register(user) {
        return AuthService.register(user).then(
            response => {
                state.status.loggedIn = false                
                return Promise.resolve(response.data)
            },
            error => {
                state.status.loggedIn = false
                return Promise.reject(error)
            }
        )
    }

    return {login, logout,register, state}
})
