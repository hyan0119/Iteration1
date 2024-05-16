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
                            <span style="font-family: 'Fredoka One', cursive;">Balcony Size (sqm)</span>
                            <el-tooltip class="item" effect="dark"
                                content="Enter a number to the plot size field. Make sure to enter your plot size area in sqm."
                                placement="top-start">
                                <img src="@/assets/info.png" alt="" class="info" />
                            </el-tooltip>
                            <div class="tips"></div>

                        </div>
                        <div class="select_input">
                            <input placeholder="ex: 2" type="text" id="apartmentSize" v-model="apartmentSize" class="input-field" style="font-family: 'Fredoka One', cursive;">
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
                                <el-option label="high" value="high"></el-option>
                                <el-option label="medium" value="medium"></el-option>
                                <el-option label="low" value="low"></el-option>
                            </el-select>
                        </div>


                    </div>
                    <div class="seletc_item">
                        <div class="label">
                            <span>Postcode</span>
                            <el-tooltip class="item" effect="dark" content="Enter your postcode" placement="top-start">
                                <img src="@/assets/info.png" alt="" class="info" />
                            </el-tooltip>
                        </div>
                        <div class="select_input">
                            <el-select v-model="postcode" placeholder="ex: 3000" class="select-field">
                                <el-option
                                    v-for="item in postcodes"
                                    :key="item"
                                    :label="item"
                                    :value="item">
                                </el-option>
                            </el-select>
                        </div>
                    </div>
                    <div class="generate-button">
                        <el-button @click="viewPlantMatch" size="large" :loading="loading">GENERATE PLANT</el-button>
                    </div>
                    <div>
                        <div class="info-container" v-if="plantImageUrl || no_matched_plant">
                            <img :src="plantImageUrl" alt="Plant Image" v-if="plantImageUrl" class="plant-image">
                            <div v-if="plantImageUrl" class="Unsplash">Photo by Prudence Earl on Unsplash</div>
                            <div class="info-container_inner" v-if="plantImageUrl || no_matched_plant">
                                <div class="container_inner_top">
                                    <div v-if="no_image" class="container_inner_top_item">
                                        <div class="label" style="font-family: Fredoka One', cursive;">image</div>
                                        <div class="dot">:</div>
                                        <div class="value">{{ no_image }}</div>
                                    </div>
                                    <div v-if="plantName" class="container_inner_top_item">
                                        <div class="label">Name of the plant</div>
                                        <div class="dot">:</div>
                                        <div class="value">{{ plantName }}</div>
                                    </div>
                                </div>
                                <h2 v-if="plantImageUrl">Day Care</h2>
                                <div v-if="watering_guide" class="text_item">{{ watering_guide }}</div>
                                <h2 v-if="plantImageUrl">Watering Guide</h2>
                                <div v-if="watering_guide_description" class="text_item">{{ watering_guide_description }}</div>
                                <h2 v-if="plantImageUrl">Sunlight Guide</h2>
                                <div v-if="sunlight_guide_description" class="text_item">{{ sunlight_guide_description }}</div>
                                <h2 v-if="plantImageUrl">Pruning Guide</h2>
                                <div v-if="pruning_guide_description" class="text_item">{{ pruning_guide_description }}</div>
                                <h2 v-if="plantImageUrl">Energy Save</h2>
                                <div v-if="energy_save" class="text_item">{{ energy_save }}</div>
                                
                                <div v-if="no_matched_plant" class="text_item">Error: {{ no_matched_plant }}</div>
                            </div>
                        </div>
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
        const postcode = ref('');

        return {
            sunlight,
            watering,
            postcode
        };
    },
    data() {
        return {
            loading: false,
            no_image: '',
            plantImageUrl: '',
            plantName: '',
            watering_guide: '',
            watering_guide_description: '',
            sunlight_guide_description: '',
            pruning_guide_description: '',
            energy_save:'',
            postcodes: [
                '3000', '3002', '3003', '3004', '3005', '3006', '3008',
                '3010', '3031', '3032', '3050', '3051', '3052', '3053',
                '3054', '3141', '3207'
            ],
            no_matched_plant: ''
        };
    },
    methods: {
        async viewPlantMatch() {
            this.loading = true;
            this.resetData();

            try {
                const response = await axios.post('https://cooldownmelbourne.com/api/plant_match', {
                    apartmentSize: this.apartmentSize,
                    sunlight: this.sunlight,
                    cycle: "perennial",
                    watering: this.watering,
                    postcode: this.postcode
                });

                const data = response.data;

                if (Object.keys(data).length === 0 || data.plantName == null) {
                    this.no_matched_plant = "No matched plant found.";
                } else {
                    this.updatePlantData(data);
                }
            } catch (error) {
                this.no_matched_plant = "Error fetching data. Please try again.";
                console.error('Error fetching data:', error);
            } finally {
                this.loading = false;
            }
        },
        resetData() {
            this.plantImageUrl = '';
            this.plantName = '';
            this.watering_guide = '';
            this.watering_guide_description = '';
            this.sunlight_guide_description = '';
            this.pruning_guide_description = '';
            this.energy_save = '';
            this.no_matched_plant = '';
        },
        updatePlantData(data) {
            if (data.plantImageUrl == null) {
                this.no_image = "No image for " + data.plantName + "!";
            } else {
                this.plantImageUrl = data.plantImageUrl;
            }

            this.plantName = data.plantName;
            this.watering_guide = data.watering_guide;
            this.watering_guide_description = data.watering_guide_description;
            this.sunlight_guide_description = data.sunlight_guide_description;
            this.pruning_guide_description = data.pruning_guide_description;
            this.energy_save = data.energy_save;
        }
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
    font-family: 'Fredoka One', cursive;
    font-size: 24px;
    font-weight: 600;
    line-height: 86px;
    text-align: center;
    color: #fff;
}

.info-container {
    background-color: rgba(255, 255, 255, 1);
    border-radius: 5px;
    width: 50%;
    margin: 10px auto 0 auto;
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
    font-family: 'Fredoka One', cursive;
}

.input-group {
    margin-bottom: 20px;
    font-family: 'Fredoka One', cursive;
}

.input-group label {
    display: block;
    margin-bottom: 5px;
    font-family: 'Fredoka One', cursive;
}

.input-group input,
.input-group select {
    font-size: 16px;
    line-height: 1.5;
}

select.input-field {
    background-size: 12px 12px;
    padding-right: 14px;
    font-size: 14px;
    padding: 8px; 
    box-sizing: border-box;
    
}

select.input-field option {
    color: black !important;
}

.input-group {
    width: 220px;
}

.title {
    width: 100%;
    height: 150px;
    font-family: 'Fredoka One', cursive;
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
    font-family: 'Fredoka One', cursive;
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
    font-family: 'Fredoka One', cursive;
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
    font-family: 'Fredoka One', cursive;
}

.select_input input {
    width: 100%;
    height: 54px;
    background: #EDEDED;
    font-size: 24px;
    margin-top: 10px;
    padding: 0;
}

.input-field {
    width: 100%;
    height: 35px;
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
    font-family: 'Fredoka One', cursive;
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
    font-family: 'Fredoka One', cursive;
    font-size: 28px;
    font-weight: 600;
    text-align: left;
    color: #000;
}

.dot {
    width: 10%;
    font-family: 'Fredoka One', cursive;
    font-size: 28px;
    font-weight: 400;
    text-align: center;
    color: #000;
}

.value {
    width: 45%;
    font-family: 'Fredoka One', cursive;
    font-size: 28px;
    font-weight: 400;
    text-align: left;
    color: #000;
}

.el-option {
    font-family: 'Fredoka One', cursive;
    font-size: 24px;
    font-weight: 400;
    color: #000;
}

h2{
    font-size: 40px;
    font-family: 'Fredoka One', cursive;
    font-weight: 600;
    text-align: center;
    color: #000;

}

.text_item{
    font-size: 24px;
    font-family: 'Fredoka One', cursive;
    font-weight: 100;
    text-align: center;
    color: #000;
}

</style>
<style src="./style.css"></style>
