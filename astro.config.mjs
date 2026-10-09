// @ts-check
import { defineConfig } from "astro/config";
import react from "@astrojs/react";

export default defineConfig({
  site: "https://parano-ai.com",
  integrations: [react()],
  trailingSlash: "ignore",
});
