<template>
    
        <div class="card">
                    <TabView>
                        
                        <TabPanel header="区域管理">
                            <Button type="button" label="新增"  v-tooltip="'Click to proceed'" class="p-button-info mb-2" />
                            <Button type="button" label="批量删除"  v-tooltip="'Click to proceed'" class="p-button-danger ml-2 mb-2" />

                            <p class="line-height-3 m-0">
                                <DataTable :value="customer3" class="p-datatable-gridlines">
                                <Column field="上级机构" header="上级机构"></Column>
                                <Column field="区域名称" header="区域名称"></Column>
                                <Column field="体育项目分类" header="体育项目分类"></Column>
                                <Column field="区域排序" header="区域排序"></Column>
                                <Column field="闸机序列号" header="闸机序列号"></Column>
                                <Column field="周一至周五" header="周一至周五"></Column>
                                <Column field="周六至周日" header="周六至周日"></Column>
                                <Column field="操作" header="操作"></Column>
    
                    </DataTable>
                            </p>
                            </TabPanel>

   
                        <TabPanel header="场地管理">
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