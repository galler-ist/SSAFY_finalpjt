<template>
  <div class="img">
    <h1>게시판</h1>
    <RouterLink :to="{ name: 'CreateView' }">
      [CREATE]
    </RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useCounterStore()

onMounted(() => {
  store.getArticles()
})

</script>

<style>
.img {
  position:relative;
  width: 80%;
  height: 20rem;
  margin-left: 10%;
}
.background {
    background-color: #F6F1FF;
}
</style>
