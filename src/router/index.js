import { createRouter, createWebHistory } from 'vue-router';
import QueryView from '../views/QueryView.vue';
import AnalysisView from '../views/AnalysisView.vue';

const routes = [
  {
    path: '/',
    redirect: '/query'
  },
  {
    path: '/query',
    name: 'Query',
    component: QueryView
  },
  {
    path: '/analysis',
    name: 'Analysis',
    component: AnalysisView
  }
];

const router = createRouter({
  history: createWebHistory(), // import.meta.env.BASE_URL
  routes
});

export default router;  