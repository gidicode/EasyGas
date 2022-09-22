<!-- eslint-disable prettier/prettier -->
<template>
    <div>
        <form class="flex flex-col justify-start" enctype="multipart/form-data">
            <label for="" class="block drop-shadow-md">
                <span class="sr-only"> Choose Profile photo</span>
                <input type="file" accept="image/*" ref="file" @input="showUpload" class="block w-full text-sm text-slate-500
                    file:mr-4 file:py-2 file:px-4
                    file:rounded-full file:border-0
                    file:text-sm file:font-semibold
                    file:bg-violet-50 file:text-violet-700
                    hover:file:bg-violet-100
                ">
            </label>                                   
            <!-- v-if="showProgress" -->
            <section v-if="showUploadState" class="mt-3">                                    
                                            
                  <div class="w-full bg-gray-200 rounded-full dark:bg-gray-700" v-if="showProgress">
                    <div 
                      :value.prop="progress" 
                      max="100"
                      class="bg-blue-600 text-xs font-medium text-blue-100 text-center p-0.5 leading-none rounded-full" 
                      :style="{width: progress + '%'}"> {{progress}}%</div>                  
              </div>              
              <br>
              <button @click.prevent="ChangeProfilePicture" class="w-full rounded-lg bg-[#5400C0] hover:bg-[#8700C0] mt-2 text-white text-base p-2">
                    Upload 
              </button>    
            </section>            
            <small v-if="uploadError"> An eror occured</small>
        </form>
    </div>
</template>

<script setup>
import { ref } from "vue";
import UserService from "../../services/user.service";
import { useGasStore } from "../../store"

const store = useGasStore()
const showUploadState = ref(false);
const showUpload = () => (showUploadState.value = true);
const Submitting = ref(false);
const file = ref(null);
const progress = ref(0)
const uploadError = ref(false)
const showProgress = ref(false)

const ChangeProfilePicture = () => {
  showProgress.value = true
  Submitting.value = true;
  UserService.changeProfilePicture({    
    profile_picture: file.value.files[0],
  }, event => {    
    progress.value = parseInt(Math.round((event.loaded / event.total) * 100))
  }).then(
    () => {
      store.getCurrentUser() 
    },
    (error) => {
      uploadError.value = true
      if(error.response.status == 401){
        store.logoutUser()
      }
      console.log(error); 
    }
  );
};
</script>
