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
        <label for="deposits">Deposits:</label>
      <div v-for="deposit in availableDeposits" :key="deposit.deposit_code">
        <input type="checkbox" :value="deposit.deposit_code" @change="updateSelectedDeposits(deposit)">
        {{ deposit.name }} ({{ deposit.kor_co_nm }})
      </div>

      <label for="savings">Savings:</label>
      <div v-for="saving in availableSavings" :key="saving.saving_code">
        <input type="checkbox" :value="saving.saving_code" @change="updateSelectedSavings(saving)">
        {{ saving.name }} ({{ saving.kor_co_nm }})
      </div>


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

const savings = ref([]);
const deposits = ref([]);
const selectedSavings = ref([]);
const selectedDeposits = ref([]);
const birth = ref('');
const householdSize = ref(1);
const maritalStatus = ref('single');
const hasChildren = ref(false);
const income = ref(0);

const portfolio = ref({
  birth: '',
  household_size: 0,
  marital_status: 'single',
  has_children: false,
  income: 0,
  deposits: [],
  savings: []
})
const availableDeposits  = ref([]);
const availableSavings  = ref([]);

const fetchDeposits = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/finance/api/v1/deposits/`);
    console.log(response.data)
    availableDeposits.value = response.data;
  } catch (error) {
    console.error(error);
  }
};

const fetchSavings = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/finance/api/v1/savings/`);
    availableSavings.value = response.data;
  } catch (error) {
    console.error(error);
  }
};

const fetchPortfolio = async () => {
  if (store.username) {
      console.log(portfolio.value.income)
  try {
  
    const response = await axios.get(`${store.API_URL}/portfolio/api/user/${store.username}/`,  {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      portfolio.value = response.data;
    } catch (error) {
      console.error(error,'fetchPortfolio 부분입니다.');
    }
  }
};

// const fetchFinanceProducts = async () => {
//   try {
//     const savingsResponse = await axios.get(`${store.API_URL}/api/savings/`, {
//       headers: {
//         Authorization: `Token ${store.token}`
//       }
//     });
//     savings.value = savingsResponse.data;

//     const depositsResponse = await axios.get(`${store.API_URL}/api/deposits/`, {
//       headers: {
//         Authorization: `Token ${store.token}`
//       }
//     });
//     deposits.value = depositsResponse.data;

//     if (route.params.id) {
//       isEditMode.value = true;
//       const response = await axios.get(`${store.API_URL}/portfolio/api/user/${route.params.id}/`, {
//         headers: {
//           Authorization: `Token ${store.token}`
//         }
//       });
//       const data = response.data;
//       birth.value = data.birth;
//       householdSize.value = data.household_size;
//       maritalStatus.value = data.marital_status;
//       hasChildren.value = data.has_children;
//       income.value = data.income;
//       selectedSavings.value = data.savings.map(saving => saving.saving_code);
//       selectedDeposits.value = data.deposits.map(deposit => deposit.deposit_code);
//       portfolio.value = data;
//     }
//   } catch (error) {
//     console.error('Error fetching finance products:', error);
//   }
// };

// const fetchPortfolio = async () => {
//     const username = store.username
//   try {
//     const response = await axios.get(`${store.API_URL}/portfolio/api/user/${username}/`, {
//       headers: {
//         Authorization: `Token ${store.token}`
//       }
//     })
//     portfolio.value = response.data
//   } catch (error) {
//     console.error(error)
//     isEditMode.value = false
//   }
// }

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

const updateSelectedDeposits = (deposit) => {
  const index = portfolio.value.deposits.findIndex(d => d.deposit_code === deposit.deposit_code);
  if (index === -1) {
    portfolio.value.deposits.push(deposit);
  } else {
    portfolio.value.deposits.splice(index, 1);
  }
};

const updateSelectedSavings = (saving) => {
  const index = portfolio.value.savings.findIndex(s => s.saving_code === saving.saving_code);
  if (index === -1) {
    portfolio.value.savings.push(saving);
  } else {
    portfolio.value.savings.splice(index, 1);
  }
};



onMounted(() => {
  fetchDeposits();
  fetchSavings();
  fetchPortfolio();
});

const savePortfolio = async () => {
  console.log(store.username,'store.username===route.params.id')
  console.log(store.user_id)
  try {
    const data = {
      birth: portfolio.value.birth,
      household_size: portfolio.value.household_size,
      marital_status: portfolio.value.marital_status,
      has_children: portfolio.value.has_children,
      income: portfolio.value.income,
      deposits: portfolio.value.deposits.map(deposit => ({
        deposit_code: deposit.deposit_code,
        kor_co_nm: deposit.kor_co_nm,
        name: deposit.name
      })),
      savings: portfolio.value.savings.map(saving => ({
        saving_code: saving.saving_code,
        kor_co_nm: saving.kor_co_nm,
        name: saving.name
      }))
    };
    console.log(data,'dataaaaa')
    if (route.params.id) {
      await axios.put(`${store.API_URL}/portfolio/api/user/${store.username}/`, data, {
        headers: {
          Authorization: `Token ${store.token}`
        }
      });
    } else {
      await axios.post(`${store.API_URL}/portfolio/api/user/`, data, {
        headers: {
          Authorization: `Token ${store.token}`
        }
      });
    }
    router.push({ name: 'PortfolioList' });
  } catch (error) {
    console.error('Error saving portfolio:', error.response ? error.response.data : error);
  }
};



// finance쪽 URL은 finance / api / v1 / > router.urls (deposits, savings)
// <div>
//   <label for="savings">Savings</label>
//   <select v-model="portfolio.savings" multiple>
//     <option v-for="saving in savings" :key="saving.saving_code" :value="saving">
//       {{ saving.kor_co_nm }} - {{ saving.name }}
//     </option>
//   </select>   
// </div>
// <div>
//   <label for="deposits">Deposits</label>
//   <select v-model="portfolio.deposits" multiple>
//     <option v-for="deposit in deposits" :key="deposit.deposit_code" :value="deposit">
//       {{ deposit.kor_co_nm }} - {{ deposit.name }}
//     </option>
//   </select>
// </div>
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

