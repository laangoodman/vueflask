<script setup>
import { ref } from 'vue';
import GoodsSalesLeft from '@/views/GymPages/snippits/GoodsSales/GoodsSalesLeft.vue';
import GoodsSalesRight from '@/views/GymPages/snippits/GoodsSales/GoodsSalesRight.vue';


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
            <GoodsSalesLeft/>
  
        </div>

        <div class="col-12 md:col-8">


        <GoodsSalesRight/>

        </div>
    
    </div>
</template>
