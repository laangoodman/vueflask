import { reactive } from 'vue';

export const store = reactive({
  selectedItem: null,
  showItemDetails(item) {
    this.selectedItem = item;
  }
});