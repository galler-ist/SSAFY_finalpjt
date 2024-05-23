<template>
    <div class="page-container">
      <div class="page-row">
        <div class="left-container">
          <div class="sub-row" v-if="portfolio">
            <div class="sub-left">
              <p>생일</p>
              <p>가구원수</p>
              <p>결혼 상태</p>
              <p>자녀 여부</p>
              <p>수입</p>
            </div>
            <div class="sub-right">
              <p>{{ portfolio.birth }}</p>
              <p>{{ portfolio.household_size }}</p>
              <p v-if="portfolio.marital_status === 'married'">기혼</p>
              <p v-if=" portfolio.has_children === false">없음</p>
              <p>{{ portfolio.income }}</p>
            </div>
          </div>
          <div v-else>
              <h2>포트폴리오가 아직 없어요</h2>
              <router-link :to="{ name: 'PortfolioEdit' }">Create New Portfolio</router-link>
          </div>
          
        </div>
        <div class="right-container">
          <h3>가입한 예금 상품:</h3>
            <ul>
              <li v-for="deposit in portfolio.deposits" :key="deposit.deposit_code">
                {{ deposit.name }} ({{ deposit.kor_co_nm }})
              </li>
            </ul>
            <h3>가입한 적금 상품:</h3>
            <ul>
              <li v-for="saving in portfolio.savings" :key="saving.saving_code">
                {{ saving.name }} ({{ saving.kor_co_nm }})
              </li>
            </ul>    
            <p>score: {{ score }}</p>   
        </div>
      </div>
    </div>
  </template>
  
<script setup>
  import axios from 'axios'
  import { ref, onMounted, watch, computed } from 'vue'
  import { useCounterStore } from '@/stores/counter.js' 

  const store = useCounterStore()
  const portfolio = ref([])
  const score = ref(0)

  const fetchPortfolio = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/portfolio/api/user/${store.username}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    portfolio.value = response.data
    await calculateScore()
  } catch (error) {
    console.error('Error fetching portfolio:', error)
  }
}


const calculateScore = async () => {
  if (!portfolio.value) return
  try {
    const response = await axios.post(`${store.API_URL}/portfolio/score/`, {
      birth: portfolio.value.birth,
      household_size: portfolio.value.household_size,
      marital_status: portfolio.value.marital_status,
      has_children: portfolio.value.has_children,
      income: portfolio.value.income
    }, {
      headers: {
        Authorization: `Token ${store.token}`,
        'Content-Type': 'application/json'
      }
    })
    score.value = response.data.score
  } catch (error) {
    console.error('Error calculating score:', error)
  }
}








onMounted(() => {
  fetchPortfolio();
});
//   const fetchPortfolio = async () => {
//   if (!store.token) {
//     console.error('Token is not available')
//     return
//   }

//   try {
//       const response = await axios.get(`${store.API_URL}/portfolio/api/user/${store.username}/`, {
//           headers: {
//               Authorization: `Token ${store.token}`
//             }
//         })
//         portfolio.value = response.data
//         console.log('portfolio~~~', portfolio.value)
//   } catch (error) {
//     console.error('Error fetching portfolio:', error)
//   }
// }

// watch(
//   () => store.token,
//   (newToken) => {
//     if (newToken) {
//       fetchPortfolio()
//     }
//   }
// )

</script>
  
<style scoped>

.page-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.page-row {
  display: flex;
  flex-direction: row;
  width: 65%;
  margin: 20px;
  margin-left: 100px;
}
.left-container {
  border: 1px solid rgb(230, 230 ,230);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width:45%;
  box-shadow: 1px 1px gray;
  border-radius: 10px;
  padding: 15px;
}
.right-container {
  border: 1px solid rgb(230, 230 ,230);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width:45%;
  margin-left: 20px;
  box-shadow: 1px 1px gray;
  border-radius: 10px;
  padding: 15px;
}
.sub-left {
  text-align: left;
}
.sub-right {
  text-align: left;
  margin-left: 80px;
}
.sub-row {
  display: flex;
  flex-direction: row;
}
</style>
  