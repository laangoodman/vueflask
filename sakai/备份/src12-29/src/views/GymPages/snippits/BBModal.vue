<script setup>
import { FilterMatchMode } from 'primevue/api';
import { ref, onMounted, onBeforeMount } from 'vue';
import ProductService from '@/service/ProductService';
import { useToast } from 'primevue/usetoast';

const toast = useToast();

const products = ref(null);
const productDialog = ref(false);
const deleteProductDialog = ref(false);
const deleteProductsDialog = ref(false);
const product = ref({});
const selectedProducts = ref(null);
const dt = ref(null);
const filters = ref({});
const submitted = ref(false);
const statuses = ref([
    { label: '男', value: 'male' },
    { label: '女', value: 'female' }

]);

const productService = new ProductService();

onBeforeMount(() => {
    initFilters();
});
onMounted(() => {
    productService.getProducts().then((data) => (products.value = data));
});
const formatCurrency = (value) => {
    return value.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
};

const openNew = () => {
    product.value = {};
    submitted.value = false;
    productDialog.value = true;
};

const hideDialog = () => {
    productDialog.value = false;
    submitted.value = false;
};

const saveProduct = () => {
    submitted.value = true;
    if (product.value.name && product.value.name.trim() && product.value.price) {
        if (product.value.id) {
            product.value.inventoryStatus = product.value.inventoryStatus.value ? product.value.inventoryStatus.value : product.value.inventoryStatus;
            products.value[findIndexById(product.value.id)] = product.value;
            toast.add({ severity: 'success', summary: 'Successful', detail: 'Product Updated', life: 3000 });
        } else {
            product.value.id = createId();
            product.value.code = createId();
            product.value.image = 'product-placeholder.svg';
            product.value.inventoryStatus = product.value.inventoryStatus ? product.value.inventoryStatus.value : 'INSTOCK';
            products.value.push(product.value);
            toast.add({ severity: 'success', summary: 'Successful', detail: 'Product Created', life: 3000 });
        }
        productDialog.value = false;
        product.value = {};
    }
};

const editProduct = (editProduct) => {
    product.value = { ...editProduct };
    console.log(product);
    productDialog.value = true;
};

const confirmDeleteProduct = (editProduct) => {
    product.value = editProduct;
    deleteProductDialog.value = true;
};

const deleteProduct = () => {
    products.value = products.value.filter((val) => val.id !== product.value.id);
    deleteProductDialog.value = false;
    product.value = {};
    toast.add({ severity: 'success', summary: 'Successful', detail: 'Product Deleted', life: 3000 });
};

const findIndexById = (id) => {
    let index = -1;
    for (let i = 0; i < products.value.length; i++) {
        if (products.value[i].id === id) {
            index = i;
            break;
        }
    }
    return index;
};

const createId = () => {
    let id = '';
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    for (let i = 0; i < 5; i++) {
        id += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return id;
};

const exportCSV = () => {
    dt.value.exportCSV();
};

const confirmDeleteSelected = () => {
    deleteProductsDialog.value = true;
};
const deleteSelectedProducts = () => {
    products.value = products.value.filter((val) => !selectedProducts.value.includes(val));
    deleteProductsDialog.value = false;
    selectedProducts.value = null;
    toast.add({ severity: 'success', summary: 'Successful', detail: 'Products Deleted', life: 3000 });
};

const initFilters = () => {
    filters.value = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS }
    };
};
</script>

<template>


                        
    <Button label="New" icon="pi pi-plus" class="p-button-success mr-2" @click="openNew" />

        <Dialog v-model:visible="productDialog" :style="{ width: '950px' }" header="新增" :modal="true" class="p-fluid">
                <img :src="'demo/images/product/' + product.image" :alt="product.image" v-if="product.image" width="150" class="mt-0 mx-auto mb-5 block shadow-2" />

                <div class="formgrid grid">
        <div class="field col">
            <label for="price">会员卡号</label>
            <InputNumber id="price" v-model="product.price" mode="currency" currency="USD" locale="en-US" :class="{ 'p-invalid': submitted && !product.price }" :required="true" />
            <small class="p-invalid" v-if="submitted && !product.price">Price is required.</small>
        </div>
        <div class="field col">
            <label for="quantity">会员姓名</label>
            <InputNumber id="quantity" v-model="product.quantity" integeronly />
        </div>
        
    </div>

                <div class="formgrid grid">
        <div class="field col">
            <label for="price">手机号码</label>
            <InputNumber id="price" v-model="product.price" mode="currency" currency="USD" locale="en-US" :class="{ 'p-invalid': submitted && !product.price }" :required="true" />
            <small class="p-invalid" v-if="submitted && !product.price">Price is required.</small>
        </div>
        <div class="field col">
            <label for="quantity">身份证号</label>
            <InputNumber id="quantity" v-model="product.quantity" integeronly />
        </div>
        
    </div>


    <div class="formgrid grid">
        <div class="field col">
            <label for="inventoryStatus" class="mb-3">性别</label>
            <Dropdown id="inventoryStatus" v-model="product.inventoryStatus" :options="statuses" optionLabel="label" placeholder="Select a Status">
                <template #value="slotProps">
                    <div v-if="slotProps.value && slotProps.value.value">
                        <span :class="'product-badge status-' + slotProps.value.value">{{ slotProps.value.label }}</span>
                    </div>
                    <div v-else-if="slotProps.value && !slotProps.value.value">
                        <span :class="'product-badge status-' + slotProps.value.toLowerCase()">{{ slotProps.value }}</span>
                    </div>
                        <span v-else>
                            {{ slotProps.placeholder }}
                        </span>
                    </template>
                </Dropdown>

                
                
        </div>
        <div class="field col">
            <label for="quantity">卡面号码</label>
            <InputNumber id="quantity" v-model="product.quantity" integeronly />
        </div>
        
    </div>
    <div class="formgrid grid">
        <div class="field col">
            <label for="price">会员生日</label>
            <InputNumber id="price" v-model="product.price" mode="currency" currency="USD" locale="en-US" :class="{ 'p-invalid': submitted && !product.price }" :required="true" />
            <small class="p-invalid" v-if="submitted && !product.price">Price is required.</small>
        </div>
        <div class="field col">
            <label for="quantity">会员密码</label>
            <InputNumber id="quantity" v-model="product.quantity" integeronly />
        </div>
        
    </div>
    <div class="formgrid grid">
        <div class="field col">
            <label for="price">确认密码</label>
            <InputNumber id="price" v-model="product.price" mode="currency" currency="USD" locale="en-US" :class="{ 'p-invalid': submitted && !product.price }" :required="true" />
            <small class="p-invalid" v-if="submitted && !product.price">Price is required.</small>
        </div>
        <div class="field col">
            <label for="quantity">会员等级</label>
            <InputNumber id="quantity" v-model="product.quantity" integeronly />
        </div>
        
    </div>
    <div class="formgrid grid">
        <div class="field col">
            <label for="price">售卡工本费</label>
            <InputNumber id="price" v-model="product.price" mode="currency" currency="USD" locale="en-US" :class="{ 'p-invalid': submitted && !product.price }" :required="true" />
            <small class="p-invalid" v-if="submitted && !product.price">Price is required.</small>
        </div>
        <div class="field col">
            <label for="quantity">注册充值</label>
            <InputNumber id="quantity" v-model="product.quantity" integeronly />
        </div>
        
    </div>
    <div class="formgrid grid">
        <div class="field col">
            <label for="price">提成员工</label>
            <InputNumber id="price" v-model="product.price" mode="currency" currency="USD" locale="en-US" :class="{ 'p-invalid': submitted && !product.price }" :required="true" />
            <small class="p-invalid" v-if="submitted && !product.price">Price is required.</small>
        </div>
        <div class="field col">
            <label for="quantity">车牌号码</label>
            <InputNumber id="quantity" v-model="product.quantity" integeronly />
        </div>
        
    </div>
    <div class="formgrid grid">
        <div class="field col">
            <label for="price">联系地址</label>
            <InputNumber id="price" v-model="product.price" mode="currency" currency="USD" locale="en-US" :class="{ 'p-invalid': submitted && !product.price }" :required="true" />
            <small class="p-invalid" v-if="submitted && !product.price">Price is required.</small>
        </div>
        <div class="field col">
            <label for="quantity">推荐人</label>
            <InputNumber id="quantity" v-model="product.quantity" integeronly />
        </div>
        
    </div>
    <template #footer>
        <Button label="取消" icon="pi pi-times" class="p-button-text" @click="hideDialog" />
        <Button label="提交" icon="pi pi-check" class="p-button-text" @click="saveProduct" />
    </template>
</Dialog>


</template>