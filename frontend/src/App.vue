<template>
  <main>
    <section class="hero">
      <h1>Antyperfectionism Habit Tracker</h1>
      <p>{{ message }}</p>
      <button @click="fetchApi">Check Backend</button>
      <p v-if="apiResponse">Backend says: {{ apiResponse }}</p>
    </section>

    <section class="habits">
      <h2>Saved Habits</h2>

      <div v-if="loading" class="status">Loading habits…</div>
      <div v-else-if="error" class="status error">{{ error }}</div>
      <div v-else-if="habits.length === 0" class="status">No habits yet.</div>

      <ul v-else>
        <li v-for="habit in habits" :key="habit.id">
          <strong>{{ habit.name }}</strong>
          <div class="habit-meta">
            <span>{{ habit.occurance }} · {{ habit.frequency }} {{ habit.habit_type === 'binary' ? 'times' : 'minutes'}}</span>
            <span>({{ habit.habit_type }})</span>
          </div>
          <p v-if="habit.description">{{ habit.description }}</p>
        </li>
      </ul>
    </section>
  </main>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

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

async function fetchApi() {
  try {
    const res = await fetch('/api/')
    const data = await res.json()
    apiResponse.value = data.message || JSON.stringify(data)
  } catch (err) {
    apiResponse.value = 'Unable to reach backend.'
  }
}

async function fetchHabits() {
  loading.value = true
  error.value = ''

  try {
    const res = await fetch('/api/habits')
    if (!res.ok) {
      throw new Error(`Server returned ${res.status}`)
    }
    habits.value = await res.json()
  } catch (err) {
    error.value = 'Unable to load habits from backend.'
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchHabits()
})
</script>

<style>
main {
  font-family: system-ui, sans-serif;
  padding: 2rem;
}
.hero,
.habits {
  max-width: 640px;
  margin: auto;
  text-align: left;
}
.hero {
  margin-bottom: 2rem;
}
.status {
  margin: 1rem 0;
  color: #4b5563;
}
.error {
  color: #b91c1c;
}
button {
  margin-top: 1rem;
  padding: 0.75rem 1.25rem;
  font-size: 1rem;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  background: #4f46e5;
  color: white;
}
button:hover {
  background: #4338ca;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  border: 1px solid #e5e7eb;
  border-radius: 0.75rem;
  padding: 1rem;
  margin-bottom: 1rem;
  background: #ffffff;
}
.habit-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  color: #6b7280;
  margin: 0.5rem 0;
}
</style>
