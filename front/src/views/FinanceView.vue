<template>
    <div>
      <h1>Finance Products</h1>
      <nav>
        <RouterLink to="/finance/deposit">Deposits</RouterLink>
        <RouterLink to="/finance/saving">Savings</RouterLink>
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
  }
  
  nav a {
    margin-right: 10px;
    text-decoration: none;
    color: #42b983;
  }
  
  nav a.router-link-exact-active {
    font-weight: bold;
  }
  </style>
  