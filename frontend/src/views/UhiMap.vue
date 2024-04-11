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
                    d3.select(this).style("fill", "pink");
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

.title h2 {
    margin: 0;
    font-size: 36px;
}

.title p {
    margin-top: 20px;
    font-size: 18px;
}



.map {
    margin-top: 20px;
}

.uhi-map {
    text-align: center;
    padding: 100px 0;
    background-color: #f4f4f4;
    background-size: contain;
    background-size: 150%;
    background-repeat: no-repeat;
    background-position: center;
}

body, html {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
}

@media only screen and (max-width: 600px) {
    .uhi-map {
        padding: 50px 0; /* Adjust the padding for smaller screens */
    }
    #container, #canvas {
        width: 100%; /* Make the map fill the width of the container */
        height: auto; /* Adjust height automatically */
    }
}
#canvas {
    margin-left: 15%;
} 
</style>
<style src="./style.css"></style>
<style src="./uhi_map.css"></style>