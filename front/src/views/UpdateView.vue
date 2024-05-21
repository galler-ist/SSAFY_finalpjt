<template>
  <div>
    <h1 class="sample-text">게시글 수정</h1>
    <form @submit.prevent="updateArticle">
    <div class="article-container">
        <div class="title-container">
          <label for="title">제목 : </label>
          <input class="title-text" type="text" v-model.trim="title" id="title">
        </div>
        <div class="content-container">
          <label for="content">내용</label>
          <textarea class="content-text" v-model.trim="content" id="content"></textarea>
        </div>
        <button class="btn w-100" type="submit" value="수정하기">수정하기</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const title = ref('')
const content = ref('')

onMounted(() => {
  fetchArticle()
})

const fetchArticle = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/api/v1/articles/${route.params.id}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    const article = response.data
    title.value = article.title
    content.value = article.content
  } catch (error) {
    console.error(error)
  }
}

const updateArticle = async () => {
  try {
    await axios.put(`${store.API_URL}/api/v1/articles/${route.params.id}/update/`, {
      title: title.value,
      content: content.value
    }, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    router.push({ name: 'DetailView', params: { id: route.params.id } })
  } catch (error) {
    console.error(error)
  }
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
