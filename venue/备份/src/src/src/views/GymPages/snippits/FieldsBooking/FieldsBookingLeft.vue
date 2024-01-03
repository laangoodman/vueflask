
<script setup>
import BBModal from '@/views/GymPages/snippits/BBModal.vue';
import { store } from '@/views/GymPages/snippits/FieldsBooking/FieldsBooking.js'; // Adjust the path as needed
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
         <div v-if="store.newButtonVisible">
            <div>
                <div class="ml-5">
            Area: {{ store.cc }}
                </div>
                <div class="col-6">
                    <div class="card">
                        <div class="grid">
                        <!-- Left column for 预约 and 价格 -->
                            <div class="col-6">
                                <div class="field">预约</div>
                                <div class="field">价格: {{ store.aa }} * {{ store.bb }}</div>
                            </div>
                        <!-- Right column for 小时 -->
                            <div class="col-6">
                                <div class="field right ml-4"> {{ store.bb }}小时</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </template>

        <style lang="scss" scoped></style>
