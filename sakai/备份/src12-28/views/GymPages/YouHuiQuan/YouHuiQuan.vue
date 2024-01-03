<template>
    
    <div class="card">
                <TabView>
                    
                    <TabPanel header="优惠券">

                        <InputText type="text" placeholder="优惠名称" v-tooltip="'Your username'" class="ml-2 mb-2"/>

                        <Button type="button" label="搜索"  v-tooltip="'Click to proceed'" class="p-button-info mb-2 ml-2" />
                        <Button type="button" label="清除"  v-tooltip="'Click to proceed'" class="p-button-danger ml-2 mb-2" />

                        <p class="line-height-3 m-0">
                            <DataTable :value="customer3" class="p-datatable-gridlines">
                            <Column field="优惠名称" header="优惠名称"></Column>
                            <Column field="优惠折扣" header="优惠折扣"></Column>
                            <Column field="优惠金额" header="优惠金额"></Column>
                            <Column field="优惠类型" header="优惠类型"></Column>
                    
                            <Column field="操作" header="操作"></Column>

                </DataTable>
                        </p>
                        </TabPanel>


                    <TabPanel header="优惠券详情">
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
      "优惠名称": "7折扣券",
      "优惠折扣": "70",
      "优惠金额": "0",
      "优惠类型": "优惠折扣",
    },
    {
      "representative.name": "John",
      "优惠名称": "10快去代金券",
      "优惠折扣": "",
      "优惠金额": "10",
      "优惠类型": "优惠金额",
    },
    {
      "representative.name": "John",
      "优惠名称": "6折优惠券",
      "优惠折扣": "60",
      "优惠金额": "0",
      "优惠类型": "优惠折扣",
    },
    {
      "representative.name": "John",
      "优惠名称": "5优惠券",
      "优惠折扣": "50",
      "优惠金额": "0",
      "优惠类型": "优惠折扣",
    },
    {
      "representative.name": "John",
      "优惠名称": "4优惠券",
      "优惠折扣": "40",
      "优惠金额": "0",
      "优惠类型": "优惠折扣",
    },
    {
      "representative.name": "John",
      "优惠名称": "储值1000元",
      "优惠折扣": "",
      "优惠金额": "400",
      "优惠类型": "优惠金额",
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