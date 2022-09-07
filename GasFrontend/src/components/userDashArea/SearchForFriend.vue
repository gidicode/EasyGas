<template>
    <div>
        <header class="flex justify-between mt-5">
            <div> <p class="text-black">hello</p></div>
            <div> 
                <p class="text-black" >
                    <font-awesome-icon icon="fa-solid fa-magnifying-glass-location" /> Search
                </p>
            </div>
        </header>

        <div>
            <h1 class="text-center mt-5">Search For Friend</h1>
            <p class="rounded-xl bg-grey text-xs text-center">Enter the location of the person, 
                get your prefered gas vendors around link them up with your friends and family
            </p>
            <img src="@/assets/searchForFriend.jpg" alt="Search for friend gas" class="">
            
            <form action="" class="mt-6 grid grid-cols-1 place-items-center">
                <div class="mt-4">                                        
                    <select id="state" name="state" v-model="state" required class="w-56 p-2 border border-[#5400C0] bg-transparent">
                        <option value="Select State" placeholder="ggg" disabled selected>Select State</option>
                        <option value="Abia">Abia</option>
                        <option value="Cross River">Cross River</option>
                        <option value="Enugu">Enugu</option>
                        <option value="Ebonyi">Audi</option>
                    </select>
                    
                </div>
                <div class="mt-4">                                        
                    <select id="lga" name="lga" v-model="lga" required class="w-56 p-2 border border-[#5400C0]">
                        <option value="Select LGA" disabled selected >LGA</option>
                        <option value="Aba">Aba</option>
                        <option value="Ohafia">Ohafia</option>
                        <option value="fiat">Arochukwu</option>
                        <option value="audi">Audi</option>
                    </select>
                </div>

                <button 
                    class="rounded-xl mt-5 bg-[#A589C9] 
                        p-2 w-56 h-11
                        text-white text-base 
                        font-medium">                        
                        Search
                </button>
            </form>
        </div>
    </div>
</template>

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