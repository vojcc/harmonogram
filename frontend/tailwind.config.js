/** @type {import('tailwindcss').Config} */
export default {
  purge: ['./index.html', './src/**/*.vue'],
  content: [],
  theme: {
    extend: {
      colors: {
        'uewyellow': {
          light: '#fdce6d',
          DEFAULT: '#fcae0c',
          dark: '#eca003'
        },
        'uewblue': {
          light: '#5f67a1',
          DEFAULT: '#1b2779',
          dark: '#101748'
        }
      },
    },
  },
  plugins: [],
}

