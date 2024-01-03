<script setup>
//123
import { ref } from 'vue';
import axios from 'axios';

const showModal = ref(false);

import { useToast } from 'primevue/usetoast';


const toast = useToast();




const fixedData = ref([
    //   { 类别名称: '终身卡', 会费金额: 3000 ,使用期限:'永久',起算日期:'购买当日'},
    //   { 类别名称: '季卡', 会费金额: 300 ,使用期限:'90',起算日期:'激活当日'},
    //   { 类别名称: '超级会员卡', 会费金额: 300 ,使用期限:'7',起算日期:'购买当日'},
    //   { 类别名称: 'k', 会费金额: 200 ,使用期限:'7',起算日期:'激活当日'},
    //   { 类别名称: '游泳季卡', 会费金额: 1000 ,使用期限:'90',起算日期:'购买当日'},
    //   { 类别名称: '游泳周卡', 会费金额: 10 ,使用期限:'7',起算日期:'购买当日'},
    //   { 类别名称: '游泳月卡', 会费金额: 5020 ,使用期限:'30',起算日期:'购买当日'},
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

const WhatAreTheChoices = ref([{ name: '周卡' },
{ name: '月卡' },
{ name: '季卡' },
{ name: '年卡' },
{ name: '终身卡' },
{ name: '其他' },
]);


//初始化起算日期
const StartDate = ref('');
const CategoryName = ref('');
const MembershipFee = ref('');
const MembershipDuration = ref('');

const selectedMembership = ref(null);
const updateMembershipDuration = () => {
    switch (selectedMembership.value?.name) {
        case '周卡':
            MembershipDuration.value = '7';
            break;
        case '月卡':
            MembershipDuration.value = '30';
            break;
        case '季卡':
            MembershipDuration.value = '90';
            break;
        case '年卡':
            MembershipDuration.value = '365';
            break;
        case '终身卡':
            MembershipDuration.value = '99999';
            break;
    }
};


//获取数据
const fetchData = async () => {
    try {

        // const response = await axios.get('http://127.0.0.1:5000/api/Membership/Get_membership_categories');
        const response = await axios.get(`${API}/api/Membership/Get_membership_categories`);
        const data = response.data; // 从响应中获取数据

        fixedData.value = data;
        console.log(fixedData+'666');

    } catch (error) {
        console.error('获取会员等级数据出错:', error);
    }
};
fetchData(); // 调用 fetchData 来获取数据    


const submitData = async () => {
    try {

        const requestData = {
            CategoryName: CategoryName.value,
            MembershipDuration: MembershipDuration.value,
            MembershipFee: MembershipFee.value,
            StartDate: StartDate.value
        };
        const response = await axios.post('http://121.40.98.93:7002/api/Membership/Insert_membership_categories', requestData);
        // const response = await axios.post('http://127.0.0.1:5000/api/Membership/Insert_membership_categories', requestData);

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
                                <div class="card p-fluid">
                                    <div class="formgrid grid">
                                        <div class="field col">
                                            <label for="name2">类别名称</label>
                                            <InputText v-model="CategoryName" id="CategoryName" type="text" />
                                        </div>
                                        <div class="field col">
                                            <label for="email2">会费金额</label>
                                            <InputText v-model="MembershipFee" id="MembershipFee" type="text" />
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="card p-fluid">
                                    <!-- <div class="formgrid grid">
                                        <label for="name2" class="mr-4">使用期限(天)</label>                               
                                        <SelectButton v-model="MembershipDuration" :options="WhatAreTheChoices" optionLabel="name" />
                                    </div> -->
                                    <div class="grid">
                                        <div class="field col-2">
                                            <label for="name2" class="mr-4">使用期限(天)</label>
                                        </div>
                                        <div class="field col-10">
                                            <SelectButton v-model="selectedMembership" :options="WhatAreTheChoices"
                                                optionLabel="name" @change="updateMembershipDuration" />
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="card p-fluid">
                                    <div class="grid">
                                        <div class="col-12 md:col-4">
                                            <div class="field-radiobutton mb-0">
                                                <label for="name2" class="mr-4">起算日期</label>
                                            </div>
                                        </div>
                                        <div class="col-12 md:col-4">
                                            <div class="field-radiobutton mb-0">
                                                <RadioButton id="option1" name="TheDayPurChased" value="购买当日"
                                                    v-model="StartDate" />
                                                <label for="option1">购买当日</label>
                                            </div>
                                        </div>
                                        <div class="col-12 md:col-4">
                                            <div class="field-radiobutton mb-0">
                                                <RadioButton id="option2" name="TheDayActivated" value="激活当日"
                                                    v-model="StartDate" />
                                                <label for="option2">激活当日</label>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                        </div>
                        <template #footer>
                            <Button label="保存" @click="submitData" icon="pi pi-check" class="p-button-outlined" />
                            <Button label="关闭" @click="close" class="p-button-outlined" />
                        </template>
                    </Dialog>
                    <Button type="button" label="新增" v-tooltip="'Click to proceed'" @click="open" />
                </div>
                <p></p>

                <DataTable :value="fixedData" class="p-datatable-gridlines">
                    <Column field="CategoryName" header="类别名称"></Column>
                    <Column field="MembershipFee" header="会费金额"></Column>
                    <Column field="MembershipDuration" header="使用期限"></Column>
                    <Column field="StartDate" header="起算日期"></Column>
                    <!-- <Column field="操作" header="操作"></Column> -->
                </DataTable>



            </div>
        </div>
    </div>
</template>

<style scoped></style>