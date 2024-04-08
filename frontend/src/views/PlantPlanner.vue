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

        <div class="plant-section">
            <h2>PLANT PLANNER</h2>
            <p>Discover what type of plants suit your needs</p>
            <div class="postcode-input">

                <div class="input-fields">
                    <div class="input-group">
                        <label for="apartmentSize">Apartment Size:</label>
                        <input placeholder="Apartment Size" type="text" id="apartmentSize" v-model="apartmentSize"
                            class="input-field">
                    </div>

                    <div class="input-group">
                        <label for="sunlight">Sunlight:</label>
                        <select id="sunlight" v-model="sunlight" class="input-field">
                            <!-- <option disabled value="" selected>Sunlight</option> -->
                            <option selected value="full_shade">full_shade</option>
                            <option value="part_shade">part_shade</option>
                            <option value="sun-part_shade">sun-part_shade</option>
                            <option value="full_sun ">full_sun</option>
                        </select>
                    </div>

                    <!-- <div class="input-group">
                        <label for="cycle">Cycle:</label>
                        <select id="cycle" v-model="cycle" class="input-text">
                            <option selected value="perennial">perennial</option>
                            <option value="annual">annual</option>
                            <option value="biennial">biennial</option>
                            <option value="biannual">biannual</option>
                        </select>
                    </div> -->

                    <div class="input-group">
                        <label for="watering">Watering:</label>
                        <select id="watering" v-model="watering" class="input-field">
                            <!-- <option selected value="">Watering</option> -->
                            <option selected value="frequent">frequent</option>
                            <option value="average">average</option>
                            <option value="minimum">minimum</option>
                            <option value="none">none</option>
                        </select>
                    </div>
                </div>


                <button @click="viewPlantMatch">Match</button>
            </div>
            <div>
                <p v-if="plantImageUrl" class="image-container">
                    <img :src="plantImageUrl" alt="Plant Image" class="plant-image">
                </p>
                <div class="info-container">
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
        <div class="filler"></div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'PlantPlanner',
    data() {
        return {
            no_image: '',
            plantImageUrl: '',
            plantName: '',
            lifespan: 0,
            maintainingGuide: '',
            no_matched_plant: '',
            text: ''
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
                const response = await axios.post('http://3.107.48.197:8000/plant_match', {
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

.plant_planner {
    text-align: center;
    padding: 100px 0;
    background-color: #f4f4f4;
    background-image: url('../assets/plant_planner_bg.jpg');

    background-size: contain;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
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
    background-color: rgba(0, 0, 0, 0.5);
    /* 半透明的白色底色 */
    /* border: 1px solid #ccc; */
    /* padding: 10px;  */
    border-radius: 5px;
    /* 圆角 */
    max-width: 300px;
    /* 最大宽度 */
    margin: 10px auto;
    /* 上下外边距为 10px，左右自动居中 */
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

.input-text {
    width: 180px;
    /* Set a consistent width for all input fields */
    padding: 8px;
    /* Add some padding for better appearance */
    border: 1px solid #ccc;
    /* Add a border */
    border-radius: 5px;
    /* Add rounded corners */
    background-color: white;
    /* Ensure the background is white for better visibility */
    color: black !important;
    /* Set text color to black for visibility */
}

.input-group label {
    display: block;
    /* Ensure labels are on their own line */
    margin-bottom: 5px;
    /* Add space between label and input field */
}

html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  overflow-x: hidden; /* 防止水平滚动导致的空白 */
}

body {
  background-image: url('../assets/plant_planner_bg.jpg');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed; /* 使背景图像固定不动，滚动条滚动时背景不变 */
}

.plant_planner {
  min-height: 100vh; /* 确保至少有100%视口高度 */
  width: 100vw; /* 确保宽度覆盖整个视口宽度 */
  /* 其他样式保持不变 */
}

.input-field {
  width: 200px; /* Adjust width as needed */
  height: 35px; /* Adjust height as needed */
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
  font-size: 16px; /* Adjust font size as needed */
  line-height: 1.5; /* This can affect the height, so it should be the same for both */
}

/* Additional styling for selects */
select.input-field {
  background-size: 12px 12px; /* Adjust size as needed */
  padding-right: 14px; /* Add padding to not overlap the arrow icon */
}

/* Ensuring text is visible in the select options */
select.input-field option {
  color: black !important; /* This will make the text visible */
}

</style>
<style src="./style.css"></style>