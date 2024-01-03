
<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { watch } from 'vue';
import { store } from '@/views/GymPages/snippits/CardsSales/CardsSales.js'; // Adjust the path as needed

// import { store } from '@/views/GymPages/Gymjs/store2.js'; // store1是场地租用store2商品销售



const categories = ref([
  { id: 1, name: '全部计次项目' },
  { id: 2, name: '计次商品' },
  { id: 3, name: '培训商品' },
  { id: 4, name: '私教课程' }
  // Add more categories as needed
]);

const goods = ref([
    { id: 1, name: '游泳单词', price:20},
    { id: 2, name: '我的专属课程',price:1},
    { id: 3, name: '私教课程',price:0},
    { id: 4, name: '抖音团购9.9',price:0.1 },
])


// Function to filter goods by category
const filterGoods = (categoryId) => {
  if (categoryId === 1) return goods.value; // Return all goods for '全部'
  return goods.value.filter(item => item.categoryId === categoryId);
};


const selectItem = (item) => {
  store.showItemDetails(item);
  console.log('stored' + item.name);
};
</script>


<template>
    <div class="card">
      <TabView>
        <TabPanel v-for="category in categories" :header="category.name" :key="category.id">
          <div class="grid">
            <div class="col-12 md:col-6 lg:col-3" v-for="item in filterGoods(category.id)" :key="item.id">
              <div class="surface-card shadow-2 p-3 border-round" @click="selectItem(item)">
                <!-- Card Content -->
                <div class="text-900 font-medium text-xl">{{ item.name }}</div>
                <span class="text-red-500 font-medium">{{ item.price }}元</span>
              </div>
            </div>
          </div>
        </TabPanel>
      </TabView>
    </div>
  </template>
  
  <style scoped>
    /* Your CSS here */
  </style>