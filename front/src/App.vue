<template>
  <nav class="navbar navbar-expand-lg bg-body-lg custom-navbar font">
    <div class="container-fluid">
      <RouterLink class="navbar-brand" :to="{ name: 'HomeView' }">Home</RouterLink>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav me-auto font-size">
          <RouterLink class="nav-link font" :to="{ name: 'ArticleView' }">Articles</RouterLink>
          <RouterLink class="nav-link" :to="{ name: 'BankView' }">Bank</RouterLink>
          <RouterLink class="nav-link" :to="{ name: 'ExchangeView' }">Exchange</RouterLink>
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
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { computed } from 'vue'
import { useCounterStore } from '@/stores/counter.js' 

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
  background-color: transparent; /* 기본 상태에서 투명 */
  z-index: 1; /* 다른 요소들 위에 표시 */
  transition: background-color 0.3s ease, color 0.3s ease; /* 배경색과 글자색 변환 애니메이션 */
}

.navbar:hover {
  width: 100%;
  background-color: white; /* 마우스 올렸을 때 흰색 */
}

.navbar .nav-link,
.navbar .navbar-brand {
  color: white; /* 기본 글자색 흰색 */
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
</style>

<style>
.font {
  font-family: 'NPSfont_regular';
}
</style>
