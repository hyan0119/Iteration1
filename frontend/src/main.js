import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import 'aos/dist/aos.css';
import AOS from 'aos';
import * as ElementPlusIconsVue from "@element-plus/icons-vue";

const app = createApp(App);
app.use(ElementPlus);
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component);
}
app.config.globalProperties.$aos = AOS;
// 设置 productionTip
app.config.productionTip = false;

app.use(router).mount("#app");
AOS.init();