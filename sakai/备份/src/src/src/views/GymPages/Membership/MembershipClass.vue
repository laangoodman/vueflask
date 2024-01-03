<script setup>
import { ref } from 'vue';

const dropdownItems = ref([
    { name: 'Option 1', code: 'Option 1' },
    { name: 'Option 2', code: 'Option 2' },
    { name: 'Option 3', code: 'Option 3' }
]);

const dropdownItem = ref(null);



const fixedData = [
  { 类别名称: '终身卡', 会费金额: 3000 ,使用期限:'永久',起算日期:'购买当日'},
  { 类别名称: '季卡', 会费金额: 300 ,使用期限:'90',起算日期:'激活当日'},
  { 类别名称: '超级会员卡', 会费金额: 300 ,使用期限:'7',起算日期:'购买当日'},
  { 类别名称: 'k', 会费金额: 200 ,使用期限:'7',起算日期:'激活当日'},
  { 类别名称: '游泳季卡', 会费金额: 1000 ,使用期限:'90',起算日期:'购买当日'},
  { 类别名称: '游泳周卡', 会费金额: 10 ,使用期限:'7',起算日期:'购买当日'},
  { 类别名称: '游泳月卡', 会费金额: 500 ,使用期限:'30',起算日期:'购买当日'},

];


</script>





<template>
    <div class="grid">


        <div class="col-12 ">
            <div class="card">
                <div>
                    <Button type="button" label="新增"  v-tooltip="'Click to proceed'"  />
                </div>
                <p></p>
                <DataTable :value="fixedData" class="p-datatable-gridlines">
                    <Column field="类别名称" header="类别名称"></Column>
                    <Column field="会费金额" header="会费金额"></Column>
                    <Column field="使用期限" header="使用期限"></Column>
                    <Column field="起算日期" header="起算日期"></Column>
                    <Column field="操作" header="操作"></Column>
                </DataTable>
            </div>
        </div>
    
    </div>
</template>
