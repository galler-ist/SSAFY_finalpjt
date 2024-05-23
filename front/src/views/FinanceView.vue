<template>
  <!-- <div class="image-container bg-image">
    <img class="bg w-100 exchange-bg " src="/assets/saving_bg.png">
    <h1 class="title-container">예적금 조회</h1>
  </div>
    <div>
    </div> -->
  <div class="top-flex">
    <div class="blank-div">
      
    </div>
    <div>
      <h1 class="title-container">예적금 조회</h1>
      <nav class="nav-sticky nav-container">
        <RouterLink to="/finance/deposit">예금</RouterLink>
        <RouterLink to="/finance/saving">적금</RouterLink>
      </nav>
      <div class="main-container">
        <RouterView></RouterView>
      </div>
    </div>
  </div>

</template>
  
  <script>
  export default {
    name: 'FinanceView'
  }
  </script>
  
  <style scoped>

  .title-container {

    display: flex;
    justify-content: center;
    padding-top: 15vh;
    width: 100%;
    height: 30vh;
    color: black;
    font-weight: 700;
  }
  .main-container {
    background-color: rgb(248, 248, 248);
    border-top: 1px solid rgb(230, 230, 230);
  }
  .nav-sticky {
    position: sticky;
    display: flex;
    justify-content: center;
    align-items: center;
    top:17px;
    width: 100%;
  }
  .nav-container {
    margin: 20px;
    text-align: center;
    /* position: sticky; */
  }
  nav a {
    font-size: 20px;
    text-decoration: none;
    color: black;
    margin: 0px 33px;
  }
  
  nav a.router-link-exact-active {
    font-weight: bold;
    border-bottom: 3px solid rgba(241, 139, 49, 0.884);
  }

  .exchange-bg {
  width: 100%;
  height: 18rem;
  opacity: 0.7;
  }

  </style>
  