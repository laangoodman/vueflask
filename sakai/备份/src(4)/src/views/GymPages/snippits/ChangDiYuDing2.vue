
<script setup>
import CCModal from '@/views/GymPages/snippits/CCModal.vue';
import { ref } from 'vue';
import axios from 'axios';

const SportFields = ref([])
const VenueAreas = ref([])

const fetchData = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:5000/Venue/Date');
        const data = response.data; // 从响应中获取数据
        const venueData = data.venue_data; // 获取第一个数据（场馆数据）
        const areasData = data.areas_data; // 获取第二个数据（区域数据）

        SportFields.value = venueData; // 将数据赋值给 SportFields
        VenueAreas.value = areasData;

        console.log(SportFields);
        console.log(VenueAreas.value);

    } catch (error) {
        console.error('场馆预定获取数据出错:', error);
    }
};

fetchData(); // 调用 fetchData 来获取数据

</script>
<template>
    <div class="card">
        <TabView>
            <TabPanel v-for="itemArea in VenueAreas" :header="itemArea.AreaName" :key="itemArea.AreaId">
                <p class="line-height-3 m-0">
                <div class="grid">
                    <div class="col-12 md:col-6 lg:col-3" v-for="itemVenue in SportFields" :key="itemVenue.VenueId">
                        <div class="surface-card shadow-2 p-3 border-round"  v-if="itemArea.AreaName === itemVenue.AreaName">
                            <div class="flex justify-content-between mb-3">
                                <div> 
                                    <span class="block text-500 font-medium mb-3">{{ itemVenue.vacancy ? '空闲' : '忙碌' }}</span>
                                    <div class="text-900 font-medium text-xl">{{ itemVenue.disciplines }}</div>
                                </div>
                            </div>
                            <CCModal/>
                        </div>
                    </div>
                </div>
                </p>
            </TabPanel>
        </TabView>
    </div>
</template>

<style lang="scss" scoped></style>
