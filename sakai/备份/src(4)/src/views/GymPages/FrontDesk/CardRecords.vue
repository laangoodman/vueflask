<script setup>
import { ref } from 'vue';
import AASearchUser from '@/views/GymPages/snippits/AASearchUser.vue';
import KouCi from '@/views/GymPages/snippits/KouCi.vue';


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
            <AASearchUser/>

  
        </div>

        <div class="col-12 md:col-8">


        <KouCi/>

        </div>
    
    </div>
</template>
