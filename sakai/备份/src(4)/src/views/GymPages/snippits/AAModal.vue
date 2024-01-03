
<script setup>
import Dialog from 'primevue/dialog';
import { ref } from 'vue';

const productDialog = ref(false);

const OpenDialog = () => {
    productDialog.value = true
}

const CloseDialog = () => {
    productDialog.value = false
}

</script>

    <template>
        <Button label="新增" @click="OpenDialog" />
        <Dialog v-model:visible="productDialog" modal header="Header" :style="{ width: '50rem' }" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
    <template #header>
        <div class="inline-flex align-items-center justify-content-center gap-2">    
            <span class="font-bold white-space-nowrap">新增</span>
        </div>
    </template>
    <div class="formgrid grid">
        
        
            <div class="field col">
            <InputText type="text" placeholder="会员卡号" v-tooltip="'Your username'" @click="openNew"/>
            </div>
            <div class="field col">

            <InputText type="text" placeholder="会员姓名" v-tooltip="'Your username'" @click="openNew"/>

            </div>
            <div class="field col">

            <InputText type="text" placeholder="手机号码" v-tooltip="'Your username'" @click="openNew"/>
            </div>
            <div class="field col">

            <InputText type="text" placeholder="身份证号" v-tooltip="'Your username'" @click="openNew"/>

            </div>
            <div class="field col">
            <InputText type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>
            </div>
            <div class="field col">

            <InputText type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>

            </div>
            <div class="field col">

            <InputText type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>
            </div>
            <div class="field col">

            <InputText type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>

            </div>
            <div class="field col">
            <InputText type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>
            </div>
            <div class="field col">

            <InputText type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>

            </div>
            <div class="field col">

            <InputText type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>
            </div>
            <div class="field col">

            <InputText type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>

            </div>
            <div class="field col">
            <InputText type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>
            </div>
            <div class="field col">

            <InputText type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>

            </div>
            <div class="field col">

            <InputText type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>
            </div>
            <div class="field col">

            <InputText type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>

            </div>
   
    </div>

    <template #footer>
        <Button label="Ok" icon="pi pi-check" @click="CloseDialog" autofocus />
    </template>
        </Dialog>
    </template>