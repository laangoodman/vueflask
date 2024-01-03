<script setup>
import { ref } from 'vue';

import AppMenuItem from './AppMenuItem.vue';

const model = ref([
    {
        label: ' ',
        items: [{
            label: '前台收银',
            icon: 'pi pi-fw pi-home',
            //to: '/', 
            //添加子级标题

            items: [
                // {label: '场地租用',icon: 'pi pi-fw pi-bookmark',to:'/uikit/formlayout'},
                {label: '场地租用',icon: 'pi pi-fw pi-bookmark',to:'/changdizuyong'},

                {label: '商品销售',icon: 'pi pi-fw pi-bookmark',to:'/shangpinxiaoshou'},
                {label: '次卡销售',icon: 'pi pi-fw pi-bookmark',to:'/cikaxiaoshou'},
                {label: '门票销售',icon: 'pi pi-fw pi-bookmark',to:'/menpiaoxiaoshou'},
                {label: '场地状态',icon: 'pi pi-fw pi-bookmark',to:'/changdizhuangtai'},
                {label: '快速核销',icon: 'pi pi-fw pi-bookmark',to:'/kuaisuhexiao'},
                {label: '会员扣次',icon: 'pi pi-fw pi-bookmark',to:'/huiyuankouci'},
            ]
        }]
    },
    {
        label: ' ',
        items: [{
            label: '会员管理',
            icon: 'pi pi-fw pi-home',
            //to: '/', 
            //添加子级标题

            items: [
                {label: '会员卡类别',icon: 'pi pi-fw pi-bookmark',to:'/huiyuankaleibie'},
                {label: '会员等级',icon: 'pi pi-fw pi-bookmark',to:'/huiyuandengji'},
                {label: '会员列表',icon: 'pi pi-fw pi-bookmark',to:'/huiyuanliebiao'},
                {label: '会员信息',icon: 'pi pi-fw pi-bookmark',to:'/huiyuanxinxi'},
            ]
        }]
    },
    {
        label: ' ',
        items: [{
            label: '商品管理',
            icon: 'pi pi-fw pi-home',
            //to: '/', 
            //添加子级标题

            items: [
                {label: '商品列表',icon: 'pi pi-fw pi-bookmark',to:'/shangpinliebiao'},
                {label: '商品类型',icon: 'pi pi-fw pi-bookmark',to:'/shangpinleixing'},
                
            ]
        }]
    },
    {
        label: ' ',
        items: [{
            label: '场地管理',
            icon: 'pi pi-fw pi-home',
            //to: '/', 
            //添加子级标题

            items: [
                {label: '场地列表',icon: 'pi pi-fw pi-bookmark',to:'/changdiliebiao'},
                {label: '计费规则',icon: 'pi pi-fw pi-bookmark',to:'/jifeiguize'},
                {label: '设备管理',icon: 'pi pi-fw pi-bookmark',to:'/shebeiguanli'}
            ]
        }]
    },
    {
        label: ' ',
        items: [{
            label: '单据管理',
            icon: 'pi pi-fw pi-home',
            //to: '/', 
            //添加子级标题

            items: [
                {label: '单据管理',icon: 'pi pi-fw pi-bookmark',to:'/danjuguanli'}
            ]
        }]
    },
    {
        label: ' ',
        items: [{
            label: '设备管理',
            icon: 'pi pi-fw pi-home',
            //to: '/', 
            //添加子级标题

            items: [
                {label: '智能设备',icon: 'pi pi-fw pi-bookmark',to:'/zhinengshebei'},
                {label: '设备运维',icon: 'pi pi-fw pi-bookmark',to:'/shebeiyunwei'},
                {label: '设备日志',icon: 'pi pi-fw pi-bookmark',to:'/shebeirizhi'},
                {label: '智能灯',icon: 'pi pi-fw pi-bookmark',to:'/zhinengdeng'},
            ]
        }]
    },
    {
        label: ' ',
        items: [{
            label: '库存管理',
            icon: 'pi pi-fw pi-home',
            //to: '/', 
            //添加子级标题

            items: [
                {label: '库存列表',icon: 'pi pi-fw pi-bookmark',to:'/kucunliebiao'}
            ]
        }]
    },
    {
        label: ' ',
        items: [{
            label: '优惠券',
            icon: 'pi pi-fw pi-home',
            //to: '/', 
            //添加子级标题

            items: [
                {label: '优惠券',icon: 'pi pi-fw pi-bookmark',to:'/youhuiquan'}
            ]
        }]
    },
    {
        label: ' ',
        items: [{
            label: '演出/赛事管理',
            icon: 'pi pi-fw pi-home',
            //to: '/', 
            //添加子级标题

            items: [
                {label: '演出/赛事信息',icon: 'pi pi-fw pi-bookmark',to:'/saishixinxi'},
                {label: '场次管理',icon: 'pi pi-fw pi-bookmark',to:'/changciguanli'},
                {label: '座位管理',icon: 'pi pi-fw pi-bookmark',to:'/zuoweiguanli'},
                {label: '座位销售管理',icon: 'pi pi-fw pi-bookmark',to:'/zuoweixiaoshouguanli'},
                {label: '票档管理',icon: 'pi pi-fw pi-bookmark',to:'/piaodangguanli'}
            ]
        }]
    },
    {
        label: ' ',
        items: [{
            label: '工作台',
            icon: 'pi pi-fw pi-home',
            //to: '/', 
            //添加子级标题

            items: [
                {label: '工作台',icon: 'pi pi-fw pi-bookmark',to:'/uikit/formlayout'}
            ]
        }]
    },
    {
        label: ' ',
        items: [{
            label: '资源管理',
            icon: 'pi pi-fw pi-home',
            //to: '/', 
            //添加子级标题

            items: [
                {label: '对象储存',icon: 'pi pi-fw pi-bookmark',to:'/uikit/formlayout'},
                {label: '短信配置',icon: 'pi pi-fw pi-bookmark',to:'/uikit/formlayout'}
            ]
        }]
    },
    {
        label: ' ',
        items: [{
            label: '基础配置',
            icon: 'pi pi-fw pi-home',
            //to: '/', 
            //添加子级标题

            items: [
                {label: '行政区划',icon: 'pi pi-fw pi-bookmark',to:'/uikit/formlayout'},
                {label: '通用配置',icon: 'pi pi-fw pi-bookmark',to:'/'},
                {label: '动态表单',icon: 'pi pi-fw pi-bookmark'},
                {label: '设备配置',icon: 'pi pi-fw pi-bookmark'}
            ]
        }]
    },
    {
        label: ' ',
        items: [{
            label: '权限管理',
            icon: 'pi pi-fw pi-home',
            //to: '/', 
            //添加子级标题

            items: [
                {label: '角色管理',icon: 'pi pi-fw pi-bookmark',to:'/uikit/formlayout'},
                {label: '数据权限',icon: 'pi pi-fw pi-bookmark',to:'/'},
                {label: '接口权限',icon: 'pi pi-fw pi-bookmark'}
            ]
        }]
    },
    {
        label: ' ',
        items: [{
            label: '系统管理',
            icon: 'pi pi-fw pi-home',
            //to: '/', 
            //添加子级标题

            items: [
                {label: '用户管理',icon: 'pi pi-fw pi-bookmark',to:'/uikit/formlayout'},
                {label: '机构管理',icon: 'pi pi-fw pi-bookmark',to:'/'},
                {label: '岗位管理',icon: 'pi pi-fw pi-bookmark'},
                {label: '系统字典',icon: 'pi pi-fw pi-bookmark'},
                {label: '业务字典',icon: 'pi pi-fw pi-bookmark'},
                {label: '菜单管理',icon: 'pi pi-fw pi-bookmark'},
                {label: '顶部菜单',icon: 'pi pi-fw pi-bookmark'},
                {label: '参数管理',icon: 'pi pi-fw pi-bookmark'},
                {label: '日志管理',icon: 'pi pi-fw pi-bookmark',items:[
                    {label: '通知日志',icon: 'pi pi-fw pi-bookmark',to:'/uikit/formlayout'},
                    {label: '接口日志',icon: 'pi pi-fw pi-bookmark',to:'/'},
                    {label: '错误日志',icon: 'pi pi-fw pi-bookmark'},         
                ]},
                {label: '租户管理',icon: 'pi pi-fw pi-bookmark'},
                {label: '应用管理',icon: 'pi pi-fw pi-bookmark'},
                {label: '文件管理',icon: 'pi pi-fw pi-bookmark'}
            ]
        }]
    },
    // {
    //     //label: 'UI Components',
    //     items: [
    //         { label: '会员管理', icon: 'pi pi-fw pi-id-card', to: '/uikit/formlayout' },
    //         { label: '商品管理', icon: 'pi pi-fw pi-check-square', to: '/uikit/input' },
    //         { label: '场地管理', icon: 'pi pi-fw pi-bookmark', to: '/uikit/floatlabel' },
    //         { label: '单据管理', icon: 'pi pi-fw pi-exclamation-circle', to: '/uikit/invalidstate' },
    //         { label: '设备管理', icon: 'pi pi-fw pi-mobile', to: '/uikit/button', class: 'rotated-icon' },
    //         { label: '库存管理', icon: 'pi pi-fw pi-table', to: '/uikit/table' },
    //         { label: '优惠券', icon: 'pi pi-fw pi-list', to: '/uikit/list' },
    //         { label: '演出/赛事管理', icon: 'pi pi-fw pi-share-alt', to: '/uikit/tree' },
    //         { label: '工作台', icon: 'pi pi-fw pi-tablet', to: '/uikit/panel' },
    //         { label: '资源管理', icon: 'pi pi-fw pi-clone', to: '/uikit/overlay' },
    //         { label: '基础配置', icon: 'pi pi-fw pi-image', to: '/uikit/media' },
    //         { label: '权限管理', icon: 'pi pi-fw pi-bars', to: '/uikit/menu', preventExact: true },
    //         { label: '系统管理', icon: 'pi pi-fw pi-comment', to: '/uikit/message' }
  
    //     ]
    // },




  
]);


</script>

<!-- <template>
    <ul class="layout-menu">
        <template v-for="(item, i) in model" :key="item">
            <app-menu-item v-if="!item.separator" :item="item" :index="i"></app-menu-item>
            <li v-if="item.separator" class="menu-separator"></li>
        </template>
        <li>
            <a href="https://www.primefaces.org/primeblocks-vue/#/" target="_blank">
                <img src="/layout/images/banner-primeblocks.png" alt="Prime Blocks" class="w-full mt-3" />
            </a>
        </li>
    </ul>
</template> -->
<!-- 
<template>
    <ul class="layout-menu">
        <template v-for="(item, i) in model" :key="item">
            <app-menu-item v-if="!item.separator" :item="item" :index="i"></app-menu-item>
            <li v-if="item.separator" class="menu-separator"></li>
        </template>
   
    </ul>
</template> -->
<template>
    <ul class="layout-menu">
        <template v-for="(item, i) in model" :key="item">
            <app-menu-item v-if="!item.separator" :item="item" :index="i"></app-menu-item>
            <li v-if="item.separator" class="menu-separator"></li>
        </template>
    </ul>
</template>
<!-- <template>
    <ul class="layout-menu">
        <template v-for="(item, i) in model" :key="i">
            <li v-if="!item.separator">
                <a @click="item.items && toggleExpand(item)">
                    {{ item.label }}
                    <span class="pi" :class="{
                        'pi-chevron-down': item.items && !item.expanded,
                        'pi-chevron-up': item.items && item.expanded
                    }"></span>
                </a>
                <ul v-if="item.items && item.expanded">
                    <li v-for="(subItem, j) in item.items" :key="j">
                        <a :href="subItem.to">{{ subItem.label }}</a>
                    </li>
                </ul>
            </li>
            <li v-if="item.separator" class="menu-separator"></li>
        </template>
        其他内容
    </ul>
</template> -->

<style lang="scss" scoped></style>
