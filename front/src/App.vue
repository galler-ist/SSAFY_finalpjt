<template>
  <nav class="navbar navbar-expand-lg bg-body-lg custom-navbar font">
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
          <RouterLink class="nav-link" :to="{ name: 'ArticleView' }">Articles</RouterLink>
        </div>
        <div class="navbar-nav ms-auto">
          <RouterLink class="nav-link" v-if="!isLogin" :to="{ name: 'SignUpView' }">Sign In</RouterLink>
          <RouterLink class="nav-link" v-if="!isLogin" :to="{ name: 'LogInView' }">Log In</RouterLink>
          <input class="nav-link btn input-link" v-else @click="logOut" :to="{ name: 'LogInView' }" value="Log Out">
        </div>
      </div>
    </div>
  </nav>
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
.font-size {
  font-size: 20px;
}
.navbar {
  padding: 1% 5%;
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  background-color: rgb(75, 75, 75, 0);/* 기본 상태에서 투명 */
  z-index: 1; /* 다른 요소들 위에 표시 */

  transition: background-color 0.5s ease, color 0.5s ease; /* 배경색과 글자색 변환 애니메이션 */
}

.navbar:hover {
  width: 100%;
  background-color: rgba(234, 234, 234, 0.3); /* 마우스 올렸을 때 흰색 */

}

.navbar .nav-link,
.navbar .navbar-brand {
  color: rgb(255, 255, 255); /* 기본 글자색 흰색 */
  transition: color 0.3s ease; /* 글자색 변환 애니메이션 */
}

.navbar:hover .nav-link,
.navbar:hover .navbar-brand {
  color: black; /* 마우스 올렸을 때 글자색 검정색 */
}

.navbar .nav-link.btn {
  border: none;
  background: none;
  cursor: pointer;
}
.footerstyle {
border-top: 1px solid rgb(229, 229, 229);
margin-top: 3rem;
padding: 3rem;
background-color: rgb(246, 246, 246);
text-align: center;
bottom: 0%
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