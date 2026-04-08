/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      colors: {
        base:    "#0a0a0c",
        surface: "#121216",
        raised:  "#1b1b22",
        border:  "#2d2d3a",
        accent:  "#33509b",
        green:   "#689d8a",
        muted:   "#9494a3", 
        faint:   "#4a4a58",
      },
      fontFamily: {
        mono: ["'Fira Code'", "'Cascadia Code'", "'SF Mono'", "monospace"],
      },
    },
  },
  plugins: [],
};
