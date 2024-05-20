<template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit.prevent="updateArticle">
      <div>
        <label for="title">제목 : </label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용 : </label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit" value="수정하기">
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

<style>
/* Add your styles here */
</style>
