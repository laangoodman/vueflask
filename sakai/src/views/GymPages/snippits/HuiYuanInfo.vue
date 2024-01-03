<template>




 
    <div class="card">
                <TabView>
                    <TabPanel header="充值记录">
                        <p class="line-height-3 m-0">
                            <DataTable :value="fixedData" class="p-datatable-gridlines">
                            <Column field="充值时间" header="充值时间"></Column>
                            <Column field="充值金额" header="充值金额"></Column>
                            <Column field="赠送金额" header="赠送金额"></Column>
                            <Column field="实际到账" header="实际到账"></Column>
                            <Column field="备注" header="备注"></Column>

                </DataTable>
                        </p>
                        </TabPanel>
                    <TabPanel header="消费记录">
                        <p class="line-height-3 m-0">
                            <DataTable :value="fixedData" class="p-datatable-gridlines">
                            <Column field="单据号" header="单据号"></Column>
                            <Column field="消费类型" header="消费类型"></Column>
                            <Column field="商品明细" header="商品明细"></Column>
                            <Column field="场地名称" header="场地名称"></Column>
                            <Column field="预约时间" header="预约时间"></Column>
                            <Column field="消费金额" header="消费金额"></Column>
                            <Column field="优惠金额" header="优惠金额"></Column>
                            <Column field="实收" header="实收"></Column>
                            <Column field="消费时间" header="消费时间"></Column>
                            </DataTable>                        
                        </p>
                    </TabPanel>
                    <TabPanel header="充次记录">
                        <p class="line-height-3 m-0">
                            <DataTable :value="fixedData" class="p-datatable-gridlines">
                            <Column field="冲次时间" header="冲次时间"></Column>
                            <Column field="计次项目名称" header="计次项目名称"></Column>
                            <Column field="实收" header="实收"></Column>
                            <Column field="冲次次数" header="冲次次数"></Column>
  
                            </DataTable>  
                                                </p>
                    </TabPanel>
                    <TabPanel header="会费记录">
                        <p class="line-height-3 m-0">
                            <DataTable :value="fixedData" class="p-datatable-gridlines">
                            <Column field="缴费时间" header="缴费时间"></Column>
                            <Column field="会员卡类别" header="会员卡类别"></Column>
                            <Column field="会费金额" header="会费金额"></Column>
                            <Column field="会员卡期限" header="会员卡期限"></Column>   
                            <Column field="备注" header="备注"></Column>   

                            </DataTable>
                        
                        </p>
                    </TabPanel>
                    <TabPanel header="剩余项目">
                        <p class="line-height-3 m-0">
                            同上重复劳动，到时候写
                       </p>
                    </TabPanel>
                    <TabPanel header="优惠券">
                        <p class="line-height-3 m-0">
                            同上重复劳动，到时候写
                        </p>
                    </TabPanel>
                    <TabPanel header="换卡记录">
                        <p class="line-height-3 m-0">
                            同上重复劳动，到时候写
                        </p>
                    </TabPanel>
                    <TabPanel header="续费记录">
                        <p class="line-height-3 m-0">
                            同上重复劳动，到时候写
                        </p>
                    </TabPanel>
                    <TabPanel header="积分记录">
                        <p class="line-height-3 m-0">
                            同上重复劳动，到时候写
                        </p>
                    </TabPanel>
                    <TabPanel header="等级记录">
                        <p class="line-height-3 m-0">
                            同上重复劳动，到时候写
                        </p>
                    </TabPanel>
                    <TabPanel header="退款记录">
                        <p class="line-height-3 m-0">
                            同上重复劳动，到时候写
                        </p>
                    </TabPanel>
                </TabView>
            </div>



</template>