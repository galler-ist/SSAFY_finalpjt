<template>
  <div class="deposit-table">
    <h3>적금 조회</h3>

    <label class="bank-select" for="bank-select">은행 선택&nbsp;</label>
    <select id="bank-select" v-model="selectedBank">
      <option value="">모든 은행</option>
      <option v-for="bank in uniqueBanks" :key="bank" :value="bank">{{ bank }}</option>
    </select>

    <table class="table-container">
      <thead>
        <tr>
          <th>상품명</th>
          <th>은행명</th>
          <th>금리유형</th>
          <th @click="sortTable('1개월')">저축 기간-1개월
            <span v-if="sortKey === '1개월'">
              <span v-if="sortOrder === 1">▲</span>
              <span v-else>▼</span>
            </span>
          </th>
          <th @click="sortTable('3개월')">저축 기간-3개월
            <span v-if="sortKey === '3개월'">
              <span v-if="sortOrder === 1">▲</span>
              <span v-else>▼</span>
            </span>
          </th>
          <th @click="sortTable('6개월')">저축 기간-6개월
            <span v-if="sortKey === '6개월'">
              <span v-if="sortOrder === 1">▲</span>
              <span v-else>▼</span>
            </span>
          </th>
          <th @click="sortTable('12개월')">저축 기간-12개월
            <span v-if="sortKey === '12개월'">
              <span v-if="sortOrder === 1">▲</span>
              <span v-else>▼</span>
            </span>
          </th>
          <th @click="sortTable('24개월')">저축 기간-24개월
            <span v-if="sortKey === '24개월'">
              <span v-if="sortOrder === 1">▲</span>
              <span v-else>▼</span>
            </span>
          </th>
          <th @click="sortTable('36개월')">저축 기간-36개월
            <span v-if="sortKey === '36개월'">
              <span v-if="sortOrder === 1">▲</span>
              <span v-else>▼</span>
            </span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="comparison in filteredDeposits" :key="comparison.name + comparison.bank_name + comparison.interest_rate_type">
          <td>{{ comparison.name }}</td>
          <td>{{ comparison.bank_name }}</td>
          <td>{{ comparison.interest_rate_type }}</td>
          <td>{{ comparison['1개월'] || '-' }}</td>
          <td>{{ comparison['3개월'] || '-' }}</td>
          <td>{{ comparison['6개월'] || '-' }}</td>
          <td>{{ comparison['12개월'] || '-' }}</td>
          <td>{{ comparison['24개월'] || '-' }}</td>
          <td>{{ comparison['36개월'] || '-' }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const deposits = ref([]);
    const depositComparison = ref([]);
    const selectedBank = ref('');
    const sortKey = ref('');
    const sortOrder = ref(-1); // 1 for ascending, -1 for descending

    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/finance/deposit/');
        deposits.value = response.data;

        const comparisonMap = {};

        deposits.value.forEach(deposit => {
          const key = `${deposit.base.name}-${deposit.base.kor_co_nm}-${deposit.base.spcl_cnd}`;
          if (!comparisonMap[key]) {
            comparisonMap[key] = {
              name: deposit.base.name,
              bank_name: deposit.base.kor_co_nm,
              interest_rate_type: deposit.options.length > 0 ? deposit.options[0].intr_rate_type_nm : 'N/A',
              special_condition: deposit.base.spcl_cnd,
              '1개월': '-',
              '3개월': '-',
              '6개월': '-',
              '12개월': '-',
              '24개월': '-',
              '36개월': '-'
            };
          }
          deposit.options.forEach(option => {
            const termKey = `${option.save_trm}개월`;
            const interestRateDisplay = option.intr_rate2 ? `${option.intr_rate2}` : `${option.intr_rate}`;
            comparisonMap[key][termKey] = interestRateDisplay;
          });
        });

        depositComparison.value = Object.values(comparisonMap);
      } catch (error) {
        console.error(error);
      }
    };

    const sortTable = (key) => {
      if (sortKey.value === key) {
        sortOrder.value = -sortOrder.value; // Toggle sort order
      } else {
        sortKey.value = key;
        sortOrder.value = -1; // Default to ascending
      }
    };

    const uniqueBanks = computed(() => {
      const banks = deposits.value.map(deposit => deposit.base.kor_co_nm);
      return [...new Set(banks)];
    });

    const filteredDeposits = computed(() => {
      let filtered = depositComparison.value;
      if (selectedBank.value) {
        filtered = filtered.filter(deposit => deposit.bank_name === selectedBank.value);
      }
      return filtered.sort((a, b) => {
        const aValue = a[sortKey.value] || '';
        const bValue = b[sortKey.value] || '';
        return aValue.localeCompare(bValue) * sortOrder.value;
      });
    });

    onMounted(fetchData);

    return {
      deposits,
      depositComparison,
      selectedBank,
      sortTable,
      filteredDeposits,
      sortKey,
      sortOrder,
      uniqueBanks
    };
  }
};
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border: 1px solid #ddd;
  padding: 8px;
}
th {
  background-color: #f2f2f2;
  text-align: center;
  cursor: pointer;
}
td {
  text-align: center;
}
.deposit-table {
  width: 65%;
  margin: 0 auto;
}
.table-container {
  width: 100%;
  border-collapse: collapse;
}
.bank-select {
  padding: 1rem 0rem;
}
</style>
