<template>
    <Menubar :model="items">
        <template #start>
            <span class="logo-text">Habit tracker</span>
        </template>
        <template #item="{ item, props }">
            <a v-ripple class="flex items-center menu-item-link" v-bind="props.action">
                <span class="menu-item-label">{{ item.label }}</span>
            </a>
        </template>
        <template #end>
            <div class="flex items-center gap-2">
                <Select v-model="selectedLanguage" :options="languageOptions" optionLabel="label" optionValue="value" placeholder="Select Language" />
            </div>
        </template>
    </Menubar>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { MenuItem } from '../types'
import { Select, Menubar } from 'primevue';


const props = defineProps<{
  items: MenuItem[];
}>();

const selectedLanguage = ref('en');
const languageOptions = [
  { label: 'English', value: 'en' },
  { label: 'Polski', value: 'pl' }
];
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');

.logo-text {
  font-family: 'Dancing Script', cursive;
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--p-primary-color);
  margin-right: 2rem;
}

::v-deep(.p-menu-bar-item-content:hover) {
  background-color: transparent !important;
}

.menu-item-label:hover {
  color: var(--p-primary-color);
}
</style>