import { colors } from 'tailwindcss/defaultTheme'

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/**/*.html',
  ],
  theme: {
    extend: {
      backgroundImage: {
          'arvore': "url('../img/arvore.png')",
      },
      colors: {
        red: {
          ...colors.red, "yuri": "#FF0000"
        }
      }  
    },
  },
  plugins: [],
}

