<template>
  <div class="row">
    <div class="col-12 article-container">
      <div class="article-table">
        <h1 class="sample-text"></h1>
        <RouterLink class="link" :to="{ name: 'ArticleView' }">자유게시판</RouterLink>
        <div v-if="article">
        <h2>{{ article.title }}</h2>
        <hr>
        <p>{{ article.username }}</p>
        <p>{{ article.created_at.substring(0, 10) }}</p>
        <hr>
        <p>{{ article.content }}</p>
        <!-- <p>{{ article.like }}</p> -->
        <!-- <button class="btn" @click="toggleLike">
          {{ article.like ? 'Unlike' : 'Like' }}
        </button> -->
        
      </div>
      <hr>
      <div>
        <div v-if="comments.length">
          <ul v-for="comment in comments" :key="comment.id">

            <small>{{ comment.user }}</small>
            <button class="btn btn-delete comment-delete" @click="deleteComment(comment.id)">X</button>
            <p>{{ comment.content }}</p>
            <hr>

          </ul>
        </div>
        <div v-else>
          <p>No comments yet.</p>
        </div>
        <div>
          <form  class="comment-container" @submit.prevent="addComment">
            <textarea class="comment" v-model="newComment" placeholder="Write a comment..."></textarea>
            <button class="btn-comment" style="background-color: #ffffff" type="submit">Submit</button>
          </form>
        </div>
      </div>
      <button class="btn" style="background-color: #ffffff" v-if="isOwner" @click="goToUpdateView">Update Article</button>
      <button class="btn" v-if="isOwner" @click="deleteArticle">Delete Article</button>
    </div>
  </div>
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
    isOwner.value = article.value.username === store.username
  })
  .catch(error => {
    console.error(error)
  })
}


const deleteArticle = () => {
  axios.delete(`${store.API_URL}/api/v1/articles/${route.params.id}/`, {
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then(() => {
    router.push({ name: 'HomeView' })
  })
  .catch(error => {
    console.error(error)
    console.log(route.params.id)
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
    console.log(commentId)
  })
  .catch(error => {
    console.error(error)
  })
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


const goToUpdateView = () => {
  router.push({ name: 'UpdateView', params: { id: route.params.id } })
}

// const toggleLike = () => {
//   axios.patch(`${store.API_URL}/api/v1/articles/${route.params.id}/`, {
//     like: !article.value.like
//   }, {
//     headers: {
//       Authorization: `Token ${store.token}`
//     }
//   })
//   .then(response => {
//     article.value.like = true
//   })
//   .catch(error => {
//     console.error(error)
//   })
// }

</script>

<style>
.img {
  width: 60%;
  height: 20rem;
  margin-left: 20%;
}
.comment {
  width: 100%;
  padding: 10px;
  border-radius: 8px 0px 0px 8px;
}
.sample-text {
  padding: 5rem 0;
  text-align: center;
  font-size: 2rem;
}
.article-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 2rem auto;
  width: 90%;
}
.article-table {
  width: 65%;
  border-collapse: collapse;
  margin-bottom: 20px;
}
.link {
  font-size: 10px;
  text-decoration: none;
}
.comment-container {
  display: flex;
  border: 1px solid gray;
  border-radius: 10px ;

}
.btn-comment {

border: 1px;
border-radius: 0px 8px 8px 0px;
}
.btn-delete {
font:50;
}
.comment-delete {
  text-align: right;
}
</style>
