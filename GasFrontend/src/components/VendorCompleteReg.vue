<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<template>
    <div class="grid grid-col-2 place-items-center">                       
      <form @submit.prevent="completeVendorRegistration" class=" mt-4 grid grid-cols-1 place-items-center">
          <p class="text-base font-semibold text-[#3D1174] mt-4">
            Please Complete your Vendor registration to proceed.          
          </p>
          <div class="mt-4">                    
              <label for="businessName">Business name</label>
              <br/>
              <input 
                  v-model="businessName"
                  type="text" name="businessName" 
                  id="businessName" class="w-56 p-2 border border-[#5400C0]" 
                  placeholder="Company name">                   
              <p class="text-xs text-rose-500 w-56">{{errors.businessName}} </p>
          </div>

          <div class="mt-4">                    
              <label for="businessName"> Opening Hours</label>
              <br/>
              <input 
                  v-model="openingHours"
                  type="time" name="openingHours" 
                  id="openingHours" class="w-56 p-2 border border-[#5400C0]" 
                  placeholder="08:00 AM">                   
              <p class="text-xs text-rose-500 w-56"> </p>
          </div>

          <div class="mt-4">                    
              <label for="businessName"> Closing Hours</label>
              <br/>
              <input 
                  v-model="closingHours"
                  type="time" name="closingHours" 
                  id="closingHours" class="w-56 p-2 border border-[#5400C0]" 
                  placeholder="06:00 PM">                   
              <p class="text-xs text-rose-500 w-56"> </p>
          </div>

          <div class="mt-4">                    
              <label for="businessName"> Set Gas Price</label>                    
              <br/>
              <div class="relative">
                <span class="absolute left-2.5 top-3">
                  <img :src="naira" class="w-4 h-4">
                </span>
                <input 
                  v-model="gasPrice"
                  type="number" name="closingHours" 
                  id="closingHours" class="w-56 p-2 pl-8 border border-[#5400C0]" 
                  placeholder="750">                                         
              </div>
              
              <p class="text-xs text-rose-500 w-56">{{errors.gasPrice}}</p>
          </div>    

        <div class="mt-4">
          <label for="bio" >Bio</label>
          <br/>
          <textarea 
            id="bio" 
            rows="4" 
            v-model="bio"
            class="px-2 w-56 text-sm text-gray-900 bg-white border border-[#5400C0] focus:ring-0 dark:text-white dark:placeholder-gray-400" 
            placeholder="About your business..." required>
          </textarea>
          <p class="text-xs text-rose-500 w-56">{{errors.bio}}</p>
      </div>            

      <button
          disabled
          type="button"
          v-if="Submitting"
          class="text-white p-2 w-36 bg-[#8157B6] mb-2 hover:bg-[#8157B8] focus:ring-4 focus:ring-blue-300 font-medium rounded-xl text-sm text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 inline-flex items-center"
        >
          <svg
            role="status"
            class="inline mr-3 w-4 h-4 text-white animate-spin"
            viewBox="0 0 100 101"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
              fill="#E5E7EB"
            />
            <path
              d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
              fill="currentColor"
            />
          </svg>
          Loading...
        </button>             

        <button 
          v-else       
          @click="completeUserReg"
          class="rounded-xl mb-2 bg-[#8157B6] p-2 w-fit h-10 mt-5 text-white text-base text-center font-medium"
          >       
          <span>
            Next
            <font-awesome-icon icon="fa-solid fa-angles-right" />
          </span>
        </button>
      
      <p v-if="showError500" class="text-red">oops! An error occured from us, please try again.</p>   
      </form>      

    </div>
</template>

<script setup>
import { ref } from "vue";
import { useForm, useField } from "vee-validate";
import VenorService from "../services/vendor.service";
import UserService from "../services/user.service";
import * as yup from "yup";
import { useGasStore } from "../store";
import { useRouter } from "vue-router";
import userService from "../services/user.service";

const store = useGasStore();
const router = useRouter();

const schema = yup.object({
  businessName: yup.string().required(),
  openingHours: yup.string().required(),
  closingHours: yup.string().required(),
  gasPrice: yup.number().required(),
  bio: yup.string().required().max(200, "You have exceeded your words limit"),
});

const { errors, handleSubmit, setFieldError } = useForm({
  validationSchema: schema,
});

const { value: businessName } = useField("businessName");
const { value: openingHours } = useField("openingHours");
const { value: closingHours } = useField("closingHours");
const { value: gasPrice } = useField("gasPrice");
const { value: bio } = useField("bio");

const Submitting = ref(false);
const showError500 = ref(false);

const completeVendorRegistration = handleSubmit(() => {
  Submitting.value = true;
  VenorService.creatVendor({
    businessName: businessName.value,
    openingHours: openingHours.value,
    closingHours: closingHours.value,
    gasPrice: gasPrice.value,
    bio: bio.value,
    vendorProfileCompleted: true,
  }).then(
    () => {
      UserService.updateVendorReg({ data: true }).then(() => {
        Submitting.value = false;
        store.getCurrentUser();
        router.push("/dashboard/summary");
      });
    },
    (error) => {
      Submitting.value = false;
      if (error) {
        console.log(error);
        showError500.value = true;
      } else if (error.response.data.status == 401) {
        store.logoutUser();
      }
    }
  );
});
</script>

<style scoped>
select:required:invalid {
  color: #d5bcf4;
}

option[value=""][disabled] {
  display: none;
}
option {
  color: #000000;
  font-size: 14px;
}

::placeholder {
  color: #d5bcf4;
  opacity: 1;
}

:-ms-input-placeholder {
  color: #d5bcf4;
}

::-ms-input-placeholder {
  color: #d5bcf4;
}
</style>
