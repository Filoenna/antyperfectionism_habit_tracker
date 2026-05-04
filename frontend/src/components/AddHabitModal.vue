<template>
  <Dialog :visible="visible" @update:visible="$emit('update:visible', $event)" header="Add New Habit" modal>
    <form @submit.prevent="submitForm" class="p-fluid">
      <div class="p-field p-mb-3">
        <label for="name" class="p-d-block p-mb-2">Habit Name</label>
        <InputText id="name" v-model="form.name" required />
      </div>

      <div class="p-field p-mb-3">
        <label for="description" class="p-d-block p-mb-2">Description (optional)</label>
        <Textarea id="description" v-model="form.description" rows="3" />
      </div>

      <div class="p-field p-mb-3">
        <label for="habit_type" class="p-d-block p-mb-2">Habit Type</label>
        <Dropdown id="habit_type" v-model="form.habit_type" :options="habitTypeOptions" optionLabel="label" optionValue="value" placeholder="Select type" />
      </div>

      <div class="p-field p-mb-3">
        <label for="occurance" class="p-d-block p-mb-2">Occurrence</label>
        <Dropdown id="occurance" v-model="form.occurance" :options="occurrenceOptions" optionLabel="label" optionValue="value" placeholder="Select occurrence" />
      </div>

      <div class="p-field p-mb-3">
        <label for="frequency" class="p-d-block p-mb-2">Frequency</label>
        <InputNumber id="frequency" v-model="form.frequency" :min="1" required />
      </div>

      <div v-if="form.habit_type === 'quantitative'" class="p-field p-mb-3">
        <label for="target_value" class="p-d-block p-mb-2">Target Value (minutes)</label>
        <InputNumber id="target_value" v-model="form.target_value" :min="1" />
      </div>

      <div class="p-d-flex p-jc-end">
        <Button type="submit" label="Add Habit" icon="pi pi-plus" />
      </div>
    </form>
  </Dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import Dialog from 'primevue/dialog'
import InputText from 'primevue/inputtext'
import Textarea from 'primevue/textarea'
import Dropdown from 'primevue/dropdown'
import InputNumber from 'primevue/inputnumber'
import Button from 'primevue/button'

interface Props {
  visible: boolean
}

const props = defineProps<Props>()
const emit = defineEmits<{
  'update:visible': [value: boolean]
  addHabit: [habit: any]
}>()

const form = ref({
  name: '',
  description: '',
  habit_type: '',
  occurance: '',
  frequency: 1,
  target_value: null as number | null
})

const habitTypeOptions = [
  { label: 'Binary (done/not done)', value: 'binary' },
  { label: 'Quantitative (with target)', value: 'quantitative' }
]

const occurrenceOptions = [
  { label: 'Daily', value: 'daily' },
  { label: 'Weekly', value: 'weekly' },
  { label: 'Monthly', value: 'monthly' }
]

function submitForm() {
  if (!form.value.name || !form.value.habit_type || !form.value.occurance) {
    return
  }

  const habit = {
    ...form.value,
    is_active: true
  }

  emit('addHabit', habit)
  resetForm()
  emit('update:visible', false)
}
</script>