
<script setup>
import CCModal from '@/views/GymPages/snippits/CCModal.vue';
import { ref } from 'vue';
import axios from 'axios';

const SportFields = ref([])

const fetchData = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:5000/api/data');
    const data = response.data; // 从响应中获取数据
    SportFields.value = data; // 将数据赋值给 SportFields
    console.log(SportFields.value[0]);
  } catch (error) {
    console.error('获取数据出错:', error);
  }
};

fetchData(); // 调用 fetchData 来获取数据

</script>

<template>
    <div>
        <h1>11111</h1>
    </div>
     
    <div class="grid">
       
        <div class="col-12 md:col-6 lg:col-3" v-for="item in SportFields">
            <div class="surface-card shadow-2 p-3 border-round">
                <div class="flex justify-content-between mb-3">
                    <div>
                        
                        <span class="block text-500 font-medium mb-3">{{ item.vacancy ? '空闲' : '忙碌' }}</span>
                        <div class="text-900 font-medium text-xl">{{ item.discipline }}</div>
                    </div>
                </div>
                <CCModal />
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped></style>
