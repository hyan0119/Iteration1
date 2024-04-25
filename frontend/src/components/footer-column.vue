<template>
  <el-footer class="footer">
    <el-row class="footer-top" >
      <el-col :span="8" class="footer-section">
          <h3 class="el-typography">COOLDOWN MELBOURNE</h3>
         <div class="item">
            <img :src="require('@/assets/footer/icon_01.png')" alt="">
              <span>Wellington Rd, Clayton, VIC 3800</span>
         </div>
         <div class="item">
            <img :src="require('@/assets/footer/icon_02.png')" alt="">
              <span>0424281773</span>
         </div>
         <div class="item">
            <img :src="require('@/assets/footer/icon_03.png')" alt="">
              <span>info@cooldownmelbourne.com</span>
         </div>
      </el-col>

      <el-col :span="8" class="footer-section middle_section">
          <h3 class="el-typography middle">USEFUL LINKS</h3>
            <div class="item">
                <span>Home</span>
           </div>
            <div class="item">
                <span>About Us</span>
           </div>
            <div class="item">
                <span>Privacy Policy</span>
           </div>
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
.el-footer{
  padding: 0;
}
  .footer-top {
      display: flex;
      background-color: #4CAF50;
      padding: 0vh;
      align-items: center;
  }
  .item{
    display: flex;
    margin-bottom: 20px;
  }
  .item img{
    width: 20px;
    height: 20px;
    margin-right: 10px;
  }
  .footer-bottom {
      background-color: rgb(28, 61, 52);
      color: white;
      text-align: center;
      padding: 5px;
  }

  .el-typography {
      color: white;
      text-align: left;
      padding-left: 20px;
      /* 可以添加更多排版样式，如字体大小、行高等 */
  }
  .middle{
     padding-left: 0px;
  }
  .middle_section .item{
    cursor: pointer;
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
      margin-bottom: auto;
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