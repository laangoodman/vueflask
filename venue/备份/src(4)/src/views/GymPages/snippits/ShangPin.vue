<template>

<div class="card">

    <div class="grid">
        
        <div class="col-12 md:col-6 lg:col-3">
            <div class="surface-card shadow-2 p-3 border-round">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3"></span>
                        <div class="text-900 font-medium text-xl">纸巾</div>
                    </div>
                    <div class="flex align-items-center justify-content-center bg-blue-100 border-round" style="width: 2.5rem; height: 2.5rem">
                        <i class="pi pi-shopping-cart text-blue-500 text-xl"></i>
                    </div>
                </div>
                <span class="text-red-500 font-medium">3元 </span>
           
            </div>
        </div>

        
        <div class="col-12 md:col-6 lg:col-3">
            <div class="surface-card shadow-2 p-3 border-round">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3"></span>
                        <div class="text-900 font-medium text-xl">纸巾</div>
                    </div>
                    <div class="flex align-items-center justify-content-center bg-blue-100 border-round" style="width: 2.5rem; height: 2.5rem">
                        <i class="pi pi-shopping-cart text-blue-500 text-xl"></i>
                    </div>
                </div>
                <span class="text-red-500 font-medium">3元 </span>
           
            </div>
        </div>

        <div class="col-12 md:col-6 lg:col-3">
            <div class="surface-card shadow-2 p-3 border-round">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3"></span>
                        <div class="text-900 font-medium text-xl">纯悦矿泉水</div>
                    </div>
                    <div class="flex align-items-center justify-content-center bg-blue-100 border-round" style="width: 2.5rem; height: 2.5rem">
                        <i class="pi pi-shopping-cart text-blue-500 text-xl"></i>
                    </div>
                </div>
                <span class="text-red-500 font-medium">3元/瓶 </span>
           
            </div>
        </div>

        <div class="col-12 md:col-6 lg:col-3">
            <div class="surface-card shadow-2 p-3 border-round">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3"></span>
                        <div class="text-900 font-medium text-xl">纸巾</div>
                    </div>
                    <div class="flex align-items-center justify-content-center bg-blue-100 border-round" style="width: 2.5rem; height: 2.5rem">
                        <i class="pi pi-shopping-cart text-blue-500 text-xl"></i>
                    </div>
                </div>
                <span class="text-red-500 font-medium">10元 </span>
           
            </div>
        </div>       
    </div>
</div>

<div>
    <h1>{{ goods }}  </h1>
</div>



</template>

<script>
export default {
    data() {
        return {
            goods:[]
        }
    },
    mounted() {
        fetch('http://localhost:3000/goods')
        .then(res => res.json())
        .then(data => this.goods = data)
        .catch(err => console.log(err.message))
    }
}
</script>