    /** @type {import('tailwindcss').Config} */
    module.exports = {
      content: ["./templates/**/*.html"],
        safelist: ['button', 'primary', 'secondary', 'danger'],
        theme: {
          extend: {
            boxShadow: {
              underline: "inset 0 -2px 0 0"
            }
          },
        },
        plugins: [
          require("@tailwindcss/forms"),
          require("@tailwindcss/typography"),
        ],
      }