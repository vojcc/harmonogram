<script setup>
import {computed} from 'vue'
import {useUserSettingsStore} from '@/stores/UserSettingsStore.js'

const userSettingsStore = useUserSettingsStore()

const group = computed(() =>
  userSettingsStore.getGroup() ? `Grupa ${userSettingsStore.getGroup()}` : '',
)
</script>

<template>
  <nav class="bg-gray-100">
    <div class="flex flex-wrap-reverse gap-4 items-center justify-between px-4 py-3 sm:py-4">
      <div class="flex items-center gap-3">
        <img src="../../assets/uew-logo.png" alt="" class="size-7"/>
        <h1 class="w-fit text-lg sm:text-xl font-bold text-gray-800">Plan zajęć</h1>
      </div>

      <div class="flex flex-col items-end">
        <p class="text-[10px] sm:text-xs font-medium text-nowrap text-gray-800">Informatyka w biznesie</p>
        <p class="text-[10px] sm:text-xs text-gray-500 text-nowrap">{{ group }}&nbsp;</p>
      </div>
    </div>
  </nav>
</template>
