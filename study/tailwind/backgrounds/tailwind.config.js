/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/**/*.html',
  ],
  theme: {
    extend: {
      backgroundImage: {
          'arvore': "url('../img/arvore.png')",
      }  
    },
  },
  plugins: [],
}

