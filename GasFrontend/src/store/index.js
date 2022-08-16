/* eslint-disable prettier/prettier */
import {  ref } from "vue";
import { defineStore } from 'pinia'

export const useGasStore = defineStore('gas', () => {
    const showMenu = ref(false)
    const showSignIn = ref(false)

    function changeMenu(values) {
        showMenu.value = values        
    }

    function changeSignin(){
        showSignIn.value = !showSignIn.value        
    }

    return { showMenu, changeMenu, changeSignin, showSignIn}
})