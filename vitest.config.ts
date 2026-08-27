import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    include: ["mundo_*/**/*.test.ts", "logica/**/*.test.ts"],
    environment: "node",
    globals: true,
  },
});