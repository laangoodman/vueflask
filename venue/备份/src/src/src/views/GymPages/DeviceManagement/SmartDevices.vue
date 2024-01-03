<template>
    
    <div class="card">
                <TabView>
                    
                    <TabPanel header="人脸识别">
                        <Dropdown v-model="dropdownValue" :options="dropdownValues" optionLabel="name" placeholder="请选择" class="p-button-danger  ml-2 mb-2"/>
                        <Dropdown v-model="dropdownValue" :options="dropdownValues" optionLabel="name" placeholder="请选择 所属区域" class="p-button-danger  ml-2 mb-2"/>

                        <InputText type="text" placeholder="请输入场地名称" v-tooltip="'Your username'" class="ml-2"/>
                        <InputText type="text" placeholder="请输入虚拟设备ID" v-tooltip="'Your username'" class="ml-2"/>

                        <Button type="button" label="查询"  v-tooltip="'Click to proceed'" class="p-button-info ml-2 mb-2" />
                        <Button type="button" label="新增"  v-tooltip="'Click to proceed'" class="p-button-info ml-2 mb-2" />
                        <Button type="button" label="查看清理设备数据"  v-tooltip="'Click to proceed'" class="p-button-info ml-2 mb-2" />
                        <Button type="button" label="导入数据"  v-tooltip="'Click to proceed'" class="p-button-info ml-2 mb-2" />
                        <Button type="button" label="设置认证上报"  v-tooltip="'Click to proceed'" class="p-button-info ml-2 mb-2" />

                        <p class="line-height-3 m-0">
                            <DataTable :value="customer3" class="p-datatable-gridlines">
                            <Column field="公司名称" header="公司名称"></Column>
                            <Column field="设备类别" header="设备类别"></Column>
                            <Column field="所属区域" header="所属区域"></Column>
                            <Column field="适用场地" header="适用场地"></Column>
                            <Column field="虚拟ID" header="虚拟ID"></Column>
                            <Column field="IP地址" header="IP地址"></Column>
                            <Column field="端口号" header="端口号"></Column>
                            <Column field="操作" header="操作"></Column>

                </DataTable>
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