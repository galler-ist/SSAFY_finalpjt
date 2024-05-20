<template>
  <div class="login " style="background-color : #F6F1FF">
    <div class="card m-auto" style="width: 30rem;">
      <div class="card-body">
        <h5 class="card-title loginblank">회원가입</h5>
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
          <input class="btn btn-primary w-100 inputblank" type="submit" value="Sign In">
        </form>
        <hr>
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
</style>
