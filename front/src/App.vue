<template>
  <nav class="navbar navbar-expand-lg bg-body-lg">
    <div class="container-fluid">
      <RouterLink class="navbar-brand" style="color : #702828" :to="{ name: 'HomeView' }">Home</RouterLink>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav me-auto">

          <RouterLink class="nav-link" style="color : #702828" :to="{ name: 'ArticleView' }">Articles</RouterLink>
          <RouterLink class="nav-link" style="color : #702828" :to="{ name: 'BankView' }">Bank</RouterLink>
          <RouterLink class="nav-link" style="color : #702828" :to="{ name: 'ExchangeView' }">Exchange</RouterLink>
        </div>
        <div class="navbar-nav ms-auto">
          <RouterLink class="nav-link" style="color : #702828" v-if="!isLogin" :to="{ name: 'SignUpView' }">Sign In</RouterLink>
          <RouterLink class="nav-link" style="color : #702828" v-if="!isLogin" :to="{ name: 'LogInView' }">Log In</RouterLink>
          <button class="nav-link btn btn-link" style="color : #702828" v-else @click="logOut">Log Out</button>
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
</style>
