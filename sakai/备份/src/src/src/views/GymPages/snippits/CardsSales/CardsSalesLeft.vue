
<script setup>
import BBModal from '@/views/GymPages/snippits/BBModal.vue';
import { store } from '@/views/GymPages/snippits/CardsSales/CardsSales.js'; // Adjust the path as needed
const openNew = () => {
    product.value = {};
    submitted.value = false;
    productDialog.value = true;
};
</script>
    <template>
        <div class="card">
            <div class="formgroup-inline">
                <div class="grid">
                    <InputText type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>
                    <Button type="button" label="查询"  v-tooltip="'Click to proceed'" class="ml-2"  />       
                    <div class="ml-2">
                        <BBModal/>
                    </div>
                </div>      
            </div>
        </div>

        <div v-if="store.selectedItem">
            
               <div class="col-12 surface-card shadow-2 p-3 border-round yahei-font">
                <div>Name: {{ store.selectedItem.name }}</div>
                <div>Price: {{ store.selectedItem.price }}</div> 
                </div>
            
        </div>



    





        </template>

        <style lang="scss" scoped></style>
