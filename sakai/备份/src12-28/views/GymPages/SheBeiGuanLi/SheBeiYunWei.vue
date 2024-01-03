<template>
    
    <div class="card">

        <Button type="button" label="新增"  v-tooltip="'Click to proceed'" class="p-button-info ml-2 mb-2" />

        <DataTable :value="customer3" class="p-datatable-gridlines">
                            <Column field="设备名称" header="设备名称"></Column>
                            <Column field="设备类型" header="设备类型"></Column>
                            <Column field="设备状态" header="设备状态"></Column>
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
      "设备名称": "测试设备",
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