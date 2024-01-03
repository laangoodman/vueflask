

<template>

    <div class="col-12">
                <div class="card">
                    <DataTable :value="customer3" rowGroupMode="subheader" groupRowsBy="representative.name" sortMode="single" sortField="representative.name" :sortOrder="1" scrollable scrollHeight="400px" class="p-datatable-gridlines">
                        <Column field="representative.name" header="Representative"></Column>
                        <Column field="name" header="会员卡号" style="min-width: 200px"></Column>
                        <Column field="country" header="卡面号码" style="min-width: 100px"></Column>
                        <Column field="company" header="会员姓名" style="min-width: 100px"></Column>
                        <Column field="status" header="会员性别" style="min-width: 100px"></Column>
                        <Column field="date" header="手机号码" style="min-width: 100px"></Column>
                        <Column field="date" header="身份证号" style="min-width: 100px"></Column>
                        <Column field="company" header="会员生日" style="min-width: 100px"></Column>
                        <Column field="status" header="会员卡类别" style="min-width: 100px"></Column>
                        <Column field="date" header="会员等级" style="min-width: 100px"></Column>
                        <Column field="date" header="售卡工本费" style="min-width: 50px"></Column>
                        <Column field="status" header="账户余额" style="min-width: 100px"></Column>
                        <Column field="date" header="账户积分" style="min-width: 100px"></Column>
                        <Column field="date" header="操作" style="min-width: 100px"></Column>
                  
                    </DataTable>
                </div>
            </div>
    
    
    
    </template>