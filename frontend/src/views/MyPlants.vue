<template>
  <div class="common-layout">
    <el-container>
        <div>
          <HeaderNavigation/>
        </div>
      <div class="filler"></div>
      <el-main class="main-content">
        <div class="coming-soon-container">
          <div class="container">
              <div class="title">COOL CITY SOLUTIONS</div>
              <div class="sub">Check out how vegetation in the City helps reduce the heat in a particular area</div>
              <div class="container_top"> 
                <div class="subTile">Instructions</div>
                <div class="yellow">
                  <div class="yellow_inner">
                    Input a street address and discover the benefits of vegetation within a 100-meter radius of the building
                  </div>
                </div>
                 <div class="subTile">Street Address</div>
                 <div class="subSelect">
                     <el-select 
                     v-model="selectValue" 
                     placeholder="Please enter a keyword"
                     filterable
                     remote
                     reserve-keyword
                     :remote-method="remoteMethod"
                     :loading="loading"
                     >
                        <el-option
                          v-for="item in list"
                          :key="item.value"
                          :label="item.label"
                          :value="item.value"
                        >
                          <span style="float: left">{{ item.label }}</span>
                          <span
                            style="
                            float: right;
                            color: var(--el-text-color-secondary);
                            font-size: 13px;
                          "
                          >
                            {{ item.value }}
                          </span>
                        </el-option>
                      </el-select>
                 </div>
                 <div class="find">
                    <button class="find_btn" @click="fetchData">FIND OUT</button>
                 </div>
              </div>
              <!--  -->
              <div  v-if="temperatureReduction" class="container_bottom">
                <div class="results">Result</div>

                <div class="results_item">
                    <div class="results_item_title blue">
                      HEAT REDUCTION CAPABILITIES
                      <div class="Up"></div>
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
                        INTERESTING TIDBIT ABOUT THE BUILDING
                        <div class="Up"></div>
                      </div>
                      <div class="results_item_content skyGreen">
                        <div class="results_item_content_txt">
                          Within a 100-meter radius around the building, there is a green area spanning 
                        </div>
                        <div class="text">{{  greenAreaSize }}</div>
                      </div>
                  </div>
                   <div class="results_item">
                      <div class="results_item_title orgin">
                        BUILDING ROOFTOP
                        <div class="Up"></div>
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
                        GREEN ROOF POTENTIAL
                        <div class="Up"></div>
                      </div>
                      <div class="results_item_content skyRed">
                        <div class="results_item_content_txt">
                          This building is ideal for a green roof installation. Download the green roof installation guide now 
                        </div>
                        <div class="file">
                          <div class="img" >
                            <a href="2023 Biodiversity Green Roofs Guideline.pdf">
                            <img src="@/assets/pdf1.jpg" alt="Green roof installation">
                            </a>
                          </div>
                          <div class="img" >
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
      list:[],
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
.container{
  width: 1200px;
  height: auto;
  margin: 0 auto;
}
.title{
  width: 100%;
  height: 78px;
  font-size: 34px;
  font-weight: 700;
  line-height: 78px;
  text-align: center;
  margin-top: 100px;
}
.sub{
  width: 85%;
  height: auto;
  font-size: 28px;
  font-weight: 400;
  text-align: center;
  margin: 0 auto;
}
.container_top{
  width: 70%;
  margin: 50px auto 0 auto;
}
.subTile{
  font-size: 30px;
  font-weight: 700;
  text-align: left;
  margin-top: 80px;
}
.yellow{
  width: 100%;
  height: 150px;
  padding: 20px 60px;
  font-size: 26px;
  font-weight: 700;
  background: #FFD74D;
  border-radius: 30px;
  margin-top: 30px;
  position: relative;
  border-radius: 20px;
 
}
.yellow_inner{
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
.subSelect{
  margin-top: 20px;
}
.find{
  width: 100%;
  height: 70px;
  margin-top: 50px;
}
.find_btn{
  width: 180px;
  height: 50px;
  border-radius: 30px;
  background: #000;
  color: #FFF;
  font-weight: 600;
  text-align: center;
  line-height: 50PX;
  margin: 0 auto;
  cursor: pointer;
}
.container_bottom{
  width: 100%;
  height: auto;
  margin-top: 50px;
}
.results{
  /* font-family: Inter; */
  font-size: 36px;
  font-weight: 700;
  width: 100%;
  height: 70px;
  line-height: 70px;
  border-bottom: 1px solid #000;
}
.results_item{
  width: 100%;
  height: 322px;
  margin-top: 50px;
  border-radius: 20px;
}
.results_item_title{
  text-align: center;
  /* font-family: Inter; */
  font-size: 28px;
  font-weight: 700;
  position: relative;
}
.results_item_content{
  width: 100%;
  height: 251px;
  overflow: hidden;
  /* border-radius: 20px; */
}

.results_item_content_txt{
  font-size: 28px;
  font-weight: 400;
  color: #000;
  width: 90%;
  margin: 20px auto 0 auto;
}
.text{
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
.file{
  display: table;
  margin: 20px auto 0 auto; /* Centers the table horizontally and adds margin on top */
  width: auto; /* Adjust this depending on the content size */
}
.file .img{
  display: table-cell; /* Makes each .img behave like a table cell */
  width: 180px;
  height: 180px;
  vertical-align: middle; /* Aligns the content of the cell vertically */
  text-align: center;

}
.fileText{
  font-size: 16px;
  font-weight: 400;
  margin-top: 20px;
}
.Up{
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
.blue{
  background: #0BA6D7;

}
.skyBlue{
  background: #A6EAFF;
}
.green{
  background: #09B845;
}
.skyGreen{
  background: #A6FFC5;
}
.orgin{
  background: #FFA51E;
}
.skyOrgin{
  background: #F6E299;
}
.red{
  background: #FF6156;
}
.skyRed{
  background: #FFD8CF;
}
</style>

