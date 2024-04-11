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
        <section class="hero-section">
          <el-row :gutter="20">
            <el-col :span="12" class="content-and-image">
              <div class="text-content">
                <h1>JOIN OUR FIGHT AGAINST URBAN HEAT ISLAND</h1>
                <p>The Urban Heat Island effect has caused overheat to our city for a long time!</p>
                <p>Find out the easiest ways for residents of Melbourne CBD to combat its dangers.</p>
                <div class="scorll-logo">
                  <img src="@/assets/arrow_down.png" style="width: 10%; height: 10%;" alt="Logo"
                    @click="scrollToElement" />
                  <el-button @click="scrollToElement">Learn More</el-button>
                </div>
                <div ref="contentToScrollTo"></div>
              </div>
              <div class="image-content">
                <img src="@/assets/impact_image.png" alt="City">
              </div>
            </el-col>
          </el-row>
          <div class="section" id="urban-heat-effect">
            <div class="image-container">
              <img src="@/assets/city_image.png" alt="City">
              <span>Photo by Pat Wheelen on Unsplash</span>
            </div>
            <div class="content">
              <h1>URBAN HEAT ISLAND EFFECT</h1>
              <p>Urban Heat Island is a phenomenon where large urbanised areas experiencing higher temperature, more
                polluted, and posed greater risks to negative health impacts during the summer. This phenomenon is
                caused
                by
                several factors including:</p>
              <ul>
                <li>The prevalence Dark heat-absorptive surfaces in urban buildings and roads (concrete & asphalt
                  materials
                  absorb more heat than other materials).</li>
                <li>Absence of proper vegetation in the area.</li>
                <li>High number of heat-generating activities by engines & generators within the urban area.</li>
              </ul>
            </div>
          </div>

          <div class="section" id="negative-impact">
            <div class="content">
              <h1>THE NEGATIVE IMPACT</h1>
              <p>Elevated temperature caused by Urban Heat Island (UHI) effect can affect communities and environment in
                multiple ways:</p>
              <ul>
                <li>Increased Energy Consumption due to prevalence of air conditioners.</li>
                <li>Rise in Air Pollutants and Greenhouse gases emissions due to surge in energy consumption.</li>
                <li>Decline in human health and well-being living in the area.</li>
                <li>Impaired Water Quality</li>
              </ul>
            </div>
            <div class="image-container">
              <img src="@/assets/city_image.png" alt="City">
              <span>Photo by Chromatograph on Wnsplash</span>
            </div>
          </div>

          <div class="section" id="mitigate">
            <div class="image-container">
              <img src="@/assets/city_image.png" alt="City">
              <span>Photo by Chromatograph on Wnsplash</span>
            </div>
            <div class="content">
              <h2>WAYS TO MITIGATE IT</h2>
              <p>Thankfully, everyone can help to reduce the negative impact from Urban Heat Island Effect in Melbourne
                CBD.
                Here are some solutions that any Melbourne CBD resident can do to mitigate its impact:</p>
              <ul>
                <li>Grow indoor plants</li>
                <li>Grow vegetation in their home such as balcony and green roofs</li>
                <li>Reduce energy consumption</li>
                <li>Use light-coloured materials as roofs</li>
              </ul>
            </div>
          </div>
        </section>
      </el-main>
      <el-footer class="footer">
    <el-row class="footer-top" type="flex" justify="space-around" align="middle">
      <el-col :span="8" class="footer-section">
        <div>
          <h3 class="el-typography">COOLDOWN MELBOURNE</h3>
          <p><i class="el-icon-location"></i> Wellington Rd, Clayton, VIC 3800</p>
          <p><i class="el-icon-phone"></i> 0424281773</p>
          <p><i class="el-icon-message"></i> info@cooldownmelbourne.com</p>
        </div>
      </el-col>

      <el-col :span="8" class="footer-section">
        <div>
          <h3 class="el-typography">USEFUL LINKS</h3>
          <el-link type="primary" underline="false">Home</el-link>
          <el-link type="primary" underline="false">About Us</el-link>
          <el-link type="primary" underline="false">Service</el-link>
          <el-link type="primary" underline="false">Terms of Service</el-link>
          <el-link type="primary" underline="false">Privacy Policy</el-link>
        </div>
      </el-col>

      <el-col :span="8" class="footer-section">
        <div>
          <h3 class="el-typography">FOLLOW US</h3>
          <!-- ...你的社交媒体图标... -->
        </div>
      </el-col>
    </el-row>

    <div class="footer-bottom">
      <p>© Copyright Team Colon D All Rights Reserved | Designed by Monash IE Team TA 14</p>
    </div>
  </el-footer>
    </el-container>
  </div>
</template>


<script>
export default {
  name: 'HomePageNew',
  methods: {
    scrollToElement() {
      // 使用 `this.$refs` 来获取模板中的元素
      const element = this.$refs.contentToScrollTo;

      // 使用 `scrollIntoView` 方法来平滑滚动到该元素
      element.scrollIntoView({ behavior: 'smooth' });
    }
  }
}
</script>

<style scoped>
/* ... 省略已有样式 ... */



.content-and-image {
  display: flex;
  align-items: center;
  /* 如果你希望文本和图片垂直居中对齐 */
  justify-content: space-between;
  /* 在文本和图片之间提供一些空间 */
}

.content-and-image .text-content {
  flex: 1;
  /* 文本内容占用可用空间 */
  padding-right: 20px;
  align-items: center;
  display: flex;
  flex-direction: column;
  /* 以列的方式排列子元素 */
  align-items: center;
  /* 水平居中对齐子元素 */
  justify-content: center;
  /* 在文本和图片之间添加一些间隔 */
}

.content-and-image .text-content .scorll-logo {
  display: flex;
  flex-direction: column;
  /* 以列的方式排列子元素 */
  align-items: center;
  /* 水平居中对齐子元素 */
  justify-content: center;
  /* 如果需要，也可以在垂直方向上居中 */

}

.content-and-image .image-content {
  flex: 1;
  /* 图片内容也占用可用空间 */
  text-align: center;
  /* 图片居中显示 */
}

.header-content {
  background-color: #56A05B;
  /* Green background */
  color: #fff;
  padding: 20px;
  text-align: center;
}

.title-container h2 {
  margin-top: 0;
}

.learn-more {
  color: #fff;
  background-color: #333;
  padding: 10px 20px;
  border-radius: 4px;
  text-decoration: none;
}

.image-content {
  margin: 20px 0;
}

.image-container {
  text-align: center;
}

.image-container img {
  max-width: 100%;
  height: auto;
}

.image-container span {
  display: block;
  font-size: 0.8em;
  color: #666;
  text-align: center;
  margin-top: 10px;
}

.main-content {
  padding-top: 200px;
  /* 设置一个与头部高度相等的顶部边距 */
}

.urban-heat-container {
  font-family: 'Arial', sans-serif;
  margin: 0 auto;
  width: 90%;
  max-width: 1200px;
  /* Adjust this value based on your design */
}

.section {
  margin-bottom: 2em;
  display: flex;
  align-content: center;
}

.section .content {
  max-width: 40%;
  margin-left: 5%;
  margin-right: 5%;
}

.image-container {
  text-align: center;
  margin-left: 5%;
  margin-right: 5%;
}

.image-container img {
  width: 50%;
  height: auto;
}

.image-container span {
  display: block;
  font-size: 0.8em;
  margin-top: 5px;
}
</style>
<style src="./style.css"></style>
