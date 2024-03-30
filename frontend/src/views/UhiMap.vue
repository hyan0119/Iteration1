<template>
<div class="uhi-map">
    <div class="header">
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
        </ul>
        <!-- <img src="avatar.png" alt="Avatar"> -->
    </div>
    </div>
    
    <div class="map-section">
        <h2>UHI (URBAN HEAT ISLAND) MAP</h2>
        <p>check the Current heat island index in your location</p>
        <div class="postcode-input">
            <input type="text" placeholder="Enter postcode" v-model="postcode" class="input-text">
            <button @click="viewMap">View</button>
        </div>
        <div class="map">
            <!-- 在这里展示澳大利亚的地图 -->
            <p>这里展示地图</p>
            <p v-if="index">当前地图的 UHI 索引：{{ index }}</p>
        </div>
    </div>
    <div class="filler"></div>
</div>
</template>
  
<script>
import axios from 'axios';
export default {
name: 'UhiMap',
data() {
return {
    postcode: '',
    index: null
};
},
methods: {
async viewMap() {
    try {
    const response = await axios.get('http://127.0.0.1:8000/get_head_index', {
        params: {
        postcode: this.postcode
        }
    });

    this.index = response.data.index;
    } catch (error) {
    console.error('Error fetching data:', error);
    }
    }
}
}
</script>
  
<style scoped>
/* Add your CSS styles here */

.title h2 {
    margin: 0;
    font-size: 36px;
}

.title p {
    margin-top: 20px;
    font-size: 18px;
}


.map-section {
    text-align: center;
    padding: 50px 0;
    margin-top: -100px;
}

.map-section h2 {
    font-size: 24px;
}

.map-section p {
    font-size: 16px;
    color: #666;
}

.postcode-input {
    margin-top: 20px;

}

.postcode-input input {
    padding: 8px;
    border: 1px solid #ccc;

}

.postcode-input button {
    padding: 8px 20px;
    background-color: #333;
    color: #fff;
    border: none;
    cursor: pointer;
}

.map {
    margin-top: 20px;
}

.uhi-map{
    text-align: center;
    padding: 100px 0;
    background-color: #f4f4f4;
    background-image: url('../assets/uhimap_bg.jpg');

    background-size:contain;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}



</style>
<style src="./style.css"></style>
  