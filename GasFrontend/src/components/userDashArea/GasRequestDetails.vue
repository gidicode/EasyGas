<!-- eslint-disable prettier/prettier -->
<template>
    <div class="bg-neutral-900/75 relative top-0 w-screen" >    
        <section  class="grid grid-cols-1 place-items-center" @click.self="$emit('hideGasRequestDetail')">
            <div class="bg-white rounded-xl w-1/4 p-4 mt-10 mb-10">
                <p class="text-sm font-bold ml-5 mt-3 mb-6"> 12-05-2022 | 12:00AM</p>                
                <table class="table-auto w-full text-sm text-left text-black">                   
                    <tbody>
                        <tr class="border-b dark:bg-gray-800 dark:border-gray-700">
                            <th scope="row" class="text-slate-300 py-4 px-6 font-medium whitespace-nowrap">
                                KG
                            </th>                                                 
                            <td class="py-4 px-6">10</td>
                        </tr>
                        <tr class="border-b dark:bg-gray-800 dark:border-gray-700">
                            <th scope="row" class="text-slate-300 py-4 px-6 font-medium whitespace-nowrap">
                                STATUS
                            </th>                             
                            <td class="py-4 px-6">Pending</td>                        
                        </tr>
                        <tr class="border-b dark:bg-gray-800 dark:border-gray-700">
                            <th scope="row" class="text-slate-300 py-4 px-6 font-medium whitespace-nowrap">
                                PRICE SOLD
                            </th>                             
                            <td class="py-4 px-6">N780</td>                                                   
                        </tr>
                        <tr class="border-b dark:bg-gray-800 dark:border-gray-700">
                            <th scope="row" class="text-slate-300 py-4 px-6 font-medium whitespace-nowrap">
                                VENDOR
                            </th>                             
                            <td class="py-4 px-6">Raph Gas</td>                                                 
                        </tr>
                        <tr class="border-b dark:bg-gray-800 dark:border-gray-700">
                            <th scope="row" class="text-slate-300 py-4 px-6 font-medium whitespace-nowrap">
                                LOCATION
                            </th>                             
                            <td class="py-4 px-6">Calabar</td>                                                   
                        </tr>
                    </tbody>
                </table>
                
                <p class="text-[#430493] text-sm mt-10">Choose Action</p>
                <div class="flex mt-5 text-sm text-white font-semi-bold mb-10">
                    <div class="flex-1 w-32">
                        <button class="rounded bg-[#EA91D0] p-2 w-24" @click="UpdateActionType('Rate')">
                            Rate
                        </button>
                    </div>
                    <div class="flex-1 w-32">
                        <button class="rounded bg-[#EA91D0] p-2 w-24" @click="UpdateActionType('Favourite')">
                            Favourite
                        </button>
                    </div>
                    <div class="flex-1 w-32">
                        <button class="rounded bg-[#EA91D0] p-2 w-24" @click="UpdateActionType('Comment')">
                            Comment
                        </button>
                    </div>
                </div>                
                <div>
                    <action-page :actionType="actionType"/>
                </div>
            </div>            
        </section>    
    </div>
</template>

<script setup>
import ActionPage from "../userDashArea/ActionPage.vue";
import { ref } from "vue";

const actionType = ref("");

const UpdateActionType = (value) => {
  actionType.value = value;
};


</script>
