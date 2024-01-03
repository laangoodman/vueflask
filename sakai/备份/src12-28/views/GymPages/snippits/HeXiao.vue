

<template>

    <div class="col-12">
                <div class="card">
                    <DataTable rowGroupMode="subheader" groupRowsBy="representative.name" sortMode="single" sortField="representative.name" :sortOrder="1" scrollable scrollHeight="400px">

                    <!-- <DataTable :value="" rowGroupMode="subheader" groupRowsBy="representative.name" sortMode="single" sortField="representative.name" :sortOrder="1" scrollable scrollHeight="400px"> -->
                        <Column field="representative.name" header="Representative"></Column>
                        <Column field="name" header="#" style="min-width: 50px"></Column>
                        <Column field="country" header="订单号" style="min-width: 150px">
                       
                        </Column>
                        <Column field="company" header="会员卡号" style="min-width: 150px"></Column>
                        <Column field="status" header="会员名称" style="min-width: 150px">
                           
                        </Column>
                        <Column field="date" header="核销时间" style="min-width: 150px"></Column>
                        <Column field="date" header="预约时间" style="min-width: 150px"></Column>
                        <Column field="date" header="区域" style="min-width: 80px"></Column>
                        <Column field="date" header="场地" style="min-width: 80px"></Column>
                        <Column field="date" header="备注" style="min-width: 200px"></Column>

                    </DataTable>
                </div>
            </div>
    
    
    
    </template>