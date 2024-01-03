<script setup>
import { ref } from 'vue';


const dropdownItems = ref([
    { name: 'Option 1', code: 'Option 1' },
    { name: 'Option 2', code: 'Option 2' },
    { name: 'Option 3', code: 'Option 3' }
]);

const CreateColumn = 0

const statuses = ref([
    { label: '男', value: 'male' },
    { label: '女', value: 'female' }

]);

const dropdownItem = ref(null);
</script>

<template>
  

<div class="col-12">
        
  <DataTable :value="customer3" rowGroupMode="subheader"   sortField="representative.name"  class="p-datatable-gridlines">
    <Column field="representative.name" header="场地" style="min-width: 100px"></Column>
    <Column field="name" header="0:00" style="min-width: 10px"></Column>
    <Column field="name" header="1:00" style="min-width: 10px"></Column>
    <Column field="country" header="2:00" style="min-width: 10px"></Column>
    <Column field="company" header="3:00" style="min-width: 10px"></Column>
    <Column field="status" header="4:00" style="min-width: 10px"></Column>
    <Column field="status" header="5:00" style="min-width: 10px"></Column>
    <Column field="field6" header="6:00" style="min-width: 10px"></Column>
    <Column field="field7" header="7:00" style="min-width: 10px"></Column>
    <Column field="field8" header="8:00" style="min-width: 10px"></Column>
    <Column field="field9" header="9:00" style="min-width: 10px"></Column>
    <Column field="field10" header="10:00" style="min-width: 10px"></Column>
    <Column field="field11" header="11:00" style="min-width: 10px"></Column>
    <Column field="field12" header="12:00" style="min-width: 10px"></Column>
    <Column field="field13" header="13:00" style="min-width: 10px"></Column>
    <Column field="field14" header="14:00" style="min-width: 10px"></Column>
    <Column field="field15" header="15:00" style="min-width: 10px"></Column>
    <Column field="field16" header="16:00" style="min-width: 10px"></Column>
    <Column field="field17" header="17:00" style="min-width: 10px"></Column>
    <Column field="field18" header="18:00" style="min-width: 10px"></Column>
    <Column field="field19" header="19:00" style="min-width: 10px"></Column>
    <Column field="field20" header="20:00" style="min-width: 10px"></Column>
    <Column field="field21" header="21:00" style="min-width: 10px"></Column>
    <Column field="field22" header="22:00" style="min-width: 10px"></Column>
    <Column field="field23" header="23:00" style="min-width: 10px"></Column>
</DataTable>
        
    </div>







</template>




<script>
export default {
  data() {
    return {
      customer3: [
        {
          "representative.name": "羽毛球",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },
        {
          "representative.name": "羽毛球",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },
        {
          "representative.name": "羽毛球",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },
        {
          "representative.name": "羽毛球",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },
        {
          "representative.name": "羽毛球",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },
        {
          "representative.name": "足球场",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },
        {
          "representative.name": "足球场",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },
        {
          "representative.name": "网球场",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },
        {
          "representative.name": "网球场",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },
        {
        "representative.name": "田径场",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },
        {
        "representative.name": "田径场",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },
        {
        "representative.name": "篮球场",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },
        {
        "representative.name": "篮球场",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },
        {
        "representative.name": "篮球场",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },
        {
        "representative.name": "篮球场",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },
        {
        "representative.name": "篮球场",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },
        {
        "representative.name": "南广场",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },  
        {
        "representative.name": "综合篮球场",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },              
        {
        "representative.name": "游泳场",
          "name": "",
          "country": "",
          "company": "",
          "status": ""
        },
      ],
    };
  },
};
</script>

<style>
.p-datatable-gridlines td {
  vertical-align: middle;
  text-align: center;

}
</style>