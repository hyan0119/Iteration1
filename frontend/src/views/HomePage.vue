<template>
  <div class="common-layout">
    <el-container>
      <div>
        <HeaderNavigation />
      </div>
      <!-- <div class="filler"></div> -->
      <el-main class="main-content">
        <section class="hero-section" >
          <div class="section first" style="position: relative;">

            <div class="video-background">
              <video autoplay muted loop style="background-color: rgba(0,0,0,0.3); filter: brightness(0.5);">
                <source src="@/assets/impact_video2.mp4" type="video/mp4">
              </video>
              <div class="content-and-image">
                <div class="content">
                  <div class="content_text">
                    <h1>JOIN OUR FIGHT AGAINST URBAN HEAT ISLAND</h1>
                    <p>Let's save our city from excessive heat during the summer!</p>
                    <div class="scorll-logo">
                      <!-- <img src="@/assets/arrow_down.png" style="width: 20px; height: 20px;" alt="Logo"
                            @click="scrollToElement" /> -->
                      <el-button @click="scrollToElement" class="more">Learn More</el-button>
                    </div>
                  </div>
                  <!-- <p>&nbsp;</p> -->

                  <div class="contentToScrollTo" ref="contentToScrollTo"></div>
                </div>
              </div>
            </div>
          </div>


          <div class="title" data-aos="fade-up">
            <img src="@/assets/card.png" alt="" class="title_more_img img_left" />
            EXPLORE WITH US!
            <img src="@/assets/card.png" alt="" class="title_more_img img_right" />
          </div>
          <div class="section section_item" id="urban-heat-effect"  data-aos="fade-left">
            <div class="image-container">
              <img src="@/assets/city_image.png" alt="City" class="transform img-2">
            </div>
            <div class="content" data-aos="fade-right">
              <h1>COOL MAP</h1>
              <p>Discover relevant Urban Heat Island Effects in your area. Learn your area’s Urban Heat Island Index level
                and tree canopies around your area. Explore practical solutions to reduce the heat in your area.</p>
              <div class="text_btn" @click="goMore(0)">Explore more</div>
            </div>
          </div>

          <div class="section section_item" id="negative-impact" data-aos="fade-up">
            <div class="content">
              <h1>PLANT PLANNER</h1>
              <p>Discover the ideal plant for your lovely home. Find out the perfect plan based on the available area and
                your commitment to water it!</p>
              <div class="text_btn" @click="goMore(1)">Explore more</div>
            </div>
            <div class="image-container" data-aos="fade-down">
              <img src="@/assets/home2.png" alt="City" class="transform img-3">
            </div>
          </div>

          <div class="section section_item" id="mitigate" data-aos="zoom-in">
            <div class="image-container">
              <img src="@/assets/home3.png" alt="City" class="transform img-4">
            </div>
            <div class="content" data-aos="zoom-in-up">
              <h1>COOL CITY SOLUTIONS</h1>
              <p>Find out how vegetation around your home help reduces the heat. Prepare to uncover how effective
                vegetation can be for heat reduction. Explore possibilities of installing green roof on your home!</p>
              <div class="text_btn" @click="goMore(2)">Explore more</div>
            </div>
          </div>


          <div class="title_more" data-aos="fade-down">
            <img src="@/assets/card.png" alt="" class="title_more_img img_left" />
            INFORMATION SECTION
            <img src="@/assets/card.png" alt="" class="title_more_img img_right" />
          </div>

          <div class="title_line" data-aos="fade-up">
            <div class="line left_line"></div>
            <div class="text">URBAN HEAT ISLAND</div>
            <div class="line right_line"></div>
          </div>
          <div class="urban" data-aos="fade-right">
            <div class="urban_inner">
              <div class="urban_inner_text">
                Urban Heat Island effect makes cities hotter, more polluted, and dangerous in summer.
              </div>
              <div class="text_btn" @click="goMore(3)">Learn more</div>
            </div>
          </div>
          <div class="CAUSES_line" data-aos="fade-left">
            <div class="line left_line"></div>
            <div class="text">WHAT CAUSES URBAN HEAT ISLAND?</div>
            <div class="line right_line"></div>
          </div>
          <div class="card" data-aos="fade-up">
            <div class="card_item">
              <img src="@/assets/card_01.jpg" alt="">
              <div class="card_text">Photo by Inna Mikova on Unsplash</div>
              <div class="air">
                AIR POLLUTION
              </div>
              <div class="card_content" data-aos="zoom-in">
                Abundance of air pollution & dark building materials in the city trap heat in the city
              </div>
            </div>
            <div class="card_item" data-aos="zoom-in">
              <img src="@/assets/card_02.jpg" alt="">
              <div class="card_text">Photo from Freepik</div>
              <div class="air">
                DECLINING VEGETATION SPACE
              </div>
              <div class="card_content" data-aos="zoom-in">
                Less vegetation leads to less evapotranspiration and cool shades.
              </div>
            </div>
            <div class="card_item" data-aos="zoom-in">
              <img src="@/assets/card_03.jpg" alt="">
              <div class="card_text">Photo by Chromatograph on Unsplash</div>
              <div class="air">
                EXCESSIVE ENERGY USAGE
              </div>
              <div class="card_content" data-aos="zoom-in">
                Excessive energy consumption generates heat as byproduct.
              </div>
            </div>
          </div>
          <div class="more_btn" data-aos="fade-up">
            <div class="more_btn_text" @click="goMore(3)">Learn more</div>
          </div>
          <div class="CAUSES_line NEGATIVE" data-aos="fade-left">
            <div class="line left_line"></div>
            <div class="text">NEGATIVE IMPACTS OF URBAN HEAT ISLAND</div>
            <div class="line right_line"></div>
          </div>
          <div class="NEGATIVE_card" data-aos="fade-right">
            <div class="NEGATIVE_card_inner">
              <div class="NEGATIVE_card_box">
                <div class="NEGATIVE_card_item" data-aos="zoom-in">
                  <img src="@/assets/icon_01.jpg" alt="" class="NEGATIVE_icon">
                  <div class="NEGATIVE_text">
                    Temperature continuing to rise and cause health issues
                  </div>
                </div>
                <div class="NEGATIVE_card_item" data-aos="zoom-in">
                  <img src="@/assets/icon_02.jpg" alt="" class="NEGATIVE_icon">
                  <div class="NEGATIVE_text">
                    Lower people’s well-being and health condition
                  </div>
                </div>
              </div>
              <div class="NEGATIVE_card_box">
                <div class="NEGATIVE_card_item" data-aos="zoom-in">
                  <img src="@/assets/icon_03.jpg" alt="" class="NEGATIVE_icon">
                  <div class="NEGATIVE_text">
                    Impaired Water Quality
                  </div>
                </div>
                <div class="NEGATIVE_card_item" data-aos="zoom-in">
                  <img src="@/assets/icon_04.jpg" alt="" class="NEGATIVE_icon">
                  <div class="NEGATIVE_text">
                    The extra heat increases energy usage and energy bills
                  </div>
                </div>
              </div>
            </div>
            <div class="more_btn">
              <div class="NEGATIVE_btn_text" @click="goMore(3)">Learn more</div>
            </div>
          </div>
          <div class="CAUSES_line MITIGATION" data-aos="fade-left">
            <div class="line left_line"></div>
            <div class="text">MITIGATION EFFORT</div>
            <div class="line right_line"></div>
          </div>
          <div class="MITIGATION_content" data-aos="fade-up">
            <div class="MITIGATION_item">
              <img src="@/assets/line_01.jpg" alt="">
              <div class="MITIGATION_item_text">
                <p>Grow vegetation at home, whether on a balcony, rooftop, or indoors</p>
              </div>
            </div>
            <div class="MITIGATION_tip">Photo by Jonathan Kemper on Unsplash</div>
            <div class="MITIGATION_item">
              <img src="@/assets/line_02.jpg" alt="">
              <div class="MITIGATION_item_text">
                <p>Install Cool Roof / Green Roof</p>
              </div>
            </div>
            <div class="MITIGATION_tip">Photo by Tommy Kwak on Unsplash</div>
            <div class="MITIGATION_item">
              <img src="@/assets/line_03.jpg" alt="">
              <div class="MITIGATION_item_text">
                <p>Reduce Energy Consumption</p>
              </div>
            </div>
            <div class="MITIGATION_tip">Photo by Kelly Sikkema on Unsplash</div>
            <div class="MITIGATION_item">
              <img src="@/assets/line_04.jpg" alt="">
              <div class="MITIGATION_item_text">
                <p>Use Sustainable Transportation</p>
              </div>
            </div>
            <div class="MITIGATION_tip">Photo by Daniel Pelaez Duque on Unsplash</div>
            <div class="more_btn">
              <div class="MITIGATION_btn_text" @click="goMore(3)">Learn more</div>
            </div>
          </div>
          <div class="CAUSES_line MITIGATION" data-aos="fade-left">
            <div class="line left_line"></div>
            <div class="text">VISUALISATION</div>
            <div class="line right_line"></div>
          </div>
          <div class="echarts_title" data-aos="fade-up">
            Average Temperature Across Five Different types of Locations around Melbourne - January
          </div>
          <div class="echarts_content" data-aos="fade-right">
            <div id="main" class="ecarts"></div>
            <div class="echarts_content_box" data-aos="fade-left">
              <ul>
                <li>The temperature at industrial areas continues to rise indicating increasing air pollution.</li>
                <li>The temperature at urban areas such as densely populated city/town continues to be higher than 32°C.
                </li>
                <li>Melbourne’s rural areas’ temperature is lower compared to that of urban and industrial areas. </li>
                <li>This significant temperature differences between urban and rural areas is known as “Urban Heat Island
                  Effect”</li>
              </ul>
            </div>
            <div class="more_btn" data-aos="fade-up">
              <div class="NEGATIVE_btn_text" @click="goMore(3)">Learn more</div>
            </div>
          </div>
          <div class="block"></div>
        </section>
      </el-main>
      <footer-column></footer-column>
    </el-container>
  </div>
</template>

<script>
import footerColumn from "../components/footer-column";
import HeaderNavigation from "@/components/HeaderNavigation.vue";
import * as echarts from 'echarts';
export default {
  name: 'HomePageNew',
  components: {
    footerColumn,
    HeaderNavigation
  },
  data() {
    return {

    }
  },
  mounted() {
    this.getEcharts()
    this.$aos.refresh();
  },
  methods: {
    goMore(index) {
      if (index == 0) {
        this.$router.push("/uhi-map")
      } else if (index == 1) {
        this.$router.push("/plant-planner")
      } else if (index == 2) {
        this.$router.push("/my-plants")
      } else if (index == 3) {
        this.$router.push("/info-page")
      }

    },
    getEcharts() {
      var chartDom = document.getElementById('main');
      var myChart = echarts.init(chartDom);
      var option;

      option = {
        title: {
          text: ''
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          top: '10%',
          data: ['Rural', 'Residential', 'Industrial', 'Town/City', 'Park', 'Farms']
        },
        toolbox: {
          show: true,
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            dataView: { readOnly: false },
            magicType: { type: ['line', 'bar'] },
            restore: {},
            saveAsImage: {}
          }
        },
        grid: {
          left: '3%',
          top: '30%',
          right: '5%',
          bottom: '0%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: ['2019', '2020', '2021', '2022', '2023', '2024']
        },
        yAxis: {
          type: 'value',
          min: 25,
          max: 35,
          axisLabel: {
            formatter: '{value} °C'
          }
        },
        series: [
          {
            name: 'Rural',
            type: 'line',
            data: [27.0, 27.4, 27.8, 28.2, 28.6, 29.0]
          },
          {
            name: 'Residential',
            type: 'line',
            data: [28.1, 28.5, 28.9, 29.3, 29.7, 30.1]
          },
          {
            name: 'Industrial',
            type: 'line',
            data: [32.3, 32.5, 32.7, 32.9, 33.1, 33.3]
          },
          {
            name: 'Town/City',
            type: 'line',
            data: [33.5, 33.3, 33.1, 32.9, 32.7, 32.5]
          },
          {
            name: 'Park',
            type: 'line',
            data: [31.2, 31.0, 30.8, 30.6, 30.4, 30.2]
          },
          {
            name: 'Farms',
            type: 'line',
            data: [30.0, 29.6, 29.2, 28.8, 28.4, 28.0]
          }
        ]
      };

      option && myChart.setOption(option);
    },
    scrollToElement() {
      // 使用 `this.$refs` 来获取模板中的元素
      const element = this.$refs.contentToScrollTo;

      // 使用 `scrollIntoView` 方法来平滑滚动到该元素
      element.scrollIntoView({ behavior: 'smooth' });
    },
    goInfo() {
      this.$router.replace("/info-page")
    }
  }
}
</script>

<style scoped>
.content-and-image {
  /* position: absolute; */
  margin: auto;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  text-align: center;
}

.content-and-image .content {
  position: absolute;
  margin: auto;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  display: table;
  font-size: 50px;
  font-family: 'Fredoka One', cursive;
  font-weight: 600;


}

.content-and-image .content p {
  font-size: 30px;
  text-align: center;
  /* background-color: dodgerblue; */
  font-family: 'Fredoka One', cursive;
  font-weight: lighter;
}

/* .content-and-image .content_text{
  background-color: rgba(9, 134, 28, 0.9);
  border-radius: 10px;
  padding: 10px;
  margin-top: 100px
} */
.content-and-image .text-content {
  /* 文本内容占用可用空间 */
  padding-right: 20px;
  align-items: center;
  display: flex;
  flex-direction: column;
  /* 以列的方式排列子元素 */
  align-items: center;
  /* 水平居中对齐子元素 */
  justify-content: center;
  /* 在文本和图片之间添加一些间隔 */
}

.content-and-image .content .scorll-logo {
  display: flex;
  flex-direction: column;
  /* 以列的方式排列子元素 */
  align-items: center;
  /* 水平居中对齐子元素 */
  justify-content: left;
  /* 如果需要，也可以在垂直方向上居中 */

}

.content-and-image .image-container {
  flex: 1;
  /* 图片内容也占用可用空间 */
  text-align: center;
  /* 图片居中显示 */
}


.image-container {
  text-align: center;
}

.image-container img {
  max-width: 100%;
  height: auto;
}

.image-container span {
  display: block;
  font-size: 12px;
  color: #666;
  text-align: center;
  margin-top: 10px;
}

.main-content {
  padding-top: 0px;
  /* 设置一个与头部高度相等的顶部边距 */
  color: white;
  /* height: 600px; */
}
@import url('https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap');
.urban-heat-container {
  font-family: 'Fredoka One', cursive;
  margin: 0 auto;
  width: 90%;
  max-width: 1200px;
  /* Adjust this value based on your design */
}

.section {
  margin-bottom: 2em;
  display: flex;
  align-content: center;
  justify-content: center;
}

.section_item {
  color: #000;
  width: 80%;
  margin: 20px auto 30px auto;
  display: flex;

}


.ecarts_content {
  /* background: #17b34e; */
  width: 25%;
  padding: 20px;
  margin-left: auto;
  margin-left: 80px;
}

.ecarts_content .text {
  width: 100%;
  height: auto;
  margin: 30px auto 0 auto;
  font-size: 16px;
  /* font-weight: 600; */
  /* color: #fff; */
  font-family: 'Fredoka One', cursive;
}

.ecarts_content .btn {
  width: 140px;
  height: 50px;
  border-radius: 50px;
  background: #fff;
  color: rgba(9, 134, 28);
  font-size: 16px;
  text-align: center;
  line-height: 50px;
  margin-top: 30px;
  cursor: pointer;
  position: relative;
}

.ecarts_content .btn .icon {
  position: absolute;
  margin: auto;
  right: 5px;
  top: 0;
  bottom: 0;
}

.section_item .content {
  width: 50%;
  padding: 0 40px;
  font-family: 'Fredoka One', cursive;
}

.section_item .content h1 {
  width: 100%;
  display: block;
  /* border-bottom: 1px solid #000; */
  padding-bottom: 5px;
  font-size: 50px;
  font-weight: 600;
  text-align: center;
  margin: 0;
  padding: 0;
}

.section_item .content p {
  width: 80%;
  margin: 30px auto 0 auto;
  font-family: 'Fredoka One', cursive;
  font-size: 32px;
  font-weight: 400;
  line-height: 38px;
  text-align: left;

}

.section_item .content ul li {
  font-size: 20px;
  margin-top: 10px;
  font-family: 'Fredoka One', cursive;
}

.image-container img {
  width: 100%;
  height: auto;
}

.section.first {
  display: flex;
  height: calc(100vh - 80px);
  margin-bottom: 100px;
}

.contentToScrollTo {
  margin-top: 350px;
}

.section.first .content-and-image {
  width: 1200px;
}

.section.first .content {
  max-width: 60%;
}

.section.first .content h1 {
  margin-bottom: 45px;
}

.section.first .content p {
  margin-bottom: 30px;
}

.section.first .image-container {
  margin-right: 0;
}

.section.first .image-container img {
  width: 100%;
}

.video-background {
  position: absolute;
  top: 80px;
  width: 100%;
  height: 100%;
}

.video-background video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  /* Cover the entire area of the container */
}

.scorll-logo {
  margin-top: 20px;
  margin-bottom: 20px;

}

#negative-impact {
  margin-top: 50px;
}

.content {
  margin-top: 50px;
}

.image-container {
  margin-top: 50px;

}

#context_header {
  display: table;
  border-bottom: 1px solid #000;
  padding-bottom: 5px;
  font-size: 24px;
  font-weight: 600;
}

#content_text {
  font-size: 20px;
  margin-top: 10px;
}

.text {
  font-size: 20px;
  margin-top: 10px;
}

.video-background {
  background-color: rgba(0, 0, 0, 0.4);
}

.more {
  background: transparent;
  border: 1px solid #FFFFFF;
  border-radius: 25px;
  width: 200px;
  height: 50px;
  line-height: 50px;
  text-align: center;
  color: #fff;
  font-weight: 600;
  font-size: 1rem;
  font-family: "Fredoka One", cursive;
}

.title {
  width: 100%;
  height: 200px;
  font-family: 'Fredoka One', cursive;
  font-size: 50px;
  font-weight: 600;
  line-height: 200px;
  text-align: center;
  color: #000;
  position: relative;
}

.transform {
  border-radius: 40px;
}

.text_btn {
  width: 220px;
  height: 66px;
  border-radius: 30px;
  background: #09B845;
  color: #fff;
  font-family: 'Fredoka One', cursive;
  font-size: 24px;
  font-weight: 400;
  line-height: 66px;
  text-align: center;
  margin: 30px auto 0 auto;
  cursor: pointer;
}

.title_more {
  width: 100%;
  height: 200px;
  margin: 20px auto 30px auto;
  font-family: 'Fredoka One', cursive;
  font-size: 50px;
  font-weight: 600;
  line-height: 200px;
  text-align: center;
  color: #000;
  border-top: 5px solid #09B845;
  position: relative;
  margin-top: 100px;
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

.title_line {
  width: 100%;
  height: 86px;
  margin: 20px auto 30px auto;
  font-family: 'Fredoka One', cursive;
  font-size: 40px;
  position: relative;

}

.title_line .text {
  width: 30%;
  height: 100%;
  position: absolute;
  margin: auto;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  font-family: 'Fredoka One', cursive;
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

.urban {
  width: 100%;
  height: 300px;
  margin-top: 50px;
}

.urban_inner {
  width: 50%;
  height: 100%;
  margin: 0 auto;
}

.urban_inner_text {
  font-family: 'Fredoka One', cursive;
  font-size: 36px;
  font-weight: 400;
  text-align: center;
  color: #000;
  line-height: 50px;
}

.CAUSES_line {
  width: 100%;
  height: 86px;
  margin: 20px auto 30px auto;
  font-family: 'Fredoka One', cursive;
  font-size: 40px;
  position: relative;

}

.CAUSES_line .text {
  width: 40%;
  height: 100%;
  position: absolute;
  margin: auto;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  font-family: 'Fredoka One', cursive;
  font-size: 50px;
  font-weight: 600;
  line-height: 60px;
  text-align: center;
  color: #000;
}

.CAUSES_line .line {
  width: 25%;
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

.card {
  width: 100%;
  height: auto;
  margin-top: 100px;
  display: flex;
  justify-content: space-around;
}

.card_item {
  width: 25%;
  height: auto;
  border: 4px solid #09B845;
  border-radius: 30px;
  padding: 20px;
}

.card_item img {
  height: 600px;
  width: 100%;
}

.card_text {
  font-family: 'Fredoka One', cursive;
  font-size: 12px;
  text-align: center;
  color: #000;
  margin: 10px 0;
}

.air {
  width: 100%;
  height: auto;
  color: #000;
  font-family: 'Fredoka One', cursive;
  font-size: 30px;
  font-weight: 1000;
  line-height: 30px;
  text-align: center;
  background: #09B845;
  border-radius: 30px;
  padding: 30px 0px;
  white-space: pre-wrap;
}

.card_content {
  font-family: 'Fredoka One', cursive;
  font-size: 28px;
  font-weight: 400;
  line-height: 40px;
  text-align: center;
  color: #000;
  margin-top: 30px;
}

.more_btn {
  width: 100%;
  height: 50px;
  margin-top: 80px;
}

.more_btn_text {
  width: 190px;
  height: 56px;
  margin: 0 auto;
  color: #09B845;
  text-align: center;
  line-height: 56px;
  font-family: 'Fredoka One', cursive;
  font-size: 24px;
  font-weight: 600;
  color: #fff;
  border-radius: 30px;
  cursor: pointer;
}

.NEGATIVE {
  margin-top: 80px;
}

.NEGATIVE_card {
  width: 100%;
  height: auto;
  margin-top: 100px;
}

.NEGATIVE_card_inner {
  width: 70%;
  margin: 0 auto;
}

.NEGATIVE_card_box {
  display: flex;
  justify-content: space-between;
}

.NEGATIVE_card_item {
  width: 43%;
  height: 277px;
  border: 4px solid #09B845;
  border-radius: 30px;
  padding: 20px;
  margin-top: 80px;

}

.NEGATIVE_icon {
  width: 50px;
  height: 50px;
}

.NEGATIVE_text {
  font-family: 'Fredoka One', cursive;
  font-size: 28px;
  font-weight: 400;
  text-align: center;
  color: #000;
  margin-top: 10px;
}

.NEGATIVE_btn_text {
  width: 190px;
  height: 56px;
  margin: 0 auto;
  background: #09B845;
  text-align: center;
  line-height: 56px;
  font-family: 'Fredoka One', cursive;
  font-size: 24px;
  font-weight: 600;
  color: #fff;
  border-radius: 30px;
  cursor: pointer;
}

.MITIGATION {
  margin-top: 80px;
}

.MITIGATION_content {
  width: 80%;
  margin: 50px auto 0 auto;
}

.MITIGATION_item {
  width: 100%;
  height: 210px;
  border-radius: 30px;
  border: 4px #09B845;
  display: flex;
}

.MITIGATION_item img {
  width: 50%;
  height: 100%;
  border-radius: 30px;
}

.MITIGATION_item_text {
  position: relative;
  width: 50%;
}

.MITIGATION_item_text p {
  display: table;
  position: absolute;
  margin: auto;
  left: 0;
  bottom: 0;
  top: 0;
  right: 0;
  font-family: 'Fredoka One', cursive;
  font-size: 28px;
  text-align: center;
  color: #000;
}

.MITIGATION_tip {
  width: 100%;
  color: #000;
  font-family: 'Fredoka One', cursive;
  font-size: 12px;
  text-align: left;
  margin: 20px 0;
  padding-left: 200px;
}

.MITIGATION_btn_text {
  width: 190px;
  height: 56px;
  margin: 0 auto;
  color: #09B845;
  text-align: center;
  line-height: 56px;
  font-family: 'Fredoka One', cursive;
  font-size: 24px;
  font-weight: 600;
  color: #fff;
  border-radius: 30px;
  cursor: pointer;
}

.echarts_title {
  width: 80%;
  margin: 0 auto;
  font-family: 'Fredoka One', cursive;
  font-size: 38px;
  font-weight: 600;
  text-align: center;
  color: #000;
}

.echarts_content {
  width: 100%;
  margin: 50px auto 0 auto;
  padding-bottom: 80px;
  border-bottom: 4px solid #09B845;
}

.ecarts {
  width: 60%;
  height: 400px;
  margin: 0 auto;
}

.echarts_content_box {
  width: 60%;
  margin: 30px;
  height: auto;
  border: 6px solid #09B845;
  padding: 40px 20px;
  border-radius: 30px;
  margin: 50px auto 0 auto;
}

.echarts_content_box ul {
  width: 90%;
  height: 100%;

}

.echarts_content_box ul li {
  font-family: 'Fredoka One', cursive;
  font-size: 32px;
  font-weight: 400;
  line-height: 38.72px;
  text-align: left;
  color: #000;
}

.block {
  height: 50px;
}

</style>
<style src="./style.css"></style>