<template>
    
    <div class="card">
               
                    
                  
                    <div>
                        <InputText type="text" placeholder="演出名称" v-tooltip="'Your username'" class="ml-2 mb-2"/>


                        <Button type="button" label="新增"  v-tooltip="'Click to proceed'" class="p-button-info mb-2 ml-2" />
                        <Button type="button" label="清除"  v-tooltip="'Click to proceed'" class="p-button-danger ml-2 mb-2" />
                    </div>


                        <p class="line-height-3 m-0">
                            <DataTable :value="customer3" class="p-datatable-gridlines">
                            <Column field="演出名称" header="演出名称"></Column>
                            <Column field="场次名称" header="场次名称"></Column>
                            <Column field="可买多张" header="可买多张"></Column>
                            <Column field="开始日期" header="开始日期"></Column>
                            <Column field="结束日期" header="结束日期"></Column>
 
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