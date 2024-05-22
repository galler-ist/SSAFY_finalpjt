<template>
  <div>
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
