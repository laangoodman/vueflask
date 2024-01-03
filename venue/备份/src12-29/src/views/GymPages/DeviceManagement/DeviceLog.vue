<template>
    
    <div class="card">
        <InputText type="text" placeholder="请输入虚拟设备ID" v-tooltip="'Your username'" class="ml-2 mb-2"/>

        <Button type="button" label="查询"  v-tooltip="'Click to proceed'" class="p-button-info ml-2 mb-2" />

        <DataTable :value="customer3" class="p-datatable-gridlines">
                            <Column field="设备厂商" header="设备厂商"></Column>
                            <Column field="设备名称" header="设备名称"></Column>
                            <Column field="操作时间" header="操作时间"></Column>
                            <Column field="操作人名称" header="操作人名称"></Column>
                            <Column field="身份证号" header="身份证号"></Column>
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