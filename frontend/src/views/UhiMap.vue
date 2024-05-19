<template>
    <div class="uhi-map">
        <div>
            <HeaderNavigation />
        </div>
        <el-main class="main-content">
            <!-- <div id="map"></div> -->
            <h1 style="text-align: center;">UHI Map</h1>
            <h2 style="text-align: center;">Urban Heat Island Map</h2>
            <!-- <h3>Instructions</h3> -->
            <div id="instrcution">
                <div>Hover over a suburb to see the Heat Vulnerability Index (HVI) of that suburb.</div>
                <div>Click on a suburb to zoom in and see the HVI of that suburb.</div>
            </div>
            <div style="text-align: center;">
<<<<<<< HEAD
                <button id="reset" @click="handleButtonClick">Reset</button>
<<<<<<< Updated upstream
=======
                <button id="reset" @click="handleButtonClick">Reset View</button>
>>>>>>> main
=======
                <button id="swith" @click="switchMap">Switch View</button>
>>>>>>> Stashed changes
            </div>
            <!-- < @click="goMore(0)">Explore more</div> -->
            <!-- <button @click="switchMap">switch view</button> -->

            <!-- <div id="test"></div> -->
            <div id="map"></div>
        </el-main>
        <footer-column>

        </footer-column>
    </div>
</template>
    
<script>
import L from 'leaflet';
import footerColumn from "../components/footer-column";
import HeaderNavigation from "@/components/HeaderNavigation.vue";
import 'leaflet/dist/leaflet.css';

export default {
    name: 'UhiMap',
    components: {
        footerColumn,
        HeaderNavigation
    },
    data() {
        return {
            hviData: null,
            map: null
        };
    },
    mounted() {
        this.loadMapData();
    },
    methods: {
        loadMapData() {
            let hvi = '/output_file.geojson';

            fetch(hvi)
                .then(response => response.json())
                .then(data => {
                    this.hviData = data;
                    this.initMap();
                })
                .catch(error => {
                    console.log('Error loading map data:', error);
                });
        },
        initMap() {
            this.map = L.map('map').setView([-37.8136, 144.9631], 10);

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
                maxZoom: 19,
            }).addTo(this.map);

            function style(feature) {
                return {
                    fillColor: getColor(feature.properties.HVI),
                    fillOpacity: 0.1,
                    weight: 2,
                    color: 'white'
                };
            }

            L.geoJson(this.hviData).addTo(this.map);

            function getColor(hvi) {
                if (hvi == 0) {
                    return "#fff5e6";
                } else if (hvi == 1) {
                    return "#ffd699";
                } else if (hvi == 2) {
                    return "#ffc266";
                } else if (hvi == 3) {
                    return "#ffad33";
                } else if (hvi == 4) {
                    return "#ff9900";
                } else if (hvi == 5) {
                    return "#e68a00";
                } else {
                    return 'blue';
                }
            }

            function style(feature) {
                return {
                    fillColor: getColor(feature.properties.HVI),
                    fillOpacity: 0.7,
                    weight: 1,
                    color: 'white'
                };
            }
            L.geoJson(this.hviData, { style: style }).addTo(this.map);

            function highlightFeature(e) {
                var layer = e.target;

                layer.setStyle({
                    weight: 5,
                    color: '#666',
                    dashArray: '',
                    fillOpacity: 0.2
                });

                if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
                    layer.bringToFront();
                }

                imf.update(layer.feature.properties);
            }

            function resetHighlight(e) {
                geojson.resetStyle(e.target);
                imf.update();
            }

            // function zoomToFeature(e) {
            //     this.map.fitBounds(e.target.getBounds());
            // }

            var geojson;
            // geojson = L.geoJson();

            function onEachFeature(feature, layer) {
                layer.on({
                    mouseover: highlightFeature,
                    mouseout: resetHighlight,
                    click: highlightFeature
                });
            }

            geojson = L.geoJson(this.hviData, {
                style: style,
                onEachFeature: onEachFeature.bind(this)
            }).addTo(this.map);

            var imf = L.control({ position: 'topright' });

            imf.onAdd = function (map) {
                this._div = L.DomUtil.create('div', 'imf'); // create a div with a class "imf"
                this.update();
                return this._div;
            };

            // method that we will use to update the control based on feature properties passed
            imf.update = function (props) {


                if (props) {
                    var label_txt = "";
                    var exposure = "";
                    var mitigation = "";
                    var growing = "";
                    var verdict = "";
                    if (props.HVI == 0) {
                        label_txt = "Low";
                        exposure = "It is typically safe outdoors during peak hot summer times, but remember to stay hydrated and take sun precautions"
                        mitigation = "While not urgent, planting trees for shade and using light-colored materials for buildings can enhance comfort in the area."
                        growing = "Additional vegetation is not truly necessary in this area, but you can still choose to do so."
                        verdict = "This area is at low risk of heat vulnerability."

                    } else if (props.HVI == 1) {
                        label_txt = "Low-Moderate";
                        exposure = "It is typically safe outdoors during peak hot summer times, but remember to stay hydrated and take sun precautions"
                        mitigation = "While not urgent, planting trees for shade and using light-colored materials for buildings can enhance comfort in the area."
                        growing = "Additional vegetation is not truly necessary in this area, but you can still choose to do so."
                        verdict = "This area is at low-moderate risk of heat vulnerability."
                    } else if (props.HVI == 2) {
                        label_txt = "Moderate";
                        exposure = "Those with health conditions or heat sensitivity should take extra care while in this area, limiting outdoor activities during the hottest hours and seeking shade when possible"
                        mitigation = "While not urgent, planting trees for shade and using light-colored materials for buildings can enhance comfort in the area."
                        growing = "Additional vegetation is not truly necessary in this area, but you can still choose to do so."
                        verdict = "This area is at moderate risk of heat vulnerability."
                    } else if (props.HVI == 3) {
                        label_txt = "Moderate-High";
                        exposure = "It is advisable to minimize prolonged outdoor exposure, especially for vulnerable groups like the elderly and children in this area. If outdoor activities are necessary, opt for cooler early morning or late evening hours"
                        mitigation = "Reducing heat here would be vital. You might want to consider adding green spaces, implementing cool roofs, and encouraging the use of reflective materials."
                        growing = "Consider growing plants in this area as a means to reduce the heat if you reside here."
                        verdict = "This area is at moderate-high risk of heat vulnerability."
                    } else if (props.HVI == 4) {
                        label_txt = "High";
                        exposure = "It is advisable to minimize prolonged outdoor exposure, especially for vulnerable groups like the elderly and children in this area. If outdoor activities are necessary, opt for cooler early morning or late evening hours"
                        mitigation = "Reducing heat here would be vital. You might want to consider adding green spaces, implementing cool roofs, and encouraging the use of reflective materials."
                        growing = "Consider growing plants in this area as a means to reduce the heat if you reside here."
                        verdict = "This area is at high risk of heat vulnerability."
                    } else if (props.HVI == 5) {
                        label_txt = "Very High";
                        exposure = "It is advisable to minimize prolonged outdoor exposure, especially for vulnerable groups like the elderly and children in this area. If outdoor activities are necessary, opt for cooler early morning or late evening hours"
                        mitigation = "Reducing heat here would be vital. You might want to consider adding green spaces, implementing cool roofs, and encouraging the use of reflective materials."
                        growing = "Consider growing plants in this area as a means to reduce the heat if you reside here."
                        verdict = "This area is at very high risk of heat vulnerability."
                    }
                }



                this._div.innerHTML = '<h4>Urban Heat Vulnerability Map</h4>' + (props ?
<<<<<<< HEAD
                     '<b>' + "Suburb:  " + props.SA2_NAME16 + '</b><br/>' + 'HVI:  ' + props.HVI + '</b><br/>' + 'Verdict:  ' + verdict + '</b><br/>' + '<div id="suburb-info">' + "<h4>Recommendations</h4>" +'</div>'+  'Exposure:  ' + exposure + '</b><br/>' + 'Mitigation:  ' + mitigation + '</b><br/>' + 'Growing:  ' + growing
=======
                    '<b>' + "Suburb:  " + props.SA2_NAME16 + '</b><br/>' + 'HVI:  ' + props.HVI + '</b><br/>' + 'Verdict:  ' + verdict + '</b><br/>' + "<h4>Recommendations</h4>" + '</b><br/>' + 'Exposure:  ' + exposure + '</b><br/>' + 'Mitigation:  ' + mitigation + '</b><br/>' + 'Growing:  ' + growing
>>>>>>> main
                    : 'Hover over a suburb');
            };

            imf.addTo(this.map);

            var lgd = L.control({ position: 'bottomleft' });
            lgd.onAdd = function (map) {
                var div = L.DomUtil.create('div', 'imf lgd'),
                    grades = [0, 1, 2, 3, 4, 5],
                    labels = ["Very Low", "Low", "Moderate", "High", "Very High", "Extreme"];
                div.innerHTML += '<h4>Heat Vulnerability Index</h4>';

                // loop through our density intervals and generate a label with a colored square for each interval
                for (var i = 0; i < grades.length; i++) {
                    div.innerHTML +=
                        '<i style="background:' + getColor(grades[i]) + '"></i> ' +
                        grades[i] + ' ' + (grades[i + 1] ? '&ndash;' + ' ' + grades[i + 1] + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"  +labels[i] +'<br>' : '+' + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" +labels[i] +'<br>');
                }
                return div;
            };
            lgd.addTo(this.map);









        },

        // handleButtonClick() {
        //     this.map.setView([-37.8136, 144.9631], 10)
        //     // Write your code here
        // },

        // switchMap() {
        //     const getCurrentLocation = () => {
        //         if (navigator.geolocation) {
        //             navigator.geolocation.getCurrentPosition(position => {
        //                 const { latitude, longitude } = position.coords;
        //                 const marker = L.marker([latitude, longitude]).addTo(this.map);
        //                 this.map.setView([latitude, longitude], 13);
        //             }, error => {
        //                 console.log('Error getting current location:', error);
        //             });
        //         } else {
        //             console.log('Geolocation is not supported by this browser.');
        //         }
        //     }
        //     getCurrentLocation.call(this);
        // },

        handleButtonClick() {
            //reset view
            this.map.setView([-37.8136, 144.9631], 10);

        },

        switchMap() {
            // Disable animations
            if (this.map) {
                this.map.options.zoomAnimation = false;
                this.map.remove();
            }

            // Initialize new map container
            this.map = L.map('map', { zoomAnimation: true }).setView([-37.8136, 144.9631], 14);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
            maxZoom: 19,
            }).addTo(this.map);

            let canopy = '/tree.geojson';
            fetch(canopy)
            .then(response => response.json())
            .then(data => {
                this.canopy = data;
                L.geoJson(this.canopy, {
                pointToLayer: function (feature, latlng) {
                    return L.circleMarker(latlng, {
                    radius: 5,
                    fillColor: "green",
                    color: "#000",
                    weight: 1,
                    opacity: 1,
                    fillOpacity: 0.8
                    });
                },
                onEachFeature: function (feature, layer) {
                    layer.bindPopup(feature.properties.common_name);
                }


                
                }).addTo(this.map);

            })
            .catch(error => {
                console.log('Error loading map data:', error);
            });
        },





    }
};

</script>

<style src="./style.css"></style>
    
<style>
/* Add your CSS styles here */

.menu-item {
    font-size: 1.3rem !important;
    font-family: 'Fredoka One', cursive;
}

#map {
    /* top: 0;
    bottom: 0;
    left: 0;
    right: 0; */
    border: 2px solid white;
    /* margin: 75px; */
    /* width: 500px;
    height: 500px; */
    /* position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%); */
    width: auto;
    height: 700px;
    margin: 50px;
    position: relative;
    z-index: 0;

}

#instrcution {
    width: 50%;
    margin-right: auto;
    margin-left: auto;
    text-align: center;
    background-color: #11ad48;
    padding: 20px;
    border-radius: 10px;
    font-size: 20px;
    color: white;
}

.imf {
    /* font: 20px/30px Arial, Helvetica, sans-serif; */
    font-family: 'fredoka one', cursive;
    background: white;
    background: rgba(255, 255, 255, 0.8);
<<<<<<< HEAD
    padding: 10px;
    border-radius: 20px;
    text-align: center;
    max-width: 350px;
    margin: 0 auto;
    font-size: 17px;
=======
    padding: 20px;
    border-radius: 5px;
    text-align: center;
    max-width: 400px;
    margin: 0 auto;
>>>>>>> main
    
}

.imf h4 {
    margin: 0 0 5px;
    font-size: 25px;
    /* color: #777; */
    background: #09B845;
    border-radius: 20px;
    padding: 10px;
    color: #fff;
}

h2 {
    font-size: 40px;
}

h3 {
    font-size: 30px;
    text-align: center;

}

.lgd {
<<<<<<< HEAD
    /* line-height: 18px; */
    /* color: #555; */
    background: white;
    padding: 10px;
    border-radius: 20px;
=======
    line-height: 18px;
    color: #555;
    background: white;
>>>>>>> main
}

.lgd i {
    width: 18px;
    height: 18px;
    float: left;
    margin-right: 8px;
    opacity: 0.9;
}

#reset {
  width: 150px;
  height: 66px;
  border-radius: 30px;
  background: #09B845;
  color: #fff;
  font-family: 'Fredoka One', cursive;
  font-size: 20px;
  font-weight: 400;
  border: none;
  outline: none;
  line-height: 66px;
  text-align: center;
  margin: 30px auto 0 auto;
  cursor: pointer;
  margin-right: 20px;

}

#swith {
  width: 150px;
  height: 66px;
  border-radius: 30px;
  background: #09B845;
  color: #fff;
  font-family: 'Fredoka One', cursive;
  font-size: 20px;
  font-weight: 400;
  border: none;
  outline: none;
  line-height: 66px;
  text-align: center;
  margin: 30px auto 0 auto;
  cursor: pointer;
  margin-left: 20px;

}

<<<<<<< HEAD
/* .imf #suburb-info {
    font-size: 25px;
    font-family: 'Fredoka One', cursive;
    font-weight: 400;
    color: #000;

    background: #09B845;
    border-radius: 20px;
    padding: 10px;
    margin: 0 0 5px;
} */

=======
>>>>>>> main
/* #test {
        width: 1000px;
        height: 700px;
    } */
</style>
    
<<<<<<< HEAD

=======
>>>>>>> main

