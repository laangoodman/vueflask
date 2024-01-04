<script setup>

import { ref } from 'vue';
import axios from 'axios';
const API = process.env.API_URL;

</script>


<template>
  <div class="grid ml-2 mt-1">
    <div class="formgroup-inline">                
        <div class="field">
            <InputText type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>
        </div>                    
            <Button class="ml-2" type="button" label="查询"  v-tooltip="'Click to proceed'"   />                   
                 
    </div>



    <div class="card col-12">
        <div>
          <Button label="会员续费" class="p-button-outlined p-button-secondary mr-4 mb-2" />
          <Button label="会员锁定" class="p-button-outlined p-button-secondary mr-4 mb-2" />
          <Button label="积分调整" class="p-button-outlined p-button-secondary mr-4 mb-2" />
          <Button label="等级调整" class="p-button-outlined p-button-secondary mr-4 mb-2" />
          <Button label="修改资料" class="p-button-outlined p-button-secondary mr-4 mb-2" />
          <Button label="重置密码" class="p-button-outlined p-button-secondary mr-4 mb-2" />
        </div>
        <div class="grid mt-4 ">
          
            <div class="col-12 md:col-3">
                <div class="grid">
                    <div class="col-4">                        
                        <Avatar class="ml-4" :image="'demo/images/avatar/amyelsner.png'" size="large" shape="circle"></Avatar>
                    </div>
                    <div class="col-8">
                        <div>会员卡号:</div> 
                        <div>卡面号码:</div>
                    </div>
                </div>
            </div>

            <div class="col-12 md:col-3">
                <div>身份证号:</div> 
                <div>会员生日:</div>
                <div>会员等级:</div> 
                <div>售卡工本费:</div>
                <div>有效期限:</div> 
                <div>会员卡状态:</div>
            </div>
            <div class="col-12 md:col-3">
                <div>账户余额:</div> 
                <div>账户积分:</div>
                <div>累计消费:</div> 
                <div>累计充值:</div>
                <div>累计充次:</div> 
                <div>累计会费:</div>
                <div>微信绑定:</div> 
                <div>联系地址:</div>
            </div>
            <div class="col-12 md:col-3">
            
                <div>车牌号码:</div> 
                <div>提成员工:</div>
                <div>推荐人:</div> 
                <div>开卡时间:</div>
                <div>注册门店:</div> 
                <div>操作员:</div>

            </div>
        </div>
</div>



<div class="card col-12">
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
  
  </div>
</template>
