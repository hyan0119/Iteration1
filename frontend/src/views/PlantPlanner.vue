<template>
    <div class="common-layout">
        <el-container>
            <div>
                <HeaderNavigation />
            </div>
            <el-main class="main-content">

                <div class="plant-section">
                    <div class="title">
                        <img src="@/assets/card.png" alt="" class="title_more_img img_left" />
                        PLANT PLANNER
                        <img src="@/assets/card.png" alt="" class="title_more_img img_right" />
                    </div>
                    <div class="urban">
                        <div class="urban_inner">
                            <div class="urban_inner_text">
                                Discover the ideal plant that can help you cool down your home. Enter the empty fields below
                                and find out the perfect plan to grow at your home.
                            </div>
                        </div>
                    </div>
                    <div class="seletc_item">
                        <div class="label">
                            <span>Balcony Size (sqm)</span>
                            <el-tooltip class="item" effect="dark"
                                content="Enter a number to the plot size field. Make sure to enter your plot size area in sqm."
                                placement="top-start">
                                <img src="@/assets/info.png" alt="" class="info" />
                            </el-tooltip>
                            <div class="tips"></div>

                        </div>
                        <div class="select_input">
                            <input placeholder="ex: 2" type="text" id="apartmentSize" v-model="apartmentSize"
                                class="input-field">
                        </div>
                        <div class="Plot"></div>
                    </div>
                    <div class="seletc_item">
                        <div class="label">
                            <span>Sunlight</span>
                            <el-tooltip class="item" effect="dark" content="Full Sun: Plenty of direct sunlight all day.Part Shade: Some sunlight during the day.
                                Filtered Shade: Sunlight that's partially blocked by trees or other objects.
                                Full Shade: No direct sunlight.
                                Deep Shade: Extremely limited sunlight." placement="top-start">
                                <img src="@/assets/info.png" alt="" class="info" />
                            </el-tooltip>
                        </div>
                        <div class="select_input">
                            <el-select v-model="sunlight" placeholder="Select the sunlight availability at your home"
                                class="select-field">
                                <!-- <option disabled value="" selected>Sunlight</option> -->
                                <el-option label="high" value="high"></el-option>
                                <el-option label="medium" value="medium"></el-option>
                                <el-option label="low" value="low"></el-option>
                            </el-select>
                        </div>
                    </div>
                    <div class="seletc_item">
                        <div class="label">
                            <span>Watering Needs</span>
                            <el-tooltip class="item" effect="dark" content="Low: Water every 2 to 3 weeks
                                Medium: Water once or twice a week
                                High: Water daily" placement="top-start">
                                <img src="@/assets/info.png" alt="" class="info" />
                            </el-tooltip>
                        </div>
                        <div class="select_input">
                            <el-select v-model="watering"
                                placeholder="Select the Watering Needs for the plant that you desire" class="select-field">
                                <!-- <option selected value="">Watering</option> -->
                                <el-option label="high" value="high"></el-option>
                                <el-option label="medium" value="medium"></el-option>
                                <el-option label="low" value="low"></el-option>
                            </el-select>
                        </div>
                    </div>
                    <!-- <div class="seletc_item">
                        <div class="label">
                            <span>Postcode</span>
                            <el-tooltip class="item" effect="dark" content="Enter your postcode" placement="top-start">
                                <img src="@/assets/info.png" alt="" class="info" />
                            </el-tooltip>
                        </div>
                        <div class="select_input">
                            <input placeholder="ex: 3000" type="text" id="postcode" v-model="postcode" class="input-field">
                        </div>
                    </div> -->
                    <div class="generate-button">
                        <el-button @click="viewPlantMatch" size="large" :loading="loading">GENERATE PLANT</el-button>
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
                            <img :src="plantImageUrl" alt="Plant Image" class="plant-image">
                            <div class="Unsplash">Photo by Prudence Earl on Unsplash</div>
                            <div class="info-container_inner">
                                <div class="container_inner_top">
                                    <div v-if="no_image" class="container_inner_top_item">
                                        <div class="label">image</div>
                                        <div class="dot">:</div>
                                        <div class="value">{{ no_image }}</div>
                                    </div>
                                    <div v-if="plantName" class="container_inner_top_item">
                                        <div class="label">Name of the plant</div>
                                        <div class="dot">:</div>
                                        <div class="value">{{ plantName }}</div>
                                    </div>
                                    <div v-if="lifespan" class="container_inner_top_item">
                                        <div class="label">Lifespan</div>
                                        <div class="dot">:</div>
                                        <div class="value">{{ lifespan }}</div>
                                    </div>
                                    <div v-if="maintainingGuide" class="container_inner_top_item">
                                        <div class="label">Maintaining Guide</div>
                                        <div class="dot">:</div>
                                        <div class="value">{{ maintainingGuide }}</div>
                                    </div>
                                </div>
                                <div v-if="text" class="text_item">Contribution to the heat island effect: {{ text }}</div>
                                <div v-if="no_matched_plant" class="text_item">Error: {{ no_matched_plant }}</div>
                            </div>

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
import { ElSelect, ElOption } from 'element-plus';
import 'element-plus/dist/index.css';
import { ref } from 'vue'
import footerColumn from "../components/footer-column";
import HeaderNavigation from "@/components/HeaderNavigation.vue";
export default {
    name: 'PlantPlanner',
    components: {
        ElSelect,
        ElOption,
        footerColumn,
        HeaderNavigation
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
            loading: false,
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
            this.loading = true
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
                this.loading = false
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
    padding: 80px 0;
    color: #000;
}


.generate-button {
    margin-top: 20px;
    align-items: center;
    flex-direction: column;
    display: flex;
}


.generate-button .el-button {
    width: 274px;
    height: 86px;
    background: #09B845;
    border-radius: 30px;
    font-family: Fredoka One;
    font-size: 24px;
    font-weight: 600;
    line-height: 86px;
    text-align: center;
    color: #fff;
}


.info-container {
    background-color: rgba(255, 255, 255, 1);
    /* padding: 10px;  */
    border-radius: 5px;
    /* 圆角 */
    width: 50%;
    /* 最大宽度 */
    margin: 10px auto 0 auto;
    /* 上下外边距为 10px，左右自动居中 */
    padding: 10px;
}

.info-container .plant-image {
    width: 100%;
    height: 591px;
    border-radius: 30px;
}

.info-container p {
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

.input-group {
    width: 220px;
}


.title {
    width: 100%;
    height: 150px;
    font-family: Fredoka One;
    font-size: 50px;
    font-weight: 600;
    line-height: 150px;
    text-align: center;
    color: #000;
    position: relative;
}

.transform {
    border-radius: 40px;
}

.title_more_img {
    width: 239px;
    height: 86px;
    position: absolute;
    margin: auto;
    top: 0;
    bottom: 0;
}

.img_left {
    left: 0;
}

.img_right {
    right: 0;
}

.urban {
    width: 100%;
    height: auto;
    margin-top: 3px;
}

.urban_inner {
    width: 50%;
    height: 100%;
    margin: 0 auto;
}

.urban_inner_text {
    font-family: Fredoka;
    font-size: 32px;
    font-weight: 400;
    text-align: center;
    color: #000;
    line-height: 50px;
}

.seletc_item {
    width: 80%;
    height: 122px;
    margin: 60px auto 0 auto;
    position: relative;
}

.seletc_item .label {
    font-family: Fredoka One;
    font-size: 36px;
    font-weight: 600;
    text-align: left;
    color: #000;
    display: flex;
}

.info {
    width: 40px;
    height: 40px;
    margin-left: 20px;
    cursor: pointer;
    margin-top: 5px;
}

.select_input {
    width: 100%;
}

.select_input input {
    width: 100%;
    height: 54px;
    box-shadow: 0px 4px 4px 0px #00000040;
    background: #EDEDED;
    font-size: 24px;
    margin-top: 10px;
    padding: 0;
}

.input-field {
    width: 100%;
    /* Adjust width as needed */
    height: 35px;
    /* Adjust height as needed */
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: white;
    color: black !important;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
}

::v-deep .input-field::placeholder {
    color: #7E7777;
    font-weight: 600;
    padding-left: 10px;
    font-size: 24px !important;
}

::v-deep .select-field .el-select__wrapper {
    width: 100%;
    height: 58px;
    box-shadow: 0px 4px 4px 0px #00000040;
    background: #EDEDED;
    font-size: 24px;
    margin-top: 10px;
    font-weight: 600;
}

::v-deep .el-select__placeholder {
    color: #7E7777;
}

.Unsplash {
    font-family: Fredoka;
    font-size: 12px;
    font-weight: 400;
    text-align: center;
    color: #000;
    margin: 20px 0;
}

.info-container_inner {
    width: 100%;
    height: auto;
    padding: 50px 0px;
    margin-top: 50px;
    background: #85E0C4;
    border-radius: 30px;
}

.info-container_inner .text_item {
    margin: 30px auto 0 auto;
    width: 90%;
}

.container_inner_top {
    width: 80%;
    height: auto;
    margin: 0 auto;
}

.container_inner_top .container_inner_top_item {
    display: flex;
    justify-content: space-between;
    margin-bottom: 30px;
}

.label {
    width: 45%;
    font-family: Fredoka One;
    font-size: 28px;
    font-weight: 600;
    text-align: left;
    color: #000;
}

.dot {
    width: 10%;
    font-family: Fredoka One;
    font-size: 28px;
    font-weight: 400;
    text-align: center;
    color: #000;
}

.value {
    width: 45%;
    font-family: Fredoka One;
    font-size: 28px;
    font-weight: 400;
    text-align: left;
    color: #000;
}
</style>
<style src="./style.css"></style>