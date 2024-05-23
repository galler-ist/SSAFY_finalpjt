
<template >
  <div>
    <div class="">
      <h1 class="title-container">게시판</h1>
    </div>
    <div class="main-container">
      <div class="article-container">
        <div class="article-table cate">
          <h5 class="title-cate">제목</h5>
          <h5 class="username-cate">작성자</h5>
          <h5 class="dates-cate">날짜</h5>
        </div>
          
        <ArticleList />
        <input class="search-input" type="text" placeholder="작성자, 제목을 입력하세요">
        <RouterLink :to="{ name: 'CreateView' }" class="create-link">
          글쓰기
        </RouterLink>
      </div>
    </div>
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

<style scoped>

.title-container {
  display: flex;
  justify-content: center;
  padding-top: 15vh;
  width: 100%;
  height: 30vh;
  color: black;
  font-weight: 700;
}
.main-container {
  background-color: rgb(248, 248, 248);
  border-top: 1px solid rgb(230, 230, 230);
}

.search-input {
  display: block;
  padding: 8px 12px;
  margin: 20px auto;
  width: 80%;
  max-width: 600px;
  font-size: 16px;
  outline: none;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.article-bg {
  height: 20rem;
  opacity: 0.7;
}

.overlay {
  position: absolute;
  top: 20%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-weight: 800;
  font-size: 2rem;
  text-align: center;
}

.article-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0 auto;
  padding:30px 0px;
  width: 65%;
}

.article-table {
  width: 100%;
  display:flex;
  border-collapse: collapse;

}

.title-cate {
  width: 60%;
}

.username-cate {
  width: 20%;
}

.date-cate {
  width: 20%;
}

.cate {
  margin:10px;
  padding:1rem;
  border-bottom: 2px solid rgb(166, 166, 166);
  border-top: 2px solid rgb(166, 166, 166);
}

.cate th {
  padding: 12px 8px;
  text-align: left;
  font-size: 1.2rem;
  color: #333;
}

.article-table th, .article-table td {
  padding: 12px 8px;
  border-bottom: 1px solid #ddd;
}

.sample-text {
  padding: 7rem 0;
  text-align: center;
  font-size: 2rem;
  font-weight: bolder;
}

.create-link {
  display: block;
  text-align: center;
  padding: 10px 20px;
  margin: 20px auto;
  width: 150px;
  background-color: rgba(241, 139, 49, 0.884);
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.create-link:hover {
  background-color: rgba(195, 112, 39, 0.84);
  color: white;;
}
</style>
