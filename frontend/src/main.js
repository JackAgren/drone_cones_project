import { createApp } from 'vue'
import {createRouter, createWebHistory} from 'vue-router'

import Homepage from "@/components/pages/Homepage.vue"
import Dashboard from "@/components/pages/Dashboard.vue"

import Registration from "@/components/pages/registration/Registration.vue"

import Login from "@/components/pages/Login.vue"

import ManageInventory from "@/components/pages/admin/ManageInventory.vue"
import ManageInventoryRestock from "@/components/pages/admin/ManageInventoryRestock.vue"
import ManageLeasePayments from "@/components/pages/admin/ManageLeasePayments.vue"
import ManageLeasePaymentsPayLease from "@/components/pages/admin/ManageLeasePaymentsPayLease.vue"
import ManageMenu from "@/components/pages/admin/ManageMenu.vue"
import ManageMenuEdit from "@/components/pages/admin/ManageMenuEdit.vue"
import ManageMenuAdd from "@/components/pages/admin/ManageMenuAdd.vue"
import ManageMenuRemove from "@/components/pages/admin/ManageMenuRemove.vue"
import ManageAccounts from "@/components/pages/admin/ManageAccounts.vue"
import ManageAccountsEdit from "@/components/pages/admin/ManageAccountsEdit.vue"
import FinancialRecords from "@/components/pages/admin/FinancialRecords.vue"

import DroneRegistration from "@/components/pages/drone_owner/DroneRegistration.vue"
import DroneActivity from "@/components/pages/drone_owner/DroneActivity.vue"
import DroneEarnings from "@/components/pages/drone_owner/DroneEarnings.vue"
import NewDrone from "@/components/pages/drone_owner/NewDrone.vue"

import OrderHistory from "@/components/pages/customer/OrderHistory.vue";
import Menu from "@/components/pages/customer/Menu.vue";
import CheckOut from "@/components/pages/customer/CheckOut.vue";
import OrderArrived from "@/components/pages/customer/OrderArrived.vue";
import TrackOrder from "@/components/pages/customer/TrackOrder.vue";

import './assets/style.css'

import App from './App.vue'

const router = createRouter({
    history: createWebHistory(),
    routes:[
        { path: '/', component: Homepage},
        { path: '/dashboard', component: Dashboard},
        { path: '/register', component: Registration},
        { path: '/login', component: Login},

        { path: '/admin/manageInventory', component: ManageInventory},
        { path: '/admin/manageInventory/restock/:description', component: ManageInventoryRestock},
        { path: '/admin/manageLeasePayments', component: ManageLeasePayments},
        { path: '/admin/manageLeasePayments/payLease', component: ManageLeasePaymentsPayLease},
        { path: '/admin/manageMenu', component: ManageMenu},
        { path: '/admin/manageMenu/edit/:description', component: ManageMenuEdit},
        { path: '/admin/manageMenu/remove/:description', component: ManageMenuRemove},
        { path: '/admin/manageMenu/add', component: ManageMenuAdd},
        { path: '/admin/manageAccounts', component: ManageAccounts},
        { path: '/admin/manageAccounts/edit', component: ManageAccountsEdit},
        { path: '/admin/financialRecords', component: FinancialRecords},

        { path: '/customer/history', component: OrderHistory},
        { path: '/customer/menu', component: Menu},
        { path: '/customer/checkout', component: CheckOut},
        { path: '/customer/track-order', component: TrackOrder},
        { path: '/customer/arrived', component: OrderArrived},

        { path: '/drone/registration', component: DroneRegistration},
        { path: '/drone/registration/new', component: NewDrone},
        { path: '/drone/activity', component: DroneActivity},
        { path: '/drone/earnings', component: DroneEarnings},
    ]
});

const app = createApp(App)
app.use(router)
app.mount('#app')
