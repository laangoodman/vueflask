<template>
        <div class="card">
        <div class="formgroup-inline">


            
            <div class="field">

           
          
                <InputText type="text" placeholder="类别名称" v-tooltip="'Your username'" />

                类别键值:
                <InputText type="text" placeholder="类别键值" v-tooltip="'Your username'" />
    
                <Button type="button" label="查询"  v-tooltip="'Click to proceed'" class="p-button-info ml-4" />
    

            </div>


            <Button type="button" label="清空"  v-tooltip="'Click to proceed'" class="p-button-danger mr-2" />

        </div>
    </div>




    <div class="card">

        <div class="col-12">
                <div class="card">
                    <DataTable :value="customer3" rowGroupMode="subheader" groupRowsBy="representative.name" sortMode="single" sortField="representative.name" :sortOrder="1" scrollable scrollHeight="400px" class="p-datatable-gridlines">
                        <Column field="representative.name" header="Representative"></Column>
                        <Column field="name" header="序号" style="min-width: 20px"></Column>
                        <Column field="country" header="类别名称" style="min-width: 300px"></Column>
                        <Column field="company" header="类别键值" style="min-width: 300px"></Column>
                        <Column field="status" header="操作" style="min-width: 100px"></Column>

                    </DataTable>
                </div>
            </div>


    </div>


</template>

<script>
export default {
  data() {
    return {
      customer3: [
        {
          "representative.name": "John",
          "name": "1",
          "country": "普通商品",
          "company": "1",
          "status": ""
        },
        {
          "representative.name": "John",
          "name": "2",
          "country": "计件商品",
          "company": "2",
          "status": ""
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