<script setup>
import { ref } from 'vue';
import CardsSales from '@/views/GymPages/snippits/CardsSales/CardsSalesLeft.vue';
import CardsSalesRight from '@/views/GymPages/snippits/CardsSales/CardsSalesRight.vue';
import CardsSalesLeft from '../snippits/CardsSales/CardsSalesLeft.vue';


const dropdownItems = ref([
    { name: 'Option 1', code: 'Option 1' },
    { name: 'Option 2', code: 'Option 2' },
    { name: 'Option 3', code: 'Option 3' }
]);

const dropdownItem = ref(null);
</script>

<template>
    <div class="grid">
        <div class="col-12 md:col-4">
            <CardsSalesLeft/>

  
        </div>

        <div class="col-12 md:col-8">


        <CardsSalesRight/>

        </div>
    
    </div>
</template>
