<template>
  <div class="common-layout" ref="contentData">
    <el-container>
      <div>
        <HeaderNavigation />
      </div>
      <div class="filler"></div>
      <el-main class="main-content">
        <div class="coming-soon-container">
          <div class="title" data-aos="fade-up">
            <img src="@/assets/card.png" alt="" class="title_more_img img_left" />
            ADDITIONAL INFORMATION
            <img src="@/assets/card.png" alt="" class="title_more_img img_right" />
          </div>
          <div class="urban" data-aos="fade-right">
            <div class="urban_inner">
              <div class="urban_inner_text">
                Are you confused about which information to trust regarding Urban Heat Island Effect? Check out our
                reliable sources.
              </div>
            </div>
          </div>
          <div class="artles">
            <div class="title_line" data-aos="fade-left">
              <div class="line left_line"></div>
              <div class="title_text">ARTICLES</div>
              <div class="line right_line"></div>
            </div>
            <div class="artles_content" data-aos="fade-up">
              <div class="artles_item" v-for="(item, index) in artlesData" :key="index" @click="artlesClick(item)">
                <div class="artles_item_img" data-aos="zoom-in">
                  <img :src="item.img" alt="" class="item_img">
                </div>
                <div class="artles_item_title">{{ item.title }}</div>
                <div class="artles_item_content">
                  <div v-for="(items, indexs) in item.list" :key="indexs" class="artles_content_item">
                    <span class="label">By:</span>
                    <span class="value">{{ items.text }}</span>
                  </div>
                  <div class="artles_item_btn">READ MORE</div>
                </div>
              </div>
            </div>
          </div>
          <div class="videos">
            <div class="videos_title">VIDEOS</div>
            <div class="videos_content">
              <div class="videos_content_top">
                <iframe width="100%" height="100%" :src="mainUrl" title="YouTube video player" frameborder="0"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                  referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
              </div>
              <div class="videos_content_bottom">
                <vue-seamless-scroll :data="listData" :class-option="classOption" class="warp">
                  <ul class="ul-item">
                    <li class="li-item" v-for="(item, index) in listData" :key="index">
                      <div class="dialog" @click="videoClick(item)"></div>
                      <iframe width="100%" height="100%" :src="item.url" title="YouTube video player" frameborder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                    </li>
                  </ul>
                </vue-seamless-scroll>
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
import vueSeamlessScroll from "vue-seamless-scroll/src"  // vue3引入方式
import footerColumn from "../components/footer-column";
import HeaderNavigation from "@/components/HeaderNavigation.vue";
import img1 from "@/assets/assets_/img/2.png";
import img2 from "@/assets/assets_/img/1.png";
import img3 from "@/assets/assets_/img/3.png";
import img4 from "@/assets/assets_/img/4.png";
import img5 from "@/assets/assets_/img/5.png";
import img6 from "@/assets/assets_/img/6.png";
export default {
  name: 'MyPlants',
  components: {
    footerColumn,
    HeaderNavigation,
    vueSeamlessScroll
  },
  data() {
    return {
      artlesData: [
        {
          img: img1,
          title: "Heat Island Impacts",
          url: "https://www.epa.gov/heatislands/heat-island-impacts",
          list: [
            {
              text: "U.S. Environmental Protection Agency"
            },

          ]
        },
        {
          img: img2,
          title: "Using Trees and Vegetation to Reduce Heat Islands",
          url: "https://www.epa.gov/heatislands/using-trees-and-vegetation-reduce-heat-islands",
          list: [
            {
              text: "U.S. Environmental Protection Agency"
            },

          ]
        },
        {
          img: img3,
          title: "Learn About Heat Islands",
          url: "https://www.epa.gov/heatislands/learn-about-heat-islands",
          list: [
            {
              text: "U.S. Environmental Protection Agency"
            },

          ]
        },
        {
          img: img4,
          url: "https://www.abc.net.au/news/2023-10-21/dark-roofs-raising-the-heat-in-australian-new-suburbs/102990304",
          title: "Is The Sea Of Dark Roofs Raising The Heat In Australia'S New Suburbs?",
          list: [
            {
              text: "ABC News"
            },

          ]
        },
        {
          img: img5,
          url: "https://www.abc.net.au/news/2021-03-11/australians-face-unliveable-cities-less-greenspace-heat/13231068",
          title: "Australians Face A Hotter Future If Our Cities Don'T Do More To Cool 'Heat Islands', Report Finds",
          list: [
            {
              text: "ABC News"
            },
          ]
        },
        {
          img: img6,
          url: "https://link.springer.com/article/10.1007/s40572-017-0150-3",
          title: "The Urban Heat Island: Implications for Health in a Changing Environment",
          list: [
            {
              text: "Heaviside, C., Macintyre, H. & Vardoulakis, S."
            },
          ]
        },
      ],
      listData: [
        {
          url: "https://www.youtube.com/embed/PM101DvvG4Q?si=pCam9bFWzGSZwNw4"
        },
        {
          url: "https://www.youtube.com/embed/sWzfIy3wVAs?si=B8DaYx52jfZwIWDq"
        },
        {
          url: "https://www.youtube.com/embed/Y-bVwPRy_no?si=MDao-HybMFVL2s3c"
        },
        {
          url: "https://www.youtube.com/embed/ZQ6fSHr5TJg?si=qWUjNqSEI4-r7xMz"
        },
        {
          url: "https://www.youtube.com/embed/4SihdPRRMPI?si=RreyWSeVuXo_lVsU"
        },
      ],
      mainUrl: "https://www.youtube.com/embed/PM101DvvG4Q?si=pCam9bFWzGSZwNw4",
      classOption: {
        step: 0.5, // 数值越大速度滚动越快
        limitMoveNum: 2, // 开始无缝滚动的数据量
        hoverStop: true, // 是否开启鼠标悬停stop
        direction: 2, // 0向下 1向上 2向左 3向右
        openWatch: true, // 开启数据实时监控刷新dom
        singleHeight: 0, // 单步运动停止的高度(默认值0是无缝不停止的滚动) direction => 0/1
        singleWidth: 0, // 单步运动停止的宽度(默认值0是无缝不停止的滚动) direction => 2/3
        waitTime: 1000, // 单步运动停止的时间(默认值1000ms)
      }
    }
  },
  mounted() {
    this.$nextTick(() => {
      // 设置滚动行为改为平滑的滚动
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
      this.$nextTick(() => {
      this.$aos.refresh();
    });
    })
    console.log(11111)
  },
  methods: {
    artlesClick(item) {
      console.log(item)
      window.open(item.url, '_blank')
    },
    videoClick(item) {
      this.mainUrl = item.url;
      this.$nextTick(() => {
      });
    },
  }
}
</script>

<style scoped>
.coming-soon-container {
  width: 100%;
  margin: 0 auto;
  min-height: 50vh;
}

.coming-soon-container .title {
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
  width: 80%;
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

.title_line {
  width: 100%;
  height: 86px;
  margin: 20px auto 30px auto;
  font-family: 'Fredoka One', cursive;
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

.subTile {
  width: 100%;
  font-weight: 500;
  font-size: 24px;
  /* color: #999; */
  margin-top: 30px;
  text-align: center;
}

.artles,
.videos {
  width: 100%;
  margin-top: 80px;
  padding-bottom: 50px;
}

.artles_title,
.videos_title {
  width: 100%;
  height: 50px;
  font-weight: 600;
  font-size: 26px;
  color: #000;
  text-align: center;
  line-height: 50px;
}

.artles_content,
.videos_content {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  margin-top: 30px;
  padding: 0 50px;
}

.artles_item {
  width: 32%;
  height: 995px;
  margin-top: 30px;
  cursor: pointer;
  border: 4px solid #09B845;
  border-radius: 30px;
}

.artles_item_img {
  width: 80%;
  height: 400px;
  margin: 50px auto 0 auto;
}

.item_img {
  width: 100%;
  height: 100%;
  border-radius: 30px;
}

.artles_item_title {
  width: 80%;
  height: auto;
  font-family: 'Fredoka One', cursive;
  font-weight: 600;
  font-size: 32px;
  color: #000;
  text-align: center;
  line-height: 40px;
  margin: 50px auto;
}

.artles_item_content {
  margin-top: 30px;
  padding: 0 20px;
}

.artles_content_item {
  width: 90%;
  margin: 0 auto;
  font-family: 'Fredoka One', cursive;
  font-size: 28px;
  font-weight: 0;
  color: #000;
}

.artles_content_item .value {
  margin-left: 10px;
}

.artles_item_btn {
  width: 208px;
  height: 59px;
  margin: 50px auto 0 auto;
  background: #09B845;
  border-radius: 30px;
  font-family: 'Fredoka One', cursive;
  font-size: 28px;
  font-weight: 700;
  line-height: 59px;
  text-align: center;
  color: #fff;
}

.videos_content_top {
  width: 100%;
  height: 500px;
  background: #000000eb;
  margin-top: 30px;
  display: flex;
  justify-content: space-between;
  border-radius: 10px;
}

.videos_content_top_img {
  width: 50%;
  height: 100%;
  border-radius: 10px;
  position: relative;
}

.videos_content_top_img span {
  position: absolute;
  left: 30px;
}

.videos_content_top_img .num {
  font-size: 24px;
  font-weight: 600;
  color: #fff;
  bottom: 100px;
}

.videos_content_top_img .num {
  font-size: 24px;
  font-weight: 600;
  color: #fff;
  bottom: 100px;
}

.videos_content_top_img .title {
  font-size: 18px;
  font-weight: 600;
  color: #fff;
  bottom: 60px;
  text-align: left;
}

.videos_content_top_text {
  width: 50%;
  height: 100%;
  padding: 20px;
}

.videos_content_top_text .title {
  display: flex;
  width: 100%;
  height: 30px;
  font-size: 18px;
  font-weight: 600;
  line-height: 30px;
  color: #fff;
}

.videos_content_top_text .title .line {
  width: 10px;
  height: 100%;
  display: block;
  background: red;
}

.videos_content_top_text .title .text {
  margin-left: 10px;
}

.videos_content_bottom {
  width: 100%;
  height: 120px;
  margin-top: 30px;
}

.videos_content_top_text .txt {
  color: #fff;
  line-height: 25px;
  text-indent: 20px;
  font-size: 14px;
  margin-top: 10px;
}

.warp {
  width: 100%;
  height: 120px;
  margin: 0 auto;
  overflow: hidden;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0 auto;
}

.warp .ul-item {
  display: flex;
}

.li-item {
  width: 200px;
  height: 120px;
  margin-right: 10px;
  line-height: 120px;
  color: #fff;
  text-align: center;
  font-size: 30px;
  position: relative;
}

.dialog {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 99999;
  cursor: pointer;
}

.videos_title {
  width: 100%;
  height: 50px;
  font-weight: 600;
  font-size: 40px;
  color: #000;
  text-align: center;
  line-height: 50px;
  font-family: 'Fredoka One', cursive;
}
</style>