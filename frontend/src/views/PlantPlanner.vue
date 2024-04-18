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
            <el-main class="main-content">
                <div class="plant-section">
                    <h2>PLANT PLANNER</h2>
                    <p>Discover what type of plants suit your needs</p>
                    <div class="postcode-input">
                        <div class="input-fields">
                            <div class="input-group">
                                <label for="apartmentSize">Balcony Size:</label>
                                <input placeholder="Input Balcony Size" type="text" id="apartmentSize" v-model="apartmentSize"
                                    class="input-field">
                            </div>

                            <div class="input-group">
                                <label>Sunlight:</label>
                                <el-select v-model="sunlight" placeholder="Select Sunlight" class="input-field">
                                    <!-- <option disabled value="" selected>Sunlight</option> -->
                                    <el-option label="high" value="high"></el-option>
                                    <el-option label="medium" value="medium"></el-option>
                                    <el-option label="low" value="low"></el-option>
                                </el-select>
                            </div>

                            <div class="input-group">
                                <label >Watering:</label>
                                <el-select v-model="watering" placeholder="Select Watering" class="input-field">
                                    <!-- <option selected value="">Watering</option> -->
                                    <el-option label="high" value="high"></el-option>
                                    <el-option label="medium" value="medium"></el-option>
                                    <el-option label="low" value="low"></el-option>
                                </el-select>
                            </div>
                        </div>


                        <button @click="viewPlantMatch">Match</button>
                    </div>
                    <div>
                        <!-- <p v-if="plantImageUrl" class="image-container">
                            <img :src="plantImageUrl" alt="Plant Image" class="plant-image">
                        </p>
                        <div class="info-container">
                            <p v-if="no_image">image: {{ no_image }}</p>
                            <p v-if="plantName">Name of the plant: {{ plantName }}</p>
                            <p v-if="lifespan">Lifespan: {{ lifespan }}</p>
                            <p v-if="maintainingGuide">Maintaining Guide: {{ maintainingGuide }}</p>
                            <p v-if="text">Contribution to the heat island effect: {{ text }}</p>
                            <p v-if="no_matched_plant">Error: {{ no_matched_plant }}</p>
                        </div> -->

                        <div class="info-container" v-if="plantImageUrl">
                            <img :src="plantImageUrl" alt="Plant Image" class="plant-image" >
                            <p v-if="no_image">image: {{ no_image }}</p>
                            <p v-if="plantName">Name of the plant: {{ plantName }}</p>
                            <p v-if="lifespan">Lifespan: {{ lifespan }}</p>
                            <p v-if="maintainingGuide">Maintaining Guide: {{ maintainingGuide }}</p>
                            <p v-if="text">Contribution to the heat island effect: {{ text }}</p>
                            <p v-if="no_matched_plant">Error: {{ no_matched_plant }}</p>
                        </div>
                        <!-- <p v-if="temperatureContribution">Contribution towards temperature reduce: {{ temperatureContribution }}
                </p>
                <p v-if="requiredTools">Required tools to grow the plant: {{ requiredTools }}</p> -->
                    </div>
                    
                </div>
            </el-main>
         <footer-column></footer-column>
        </el-container>
    </div>
</template>

<script>
import axios from 'axios';
import { ElSelect,ElOption } from 'element-plus';
import 'element-plus/dist/index.css';
import { ref } from 'vue'
import footerColumn from "../components/footer-column";

export default {
    name: 'PlantPlanner',
    components: {
        ElSelect,
        ElOption,
        footerColumn
    },
    setup() {
    const sunlight = ref('');
    const watering = ref('');

    return {
      sunlight,
      watering,
    };
  },
    data() {
        return {
            no_image: '',
            plantImageUrl: '',
            plantName: '',
            lifespan: 0,
            maintainingGuide: '',
            no_matched_plant: '',
            text: '',

        };
    },
    methods: {
        async viewPlantMatch() {
            this.plantImageUrl = '',
                this.plantName = '',
                this.lifespan = 0,
                this.maintainingGuide = '',
                this.no_matched_plant = ''
            this.text = ''
            try {
                const response = await axios.post('https://cooldownmelbourne.com/api/plant_match', {
                    apartmentSize: this.apartmentSize,
                    sunlight: this.sunlight,
                    cycle: "perennial",
                    watering: this.watering
                });
                const data = response.data;
                if (data.plantImageUrl == null) {
                    if (data.lifespan == null && data.plantName == null && data.maintainingGuide == null) {
                        this.no_matched_plant = "no match plant"
                    } else {
                        this.no_image = "no image for " + data.plantName + "!"
                        this.plantName = data.plantName;
                        this.lifespan = data.lifespan;
                        this.maintainingGuide = data.maintainingGuide;
                        this.text = "A 10-20% increase in vegetation cover is anticipated to reduce the UHI by 0.38-0.78 °C"
                    }

                } else {
                    this.plantImageUrl = data.plantImageUrl;
                    this.plantName = data.plantName;
                    this.lifespan = data.lifespan;
                    this.maintainingGuide = data.maintainingGuide;
                    this.text = "A 10-20% increase in vegetation cover is anticipated to reduce the UHI by 0.38-0.78 °C"

                }
                // this.plantName = data.plantName;
                // this.lifespan = data.lifespan;
                // this.maintainingGuide = data.maintainingGuide;
                // this.temperatureContribution = data.temperatureContribution;
                // this.requiredTools = data.requiredTools;
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        },
    }
};
</script>

<style scoped>
.plant-section {
    text-align: center;
    padding: 80px;
    color: white;
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


.image-container {
    display: inline-block;
    /* 使容器适应图片大小 */
    border: 2px solid #ccc;
    /* 添加灰色的底框 */
    padding: 5px;
    /* 在底框和图片之间添加一些间距 */
    border-radius: 5px;
    /* 给底框添加圆角 */
}

.plant-image {
    width: 200px;
    /* 设置图片的宽度 */
    height: auto;
    /* 设置图片的高度自动适应保持纵横比 */
}

.info-container {
    background-color: rgba(255, 255, 255, 1);
    /* 半透明的白色底色 */
    border: 1px solid #ccc;
    /* padding: 10px;  */
    border-radius: 5px;
    /* 圆角 */
    max-width: 300px;
    /* 最大宽度 */
    margin: 10px auto;
    /* 上下外边距为 10px，左右自动居中 */
    padding: 10px;
}
.info-container .plant-image{
    width: 100%;
}
.info-container p{
    color: #333;
}

.input-fields {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.input-group {
    margin-bottom: 20px;
    /* Add space between input groups */
}



.input-group label {
    display: block;
    /* Ensure labels are on their own line */
    margin-bottom: 5px;
    /* Add space between label and input field */
}



.input-field {
    width: 200px;
    /* Adjust width as needed */
    height: 35px;
    /* Adjust height as needed */
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: white;
    color: black !important;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
}

/* Apply this class to both inputs and selects */
input.input-field,
select.input-field {
    font-size: 16px;
    /* Adjust font size as needed */
    line-height: 1.5;
    /* This can affect the height, so it should be the same for both */
}

/* Additional styling for selects */
select.input-field {
    background-size: 12px 12px;
    /* Adjust size as needed */
    padding-right: 14px;
    /* Add padding to not overlap the arrow icon */
}

/* Ensuring text is visible in the select options */
select.input-field option {
    color: black !important;
    /* This will make the text visible */
}
.input-group{
    width: 220px;
}
.input-field{
    width: 100% !important;
    height: 43px;
    box-sizing: border-box;
    margin-right: 0;
}

</style>
<style src="./style.css"></style>