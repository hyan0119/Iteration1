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

<!-- HVI map content -->
<!-- Starting here -->
    <div id='title'>Melbourne Urban Heat Island Vulnerability Map</div>
    <div id="intro">Find out the Urban Heat Island Vulnerability (UHI) index across Melbourne CBD’s suburbs.</div>
    <!-- <div id='title'>Melbourne Urban Heat Island Vulnerability Map</div> -->

    <div id='container'>

        <div id='leftSide'>

            <div id="legendArea">
                <div id = 'legendTitle'>HVI</div>
                <svg id='legend'>
                    <g>
                        <rect x="10" y="0" width="40" height="40" fill="#fff5e6"></rect>
                        <text x="60" y="20" fill="white">0 Vey Low</text>
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
                <div id='description'>
                    description text here!
                </div>

                <!-- <div id='description'>
                    Urban Heat Island (UHI) is a phenomenon where urban areas experience higher temperatures than their rural surroundings. This is due to the high concentration of buildings, roads, and other heat-absorbing structures in cities. The Urban Heat Island Vulnerability Index (HVI) is a measure of how vulnerable a region is to the effects of UHI. This map shows the HVI of Melbourne, Australia, with darker shades indicating higher vulnerability.
                </div> -->
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
                        // let tooltip_base = 
                        tooltip.html("You have selected <br><br>" + "Suburb: " + d.properties.SA2_NAME16 + "<br>" + "HVI: " + d.properties.HVI)
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
                        tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Heat Vulnerability Index (HVI): " + d.properties.HVI)
                        .style("display", "block")
                        .style("visibility", "visible");
                    } 
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
    min-height: 100%
}

/* body {
    background-color: #2A2D2D;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: #FDF1E7;
    margin: none;
} */

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
    margin-top: 2px;
    color: #FDF1E7;
    font-size: 24px;
    margin-bottom: 5px;
    background-color: darkcyan;
    border-radius: 5px;
    position: relative;
    padding: 20px;
    margin-right: 0px;

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
    font-size: 28px;
    color: #FDF1E7;
    text-transform: uppercase;
    margin-top: 130px;
    margin-bottom: 30px;
    text-align: center;
}

#description {
    text-decoration: none;
    color: #FDF1E7;
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
    background-color: darkcyan;
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
}

#legendArea{
    display: flex;
    flex-direction: column;
    align-items: top;
    margin-top: 20px;
    margin-bottom: 20px;
    background-color: darkcyan;
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
    font-size: 18px;
    color: #FDF1E7;
    text-align: center;
    margin-top: 10px;
    margin-bottom: 10px;
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
</style>
<!-- <style src="./style.css"></style> -->