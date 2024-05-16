<template>
  <div class="common-layout">
    <el-container>
      <div>
        <HeaderNavigation />
      </div>
      <div class="filler"></div>
      <el-main class="main-content">
        <div class="coming-soon-container">
          <div class="container">
            <!-- <div class="title">COOL CITY SOLUTIONS</div> -->
            <div class="title">
              <img src="@/assets/card.png" alt="" class="title_more_img img_left" />
              COOL CITY SOLUTIONS
              <img src="@/assets/card.png" alt="" class="title_more_img img_right" />
            </div>
            <div class="urban">
              <div class="urban_inner">
                <div class="urban_inner_text">
                  Check out how vegetation around the City of Melbourne helps reduce the heat in a particular building.
                  Additionally, assess the building’s potential for green roof. </div>
              </div>
            </div>
            <div class="container_top">
              <div class="subTile">Instructions</div>
              <div class="yellow">
                <div class="yellow_inner">
                  Input a street address and discover the benefits of vegetation within a 100-meter radius of the building
                </div>
              </div>
              <div class="subTile">Street Address</div>
              <div class="subSelect">
                <el-select v-model="selectValue" placeholder="Please enter a keyword" filterable remote reserve-keyword
                  :remote-method="remoteMethod" :loading="loading">
                  <el-option v-for="item in list" :key="item.value" :label="item.label" :value="item.value">
                    <span style="float: left">{{ item.label }}</span>
                    <span style="
                            float: right;
                            color: var(--el-text-color-secondary);
                            font-size: 13px;
                          ">
                      {{ item.value }}
                    </span>
                  </el-option>
                </el-select>
              </div>
              <div class="find">
                <button class="find_btn" @click="fetchData">FIND OUT</button>
              </div>
            </div>
            <div v-if="temperatureReduction" class="container_bottom">
              <div class="title_line">
                <div class="line left_line"></div>
                <div class="title_text">RESULTS</div>
                <div class="line right_line"></div>
              </div>
              <div class="results_inner">
                <div class="results_item">
                  <div class="results_item_title blue">
                    <div class="results_title_inner">HEAT REDUCTION CAPABILITIES</div>
                  </div>
                  <div class="results_item_content skyBlue">
                    <div class="results_item_content_txt">
                      The vegetation surrounding this area helps lower the temperature by
                    </div>
                    <div class="text">{{ temperatureReduction }}</div>
                  </div>
                </div>
                <div class="results_item">
                  <div class="results_item_title green">
                    <div class="results_title_inner">ABOUT THE BUILDING</div>
                  </div>
                  <div class="results_item_content skyGreen">
                    <div class="results_item_content_txt">
                      Within a 100-meter radius around the building, there is a green area spanning
                    </div>
                    <div class="text">{{ greenAreaSize }}</div>
                  </div>
                </div>
                <div class="results_item">
                  <div class="results_item_title orgin">

                    <div class="results_title_inner">BUILDING ROOFTOP</div>
                  </div>
                  <div class="results_item_content skyOrgin">
                    <div class="results_item_content_txt">
                      This building was designed with a
                    </div>
                    <div class="text">{{ roofType }}</div>
                  </div>
                </div>
                <div class="results_item">
                  <div class="results_item_title red">

                    <div class="results_title_inner">GREEN ROOF POTENTIAL</div>
                  </div>
                  <div class="results_item_content skyRed">
                    <div class="results_item_content_txt">
                      This building is ideal for a green roof installation. Download the green roof installation guide now
                    </div>
                    <div class="file">
                      <div class="img">
                        <a href="2023 Biodiversity Green Roofs Guideline.pdf">
                          <img src="@/assets/pdf1.jpg" alt="Green roof installation">
                        </a>
                      </div>
                      <div class="img">
                        <a href="2023 Biodiversity Green Roofs Guideline.pdf">
                          <img src="@/assets/pdf2.jpg" alt="Green roof installation">
                        </a>
                      </div>

                    </div>
                  </div>
                </div>
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
import footerColumn from "../components/footer-column";
import HeaderNavigation from "@/components/HeaderNavigation.vue";
import axios from 'axios';
export default {
  name: 'MyPlants',
  components: {
    footerColumn,
    HeaderNavigation
  },
  data() {
    return {
      selectValue: null,
      loading: false,
      list: [],
      temperatureReduction: '',  // for HEAT REDUCTION CAPABILITIES
      greenAreaSize: '',         // for INTERESTING TIDBIT ABOUT THE BUILDING
      roofType: ''               // for BUILDING ROOFTOP
    }
  },
  methods: {
    async remoteMethod(query) {
      if (query !== '') {
        this.loading = true;
        axios.get('https://cooldownmelbourne.com/api/search', {
          params: { key_word: query }  // 将参数从 'q' 改为 'search'
        })
          .then(response => {
            this.list = response.data.data.map(item => ({
              label: item.address, // 假设 'address' 是相关字段
              value: item.address,  // 你可能需要根据你的实际数据结构调整这些键
            }));
            this.loading = false;
          })
          .catch(error => {
            console.error('Error fetching search results:', error);
            this.loading = false;
          });
      } else {
        this.list = []
      }
    },
    fetchData() {
      // Fetch temperature reduction from the predict API
      if (this.selectValue) {
        this.loading = true;
        axios.get('https://cooldownmelbourne.com/api/search', {
          params: { key_word: this.selectValue }
        })
          .then(response => {
            const details = response.data.data[0];

            // Assuming your API sends back the data in this structure
            this.greenAreaSize = `${parseFloat(details.green_area).toFixed(2)} m2`;
            this.roofType = details.roof_type;
            this.loading = false;
          })

        axios.get('https://cooldownmelbourne.com/api/predict', {
          params: { street: this.selectValue }  // Assuming `value` is the address
        })

          .then(response => {
            console.log(response)
            this.temperatureReduction = `${parseFloat(response.data.result).toFixed(2)}° Celsius`;  // Adjust the key according to your API response
          })
          .catch(error => {
            console.error('Error fetching temperature reduction:', error);
          });
      }
    }
  }
}
</script>

<style scoped>
.coming-soon-container {
  min-height: 50vh;
  background-color: #f4f4f400;
}

.coming-soon-container img {
  max-width: 50%;
  /* Adjust as needed */
  max-height: 50%;
  /* Adjust as needed */
}

.container {
  width: 100%;
  height: auto;
  margin: 0 auto;
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
  width: 80%;
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

.container_top {
  width: 70%;
  margin: 50px auto 0 auto;
}

.subTile {
  font-size: 30px;
  font-weight: 700;
  text-align: left;
  margin-top: 80px;
}

.yellow {
  width: 100%;
  height: 150px;
  padding: 20px 0px;
  font-size: 26px;
  font-weight: 400;
  background: #85E0C4;
  border-radius: 30px;
  margin-top: 30px;
  position: relative;
  border-radius: 30px;

}

.yellow_inner {
  position: absolute;
  margin: auto;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  width: 80%;
  display: table;
  line-height: 50px;
}

.subSelect {
  margin-top: 20px;
}

.find {
  width: 100%;
  height: 70px;
  margin-top: 50px;
  margin-bottom: 50px;
}

.find_btn {
  display: block;
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
  border: none;
  margin: 0 auto;
  cursor: pointer;
}

.title_line {
  width: 100%;
  height: 86px;
  margin: 20px auto 30px auto;
  font-family: Fredoka One;
  font-size: 40px;
  position: relative;

}

.title_line .title_text {
  width: 30%;
  height: 100%;
  position: absolute;
  margin: auto;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  font-family: Fredoka One;
  font-size: 40px;
  font-weight: 600;
  line-height: 86px;
  text-align: center;
  color: #000;
}

.title_line .line {
  width: 30%;
  height: 5px;
  background: #09B845;
  position: absolute;
  margin: auto;
  top: 0;
  bottom: 0;
}

.left_line {
  left: 0;
}

.right_line {
  right: 0;
}

.container_bottom {
  width: 100%;
  height: auto;
  margin-top: 50px;
  margin-bottom: 50px;
}

.results {
  /* font-family: Inter; */
  font-size: 36px;
  font-weight: 700;
  width: 100%;
  height: 70px;
  line-height: 70px;
  border-bottom: 1px solid #000;
}

.results_inner {
  width: 80%;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.results_item {
  width: 48%;
  height: auto;
  margin-top: 50px;
  border-radius: 20px;
  /* overflow: hidden; */
}

.results_item_title {
  text-align: center;
  /* font-family: Inter; */
  font-size: 40px;
  font-weight: 700;
  color: #fff;
  border-radius: 20px 20px 0 0;
  height: 100px;
  position: relative;
}

.results_title_inner {
  display: table;
  width: 70%;
  white-space: pre-wrap;
  text-align: center;
  position: absolute;
  margin: auto;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
}

.results_item_content {
  width: auto;
  height: 351px;
  overflow: hidden;
  border-radius: 0 0 20px 20px;
}

.results_item_content_txt {
  font-size: 28px;
  font-weight: 400;
  color: #000;
  width: 90%;
  margin: 20px auto 0 auto;
}

.text {
  border: 3px solid #000;
  padding: 10px 20px;
  background: #fff;
  font-family: Inter;
  font-size: 24px;
  font-weight: 700;
  text-align: center;
  display: table;
  margin: 80px auto 0 auto;
}

.file {
  display: table;
  margin: 20px auto 0 auto;
  /* Centers the table horizontally and adds margin on top */
  width: auto;
  /* Adjust this depending on the content size */
}

.file .img {
  display: table-cell;
  /* Makes each .img behave like a table cell */
  width: 180px;
  height: 180px;
  vertical-align: middle;
  /* Aligns the content of the cell vertically */
  text-align: center;

}

.fileText {
  font-size: 16px;
  font-weight: 400;
  margin-top: 20px;
}

.Up {
  width: 0;
  height: 0;
  border-top: 20px solid transparent;
  border-right: 20px solid transparent;
  border-left: 20px solid transparent;
  border-bottom: 20px solid #000;
  position: absolute;
  margin: auto;
  bottom: 25%;
  right: 10px;
}

.blue {
  background: #3AA7E0;

}

.skyBlue {
  /* background: #A6EAFF; */
  border: 5px solid #3AA7E0;
}

.green {
  background: #3AE0AD;
}

.skyGreen {
  border: 5px solid #3AE0AD;
}

.orgin {
  background: #09BA88;
}

.skyOrgin {
  border: 5px solid #09BA88;
}

.red {
  background: #3AE03C;
}

.skyRed {
  border: 5px solid #3AE03C;
}</style>

