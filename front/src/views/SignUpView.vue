<template>
  <h1 class="sample-text">GeumSangChu</h1>
  <div class="login ">
    <div class="card m-auto" style="width: 30rem;">
      <div class="card-body">
        <h4 class="card-title loginblank">회원가입</h4>
        <form class="card-text" @submit.prevent="signUp">
          <div class="idblank">
            <label for="username">ID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
            <input type="text" v-model.trim="username" id="username">
          </div>
          <div class="passwordblank">
            <label for="password1">PASSWORD&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
            <input type="password" v-model.trim="password1" id="password">
          </div>
          <div class="passwordblank">
            <label for="password2">PASSWORD CONFIRM&nbsp;</label>
            <input type="password" v-model.trim="password2" id="password">
          </div>
          <div class="nicknameblank">
            <label for="nickname">NICKNAME&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
            <input type="text" v-model.trim="nickname" id="nickname">
          </div>
          <div class="emailblank">
            <label for="email-id">EMAIL&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
            <input type="text" v-model.trim="emailId" id="email-id" >
          </div>
          <div class="email-domain">
          <label for="email-domain">DOMAIN</label>          
            <select v-model="emailDomain" id="email-domain" @change="checkDomain">
              <option value="">Select domain</option>
              <option value="gmail.com">gmail.com</option>
              <option value="yahoo.com">yahoo.com</option>
              <option value="naver.com">naver.com</option>
              <option value="other">직접 추가</option>
            </select>
            <input v-if="emailDomain === 'other'" type="text" v-model.trim="customDomain">
          </div>
          <button class="btn w-100 inputblank" type="submit" value="Log In"> Sign Up </button>
        </form>
        <hr>
      </div>
    </div>
  </div>

</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter.js'

const store = useCounterStore()

const username = ref('') 
const password1 = ref('')
const password2 = ref('')
const nickname = ref('')
const emailId = ref('')
const emailDomain = ref('')
const customDomain = ref('')

const signUp = function () {
  if (password1.value !== password2.value) {
    alert("비밀번호가 틀렸어!")
    return
  }

  const email = emailDomain === 'other' ? `${emailId.value}@${customDomain.value}` : `${emailId.value}@${emailDomain.value}`
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    email: email,
  }
  store.signUp(payload)
}

const checkDomain = () => {
  if (emailDomain.value !== 'ohter') {
    customDomain.value = ''
  }
}

</script>

<style>
.login {
  text-align: center;
}
.loginblank {
  padding: 2rem;
  
}
.idblank {
  padding: 1rem;
}
.passwordblank {
  padding-bottom: 1rem;
}
.inputblank {
  padding: 2rem;
}



.sample-text {
  padding: 7rem 0rem 3rem 0rem;
  text-align: center;
  font-size: 2rem;
  font-weight: bolder;
}
.login {
  text-align: center;
}
.loginblank {
  padding: 2rem;
  
}
.idblank {
  padding: 1rem;
}
.passwordblank {
  padding: 0rem 0rem 1rem 0rem;
}
.inputblank {
  padding: 2rem;
  display: flex;
}
.card-text-my {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  width:auto;
}
.form-flex {
  display: flex;
  align-items: center;
}
</style>
