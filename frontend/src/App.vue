<template>
  <Menu :items="menuItems" />
  <AddHabitModal v-model:visible="showAddHabitModal" @addHabit="handleAddHabit" />
  <main class="app-shell">
    <section class="hero p-shadow-2 p-rounded p-p-4 p-mb-4">
      <h1 class="p-mb-3">Antyperfectionism Habit Tracker</h1>
      <p class="p-mb-4">{{ message }}</p>
      <Button label="Check Backend" icon="pi pi-cloud" @click="fetchApi" />
      <p v-if="apiResponse" class="p-mt-3">Backend says: {{ apiResponse }}</p>
    </section>

    <section class="habits">
      <h2 class="p-mb-3">Saved Habits</h2>

      <div v-if="loading" class="p-text-secondary p-mb-3">Loading habits…</div>
      <div v-else-if="error" class="p-mb-3 p-error">{{ error }}</div>
      <div v-else-if="habits.length === 0" class="p-text-secondary p-mb-3">No habits yet.</div>

      <div v-else class="p-fluid p-formgrid p-grid">
        <Card v-for="habit in habits" :key="habit.id" class="p-col-12 p-md-6 p-mb-3">
          <template #title>
            {{ habit.name }}
          </template>
          <template #content>

            <div class="p-mb-3 p-card-content">
              <span class="p-tag p-tag-rounded p-mr-2">{{ habit.habit_type }} - </span>
              <span>{{ habit.occurance }} · {{ habit.frequency }} {{ habit.habit_type === 'binary' ? 'times' : 'minutes' }}</span>
            </div>
            <p v-if="habit.description" class="p-mb-0">{{ habit.description }}</p>
          </template>
        </Card>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import Card from 'primevue/card'
import Menu from './components/Menu.vue'
import AddHabitModal from './components/AddHabitModal.vue'
import api from './api'
import { MenuItem } from './types'

type Habit = {
  id: number
  name: string
  occurance: string
  frequency: number
  habit_type: string
  target_value?: number | null
  description?: string | null
  is_active: boolean
  created_at: string
  updated_at: string
}

const message = 'A simple Vue + Vite frontend running in Docker.'
const apiResponse = ref('')
const habits = ref<Habit[]>([])
const loading = ref(false)
const error = ref('')
const menuItems: MenuItem[] = [
  { label: 'Add habit', command: () => showAddHabitModal.value = true },
  { label: 'Manage habits' }
]
const showAddHabitModal = ref(false)

async function fetchApi() {
  try {
    const res = await api.get('/')
    apiResponse.value = res.data.message || JSON.stringify(res.data)
  } catch (err) {
    apiResponse.value = 'Unable to reach backend.'
  }
}

async function fetchHabits() {
  loading.value = true
  error.value = ''

  try {
    const res = await api.get<Habit[]>('/habits')
    habits.value = res.data
  } catch (err) {
    error.value = 'Unable to load habits from backend.'
  } finally {
    loading.value = false
  }
}

async function handleAddHabit(habit: any) {
  try {
    await api.post('/habits', habit)
    await fetchHabits() // Refresh the list
  } catch (err) {
    console.error('Error adding habit:', err)
    // Maybe show an error message
  }
}

onMounted(() => {
  fetchHabits()
})
</script>

<style>
main.app-shell {
  font-family: system-ui, sans-serif;
  padding: 2rem;
}
.hero,
.habits {
  max-width: 960px;
  margin: auto;
}
</style>
