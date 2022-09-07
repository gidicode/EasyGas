<!-- eslint-disable prettier/prettier -->
<template>
    <div>
        <form action="">
            <div>
                <select  
                    id="state" name="state" v-model="state" 
                    required class="w-36 mb-2 border-b-2 border-[#5400C0] bg-transparent">
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
                    id="lga" name="lga" v-model="lga" required 
                    class="w-36 border-b-2 mb-2 border-[#5400C0]">
                    <option :value="lga" selected >{{lga}}</option>
                    <option value="Aba">Aba</option>
                    <option value="Ohafia">Ohafia</option>
                    <option value="fiat">Arochukwu</option>
                    <option value="audi">Audi</option>
                </select>
                <p class="text-xs text-rose-500 w-56"> {{ errors.lga}}</p>
            </div>              
            <div>
                <input                         
                v-model="address"                                        
                type="text" name="address" 
                id="address" class="w-36 mb-2 border-b-2 border-[#5400C0]" 
                placeholder="Your current address">
                <p class="text-xs text-rose-500 w-56"> {{ errors.address}}</p>
            </div>               
            <div>
                <input                         
                v-model="contact"
                type="text" name="contact"
                id="contact" class="w-36 mb-2 border-b-2 border-[#5400C0]" 
                placeholder="070XXXXXXXXX">
                <p class="text-xs text-rose-500 w-56"> {{ errors.contact}}</p>
            </div>          
            <button @click="saveProfile" class="rounded bg-[#D60097] mt-2 text-white text-base p-2">
                Save
            </button>            
            
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
import { useAuthUserStore } from "../../store/auth.module"
import { useGasStore } from "../../store/"
import { useRouter } from "vue-router";

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
const store = useGasStore()
const router = useRouter()
const authStore = useAuthUserStore()
const logOut = async () => {
    const log = await authStore.logout()
    router.push('/login')
    store.changeMenu(false)
    return log
}

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
      UserService.getLogedInUser()
    },
    (error) => {
      console.log(error)
      Submitting.value = false;
      if (error.response.data.phoneNumber) {
        setFieldError("phoneNumber", "This number has already in use");
      }
      if (error.response.data.status == 500) {
        showError500.value = true;
      }else if (error.response.data.status == 401) {
            logOut()
      }
    }
  );
});
</script>