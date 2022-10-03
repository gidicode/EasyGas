<!-- eslint-disable prettier/prettier -->
<template>
    <div>
        <section v-if="props.actionType == 'Rate'">
            <vue3starRatings 
                v-model="rating"
                starSize="23"
            />        
            <p class="text-sm text-center">Submit</p>
        </section>        

        <section v-else-if="props.actionType == 'Favourite'" class="text-center mb-20 font-bold text-emerald-500">
            <font-awesome-icon class="text-xl" icon="fa-solid fa-circle-check" />
            <p class="text-sm">Added to Favourite</p>
        </section>

        <section v-else-if="props.actionType == 'Comment'">            
            <action-comment/>
        </section>
    </div>
</template>
<script setup>
import vue3starRatings from "vue3-star-ratings"
import ActionComment from "../userDashArea/ActionComment.vue"
import { ref } from "vue"

const rating = ref(0)
const props = defineProps({
    actionType: String
})
</script>