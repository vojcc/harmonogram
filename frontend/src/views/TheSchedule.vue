<script setup>
import { onMounted, onUpdated, ref } from 'vue'
import { groups } from '../../../backend/schedule.json'
import { ChevronDownIcon, ChevronUpIcon } from '@heroicons/vue/24/outline/index.js'
import { onClickOutside, useStorage } from '@vueuse/core'
import NoLessons from '@/components/UI/empty_states/NoLessons.vue'
import SetSettings from '@/components/UI/empty_states/SetSettings.vue'
import LessonScheduleCard from '@/components/UI/LessonScheduleCard.vue'

const group = useStorage('group', null)
const selectedDay = ref('')
const showGroupList = ref(false)
const groupList = ref(null)
const buttonRefs = ref({})
const scrollContainer = ref(null)

onMounted(() => {
  if (group.value) {
    refreshSelectedGroupDays()
  }
})

onUpdated(() => {
  if (selectedDay.value && buttonRefs.value[selectedDay.value.date]) {
    buttonRefs.value[selectedDay.value.date].scrollIntoView({
      behavior: 'smooth',
      inline: 'center',
      block: 'nearest',
    })
  }
})

function selectGroup(groupName) {
  group.value = groupName
  refreshSelectedGroupDays()
  toggleShowGroupList()
}

function selectDay(day) {
  selectedDay.value = day
}

const selectedGroupDays = ref([])

function refreshSelectedGroupDays() {
  const selectedGroup = groups.find((item) => item.name === group.value)
  selectedGroupDays.value = selectedGroup?.days

  //If user selected day, find in selectedGroupDays day with the closest date, if not find the closest day to today's date
  let date = selectedDay.value ? new Date(selectedDay.value.date) : new Date()

  const closest = selectedGroupDays.value
    .map((entry) => ({
      ...entry,
      parsedDate: new Date(entry.date),
    }))
    .filter((entry) => {
      const entryDateWithoutTime = new Date(entry.parsedDate).setHours(0, 0, 0, 0)
      const currentDateWithoutTime = new Date(date).setHours(0, 0, 0, 0)

      return entryDateWithoutTime >= currentDateWithoutTime
    })
    .sort((a, b) => a.parsedDate - b.parsedDate)

  selectedDay.value =
    closest.length > 0 ? closest[0] : selectedGroupDays.value[selectedGroupDays.value.length - 1]
}

function setButtonRef(date, element) {
  if (element) {
    buttonRefs.value[date] = element
  }
}

function toggleShowGroupList() {
  showGroupList.value = !showGroupList.value
}

onClickOutside(groupList, () => {
  showGroupList.value = false
})
</script>

<template>
  <main>
    <div class="p-4 sm:p-5">
      <div class="flex flex-col">
        <div class="w-full">
          <form class="flex flex-col gap-6">
            <div>
              <label class="block text-sm font-bold text-gray-900 mb-0.5">Grupa</label>
              <div ref="groupList" class="relative">
                <button
                  @click="toggleShowGroupList"
                  type="button"
                  :class="showGroupList ? 'ring-uewblue ring-2' : 'ring-gray-200 ring-1'"
                  class="flex items-center shadow relative min-h-12 w-full lg:w-1/4 rounded-lg p-3 text-left text-gray-800 ring-inset"
                >
                  <span class="text-sm">{{ group }}</span>
                  <span
                    class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-2"
                  >
                    <ChevronUpIcon v-if="showGroupList" class="size-4 text-gray-800" />
                    <ChevronDownIcon v-else class="size-4 text-gray-800" />
                  </span>
                </button>

                <transition name="slide-down">
                  <ul
                    v-if="showGroupList"
                    class="absolute z-10 mt-1 max-h-60 w-full lg:w-1/4 overflow-auto rounded-lg bg-white py-1 shadow-lg ring-1 ring-black/5 focus:outline-none text-sm"
                  >
                    <li
                      @click="selectGroup(groupToSelect.name)"
                      v-for="groupToSelect in groups"
                      :key="groupToSelect.name"
                      class="relative select-none py-2 pl-3 pr-9 text-gray-900 cursor-pointer"
                      :class="
                        groupToSelect.name === group
                          ? 'bg-gray-100 font-medium'
                          : 'hover:bg-gray-50'
                      "
                    >
                      {{ groupToSelect.name }}
                    </li>
                  </ul>
                </transition>
              </div>
            </div>
          </form>
        </div>
      </div>

      <section>
        <div v-if="selectedGroupDays.length">
          <div
            class="flex flex-row overflow-x-auto lg:flex-wrap gap-2 mt-6 mb-2"
            ref="scrollContainer"
          >
            <button
              @click="selectDay(day)"
              class="px-3 py-1.5 mb-4 text-sm border rounded-lg shadow"
              v-for="day in selectedGroupDays"
              :key="day.date"
              :class="
                selectedDay && selectedDay.date === day.date
                  ? 'bg-uewblue text-white '
                  : 'text-gray-800 hover:bg-gray-50'
              "
              :ref="(element) => setButtonRef(day.date, element)"
            >
              <span class="flex flex-col justify-center items-center">
                <span class="font-medium whitespace-nowrap">{{
                  new Date(day.date).toLocaleDateString('pl-PL', {
                    day: '2-digit',
                    month: '2-digit',
                    year: 'numeric',
                  })
                }}</span>
                <small
                  :class="
                    selectedDay && selectedDay.date === day.date ? 'text-white' : 'text-gray-400'
                  "
                >
                  {{ day.name }}
                </small>
              </span>
            </button>
          </div>

          <div v-if="selectedDay?.lessons?.length">
            <div class="flex" v-for="(lesson, index) in selectedDay.lessons" :key="index">
              <div class="flex flex-col my-3 gap-1 w-full">
                <LessonScheduleCard :lesson="lesson" />
              </div>
            </div>
          </div>
          <div v-else class="mt-12">
            <NoLessons />
          </div>
        </div>
        <div v-else class="mt-12">
          <SetSettings />
        </div>
      </section>
    </div>
  </main>
</template>

<style scoped>
.slide-down-enter-active,
.slide-down-leave-active {
  transition:
    max-height 0.3s ease,
    opacity 0.3s ease;
  overflow: hidden;
}

.slide-down-enter-from {
  max-height: 0;
  opacity: 0;
}

.slide-down-enter-to {
  max-height: 15rem;
  opacity: 1;
}

.slide-down-leave-from {
  max-height: 15rem;
  opacity: 1;
}

.slide-down-leave-to {
  max-height: 0;
  opacity: 0;
}
</style>
