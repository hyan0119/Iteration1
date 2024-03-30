import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

const app = createApp(App);

// 设置 productionTip
app.config.productionTip = false;

app.use(router).mount('#app');
