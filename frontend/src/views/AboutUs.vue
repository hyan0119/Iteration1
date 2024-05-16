<template>
  <div class="common-layout">
    <el-container>
        <div>
              <HeaderNavigation/>
          </div>
      <div class="filler"></div>
      <el-main class="main-content">
        <div class="coming-soon-container">
          <div class="title">
                        <img src="@/assets/card.png" alt="" class="title_more_img img_left"/>
                        ABOUT US
                        <img src="@/assets/card.png" alt="" class="title_more_img img_right"/>
              </div>
              <div class="urban">
                        <div class="urban_inner">
                            <div class="urban_inner_text">
                              We are four passionate FIT studentsthat eager to help lower the temperature in Melbourne!
                            </div>
                        </div>
              </div>
              <div class="title_line">
                  <div class="line left_line"></div>
                  <div class="title_text">PROJECT TIMELINE</div>
                  <div class="line right_line"></div>
              </div>
              <div class="line_container">
                <div class="line_container_item">
                  <div class="randor randor_top red">March 2024</div>
                  <div class="line_item line_start red"></div>
                  <div class="line_text line_text_top redC">PROPOSAL</div>
                </div>
                <div class="line_container_item">
                  <div class="randor randor_bottom orgin">April 2024</div>
                  <div class="line_item line_middle orgin"></div>
                  <div class="line_text line_text_bottom orginC">ITERATION I</div>
                </div>
                <div class="line_container_item">
                  <div class="randor randor_top yellow">April 2024</div>
                  <div class="line_item line_middle yellow"></div>
                  <div class="line_text line_text_top yellowC">ITERATION II</div>
                </div>
                <div class="line_container_item">
                  <div class="randor randor_bottom green">May 2024</div>
                  <div class="line_item line_end green"></div>
                  <div class="line_text line_text_bottom greenC">ITERATION III</div>
                </div>
              </div>
              <div class="img_container">
                <img src="@/assets/about.jpg" alt="">
              </div>
              <div class="tackle">
                <div class="tackle_title">Why Tackle Urban Heat Island Effect?</div>
                <div class="tackle_text">
                  Urban Heat Island Effect in major cities such as Melbourne are not well-known by its own residents. We aim to raise their awareness through this project
                </div>
                <div class="tackle_text">
                  We also want to provide practical solutions to ordinary Melbourne residents. Empowering them in their effort to cool down their area
                </div>
              </div>
              <div class="title_line">
                  <div class="line left_line"></div>
                  <div class="title_text">OUR CO-FOUNDERS</div>
                  <div class="line right_line"></div>
              </div>
              <div class="card">
                <div class="card_item">
                  <div class="card_item_top"></div>
                  <div class="card_item_bottom">RENTARO</div>
                </div>
                <div class="card_item">
                  <div class="card_item_top"></div>
                  <div class="card_item_bottom">HAO YANG</div>
                </div>
                <div class="card_item">
                  <div class="card_item_top"></div>
                  <div class="card_item_bottom">TING ZHOU</div>
                </div>
                <div class="card_item">
                  <div class="card_item_top"></div>
                  <div class="card_item_bottom">AGUNG</div>
                </div>
              </div>
              <div class="card_empty">
                <div class="card_empty_item">
                  <div class="card_empty_item_top">
                    <div class="card_empty_item_text">
                      MASTER OF DATA SCIENCE
                    </div>
                  </div>
                </div>
                <div class="card_empty_item">
                  <div class="card_empty_item_top">
                    <div class="card_empty_item_text">
                      MASTER OF INFORMATION TECHNOLOGY
                    </div>
                  </div>
                </div>
                <div class="card_empty_item">
                  <div class="card_empty_item_top">
                    <div class="card_empty_item_text">
                      MASTER OF DATA SCIENCE
                    </div>
                  </div>
                </div>
                <div class="card_empty_item">
                  <div class="card_empty_item_top">
                    <div class="card_empty_item_text">
                      MASTER OF BUSINESS INFORMATION SYSTEMS
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
export default {
  name: 'AboutUs',
  components: {
    footerColumn,
    HeaderNavigation
  },
}
</script>

<style scoped>
.coming-soon-container {
  width: 100%;
  margin: 0 auto;
  min-height: 50vh;
}
@import url('https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap');
.coming-soon-container .title{
  width: 100%;
  height: 150px;
  font-family: 'Fredoka One', cursive;
  font-size: 64px;
  font-weight: 600;
  line-height: 150px;
  text-align: center;
  color: #000;
  position: relative;
}
.transform{
  border-radius: 40px;
}
.title_more_img{
  width: 239px;
  height: 86px;
  position: absolute;
  margin: auto;
  top: 0;
  bottom: 0;
}
.img_left{
  left: 0;
}
.img_right{
  right: 0;
}
.urban{
  width: 100%;
  height: auto;
  margin-top: 3px;
}
.urban_inner{
  width: 40%;
  height: 100%;
  margin: 0 auto;
}
.urban_inner_text{
  font-family: 'Fredoka One', cursive;
  font-size: 32px;
  font-weight: 400;
  text-align: center;
  color: #000;
  line-height: 50px;
}
.title_line{
  width: 100%;
  height: 86px;
  margin: 100px auto  30px auto;
  font-family: 'Fredoka One', cursive;
  font-size: 40px;
  position: relative;

}
.title_line .title_text{
  width: 40%;
  height: 100%;
  position: absolute;
  margin: auto;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  font-family: 'Fredoka One', cursive;
  font-size: 58px;
  font-weight: 600;
  line-height: 86px;
  text-align: center;
  color: #000;
}
.title_line .line {
  width: 30%;
  height: 5px;
  /* background: #09B845; */
  position: absolute;
  margin: auto;
  top: 0;
  bottom: 0;
}
.left_line{
  left: 0;
}

.right_line{
  right: 0;
}
.line_container{
  width: 80%;
  height: 350px;
  margin: 50px auto 0 auto;
  display: flex;
}
.line_container_item{
  width: 25%;
  height: 100%;
  position: relative;
}
.line_item{
  width: 100%;
  height: 50px;
  position: absolute;
  margin: auto;
  top: 0;
  bottom: 0;
}
.line_start{
  border-radius: 30px 0 0 30px;
}
.line_end{
  border-radius: 0 30px 30px 0;
}

.randor{
  width: 220px;
  height: 80px;
  position: absolute;
  margin: auto;
  right: 0;
  left: 0;
  border-radius: 30px;
  white-space: wrap;
  /* font-family: Lora; */
  font-family: 'Fredoka One', cursive;
  font-size: 24px;
  font-weight: 700;
  line-height: 80px;
  text-align: center;
  color: #fff;
  /* padding-top: 25px; */
}
.randor_top{
  top: 10%;
}
.randor_bottom{
  bottom: 10%;
}
.line_text{
  width: 200px;
  height: 80px;
  line-height: 80px;
  font-family: 'Fredoka One', cursive;
  font-size: 24px;
  font-weight: 700;
  text-align: center;
  position: absolute;
  margin: auto;
  right: 0;
  left: 0;
}
.line_text_top{
  bottom: 10%;
}
.line_text_bottom{
  top: 10%;
}
.red{
  background: #CC0A11;
}
.orgin{
  background: #F98E11;
}
.yellow{
  background: #D2E315;
}
.green{
  background: #09B845;
}
.redC{
  color: #CC0A11;
}
.orginC{
  color: #F98E11;
}
.yellowC{
  color: #D2E315;
}
.greenC{
  color: #09B845;
}
.img_container{
  width: 80%;
  height: 380px;
  margin: 50px auto 0 auto;
}
.img_container img{
  width: 100%;
  height: 100%;
  border-radius: 30px;
}
.tackle{
  width: 60%;
  height: 410px;
  margin: 50px auto 0 auto;
}
.tackle_title{
  font-family: 'Fredoka One', cursive;
  font-size: 40px;
  font-weight: 600;
  text-align: center;
  color: #000;
}
.tackle_text{
  width: 55%;
  height: auto;
  padding: 20px;
  background: #3AE03C;
  font-family: 'Fredoka One', cursive;
  font-size: 24px;
  font-weight: 400;
  color: #000;
  margin: 50px auto 0 auto;
}
.card{
  width: 80%;
  height: 340px;
  margin: 50px auto 0 auto;
  display: flex;
  justify-content: space-between;
}
.card_item{
  width: 25%;
  height: 100%;
}
.card_item_top{
  width: 220px;
  height: 240px;
  border-radius: 30px;
  background: #D9D9D9;
  margin: 0 auto;
}
.card_item_bottom{
  height: 100px;
  line-height: 100px;
  color: #000;
  font-family: 'Fredoka One', cursive;
  font-size: 36px;
  font-weight: 600;
  line-height: 100px;
  text-align: center;
}
.card_empty{
  width: 80%;
  height: 340px;
  margin: 50px auto 0 auto;
  display: flex;
  justify-content: space-between;
}
.card_empty_item{
  width: 25%;
  height: 100%;
}
.card_empty_item_top{
  width: 220px;
  height: 240px;
  border-radius: 30px;
  border: 3px solid #000000;
  margin: 0 auto;
  position: relative;
}
.card_empty_item_text{
  display: table;
  position: absolute;
  margin: auto;
  top: 0;
  bottom: 0;
  font-family: 'Fredoka One', cursive;
  font-size: 26px;
  font-weight: 600;
  text-align: center;
}
</style>
<style src="./style.css"></style>
