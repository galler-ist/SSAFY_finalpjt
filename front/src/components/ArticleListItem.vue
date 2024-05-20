<template>
  <div>
    <thead>
      <tr class="css-17wis8 e1bqvdeb3">
        <th width="192px" class="css-153q73d e1bqvdeb5">작성자</th>
        <th width="726px" class="css-1i8er73 e1bqvdeb5">제목</th>
        <th width="202px" class="css-1k8lsbw e1bqvdeb5">날짜</th>
      </tr>
    </thead>
    <tbody>
      <tr class="css-17wis8 e1bqvdeb3">
        <td class="css-1biv9gc e1bqvdeb2">{{ article.username }}</td>
        <td class="css-1biv9gc e1bqvdeb2"><RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">{{ article.title }}</RouterLink></td>
        <td class="css-1biv9gc e1bqvdeb2">{{ article.created_at }}</td>
      </tr>
    </tbody> 
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})
</script>
<style>

</style>