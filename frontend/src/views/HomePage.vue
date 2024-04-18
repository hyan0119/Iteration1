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
      <!-- <div class="filler"></div> -->
      <el-main class="main-content">
        <section class="hero-section">
          <div class="section first" >
              <div class="content-and-image">
                <div class="content">
                  <h1>JOIN OUR FIGHT AGAINST URBAN HEAT ISLAND</h1>
                  <p>The Urban Heat Island effect has caused overheat to our city for a long time!</p>
                  <p>Find out the easiest ways for residents of Melbourne CBD to combat its dangers.</p>
                  <div class="scorll-logo">
                    <img src="@/assets/arrow_down.png" style="width: 20px; height: 20px;" alt="Logo"
                      @click="scrollToElement" />
                    <el-button @click="scrollToElement">Learn More</el-button>
                  </div>
                  <div ref="contentToScrollTo"></div>
                </div>
                <div class="image-container">
                  <img src="@/assets/impact_image.png" alt="City" class="transform img-1">
                </div>
              </div>
          </div>
          
          <div class="section" id="urban-heat-effect">
            <div class="image-container">
              <img src="@/assets/city_image.png" alt="City" class="transform img-2">
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
              <img src="@/assets/home2.png" alt="City" class="transform img-3">
              <span>Photo by Chromatograph on Wnsplash</span>
            </div>
          </div>

          <div class="section" id="mitigate">
            <div class="image-container">
              <img src="@/assets/home3.png" alt="City" class="transform img-4">
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
      <footer-column></footer-column>
    </el-container>
  </div>
</template>

<script>
import footerColumn from "../components/footer-column";
export default {
  name: 'HomePageNew',
  components: {
    footerColumn
  },
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

.content-and-image .content .scorll-logo {
  display: flex;
  flex-direction: column;
  /* 以列的方式排列子元素 */
  align-items: center;
  /* 水平居中对齐子元素 */
  justify-content: left;
  /* 如果需要，也可以在垂直方向上居中 */

}

.content-and-image .image-container {
  flex: 1;
  /* 图片内容也占用可用空间 */
  text-align: center;
  /* 图片居中显示 */
}

.transform.img-1{
   transform: rotate(0deg) translate(0, 0);
}
.transform.img-2{
   transform: rotate(0deg) translate(0, 0);
}
.transform.img-3{
   transform: rotate(0deg) translate(0, 0);
}
.transform.img-4{
   transform: rotate(0deg) translate(0, 0);
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
  color: white;
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
  justify-content: center;
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

.section.first{
  height: 100vh;
  margin-bottom: 0;
}

.section.first .content-and-image{
   width: 1200px;
}
.section.first .content{
   max-width: 60%;
}
.section.first .content h1{
   margin-bottom: 65px;
}
.section.first .content p{
   margin-bottom: 45px;
}
.section.first .image-container {
  margin-right: 0;
}
.section.first .image-container img {
  width: 100%;
}

</style>
<style src="./style.css"></style>
