<template>
    
    <div class="card">
        <InputText type="text" placeholder="商品编号/商品名称" v-tooltip="'Your username'" class="ml-2 mb-2"/>

        <Button type="button" label="查询"  v-tooltip="'Click to proceed'" class="p-button-info ml-2 mb-2" />

        <DataTable :value="customer3" class="p-datatable-gridlines">
                            <Column field="商品编号" header="商品编号"></Column>
                            <Column field="商品名称" header="商品名称"></Column>
                            <Column field="库存总数" header="库存总数"></Column>
                            <Column field="总金额" header="总金额"></Column>
                            <Column field="零售价格" header="零售价格"></Column>
                            <Column field="商品规格" header="商品规格"></Column>
                            <Column field="商品单位" header="商品单位"></Column>
                            <Column field="注册门店" header="注册门店"></Column>
                            <Column field="操作" header="操作"></Column>             

                </DataTable>
           
            </div>



</template>

<script>
export default {
data() {
return {
  customer3: [
    {
      "representative.name": "John",
      "设备名称": "",
      "设备类型": "人脸识别",
      "设备状态": "正常",

    }

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