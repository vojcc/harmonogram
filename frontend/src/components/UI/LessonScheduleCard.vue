<script setup>
defineProps({
  lesson: Object,
})
</script>

<template>
  <div class="w-full flex gap-3 items-center">
    <span class="text-xs font-medium text-gray-800">{{ lesson.start_hour }}</span>
    <hr class="flex-grow border-t border-gray-200" />
  </div>

  <div class="flex justify-end">
    <div
      :style="`border-color: ${lesson.color}`"
      class="flex flex-col border-l-[5px] border-dotted ml-10 w-full px-4"
    >
      <span class="font-bold text-gray-800">{{ lesson.name }}</span>
      <span class="text-xs text-gray-600">{{ lesson.name_abbr }}</span>
      <span class="text-gray-600 text-xs">{{ lesson.teacher_name }}</span>
    </div>
  </div>

  <div class="w-full flex gap-3 items-center">
    <span class="text-xs font-medium text-gray-800">{{ lesson.end_hour }}</span>
    <hr class="flex-grow border-t border-gray-200" />
  </div>
</template>
