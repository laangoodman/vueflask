<script setup>
import { ref } from 'vue';
import axios from 'axios';


const fetchData = async () => {
    try {
        const response = await axios.get('http://121.40.98.93:7002/api/Venue/Date');
        const data = response.data; // 从响应中获取数据

//data.a 
//data.b后面再写
        console.log(data);
        console.log('66');
    } catch (error) {
        console.error('快速核销获取数据出错:', error);
    }
};
fetchData(); // 调用 fetchData 来获取数据

</script>

<template>
    <div class="grid">
        <div class="col-12">
            <cards>
                <div class="formgroup-inline">                
                    <div class="field">
                        <InputText type="text" placeholder="" v-tooltip="'Your username'" @click="openNew"/>
                    </div>                    
                        <Button type="button" label="核销"  v-tooltip="'Click to proceed'" />                   
                    <div class="ml-2">
                        <BBModal/>   
                    </div>
                </div>
            </cards> 
        </div>
        <div class="col-12 ">
            <div class="card">
                <DataTable :value="customer3" rowGroupMode="subheader" groupRowsBy="representative.name" sortMode="single" sortField="representative.name" :sortOrder="1" scrollable scrollHeight="400px" class="p-datatable-gridlines">
                    <Column field="representative.name" header="Representative"></Column>
                    <Column field="标号" header="#"></Column>
                    <Column field="name" header="订单号" style="min-width: 150px"></Column>
                    <Column field="country" header="会员卡号" style="min-width: 150px"></Column>
                    <Column field="company" header="会员名称" style="min-width: 150px"></Column>
                    <Column field="status" header="核销时间" style="min-width: 150px"></Column>
                    <Column field="date" header="预约时间" style="min-width: 200px"></Column>
                    <Column field="date" header="区域" style="min-width: 150px"></Column>
                    <Column field="date" header="场地" style="min-width: 150px"></Column>
                    <Column field="date" header="备注" style="min-width: 200px"></Column>              
                </DataTable>
            </div>
        </div> 
    </div>
</template>
