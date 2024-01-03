<script setup>
import { ref } from 'vue';
import AASearchMenPiao from '@/views/GymPages/snippits/AASearchMenPiao.vue';
import MenPiao from '@/views/GymPages/snippits/MenPiao.vue';


const dropdownItems = ref([
    { name: 'Option 1', code: 'Option 1' },
    { name: 'Option 2', code: 'Option 2' },
    { name: 'Option 3', code: 'Option 3' }
]);

const dropdownItem = ref(null);
</script>

<template>
    <div class="grid">
        <div class="col-12">
            <cards>
                <div class="formgroup-inline">                
                    <div class="field">
                        <InputText type="text" placeholder="演出名称/演出场次/场馆名/作为区域名" v-tooltip="'Your username'" @click="openNew"/>
                    </div>                    
                        <Button type="button" label="查询"  v-tooltip="'Click to proceed'"   />                   
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
                    <Column field="name" header="演出名称" style="min-width: 200px"></Column>
                    <Column field="country" header="演出场次" style="min-width: 200px">
                   
                    </Column>
                    <Column field="company" header="票档" style="min-width: 200px"></Column>
                    <Column field="status" header="票价" style="min-width: 200px">
                       
                    </Column>
                    <Column field="date" header="作为区域名" style="min-width: 200px"></Column>
                    <Column field="date" header="座位名" style="min-width: 200px"></Column>
              
                </DataTable>
            </div>

        </div>
    
    </div>
</template>
