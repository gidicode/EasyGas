<!-- eslint-disable prettier/prettier -->
<template>
    <main class="mt-8">
        <div class="grid grid-cols-1 md:place-items-center">
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
import { onMounted } from "vue";
import UserService from "../../services/user.service";
import { useAuthUserStore } from "../../store/auth.module";
import { useGasStore } from "../../store";
import { useRouter, RouterLink } from "vue-router";

const router = useRouter();
const authStore = useAuthUserStore();
const store = useGasStore();
const logOut = async () => {
  const log = await authStore.logout();
  router.push("/login");
  store.changeMenu(false);
  return log;
};

onMounted(async () => {
  await UserService.curentUser();
  store.getCurrentUser() 

  UserService.getLogedInUser().then(
    (response) => {
      if (response.data.reg_complete == false) {
        router.push("/dashboard/complete-registration");
      } else if (
        response.data.reg_complete == true &&
        response.data.vendor == false
      ) {
        router.push("/dashboard/summary");
      } else {
        router.push("/dashboard/vendor-summary")
      }
    },
    (error) => {
      if (error.response.status == 401) {
        logOut();
      }
    }
  );
});
</script>
