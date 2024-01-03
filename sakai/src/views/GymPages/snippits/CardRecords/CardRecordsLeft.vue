
<script setup>
import BBModal from '@/views/GymPages/snippits/BBModal.vue';
import { store } from '@/views/GymPages/snippits/CardsSales/CardsSales.js'; // Adjust the path as needed
import { onBeforeUnmount } from 'vue';

const openNew = () => {
    product.value = {};
    submitted.value = false;
    productDialog.value = true;
};


</script>
    <template>
    <div class="card" style="display: flex; flex-direction: column; justify-content: flex-start; height: 82vh;">
                <div class="formgroup-inline">                
                    <div class="field">
                        <InputText type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>
                    </div>                    
                        <Button type="button" label="查询"  v-tooltip="'Click to proceed'"   />                   
                       
                </div>

        <div class="col-12" v-if="store.selectedItem" style="margin-top: 10px;">
            <div style="height: 160px; padding: 2px; border-radius: 10px; background: linear-gradient(90deg, rgba(253, 228, 165, 0.2), rgba(187, 199, 205, 0.2)), linear-gradient(180deg, rgba(253, 228, 165, 0.2), rgba(187, 199, 205, 0.2))">
                <div class="p-3 surface-card h-full" style="border-radius: 8px">
                    <div class="flex align-items-center justify-content-center bg-yellow-200 mb-3" style="width: 3.5rem; height: 3.5rem; border-radius: 10px">
                        <i class="pi pi-fw pi-users text-2xl text-yellow-700"></i>
                    </div>
                    <h5 class="mb-2 text-900">Name: {{ store.selectedItem.name }}</h5>
                    <span class="text-600">Price: {{ store.selectedItem.price }}</span>
                </div>
            </div>
        </div>

        <div style="margin-top: auto;">
            <Button :label="'应付' + store.selectedItem.price + '元'" class="p-button-rounded border-none font-light line-height-2 bg-blue-500 text-white" v-if="store.selectedItem" style="width: 100%;"></Button>
        </div>
    </div>
</template>

        <style lang="scss" scoped></style>
