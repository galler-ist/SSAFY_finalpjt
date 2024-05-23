<template>
  <!-- <div>
    <h1 class="sample-text">GeumSangChu</h1>
    <div class="login">
      <div class="card m-auto" style="width: 30rem;">
        <div class="card-body">
          <h4 class="card-title loginblank">Log In</h4>
          <form class="card-text-my form-flex" @submit.prevent="logIn">
            <div class="idblank">
              <label for="username">ID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
              <input type="text" v-model.trim="username" id="username">
            </div>
            <div class="passwordblank">
              <label for="password">PASSWORD&nbsp;</label>
              <input type="password" v-model.trim="password" id="password">
            </div>
            <button class="btn w-100 inputblank" type="submit" value="Log In"> Log In </button>
          </form>
          <hr>

        </div>
      </div>
    </div>
  </div> -->
  <div>
    <div class="img-container">
      <div class="left-div">
        <RouterLink class="logo-text" style="color: black" :to="{ name: 'HomeView' }">GSC</RouterLink>
      </div>
      <div class="right-div">
        <div class="">
          <h1 class="login-text ">로그인</h1><hr>
          <form class="" @submit.prevent="logIn">
            <input class="input-box" style="margin-top: 20px" type="text" v-model.trim="username" id="username" placeholder="아이디를 입력하세요"><br>
            <input class="input-box" style="margin-bottom: 20px" type="password" v-model.trim="password" id="password" placeholder="비밀번호를 입력하세요"><hr>
            <button class="login-button" type="submit" value="Log In"> Log In </button><br>
            <button class="signup-button">
              <RouterLink style="text-decoration: none; color: black;" :to="{name:'SignUpView'}">Sign Up</RouterLink>
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router';

const username = ref(null)
const password = ref(null)
const store = useCounterStore()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
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
  width: 66%;
  height: 100vh;
  border-right: 1px solid white;
}
.logo-text {
  color: white;
  font-size: 2rem; 
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  text-decoration: none;
  padding: 30px;
}
.right-div {
  width: 34%;
  height:100vh;
  display: flex;
  flex-direction: column;
  background-color: white;
  justify-content: center;
  align-items: center;
}
.login-text {
  width: 18rem;
  margin-bottom: 50px;
}
.input-box {
  width:100%;
  height: 40px;
  margin: 5px;
  margin-left: 0px;
 
}
.login-button {
  width: 100%;
  height: 40px;
  margin: 5px;
  margin-top: 20px;
  margin-left: 0px;
  background-color: black;
  color: white;
}
.signup-button {
  width: 100%;
  height: 40px;
  margin: 5px;
  margin-left: 0px;
  text-decoration: none;
  color: black;
  background-color: white;
}
</style>
