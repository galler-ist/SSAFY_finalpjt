<template>

  <div>
    <tbody>
      <tr class="">
        <td width="250px" class="">{{ article.username }}</td>
        <td width="668px" class=""><RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">{{ article.title }}</RouterLink></td>
        <td width="202px" class="">{{ article.created_at.substring(0, 10) }}</td>
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
.category {
  background-color: #9e9c9c;
}
</style>