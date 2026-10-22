import { defineConfig } from 'vite';
import angular from '@vitejs/plugin-angular';
import path from 'path';

export default defineConfig({
  plugins: [angular()],
  root: path.resolve(__dirname),
  build: {
    outDir: 'dist'
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:4000',
        changeOrigin: true
      }
    }
  }
});
