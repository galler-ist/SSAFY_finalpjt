<template>
    <div>
      <h1 class="title-container">Finance Products</h1>
      <nav>
        <RouterLink to="/finance/deposit">예금</RouterLink>
        <RouterLink to="/finance/saving">적금</RouterLink>
      </nav>
      <RouterView></RouterView>
    </div>
  </template>
  
  <script>
  export default {
    name: 'FinanceView'
  }
  </script>
  
  <style scoped>
  nav {
    margin-bottom: 20px;
    text-align: center;
    font-size: 20px;
  }
  
  nav a {
    margin-right: 10px;
    text-decoration: none;
    color: #42b983;
  }
  
  nav a.router-link-exact-active {
    font-weight: bold;
  }
  .title-container {
    padding: 7rem 0rem 3rem 0rem;
    text-align: center;
    font-size: 2rem;
    font-weight: bolder;
  }
  </style>
  