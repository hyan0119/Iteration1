<template>
  <div class="homepage">
    <div class="menu-bar">
      <div class="logo">
        <img src="@/assets/logo.png" alt="Logo" />
        <router-link to="/">
          <h2>Home</h2>
        </router-link>
      </div>
      <div class="menu">
        <ul>
          <router-link to="/uhi-map">
            <li>UHI MAP</li>
          </router-link>
          <router-link to="/plant-planner">
            <li>PLANT PLANNER</li>
          </router-link>
          <router-link to="/my-plants">
            <li>MY PLANTS</li>
          </router-link>
          <router-link to="/info">
            <li>INFO</li>
          </router-link>
          <router-link to="/about-us">
            <li>ABOUT US</li>
          </router-link>
        </ul>
      </div>
    </div>
    <div class="short_desription">
      <div class="title">
        <h2>WELCOME TO COOL DOWN OUR MELBOURNE!</h2>
        <!-- <h2>ISLAND INTRO</h2> -->
        <p>Ever wonder what causes the heat in Melbourne CBD to be higher than the neighbouring suburbs? You are not
          alone. Our city is experiencing a growing problem - the “Urban Heat Island Effect” problem. As you explore our
          website, you will discover valuable insights regarding this phenomenon and learn how you can play a role in
          addressing it first-hand! </p>
        <a href="#introduction" class="scroll-down">
          <i class="fas fa-angle-double-down"><img src="../assets/arrow_down.png" style="width: 10%; height:10%"></i>
        </a>
        <p>click here to learn more</p>
      </div>
    </div>
    <div class="filler"></div>
    <div id="introduction" class="introduction">
      <div class="filler"></div>

      <div class="urban-heat-container">
        <div class="section" id="urban-heat-effect">
          <div class="image-container">
            <img src="@/assets/city_image.png" alt="City">
            <span>Photo by Pat Wheelen on Unsplash</span>
          </div>
          <div class="content">
            <h1>URBAN HEAT ISLAND EFFECT</h1>
            <p>Urban Heat Island is a phenomenon where large urbanised areas experiencing higher temperature, more
              polluted, and posed greater risks to negative health impacts during the summer. This phenomenon is caused
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
      </div>
      <!-- <div class="section" id="mitigate">
        <h2>WAYS TO MITIGATE IT</h2>
        <p>Thankfully, everyone can help to reduce the negative impact from Urban Heat Island Effect in Melbourne CBD.
          Here are some solutions that any Melbourne CBD resident can do to mitigate its impact:</p>
        <ul>
          <li>Grow indoor plants</li>
          <li>Use light-coloured materials as roofs</li>
        </ul>
      </div> -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
}
</script>

<style scoped>
/* Add your CSS styles here */


.short_desription {
  text-align: center;
  padding: 100px 0;
}

.title {
  text-align: center;
}

.title h2 {
  margin: 0;
  font-size: 36px;
}

.title p {
  /* margin-top: 40px; */
  font-size: 20px;
  width: 80%;
  margin: 0 auto;
  margin-top: 40px;
}

.scroll-down {
  display: inline-block;
  margin-top: 50px;
  text-decoration: none;
}

.scroll-down i {
  color: #333;
  font-size: 24px;
}



.homepage {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center; /* 确保内容垂直居中 */
  min-height: 100vh; /* 视口高度 */
  width: 100vw; /* 视口宽度 */
  padding: 100px 0;
  background-color: #f4f4f4;
  background-image: url('../assets/homepage_bg.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  margin: 0 auto; /* 确保左右居中 */
}


.menu-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: transparent;
  padding: 20px; /* 将内边距设置为 0 */
  margin: 0; /* 将外边距设置为 0 */
  position: absolute; /* 绝对定位 */
  top: 0; /* 顶部对齐 */
  left: 0; /* 左侧对齐 */
  width: 100%; /* 宽度设置为100% */
  z-index: 10; /* 确保菜单栏在页面的最上层 */
}

.short_desription {
  text-align: center;
  padding: 100px 0;
  width: 100%;
  max-width: 1200px; /* Adjust this value based on your design */
}

.title h2 {
  margin: 0;
  font-size: 36px;
}

.title p {
  font-size: 20px;
  width: 80%;
  margin: 0 auto;
  margin-top: 40px;
}

.introduction {
  width: 100%;
  max-width: 1200px; /* Adjust this value based on your design */
}

.urban-heat-container {
  font-family: 'Arial', sans-serif;
  margin: 0 auto;
  width: 90%;
  max-width: 1200px; /* Adjust this value based on your design */
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
  max-width: 100%;
  height: auto;
}

.image-container span {
  display: block;
  font-size: 0.8em;
  margin-top: 5px;
}

h1 {
  color: #a00;
  font-size: 2em;
}

h2 {
  font-size: 1.5em;
  color: #333;
}

p, li {
  line-height: 1.6;
}

ul {
  padding-left: 20px;
}

li {
  margin-bottom: 10px;
  text-align: left;
}

@media (max-width: 768px) {
  .section {
    flex-direction: column;
  }

  .section .content, .image-container {
    max-width: 100%;
    margin-left: 0;
    margin-right: 0;
  }
  
  html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow-x: hidden; /* 防止横向滚动 */
  }

  
}
</style>
<style src="./style.css"></style>
