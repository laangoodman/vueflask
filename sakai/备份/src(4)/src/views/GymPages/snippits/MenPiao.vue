

<template>

<div class="col-12">
            <div class="card">
                <DataTable :value="customer3" rowGroupMode="subheader" groupRowsBy="representative.name" sortMode="single" sortField="representative.name" :sortOrder="1" scrollable scrollHeight="400px" class="p-datatable-gridlines">
                    <Column field="representative.name" header="Representative"></Column>
                    <Column field="name" header="演出名称" style="min-width: 200px"></Column>
                    <Column field="country" header="演出场次" style="min-width: 200px">
                   
                    </Column>
                    <Column field="company" header="票档" style="min-width: 200px"></Column>
                    <Column field="status" header="票价" style="min-width: 200px">
                       
                    </Column>
                    <Column field="date" header="作为区域名" style="min-width: 200px"></Column>
                    <Column field="date" header="座位名" style="min-width: 200px"></Column>
              
                </DataTable>
            </div>
        </div>



</template>