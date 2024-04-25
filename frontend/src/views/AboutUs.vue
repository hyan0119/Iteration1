<template>
  <div class="common-layout">
    <el-container>
        <div>
              <HeaderNavigation/>
          </div>
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
import HeaderNavigation from "@/components/HeaderNavigation.vue";
export default {
  name: 'AboutUs',
  components: {
    footerColumn,
    HeaderNavigation
  },
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

.plant_planner {
  text-align: center;
  padding: 100px 0;
  background-color: #f4f4f4;
  background-image: url('../assets/plant_planner_bg.jpg');

  background-size: contain;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  min-height: 100vh;
  /* 确保至少有100%视口高度 */
  width: 100vw;
  /* 确保宽度覆盖整个视口宽度 */
}
</style>
<style src="./style.css"></style>
