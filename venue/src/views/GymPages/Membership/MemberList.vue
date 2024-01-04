<script setup>
  import HuiYuanLieBiaoTop from '@/views/GymPages/snippits/HuiYuanLieBiaoTop.vue';
  import AASearchMember from '@/views/GymPages/snippits/AASearchMember.vue';
  import HuiYuanList from '@/views/GymPages/snippits/HuiYuanList.vue';
  const API = process.env.API_URL;

</script>


<template>
  <div class="grid ml-2 mt-1">
    


    <div class="col-3  p-0 lg:pr-5 lg:pb-5 mt-4 lg:mt-0 ">
        <div
            style="height: 160px; padding: 2px; border-radius: 10px; background: linear-gradient(90deg, rgba(253, 228, 165, 0.2), rgba(187, 199, 205, 0.2)), linear-gradient(180deg, rgba(253, 228, 165, 0.2), rgba(187, 199, 205, 0.2))">
            <div class="p-3 surface-card h-full bg-yellow-200" style="border-radius: 8px">
                <h5 class="mt-2 text-900">今日新增</h5>
                <h5 class="mb-2 text-900">0</h5>
                <h5 class="mb-2 text-900">0</h5>
                <span class="text-600">近7天</span>                                            
            </div>
        </div>
    </div>
    <div class="col-3  p-0 lg:pr-5 lg:pb-5 mt-4 lg:mt-0 ">
        <div
            style="height: 160px; padding: 2px; border-radius: 10px; background: linear-gradient(90deg, rgba(253, 228, 165, 0.2), rgba(187, 199, 205, 0.2)), linear-gradient(180deg, rgba(253, 228, 165, 0.2), rgba(187, 199, 205, 0.2))">
            <div class="p-3 surface-card h-full bg-yellow-200" style="border-radius: 8px">
                <h5 class="mt-2 text-900">今日生日</h5>
                <h5 class="mb-2 text-900">0</h5>
                <h5 class="mb-2 text-900">0</h5>
                <span class="text-600">近7天</span>                                            
            </div>
        </div>
    </div>
    <div class="col-3  p-0 lg:pr-5 lg:pb-5 mt-4 lg:mt-0 ">
        <div
            style="height: 160px; padding: 2px; border-radius: 10px; background: linear-gradient(90deg, rgba(253, 228, 165, 0.2), rgba(187, 199, 205, 0.2)), linear-gradient(180deg, rgba(253, 228, 165, 0.2), rgba(187, 199, 205, 0.2))">
            <div class="p-3 surface-card h-full bg-yellow-200" style="border-radius: 8px">
                <h5 class="mt-2 text-900">今日未消费</h5>
                <h5 class="mb-2 text-900">0</h5>
                <h5 class="mb-2 text-900">0</h5>
                <span class="text-600">近7天</span>                                            
            </div>
        </div>
    </div>
    <div class="col-3  p-0 lg:pr-5 lg:pb-5 mt-4 lg:mt-0 ">
        <div
            style="height: 160px; padding: 2px; border-radius: 10px; background: linear-gradient(90deg, rgba(253, 228, 165, 0.2), rgba(187, 199, 205, 0.2)), linear-gradient(180deg, rgba(253, 228, 165, 0.2), rgba(187, 199, 205, 0.2))">
            <div class="p-3 surface-card h-full bg-yellow-200" style="border-radius: 8px">
                <h5 class="mt-2 text-900">今日到期</h5>
                <h5 class="mb-2 text-900">0</h5>
                <h5 class="mb-2 text-900">0</h5>
                <span class="text-600">近7天</span>                                            
            </div>
        </div>
    </div>

    <div class="formgroup-inline">                
                    <div class="field">
                        <InputText type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>
                    </div>                    
                        <Button class="ml-2" type="button" label="查询"  v-tooltip="'Click to proceed'"   />                   
                        <Button class="ml-2" type="button" label="新增"  v-tooltip="'Click to proceed'"   />                   
                        <Button class="ml-2" type="button" label="删除"  v-tooltip="'Click to proceed'"   />                   
                        <Button class="ml-2" type="button" label="导入"  v-tooltip="'Click to proceed'"   />                   
                        <Button class="ml-2" type="button" label="导出"  v-tooltip="'Click to proceed'"   />                   

                </div>

                <DataTable :value="customer3" rowGroupMode="subheader" groupRowsBy="representative.name" sortMode="single" sortField="representative.name" :sortOrder="1" scrollable scrollHeight="400px" class="p-datatable-gridlines">
                    <Column field="representative.name" header="Representative"></Column>
                    <Column field="name" header="会员卡号" style="min-width: 100px"></Column>
                    <Column field="country" header="卡面号码" style="min-width: 100px">
                   
                    </Column>
                    <Column field="company" header="会员姓名" style="min-width: 100px"></Column>
                    <Column field="status" header="会员性别" style="min-width: 100px">
                       
                    </Column>
                    <Column field="date" header="手机号码" style="min-width: 100px"></Column>
                    <Column field="date" header="身份证号" style="min-width: 100px"></Column>
                    <Column field="date" header="会员生日" style="min-width: 100px"></Column>
                    <Column field="date" header="会员等级" style="min-width: 100px"></Column>
                    <Column field="date" header="售卡工本费" style="min-width: 100px"></Column>
                    <Column field="date" header="账户余额" style="min-width: 100px"></Column>
                    <Column field="date" header="账户积分" style="min-width: 100px"></Column>
                    <Column field="date" header="累计消费" style="min-width: 100px"></Column>
                    <Column field="date" header="累计充值" style="min-width: 100px"></Column>
                    <Column field="date" header="操作" style="min-width: 180px"></Column>
              
                </DataTable>
  
  </div>
</template>

<style scoped>
.p-datatable-gridlines {
  font-size: 12px; /* Adjust the size as needed */
}
</style>