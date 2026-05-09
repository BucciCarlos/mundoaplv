/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./backend/templates/**/*.html",
    "./backend/static/js/**/*.js",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#2A9D8F', // Turquesa profesional
          dark: '#1E6F65',
          light: '#E9F5F4',
        },
        secondary: {
          DEFAULT: '#72EFDD', // Verde seguro
          dark: '#56B3A6',
        },
        accent: {
          DEFAULT: '#E76F51', // Naranja/Ambar para alertas
          light: '#F4A261',
        },
        health: {
          blue: '#264653', // Azul marino profundo
          slate: '#333333',
        }
      },
      fontFamily: {
        sans: ['Lato', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
