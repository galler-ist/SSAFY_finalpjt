<template>
  <div>
    <div class="img-container">
      <div class="left-div">
        <RouterLink style="color: black" :to="{ name: 'HomeView' }"><img class="logo-img" src="/assets/Logo.png" alt="GSC"></RouterLink>
      </div>
      <div class="right-div">
        <div class="sub-container">
          <RouterLink class="sub-text" :to="{ name: 'BankView' }">은행찾기</RouterLink>
        </div>
        <div class="sub-container">
          <RouterLink class="sub-text" :to="{ name: 'ExchangeView' }">환율</RouterLink>
        </div>
        <div class="sub-container">
          <RouterLink class="sub-text" :to="{ name: 'DepositList' }">예적금조회</RouterLink>
        </div>
        <div class="sub-container">
          <RouterLink class="sub-text" :to="{ name: 'ArticleView' }">커뮤니티</RouterLink>
        </div>
        <div class="last-sub-container">
          <RouterLink class="sub-text" :to="{ name: 'PortfolioList' }">포트폴리오</RouterLink>
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
    background-image: url('assets/bgbg4.png');
    background-size: cover;
    background-position: center;
    width: 100%;
    height: 100vh;
    display: flex;
    position: relative;

  }


  .left-div {
    width: 66%;
    height: 100vh;
    border-right: 1px solid rgb(127, 127, 127);
  }
  .logo-img {
    width: 8rem;
    padding: 20px;
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
    border-bottom: 1px solid rgb(127, 127, 127);
    align-items: center;
  }
  .last-sub-container {
    display: flex;
    width: 100%;
    height: 20vw;
    width: 100%;
    height: 20vw;
  }
  .sub-container:hover {
    width: 100%;
    background-color: rgba(0, 0, 0, 0.4);

  }
  .last-sub-container:hover {
    width: 100%;
    background-color: rgba(0, 0, 0, 0.4);

  }
  .sub-text {
    padding: 60px 280px 60px 40px;
    text-decoration: none;
    color: rgb(255, 255, 255);
    font-weight: 1000;
    font-size: 20px;
  }
  .sub-text:hover {
    color: rgb(225, 167, 78);
  }
</style>