<template>
  <div class="homepage">
    <div class="header" >
      <div class="logo">
        <router-link to="/"><h1>SHADE OF GREEN</h1></router-link>
      </div>
      <div class="menu">
        <ul>
          <router-link to="/uhi-map"><li>UHI MAP</li></router-link>
          <router-link to="/plant-planner"><li>PLANT PLANNER</li></router-link>
          <router-link to="/my-plants"><li>MY PLANTS</li></router-link>
          <router-link to="/info"><li>INFO</li></router-link>
          <router-link to="/about-us"><li>ABOUT US</li></router-link>
          <!-- <li>
            <img src="./person.png" style="width: 10%; height:10%" alt="Avatar">
          </li> -->
        </ul>
      </div>
    </div>
    <div class="content">
      <div class="title">
        <h2>URBAN HEAT</h2>
        <h2>ISLAND INTRO</h2>
        <p>brief intro here</p>
        <a href="#introduction" class="scroll-down">
          <i class="fas fa-angle-double-down"><img src="../assets/arrow_down.png" style="width: 10%; height:10%"></i>
        </a>
      </div>
    </div>
    <div id="introduction" class="introduction">
      <h3>Welcome to our website!</h3>
      <p>This is where we introduce our website in detail.</p>
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


.content {
  text-align: center;
  padding: 100px 0;
}

.title h2 {
  margin: 0;
  font-size: 36px;
}

.title p {
  margin-top: 20px;
  font-size: 18px;
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
  text-align: center;
  padding: 100px 0;
  background-color: #f4f4f4;

  background-image: url('../assets/homepage_bg.jpg');

  background-size: cover;

  background-position: center;
}

.introduction h3 {
  font-size: 36px;
}

.introduction p {
  font-size: 18px;
}

</style>
<!-- <style src="./style.css"></style> -->
