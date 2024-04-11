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
      <el-footer class="footer">
        <div class="footer-top">

          <!-- Column for COOLDOWN MELBOURNE -->
          <div class="footer-section"
            style="flex: 1; padding-right: 20px; border-right: 2px solid white; margin-right: 20px; height: 150px; display: flex; flex-direction: column; justify-content: space-between;">
            <h2 style="color: white; margin-top: 0;">COOLDOWN MELBOURNE</h2>
            <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-around;">
              <p style="color: white;"><i class="el-icon-location"></i> Wellington Rd, Clayton, VIC 3800</p>
              <p style="color: white;"><i class="el-icon-phone"></i> 0424281773</p>
              <p style="color: white;"><i class="el-icon-message"></i> info@cooldownmelbourne.com</p>
            </div>
          </div>

          <!-- Column for USEFUL LINKS -->
          <div class="footer-section"
            style="flex: 1; padding-right: 20px; border-right: 2px solid white; margin-right: 20px; height: 150px; display: flex; flex-direction: column; justify-content: space-between;">
            <h2 style="color: white; margin-top: 0;">USEFUL LINKS</h2>
            <ul
              style="list-style: none; padding: 0; color: white; flex-grow: 1; display: flex; flex-direction: column; justify-content: space-around;">
              <li>Home</li>
              <li>About Us</li>
              <li>Service</li>
              <li>Terms of Service</li>
              <li>Privacy Policy</li>
            </ul>
          </div>

          <!-- Column for FOLLOW US -->
          <div class="footer-section"
            style="flex: 1; height: 150px; display: flex; flex-direction: column; justify-content: space-between;">
            <h2 style="color: white; margin-top: 0;">FOLLOW US</h2>
            <div class="social-icons"
              style="flex-grow: 1; display: flex; flex-direction: column; justify-content: center;">
              <i class="el-icon-facebook" style="color: white;"></i>
              <i class="el-icon-instagram" style="color: white;"></i>
              <!-- Replace placeholder with actual icon class -->
              <i class="custom-icon-x" style="color: white;"></i> <!-- Placeholder for the actual icon -->
              <i class="el-icon-linkedin" style="color: white;"></i>
              <i class="el-icon-tiktok" style="color: white;"></i>
            </div>
          </div>

        </div>

        <!-- Separate line for Copyright notice -->
        <!-- <div class="footer-bottom" style="background-color: #4CAF50; color: white; text-align: center; padding: 10px;"> -->
        <div class="footer-bottom">
          <p>© Copyright Team Colon D All Rights Reserved | Designed by Monash IE Team TA 14</p>
        </div>
      </el-footer>



    </el-container>
  </div>
</template>

<script>
export default {
  name: 'AboutUs'
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
