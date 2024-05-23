<template>
    <div>
      <h2>My Profile</h2>
      <div v-if="user">
        <h3>Username: {{ user.username }}</h3>
        <h3>Nickname: seungwoo </h3>
        <p>Email: {{ user.email }}</p>
        <h3>Last Login: 2024년 05월 23일</h3>
      </div>
      <p v-else>유저가 없어요</p>
    </div>
  </template>
  
<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter.js' 
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const user = ref(null);

onMounted(() => {
  fetchProfile()
})



 
const fetchProfile = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/accounts/api/profile/`, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${store.token}`
      }
    });
    user.value = response.data
  } catch (error) {
    console.error('Failed to fetch user data:', error);
  }
};


const formatDate = (date) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
  return new Date(date).toLocaleDateString(undefined, options);
};
</script>



  
  <style scoped>
  /* 스타일을 여기에 작성 */
  </style>
  