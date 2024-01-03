<script setup>
import { ref } from 'vue';
import AASearchHeXiao from '@/views/GymPages/snippits/AASearchHeXiao.vue';

import HeXiao from '@/views/GymPages/snippits/HeXiao.vue';


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
            <AASearchHeXiao/>
            <!-- <AASearchMenPiao/> -->
  
        </div>

        <div class="col-12 ">


        <HeXiao/>

        </div>
    
    </div>
</template>
