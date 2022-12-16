<!-- eslint-disable prettier/prettier -->
<template>
    <main class="mt-8">
        <div v-if="loading"> loading...</div>
        <div class="grid grid-cols-1 md:place-items-center" v-else>
          <section class="flex flex-row justify-between px-3 mt-2 mb-0.5">
             <router-link to="/dashboard/gas-request">
              <section class="rounded-xl bg-[#FFE5F8] w-36 mr-4 h-20 p-2">
                  <p class="text-sm ml-2 mt-1">Gas Request</p>
              </section>
            </router-link>

            <router-link to="/dashboard/vendors-list">
              <section class="rounded-xl bg-[#E5D0FF] w-36 h-20 p-2">
                  <p class="text-sm ml-2 mt-1">Vendors</p>                  
              </section>           
            </router-link>              
          </section>                    
        </div>

         <hr class="mt-9">

         <div class="grid grid-cols-1 place-items-center mt-20">
            <section>        
              <router-link to="/dashboard/vendors-nearme">        
                <button 
                    class="rounded-xl mb-8 bg-[#D60097] 
                        p-2 w-56 h-11
                        text-white text-base 
                        font-medium">
                        <font-awesome-icon icon="fa-solid fa-magnifying-glass-location" />
                        Vendor Near Me
                </button>
              </router-link>
            </section>

            <section>
                <router-link to="/dashboard/search-forfriend">
                <button 
                    class="rounded-xl mb-8 bg-[#A589C9] 
                        p-2 w-56 h-10
                        text-white text-base 
                        font-medium">
                        <font-awesome-icon icon="fa-solid fa-magnifying-glass-location" />
                        For Friend
                </button>
                </router-link>
            </section>
         </div>         
    </main>
</template>

<script setup>
import { computed, watch } from "vue";
import { useGasStore } from "../../store";
import { useRouter, RouterLink } from "vue-router";
import { storeToRefs } from 'pinia'

const router = useRouter();
const store = useGasStore();
const { loading } = storeToRefs(store)

watch(loading, (value) => {
    if (!value) {
      checkUserStatus()
    }
});

function checkUserStatus(){
  const currentUser = computed(() => store.currentUserData);  
  //user not registered
  if (!currentUser.value.reg_complete) {
    router.push("/dashboard/user-complete-registration");
    //user registered and user is vendor but not registered
  } else if (
    currentUser.value.reg_complete &&
    currentUser.value.vendor && 
    !currentUser.value.vendor_reg_complete
  ) {
    router.push("/dashboard/vendor-complete-registration");
  } else {
    router.push("/dashboard/summary");
  }
}
</script>
