// registerGlobalComponents.js

import LifecycleHooks1 from './components/LifecycleHooks1.vue'
import LifecycleHooks2 from './components/LifecycleHooks2.vue'
import LifecycleHooks3 from './components/LifecycleHooks3.vue'
// import GlobalHeader from './components/GlobalHeader.vue';

export function registerGlobalComponents(app) {
  app.component('LifecycleHooks1', LifecycleHooks1)
  app.component('LifecycleHooks2', LifecycleHooks2)
  app.component('LifecycleHooks3', LifecycleHooks3)
  // app.component('GlobalHeader', GlobalHeader);
}
