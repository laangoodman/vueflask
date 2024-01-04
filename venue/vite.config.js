import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import { fileURLToPath, URL } from 'node:url';

export default defineConfig(() => {
    return {
        plugins: [vue()],
        resolve: {
            alias: {
                '@': fileURLToPath(new URL('./src', import.meta.url)),
            },
        },
        // Define global constants here 3
        define: {
            // 'process.env.API_URL': JSON.stringify('http://121.40.98.93:7002')            
            'process.env.API_URL': JSON.stringify('http://127.0.0.1:5000')            

        },
    };
});