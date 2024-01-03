
<script setup>
import BBModal from '@/views/GymPages/snippits/BBModal.vue';
import { store } from '@/views/GymPages/snippits/FieldsBooking/FieldsBooking.js'; // Adjust the path as needed
import axios from 'axios';
const openNew = () => {
    product.value = {};
    submitted.value = false;
    productDialog.value = true;
};


const submitData = async () => {
      try {
        const response = await axios.post('http://121.40.98.93:7002/api/Venue/Insert_Booking', {
          bookingInfo: {
            BillNumber: '1234567890',
            MemberID: '1001',
            MemberName: '王小明',
            CardNumber: 'A12345',
            PhoneNumber: '13812345678',
            VenueName: '羽毛球1',
            AreaName: '篮球场',
            ReservationDate: '2024-01-10',
            ReservationTime: '1,3,4',
            OrderStatusCode: 1,
            OrderStatusDescription: '待核销',
            TotalAmount: 100.00,
            DiscountAmount: 10.00,
            AmountPaid: 90.00,
            PaymentMethodCode: 1,
            PaymentMethodDescription: '现金',
            OrderTime: '2024-01-05 12:00:00',
            Store: '深圳分店',
            Notes: '备注信息'
          }
        });

        // 处理后端响应
        console.log('发送成功',response.bookingInfo);
      } catch (error) {
        // 处理错误
        console.error('发送请求时出错:', error);
      }
    };


</script>
    <template>
        <div class="card">
            <div class="formgroup-inline">
                <div class="grid">
                    <InputText class="col-6" type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>
                    <Button class="ml-2" type="button" label="查询"  v-tooltip="'Click to proceed'"   />       
                    <div class="ml-2">
                        <BBModal/>
                    </div>
                </div>      
            </div>
        </div>
         <div v-if="store.newButtonVisible">
            <div>
                <div class="ml-5">
            Area: {{ store.cc }}
                </div>
                <div class="col-6">
                    <div class="card">
                        <div class="grid">
                        <!-- Left column for 预约 and 价格 -->
                            <div class="col-6">
                                <div class="field">预约</div>
                                <div class="field">价格: {{ store.aa }} * {{ store.bb }}</div>
                            </div>
                        <!-- Right column for 小时 -->
                            <div class="col-6">
                                <div class="field right ml-4"> {{ store.bb }}小时</div>
                            </div>
                            
                        </div>
                        
                    </div>
                </div>
            </div>
        </div>
        <Button @click="submitData">提交</Button>
        </template>

        <style lang="scss" scoped></style>
