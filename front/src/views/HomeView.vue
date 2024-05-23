<template>
  <div>
    <div class="img-container">
      <div class="left-div">
        <RouterLink class="logo-text" style="color: black" :to="{ name: 'HomeView' }"><img class="logo-img" src="/assets/Logo.png" alt="GSC"></RouterLink>
      </div>
      <div class="right-div">
        <div class="sub-container">
          <RouterLink class="sub-text" :to="{ name: 'BankView' }">Bank</RouterLink>
        </div>
        <div class="sub-container">
          <RouterLink class="sub-text" :to="{ name: 'ExchangeView' }">Exchange</RouterLink>
        </div>
        <div class="sub-container">
          <RouterLink class="sub-text" :to="{ name: 'DepositList' }">Finance</RouterLink>
        </div>
        <div class="sub-container">
          <RouterLink class="sub-text" :to="{ name: 'ArticleView' }">Articles</RouterLink>
        </div>
        <div class="last-sub-container">
          <h3>5번</h3>
        </div>
      </div>
    </div>
    <div>
    </div>
  </div>
</template>

<script setup>

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
    filter: brightness(90%);
  }

  .left-div {
    width: 66%;
    height: 100vh;
    border-right: 1px solid lightgray;
  }
  .logo-text {
    color: white;
    font-size: 2rem; 
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    text-decoration: none;
    padding: 30px;
  }
  .logo-img {
    width: 8rem;
    padding-top: 20px;
  }
  .right-div {
    width:34%;
    height: 100vh;
    color: white;
    color: lightgray;
    font-size: 1rem;
    display: flex;
    flex-direction: column;
  }
  .sub-container {
    display: flex;
    width: 100%;
    height: 20vw;
    border-bottom: 1px solid lightgray;
    align-items: center;
  }
  .last-sub-container {
    width: 100%;
    height: 20vw;
  }
  .sub-container:hover {
    width: 100%;
    background-color: rgba(55, 54, 54, 0.5);
    color: beige;
  }
  .sub-text {
    padding: 60px 280px 60px 40px;
    text-decoration: none;
    color: gray;
    font-weight: 700;
    font-size: 1000;
  }
  .sub-text:hover {
    color: rgb(187, 138, 47);
  }
</style>