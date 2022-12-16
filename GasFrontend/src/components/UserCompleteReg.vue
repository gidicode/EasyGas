<!-- eslint-disable prettier/prettier -->
<template>
  <div class="grid grid-col-2 place-items-center">
    <div class="drop-shadow-md rounded w-6/12 mt-2 p-4">
      <form class="grid grid-cols-1 place-items-center">        
         <p class="text-base font-semibold text-[#3D1174]">
          Please Complete your User registration to proceed.
        </p>  
        <div class="mt-4">
          <label for="state"> State</label>
          <br/>
          <select
            id="state"
            name="state"
            v-model="state"
            required
            class="w-full p-2 border border-[#5400C0] bg-transparent"
          >
            <option value="State" disabled selected>State</option>
            <option value="Abia">Abia</option>
            <option value="Cross River">Cross River</option>
            <option value="Enugu">Enugu</option>
            <option value="Ebonyi">Audi</option>
          </select>
          <p class="text-xs text-rose-500 w-56">{{ errors.state }}</p>
        </div>

        <div class="mt-2">
          <label for="lga"> L.G.A</label>
          <br />
          <select
            id="lga"
            name="lga"
            v-model="lga"
            required
            class="w-56 p-2 border border-[#5400C0]"
          >
            <option value="LGA" disabled selected>LGA</option>
            <option value="Aba">Aba</option>
            <option value="Ohafia">Ohafia</option>
            <option value="fiat">Arochukwu</option>
            <option value="audi">Audi</option>
          </select>
          <p class="text-xs text-rose-500 w-56">{{ errors.lga }}</p>
        </div>

        <div class="mt-2">
          <label for="address">Address</label>
          <br/>
          <input
            v-model="address"
            type="text"
            name="address"
            id="address"
            class="w-56 p-2 border border-[#5400C0]"
            placeholder="Address"
          />
          <p class="text-xs text-rose-500 w-56">{{ errors.address }}</p>
        </div>

        <div class="mt-2">
          <label for="contact">Phone Number</label>
          <br/>
          <input
            v-model="phone_number"
            type="text"
            name="contact"
            id="contact"
            class="w-56 p-2 border border-[#5400C0]"
            placeholder="070XXXXXXXXX"
          />
          <p class="text-xs text-rose-500 w-56">{{ errors.phone_number }}</p>
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
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useGasStore } from "../store";
import UserService from "../services/user.service";
import { useForm, useField } from "vee-validate";
import * as yup from "yup";
import { useRouter } from "vue-router";

const store = useGasStore();
const router = useRouter();

//const accountType = ref(props.accountType)
const schema = yup.object({
  state: yup.string().required(),
  lga: yup.string().required(),
  address: yup.string().required(),
  phone_number: yup
    .string()
    .required()
    .matches(/^[0-9]+$/, "Must be only digits")
    .min(11, "Phone number is not complete")
    .max(11, "You have more than 11 digits"),
});

const { errors, handleSubmit, setFieldError } = useForm({
  validationSchema: schema,
});

const { value: state } = useField("state");
const { value: lga } = useField("lga");
const { value: address } = useField("address");
const { value: phone_number } = useField("phone_number");

const Submitting = ref(false);
const showError500 = ref(false);

const completeUserReg = handleSubmit(() => {
  Submitting.value = true;
  UserService.completeRegistration({
    state: state.value,
    lga: lga.value,
    address: address.value,
    phoneNumber: phone_number.value,
    reg_complete: true,
  }).then(
    () => {
      Submitting.value = false;
      store.getCurrentUser()
      router.push("/dashboard/summary");
      //router.push("/dashboard/registration-complete");
    },
    (error) => {
      Submitting.value = false;
      if (error.response.data.phoneNumber) {
        setFieldError("phone_number", "This number has already in use");
      }
      if (error.response.data.status == 500) {
        showError500.value = true;
      } else if (error.response.data.status == 401) {
        store.logoutUser()
      }
    }
  );
});
</script>

<style scoped>
select:required:invalid {
  color: #4c4457;
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
