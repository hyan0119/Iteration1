<template>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <div class="uhi-map">
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


          <div id='container' style="width: 100vw; height: 100vh;">
              <svg id='canvas'>

              </svg>
              <div id='rightSide'>


                  <div id='tooltip'>

                  </div>
                  <div id="legend_area">
                      <div id='description'>Heat Island Vulnerability Index</div>
                      <svg id='legend'>
                          <g>
                              <rect x="10" y="0" width="40" height="40" fill="#fff5e6"></rect>
                              <text x="60" y="20" fill="black">0 - Very Low</text>
                          </g>
                          <g>
                              <rect x="10" y="40" width="40" height="40" fill="#ffd699"></rect>
                              <text x="60" y="60" fill="black">1 - Low</text>
                          </g>
                          <g>
                              <rect x="10" y="80" width="40" height="40" fill="#ffc266"></rect>
                              <text x="60" y="100" fill="black">2 - Moderate</text>
                          </g>
                          <g>
                              <rect x="10" y="120" width="40" height="40" fill="#ffad33"></rect>
                              <text x="60" y="140" fill="black">3 - High</text>
                          </g>
                          <g>
                              <rect x="10" y="160" width="40" height="40" fill="#ff9900"></rect>
                              <text x="60" y="180" fill="black">4 - Very High</text>
                          </g>
                          <g>
                              <rect x="10" y="200" width="40" height="40" fill="#e68a00"></rect>
                              <text x="60" y="220" fill="black">5 - Extreme</text>
                          </g>
                      </svg>
                  </div>
              </div>

          </div>
          <div id="promotion-container">

              <div id="promotion">Are you interested in learning how you, as an individual, can contribute to making
                  your
                  suburb cooler, more comfortable, and less vulnerable to the threats posed by heatwaves? We have
                  outlined
                  features that offer solutions to the urban heat island effect – a phenomenon responsible for higher
                  temperatures in Melbourne's CBD suburbs compared to the countryside. Discover how you can help
                  reduce
                  heat
                  in your area by growing plants in your home on our 'Plant Planner' page. <br> If you would like to
                  know
                  more
                  about what is “urban heat island effect” and its potential adverse effect on your well-being, you
                  can
                  check
                  our “Urban Heat Island Encyclopedia” feature and educate yourself about the issue.</div>
          </div>
      </el-main>
      <el-footer class="footer">
          <div class="footer-top">

              <!-- Column for COOLDOWN MELBOURNE -->
              <div class="footer-section"
                  style="flex: 1; padding-right: 20px; border-right: 2px solid white; margin-right: 20px; height: 150px; display: flex; flex-direction: column; justify-content: space-between;">
                  <h2 style="color: white; margin-top: 0;">COOLDOWN MELBOURNE</h2>
                  <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-around;">
                      <p style="color: white;"><i class="el-icon-location"></i> Wellington Rd, Clayton, VIC 3800</p>
                      <p style="color: white;"><i class="el-icon-phone"></i> 0424281773</p>
                      <p style="color: white;"><i class="el-icon-message"></i> info@cooldownmelbourne.com</p>
                  </div>
              </div>

              <!-- Column for USEFUL LINKS -->
              <div class="footer-section"
                  style="flex: 1; padding-right: 20px; border-right: 2px solid white; margin-right: 20px; height: 150px; display: flex; flex-direction: column; justify-content: space-between;">
                  <h2 style="color: white; margin-top: 0;">USEFUL LINKS</h2>
                  <ul
                      style="list-style: none; padding: 0; color: white; flex-grow: 1; display: flex; flex-direction: column; justify-content: space-around;">
                      <li>Home</li>
                      <li>About Us</li>
                      <li>Service</li>
                      <li>Terms of Service</li>
                      <li>Privacy Policy</li>
                  </ul>
              </div>

              <!-- Column for FOLLOW US -->
              <div class="footer-section"
                  style="flex: 1; height: 150px; display: flex; flex-direction: column; justify-content: space-between;">
                  <h2 style="color: white; margin-top: 0;">FOLLOW US</h2>
                  <div class="social-icons"
                      style="flex-grow: 1; display: flex; flex-direction: column; justify-content: center;">
                      <i class="el-icon-facebook" style="color: white;"></i>
                      <i class="el-icon-instagram" style="color: white;"></i>
                      <!-- Replace placeholder with actual icon class -->
                      <i class="custom-icon-x" style="color: white;"></i> <!-- Placeholder for the actual icon -->
                      <i class="el-icon-linkedin" style="color: white;"></i>
                      <i class="el-icon-tiktok" style="color: white;"></i>
                  </div>
              </div>

          </div>

          <!-- Separate line for Copyright notice -->
          <div class="footer-bottom">
              <p>© Copyright Team Colon D All Rights Reserved | Designed by Monash IE Team TA 14</p>
          </div>
      </el-footer>
  </div>
</template>


<script>
import * as d3 from 'd3'
export default {
  name: 'UhiMap',
  data() {
      return {
          hviData: null
      };
  },
  mounted() {
      this.loadMapData();
  },
  methods: {
      loadMapData() {
          // 使用import引入hvi.json数据
          let hvi = '/hvi.json'

          d3.json(hvi).then(
              (data, error) => {
                  if (error) {
                      console.log('err')
                  } else {
                      this.hviData = data
                      // console.log(this.hviData)
                      this.drawMap()
                      // drawMap()
                  }
              }
          )
      },
      drawMap() {
          let selectedPath = null

          let canvas = d3.select('#canvas')
          let tooltip = d3.select('#tooltip')
          // 这里使用D3.js的代码绘制地图
          // 您需要将原始JavaScript代码适配到Vue的方法中
          var projection = d3.geoMercator()
              .fitSize([800, 800], this.hviData);

          var path = d3.geoPath()
              .projection(projection);
          // console.log(this.hviData)
          // console.log(projection)
          // console.log(path)

          canvas.selectAll("path")
              .data(this.hviData.features)
              .enter().append("path")
              .attr("d", path)
              .attr('data-fips', (d) => d.properties.id) // FIPSコードをデータ属性として追加
              .style("fill", function (d) {
                  // データに基づいた色を適用
                  if (d.properties.HVI == 0) {
                      return "#fff5e6";
                  } else if (d.properties.HVI == 1) {
                      return "#ffd699";
                  } else if (d.properties.HVI == 2) {
                      return "#ffc266";
                  } else if (d.properties.HVI == 3) {
                      return "#ffad33";
                  } else if (d.properties.HVI == 4) {
                      return "#ff9900";
                  } else if (d.properties.HVI == 5) {
                      return "#e68a00";
                  } else { return "blue" }
              })
              .style("stroke", "white")
              .style("stroke-width", 0.5)
              .on("mouseover", function (event, d) {
                  // マウスオーバー時の処理
                  // tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI)
                  // .style("left", (event.pageX + 10) + "px")
                  // .style("top", (event.pageY - 10) + "px")
                  // .style("display", "block")
                  // .style("visibility", "visible")

                  if (d.properties.HVI == 0) {
                      tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb is not vulnerable to Urban Heat Island.")
                          .style("left", (event.pageX + 10) + "px")
                          .style("top", (event.pageY - 10) + "px")
                          .style("display", "block")
                          .style("visibility", "visible")
                  } else if (d.properties.HVI == 1) {
                      tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb is slightly vulnerable to Urban Heat Island.")
                          .style("left", (event.pageX + 10) + "px")
                          .style("top", (event.pageY - 10) + "px")
                          .style("display", "block")
                          .style("visibility", "visible")
                  } else if (d.properties.HVI == 2) {
                      tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb is moderately vulnerable to Urban Heat Island.")
                          .style("left", (event.pageX + 10) + "px")
                          .style("top", (event.pageY - 10) + "px")
                          .style("display", "block")
                          .style("visibility", "visible")
                  } else if (d.properties.HVI == 3) {
                      tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb is highly vulnerable to Urban Heat Island.")
                          .style("left", (event.pageX + 10) + "px")
                          .style("top", (event.pageY - 10) + "px")
                          .style("display", "block")
                          .style("visibility", "visible")
                  } else if (d.properties.HVI == 4) {
                      tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb is extremely vulnerable to Urban Heat Island.")
                          .style("left", (event.pageX + 10) + "px")
                          .style("top", (event.pageY - 10) + "px")
                          .style("display", "block")
                          .style("visibility", "visible")
                  } else if (d.properties.HVI == 5) {
                      tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb is severely vulnerable to Urban Heat Island.")
                          .style("left", (event.pageX + 10) + "px")
                          .style("top", (event.pageY - 10) + "px")
                          .style("display", "block")
                          .style("visibility", "visible")
                  } else { return "blue" }


              })
              .on("mouseout", function (d) {
                  console.log(d)
                  // マウスアウト時の処理
                  tooltip.style("display", "none");
              })
              .on("click", function (event, d) {
                  console.log(event, d)

                  d3.select(this).style("fill", "orange");
              })
              .on("click", function (event, d) {
                  console.log(event, d)
                  // クリックされたパスの色を変更
                  if (selectedPath) {
                      // 以前に選択されたパスがある場合、その色を元に戻す
                      selectedPath.style("fill", function (d) {
                          if (d.properties.HVI == 0) {
                              return "#fff5e6";
                          } else if (d.properties.HVI == 1) {
                              return "#ffd699";
                          } else if (d.properties.HVI == 2) {
                              return "#ffc266";
                          } else if (d.properties.HVI == 3) {
                              return "#ffad33";
                          } else if (d.properties.HVI == 4) {
                              return "#ff9900";
                          } else if (d.properties.HVI == 5) {
                              return "#e68a00";
                          } else {
                              return "blue"
                          }
                      });
                  }
                  // 新しいパスの色を変更
                  d3.select(this).style("fill", "limegreen");
                  // 選択されたパスを更新
                  selectedPath = d3.select(this);




              });

          let isClicking = false; // マウスがクリックされているかどうかの状態

          canvas.on("mousedown", function () {
              isClicking = true;
          }).on("mouseup", function () {
              isClicking = false;
              console.log(isClicking)
          });
      }

  }
}
// console.log('test')

</script>

<style scoped>
/* Add your CSS styles here */

@import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro&display=swap');

*{
    font-family: 'Source Sans Pro', sans-serif;
}

html, body{
    margin: 0; /* 移除默认边距 */
    padding: 0; /* 移除默认内边距 */
    height: 100%; /* 设置为整个视口高度 */
}



svg{
    /* 图的背景色 */
    /* background-color: rgb(65, 67, 93); */
    background-color: rgba(0, 0, 0, 0.3); 
    box-shadow: 0px 3px 15px rgba(0,0,0,0.2);
    /*border-radius: 5px; */
    padding: 10px;
    border-radius: 5px;
}

#canvas{
    min-height: 700px;
    min-width: 900px;
    max-width: 900px;
    max-height: 800px;
    margin-top: 50px;
    top: 500px;

}


.county:hover{
    fill: black
}

g{
    color: #FDF1E7
}

#tooltip{
    background-color: #128ee1;
    padding: 10px;
    border-radius: 5px;
    visibility: hidden;
    height: auto;
    width: auto;
    margin-top: 2px;
    color: #FDF1E7;
    font-size: 24px;
    margin-bottom: 5px;
}

#legend{
    color: rgb(56, 58, 74);
    font-size: 20px;
    text-align: center;
    min-height: 240px;
    max-width: 180px;
    margin-top: 0px;
    margin-bottom: 0px;
}


#title{
    font-size: 28px;
    color: #FDF1E7;
    text-transform: uppercase;
    margin-top: 10px;
    margin-bottom: 30px;
}

#description a{
    text-decoration: none;
    color: #FDF1E7;
    text-align: center;
}

#container{
    display: flex;
    align-items: center;
    width: 100%;
}

#rightSide{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-left: 50px;
}

#legend_area {
    background-color: darkcyan;
    padding: 10px;
    border-radius: 5px;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
}


#promotion-container {
    display: flex;
    justify-content: center;
    align-items: center;
    /* height: 100vh; 使用视口高度，确保div在视口中垂直居中 */
  }
#promotion {
    font-family: 'Arial', sans-serif; /* 使用网站常用的字体 */
    font-size: 1em; /* 根据需要调整字号 */
    color: #f5f5f5; /* 字体颜色，选择对比度适中的颜色 */
    background-color: rgba(0, 0, 0, 0.6); /* 半透明的黑色背景，提高可读性 */
    padding: 20px; /* 文本四周的填充 */
    border-radius: 10px; /* 圆角边框 */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 轻微的阴影效果 */
    margin: 20px; /* 与其他元素的距离 */
    line-height: 1.6; /* 行间距 */
    max-width: 800px; /* 最大宽度，确保文本不会过长 */
    text-align: justify; /* 文本两端对齐 */
    max-width: 800px; /* 或您希望的宽度 */
    text-align: center; /* 文本居中 */
  }
  



.uhi-map {
display: flex;
flex-direction: column;
min-height: 100%; /* 确保至少与视口一样高 */

}



.main-content {
  width: 100% ;
}


/* @media only screen and (max-width: 600px) {
  .uhi-map {
      padding: 50px 0; 
  }
  #container, #canvas {
      width: 100%;
      height: auto; 
  }
}
  */
#canvas {
  margin-left: 15%;
}
</style>
<style src="./style.css"></style>