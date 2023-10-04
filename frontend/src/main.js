import { createApp } from 'vue'
import {createRouter, createWebHistory} from 'vue-router'

import HelloWorldComponent from "@/components/HelloWorld.vue";
import SecondSampleComponent from "@/components/SecondSample.vue";

import './assets/style.css'

import App from './App.vue'

const router = createRouter({
    history: createWebHistory(),
    routes:[
        { path: '/', component: HelloWorldComponent},
        { path: '/second-page', component: SecondSampleComponent},
        //{ path: '/:pathMatch(.*)*', component: NotFoundComponent},
    ]
});

const app = createApp(App)
app.use(router)
app.mount('#app')
