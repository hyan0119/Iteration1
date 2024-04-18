<template>
  <div class="common-layout">
    <el-container>
      <el-header class="header">
        <div class="menu-container">
          <el-menu mode="horizontal" class="menu left-menu" background-color="transparent">
            <el-menu-item index="0" class="menu-item logo-item">
              <router-link to="/">
                <img src="@/assets/logo.png" alt="Logo" class="logo" />
              </router-link>
            </el-menu-item>
            <el-menu-item index="1" class="menu-item home">
              <router-link to="/">Home</router-link>
            </el-menu-item>
          </el-menu>

          <el-menu mode="horizontal" class="menu right-menu" background-color="transparent">
            <el-menu-item index="2" class="menu-item">
              <router-link to="/uhi-map">UHI MAP</router-link>
            </el-menu-item>
            <el-menu-item index="3" class="menu-item">
              <router-link to="/plant-planner">PLANT PLANNER</router-link>
            </el-menu-item>
            <el-menu-item index="4" class="menu-item">
              <router-link to="/my-plants">MY PLANTS</router-link>
            </el-menu-item>
            <el-menu-item index="5" class="menu-item">
              <router-link to="/info-page">INFO</router-link>
            </el-menu-item>
            <el-menu-item index="6" class="menu-item">
              <router-link to="/about-us">ABOUT US</router-link>
            </el-menu-item>
          </el-menu>
        </div>
      </el-header>
      <div class="filler"></div>
      <el-main class="main-content">
        <div class="coming-soon-container">
          <img src="@/assets/comingsoon.png" alt="Coming Soon" />
        </div>
      </el-main>
      <footer-column></footer-column>
    </el-container>
  </div>
</template>

<script>
import footerColumn from "../components/footer-column";
export default {
  name: 'MyPlants',
  components: {
    footerColumn
  }
}
</script>

<style scoped>
.coming-soon-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 50vh;
  background-color: #f4f4f400;
}

.coming-soon-container img {
  max-width: 50%;
  /* Adjust as needed */
  max-height: 50%;
  /* Adjust as needed */
}


</style>
<style src="./style.css"></style>