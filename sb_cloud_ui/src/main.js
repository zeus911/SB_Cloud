// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import './theme/index.css'
import './assets/css/font-awesome.min.css'
import './assets/css/style.css'
import $ from 'jquery'
import {setCookie, getCookie, delCookie} from "./assets/utils/cookies";
import Config from './config/'
import Api from './api/'
import Function from './utils/'
import hookAjax from 'ajax-hook'

Vue.use(ElementUI);
Vue.prototype.$Api = Api
Vue.prototype.$Config = Config
Vue.prototype.$Func = Function
Vue.config.productionTip = false;
Vue.prototype.$cookieStore = {
  setCookie,
  getCookie,
  delCookie
};
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireAuth)) { // 判断该路由是否需要登录权限
    console.log('需要登录');
    if (getCookie('user_token')) { // 判断当前的token是否存在 ； 登录存入的token
      next();
    }
    else {
      next({
        path: '/',
        query: {redirect: to.fullPath} // 将跳转的路由path作为参数，登录成功后跳转到该路由
      })
    }
  }
  else {
    next();
  }
});
// hookAjax({
//   onreadystatechange: function (xhr) {
//
//   },
//   onload: function (xhr) {
//
//   },
//   open: function (arg,xhr) {
//
//   }
// })
$.ajaxSetup({
  contentType: "application/x-www-form-urlencoded;charset=utf-8",
  complete: function (XMLHttpRequest, textStatus) {
    //通过XMLHttpRequest取得响应头，sessionstatus，
    var xhr = XMLHttpRequest;
    console.log(xhr)
    console.log(textStatus)
  }
});
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
});