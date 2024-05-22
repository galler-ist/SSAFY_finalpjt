<template>
    <div>
      <h2>{{ isEditMode ? 'Edit' : 'Create' }} Portfolio</h2>
      <form @submit.prevent="savePortfolio">
        <div>
            <label for="birth">Birth :</label>
            <input type="date" v-model="portfolio.birth" />
        </div>
        <div>
            <label for="household_size">Household Size:</label>
            <input type="number" v-model="portfolio.household_size" />
        </div>
        <div>
            <label for="marital_status">Marital Status:</label>
            <select v-model="portfolio.marital_status" @change="toggleChildren">
            <option value="single">미혼</option>
            <option value="married">기혼</option>
            </select>
        </div>
        <div v-if="portfolio.marital_status === 'married'">
            <label for="has_children">Has Children:</label>
            <input type="checkbox" v-model="portfolio.has_children" />
        </div>
        <div>
            <label for="income">Income:</label>
            <input type="number" v-model="portfolio.income" step="0.01" />
        </div>
        <!-- <div>
            <label for="savings">Savings:</label>
            <div v-for="option in savingsOptions" :key="option.id">
            <input type="checkbox" :value="option.id" v-model="portfolio.savings" />
            <label>{{ option.name }}</label>
            </div>
        </div> -->
        <button type="submit">Save</button>
        </form>
    </div>
  </template>
  
<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const portfolio = ref({
  birth: '',
  household_size: 0,
  marital_status: 'single',
  has_children: false,
  income: 0,
})
const isEditMode = ref(false)
// const savingsOptions = ref([])
  
const fetchPortfolio = async () => {
    const username = store.username
  try {
    console.log('store.API_URL 는', store.API_URL)
    console.log('store.username 는', store.username)
    console.log('store.token 는', store.token)
    const response = await axios.get(`${store.API_URL}/portfolio/api/user/${username}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    portfolio.value = response.data
  } catch (error) {
    console.error(error)
    isEditMode.value = false
  }
}

// const fetchSavingsOptions = async () => {
//   try {
//     const response = await axios.get(`${store.API_URL}/portfolio/api/saving-options/`, {
//       headers: {
//         Authorization: `Token ${store.token}`
//       }
//     })
//     savingsOptions.value = response.data
//   } catch (error) {
//     console.error(error)
//   }
// }

// const updatePortfolio = async () => {
//   try {
//     await axios.put(`${store.API_URL}/portfolio/api/portfolios/${store.username}/`, portfolio.value, {
//       headers: {
//         Authorization: `Token ${store.token}`
//       }
//     })
//     router.push({ name: 'PortfolioList' })
//   } catch (error) {
//     console.error(error)
//   }
// }

const toggleChildren = () => {
  if (portfolio.value.marital_status !== 'married') {
    portfolio.value.has_children = false
  }
}

onMounted( () => {
  const { id } = route.params
  if (id) {
    isEditMode.value = true
    fetchPortfolio(id)
  }
})

const savePortfolio = async () => {
  const { id } = route.params
  try {
    if (isEditMode.value) {
      await axios.put(`${store.API_URL}/portfolio/api/user/${id}/`, portfolio.value, {
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
    } else {
      await axios.post(`${store.API_URL}/portfolio/api/portfolios/`, portfolio.value, {
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
    }
    router.push({ name: 'PortfolioList' })
  } catch (error) {
    console.error('Error saving portfolio:',error)
  }
}





</script>

<style scoped>
/* 스타일을 여기에 작성 */
</style>
