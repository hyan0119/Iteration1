<template>
    <!-- <meta name="viewport" content="width=device-width, initial-scale=1"> -->
    <div class="uhi-map">
        <div>
            <HeaderNavigation/>
          </div>
        <el-main class="main-content">
  
  <!-- HVI map content -->
  <!-- Starting here -->
      <div id='title'>Melbourne Urban Heat Vulnerability Map</div>
      <div id="intro">Find out the Urban Heat Vulnerability Index (UHVI) across Melbourne CBD</div>
      <div id="explain">The Urban Heat Vulnerability Index (UHVI) assesses areas in cities vulnerable to extreme heat by evaluating factors like green space and infrastructure.</div>
      <!-- <div id='title'>Melbourne Urban Heat Island Vulnerability Map</div> -->
  
    <div id='container'>

        <div id='leftSide'>

            <div id="legendArea">
                <div id = 'legendTitle'>UHVI</div>
                <svg id='legend'>
                    <g>
                        <rect x="10" y="0" width="40" height="40" fill="#fff5e6"></rect>
                        <text x="60" y="20" fill="white">0 Very Low</text>
                    </g>
                    <g>
                        <rect x="10" y="40" width="40" height="40" fill="#ffd699"></rect>
                        <text x="60" y="60" fill="white">1 Low</text>
                    </g>
                    <g>
                        <rect x="10" y="80" width="40" height="40" fill="#ffc266"></rect>
                        <text x="60" y="100" fill="white">2 Moderate</text>
                    </g>
                    <g>
                        <rect x="10" y="120" width="40" height="40" fill="#ffad33"></rect>
                        <text x="60" y="140" fill="white">3 High</text>
                    </g>
                    <g>
                        <rect x="10" y="160" width="40" height="40" fill="#ff9900"></rect>
                        <text x="60" y="180" fill="white">4 Very High</text>
                    </g>
                    <g>
                        <rect x="10" y="200" width="40" height="40" fill="#e68a00"></rect>
                        <text x="60" y="220" fill="white">5 Extreme</text>
                    </g>
                </svg>
            </div>
            <svg id='canvas'>
            </svg>
            <div id="leftPane">
                <!-- <div id='description'>
                    description text here!
                </div> -->
                <div id = 'instruction_title'>
                    <div id='w'>Instruction<br></div>
                    <div id = 'instruction'>
                        <div id = 'instruction_1'> •⁠   ⁠Hover over suburbs on the map for information.</div>
                        <div id = 'instruction_2'> •⁠   ⁠Click a suburb to pin the information box on your screen.</div>
                        <div id = 'instruction_3'> •⁠   ⁠Click “reset” to unpin the information box.</div>
                    </div>

                </div>

                <div id='tooltip'>
    
                </div>
                <button id="resetButton">Reset</button>

            </div>
    </div>
  
          
  
          
  
  
          
      </div>
  
  <!-- view contets end here -->
  
  
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
                    our “Urban Heat Island Encyclopedia” feature and educate yourself about the issue. <button><a href="/info-page">Click here to learn more</a></button></div>
            </div>
        </el-main>
        <footer-column></footer-column>
    </div>
  </template>
  
  
  <script>
  import * as d3 from 'd3';
  import footerColumn from "../components/footer-column";
  import HeaderNavigation from "@/components/HeaderNavigation.vue";
  export default {
      name: 'UhiMap',
      components: {
        footerColumn,
        HeaderNavigation
      },
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
                              // this.resetMap()
                          }
                      }
                  )
              },
              drawMap() {
                  //   let selectedPath = null
                      
  
                  let canvas = d3.select('#canvas')
                  let tooltip = d3.select('#tooltip')
                  // 这里使用D3.js的代码绘制地图
                  // 您需要将原始JavaScript代码适配到Vue的方法中
                  var projection = d3.geoMercator().fitSize([700, 700], this.hviData);
  
                  // Description: create a path generator
                  var path = d3.geoPath().projection(projection);
                  // console.log(this.hviData)
                      // console.log(projection)
                      // console.log(path)
                  let resetButton = d3.select('#resetButton');
                  resetButton.style("display", "none");
  
                  
                  canvas.selectAll("path")
                  .data(this.hviData.features)
                  .enter()
                  .append("path")
                  .attr("d", path)
                  .attr("data-fips", (d) => d.properties.id)
                  .style("fill", function(d) {
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
                          return "blue";
                      }
                  })
                  .style("stroke", "green")
                  .style("stroke-width", 0.8)
                  .style("cursor", "pointer")
                  .style("border", "1px solid black")
                  .style("box-shadow", "0px 0px 10px rgba(0, 0, 0, 0.5)")
                  .on("click", function(event, d) {
  
  
                      if (d3.select(this).style("fill") !== "darkcyan") {
                          // Add your code here for when the path is not clicked
                        let tooltip_base = "You have selected: <br><br>" + "Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Heat Vulnerability Index (HVI): " + d.properties.HVI + "<br><br>";
                          
                        if (d.properties.HVI == 0) {
                            tooltip_base += "Not vulnerable to Urban Heat Island";
                        } else if (d.properties.HVI == 1) {
                            tooltip_base += "Slightly vulnerable to Urban Heat Island";
                        } else if (d.properties.HVI == 2) {
                            tooltip_base += "Moderately vulnerable to Urban Heat Island";
                        } else if (d.properties.HVI == 3) {
                            tooltip_base += "Highly vulnerable to Urban Heat Island";
                        } else if (d.properties.HVI == 4) {
                            tooltip_base += "Severely vulnerable to Urban Heat Island";
                        } else if (d.properties.HVI == 5) {
                            tooltip_base += "Extremely vulnerable to Urban Heat Island";
                        }

                        //   tooltip.html("You have selected <br><br>" + "Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Heat Vulnerability Index (HVI): " + d.properties.HVI)
                          tooltip.html(tooltip_base)
                          .style("display", "block")
                          .style("visibility", "visible")
                          .style("text-align", "center");
  
                          canvas.selectAll("path")
                              .style("fill", function(d) {
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
                                      return "blue";
                                  }
                                  
                              })
  
                              d3.select(this)
                              .style("fill", "darkcyan");
  
                              if (d3.select(this).style("fill") == "darkcyan"){
                                  
                                  resetButton.style("display", "block");
                                  resetButton.style('visibility', 'visible');
                                  resetButton.on('click', function(){
                                      canvas.selectAll("path")
                                      .style('fill', function(d){
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
                                              return "blue";
                                          }
                                      })
  
                                  })
  
  
                              }
  
                          }    
                  })
                  .on("mouseover", function(event, d) {
                      if (d3.selectAll('path').filter(function() { return d3.select(this).style("fill") === "darkcyan"; }).size() < 1) {
                        let tooltip_base = "Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Heat Vulnerability Index (HVI): " + d.properties.HVI + "<br><br>";
                          
                        if (d.properties.HVI == 0) {
                            tooltip_base += "Not vulnerable to Urban Heat Island";
                        } else if (d.properties.HVI == 1) {
                            tooltip_base += "Slightly vulnerable to Urban Heat Island";
                        } else if (d.properties.HVI == 2) {
                            tooltip_base += "Moderately vulnerable to Urban Heat Island";
                        } else if (d.properties.HVI == 3) {
                            tooltip_base += "Highly vulnerable to Urban Heat Island";
                        } else if (d.properties.HVI == 4) {
                            tooltip_base += "Severely vulnerable to Urban Heat Island";
                        } else if (d.properties.HVI == 5) {
                            tooltip_base += "Currently extremely vulnerable to Urban Heat Island";
                        }

                        //   tooltip.html("You have selected <br><br>" + "Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Heat Vulnerability Index (HVI): " + d.properties.HVI)
                          tooltip.html(tooltip_base)
                          .style("display", "block")
                          .style("visibility", "visible")
                      } 
                  });
                  
   
  
  
  
              }
  
  
  
  
  
  
          }
  }
  </script>
<style scoped>
    .menu-item {
        font-size: 1.3rem !important;
    }
</style>
  <style scoped>
    /* Add your CSS styles here */
  
  @import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro&display=swap');
  

  
  html, body{
      min-height: 100%
  }
  

  
  svg{
      /* background-color: #305555; */
      /*box-shadow: 0px 3px 15px rgba(0,0,0,0.2); */
      /*border-radius: 5px; */
      padding: 10px;
      border-radius: 20px;
      margin: auto;
  }
  
  #canvas{
      /* min-height: 00px;
      min-width: 600px; */
      height: 750px;
      width: 750px;
      margin-right: 0px;
      margin-left: 0px;
      margin-right: 0px;
      /* margin: auto;
      inset: 0;
      position: absolute; */
      /* top: 50%;
      left: 50%;
      transform: translate(-50%, -50%); */
  }
  
  g{
      color: #FDF1E7
  }
  
  #tooltip{
      visibility: hidden;
      height: auto;
      width: auto;
      margin-top: 20px;
      color: #FDF1E7;
      font-size: 24px;
      margin-bottom: 5px;
      background-color: darkcyan;
      border-radius: 5px;
      padding: 20px;
      /* margin-right: 0px; */
  
  }
  
  #legend{
      color: rgb(56, 58, 74);
      font-size: 18px;
      text-align: center;
      height: 240px;
      width: 150px;
      text-align: center;
  
      display: flex;
      flex-direction: column;
      align-items: center;
      /* margin-left: 50px; */
      margin-right: 0px;
      margin-left: 0px;
  
  }
  
  
  
  #title{
      font-size: 50px;
      background: linear-gradient(90deg, #58c6ff 0%, #076ad9 40%, #ff3bef 90%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-transform: uppercase;
      margin-top: 130px;
      margin-bottom: 0px;
      text-align: center;
  }
  
  #description {
      text-decoration: none;
      color: #58c6ff;
      text-align: center;
      margin: auto;
  }
  
  #leftSide{
      display: flex;
      /* flex-direction: column; */
      justify-content: center;
      align-items: center;
      /* margin-left: 200px;
      margin-right: 200px; */
      margin-top: 0px;
      margin-bottom: 0px;
      align-self: center;
  }
  
  #resetButton{
      background-color: #58c6ff;
      border: none;
      padding: 10px;
      border-radius: 5px;
      margin-top: 10px; 
      margin-bottom: 10px;
      cursor: pointer;
      align-items: center;
      display: flex;
      justify-content: center;
      align-self: center;
      color: black;
  }
  
  #legendArea{
      display: flex;
      flex-direction: column;
      align-items: top;
      margin-top: 20px;
      margin-bottom: 20px;
      /* background: linear-gradient(180deg, rgb(255, 214, 153) 0%, #076ad9 40%, #ff3bef 90%); */
      background: darkcyan;
    
      border-radius: 5px;
      justify-content: center;
      align-items: top;
      margin-left: 0px;
      margin-right: 0px;
      text-align: center;
      /* padding: 10px; */
      }
  
  #legendTitle{
      font-size: 25px;
      color: #FDF1E7;
      margin-top: 10px;
      margin-bottom: 10px;
  }
  
  
  
  
  #intro{
      font-size: 30px;
      color: #000;
      text-align: center;
      margin-top: 0px;
      margin-bottom: 40px;
      margin-left: 200px;
      margin-right: 200px;
  }
  
  #container{
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      /* margin-left: 200px;
      margin-right: 200px; */
      margin-top: 0px;
      margin-bottom: 0px;
      align-self: center;
  }
  
  #leftPane{
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      /* margin-left: 200px;
      margin-right: 200px; */
      margin-top: 0px;
      margin-bottom: 0px;
      align-self: center;
  }

  #promotion{
        font-size: 18px;
        color: #000;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 10px;
        margin-left: 200px;
        margin-right: 200px;
  }
  #promotion a{
    color: #076ad9;
  }

  #instruction{
      /* font-size: 18px; */
      color: darkcyan;
      text-align: left;
      /* margin-top: 10px;
      margin-bottom: 10px;
      margin-left: 200px;
      margin-right: 200px; */

  }

  #instruction_title{
      font-size: 30px;

      color: #FDF1E7;
      text-align: center;
      margin-top: 10px;
      /* margin-bottom: 10px; */
      margin-bottom: 30px;
      background-color: darkcyan;
      border-radius: 5px;
      padding: 20px;
      width: 450px;
      margin-bottom: 0px;
  }

  #instruction_1{
      font-size: 20px;
      color: #FDF1E7;
      text-align: left;
      margin-top: 10px;
      margin-bottom: 10px;
  }
  #instruction_2{
      font-size: 20px;
      color: #FDF1E7;
      text-align: left;
      margin-top: 10px;
      margin-bottom: 10px;
  }
  #instruction_3{
      font-size: 20px;
      color: #FDF1E7;
      text-align: left;
      margin-top: 10px;
      margin-bottom: 10px;
  }

  #explain{
        font-size: 20px;
        color: #000;
        text-align: center;
        margin-top: 0px;
        margin-bottom: 40px;
        margin-left: 200px;
        margin-right: 200px;
  }


  </style>

  <style src="./style.css"></style>