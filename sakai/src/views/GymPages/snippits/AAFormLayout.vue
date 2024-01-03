<script setup>
import { ref } from 'vue';
import AASearchUser from './AASearchUser.vue';


const dropdownItems = ref([
    { name: 'Option 1', code: 'Option 1' },
    { name: 'Option 2', code: 'Option 2' },
    { name: 'Option 3', code: 'Option 3' }
]);

const dropdownItem = ref(null);
</script>

<template>
    <div class="grid">
        <div class="col-12 md:col-4">
            <AASearchUser/>

  
        </div>

        <div class="col-12 md:col-6">
            <div class="card p-fluid">
                <h5>Horizontal</h5>
                <div class="field grid">
                    <label for="name3" class="col-12 mb-2 md:col-2 md:mb-0">Name</label>
                    <div class="col-12 md:col-10">
                        <InputText id="name3" type="text" />
                    </div>
                </div>
                <div class="field grid">
                    <label for="email3" class="col-12 mb-2 md:col-2 md:mb-0">Email</label>
                    <div class="col-12 md:col-10">
                        <InputText id="email3" type="text" />
                    </div>
                </div>
            </div>

            <div class="card">
                <h5>Inline</h5>
                <div class="formgroup-inline">
                    <div class="field">
                        <label for="firstname1" class="p-sr-only">Firstname</label>
                        <InputText id="firstname1" type="text" placeholder="Firstname" />
                    </div>
                    <div class="field">
                        <label for="lastname1" class="p-sr-only">Lastname</label>
                        <InputText id="lastname1" type="text" placeholder="Lastname" />
                    </div>
                    <Button label="Submit"></Button>
                </div>
            </div>

            <div class="card">
                <h5>Help Text</h5>
                <div class="field p-fluid">
                    <label for="username">Username</label>
                    <InputText id="username" type="text" />
                    <small>Enter your username to reset your password.</small>
                </div>
            </div>
        </div>

    
    </div>
</template>
