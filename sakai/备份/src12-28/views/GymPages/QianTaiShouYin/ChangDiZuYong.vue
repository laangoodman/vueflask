<script setup>
import { ref } from 'vue';
import AASearchUser from '@/views/GymPages/snippits/AASearchUser.vue';
import ChangDiYuDing from '@/views/GymPages/snippits/ChangDiYuDing.vue';
// import AAModal from '@/views/GymPages/snippits/AAModal.vue';
// import BBModal from '@/views/GymPages/snippits/BBModal.vue';

import TabA from '@/views/GymPages/snippits/TabA.vue';


import { FilterMatchMode } from 'primevue/api';
import { onMounted, onBeforeMount } from 'vue';
import ProductService from '@/service/ProductService';
import { useToast } from 'primevue/usetoast';

</script>
<template> 
    <div class="grid">    
        <div class="col-12 md:col-4">
            <AASearchUser/>
        </div>

        <div class="col-12 md:col-8">
            <ChangDiYuDing/>
        </div>
    </div>
</template>

<style lang="scss" scoped></style>
