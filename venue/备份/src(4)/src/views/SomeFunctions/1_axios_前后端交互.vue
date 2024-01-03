<template>
    <div>
      <h1>Vue 3 和 Flask 交互</h1>
      <button @click="fetchData">从 Flask 获取数据</button>
      <button @click="sendData">发送数据到 Flask</button>
      <p>从 Flask 接收的消息: {{ message }}</p>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import axios from 'axios';
  
  export default {
    setup() {
      const message = ref('');
  
      const fetchData = async () => {
        try {
          const response = await axios.get('http://localhost:5000/api/data');
          //const response = await axios.get('api/data');
          message.value = response.data.message;
        } catch (error) {
          console.error('获取数据出错:', error);
        }
      };
  
      const sendData = async () => {
        try {
          const response = await axios.post('http://localhost:5000/api/data', { data: '这是来自 Vue 3 的数据' });
          //const response = await axios.post('api/data', { data: '这是来自 Vue 3 的数据' });
          message.value = response.data.message;
        } catch (error) {
          console.error('发送数据出错:', error);
        }
      };
  
      return { message, fetchData, sendData };
    }
  };
  </script>