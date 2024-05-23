import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const username = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  const router = useRouter()

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(response => {
        articles.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const signUp = async function (payload) {
    const { username, password1, password2, nickname, email } = payload
    try {
      const response = await axios.post(`${API_URL}/accounts/signup/`, {
        username, password1, password2, nickname, email
      })
      console.log('회원가입 성공!')
      const password = password1

      logIn({ username, password })
    } catch (error) {
      console.log('회원가입 실패:', error)
    }
  }

  // const signUp = function (payload) {
  //   const { username, password1, password2, nickname, email } = payload

  //   axios({
  //     method: 'post',
  //     url: `${API_URL}/accounts/signup/`,
  //     data: {
  //       username, password1, password2, nickname, email
  //     }
  //   })
  //     .then((response) => {
  //     console.log('회원가입 성공!')
  //     const password = password1

  //     logIn({ username, password })
  //     })
  //     .catch((error) => {
  //      console.log('뭔 error')
  //     })
  //  }

  const logIn = async function (payload) {
    // 1. 사용자 입력 데이터를 받아
    const { username: loginUser, password } = payload
    // 2. axios로 django에 요청을 보냄
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username: loginUser, password
      }
    })
      .then((response) => {
        token.value = response.data.key
        username.value = loginUser
        console.log('로그인 성공:', loginUser)
        router.push({ name : 'HomeView' })
      })
      .catch((error) => {
        console.log(error)
      })
  }
  const logOut = function () {
    token.value = null
    username.value = null
    router.push({ name: 'LogInView' })
  }

  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin, logOut, username }
}, { persist: true })
