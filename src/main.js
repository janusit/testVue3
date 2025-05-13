import { createApp } from 'vue'
import App from './App.vue'
// import router from './router';
// import axios from 'axios';

// import LifecycleHooks1 from './components/LifecycleHooks1.vue'
import { registerGlobalComponents } from './registerGlobalComponents'

// 配置axios基础URL
// axios.defaults.baseURL = 'http://localhost:5000';

const app = createApp(App)

// 注册全局组件
// app.component('LifecycleHooks1', LifecycleHooks1)
registerGlobalComponents(app)
// import GlobalHeader from './components/GlobalHeader.vue';
// app.component('GlobalHeader', GlobalHeader);

// createApp(App).mount('#app')
// app.use(router);
app.mount('#app'); 

// app.use(router).mount('#app'); // 确保挂载到 #app
