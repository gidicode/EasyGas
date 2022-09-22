<!-- eslint-disable prettier/prettier -->
<template>
    <div>
        <form action="" class="grid grid-rows-4 gap-1 justify-items-center">        
            <div>
                <input                         
                v-model="oldPassword" 
                required                       
                type="password" name="Oldpassword" 
                id="oldpassword" class="w-56 border-b-2 focus:outline-none border-[#5400C0]" 
                placeholder="Enter Old PassWord">
                <p class="text-red-500 text-xs w-56 mb-2">{{ errorMessageOld }}</p>
            </div>   
            
            <div>
                <input                         
                v-model="password"
                required
                type="password" name="password1" 
                id="password1" class="w-56 mb-2 focus:outline-none border-b-2 border-[#5400C0]" 
                placeholder="Enter New Password">
                <p class="text-red-500 text-xs w-56 mb-2"> {{ errorMessageNewpass }} </p>
            </div>

            <div>
                <input                         
                v-model="Password2"
                required
                type="password" name="password2" 
                id="password2" class="w-56 mb-2 focus:outline-none border-b-2 border-[#5400C0]" 
                placeholder="Confirm New Password">
            </div>

            <button 
                disabled 
                type="button" 
                v-if="loading" 
                class="p-2 w-64 rounded bg-[#5400C0] hover:bg-[#8700C0] mt-2 text-white focus:ring-4 focus:ring-blue-300 font-medium  dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 inline-flex text-center">
                <svg role="status" class="inline mr-3 w-4 h-4 text-white animate-spin" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="#E5E7EB"/>
                  <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentColor"/>
                </svg>
                Loading...
              </button>

            <button v-else @click.prevent="UpdatePassword" class="w-full rounded bg-[#5400C0] mt-2 text-white text-base p-2">
                Change Password
            </button>                        
        </form>
    </div>
</template>

<script setup>
import UserService from "../../services/user.service"
import { ref } from "vue"
import { useGasStore } from "../../store"

const store = useGasStore()
const oldPassword = ref('')
const password = ref('')
const Password2 = ref('')
const loading = ref(false)
const errorMessageOld = ref(null)
const errorMessageNewpass = ref(null)


const UpdatePassword = () => (
    loading.value = true,
    UserService.changePassword({
       password: password.value,
       password2: Password2.value,
        oldPassword: oldPassword.value
    }).then(
        ()=> {
            loading.value = false
            store.logoutUser()
        }, (error) => {
            console.log(error)
            loading.value = false            
            errorMessageOld.value = error.response.data.old_password.old_password
            errorMessageNewpass.value = error.response.data.password[0]
        }
    )
)
</script>