/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      colors: {
        base:    "#0a0c14",
        surface: "#121626",
        raised:  "#1a1f35",
        border:  "#2c3353",
        accent:  "#4f7cff",
        green:   "#3ddc97",
        muted:   "#b0b7d1",
        faint:   "#6c7393",
      },
      fontFamily: {
        mono: ["'Fira Code'", "'Cascadia Code'", "'SF Mono'", "monospace"],
      },
    },
  },
  plugins: [],
};
