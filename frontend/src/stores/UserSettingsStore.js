import { defineStore } from 'pinia'

export const useUserSettingsStore = defineStore('UserSettingsStore', {
  state: () => ({
    group: '',
    semester: 'zimowy',
  }),
  actions: {
    setGroup(group) {
      this.group = group
      localStorage.setItem('group', group)
    },
    getGroup() {
      return this.group || localStorage.getItem('group') || ''
    },

    getSemester() {
      return this.semester || localStorage.getItem('semester') || ''
    },
  },
})
