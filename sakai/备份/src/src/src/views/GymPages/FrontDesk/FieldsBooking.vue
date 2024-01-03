<script setup>
import { ref } from 'vue';
import FieldsBookingLeft from '@/views/GymPages/snippits/FieldsBooking/FieldsBookingLeft.vue';
import FieldsBookingRight from '@/views/GymPages/snippits/FieldsBooking/FieldsBookingRight.vue';
import { FilterMatchMode } from 'primevue/api';
import { onMounted, onBeforeMount } from 'vue';
import ProductService from '@/service/ProductService';
import { useToast } from 'primevue/usetoast';
import { store } from '@/views/GymPages/Gymjs/store1.js'; // Adjust the path as needed

const isUserSearchButtonVisible = ref(false);


</script>

<template> 


    <div class="grid">    
        <div class="col-12 md:col-4">
            <!-- 页面左边 -->




            <FieldsBookingLeft/>
        </div>

        <div class="col-12 md:col-8">
            <!-- 页面右边 -->



            <FieldsBookingRight/>
        </div>
    </div>
    
</template>

<style lang="scss" scoped></style>
