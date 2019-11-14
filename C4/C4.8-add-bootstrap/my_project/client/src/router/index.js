import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import FetchTest from '../components/FetchTest.vue';
import TaskList from '../components/Tasks.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/fetch',
    name: 'FetchTest',
    component: FetchTest,
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/tasks',
    name: 'TaskList',
    component: TaskList,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
