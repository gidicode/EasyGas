<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<template>
    <div>
        <header class="flex justify-between mt-5">
            <div> <p class="text-black">hello</p></div>
            <div> 
                <p class="text-black" @click="clickEdit">
                    <font-awesome-icon icon="fa-solid fa-pen-to-square" />
                </p>
            </div>
        </header>

        <section class="grid grid-col-2 place-items-center mt-5">                        
            <img :src="userData.profile_picture" alt="profile picture" class="rounded-full w-28 h-28"/>            
        </section>

        <div>
            <div class="grid grid-cols-2 mt-2">
                <section class="text-base font-semibold text-right mr-2">
                    <p class="mb-2" >USERNAME</p>                    
                    <p class="mb-2">EMAIL</p>
                    <p class="mb-2">STATE</p>
                    <p class="mb-2">LGA</p>
                    <p class="mb-2">ADDRESS</p>
                    <p class="mb-2">CONTACT</p>                    
                </section>

                 <section  v-if="edit">
                    <p class="mb-2" v-if="loading">Loading...</p>
                    <p class="mb-2">{{ userData.username }}</p>                    
                    <p class="mb-2">{{ userData.email }}</p>    
                    <EditProfileForm
                        :state="state"
                        :lga="lga"
                        :address="address"
                        :contact="contact"
                        :profilePicture="profilePicture"                        
                    />
                 </section>        
                 <section v-else>                    
                    <p class="mb-2" v-if="loading">Loading...</p>
                    <p class="mb-2">{{ userData.username }}</p>                    
                    <p class="mb-2">{{ userData.email }}</p>                                        
                    <p class="mb-2">{{ userData.state }}</p>                                                     
                    <p class="mb-2">{{ userData.lga }}</p>                                     
                    <p class="mb-2">{{ userData.Address }}</p>                                                                         
                    <p class="mb-2">{{ userData.phoneNumber }}</p>                                        
                 </section>                                               
            </div>             
            <div>
              <button 
                v-if="changePassword"
                @click="changePasswordState()"
                class="rounded-xl bg-[#D60097] mt-10 mb-5 text-white p-2 w-53 h-11">
                Close
              </button>
            
              <button 
                v-else
                @click="changePasswordState()"
                class="rounded-xl bg-[#D60097] mt-10 mb-5 text-white p-2 w-53 h-11">
                Change Password
              </button>              
              <section v-if="changePassword">
                <ChangePassword/>
              </section>              
            </div>                    
        </div>
    </div>   
</template>

<script setup>
import UserService from "../../services/user.service";
import { onMounted, ref } from "vue";
import { useAuthUserStore } from "../../store/auth.module";
import { useGasStore } from "../../store";
import { useRouter } from "vue-router";
import EditProfileForm from "../userDashArea/EditProfileForm.vue";
import ChangePassword from "../userDashArea/ChangePassword.vue";

const store = useGasStore();
const authStore = useAuthUserStore();
const router = useRouter();

const userData = ref({});
const displayError = ref(false);
const loading = ref(false);
const logOut = async () => {
  const log = await authStore.logout();
  router.push("/login");
  store.changeMenu(false);
  return log;
};

const edit = ref(false);

const clickEdit = () => (edit.value = !edit.value)
const changePassword = ref(false);
const changePasswordState = () =>
  (changePassword.value = !changePassword.value);

const state = ref("");
const lga = ref("");
const address = ref("");
const contact = ref("");
const profilePicture = ref("")

onMounted(async () => {
  await UserService.curentUser();
  loading.value = true;
  UserService.getLogedInUser().then(
    (response) => {
      console.log(response)
      userData.value = response.data;
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
});
</script>
