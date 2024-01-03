import { reactive } from 'vue';

export const store = reactive({

  
  newButtonVisible: false,
  selectedSlots: [],
  AreaName: '',
  get howmany() {
    return this.selectedSlots.length;
  },

  get bb() {
    return this.howmany;
  },
  aa: '',
  cc: '',

});



// Function to update the selected times and area name
export function updateTimeSelection(timeSlot) {
  const index = store.selectedSlots.findIndex(time => time === timeSlot);
  if (index !== -1) {
    store.selectedSlots.splice(index, 1);
  } else {
    store.selectedSlots.push(timeSlot);
  }
  // console.log(AreaName);
 
  const price = timeSlot.value

 
}

export function ClearDataWhenTabChanged() {
  store.selectedSlots = [];
  console.log('changed11' + store.selectedSlots);
 
}