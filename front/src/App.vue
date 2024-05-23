<template>
  <!-- <nav class="navbar navbar-expand-lg bg-body-lg custom-navbar my-nav">
    <div class="container-fluid">
      <RouterLink class="navbar-brand" style="color: black" :to="{ name: 'HomeView' }">GSC</RouterLink>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav me-auto font-size">
          <RouterLink class="nav-link" :to="{ name: 'BankView' }">Bank</RouterLink>
          <RouterLink class="nav-link" :to="{ name: 'ExchangeView' }">Exchange</RouterLink>
          <RouterLink class="nav-link" :to="{ name: 'DepositList' }">Finance</RouterLink>
          <RouterLink class="nav-link" :to="{ name: 'PortfolioView' }">Portfolio</RouterLink>
          <RouterLink class="nav-link" :to="{ name: 'ArticleView' }">Articles</RouterLink>
        </div>
        <div class="navbar-nav">
          <RouterLink class="nav-link" v-if="!isLogin" :to="{ name: 'SignUpView' }">Sign In</RouterLink>
          <RouterLink class="nav-link" v-if="!isLogin" :to="{ name: 'LogInView' }">Log In</RouterLink>
          <input class="nav-link btn input-link" v-else @click="logOut" :to="{ name: 'LogInView' }" value="Log Out">
        </div>
      </div>
    </div>
  </nav> -->

  <div>
    <div class="nav1">
      <RouterLink style="color: black" :to="{ name: 'HomeView' }"><img class="logo-img" src="/assets/Logo.png" alt="GSC"></RouterLink>
      <div class="nav2">
        <RouterLink class="cate-form" :to="{ name: 'BankView' }">지도</RouterLink>
        <RouterLink class="cate-form" :to="{ name: 'ExchangeView' }">환율</RouterLink>
        <RouterLink class="cate-form" :to="{ name: 'DepositList' }">예적금</RouterLink>
        <RouterLink class="cate-form" :to="{ name: 'ArticleView' }">게시판</RouterLink>
      </div>
      <div class="login-form d-flex">
        <!-- <p><RouterLink :to="{ name: 'Profile' }">님 환영합니다.</RouterLink></p> -->
        <button class="btn login-text w-10" v-if="!isLogin" :to="{ name: 'SignUpView' }" value="Sign In">Sign In</button>
        <button class="btn login-text w-10" v-if="!isLogin" :to="{ name: 'LogInView' }" value="Log In">Log In</button>
        <input class="btn login-form" v-else @click="logOut" :to="{ name: 'LogInView' }" value="Log Out">
      </div>
    </div>
  </div>

  

  <RouterView />
  <footer class="footerstyle">
    <div class="foot">
      <div class="seung">
        <p>Back developer</p>
        <small>name&nbsp;&nbsp;: Baek seungwoo</small>
        <small>e-mail&nbsp;: swghj@naver.com</small>
      </div>
      <div class="nong">
        <p>Front developer</p>
        <small>name&nbsp;&nbsp;: Kim geunwook</small>
        <small>e-mail&nbsp;: nonggeun0827@naver.com</small>
      </div>
      <div class="icons">
        <a href="https://www.instagram.com/hellossafy/">
          <img class="insta-icon" src="/assets/instagram_icon.png" alt="...">
        </a>
        <a href="https://github.com/galler-ist/SSAFY_finalpjt">
          <img class="github-icon" src="/assets/github2_icon.png" alt="...">
        </a>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { computed } from 'vue'
import { useCounterStore } from '@/stores/counter.js' 
import './style/style.css'

const counterStore = useCounterStore()
const isLogin = computed(() => counterStore.isLogin)
const logOut = () => {
  counterStore.logOut()
}
</script>

<style scoped>
.nav1 {
  position: fixed;
  display: flex;
  flex-direction: row;
  align-items: center;
  background-color: white;
  width: 100%;
  height: 4rem;
}
.nav2 {
  display: flex;
  flex: row;
  align-items: center;
}
.logo-form {
  font-size: 30px;
  text-decoration: none;
  color: black;
  margin: 0px 30px;
}
.cate-form {
  font-size: 20px;
  text-decoration: none;
  color: black;
  margin: 0px 32px;
}
.login-form {
  margin-left: auto;
  font: 15px;
  text-decoration: none;
  display: flex;
  /* align-items: flex-end; */
  color: black;
  /* padding-left: 100px; */
}
.login-text {
  margin-right: 20px;
}
.logo-img {
    width: 8rem;
    padding-top: 20px;
  }





.my-nav {
  position: fixed
}

.footerstyle {
border-top: 1px solid rgb(229, 229, 229);
padding: 3rem;
background-color: rgb(246, 246, 246);
text-align: center;
bottom: 0;
}
.insta-icon {
  width: 30px;
  height: 30px;
  margin-top: 10px;
}
.github-icon {
  width: 30px;
  height: 30px;
  margin-top: 10px;
}
.foot {
  color: gray;
  display: flex;
  flex-direction: row;
  width: 65%;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
  padding: 0;
}
.icons {
  display: flex;
  flex-direction: column;
  width: 10%;
}
.seung {
  width: 45%;
  display: flex;
  flex-direction: column;
  text-align: left;
}
.nong {
  width: 45%;
  display: flex;
  flex-direction: column;
  text-align: left;
}
</style>

<style>
* {
  font-family: 'NPSfont_regula';
}
</style>