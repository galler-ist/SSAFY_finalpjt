<template>
  <div>
    <h1>DetailView</h1>
    <div v-if="article">
      <p>{{ article.id }}</p>
      <p>{{ article.title }}</p>
      <p>{{ article.user }}</p>
      <p>{{ article.content }}</p>
      <p>{{ article.created_at }}</p>
      <p>{{ article.updated_at }}</p>
      <p>{{ article.like }}</p>
    </div>
    <h2>Comments</h2>
    <div v-if="comments.length">
      <ul>
        <li v-for="comment in comments" :key="comment.id">
          <p>{{ comment.content }}</p>
          <small>by {{ comment.user }}</small>
          <button @click="deleteComment(comment.id)">Delete</button>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>No comments yet.</p>
    </div>

    <form @submit.prevent="addComment">
      <textarea v-model="newComment" placeholder="Write a comment..."></textarea>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const article = ref(null)
const comments = ref([])
const newComment = ref('')


onMounted(() => {
  fetchArticle()
  fetchComments()
})

const fetchArticle = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/api/v1/articles/${route.params.id}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    article.value = response.data
  } catch (error) {
    console.error(error)
  }
}

const fetchComments = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/api/v1/articles/${route.params.id}/comments/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    comments.value = response.data
  } catch (error) {
    console.error(error)
  }
}

const addComment = async () => {
  try {
    const response = await axios.post(`${store.API_URL}/api/v1/articles/${route.params.id}/comments/`, {
      content: newComment.value
    }, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    comments.value.push(response.data)
    newComment.value = ''
  } catch (error) {
    console.error(error)
  }
}

const deleteComment = async (commentId) => {
  try {
    await axios.delete(`${store.API_URL}/api/v1/comments/${commentId}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    comments.value = comments.value.filter(comment => comment.id !== commentId)
  } catch (error) {
    console.error(error)
  }
}

</script>

<style>

</style>
