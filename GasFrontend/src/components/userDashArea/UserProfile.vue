<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<template>
    <div>
        <header class="flex justify-between mt-5">
            <div>
                <history-back/>
            </div>
            <div> 
                <p class="text-black" @click="clickEdit">
                    <font-awesome-icon icon="fa-solid fa-pen-to-square" />
                </p>
            </div>
        </header>       
        <div v-if="loading" class="text-black">Loading</div>
        <div v-else>
            <div class="grid grid-cols-2 divide-x mt-5">
                 <div class="grid grid-col-1 place-items-center h-min mt-5">                                                            
                    <img :src="userData.profile_picture" alt="profile picture" class=" rounded-full drop-shadow-md w-32 h-32"/> 
                    <div v-if="changeProfileState" class="mt-3">
                      <ChangeProfilePicture/>
                    </div>
                  <p 
                    @click="changeProfile" 
                    class="mt-5 text-sm text-[#D9BCFF] hover:text-[#3E1177] cursor-pointer">Change Picture</p>                  
                </div>                
                                
                 <div v-if="edit" class="grid grid-col-1 place-items-center ">                      
                  <section class="bg-white shadow-md rounded-lg p-5">
                    <p class="mb-4 text-lg font-bold text-[#5400C0]"> Edit Profile </p>
                    <p class="mb-2" v-if="loading">Loading...</p>
                    <p class="mb-3 text-base font-semibold">USERNAME: 
                        <span class="font-normal"> {{ userData.username }}</span>
                    </p>
                    <p class="mb-3 text-base font-semibold">EMAIL: 
                      <span class="font-normal"> {{ userData.email }} </span> 
                    </p>
                    <EditProfileForm
                        :state="userData.state"
                        :lga="userData.lga"
                        :address="userData.Address"
                        :contact="userData.phoneNumber"
                        :profilePicture="userData.profile_picture"                        
                    />

                    <div class="grid grid-col-1 place-items-center">
                      <button 
                        v-if="changePassword"
                        @click="changePasswordState()"
                        class="drop-shadow-md rounded-lg bg-[#D9BCFF] h-9 w-36 mt-10 mb-5 text-sm  text-[#3E1177] p-1">
                        Close
                      </button>
                    
                      <button 
                        v-else
                        @click="changePasswordState()"
                        class="drop-shadow-md rounded-lg bg-[#D9BCFF] hover:bg-[#D2BCFF] h-9 w-36 mt-10 mb-5 text-sm  text-[#3E1177] p-1">
                        Change Password
                      </button>              
                      <div v-if="changePassword">
                        <ChangePassword/>
                      </div>              
                    </div>  
                  </section>                    
                 </div>        
                 <div v-else class="grid grid-col-1 place-items-center">
                    <section class="bg-inherit rounded-lg p-5">
                      <p class="mt-10" v-if="loading">Loading...</p>
                      <p class="mb-3 mt-5 text-base font-semibold">USERNAME: 
                        <span class="font-normal"> {{ userData.username }}</span>
                      </p>

                      <p class="mb-3 text-base font-semibold">EMAIL: 
                        <span class="font-normal"> {{ userData.email }} </span> 
                      </p>

                      <p class="mb-3 text-base font-semibold">STATE:
                        <span class="font-normal"> {{ userData.state }}</span>
                      </p> 

                      <p class="mb-3 text-base font-semibold"> LGA:
                        <span class="font-normal"> {{ userData.lga }}</span> 
                      </p>  

                      <p class="mb-3 text-base font-semibold">ADDRESS: 
                        <span class="font-normal"> {{userData.Address}}</span> 
                      </p>            

                      <p class="mb-3 text-base font-semibold">PHONE CONTACT: 
                        <span class="font-normal"> {{ userData.phoneNumber }} </span> 
                      </p>  
                    </section>                                                                            
                 </div>                                               
            </div>                                           
        </div>
    </div>   
</template>

<script setup>
//import UserService from "../../services/user.service";
import { computed, ref } from "vue";
//import { useAuthUserStore } from "../../store/auth.module";
import { useGasStore } from "../../store";
import EditProfileForm from "../userDashArea/EditProfileForm.vue";
import ChangePassword from "../userDashArea/ChangePassword.vue";
import ChangeProfilePicture from "../userDashArea/ChangeProfilePicture.vue"
import HistoryBack from "../userDashArea/HistoryBack.vue"

const store = useGasStore();
store.getCurrentUser()

const userData = computed(() => store.currentUserData);
const loading = computed(() => store.loading);
const edit = ref(false);
const clickEdit = () => (edit.value = !edit.value)
const changePassword = ref(false);
const changePasswordState = () =>
  (changePassword.value = !changePassword.value);
const changeProfileState = ref(false)
const changeProfile = () =>
  (changeProfileState.value = !changeProfileState.value);
/*
const displayError = ref(false);
const authStore = useAuthUserStore();
const router = useRouter();

function GetUser(){
  loading.value = true;
  return UserService.getLogedInUser().then(
    (response) => {     
      state.value = response.data.state;
      lga.value = response.data.lga;
      address.value = response.data.Address;
      contact.value = response.data.phoneNumber;
      profilePicture.value = response.data.profile_picture;
      loading.value = false;
    },
    (error) => {
      displayError.value = true;
      if (error.response.status == 401) {
        logOut();
      }
    }
  );
}*/
</script>
