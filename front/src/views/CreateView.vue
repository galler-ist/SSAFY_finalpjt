<template>
  <div>
    <h1 class="sample-text">게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <div class="article-container">
        <div class="title-container">
          <label for="title">제목 : </label>
          <input class="title-text" type="text" v-model.trim="title" id="title">
        </div>
        <div class="content-container">
          <label for="content">내용</label>
          <textarea class="content-text" v-model.trim="content" id="content"></textarea>
        </div>
        <button class="btn title-text" type="submit">글쓰기</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const title = ref(null)
const content = ref(null)
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      // console.log(response.data)
      router.push({ name: 'ArticleView' })
    })
    .catch((error) => {
      console.log('error')
    })
}

</script>

<style scoped>
.article-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0 auto;
  padding:0;
  width: 65%;
}
.sample-text {
  padding: 7rem 0rem 3rem 0rem;
  text-align: center;
  font-size: 2rem;
  font-weight: bolder;
}
.title-container {
  width:100%;
  padding: 1rem 0rem;
}
.title-text {
  width: 90%;
}
.content-container {
  width:100%;
}
.content-text {
  width: 100%;
  height: 30rem;
}
</style>
