<template>
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

      <el-menu class="menu right-menu" background-color="transparent">
        <el-menu-item index="2" class="menu-item">
          <router-link to="/uhi-map">UHI MAP</router-link>
        </el-menu-item>
        <el-menu-item index="3" class="menu-item">
          <router-link to="/plant-planner">PLANT PLANNER</router-link>
        </el-menu-item>
        <el-menu-item index="4" class="menu-item">
          <router-link to="/my-plants">COOL CITY</router-link>
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
</template>

<script>
export default {
  name: 'HeaderNavigation'
}
</script>

<style scoped>

</style>
