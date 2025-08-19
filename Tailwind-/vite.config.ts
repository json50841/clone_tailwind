import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { resolve } from "path";

export default defineConfig({
  plugins: [react()],
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, "./index.html"),
        admin: resolve(__dirname, "./public/Admin.html"),
      },
    },
  },
  server: {
    port: 5173, // 可以改成你想要的端口
    fs: {
      allow: ["."], // 允许访问项目根目录
    },
    // ✅ Vite 4+ 不用 historyApiFallback，默认支持 SPA fallback
  },
});
