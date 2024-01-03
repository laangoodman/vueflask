
<template>

    <div class="card">
        <div class="formgroup-inline">
            <div class="field">
                <InputText type="text" placeholder="会员卡号/手机号码/会员姓名" v-tooltip="'Your username'" />
    
                <Button type="button" label="查询"  v-tooltip="'Click to proceed'"  />
    
            </div>
    
            <Button type="button" label="新增" icon="pi pi-plus" v-tooltip="'Click to proceed'" class="p-button-success mr-2" />

            <Button type="button" label="删除" icon="pi pi-plus" v-tooltip="'Click to proceed'" class="p-button-secondary mr-2" />

            <Button type="button" label="导入" icon="pi pi-plus" v-tooltip="'Click to proceed'" class="p-button-warning mr-2" />

            <Button type="button" label="导出" icon="pi pi-plus" v-tooltip="'Click to proceed'" class="p-button-danger mr-2" />

        </div>
    </div>
    
    </template>