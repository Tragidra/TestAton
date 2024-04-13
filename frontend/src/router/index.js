import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/Login.vue';
import Table from "../views/Table.vue";

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/table',
    name: 'Table',
    component: Table,
    // props: route => ({ clients: route.params.clients })
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
