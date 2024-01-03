
<script setup>

import BBModal from '@/views/GymPages/snippits/BBModal.vue';


const openNew = () => {
    product.value = {};
    submitted.value = false;
    productDialog.value = true;
};

</script>

<template>
<div class="card">
    <div class="formgroup-inline">
        <div class="field">
            <InputText type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>

            <Button type="button" label="查询"  v-tooltip="'Click to proceed'" class="ml-2"  />

        </div>

        <BBModal/>
        <!-- <Button type="button" label="新增" icon="pi pi-plus" v-tooltip="'Click to proceed'" class="p-button-success" /> -->

    </div>
</div>

</template>

<style lang="scss" scoped></style>
