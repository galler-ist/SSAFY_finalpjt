<template>
    <div>
      <h2>My Portfolio</h2>
        <div v-if="portfolio">
            <p>생일: {{ portfolio.birth }}</p>
            <p>가구원수: {{ portfolio.household_size }}</p>
            <p>결혼 상태: {{ portfolio.marital_status }}</p>
            <p>자녀 여부: {{ portfolio.has_children }}</p>
            <p>수입: {{ portfolio.income }}</p>
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
          </div>
        <div v-else>
            <h2>포트폴리오가 아직 없어요</h2>
        </div>
    </div>
  </template>
  
<script setup>
  import axios from 'axios'
  import { ref, onMounted, watch } from 'vue'
  import { useCounterStore } from '@/stores/counter.js' 

  const store = useCounterStore()
  const portfolio = ref([])
  
  const fetchPortfolio = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/portfolio/api/user/${store.username}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    portfolio.value = response.data
  } catch (error) {
    console.error('Error fetching portfolio:', error)
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
  /* 스타일을 여기에 작성 */
  </style>
  