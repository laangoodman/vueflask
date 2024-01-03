<script setup>
import { ref } from 'vue';
import AASearchMenPiao from '@/views/GymPages/snippits/AASearchMenPiao.vue';
import MenPiao from '@/views/GymPages/snippits/MenPiao.vue';


const dropdownItems = ref([
    { name: 'Option 1', code: 'Option 1' },
    { name: 'Option 2', code: 'Option 2' },
    { name: 'Option 3', code: 'Option 3' }
]);

const dropdownItem = ref(null);
</script>

<template>
    <div class="grid">
        <div class="col-12">
            <AASearchMenPiao/>

  
        </div>

        <div class="col-12 ">


        <MenPiao/>

        </div>
    
    </div>
</template>
