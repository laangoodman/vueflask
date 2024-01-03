
<template>

    <div class="card">
        <div class="formgroup-inline">
            <div class="field">
                <InputText type="text" placeholder="演出名称/演出场次/场馆名/作为区域名" v-tooltip="'Your username'" />
    
                <Button type="button" label="查询"  v-tooltip="'Click to proceed'"  />
    
            </div>
    
            <Button type="button" label="购票" icon="pi pi-plus" v-tooltip="'Click to proceed'" class="p-button-success" />
    
        </div>
    </div>
    
    </template>