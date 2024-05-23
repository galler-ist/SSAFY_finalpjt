<template>
  <div class="">
    <div v-if="user">
      <div class="page-container">
        <div class="left-container">
          <p class="p-tag">Username</p>
          <p class="p-tag">Nickname</p>
          <p class="p-tag">Email</p>
          <p class="p-tag">Last Login</p>
        </div>
        <div class="right-container">
          <p class="p-tag">{{ user.username }}</p>
          <p class="p-tag">nonggeun</p>
          <p class="p-tag">{{ user.email }}</p>
          <p class="p-tag">2024년 5월 24일</p>
        </div>
      </div>
    </div>
    <h3 class="page-container" v-else>Log In 하고 와요</h3>
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
    console.log(user.username)
    console.log(user.last_login)
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
.page-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 30px;

}
.page-row {

  width: 80%;

}
.left-container {
  border-right: 1px dashed gray;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width:45%;
  padding: 15px;
  margin-left: 20px;
  text-align: left;
}
.right-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width:45%;
  padding: 15px;
  text-align: left;
}
.p-tag {
  margin: 20px;
  font-size: 20px;
  text-align: left;

}

  </style>
  