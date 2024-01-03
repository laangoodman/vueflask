<script setup>
//123
import { ref, computed, watch } from 'vue';
import axios from 'axios';

import { useToast } from 'primevue/usetoast';
const toast = useToast();
const fixedData = ref([
]);


//控制dialog是否显示，初始false，点新增变true弹出，dialog内点关闭变false关闭
const display = ref(false);
//绑在新增上，点击后value变true
const open = () => {
    display.value = true;
};
//绑在dialog内关闭按钮上，点击后value变false
const close = () => {
    display.value = false;
};

//初始化起算日期
const LevelName = ref('');
const PointsRatio = ref('');
const ProductDiscount = ref(10);
const VenueDiscount = ref(10);
const AccumulatedRecharge = ref('');
const OnlineActivation = ref('');
const OfflineActivation = ref('');
const PurchaseAmount = ref('');
const Points = ref('');
const PointsRequiredForUpgrade = ref('')

const computedPointsRatio = computed(() => {
    if (PurchaseAmount.value > 0) {
        // Calculate the ratio and limit it to two decimal places
        return (Points.value / PurchaseAmount.value).toFixed(2);
    }
    return 0;
});

// Watch for changes in Points and PurchaseAmount
watch([Points, PurchaseAmount], ([newPoints, newPurchaseAmount]) => {
    // Update computedPointsRatio when either Points or PurchaseAmount changes
    computedPointsRatio.value = (newPoints / newPurchaseAmount).toFixed(2);
});


//获取数据
const fetchData = async () => {
    try {

        // const response = await axios.get('http://172.16.16.128:5000/api/Membership/Get_membership_categories');
        const response = await axios.get(`${API}/api/Membership/Get_member_levels`);
        const data = response.data; // 从响应中获取数据

        fixedData.value = data;
        console.log(fixedData);

    } catch (error) {
        console.error('获取会员等级数据出错:', error);
    }
};
fetchData(); // 调用 fetchData 来获取数据    


const submitData = async () => {
    try {
        OnlineActivation.value = 0;
        OfflineActivation.value = 0;
        const requestData = {
            LevelName: String(LevelName.value),
            ProductDiscount: String(ProductDiscount.value),
            VenueDiscount: String(VenueDiscount.value),
            AccumulatedRecharge: String(AccumulatedRecharge.value),
            PointsRatio: String(computedPointsRatio.value),
            OnlineActivation: String(OnlineActivation.value),
            OfflineActivation: String(OfflineActivation.value),
            Points: String(Points.value),
            PurchaseAmount: String(PurchaseAmount.value),
            PointsRequiredForUpgrade: String(PointsRequiredForUpgrade.value)
        };
        console.log('发送成功', requestData);

        const response = await axios.post(`${API}/api/Membership/Insert_member_levels`, requestData);

        // 处理后端响应
        console.log('发送成功', requestData);

        //发送成功以后保存
        display.value = false;
        toast.add({ severity: 'success', summary: '保存成功', detail: CategoryName.value, life: 5000 });

        //刷新数据
        fetchData();
    } catch (error) {
        // 处理错误
        console.error('发送请求时出错:', error);
        toast.add({ severity: 'error', summary: '保存失败', detail: '', life: 5000 });
    }
};

</script>

<template>
    <Toast />
    <div class="grid">
        <div class="col-12 ">
            <div class="card">
                <div>
                    <Dialog header="新增" v-model:visible="display" :breakpoints="{ '960px': '75vw' }"
                        :style="{ width: '50vw' }" :modal="true">
                        <div class="grid">
                            <div class="col-12">
                                <div class="p-fluid">
                                    <div class="formgrid grid">
                                        <div class="field col">
                                            <label for="name2">等级名称</label>
                                            <InputText v-model="LevelName" id="CategoryName" type="text" />
                                        </div>
                                        <div class="field col">
                                            <label for="email2">累计充值</label>
                                            <InputText v-model="AccumulatedRecharge" id="MembershipFee" type="text" />
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="p-fluid">
                                    <div class="formgrid grid">
                                        <div class="field col">
                                            <label for="name2">商品折扣</label>
                                            <InputNumber v-model="ProductDiscount" showButtons mode="decimal" :max="10"></InputNumber>
                                        </div>
                                        <div class="field col">
                                            <div class="col-12">
                                                <label for="name2">''</label>
                                            </div>
                                            <div>
                                                <label for="email2">注:默认10为没有折扣，8表示为8折</label>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="p-fluid">
                                    <div class="formgrid grid">
                                        <div class="field col">
                                            <label for="name2">场地折扣</label>
                                            <InputNumber v-model="VenueDiscount" showButtons mode="decimal" :max="10"></InputNumber>
                                        </div>
                                        <div class="field col">
                                            <div class="col-12">
                                                <label for="name2">''</label>
                                            </div>
                                            <div>
                                                <label for="email2">注:默认10为没有折扣，8表示为8折</label>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="col-12">
                                <div class="p-fluid">
                                    <div class="formgrid grid">
                                        <div class="field col">
                                            <label for="name2">积分比例</label>
                                            <InputText type="text" :value="computedPointsRatio" :placeholder=PointsRatio
                                                :disabled="true"></InputText>
                                        </div>
                                        <div class="field col">
                                            <label for="name2">消费金额</label>
                                            <InputNumber v-model="PurchaseAmount" showButtons mode="decimal"></InputNumber>
                                        </div>
                                        <div class="field col">
                                            <label for="name2">获得积分</label>
                                            <InputNumber v-model="Points" showButtons mode="decimal"></InputNumber>
                                        </div>
                                    </div>
                                </div>
                            </div>

                        </div>
                        <template #footer>
                            <Button label="提交" @click="submitData" icon="pi pi-check" class="p-button-outlined" />
                            <Button label="关闭" @click="close" class="p-button-outlined" />
                        </template>
                    </Dialog>
                    <Button type="button" label="新增" v-tooltip="'Click to proceed'" @click="open" />
                </div>
                <p></p>

                <DataTable :value="fixedData" class="p-datatable-gridlines">
                    <Column field="LevelName" header="等级名称"></Column>
                    <Column field="PointsRatio" header="积分比例"></Column>
                    <Column field="ProductDiscount" header="商品折扣"></Column>
                    <Column field="VenueDiscount" header="场地折扣"></Column>
                    <Column field="AccumulatedRecharge" header="累计充值"></Column>
                    <Column field="" header="品类折扣"></Column>
                    <Column field="OnlineActivation" header="线下启用"></Column>
                    <Column field="OfflineActivation" header="线上启用"></Column>
                    <Column field="" header="操作">
                    <template #body="slotProps">
                        <!-- Edit Button -->
                        <Button icon="pi pi-pencil" class="p-button-rounded p-button-success" @click="editItem(slotProps.data)"></Button>
                        <!-- Actions Button -->
                        <Button icon="pi pi-cog" class="p-button-rounded p-button-secondary" @click="performActions(slotProps.data)"></Button>
                    </template>
                    </Column>
                </DataTable>



            </div>
        </div>
    </div>

    <!-- 等级名称
积分比例
商品折扣
场地折扣
累计充值
品类折扣
线下启用
线上启用
操作 -->
</template>

<style scoped></style>