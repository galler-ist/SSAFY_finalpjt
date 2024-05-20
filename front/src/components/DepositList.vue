<template>
    <div>
      <h1>Deposits</h1>
      <ul>
        <li v-for="deposit in deposits" :key="deposit.id">
          <!-- 이름-: {{ deposit.name }} - {{ deposit.interest_rate }}% -->
          이름: {{ deposit.name }} , 은행: {{ deposit.cor_co_nm }}, 이자계산: {{ deposit.mtrt_int }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        deposits: []
      };
    },
    created() {
      axios.get('http://localhost:8000/finance/deposit/')
        .then(response => {
          this.deposits = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  };
  </script>
  