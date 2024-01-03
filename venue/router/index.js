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
                    component: () => import('@/views/GymPages/QianTaiShouYin/ChangDiZuYong.vue')
                },
                {
                    path: '/uikit/formlayout',
                    name: 'formlayout',
                    component: () => import('@/views/uikit/FormLayout.vue')
                },
                {
                    path: '/changdizuyong',
                    name: 'changdizuyong',
                    component: () => import('@/views/GymPages/QianTaiShouYin/ChangDiZuYong.vue')
                },

                {
                    path: '/shangpinxiaoshou',
                    name: 'shangpinxiaoshou',
                    component: () => import('@/views/GymPages/QianTaiShouYin/ShangPinXiaoShou.vue')
                },

                {
                    path: '/cikaxiaoshou',
                    name: 'cikaxiaoshou',
                    component: () => import('@/views/GymPages/QianTaiShouYin/CiKaXiaoShou.vue')
                },
                {
                    path: '/menpiaoxiaoshou',
                    name: 'menpiaoxiaoshou',
                    component: () => import('@/views/GymPages/QianTaiShouYin/MenPiaoXiaoShou.vue')
                },
                {
                    path: '/changdizhuangtai',
                    name: 'changdizhuangtai',
                    component: () => import('@/views/GymPages/QianTaiShouYin/ChangDiZhuangTai.vue')
                },
                {
                    path: '/kuaisuhexiao',
                    name: 'kuaisuhexiao',
                    component: () => import('@/views/GymPages/QianTaiShouYin/KuaiSuHeXiao.vue')
                },
                {
                    path: '/huiyuankouci',
                    name: 'huiyuankouci',
                    component: () => import('@/views/GymPages/QianTaiShouYin/HuiYuanKouCi.vue')
                },
                {
                    path: '/huiyuankaleibie',
                    name: 'huiyuankaleibie',
                    component: () => import('@/views/GymPages/HuiYuanGuanLi/HuiYuanKaLeiBie.vue')
                },
                {
                    path: '/huiyuandengji',
                    name: 'huiyuandengji',
                    component: () => import('@/views/GymPages/HuiYuanGuanLi/HuiYuanDengJi.vue')
                },
                {
                    path: '/huiyuanliebiao',
                    name: 'huiyuanliebiao',
                    component: () => import('@/views/GymPages/HuiYuanGuanLi/HuiYuanLieBiao.vue')
                },
                {
                    path: '/huiyuanxinxi',
                    name: 'huiyuanxinxi',
                    component: () => import('@/views/GymPages/HuiYuanGuanLi/HuiYuanXinXi.vue')
                },
                {
                    path: '/shangpinliebiao',
                    name: 'shangpinliebiao',
                    component: () => import('@/views/GymPages/ShangPinGuanLi/ShangPinLieBiao.vue')
                },
                {
                    path: '/shangpinleixing',
                    name: 'shangpinleixing',
                    component: () => import('@/views/GymPages/ShangPinGuanLi/ShangPinLeiXing.vue')
                },
                {
                    path: '/changdiliebiao',
                    name: 'changdiliebiao',
                    component: () => import('@/views/GymPages/ChangDiGuanLi/ChangDiLieBiao.vue')
                },
                {
                    path: '/jifeiguize',
                    name: 'jifeiguize',
                    component: () => import('@/views/GymPages/ChangDiGuanLi/JiFeiGuiZe.vue')
                },
                {
                    path: '/shebeiguanli',
                    name: 'shebeiguanli',
                    component: () => import('@/views/GymPages/ChangDiGuanLi/SheBeiGuanLi.vue')
                },
                {
                    path: '/danjuguanli',
                    name: 'danjuguanli',
                    component: () => import('@/views/GymPages/DanJuGuanLi/DanJuGuanLi.vue')
                },
                {
                    path: '/zhinengshebei',
                    name: 'zhinengshebei',
                    component: () => import('@/views/GymPages/SheBeiGuanLi/ZhiNengSheBei.vue')
                },
                {
                    path: '/shebeiyunwei',
                    name: 'shebeiyunwei',
                    component: () => import('@/views/GymPages/SheBeiGuanLi/SheBeiYunWei.vue')
                },
                {
                    path: '/shebeirizhi',
                    name: 'shebeirizhi',
                    component: () => import('@/views/GymPages/SheBeiGuanLi/SheBeiRiZhi.vue')
                },
                {
                    path: '/zhinengdeng',
                    name: 'zhinengdeng',
                    component: () => import('@/views/GymPages/SheBeiGuanLi/ZhiNengDeng.vue')
                },
                {
                    path: '/kucunliebiao',
                    name: 'kucunliebiao',
                    component: () => import('@/views/GymPages/KuCunGuanLi/KuCunLieBiao.vue')
                },
                {
                    path: '/youhuiquan',
                    name: 'youhuiquan',
                    component: () => import('@/views/GymPages/YouHuiQuan/YouHuiQuan.vue')
                },
                {
                    path: '/saishixinxi',
                    name: 'saishixinxi',
                    component: () => import('@/views/GymPages/SaiShiGuanLi/SaiShiXinXi.vue')
                },       
                {
                    path: '/changciguanli',
                    name: 'changciguanli',
                    component: () => import('@/views/GymPages/SaiShiGuanLi/ChangCiGuanLi.vue')
                }, 
                {
                    path: '/zuoweiguanli',
                    name: 'zuoweiguanli',
                    component: () => import('@/views/GymPages/SaiShiGuanLi/ZuoWeiGuanLi.vue')
                },   
                {
                    path: '/zuoweixiaoshouguanli',
                    name: 'zuoweixiaoshouguanli',
                    component: () => import('@/views/GymPages/SaiShiGuanLi/ZuoWeiXiaoShouGuanLi.vue')
                },   
                {
                    path: '/piaodangguanli',
                    name: 'piaodangguanli',
                    component: () => import('@/views/GymPages/SaiShiGuanLi/PiaoDangGuanLi.vue')
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
