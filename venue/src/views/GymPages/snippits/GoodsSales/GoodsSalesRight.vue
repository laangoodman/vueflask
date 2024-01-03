
<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { watch } from 'vue';
import { store } from '@/views/GymPages/snippits/GoodsSales/GoodsSales.js'; // Adjust the path as needed

// import { store } from '@/views/GymPages/Gymjs/store2.js'; // store1是场地租用store2商品销售



const categories = ref([
  { id: 1, name: '全部' },
  { id: 2, name: '普通商品' },
  // { id: 3, name: '服务商品' },
  // Add more categories as needed
]);

const goods = ref([
    { id: 1, name: '纸巾', price:2},
    { id: 2, name: '矿泉水',price:3},
    { id: 3, name: '纸巾',price:4},

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


const onTabChange = () => {
  store.selectedItem = null;
};

</script>

<template>
    <div class="card">
      <TabView @tab-change="onTabChange">
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