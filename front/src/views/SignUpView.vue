<template>
  <!-- <h1 class="sample-text">GeumSangChu</h1>
  <div class="login ">
    <div class="card m-auto" style="width: 30rem;">
      <div class="card-body">
        <h4 class="card-title loginblank">회원가입</h4>
        <form class="card-text" @submit.prevent="signUp">
          <div class="idblank">
            <label for="last_name">Last name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
            <input type="text" v-model.trim="last_name" id="last_name">
          </div>
          <div class="first_name">
            <label for="username">First name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
            <input type="text" v-model.trim="first_name" id="first_name">
          </div>
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
  </div> -->
  
  <div class="img-container">
    <div class="left-div">
      <RouterLink style="color: black" :to="{ name: 'HomeView' }"><img class="logo-text" src="/assets/Logo.png" alt="GSC"></RouterLink>
    </div>
    <div class="middle-div">
      <h1 class="login-text">회원가입</h1><hr>
      <div class="low-div">
        <div class="left-div">
          <p class="text">아이디</p>
          <p class="text">성</p>
          <p class="text">이름</p>
          <p class="text">비밀번호</p>
          <p class="text">비밀번호 확인</p>
          <p class="text">닉네임</p>
          <p class="text">E-mail</p>
        </div>
        <div class="rigth-div">
          <form class="" @submit.prevent="signUp">
            <input class="input-box" type="text" v-model.trim="username" id="username" placeholder="아이디">
            <input class="input-box" type="text" v-model.trim="last_name" id="last_name" placeholder="성">
            <input class="input-box" type="text" v-model.trim="first_name" id="first_name" placeholder="이름">
            <input class="input-box" type="password" v-model.trim="password1" id="password" placeholder="비밀번호">
            <input class="input-box" type="password" v-model.trim="password2" id="password" placeholder="비밀번호 확인">
            <input class="input-box" type="nickname" v-model.trim="nickname" id="nickname" placeholder="닉네임">
            <input class="input-box" type="emailId" v-model.trim="emailId" id="email-Id" placeholder="이메일">
            <div class="email-domain">         
                <select class="input-box" v-model="emailDomain" id="email-domain" @change="checkDomain">
                  <option value="">-------------</option>
                  <option value="gmail.com">gmail.com</option>
                  <option value="yahoo.com">yahoo.com</option>
                  <option value="naver.com">naver.com</option>
                  <option value="other">직접 추가</option>
                </select>
                <input v-if="emailDomain === 'other'" type="text" v-model.trim="customDomain">
              </div>
            <button class="signup-button" type="submit">Sign Up</button><br>
          </form>
        </div>
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
const last_name = ref('')
const first_name = ref('')

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
    last_name: last_name,
    first_name: last_name
  }
  store.signUp(payload)
}

const checkDomain = () => {
  if (emailDomain.value !== 'ohter') {
    customDomain.value = ''
  }
}

</script>

<style scoped>
.img-container {
  background-image: url('assets/bgbg2.png');
  background-size: cover;
  background-position: center;
  width: 100%;
  height: 100vh;
  display: flex;
  position: relative;
  /* filter: brightness(70%); */
}

.left-div {
  width: 32%;
  text-align: left;
  border-right: 1px solid white;
  /* padding-top: 20px; */
  padding-bottom: 60px;
}
.logo-text {
  width: 8rem;
  padding: 20px;
}
.middle-div {
  width: 34%;
  height:100vh;
  display: flex;
  flex-direction: column;
  background-color: white;
  justify-content: center;
  align-items: center;
}
.low-div {
  width:90%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.login-text {
  width: 15rem;
  margin-bottom: 50px;
  display: flex;
  flex-wrap: wrap;
  margin-left: 80px;
}
.input-box {
  width:100%;
  height: 40px;
  margin: 5px;
  margin-left: 0px;
}
.signup-button {
  width: 100%;
  height: 40px;
  margin: 5px;
  margin-top: 20px;
  margin-left: 0px;
  background-color: black;
  color: white;
}
.text {
  display: flex;
  flex-direction: row;
  padding-top: 10px;
}
.left-div {
  width: 30%;
  margin-bottom: 70px;
}
.rigth-div {
  width: 70%;
}
/* .login-form {
  width: 100%;
} */

/* .login {
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
} */
</style>
