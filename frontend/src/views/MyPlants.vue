<template>
  <div class="plant_planner">
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
                <router-link to="/info-page">
                    <li>INFO</li>
                </router-link>
                <router-link to="/about-us">
                    <li>ABOUT US</li>
                </router-link>
            </ul>
        </div>
    </div>
    <div class="coming-soon-container">
      <img src="@/assets/comingsoon.png" alt="Coming Soon" />
    </div>
  </div>
  </template>
  
  <script>
  export default {
    name: 'MyPlants'
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
    max-width: 50%; /* Adjust as needed */
    max-height: 50%; /* Adjust as needed */
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
    min-height: 100vh; /* 确保至少有100%视口高度 */
    width: 100vw; /* 确保宽度覆盖整个视口宽度 */
}
  </style>
  