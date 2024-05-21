<!-- 
<template>
  <tbody class="row">
    <tr class="col- article-container">

        <td width="60%">
          <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">{{ article.title }}</RouterLink>
        </td>
        <td width="20%">
          {{ article.username }}
        </td>
        <td width="20%">
          {{ article.created_at.substring(0, 10) }}
        </td>
      
    </tr>
  </tbody>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.article-container {
  display: flex;
  flex-direction: row;
  justify-items: center;
  width: 100%;
}
.article-table {
  width: 90%;
  /* border-collapse: collapse; */
  /* margin-bottom: 20px; */
}
td {
  padding: 12px 8px;
  border-bottom: 1px solid #ddd;
}

a {
  text-decoration: none;
  color: #007bff;
  transition: color 0.3s ease;
}

a:hover {
  color: #0056b3;
}
</style> -->
<template>

    <div class="col">
      
      <p class="title-column"><RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">{{ article.title }}</RouterLink></p>
      <p class="username-column">{{ article.username }}</p>
      <p class="date-column">{{ article.created_at.substring(0, 10) }}</p>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.col {
  width: 100%;
  display: flex;

}

.title-column {
  width: 60%;
  padding: 12px 0px;
  border-bottom: 1px solid #ddd;
  color: black;
}

.username-column {
  width: 20%;
  padding: 12px 0px;
  border-bottom: 1px solid #ddd;
}

.date-column {
  width: 20%;
  padding: 12px 0px;
  border-bottom: 1px solid #ddd;

}

a {
  text-decoration: none;
  color: black;
  transition: color 0.3s ease;
}

a:hover {
  color: #0056b3;
}

tr {
  width: 100%;
}
</style>
