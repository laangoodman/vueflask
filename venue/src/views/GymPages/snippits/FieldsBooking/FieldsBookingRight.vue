
<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { watch } from 'vue';
import { store } from '@/views/GymPages/snippits/FieldsBooking/FieldsBooking.js'; // Adjust the path as needed
import { updateTimeSelection } from '@/views/GymPages/Gymjs/store1.js'; // Adjust the path as needed
import { ClearDataWhenTabChanged } from '@/views/GymPages/Gymjs/store1.js'; // Adjust the path as needed
const SportFields = ref([])
const VenueAreas = ref([])
const API = process.env.API_URL;


const fetchData = async () => {
    try {


        const response = await axios.get(`${API}/api/Venue/Date`);
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
const isCardVisible = ref(false);
const selectedTime = ref([]);
const toggleTimeSelection = (timeSlot) => {
  updateTimeSelection(timeSlot);
  store.aa = timeSlot.price;
  console.log(timeSlot.price);
  if (timeSlot.status !== 1) return; // Only proceed if the slot is available
  const index = selectedTime.value.findIndex(time => time === timeSlot.time);
  if (index !== -1) {
    selectedTime.value.splice(index, 1); // Time already selected, remove it
  } else {
    selectedTime.value.push(timeSlot.time); // Add time since it's available
  }  
  store.newButtonVisible = true; // Show the new button
};

const onTabChange = () => {
  isCardVisible.value = false;
  selectedTime.value = [];
  ClearDataWhenTabChanged();
  store.newButtonVisible = false; // Hide the new button

  console.log('changed13' );
};

const calendarValue = ref(new Date()); // Set to today's date by default
const minDate = ref(new Date()); // Set the minimum date to today
const maxDate = ref(new Date()); // Set the maximum date to 4 days from today
// Set the maxDate to 4 days from today
maxDate.value.setDate(maxDate.value.getDate() + 4);
//选时间段
const lastSelectedDiscipline = ref(null); // Keep track of the last selected discipline
const timeSlots = ref([]); // Initially an empty array
// Watching calendarValue for changes
watch(calendarValue, async (newValue, oldValue) => {

      const response = await axios.post(`${API}/api/Venue/VenueTime`, {

      date: calendarValue.value.toISOString().split('T')[0] // Format date as YYYY-MM-DD
    });
     console.log('新值：', newValue);
      console.log('旧值：', oldValue);
   // 在这里执行您想要的操作，比如向服务器发送 POST 请求
      timeSlots.value = response.data.map(slot => ({
      time: slot.Time,
      status: slot.DateStatus // Make sure this matches the property name in your server response
    }));
  });
  
const toggleCard = async (disciplines) => {
        ClearDataWhenTabChanged();
        selectedTime.value = [];
        store.newButtonVisible = false; // Hide the new button
        store.cc = disciplines;  // Update the store's AreaName
        if (lastSelectedDiscipline.value !== disciplines) {
          // If the newly selected discipline is different from the last, always show the card
          isCardVisible.value = true;
        } else {
          // If the same discipline is clicked, toggle the visibility
          isCardVisible.value = !isCardVisible.value;
        }
        lastSelectedDiscipline.value = disciplines; // Update the last selected discipline
        if (isCardVisible.value) {
        try {
          const response = await axios.post(`${API}/api/Venue/VenueTime`, {
            data: disciplines,
            date: calendarValue.value.toISOString().split('T')[0] // Format date as YYYY-MM-DD
          });
          // Handling server response
          console.log('Server Response:', response.data);
          // Updating timeSlots based on the server response
          // Map each slot to a new format if needed
          timeSlots.value = response.data.map(slot => ({
            time: slot.Time,
            status: slot.DateStatus, // Make sure this matches the property name in your server response
            price: slot.Price // 把价格加上去，之前没加
          }));
        } catch (error) {
          // Handling errors
          console.error('Error:', error);
        }
      }
};
//功能：选中球场后选时间
        const SelectTime = (time) => {
          selectedTime.value = time;
        };

// 先点击场馆，然后选中时间，
//例如我选中了篮球场1然后选择1-3点然后点提交
//那么我会传这样一个json到后端: 
//  {
//    user： xx  
//    Field : 篮球场1的对应id
//    timeslot  : 数据库里对应的时间
//    
//    
//  }
// 在此之前我会从后端收到一个像timeslot的数据，是boolean值（别的形式也OK）像
// const timeSlots里一样，在第52行查看
//是否是这个逻辑
//有出入的地方我们沟通，变量名我对应改成数据库里的
//设置 timeslot= 0的地方样式变为不可选取
      const handleSelectTime = (time) => {
        if (time.clickable) {
          selectedTime.value = time;
        }
      };

</script>
<template>
    <div class="card">
        <TabView @tab-change="onTabChange">
              <!-- New Tab for 'All' -->
    <TabPanel header="全部">
        <div class="grid">
            <template v-for="itemVenue in SportFields" :key="itemVenue.VenueId">
                <div class="col-4">
                    <!-- Venue Card -->
                    <div class="col-12 surface-card shadow-2 p-3 border-round yahei-font" @click="toggleCard(itemVenue.disciplines)">
                        <!-- Venue Details -->
                        <div class="flex justify-content-between mb-3">
                            <div>
                                <span class="block text-500 font-medium mb-3">{{ itemVenue.vacancy ? '空闲' : '忙碌' }}</span>
                                <span class="text-900 font-medium text-xl">{{ itemVenue.disciplines }}</span>
                            </div>
                        </div>
                        <hr>
                        <button>
                            <span class="center">场地预定</span>
                        </button>
                    </div>
                </div>
            </template>
        </div>
    </TabPanel>

    <!-- Existing Tabs for Each Area -->
            <TabPanel v-for="itemArea in VenueAreas" :header="itemArea.AreaName" :key="itemArea.AreaId">
                <p class="line-height-3 m-0">
                <div class="grid">
                    <template  v-for="itemVenue in SportFields" :key="itemVenue.VenueId">
                        <template v-if="itemArea.AreaName === itemVenue.AreaName">
                        
                          <div class="col-4">   
                            <div class="col-12 surface-card shadow-2 p-3 border-round yahei-font" @click="toggleCard(itemVenue.disciplines)">
                              <div class="flex justify-content-between mb-3">
                                <div> 
                                  <span class="block text-500 font-medium mb-3">{{ itemVenue.vacancy ? '空闲' : '忙碌' }}</span>
                                  <span class="text-900 font-medium text-xl">{{ itemVenue.disciplines }}</span>
                                </div>
                              </div>
                              <hr>
                              <button>
                                <span class="center">
                                  场地预定
                                </span>
                              </button>
                            </div>
                          </div>
                </template>
                </template>
                </div>
                </p>
            </TabPanel>
        </TabView>
    </div>

    <div class="card fixed-card" v-if="isCardVisible">
        <div class="mb-4">
            <h5>Calendar</h5>
            <Calendar :showIcon="true" :showButtonBar="true" v-model="calendarValue" :minDate="minDate" :maxDate="maxDate"></Calendar>
        </div>
      <div class="grid">
          <template v-for="timeSlot in timeSlots" :key="timeSlot.time">
                <div class="col-1 ">
                        <button class="time-button"
                              :class="{
                                'selected': selectedTime.includes(timeSlot.time),
                                'available': timeSlot.status === 1,
                                'booked': timeSlot.status === 2
                          }"
                              @click="toggleTimeSelection(timeSlot)"
                              :disabled="timeSlot.status === 0 || timeSlot.status === 2">
                              {{ timeSlot.time }}
                        </button>  
                </div>
          </template>
      </div>    
  </div> 
</template>

<style scoped>

.fixed-card {
    position: fixed;   /* Fixed positioning relative to the viewport */
    bottom: 15px;      /* Positioned 20px above the bottom */
    right: 25px;       /* Positioned 20px from the right */
    width: 980px;      /* Fixed width, adjust as needed */
    height: auto;      /* Height will adjust based on content */
    z-index: 1000;     /* Ensure it's above other elements */
    background-color: white; /* Optional: Set background color */
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2); /* Optional: Add shadow for better visibility */
    overflow: auto;    /* Add scroll if content overflows */
}

.center {
    display: flex;
    justify-content: center; /* Horizontally center */
    align-items: center;     /* Vertically center */
    
}

.time-button {
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 0.25rem;
    background-color: #f0f0f0;
    color: #333;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.2s, box-shadow 0.2s, transform 0.2s;
    margin: 0.2rem;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2);
  }

  .time-button.available {
    background-color: rgb(167, 233, 167); /* Color for available slots */
  }

  .time-button.booked {
    background-color: red; /* Color for booked slots */
  }

  .time-button.booked, .time-button.booked:disabled {
    background-color: red; /* Color for booked slots */
    color: white; /* Change text color for better visibility */
}

.time-button:disabled {
    background-color: grey; /* Color for other disabled slots */
    color: #666666;
    cursor: not-allowed;
}

  .time-button:disabled {
    background-color: grey; /* Color for disabled slots */
  }

  .time-button:hover {
    background-color: #e0e0e0;
  }

  .time-button:active {
    transform: translateY(2px);
    box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.2);
  }


  .time-button.selected {
    background-color: blue;
    color: white;
  }

  .time-button:disabled {
    background-color: #cccccc;
    color: #666666;
    cursor: not-allowed;
  }



  .surface-card button {
    width: 100%;
    border: none;
    padding: 10px 0;
    background-color: transparent;
    cursor: pointer;
    transition: background-color 0.2s; /* Smooth transition for background color */
    /* Rest of your button styling */
  }

  .surface-card button:active {
    background-color: rgb(127, 127, 255); /* Change background to blue when active */
    color: white; /* Optional: change text color if needed */
  }

  .center {
    display: flex;
    justify-content: center;
    align-items: center;
    /* Other styling as needed */
  }

  .yahei-font {
  font-family: 'Microsoft YaHei', sans-serif;
}

</style>

