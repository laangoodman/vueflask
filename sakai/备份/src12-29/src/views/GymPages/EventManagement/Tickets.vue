
<script setup>
import { ref } from 'vue';

const dropdownValues = ref([
    { name: '足球场', code: 'NY' },
    { name: '羽毛球场', code: 'RM' },
    { name: '网球场', code: 'LDN' },
    { name: '田径场', code: 'IST' },
    { name: '篮球场', code: 'PRS' }
]);

const dropdownValue = ref(null);


</script>

<template>
    
    <div class="card">
               

                <InputText type="text" placeholder="请输入场地名称" v-tooltip="'Your username'" class="mb-2 ml-2"/>

                        <Button type="button" label="查询"  v-tooltip="'Click to proceed'" class="p-button-info ml-2 mb-2" />
                        <Button type="button" label="新增"  v-tooltip="'Click to proceed'" class="p-button-danger ml-2 mb-2" />
                        <Button type="button" label="删除"  v-tooltip="'Click to proceed'" class="p-button-danger ml-2 mb-2" />

                        <p class="line-height-3 m-0">
                            <DataTable :value="customer3" class="p-datatable-gridlines">
                            <Column field="演出名称" header="演出名称"></Column>
                            <Column field="场次名称" header="场次名称"></Column>
                            <Column field="票档" header="票档"></Column>
                            <Column field="票价" header="票价"></Column>

                            <Column field="操作" header="操作"></Column>

                </DataTable>
                        </p>
           
            </div>



</template>

<script>
export default {
data() {
return {
  customer3: [
    {
      "representative.name": "John",
      "上级机构": "邯郸市综合体育馆",
      "区域名称": "羽毛球",
      "体育项目分类": "羽毛球",
      "区域排序": "0",
      "闸机序列号": "",
      "周一至周五": "0,1,2,3,4,5,6,7,21,22,23,24",
      "周六至周日": "0,1,2,3,4,5,6,7,21,22,23,24",
    },
    
    {
      "representative.name": "John",
      "上级机构": "赵王大街健身长廊",
      "区域名称": "足球场",
      "体育项目分类": "足球",
      "区域排序": "0",
      "闸机序列号": "",
      "周一至周五": "0,1,2,3,4,5,6,22,23,24",
      "周六至周日": "0,1,2,3,4,5,6,22,23,24",
    },
    {
      "representative.name": "John",
      "name": "3",
      "country": "培训商品",
      "company": "3",
      "status": ""
    },
    {
      "representative.name": "John",
      "name": "4",
      "country": "服务商品",
      "company": "4",
      "status": ""
    },
    {
      "representative.name": "John",
      "name": "5",
      "country": "私教课程",
      "company": "5",
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