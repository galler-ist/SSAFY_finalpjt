<template>
  <div>
    <img class="bg w-100 excahnge-bg" src="/assets/exchange_bg.png" alt="...">
    <h1 class="overlay">환율 계산기</h1>
  </div>
  <div class="all">
    <div>
      <form @submit.prevent="calculate">
        <div>
          <label class="krw-container" for="amount">원화 입력</label>
          <input class="county-money" type="number" v-model="amount" id="amount" required />
        </div>
        <div>
          <label for="toCurrency">타국 통화:</label>
          <select v-model="toCurrency" id="toCurrency" required>
            <option v-for="currency in currencies" :key="currency.cur_unit" :value="currency.cur_unit">{{ currency.cur_unit }} - {{ currency.cur_nm }}</option>
          </select>
          <span>{{ toCurrencySymbol }}</span>
        </div>
        <button type="submit">계산</button>
      </form>
      <div v-if="result !== null">
        <h2>결과: {{ amount }} KRW = {{ result }} {{  toCurrency }}</h2>
      </div>
    </div>
      <hr>
      <form @submit.prevent="calculateReverse">
        <h2>타국 -> 한화</h2>
        <div>
            <label for="foreignAmount">타국 통화 입력:</label>
            <input type="number" v-model="foreignAmount" id="foreignAmount" required />
            <span>{{ toCurrency }}</span>
        </div>

        <button type="submit">계산</button>
        </form>
        <div v-if="reverseResult !== null">
        <h2>결과: {{ foreignAmount }} {{ toCurrency }} = {{ reverseResult }} KRW</h2>
        </div>
        <hr>
        <h2 class="exchange100">인도네시아 루피아(IDR), 일본 옌(JPY)은 100단위로 들어감</h2>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        amount: 0,
        foreignAmount: 0,
        fromCurrency: 'KRW',
        toCurrency: '',
        currencies: ['USD','JPY','EUR'],
        rates: {},
        result: null,
        reverseResult: null,
      };
    },
    computed: {
        toCurrencySymbol() {
            const currency = this.currencies.find( c=> {
                c.cur_unit === this.toCurrency;
            })
            return currency ? currency.symbol : '';
        }
    },
    mounted() {
      this.fetchRates();
    },
    methods: {
      async fetchRates() {
        try {
          const response = await fetch('http://127.0.0.1:8000/exchange/');
          const data = await response.json();
          this.currencies = data;
          this.rates = data.reduce((acc, cur) => {
            acc[cur.cur_unit] = parseFloat(cur.deal_bas_r.replace(/,/g, ''));
            return acc;
          }, {});
        } catch (error) {
          console.error('Failed to fetch exchange rates:', error);
        }
      },
      getKoreanPostposition(word) {
        const lastChar = word[word.length - 1];
        const code = lastChar.charCodeAt(0);

        if (code >= 0xAC00 && code <= 0xD7A3) { // 한글인지 확인
        const hasBatchim = (code - 0xAC00) % 28 > 0;
        return hasBatchim ? '을' : '를';
      }
      // 알파벳(L,M,N,R)이면 '을' 나머지 알파벳은 '를'
      const isLMNR = ['L', 'M', 'N', 'R', 'l', 'm', 'n', 'r'].includes(lastChar);
      return isLMNR ? '을' : '를';
    },
      calculate() {
        if (this.amount <= 0) {
          alert('한화를 입력하세요');
          return;
        }

        if (this.toCurrency && this.amount > 0) {
          const rate = this.rates[this.toCurrency];
          if (rate) {
            this.result = (this.amount / rate).toFixed(2);
          } else {
            alert(`${this.toCurrency}${this.getKoreanPostposition(this.toCurrency)} 찾을 수 없습니다.`);
            this.result = null;
          }
        }
      },
      calculateReverse() {
        if (this.foreignAmount <= 0) {
        alert(`${this.toCurrency}${this.getKoreanPostposition(this.toCurrency)} 입력하세요`);
        return;
      }
        if (this.toCurrency && this.foreignAmount > 0) {
            const rate = this.rates[this.toCurrency];
            if (rate) {
                this.reverseResult = (this.foreignAmount * rate).toFixed(2);
            } else {
                alert('해당 환율 정보를 찾을 수 없습니다.');
                this.reverseResult = null;
            }
        }
      }
    },
  };
  </script>
  
  <style scoped>
  form div {
    margin-bottom: 10px;
  }

  .exchange100 {
    color: gray;
    
  }
  .excahnge-bg {
    height: 20rem;
    opacity: 0.7;
  }
  .overlay {
    position: absolute;
    top: 20%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: black;
    font-weight: 500;
    font-size: 2rem;
    text-align: center;
  }

  .all {
    margin: 2rem 15rem;
  }
  .krw-container {
    display: flex;
    width: auto;
    border: 1px solid gray;
    border-radius: 10px 0px 0px 10px;
  }
  .county-money {
    display: flex;
    border: 1px solid gray;
    border-radius: 0px 10px 10px 0px;
  }
  </style>
  