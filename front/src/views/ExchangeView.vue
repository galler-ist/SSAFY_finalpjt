<template>
  <div class="image-container bg-image">
    <img class="bg w-100 exchange-bg " src="/assets/exchange2_bg.png" alt="...">
    <h1 class="title-container">환율 계산기</h1>
  </div>
  <div class="main-container">
    <div class="exchange-container">
      <div>
        <p>원화 입력</p>
        <input type="number" v-model="amount" id="amount" required />
      </div>
      <div>
        <p>타국 통화</p>
        <select v-model="toCurrency" id="toCurrency" required>
          <option v-for="currency in currencies" :key="currency.cur_unit" :value="currency.cur_unit">{{ currency.cur_unit }} - {{ currency.cur_nm }}</option>
        </select>
      </div>
    </div>
    <button class="custom-button">
      <img style="width: 30px" class="exchange-icon" src="/assets/exchange_icon.png" alt="...">
    </button>
    <div class="exchange-container">
      <div>
        <p>원화 입력</p>
        <input type="number" v-model="amount" id="amount" required />
      </div>
      <div>
        <p>타국 통화</p>
        <select v-model="toCurrency" id="toCurrency" required>
          <option v-for="currency in currencies" :key="currency.cur_unit" :value="currency.cur_unit">{{ currency.cur_unit }} - {{ currency.cur_nm }}</option>
        </select>
      </div>
    </div>
    
  </div>


  <!-- <hr><hr><hr>
  <form @submit.prevent="calculate">
    <div class="firstflex">
      <label class="krw-container" for="amount">원화 입력</label>
      <input class="county-money" type="number" v-model="amount" id="amount" required />
    </div>
    <div>
      <label for="toCurrency">타국 통화:</label>
      <span>{{ toCurrencySymbol }}</span>
    </div>
    <button type="submit">계산</button>
  </form>

  <div class="all-container">
    <div>
      <div v-if="result !== null">
        <h2>결과: {{ amount }} KRW = {{ result }} {{ toCurrency }}</h2>
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
  </div> -->
</template>

<script>
export default {
  data() {
    return {
      amount: 0,
      foreignAmount: 0,
      fromCurrency: 'KRW',
      toCurrency: '',
      currencies: [],
      rates: {},
      result: null,
      reverseResult: null,
    };
  },
  computed: {
    toCurrencySymbol() {
      const currency = this.currencies.find(c => c.cur_unit === this.toCurrency);
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
        console.log('우선 response자체가 받아는 와질까', response)
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        const data = await response.json();
        this.currencies = data;
        console.log('this.currencies이자 data야', data)
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
        alert('금액을 입력하세요');
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
.image-container {
  position: relative;
  text-align: center;
}

.exchange-bg {
  width: 100%;
  height: 18rem;
  opacity: 0.7;
}

.image-container::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
}

.title-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-weight: 500;
  font-size: 2rem;
  text-align: center;
  z-index: 1;
}

.all-container {
  display: flex;
  flex-direction: column;
  width: 65%;
  margin: 0 auto;
  padding: 0;
}

.firstflex {
  display: flex;
  align-items: center;
}

.krw-container {
  display: flex;
  width: 5rem;
  border: 1px solid gray;
  border-radius: 5px 0 0 5px;
}

.county-money {
  display: flex;
  flex-wrap: nowrap;
  border: 1px solid gray;
  border-radius: 0 5px 5px 0;
}

.exchange100 {
  color: gray;
}

form div {
  margin-bottom: 10px;
}

.exchange-container {
  border: 1px solid gray;
  border-radius: 10px;
  box-shadow: 1px 1px 1px 1px lightgray;
  margin: 10px;
  padding: 10px;
  width: 40%;
}
.main-container {
  display: flex;
  flex-direction: row;
  width: 65%;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
}
.exchange-icon {

  width:5%;
  height: 5%;
}
.bg-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  mask-image: linear-gradient(to bottom, rgba(0, 0, 0, 1), rgba(0, 0, 0, 0));
  /* or use -webkit-mask-image for better compatibility with some browsers */
  -webkit-mask-image: linear-gradient(to bottom, rgba(0, 0, 0, 1), rgba(0, 0, 0, 0));
}
.custom-button {
  background-color: white; /* 버튼 배경색 흰색 */
  border: 1px solid white; /* 버튼 경계선 흰색 */
  padding: 5px; /* 이미지를 더 잘 보이도록 패딩 추가 */
  border-radius: 4px; /* 경계선 모서리 둥글게 */
}
</style>
