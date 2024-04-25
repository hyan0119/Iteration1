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
  name: 'MyPlants',
  components: {
    footerColumn,
    HeaderNavigation
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