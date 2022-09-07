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
            <h3>VENDORS NEARBY</h3>
            <p class="rounded-xl bg-grey ">0 Result found</p>

            <RouterLink to="/dashboard/vendor-details">
            <section class="grid grid-cols-3 place-items-center mt-10" >
                <div>
                    <h6>Biggins Gas Vendor..</h6>
                </div>

                <div>
                    <p>Star</p>
                </div>

                <div>
                    <font-awesome-icon icon="fa-solid fa-circle-user" />
                </div>
            </section>
            </RouterLink>>
        </div>
    </div>
</template>

