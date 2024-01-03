import { reactive } from 'vue';

export const store = reactive({
  selectedItem: null,
  showItemDetails(item) {
    this.selectedItem = item;
  }
});

export function ClearData() {
    selectedItem = null;
    console.log('changed11' );
   
  }