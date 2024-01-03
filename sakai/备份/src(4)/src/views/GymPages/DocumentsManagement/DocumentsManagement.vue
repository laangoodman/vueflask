
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
                <TabView>
                    
                    <TabPanel header="统计报表">

                <InputText type="text" placeholder="刷卡或输入卡号/手机号/姓名" v-tooltip="'Your username'" class="ml-2"/>
                <Dropdown v-model="dropdownValue" :options="dropdownValues" optionLabel="name" placeholder="请选择 会员等级" class="p-button-danger  ml-2 mb-2"/>
                <Dropdown v-model="dropdownValue" :options="dropdownValues" optionLabel="name" placeholder="请选择 操作员" class="p-button-danger  ml-2 mb-2"/>
                <Dropdown v-model="dropdownValue" :options="dropdownValues" optionLabel="name" placeholder="请选择 支付方式" class="p-button-danger  ml-2 mb-2"/>
                <InputText type="text" placeholder="请输入 充次卡号" v-tooltip="'Your username'" class="ml-2"/>
                <Button type="button" label="重置"  v-tooltip="'Click to proceed'" class="p-button-info ml-2 mb-2" />
                <Button type="button" label="查询"  v-tooltip="'Click to proceed'" class="p-button-info ml-2 mb-2" />


                        <div>
                        <Button type="button" label="导出"  v-tooltip="'Click to proceed'" class="p-button-info ml-2 mb-2" />
                    </div>


                        <p class="line-height-3 m-0">
                            <DataTable :value="customer3" class="p-datatable-gridlines">
                            <Column field="消费类型" header="消费类型"></Column>
                            <Column field="总金额" header="总金额"></Column>
                            <Column field="优惠金额" header="优惠金额"></Column>
                            <Column field="实收金额" header="实收金额"></Column>
                            <Column field="实收金额详情" header="实收金额详情"></Column>
                            <Column field="退款总金额详情" header="退款总金额详情"></Column>
                            <Column field="实际收入" header="实际收入"></Column>


                </DataTable>
                        </p>
                        </TabPanel>


                    <TabPanel header="场地预约订单">
                        <p class="line-height-3 m-0">
                            同上重复劳动，到时候写
                       </p>
                    </TabPanel>

                    <TabPanel header="场地消费单据">
                        <p class="line-height-3 m-0">
                            同上重复劳动，到时候写
                       </p>
                    </TabPanel>

                    <TabPanel header="演出售票订单">
                        <p class="line-height-3 m-0">
                            同上重复劳动，到时候写
                       </p>
                    </TabPanel>

                    <TabPanel header="消费单据">
                        <p class="line-height-3 m-0">
                            同上重复劳动，到时候写
                       </p>
                    </TabPanel>

                    <TabPanel header="充值单据">
                        <p class="line-height-3 m-0">
                            同上重复劳动，到时候写
                       </p>
                    </TabPanel>

                    <TabPanel header="充次单据">
                        <p class="line-height-3 m-0">
                            同上重复劳动，到时候写
                       </p>
                    </TabPanel>

                    <TabPanel header="挂单列表">
                        <p class="line-height-3 m-0">
                            同上重复劳动，到时候写
                       </p>
                    </TabPanel>

                    <TabPanel header="退款单据">
                        <p class="line-height-3 m-0">
                            同上重复劳动，到时候写
                       </p>
                    </TabPanel>

                </TabView>
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