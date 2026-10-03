/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./*.html'],
  // used only by the PHP templates in kollargumi-com (tools/build_from_redesign.py)
  safelist: ['text-right', 'overflow-x-auto', 'px-3', 'md:p-6', 'md:text-5xl'],
  theme: {
    extend: {
      colors: {
        brand: { DEFAULT: '#0B7385', light: '#00B4C9', dark: '#094E5A' },
        dark: { DEFAULT: '#0D1B1E', light: '#16292D', muted: '#1E3438' },
        cream: { DEFAULT: '#F6FAFB', dark: '#E9F1F2' },
        ink: '#0D1B1E',
        muted: '#566B6E',
      },
      fontFamily: {
        display: ['"Sora"', 'system-ui', 'sans-serif'],
        body: ['"DM Sans"', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
