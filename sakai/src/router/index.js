import { createRouter, createWebHashHistory } from 'vue-router';
import AppLayout from '@/layout/AppLayout.vue';

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        {
            path: '/',
            component: AppLayout,
            children: [
                {
                    path: '/',
                    // name: 'dashboard',
                    // component: () => import('@/views/Dashboard.vue')
                    name: 'HomePage',
                    component: () => import('@/views/GymPages/FrontDesk/FieldsBooking.vue')
                },
                {
                    path: '/uikit/formlayout',
                    name: 'formlayout',
                    component: () => import('@/views/uikit/FormLayout.vue')
                },
                {
                    path: '/FieldsBooking',
                    name: 'FieldsBooking',
                    component: () => import('@/views/GymPages/FrontDesk/FieldsBooking.vue')
                },

                {
                    path: '/GoodsSales',
                    name: 'GoodsSales',
                    component: () => import('@/views/GymPages/FrontDesk/GoodsSales.vue')
                },

                {
                    path: '/CardsSales',
                    name: 'CardsSales',
                    component: () => import('@/views/GymPages/FrontDesk/CardsSales.vue')
                },
                {
                    path: '/TicketsSales',
                    name: 'TicketsSales',
                    component: () => import('@/views/GymPages/FrontDesk/TicketsSales.vue')
                },
                {
                    path: '/FieldsVacancy',
                    name: 'FieldsVacancy',
                    component: () => import('@/views/GymPages/FrontDesk/FieldsVacancy.vue')
                },
                {
                    path: '/WriteOffs',
                    name: 'WriteOffs',
                    component: () => import('@/views/GymPages/FrontDesk/WriteOffs.vue')
                },
                {
                    path: '/CardRecords',
                    name: 'CardRecords',
                    component: () => import('@/views/GymPages/FrontDesk/CardRecords.vue')
                },
                {
                    path: '/MembershipClass',
                    name: 'MembershipClass',
                    component: () => import('@/views/GymPages/Membership/MembershipClass.vue')
                },
                {
                    path: '/MembershipLevel',
                    name: 'MembershipLevel',
                    component: () => import('@/views/GymPages/Membership/MembershipLevel.vue')
                },
                {
                    path: '/MemberList',
                    name: 'MemberList',
                    component: () => import('@/views/GymPages/Membership/MemberList.vue')
                },
                {
                    path: '/MemberInfo',
                    name: 'MemberInfo',
                    component: () => import('@/views/GymPages/Membership/MemberInfo.vue')
                },
                {
                    path: '/GoodsList',
                    name: 'GoodsList',
                    component: () => import('@/views/GymPages/GoodsManagement/GoodsList.vue')
                },
                {
                    path: '/GoodsTypes',
                    name: 'GoodsManagement',
                    component: () => import('@/views/GymPages/GoodsManagement/GoodsTypes.vue')
                },
                {
                    path: '/FieldsList',
                    name: 'FieldsList',
                    component: () => import('@/views/GymPages/FieldsManagement/FieldsList.vue')
                },
                {
                    path: '/BillingRules',
                    name: 'BillingRules',
                    component: () => import('@/views/GymPages/FieldsManagement/BillingRules.vue')
                },
                {
                    path: '/DeviceManagement',
                    name: 'DeviceManagement',
                    component: () => import('@/views/GymPages/FieldsManagement/DeviceManagement.vue')
                },
                {
                    path: '/DocumentsManagement',
                    name: 'DocumentsManagement',
                    component: () => import('@/views/GymPages/DocumentsManagement/DocumentsManagement.vue')
                },
                {
                    path: '/SmartDevices',
                    name: 'SmartDevices',
                    component: () => import('@/views/GymPages/DeviceManagement/SmartDevices.vue')
                },
                {
                    path: '/DeviceMaintainance',
                    name: 'DeviceMaintainance',
                    component: () => import('@/views/GymPages/DeviceManagement/DeviceMaintainance.vue')
                },
                {
                    path: '/DeviceLog',
                    name: 'DeviceLog',
                    component: () => import('@/views/GymPages/DeviceManagement/DeviceLog.vue')
                },
                {
                    path: '/SmartLights',
                    name: 'SmartLights',
                    component: () => import('@/views/GymPages/DeviceManagement/SmartLights.vue')
                },
                {
                    path: '/InventoryList',
                    name: 'InventoryList',
                    component: () => import('@/views/GymPages/Inventory/InventoryList.vue')
                },
                {
                    path: '/Coupon',
                    name: 'Coupon',
                    component: () => import('@/views/GymPages/Coupon/Coupon.vue')
                },
                {
                    path: '/EventInfo',
                    name: 'EventInfo',
                    component: () => import('@/views/GymPages/EventManagement/EventInfo.vue')
                },       
                {
                    path: '/SessionManagement',
                    name: 'SessionManagement',
                    component: () => import('@/views/GymPages/EventManagement/SessionManagement.vue')
                }, 
                {
                    path: '/Seats',
                    name: 'Seats',
                    component: () => import('@/views/GymPages/EventManagement/Seats.vue')
                },   
                {
                    path: '/SeatsSales',
                    name: 'SeatsSales',
                    component: () => import('@/views/GymPages/EventManagement/SeatsSales.vue')
                },   
                {
                    path: '/Tickets',
                    name: 'Tickets',
                    component: () => import('@/views/GymPages/EventManagement/Tickets.vue')
                },                                                                                
                {
                    path: '/uikit/input',
                    name: 'input',
                    component: () => import('@/views/uikit/Input.vue')
                },
                {
                    path: '/uikit/floatlabel',
                    name: 'floatlabel',
                    component: () => import('@/views/uikit/FloatLabel.vue')
                },
                {
                    path: '/uikit/invalidstate',
                    name: 'invalidstate',
                    component: () => import('@/views/uikit/InvalidState.vue')
                },
                {
                    path: '/uikit/button',
                    name: 'button',
                    component: () => import('@/views/uikit/Button.vue')
                },
                {
                    path: '/uikit/table',
                    name: 'table',
                    component: () => import('@/views/uikit/Table.vue')
                },
                {
                    path: '/uikit/list',
                    name: 'list',
                    component: () => import('@/views/uikit/List.vue')
                },
                {
                    path: '/uikit/tree',
                    name: 'tree',
                    component: () => import('@/views/uikit/Tree.vue')
                },
                {
                    path: '/uikit/panel',
                    name: 'panel',
                    component: () => import('@/views/uikit/Panels.vue')
                },

                {
                    path: '/uikit/overlay',
                    name: 'overlay',
                    component: () => import('@/views/uikit/Overlay.vue')
                },
                {
                    path: '/uikit/media',
                    name: 'media',
                    component: () => import('@/views/uikit/Media.vue')
                },
                {
                    path: '/uikit/menu',
                    component: () => import('@/views/uikit/Menu.vue'),
                    children: [
                        {
                            path: '/uikit/menu',
                            component: () => import('@/views/uikit/menu/PersonalDemo.vue')
                        },
                        {
                            path: '/uikit/menu/seat',
                            component: () => import('@/views/uikit/menu/SeatDemo.vue')
                        },
                        {
                            path: '/uikit/menu/payment',
                            component: () => import('@/views/uikit/menu/PaymentDemo.vue')
                        },
                        {
                            path: '/uikit/menu/confirmation',
                            component: () => import('@/views/uikit/menu/ConfirmationDemo.vue')
                        }
                    ]
                },
                {
                    path: '/uikit/message',
                    name: 'message',
                    component: () => import('@/views/uikit/Messages.vue')
                },
                {
                    path: '/uikit/file',
                    name: 'file',
                    component: () => import('@/views/uikit/File.vue')
                },
                {
                    path: '/uikit/charts',
                    name: 'charts',
                    component: () => import('@/views/uikit/Chart.vue')
                },
                {
                    path: '/uikit/misc',
                    name: 'misc',
                    component: () => import('@/views/uikit/Misc.vue')
                },
                {
                    path: '/blocks',
                    name: 'blocks',
                    component: () => import('@/views/utilities/Blocks.vue')
                },
                {
                    path: '/utilities/icons',
                    name: 'icons',
                    component: () => import('@/views/utilities/Icons.vue')
                },
                {
                    path: '/pages/timeline',
                    name: 'timeline',
                    component: () => import('@/views/pages/Timeline.vue')
                },
                {
                    path: '/pages/empty',
                    name: 'empty',
                    component: () => import('@/views/pages/Empty.vue')
                },
                {
                    path: '/pages/crud',
                    name: 'crud',
                    component: () => import('@/views/pages/Crud.vue')
                },
                {
                    path: '/documentation',
                    name: 'documentation',
                    component: () => import('@/views/utilities/Documentation.vue')
                }
            ]
        },
        {
            path: '/landing',
            name: 'landing',
            component: () => import('@/views/pages/Landing.vue')
        },
        {
            path: '/pages/notfound',
            name: 'notfound',
            component: () => import('@/views/pages/NotFound.vue')
        },

        {
            path: '/auth/login',
            name: 'login',
            component: () => import('@/views/pages/auth/Login.vue')
        },
        {
            path: '/auth/access',
            name: 'accessDenied',
            component: () => import('@/views/pages/auth/Access.vue')
        },
        {
            path: '/auth/error',
            name: 'error',
            component: () => import('@/views/pages/auth/Error.vue')
        }
    ]
});

export default router;
