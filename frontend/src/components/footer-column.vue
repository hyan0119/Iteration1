<template>
  <el-footer class="footer">
    <el-row class="footer-top" >
      <el-col :span="8" class="footer-section">
          <h3 class="el-typography">COOLDOWN MELBOURNE</h3>
          <el-link type="primary" underline="false">
            <i class="el-icon-location"></i>
            <span>Wellington Rd, Clayton, VIC 3800</span>
          </el-link>
          <el-link type="primary" underline="false">
            <i class="el-icon-phone"></i>
            <span>0424281773</span>
          </el-link>
          <el-link type="primary" underline="false">
            <i class="el-icon-message"></i>
            <span>info@cooldownmelbourne.com</span>
          </el-link>
      </el-col>

      <el-col :span="8" class="footer-section">
          <h3 class="el-typography">USEFUL LINKS</h3>
          <el-link type="primary" underline="false">Home</el-link>
          <el-link type="primary" underline="false">About Us</el-link>
          <el-link type="primary" underline="false">Privacy Policy</el-link>
      </el-col>

      <el-col :span="8" class="footer-section">
          <h3 class="el-typography">FOLLOW US</h3>
          <!-- ...你的社交媒体图标... -->
          <div class="footer-icons">
            <img :src="require('@/assets/footer/img-1.png')" class="img">
            <img :src="require('@/assets/footer/img-2.png')" class="img">
            <img :src="require('@/assets/footer/img-3.png')" class="img">
            <img :src="require('@/assets/footer/img-4.png')" class="img">
            <img :src="require('@/assets/footer/img-5.png')" class="img">
          </div>
      </el-col>
    </el-row>

    <div class="footer-bottom">
      <p>© Copyright Team Colon D All Rights Reserved | Designed by Monash IE Team TA 14</p>
    </div>
  </el-footer>
</template>

<script>
export default {
  name: 'footer-column',
  props: { }
}
</script>

<style scoped>
  .footer-top {
      display: flex;
      background-color: #4CAF50;
      padding: 8vh;
      align-items: center;
  }

  .footer-bottom {
      background-color: rgb(28, 61, 52);
      color: white;
      text-align: center;
      padding: 10px;
  }

  .el-typography {
      color: white;
      text-align: left;
      /* 可以添加更多排版样式，如字体大小、行高等 */
  }

  .footer-section {
      flex-grow: 1; /* 添加这个属性 */
      padding: 20px 20px 20px 6vw;
      border-right: 2px solid white;
      height: auto;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      color: white;
  }
  .footer-section el-link{
    text-align: left;
  }
  .footer-section p{
    text-align: left;
  }
  .footer-section h2{
      text-align: center;
  }
  .footer-section:last-child {
      border-right: none;
      margin-right: 0;
  }

  .footer-icons{
      display: flex;
      justify-content: left;
  }
  .footer-icons .img{
      flex: 0 0 32px;
      height: 32px;
      margin-right: 15px;
  }
  .footer-icons .img:last-child{
      margin-right: 0;
  }
</style>