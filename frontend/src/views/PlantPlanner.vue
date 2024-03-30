<template>
<div class="plant_planner">
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
    
    <div class="plant-section">
        <h2>PLANT PLANNER</h2>
        <p>Discover what type of plants suit your needs</p>
        <div class="postcode-input">

            <div class="input-fields">
                <input placeholder="apartment Size" type="text" id="apartmentSize" v-model="apartmentSize" class="input-text">
                <input placeholder="number of windows" type="text" id="numWindows" v-model="numWindows" class="input-text">
                <input placeholder="maintenance Availability" type="text" id="maintenanceAvailability" v-model="maintenanceAvailability" class="input-text">
                <input placeholder="building Direction" type="text" id="buildingDirection" v-model="buildingDirection" class="input-text">
            </div>
            <button @click="viewPlantMatch">Match</button>
        </div>
        <div>
            <p v-if="plantImageUrl" class="image-container">
            <img :src="plantImageUrl" alt="Plant Image" class="plant-image">
            </p>
            <p v-if="plantName">Name of the plant: {{ plantName }}</p>
            <p v-if="lifespan">Lifespan: {{ lifespan }}</p>
            <p v-if="maintainingGuide">Maintaining Guide: {{ maintainingGuide }}</p>
            <p v-if="temperatureContribution">Contribution towards temperature reduce: {{ temperatureContribution }}</p>
            <p v-if="requiredTools">Required tools to grow the plant: {{ requiredTools }}</p>
        </div>
    </div>
    <div class="filler"></div>
</div>
</template>
  
<script>
import axios from 'axios';
export default {
name: 'PlantPlanner',
data() {
    return {
      plantImageUrl: '',
      plantName: '',
      lifespan: 0,
      maintainingGuide: '',
      temperatureContribution: '',
      requiredTools: ''
    };
},
methods: {
    async viewPlantMatch() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/plant_match', {
          apartmentSize: this.apartmentSize,
          numWindows: this.numWindows,
          maintenanceAvailability: this.maintenanceAvailability,
          buildingDirection: this.buildingDirection
        });
        const data = response.data;
        this.plantImageUrl = data.plantImageUrl;
        this.plantName = data.plantName;
        this.lifespan = data.lifespan;
        this.maintainingGuide = data.maintainingGuide;
        this.temperatureContribution = data.temperatureContribution;
        this.requiredTools = data.requiredTools;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
  }
};
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


.plant-section {
    text-align: center;
    padding: 50px 0;
    margin-top: -100px;
}

.plant-section h2 {
    font-size: 24px;
}

.plant-section p {
    font-size: 16px;
    color: #666;
}

/* .postcode-input {
    margin-top: 20px;
} */

/* .postcode-input {
  display: flex;
  flex-direction: column;
  align-items: center;
} */

.input-labels {
  display: flex;
  font-size: smaller;
}

.postcode-input {
    margin-top: 20px;
    align-items: center;
    flex-direction: column;
    display: flex;

}

.postcode-input input {
    padding: 8px;
    border: 1px solid #ccc;
    margin-right: 20px;
    width: 180px;
}

.postcode-input button {
    padding: 8px 20px;
    background-color: #333;
    color: #fff;
    border: none;
    cursor: pointer;
    margin-top: 20px;
}

.plant_planner{
    text-align: center;
    padding: 100px 0;
    background-color: #f4f4f4;
    background-image: url('../assets/plant_planner_bg.jpg');

    background-size:contain;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}

  </style>
  <style src="./style.css"></style>
  