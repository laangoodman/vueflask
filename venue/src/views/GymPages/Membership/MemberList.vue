<script setup>


import { ref } from 'vue';
import axios from 'axios';
import { useToast } from 'primevue/usetoast';
const API = process.env.API_URL
const toast = useToast();

const MemberPassword = ref('6666');
const ConfirmPassword = ref('6666');

const selectedCity1 = ref({})

const openNew = () => {

};


const fixedData = ref([
    // { huiyuan: 'ddd', kahao: 100 },
    // { huiyuan: 'eee', kahao: 101 },
    // { huiyuan: 'fff', kahao: 102 },
]);

// data = {
//     "MemberAvatar": b'\x00\x01\x02\x03',  # 二进制头像数据
//     "MemberID": "M12345", 会员卡号
//     "CardFaceNumber": "CF123", 卡面卡号
//     "Name": "张三", 会员姓名
//     "Gender": "男", 会员性别
//     "PhoneNumber": "1234567890", 手机号码
//     "IDNumber": "123456789012345", 身份证号
//     "Birthday": "1990-01-15", 会员生日
//     "PlateNumber": "C78901",  车牌号
//     "Password": "my_password",密码
//     "CardIssuanceFee": 50.00, 售卡工本费
//     "Address": "北京市朝阳区", 联系地址
//     "CurrentBalance": 1000.00, 账户余额
//     "Operator": "Admin"
// }


//response: 不管是POST还是GET，最后都会有一个response值， 例如我想Post以后马上从后端get一个值，instead of 再写一个get，可以在后端定义这个response值，达到和写一个GET同样的效果
const fetchData = async () => {

    try {
        const response = await axios.post(`${API}/api/Membership/Get_members`, {
            search_query: "", // 通过search_query字段传递查询参数
        });
        //
        // Handling server response
        console.log('Server Response:', response.data);
        // Updating timeSlots based on the server response
        fixedData.value = response.data.value
        console.log("@@@@", fixedData.value)
    } catch (error) {
        // Handling errors
        console.error('Error:', error);
    }

    // try {

    //     // const response = await axios.get('http://:5000/api/Membership/Get_membership_categories');
    //     const response = await axios.get(`${API}/api/Membership/Get_members`);
    //     const data = response.data; // 从响应中获取数据

    //     fixedData.value = data;
    //     console.log(fixedData);
    //     console.log('成功拿到fixedData' + fixedData);


    // } catch (error) {
    //     console.error('出错:', error);
    // }
};
fetchData();


const CommissionMember = ref([
    { name: 'New York', code: 'NY' },
    { name: 'Rome', code: 'RM' },
    { name: 'London', code: 'LDN' },
    { name: 'Istanbul', code: 'IST' },
    { name: 'Paris', code: 'PRS' }
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

        <div class="formgroup-inline my-4">
            <div class="field">
                <InputText type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew" />
            </div>
            <Button class="ml-2 p-button-secondary" type="button" label="查询" v-tooltip="'Click to proceed'" />
            <Button class="ml-2 p-button-primary" type="button" label="新增" v-tooltip="'Click to proceed'" @click="open" />

            <Button class="ml-2 p-button-danger" type="button" label="删除" v-tooltip="'Click to proceed'" />
            <Button class="ml-2 p-button-success" type="button" label="导入" v-tooltip="'Click to proceed'" />
            <Button class="ml-2 p-button-warning" type="button" label="导出" v-tooltip="'Click to proceed'" />

        </div>

    </div>

    <!-- 如果要让responsivelayourscroll work 不能把datatable放在最上面的div里面，会改变里面css -->
    <DataTable :value="fixedData" rowGroupMode="subheader" groupRowsBy="representative.name" sortMode="single"
        sortField="representative.name" :sortOrder="1" scrollable scrollHeight="400px" class="p-datatable-gridlines"
        responsiveLayout="scroll">


        <Column selectionMode="multiple" :styles="{ 'min-width': '3rem' }"></Column>

        <Column field="representative.name" header="Representative"></Column>
        <Column field="MemberAvatar" header="会员头像" style="min-width: 13rem"></Column>
        <Column field="MemberID" header="会员卡号" style="min-width: 13rem"></Column>
        <Column field="CardFaceNumber" header="卡面号码" style="min-width: 13rem"></Column>
        <Column field="Name" header="会员姓名" style="min-width: 13rem"></Column>
        <Column field="Gender" header="会员性别" style="min-width: 13rem"></Column>
        <Column field="PhoneNumber" header="手机号码" style="min-width: 13rem"></Column>
        <Column field="IDNumber" header="身份证号" style="min-width: 13rem"></Column>
        <Column field="Birthday" header="会员生日" style="min-width: 13rem"></Column>
        <Column field="PlateNumber" header="车牌号" style="min-width: 13rem"></Column>
        <Column field="CardIssuanceFee" header="售卡工本费" style="min-width: 13rem"></Column>
        <Column field="Address" header="联系地址" style="min-width: 13rem"></Column>
        <Column field="CurrentBalance" header="账户余额" style="min-width: 13rem"></Column>
        <!-- <Column field="date" header="累计消费" style="min-width: 13rem"></Column> -->
        <!-- <Column field="date" header="累计充值" style="min-width: 13rem"></Column> -->
        <!-- <Column field="date" header="累计充次" style="min-width: 13rem"></Column> -->
        <!-- <Column field="date" header="累计会费" style="min-width: 13rem"></Column> -->
        <!-- <Column field="date" header="提成员工" style="min-width: 13rem"></Column> -->
        <!-- <Column field="date" header="车辆号码" style="min-width: 13rem"></Column>
                    <Column field="date" header="联系地址" style="min-width: 13rem"></Column>
                    <Column field="date" header="会员状态" style="min-width: 13rem"></Column> -->
        <!-- <Column field="date" header="微信" style="min-width: 13rem"></Column> -->
        <!-- <Column field="date" header="开卡时间" style="min-width: 13rem"></Column>
                    <Column field="date" header="注册门店" style="min-width: 13rem"></Column>
                    <Column field="date" header="到期时间" style="min-width: 13rem"></Column>
                    <Column field="date" header="操作" style="min-width: 13rem"></Column>  -->

    </DataTable>

    <Dialog header="新增" v-model:visible="display" :breakpoints="{ '960px': '75vw' }" :style="{ width: '50vw' }"
        :modal="true">

        <div class=" p-fluid grid formgrid">
            <div class="field col-12 md:col-6 mt-4">
                <label for="username">上传头像</label>
            </div>
            <div class="field col-12 md:col-6 mt-4">

                <FileUpload name="demo[]" @uploader="onUpload" :multiple="true" accept="image/*" :maxFileSize="1000000"
                    customUpload />

            </div>

            <div class="field col-12 md:col-6 mt-4">
                <span class="p-float-label">
                    <InputText id="inputtext" type="text" v-model="value1" />
                    <label for="inputtext">会员卡号</label>
                </span>
            </div>
            <div class="field col-12 md:col-6 mt-4">
                <span class="p-float-label">
                    <InputText id="inputtext" type="text" v-model="value1" />
                    <label for="inputtext">会员姓名</label>
                </span>
            </div>
            <div class="field col-12 md:col-6 mt-4">
                <span class="p-float-label">
                    <InputText id="inputtext" type="text" v-model="value1" />
                    <label for="inputtext">手机号码</label>
                </span>
            </div>
            <div class="field col-12 md:col-6 mt-4">
                <span class="p-float-label">
                    <InputText id="inputtext" type="text" v-model="value1" />
                    <label for="inputtext">身份证号</label>
                </span>
            </div>
            <div class="field col-12 md:col-6 mt-4">
                <div class=" p-fluid grid formgrid">
                    <div class="mb-0 col-12 md:col-6">
                        <label for="disableddays">会员性别:</label>
                    </div>
                    <!-- <div class="field col-12 md:col-6"> -->
                    <div class="field-radiobutton mb-0 col-12 md:col-3">
                        <RadioButton id="city1" name="city" value="Chicago" v-model="city" />
                        <label class="ml-4 mt-2" for="city1">男</label>
                    </div>
                    <!-- <div class="field col-12 md:col-6"> -->
                    <div class="field-radiobutton mb-0 col-12 md:col-3">
                        <RadioButton id="city1" name="city" value="Chicago" v-model="city" />
                        <label class="ml-4 mt-2" for="city1">女</label>
                    </div>
                </div>
            </div>


            <!-- <div class="field-radiobutton mb-0">
                                                <RadioButton id="option1" name="TheDayPurChased" value="购买当日"
                                                    v-model="StartDate" />
                                                <label for="option1">购买当日</label>
                                            </div> -->

            <div class="field col-12 md:col-6 mt-4">
                <span class="p-float-label">
                    <InputText id="inputtext" type="text" v-model="value1" />
                    <label for="inputtext">卡面号码</label>
                </span>
            </div>
            <div class="field col-12 md:col-6 mt-4">
                <span class="p-float-label">
                    <InputText id="inputtext" type="text" v-model="value1" />
                    <label for="inputtext">会员生日</label>
                </span>
            </div>
            <div class="field col-12 md:col-6 mt-4">
                <span class="p-float-label">
                    <Password v-model="MemberPassword" toggleMask></Password>
                    <label for="MemberPassword">会员密码</label>
                </span>
            </div>
            <div class="field col-12 md:col-6 mt-4">
                <span class="p-float-label">
                    <Password v-model="ConfirmPassword" toggleMask></Password>
                    <label for="ConfirmPassword">确认密码</label>
                </span>
            </div>
            <div class="field col-12 md:col-6 mt-4">
                <span class="p-float-label">
                    <InputText id="inputtext" type="text" v-model="value1" />
                    <label for="inputtext">会员等级</label>
                </span>
            </div>
            <div class="field col-12 md:col-6 mt-4">
                <span class="p-float-label">
                    <InputText id="inputtext" type="text" v-model="value1" />
                    <label for="inputtext">售卡工本费</label>
                </span>
            </div>
            <div class="field col-12 md:col-6 mt-4">
                <span class="p-float-label">
                    <InputText id="inputtext" type="text" v-model="value1" />
                    <label for="inputtext">注册充值</label>
                </span>
            </div>
            <!-- <div class="field col-12 md:col-6 mt-4">
                                <span class="p-float-label">
                                    <InputText id="inputtext" type="text" v-model="value1" />
                                    <label for="inputtext">提成员工</label>
                                </span>
                            </div> -->
            <!-- <div class="field col-12 md:col-6 mt-4">
                                    <Dropdown v-model="selectedCity1" :options="CommissionMember" optionLabel="name" placeholder="选择提成员工" />

                            </div> -->


            <div class="field col-12 md:col-6 mt-4">
                <span class="p-float-label">
                    <InputText id="inputtext" type="text" v-model="value1" />
                    <label for="inputtext">车牌号码</label>
                </span>
            </div>
            <div class="field col-12 md:col-6 mt-4">
                <span class="p-float-label">
                    <InputText id="inputtext" type="text" v-model="value1" />
                    <label for="inputtext">联系地址</label>
                </span>
            </div>
            <!-- <div class="field col-12 md:col-6 mt-4">
                                <span class="p-float-label">
                                    <InputText id="inputtext" type="text" v-model="value1" />
                                    <label for="inputtext">推荐人</label>
                                </span>
                            </div> -->
        </div>






        <template #footer>
            <Button label="保存" @click="submitData" icon="pi pi-check" class="p-button-outlined" />
            <Button label="关闭" @click="close" class="p-button-outlined" />
        </template>
    </Dialog>
</template>

<style scoped>
.p-datatable-gridlines {
    font-size: 12px;
    /* Adjust the size as needed */
}
</style>