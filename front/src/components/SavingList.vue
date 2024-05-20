<template>
  <div>
    <h1>Savings</h1>
    <ul>
      <li v-for="saving in savings" :key="saving.id">
        <!-- 이름-: {{ saving.name }} - {{ saving.interest_rate }}% -->
        <!-- saving: {{saving}} -->
        이름: {{ saving.name }} , 은행: {{ saving.kor_co_nm }}, 이자계산: {{ saving.mtrt_int }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      savings: []
    };
  },
  created() {
    axios.get('http://localhost:8000/finance/savings/')
      .then(response => {
        this.savings = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  }
};
</script>
