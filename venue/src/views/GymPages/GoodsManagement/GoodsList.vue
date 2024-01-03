<template>
 <div class="card">
    <div class="surface-ground px-4 py-5 md:px-6 lg:px-8">
        <div class="grid">

            
            <div class="col-12 md:col-6 lg:col-6" >
                <div class="surface-card shadow-2 p-3 border-round" style="height: 200px;">
                    
                    <div class="flex justify-content-between mb-3">
                        <div>
                            <span class="block text-500 font-medium mb-3"></span>
                            <div class="text-900 font-medium text-sm">商品总量</div>
                        </div>
                      
                    </div>
                    <span class="text-red-500 font-medium"> </span>
                    
                        <div>                    
                            <span class="block text-500 font-medium mb-8"></span>
                            <div class="text-900 font-medium text-sm"></div>
                        </div>

                </div>
                
            </div>
    
            <div class="col-12 md:col-6 lg:col-6" >
                <div class="surface-card shadow-2 p-3 border-round" style="height: 200px;">
                    
                    <div class="flex justify-content-between mb-3">
                        <div>
                            <span class="block text-500 font-medium mb-3"></span>
                            <div class="text-900 font-medium text-sm">库存预警</div>
                        </div>
                      
                    </div>
                    <span class="text-red-500 font-medium"> </span>
                    
                        <div>                    
                            <span class="block text-500 font-medium mb-8"></span>
                            <div class="text-900 font-medium text-sm"></div>
                        </div>

                </div>
                
            </div>
            
        </div>
    </div>


        <div class="card">
        <div class="formgroup-inline">
            <div class="field">
                <InputText type="text" placeholder="商品编号/商品编码/商品名称/货号" v-tooltip="'Your username'" />
    
                <Button type="button" label="查询"  v-tooltip="'Click to proceed'"  />
    
            </div>
    
            <Button type="button" label="新增" icon="pi pi-plus" v-tooltip="'Click to proceed'" class="p-button-success mr-2" />


            <Button type="button" label="导入" icon="pi pi-plus" v-tooltip="'Click to proceed'" class="p-button-warning mr-2" />

            <Button type="button" label="导出" icon="pi pi-plus" v-tooltip="'Click to proceed'" class="p-button-danger mr-2" />

        </div>
    </div>
    
    <div class="card">

    <div class="grid">


<div class="col-12 ">
    <div class="card">
   
        <p></p>
        <DataTable :value="fixedData" class="p-datatable-gridlines">
            <Column field="商品编号" header="商品编号"></Column>
            <Column field="货号" header="货号"></Column>
            <Column field="商品名称" header="商品名称"></Column>
            <Column field="商品简码" header="商品简码"></Column>
            <Column field="商品类型" header="商品类型"></Column>
            <Column field="计次商品类型" header="计次商品类型"></Column>
            <Column field="适用机构" header="适用机构"></Column>
            <Column field="适用区域" header="适用区域"></Column>
            <Column field="计次次数" header="计次次数"></Column>
            <Column field="操作" header="操作"></Column>
        </DataTable>
    </div>
</div>

</div>
    </div>
</div>

    </template>