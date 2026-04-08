import { defineConfig } from "astro/config";
import react from "@astrojs/react";
import tailwind from "@astrojs/tailwind";

export default defineConfig({
  site: "https://vlegend14.github.io",
  base: "/code-handbook",

  integrations: [
    react(),
    tailwind(),
  ],

  output: "static",
});
