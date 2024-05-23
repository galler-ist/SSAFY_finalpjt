<template>
    <div>
        <h1 class="title-container">포트폴리오</h1>
    </div>

    <nav class="nav-sticky nav-container">
      <RouterLink :to="{ name: 'PortfolioList' }">PORTFOLIO</RouterLink>|
      <RouterLink :to="{ name: 'PortfolioEdit', params: { id: id} }">EDIT PORTFOLIO</RouterLink>|
      <RouterLink :to="{ name: 'Profile' }">프로필</RouterLink>
    </nav>
    <div class="main-container">
      <router-view></router-view>
    </div>
    </template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter.js' 

const counterStore = useCounterStore()
const id = counterStore.username


</script>
<style scoped>
.title-container {
  display: flex;
  justify-content: center;
  padding-top: 15vh;
  width: 100%;
  height: 30vh;
  color: black;
  font-weight: 700;
}
.main-container {
  background-color: rgb(248, 248, 248);
  border-top: 1px solid rgb(230, 230, 230);
}
.nav-sticky {
  position: sticky;
  display: flex;
  justify-content: center;
  align-items: center;
  top:15px;
  width: 100%;
}
.nav-container {
  margin: 20px;
  text-align: center;
  /* position: sticky; */
}
nav a {
  font-size: 20px;
  text-decoration: none;
  color: black;
  margin: 0px 33px;
}

nav a.router-link-exact-active {
  font-weight: bold;
  border-bottom: 3px solid rgba(241, 139, 49, 0.884);
}

</style>