<template>
  <div class="img">
    <div v-if="article">
      <h2>{{ article.title }}</h2>
      <p>{{ article.username }}</p>
      <p>{{ article.created_at }}</p>
      <hr>
      <p>{{ article.content }}</p>
      <p>{{ article.like }}</p>
    </div>
    <button class="btn"><RouterLink :to="{ name: 'ArticleView' }">목록</RouterLink></button>
    <button class="btn" v-if="!isOwner" @click="goToUpdateView">Update Article</button>
    <button class="btn" v-if="!isOwner" @click="deleteArticle">Delete Article</button>
    <hr>
    <div v-if="comments.length">
      <ul>
        <li v-for="comment in comments" :key="comment.id">
          <p>{{ comment.content }}</p>
          <small>by {{ comment.user }}</small>
          <button class="btn" @click="deleteComment(comment.id)">Delete</button>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>No comments yet.</p>
    </div>

    <form @submit.prevent="addComment">
      <textarea class="comment" v-model="newComment" placeholder="Write a comment..."></textarea>
      <br>
      <button class="btn" type="submit">Submit</button>
    </form>
    
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, watch } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const comments = ref([])
const newComment = ref('')
const isOwner = ref(false)
watch(() => store.username, (newUsername) => {
  if (article.value) {
    // console.log(store.username)
    isOwner.value = article.value.username === newUsername
  }
})
onMounted(() => {
  fetchArticle()
  fetchComments()
})

const fetchArticle = () => {
  axios.get(`${store.API_URL}/api/v1/articles/${route.params.id}/`, {
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then(response => {
    article.value = response.data
    // const articleUser = String(article.value.user).trim().toLowerCase()
    // const storeUser = store.username.trim().toLowerCase()
    // isOwner.value = articleUser === storeUser
    console.log(article.value.username)
    console.log(store.username) // 이거 로그인에서 넘어오는 username인데 왜 undefined로 나오지????????? 이게 안되서 update 버튼이 안나오는 거같은데
    isOwner.value = article.value.username === store.username
  })
  .catch(error => {
    console.error(error)
  })
}

const deleteArticle = async () => {
  try {
    await axios.delete(`${store.API_URL}/api/v1/articles/${route.params.id}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    router.push({ name: 'HomeView' }) // 글 삭제 후 홈으로 이동
  } catch (error) {
    console.error(error)
  }
}

const fetchComments = () => {
  axios.get(`${store.API_URL}/api/v1/articles/${route.params.id}/comments/`, {
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then(response => {
    comments.value = response.data
  })
  .catch(error => {
    console.error(error)
  })
}

const addComment = () => {
  axios.post(`${store.API_URL}/api/v1/articles/${route.params.id}/comments/`, {
    content: newComment.value
  }, {
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then(response => {
    comments.value.push(response.data)
    newComment.value = ''
  })
  .catch(error => {
    console.error(error)
  })
}

const deleteComment = (commentId) => {
  axios.delete(`${store.API_URL}/api/v1/comments/${commentId}/`, {
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then(() => {
    comments.value = comments.value.filter(comment => comment.id !== commentId)
  })
  .catch(error => {
    console.error(error)
  })
}

const goToUpdateView = () => {
  router.push({ name: 'UpdateView', params: { id: route.params.id } })
}

</script>

<style>
.img {
  position:relative;
  width: 60%;
  height: 20rem;
  margin-left: 20%;
}
.comment {
  width: 60%;
}
</style>
