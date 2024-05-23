<template>
    <div>
        <h1>여기는 포폴 사이트야</h1>
    </div>

    <nav>
      <RouterLink :to="{ name: 'PortfolioList' }">My Portfolio</RouterLink>|
      <RouterLink :to="{ name: 'PortfolioEdit', params: { id: id} }">Edit Portfolio</RouterLink>|
      <RouterLink :to="{ name: 'Profile' }">My Profile</RouterLink>

    </nav>
    <router-view></router-view>
    </template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter.js' 

const counterStore = useCounterStore()
const id = counterStore.username


</script>
<style scoped>

</style>