<!-- eslint-disable prettier/prettier -->
<template>
    <main class="mt-8">
        <div class="grid grid-cols-2 gap-4 place-items-center">
            <section class="rounded-xl bg-[#FFE5F8] w-36 h-20 p-2">
                <p class="text-xs ml-2 mt-1 font-medium">Gas Request</p>
            </section>

            <section class="rounded-xl bg-[#E5D0FF] w-36 h-20 p-2">
                <p class="text-xs ml-2 mt-1 font-medium">Vendors</p>
            </section>           
        </div>
         <hr class="mt-9">

         <div class="grid grid-cols-1 place-items-center mt-20">
            <section>                
                <button 
                    class="rounded-xl mb-8 bg-[#D60097] 
                        p-2 w-56 h-11
                        text-white text-base 
                        font-medium">
                        <font-awesome-icon icon="fa-solid fa-magnifying-glass-location" />
                        Vendor Near Me
                </button>
            </section>

            <section>
                
                <button 
                    class="rounded-xl mb-8 bg-[#A589C9] 
                        p-2 w-56 h-10
                        text-white text-base 
                        font-medium">
                        <font-awesome-icon icon="fa-solid fa-magnifying-glass-location" />
                        For Friend
                </button>
            </section>
         </div>

         <div class="grid grid-cols-1 place-items-center mt-20">            
            <img src="@/assets/Locate.png" alt="Locate Gas Vendor" class="h-64 w-64 opacity-40">            
         </div>
    </main>
</template>

<script setup>
import { onMounted} from "vue"
import UserService from "../../services/user.service";
import { useAuthUserStore } from "../../store/auth.module";
import { useGasStore } from '../../store'
import { useRouter } from "vue-router";

const router = useRouter();
const authStore = useAuthUserStore();
const store = useGasStore()
const logOut = async () => {
    const log = await authStore.logout()
    router.push('/login')
    store.changeMenu(false)
    return log
}

onMounted( async () => {  
  await UserService.curentUser()

  UserService.getLogedInUser().then(
    (response) => {
      if (response.data.reg_complete == false) {
        router.push("/dashboard/complete-registration");
      } else {
        router.push("/dashboard/summary");
      }
    },
    (error) => {
      console.log(error);
      if (error.response.status == 401) {
        logOut()
      }
    }
  );
});
</script>
