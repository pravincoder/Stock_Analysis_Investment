/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      typography: {
        DEFAULT: {
          css: {
            color: '#333',
            a: {
              color: '#1d4ed8',
              textDecoration: 'underline',
              '&:hover': {
                color: '#2563eb',
              },
            },
            code: {
              color: '#e11d48',
            },
            pre: {
              backgroundColor: '#f3f4f6',
            },
          },
        },
      },
    },
  },
    plugins: [
      require('@tailwindcss/typography'),
  ],
};
