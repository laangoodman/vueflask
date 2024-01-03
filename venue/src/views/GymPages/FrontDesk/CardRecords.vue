<script setup>
import { ref } from 'vue';
import CardRecordsLeft from '@/views/GymPages/snippits/CardRecords/CardRecordsLeft.vue';
import CardRecordsRight from '@/views/GymPages/snippits/CardRecords/CardRecordsRight.vue';


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
            <CardRecordsLeft/>

  
        </div>

        <div class="col-12 md:col-8">


        <CardRecordsRight/>

        </div>
    
    </div>
</template>
