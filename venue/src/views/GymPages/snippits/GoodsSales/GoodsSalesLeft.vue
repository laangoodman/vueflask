
<script setup>
import { ref } from 'vue';
import BBModal from '@/views/GymPages/snippits/BBModal.vue';
import { store } from '@/views/GymPages/snippits/GoodsSales/GoodsSales.js'; // Adjust the path as needed
import { onBeforeUnmount } from 'vue';

const API = process.env.API_URL;

const currentPaymentMethod = ref('微信');


const appendedNumbers = ref('0.00');
const appendNumber = (number) => {
    if (appendedNumbers.value === '0.00') {
        appendedNumbers.value = number;
    } else {
        appendedNumbers.value += number;
    }
};
const removeLastDigit = () => {
    if (appendedNumbers.value.length > 1) {
        appendedNumbers.value = appendedNumbers.value.slice(0, -1);
    } else {
        appendedNumbers.value = '0.00';
    }
};

const clearNumber = () => {
    appendedNumbers.value = '0.00';
};

const modalVisible = ref(false);

const submitModal = () => {
    modalVisible.value = true;
};

onBeforeUnmount(() => {
  store.selectedItem = null;
});
</script>
    <template>
    <div class="card" style="display: flex; flex-direction: column; justify-content: flex-start; height: 82vh;">

        
            <div class="formgroup-inline">                
                <div class="grid">
                    <InputText class="col-6" type="text" placeholder="请刷卡/输入卡号/手机号" v-tooltip="'Your username'" @click="openNew"/>
                    <Button class="ml-2" type="button" label="查询"  v-tooltip="'Click to proceed'"   />       
                    <div class="ml-2">
                        <BBModal/>
                    </div>
                </div>  
            </div>
        
       


        <div class="col-12" v-if="store.selectedItem" style="margin-top: 10px;">
                        <div
                            style="height: 160px; padding: 2px; border-radius: 10px; background: linear-gradient(90deg, rgba(253, 228, 165, 0.2), rgba(187, 199, 205, 0.2)), linear-gradient(180deg, rgba(253, 228, 165, 0.2), rgba(187, 199, 205, 0.2))"
                        >
                            <div class="p-3 surface-card h-full" style="border-radius: 8px">
                                <div class="flex align-items-center justify-content-center bg-yellow-200 mb-3" style="width: 3.5rem; height: 3.5rem; border-radius: 10px">
                                    <i class="pi pi-fw pi-users text-2xl text-yellow-700"></i>
                                </div>
                                <h5 class="mb-2 text-900">Name: {{ store.selectedItem.name }}</h5>
                                <span class="text-600">Price: {{ store.selectedItem.price }}</span>
                            </div>
                        </div>
                    </div>


            <div style="margin-top: auto;">
                <Button :label="'应付' + store.selectedItem.price + '元'" class="p-button-rounded border-none font-light line-height-2 bg-blue-500 text-white" 
                        v-if="store.selectedItem" style="width: 100%;"
                        @click="submitModal">
                </Button>

            </div>
        </div>

                        <Dialog v-model:visible="modalVisible" :style="{ width: '1350px', height: '800px'}" header="收银付款" :modal="true">
                            <div class="grid">
                                <div class="col-5">
                                    <div class="card">
                                        <h2>散客</h2>
                                        <div class="grid">
                                            <div class="card col-4">
                                                <button class="col-12" @click="currentPaymentMethod = '微信'">
                                                   
                                                    <span class="center">微信</span>
                                               
                                                </button>
                                            </div>
                                            <div class="card col-4">
                                                <button class="col-12" @click="currentPaymentMethod = '现金'">
                                                    <span class="center">现金</span>
                                                </button>                 
                                            </div>
                                            <div class="card col-4">
                                                <button class="col-12" @click="currentPaymentMethod = 'Pos机'">
                                                    <span class="center">Pos机</span>
                                                </button>
                                            </div>
                                            <div class="card col-4">
                                                <button class="col-12">
                                                    <span class="center">整单优惠</span>
                                                </button>
                                            </div>
                                            <div class="card col-4">
                                                <button class="col-12">
                                                    <span class="center">整单提成</span>
                                                </button>
                                            </div>
                                            <div class="card col-4">
                                                <button class="col-12">
                                                    <span class="center">备注</span>
                                                </button>
                                            </div>
                                        </div>  
                                    </div>
                                </div>
                                <div class="col-6">
                                    <div class="card">
                                        <div class="grid">
                                            <div class="col-4" style="text-align: center;">实收</div>
                                            <div class="col-4" style="text-align: center;">待收</div>
                                            <div class="col-4" style="text-align: center;">优惠</div>
                                            <div class="card col-12">
                                                
                                                <div class="card col-6">
                                                    <div>优惠券</div>
                                                    <div>5元</div>
                                                </div>
                                                <!-- 不同支付方式显示不同<div> -->
                                                    <template v-if="currentPaymentMethod === '现金'">
                                                        <div style="display: flex; justify-content: space-between; align-items: center;">
                                                            <div class="card" style="flex-grow: 1; margin-right: 10px; display: flex; justify-content: space-between; align-items: center;">
                                                            <div style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
                                                                <div>{{ currentPaymentMethod }}</div>
                                                                <div>{{ appendedNumbers }}</div>
                                                            </div>
                                                            </div>
                                                            <div class="card" style="flex-grow: 1; margin-bottom: 30px; display: flex; justify-content: space-between; align-items: center;">
                                                            <div style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
                                                                <div>找零</div>
                                                                
                                                            </div>
                                                            </div>
                                                        </div>
                                                    </template>
                                                <template v-else>
                                                    <div class="card" style="display: flex; justify-content: space-between; align-items: center;">
                                                        <div>{{currentPaymentMethod}}</div>
                                                        <div>{{ appendedNumbers }}</div>
                                                    </div>
                                                </template> 

                                            </div>
                                            <div class="card col-2">
                                                <button @click="appendNumber('1')" style="width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;">
                                                    <span class="center">1</span>
                                                </button>
                                            </div>
                                            <div class="card col-2">
                                                <button @click="appendNumber('2')" style="width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;">
                                                    <span class="center">2</span>
                                                </button>
                                            </div>
                                            <div class="card col-2">
                                                <button @click="appendNumber('3')" style="width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;">
                                                    <span class="center">3</span>
                                                </button>
                                            </div>
                                            <div class="card col-2">
                                                <button @click="appendNumber('4')" style="width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;">
                                                    <span class="center">4</span>
                                                </button>
                                            </div>
                                            <div class="card col-2">
                                                <button @click="appendNumber('5')" style="width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;">
                                                    <span class="center">5</span>
                                                </button>
                                            </div>
                                            <div class="card col-2">
                                                <button @click="removeLastDigit" style="width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;">
                                                    <span class="center">X</span>
                                                </button>
                                            </div>
                                            <div class="card col-2">
                                                <button @click="appendNumber('6')" style="width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;">
                                                    <span class="center">6</span>
                                                </button>
                                            </div>
                                            <div class="card col-2">
                                                <button @click="appendNumber('7')" style="width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;">
                                                    <span class="center">7</span>
                                                </button>
                                            </div>
                                            <div class="card col-2">
                                                <button @click="appendNumber('8')" style="width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;">
                                                    <span class="center">8</span>
                                                </button>
                                            </div>
                                            <div class="card col-2">
                                                <button @click="appendNumber('9')" style="width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;">
                                                    <span class="center">9</span>
                                                </button>
                                            </div>
                                            <div class="card col-2">
                                                <button @click="appendNumber('0')" style="width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;">
                                                    <span class="center">0</span>
                                                </button>
                                            </div>
                                            <div class="card col-2">
                                            <button @click="clearNumber" style="width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;">
                                                <span class="center">清空</span>
                                            </button>
                                        </div>
                                            <div class="card col-2">
                                                <button style="width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;">
                                                    <span class="center">00</span>
                                                </button>
                                            </div>
                                            <div class="card col-2">
                                                <button style="width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;">
                                                    <span class="center">100</span>
                                                </button>
                                            </div>
                                            <div class="card col-2">
                                                <button style="width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;">
                                                    <span class="center">200</span>
                                                </button>
                                            </div>
                                            <div class="card col-2">
                                                <button style="width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;">
                                                    <span class="center">500</span>
                                                </button>
                                            </div>
                                            <div class="card col-2">
                                                <button style="width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;">
                                                    <span class="center">.</span>
                                                </button>
                                            </div>
                                            <div class="card col-2">
                                                <button style="width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;">
                                                    <span class="center">确定支付</span>
                                                </button>
                                            </div>
                                        </div>  
                                    </div>
                                </div>
                            </div>

                        </Dialog>

            </template>

    <style scoped>
    

    .text-white {
    color: white;
}

    </style>
