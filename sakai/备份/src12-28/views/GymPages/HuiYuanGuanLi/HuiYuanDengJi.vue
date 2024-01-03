<script setup>
import { ref } from 'vue';

const dropdownItems = ref([
    { name: 'Option 1', code: 'Option 1' },
    { name: 'Option 2', code: 'Option 2' },
    { name: 'Option 3', code: 'Option 3' }
]);

const dropdownItem = ref(null);



const fixedData = [
    { 等级名称: '一级', 积分比例: 0 ,商品折扣:10,
    场地折扣: 4, 累计充值: 3000 ,品类折扣:'无',
    线下启用:0, 线上启用: 0 },
    { 等级名称: '钻石', 积分比例: 0 ,商品折扣:10,
    场地折扣: 4, 累计充值: 10000 ,品类折扣:'无',
    线下启用:0, 线上启用: 0 },  
    { 等级名称: '默认等级', 积分比例: 1 ,商品折扣:10,
    场地折扣: 4, 累计充值: 0 ,品类折扣:'无',
    线下启用:0, 线上启用: 0 },  


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
                    <Column field="等级名称" header="等级名称"></Column>
                    <Column field="积分比例" header="积分比例"></Column>
                    <Column field="商品折扣" header="商品折扣"></Column>
                    <Column field="场地折扣" header="场地折扣"></Column>
                    <Column field="累计充值" header="累计充值"></Column>
                    <Column field="品类折扣" header="品类折扣"></Column>
                    <Column field="线下启用" header="线下启用"></Column>
                    <Column field="线上启用" header="线上启用"></Column>
                    <Column field="操作" header="操作"></Column>
                </DataTable>
            </div>
        </div>
    
    </div>
</template>
