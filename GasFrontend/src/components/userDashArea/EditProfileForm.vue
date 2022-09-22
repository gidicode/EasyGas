<!-- eslint-disable prettier/prettier -->
<template>
    <div>
        <form action="" >
            <div>
                <select  
                    id="state" name="state" v-model="state" @input="changeSaveState" 
                    required class="w-64 focus:outline-none mb-3 border-b-2 border-[#5400C0]">
                    <option :value="state" selected >{{state}}</option>
                    <option value="Abia">Abia</option>
                    <option value="Cross River">Cross River</option>
                    <option value="Enugu">Enugu</option>
                    <option value="Ebonyi">Audi</option>
                </select>
                <p class="text-xs text-rose-500 w-56"> {{ errors.state}}</p>
            </div>            
            <div>
                <select  
                    id="lga" name="lga" v-model="lga" required @input="changeSaveState"
                    class="w-64 focus:outline-none border-b-2 mb-3 border-[#5400C0]">
                    <option :value="lga" selected >{{lga}}</option>
                    <option value="Aba">Aba</option>
                    <option value="Ohafia">Ohafia</option>
                    <option value="Arochukwu">Arochukwu</option>
                    <option value="audi">Audi</option>
                </select>
                <p class="text-xs text-rose-500 w-56"> {{ errors.lga}}</p>
            </div>              
            <div>
                <input                         
                v-model="address" @input="changeSaveState"                                     
                type="text" name="address" 
                id="address" class="w-64 focus:outline-none mb-3 border-b-2 border-[#5400C0]" 
                placeholder="Your current address">
                <p class="text-xs text-rose-500 w-56"> {{ errors.address}}</p>
            </div>               
            <div>
                <input                         
                v-model="contact" @input="changeSaveState"
                type="text" name="contact"
                id="contact" class="w-64 focus:outline-none mb-3 border-b-2 border-[#5400C0]" 
                placeholder="070XXXXXXXXX">
                <p class="text-xs text-rose-500 w-56"> {{ errors.contact}}</p>
            </div>  
            
            <section v-if="save">
              <button 
                disabled 
                type="button" 
                v-if="Submitting" 
                class="p-2 w-64 rounded bg-[#5400C0] hover:bg-[#8700C0] mt-2 text-white focus:ring-4 focus:ring-blue-300 font-medium  dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 inline-flex text-center">
                <svg role="status" class="inline mr-3 w-4 h-4 text-white animate-spin" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="#E5E7EB"/>
                  <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentColor"/>
                </svg>
                Loading...
              </button>
          
              <button v-else @click="saveProfile" class="rounded w-64 bg-[#5400C0] hover:bg-[#8700C0] mt-2 text-white text-base p-2">
                  Save
              </button>
            </section>
                                    
            <p v-if="showError500" class="text-xs text-rose-500 w-56">
                An error occured, please try Again
            </p>        
        </form>
    </div>
</template>

<script setup>
import { useForm, useField } from "vee-validate";
import * as yup from "yup";
import UserService from "../../services/user.service"
import { ref } from "vue"
import { useGasStore } from "../../store/"

 const props = defineProps({
    state:String,
    address: String,
    lga: String,
    contact: Number,    
})

const schema = yup.object({
  state: yup.string().required(),
  lga: yup.string().required(),
  address: yup.string().required(),
  contact: yup.number("Ths is a number field").required('This field is required').min(10),  
});

const formValues = {
  state: props.state,
  lga: props.lga,
  address: props.address,
  contact: props.contact,  
}

const { errors, handleSubmit, setFieldError } = useForm({
  validationSchema: schema,
  initialValues: formValues
});

const { value: state} = useField("state");
const { value: lga } = useField("lga");
const { value: address } = useField("address");
const { value: contact } = useField("contact");

const Submitting = ref(false)
const showError500 = ref(false)
const save = ref(false)
const store = useGasStore()
const changeSaveState = () => (save.value = true)

const saveProfile = handleSubmit(() => {
  Submitting.value = true;
  UserService.userEditProfile({
    state: state.value,
    lga: lga.value,
    address: address.value,
    phoneNumber: contact.value,
    reg_complete: true,
  }).then(
    () => {
      Submitting.value = false;
      return store.getCurrentUser()
    },
    (error) => {
      console.log(error)
      Submitting.value = false;
      if (error.response.data.phoneNumber) {
        setFieldError("phoneNumber", "This number has already in use");
      }
      if (error.response.status == 500) {
        showError500.value = true;
      }else if (error.response.status == 401) {
            store.logoutUser()
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