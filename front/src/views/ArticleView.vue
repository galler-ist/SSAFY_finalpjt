<template>
  <div class="img">
    <h1>게시판</h1>
    <RouterLink :to="{ name: 'CreateView' }">
      글쓰기
    </RouterLink>
    <thead>
      <tr class="category">
        <th width="250px" class="">작성자</th>
        <th width="668px" class="">제목</th>
        <th width="202px" class="">날짜</th>
      </tr>
    </thead>
    <ArticleList />
    <input class="search-input" type="text" placeholder="작성자, 제목을 입력하세요">
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
.search-input {
  display: block;
  padding: 4px 8px;
  margin: 10px auto;
  width: 320px;
  font-size: 16px;
  outline: none;
}

</style>
