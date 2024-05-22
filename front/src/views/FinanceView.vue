<template>
  <div class="image-container bg-image">
    <img class="bg w-100 exchange-bg " src="/assets/saving_bg.png">
    <h1 class="title-container">Finance Products</h1>
  </div>
    <div>
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
    position: absolute;
    top: 20%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    font-weight: 500;
    font-size: 2rem;
    text-align: center;
    z-index: 1;
  }
  .exchange-bg {
  width: 100%;
  height: 18rem;
  opacity: 0.7;
}

.image-container::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
}
.bg-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  mask-image: linear-gradient(to bottom, rgba(0, 0, 0, 1), rgba(0, 0, 0, 0));
  /* or use -webkit-mask-image for better compatibility with some browsers */
  -webkit-mask-image: linear-gradient(to bottom, rgba(0, 0, 0, 1), rgba(0, 0, 0, 0));
}
  </style>
  