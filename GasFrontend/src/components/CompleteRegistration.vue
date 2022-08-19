<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<template>
    <div class="grid grid-col-2 place-items-center">
        <div class="mt-16">
            <p class="text-xs font-semibold text-[#3D1174]"> Please Complete your registration to proceed.</p>
        </div>
        <div class="bg-[#FAF5FF] drop-shadow-md rounded w-64 mt-10 p-4">
            <form action="" class="grid grid-cols-1 place-items-center">
                <div class="mt-4">                    
                    <select id="state" name="state" required class="w-56 p-2 border border-[#5400C0] bg-transparent">
                        <option value="" disabled selected hidden>State</option>
                        <option value="volvo">Abia</option>
                        <option value="saab">Saab</option>
                        <option value="fiat">Fiat</option>
                        <option value="audi">Audi</option>
                    </select>
                </div>

                <div class="mt-4">                    
                    <select id="lga" name="lga" required class="w-56 p-2 border border-[#5400C0]">
                        <option value="" disabled selected hidden>LGA</option>
                        <option value="volvo">Aba</option>
                        <option value="saab">Ohafia</option>
                        <option value="fiat">Arochukwu</option>
                        <option value="audi">Audi</option>
                    </select>
                </div>

                <div class="mt-4">
                    <input 
                        type="text" name="address" 
                        id="address" class="w-56 p-2 border border-[#5400C0]" 
                        placeholder="Address">
                </div>
                
                <div class="mt-4">
                    <input 
                        type="text" name="contact" 
                        id="contact" class="w-56 p-2 border border-[#5400C0]" 
                        placeholder="070XXXXXXXXX">
                </div>

                <div class="mt-5">
                        <RouterLink to= "/dashboard/registration-complete">
                            <button 
                                class="rounded-xl mb-2 bg-[#8157B6] 
                                    p-2 w-36 h-10
                                    text-white text-base 
                                    font-medium">
                                    Proceed
                            </button>
                        </RouterLink>
                    </div>  
            </form>
        </div>

    </div>
</template>

<style scoped>
select:required:invalid {
        color: #D5BCF4;
      }
      
option[value=""][disabled]{
    display: none;    
}
option{
    color: #000000;
    font-size: 14px;
}

::placeholder{
    color: #D5BCF4;
    opacity: 1;
}

:-ms-input-placeholder{
    color: #D5BCF4;
}

::-ms-input-placeholder{
    color: #D5BCF4;
}
</style>