// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './components/App'
import Content from './components/Content'
import Mask from './components/Mask'
import Optim from './components/Optim'
import Cut from './components/Cut'
import SR from './components/SR'
import Home from './components/Home'
import NSTjt from './components/NSTjt'
import NSTpt from './components/NSTpt'
// import Sidebar from './components/Sidebar'
import VueRouter from 'vue-router'
import axios from 'axios'
import Element from 'element-ui'
import echarts from "echarts";

import Photoshop from 'vue-color'

Vue.prototype.$echarts = echarts;
import '../node_modules/element-ui/lib/theme-chalk/index.css'
import '../src/assets/style.css'
import './theme/index.css'

Vue.use(Element)
Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.prototype.$http = axios

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
    return originalPush.call(this, location).catch(err => err)
}

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home,
    },
    {
        path: '/match',
        name: 'match',
        component: Content,
    },
    {
        path: '/mask',
        name: 'mask',
        component: Mask,
    },
    {
        path: '/nstjt',
        name: 'nstjt',
        component: NSTjt,
    },
    {
        path: '/nstpt',
        name: 'nstpt',
        component: NSTpt,
    },
    {
        path: '/post',
        name: 'post',
        component: Optim,
    },
    {
        path: '/cut',
        name: 'cut',
        component: Cut,
    },
    {
        path: '/sr',
        name: 'sr',
        component: SR,
    }
]

const router = new VueRouter({
    // routes: [
    //     {path: "/App", component: App, meta: {title: "rua"},},
    // ],
    // mode: "history",
    // base: process.env.BASE_URL,
    routes
})

// // 全局注册组件
Vue.component("App", App);
// Vue.component("Sidebar", Sidebar);

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    render: h => h(App),
    components: {
        'photoshop-picker': Photoshop
      }
})
