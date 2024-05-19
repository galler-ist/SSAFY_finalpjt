<template>
  <div class="login" style="background-color : #F6F1FF">
    <div class="card m-auto" style="width: 30rem;">
      <div class="card-body">
        <h5 class="card-title loginblank">Log In</h5>
        <form class="card-text" @submit.prevent="logIn">
          <div class="idblank">
            <label for="username">ID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
            <input type="text" v-model.trim="username" id="username">
          </div>
          <div class="passwordblank">
            <label for="password">PASSWORD&nbsp;</label>
            <input type="password" v-model.trim="password" id="password">
          </div>
          <input class="btn btn-primary w-100 inputblank" type="submit" value="Log In">
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
