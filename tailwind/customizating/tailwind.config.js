/** @type {import('tailwindcss').Config} */

const { colors } = require("tailwindcss/defaultTheme") 

module.exports = {
  content: [
    './src/**/*.{html,js}',
  ],
  theme: {
    extend: {
      colors: {
        red: {
          ...colors.red,
          "500": "#FFFFF",
        },
      }
    },
  },
  plugins: [],
}

