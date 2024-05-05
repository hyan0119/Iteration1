<template>
  <div class="common-layout">
    <el-container>
      <div>
        <HeaderNavigation/>
      </div>
      <!-- <div class="filler"></div> -->
      <el-main class="main-content">
        <section class="hero-section">
          <div class="section first" style="position: relative;" >
            
              <div class="video-background">
                    <video autoplay muted loop style="background-color: rgba(0,0,0,0.3); filter: brightness(0.5);">
                      <source src="@/assets/impact_video2.mp4" type="video/mp4" >
                    </video>
                    <div class="content-and-image">
                      <div class="content">
                        <div class="content_text">
                          <h1>JOIN OUR FIGHT AGAINST URBAN HEAT ISLAND</h1>
                          <p>Let's save our city from excessive heat during the summer!</p>
                          <div class="scorll-logo">
                          <!-- <img src="@/assets/arrow_down.png" style="width: 20px; height: 20px;" alt="Logo"
                            @click="scrollToElement" /> -->
                          <el-button @click="scrollToElement">Learn More</el-button>
                        </div>
                      </div>
                        <!-- <p>&nbsp;</p> -->

                        <div class="contentToScrollTo" ref="contentToScrollTo"></div>
                      </div>
                </div>
            </div>
          </div>
       

          
          
          <div class="section section_item" id="urban-heat-effect">
            <div class="image-container">
              <img src="@/assets/city_image.png" alt="City" class="transform img-2">
              <span>Photo by Pat Wheelen on Unsplash</span>
            </div>
            <div class="content">
              <h1>URBAN HEAT ISLAND EFFECT</h1>
              <p>Urban Heat Island is a phenomenon where large urbanised areas experiencing higher temperature, more
                polluted, and posed greater risks to negative health impacts during the summer. This phenomenon is
                caused
                by
                several factors including:</p>
              <ul>
                <li>The prevalence Dark heat-absorptive surfaces in urban buildings and roads (concrete & asphalt
                  materials
                  absorb more heat than other materials).</li>
                <li>Absence of proper vegetation in the area.</li>
                <li>High number of heat-generating activities by engines & generators within the urban area.</li>
              </ul>
            </div>
          </div>

          <div class="section section_item" id="negative-impact">
            <div class="content">
              <h1>THE NEGATIVE IMPACT</h1>
              <p>Elevated temperature caused by Urban Heat Island (UHI) effect can affect communities and environment in
                multiple ways:</p>
              <ul>
                <li>Increased Energy Consumption due to prevalence of air conditioners.</li>
                <li>Rise in Air Pollutants and Greenhouse gases emissions due to surge in energy consumption.</li>
                <li>Decline in human health and well-being living in the area.</li>
                <li>Impaired Water Quality</li>
              </ul>
            </div>
            <div class="image-container">
              <img src="@/assets/home2.png" alt="City" class="transform img-3">
              <span>Photo by Chromatograph on Wnsplash</span>
            </div>
          </div>

          <div class="section section_item" id="mitigate">
            <div class="image-container">
              <img src="@/assets/home3.png" alt="City" class="transform img-4">
              <span>Photo by Chromatograph on Wnsplash</span>
            </div>
            <div class="content">
              <h1>WAYS TO MITIGATE IT</h1>
              <p>Thankfully, everyone can help to reduce the negative impact from Urban Heat Island Effect in Melbourne
                CBD.
                Here are some solutions that any Melbourne CBD resident can do to mitigate its impact:</p>
              <ul>
                <li>Grow indoor plants</li>
                <li>Grow vegetation in their home such as balcony and green roofs</li>
                <li>Reduce energy consumption</li>
                <li>Use light-coloured materials as roofs</li>
              </ul>
            </div>
          </div>
          <div class="section section_item">
            <div class="image-container">
              <div id="main" class="ecarts"></div>
            </div>
            <div class="content ecarts_content">
              <div class="text">
                <div id="context_header">Average January temperatures for five different areas of Melbourne</div>
                <p></p>
                <p></p>
                <div id="content_text">The data shows that temperatures in industrial areas and urban areas continue to rise in January (during the hot summer months), 
                while parks and farms covered by green spaces have relatively cooler temperatures, reflecting the impact of the heat island effect. 
                To mitigate this effect, measures such as increased greening and improved building materials could be considered in urban planning.</div>
              </div>
              <div class="btn" @click="goInfo">Read More 
                 <el-icon :size="20" color="#3ad345eb" class="icon">
                    <Right />
                  </el-icon>
                 </div>
            </div>
          </div>
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
  },
  methods: {
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
.content-and-image .content{
    position: absolute;
    margin: auto;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    display: table;
    font-size: 50px;

    
}
.content-and-image .content p{
  font-size: 30px;
  text-align: center;
  /* background-color: dodgerblue; */
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

.urban-heat-container {
  font-family: 'Arial', sans-serif;
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
.section_item{
  color: #000;
  width: 80%;
  margin: 20px auto  30px auto;
  display: flex;

}
.ecarts{
  width:130%;
  height: 400px;
}
.ecarts_content{
  /* background: #17b34e; */
  width: 25%;
  padding: 20px;
  margin-left: auto;
  margin-left: 80px;
}
.ecarts_content .text{
  width: 100%;
  height: auto;
  margin: 30px auto 0 auto;
  font-size: 16px;
  /* font-weight: 600; */
  /* color: #fff; */
}
.ecarts_content .btn{
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
.ecarts_content .btn .icon{
 position: absolute;
 margin: auto;
 right: 5px;
 top: 0;
 bottom: 0;
}
.section_item .image-container {
  text-align: center;
  width: 30%;
  margin-left: 5%;
  margin-right: 5%;
}
.section_item .content {
  width: 50%;
  padding: 0 40px;
}
.section_item .content h1{
  display: table;
  border-bottom: 1px solid #000;
  padding-bottom: 5px;
  font-size: 24px;
  font-weight: 600;
}
.section_item .content p{
  font-size: 20px;
}
.section_item .content ul li{
   font-size: 20px;
   margin-top: 10px;
}
.image-container img {
  width: 100%;
  height: auto;
}
.section.first{
  display: flex;
  height: calc(100vh - 80px);
  margin-bottom: 100px;
}
.contentToScrollTo{
  margin-top: 350px;
}
.section.first .content-and-image{
   width: 1200px;
}
.section.first .content{
   max-width: 60%;
}
.section.first .content h1{
   margin-bottom: 45px;
}
.section.first .content p{
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
  object-fit: cover; /* Cover the entire area of the container */
}

.scorll-logo{
  margin-top: 20px;
  margin-bottom: 20px;

}
#negative-impact{
margin-top: 50px;
}
.content{
  margin-top: 50px;
}
.image-container{
  margin-top: 50px;

}
#context_header{
  display: table;
  border-bottom: 1px solid #000;
  padding-bottom: 5px;
  font-size: 24px;
  font-weight: 600;
}
#content_text{
  font-size: 20px;
  margin-top: 10px;
}
.text{
  font-size: 20px;
   margin-top: 10px;
}
.video-background {
  background-color: rgba(0,0,0,0.4);
}

</style>
<style src="./style.css"></style>
