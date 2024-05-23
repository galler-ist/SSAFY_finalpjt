<template>
  <form @submit.prevent="savePortfolio">
    <div class="page-container">
      <div class="page-row">
        <div class="left-container">
          <div class="sub-left">
            <label class="label-tag" for="birth">생년월일&nbsp;&nbsp;</label>
            <label class="label-tag" for="household_size">가구원 수&nbsp;&nbsp;</label>
          </div>
          <div class="sub-right">
            <input class="input-tag" type="date" v-model="portfolio.birth" />
            <input class="input-tag" type="number" v-model="portfolio.household_size" />
          </div>
        </div>
        <div class="right-container">
          <div class="sub-left">
            <label class="label-tag" for="income">수입&nbsp;&nbsp;</label>
            <label class="label-tag" for="marital_status">결혼 여부&nbsp;&nbsp;</label>
            <label class="label-tag" for="has_children">자녀 유무&nbsp;&nbsp;</label>
          </div>
          <div class="sub-right">
            <input class="input-tag" type="number" v-model="portfolio.income" step="0.01" />
            <select class="input-tag" v-model="portfolio.marital_status" @change="toggleChildren">
              <option value="single">미혼</option>
              <option value="married">기혼</option>
            </select>
            <div v-if="portfolio.marital_status === 'married'">
            <input class="input-tag" type="checkbox" v-model="portfolio.has_children" />
            </div>
          </div>
          
        </div>
        <!-- <div>
            <label for="savings">Savings:</label>
            <div v-for="option in savingsOptions" :key="option.id">
            <input type="checkbox" :value="option.id" v-model="portfolio.savings" />
            <label>{{ option.name }}</label>
            </div>
        </div> -->

      </div>
      <div class="chartlist">
        <p>Chart List</p>
      </div>
      <button class="btn" type="submit">Save</button>
    </div>
  </form>
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
    console.log(portfolio.value.income)
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
.page-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 30px;
}
.page-row {
  display: flex;
  flex-direction: row;
  width: 80%;

}
.left-container {
  border-right: 1px dashed gray;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  width:45%;
  padding: 15px;
  margin-left: 60px;
}
.right-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  width:45%;

  padding: 15px;
}
.sub-left {
  display: flex;
  flex-direction: column;
  text-align: left;
}
.sub-right {
  display: flex;
  flex-direction: column;
  text-align: right;
}
.input-tag {
  margin: 10px;
}
.label-tag {
  margin: 10px;
}
.chartlist {
  border: 1px solid gray;
  width: 65%;
  text-align: center;
  height: 50rem;
}
</style>
