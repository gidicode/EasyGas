<!-- eslint-disable prettier/prettier -->
<template>
    <div>
        <form action="" class="grid grid-rows-4 gap-1 justify-items-center">        
            <div>
                <input                         
                v-model="oldPassword"                        
                type="password" name="Oldpassword" 
                id="oldpassword" class="w-56 mb-2 border-b-2 border-[#5400C0]" 
                placeholder="Enter Old PassWord">
            </div>   
            
            <div>
                <input                         
                v-model="newPassword"
                type="password" name="password1" 
                id="password1" class="w-56 mb-2 border-b-2 border-[#5400C0]" 
                placeholder="Enter New Password">
            </div>

            <div>
                <input                         
                v-model="confirmPassword"
                type="password" name="password2" 
                id="password2" class="w-56 mb-2 border-b-2 border-[#5400C0]" 
                placeholder="Confirm New Password">
            </div>

            <button class="rounded bg-[#D60097] mt-2 text-white text-base p-2">
                Save
            </button>            
        </form>
    </div>
</template>