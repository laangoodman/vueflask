<template>
    
    <div class="card">
               
                    
                  
                    <div>
                        <InputText type="text" placeholder="演出名称" v-tooltip="'Your username'" class="ml-2 mb-2"/>
                        <InputText type="text" placeholder="所属单位" v-tooltip="'Your username'" class="ml-2 mb-2"/>
                        <InputText type="text" placeholder="场馆区域" v-tooltip="'Your username'" class="ml-2 mb-2"/>

                        <Button type="button" label="搜索"  v-tooltip="'Click to proceed'" class="p-button-info mb-2 ml-2" />
                        <Button type="button" label="清除"  v-tooltip="'Click to proceed'" class="p-button-danger ml-2 mb-2" />
                    </div>

                    <div class="my-4">
                        <Button type="button" label="新增"  v-tooltip="'Click to proceed'" class="p-button-info mb-2 ml-2" />
                        <Button type="button" label="删除"  v-tooltip="'Click to proceed'" class="p-button-danger ml-2 mb-2" />
                    </div>
                        <p class="line-height-3 m-0">
                            <DataTable :value="customer3" class="p-datatable-gridlines">
                            <Column field="演出名称" header="演出名称"></Column>
                            <Column field="演出类型" header="演出类型"></Column>
                            <Column field="开始日期" header="开始日期"></Column>
                            <Column field="结束日期" header="结束日期"></Column>
                            <Column field="最低价格" header="最低价格"></Column>
                            <Column field="最高价格" header="最高价格"></Column>
                            <Column field="是否选座" header="是否选座"></Column>
                            <Column field="所属部门" header="所属部门"></Column>  
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