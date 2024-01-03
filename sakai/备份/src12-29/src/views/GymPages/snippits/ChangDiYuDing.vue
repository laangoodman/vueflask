
<script setup>
    import CCModal from '@/views/GymPages/snippits/CCModal.vue';
    import axios from 'axios';
    import { ref } from 'vue';




const fetchData = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:5000/SportFields');
        console.log('11');

    } catch (error) {
        console.log('11');

    }
};

</script>

<template>
    <div class="grid">
        <div class="col-12 md:col-6 lg:col-3" >
            <div class="surface-card shadow-2 p-3 border-round">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">66</span>
                        <div class="text-900 font-medium text-xl">66</div>
                    </div>    
                </div>
                <CCModal/>
            </div>
        </div>      
    </div>
    <div class="grid">
        <div class="col-12 md:col-6 lg:col-3" v-for="item in aa">
            <div class="surface-card shadow-2 p-3 border-round">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">{{ item.vacancy ? '空闲' : '忙碌' }}</span>
                        <div class="text-900 font-medium text-xl">{{item. disciplines}}</div>
                    </div>    
                </div>
                <CCModal/>
            </div>
        </div>      
    </div>

</template>

<style lang="scss" scoped></style>
