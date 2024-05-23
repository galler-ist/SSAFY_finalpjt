<template>
  <!-- <h1 class="sample-text">GeumSangChu</h1>
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
            <label for="password">PASSWORD&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
            <input type="password" v-model.trim="password1" id="password">
          </div>
          <div class="passwordblank">
            <label for="password">PASSWORD CONFIRM&nbsp;</label>
            <input type="password" v-model.trim="password2" id="password">
          </div>
          <button class="btn w-100 inputblank" type="submit" value="Log In"> Sign Up </button>
        </form>
        <hr>
      </div>
    </div>
  </div> -->

  <div class="img-container">
    <div class="left-div">
        <RouterLink class="logo-text" style="color: black" :to="{ name: 'HomeView' }">GSC</RouterLink>
    </div>
    <div class="middle-div">
      <div>
        <h1 class="login-text">회원가입</h1><hr>
        <form class="" @submit.prevent="signUp">
          <input class="input-box" style="margin-top: 20px" type="text" v-model.trim="username" id="username" placeholder="아이디를 입력하세요"><br>
          <input class="input-box" type="password" v-model.trim="password1" id="password" placeholder="비밀번호를 입력하세요">
          <input class="input-box" style="margin-bottom: 20px" type="password" v-model.trim="password2" id="password" placeholder="비밀번호를 확인하세요"><hr>
          <button class="signup-button" type="submit"> Sign Up </button><br>
        </form>
      </div>
    </div>
  </div>






</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const username = ref(null) 
const password1 = ref(null)
const password2 = ref(null)
const store = useCounterStore()

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
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
.middle-div {
  width: 34%;
  height:100vh;
  display: flex;
  flex-direction: column;
  background-color: white;
  justify-content: center;
  align-items: center;
}
.login-text {
  width: 15rem;
  margin-bottom: 50px;
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
