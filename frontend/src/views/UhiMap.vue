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
                <div style="font-family: 'Fredoka', cursive;">Hover over a suburb to see the information of that suburb.</div>
                <div style="font-family: 'Fredoka', cursive;">Click on HVI and Green Area Coverage buttons to switch maps</div>
                <div style="font-family: 'Fredoka', cursive;">Click on Reset View button to reset the position of the map</div>
            </div>
            <div style="text-align: center;">
                <button id="reset" @click="handleButtonClick">Reset View</button>
                <button id="test" @click="defaultMap">HVI</button>
                <button id="switch_view" @click="switchMap">Green Area Coverage</button>


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
            map: null,
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
            this.map = L.map('map').setView([-37.8136, 145.2], 10);

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
                    "<h5>" + '<b>' + "<div id='elmnt'>" + "Suburb:  " + "</div>"+ props.SA2_NAME16 + '</b><br/>' + "<div id='elmnt'>" + 'HVI:  ' + "</div>" + props.HVI + '</b><br/>' + "<div id='elmnt'>" + 'Verdict:  ' + "</div>" + verdict + '</b><br/>' + "</h5>"  + "<h4>Recommendations</h4>" + "<h5>" + "<div id='elmnt'>" +'Exposure:  ' + "</div>"+ exposure + '</b><br/>' + "<div id='elmnt'>" + 'Mitigation:  ' +"</div>"+ mitigation + '</b><br/>' + "<div id='elmnt'>" +'Growing:  ' +"</div>"+ growing + "</h5>"
                    : "<h5>" + 'Hover over a suburb' + "</h5>");
            };

            imf.addTo(this.map);

            var lgd = L.control({ position: 'bottomleft' });
            lgd.onAdd = function (map) {
                var div = L.DomUtil.create('div', 'imf lgd'),
                    grades = [0, 1, 2, 3, 4, 5],
                    labels = ["Low", "Low-Moderate", "Moderate", "Moderate-High", "High", "Very High"];
                div.innerHTML += '<h4>Heat Vulnerability Index</h4>';

                // loop through our density intervals and generate a label with a colored square for each interval
                for (var i = 0; i < grades.length; i++) {
                    div.innerHTML +=
                        '<i style="background:' + getColor(grades[i]) + '"></i> ' + "<h5>" +
                        grades[i] + ' ' + (grades[i + 1] ? '&ndash;' + ' ' + grades[i + 1] + '&nbsp;' + '&nbsp;' + '&nbsp;' +'&nbsp;' +'&nbsp;' +'&nbsp;' +'&nbsp;' +'&nbsp;' + labels[i] + '<br>' +"</h5>" : '+' +  '&nbsp;' + '&nbsp;' + '&nbsp;' +'&nbsp;' +'&nbsp;' +'&nbsp;' +'&nbsp;' +'&nbsp;'  + labels[i] + '<br>');
    
                }
                return div;
            };
            lgd.addTo(this.map);









        },

        // handleButtonClick() {
        //     this.map.setView([-37.8136, 144.9631], 10)
        //     // Write your code here
        // },

        // handleButtonClick() {
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
            this.map.setView([-37.8136, 145.2], 10);

        },

        switchMap() {
            //switch view
            this.map.remove();
            this.map = L.map('map').setView([-37.8136, 145.2], 10);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
            maxZoom: 19,
            }).addTo(this.map);
            fetch('/vege.geojson')
            .then(response => response.json())
            .then(data => {
                // L.geoJson(data, {
                //     style: {
                //         // fillColor: 'green',
                //         // fillOpacity: 0.7,
                //         // weight: 1,
                //         // color: 'white'
                //     }
                // }).addTo(this.map);

            //     function style(feature) {
            //     return {
            //         fillColor: getColor(feature.properties.HVI),
            //         fillOpacity: 0.1,
            //         weight: 2,
            //         color: 'white'
            //     };
            // }

            L.geoJson(data).addTo(this.map);

            function getColorV(hvi) {
                if (hvi == "Very Low") {
                    return "#CCFF33";
                } else if (hvi == "Low") {
                    return "#9EF01A";
                } else if (hvi == "Moderate") {
                    return "#70E000";
                } else if (hvi == "High") {
                    return "#008000";
                } else if (hvi == "Very High") {
                    return "#004b23";
                } else {
                    return '#004b23';
                }
            }

            function style1(feature) {
                return {
                    fillColor: getColorV(feature.properties.label),
                    fillOpacity: 0.7,
                    weight: 1,
                    color: 'white'
                };
            }
            L.geoJson(data, { style: style1 }).addTo(this.map);

            function highlightFeature1(e) {
                var layer = e.target;

                layer.setStyle({
                    weight: 5,
                    // color: '#666',
                    dashArray: '',
                    fillOpacity: 0.2
                });

                if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
                    layer.bringToFront();
                }

                imf.update(layer.feature.properties);
            }

            function resetHighlight1(e) {
                geojson.resetStyle(e.target);
                imf.update();
            }

            // function zoomToFeature(e) {
            //     this.map.fitBounds(e.target.getBounds());
            // }

            var geojson;
            // geojson = L.geoJson();

            function onEachFeature1(feature, layer) {
                layer.on({
                    mouseover: highlightFeature1,
                    mouseout: resetHighlight1,
                    click: highlightFeature1
                });
            }

            geojson = L.geoJson(data, {
                style: style1,
                onEachFeature: onEachFeature1.bind(this)
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
                    if (props.label == "Very High") {
                        label_txt = "Low";
                        exposure = "It is typically safe outdoors during peak hot summer times, but remember to stay hydrated and take sun precautions"
                        mitigation = "While not urgent, planting trees for shade and using light-colored materials for buildings can enhance comfort in the area."
                        growing = "Additional vegetation is not truly necessary in this area, but you can still choose to do so."
                        verdict = "This area is at low risk of heat vulnerability."

                    } else if (props.label == "High") {
                        label_txt = "Low-Moderate";
                        exposure = "It is typically safe outdoors during peak hot summer times, but remember to stay hydrated and take sun precautions"
                        mitigation = "While not urgent, planting trees for shade and using light-colored materials for buildings can enhance comfort in the area."
                        growing = "Additional vegetation is not truly necessary in this area, but you can still choose to do so."
                        verdict = "This area is at low-moderate risk of heat vulnerability."
                    } else if (props.label == "Moderate") {
                        label_txt = "Moderate";
                        exposure = "Those with health conditions or heat sensitivity should take extra care while in this area, limiting outdoor activities during the hottest hours and seeking shade when possible"
                        mitigation = "While not urgent, planting trees for shade and using light-colored materials for buildings can enhance comfort in the area."
                        growing = "Additional vegetation is not truly necessary in this area, but you can still choose to do so."
                        verdict = "This area is at moderate risk of heat vulnerability."
                    } else if (props.label == "Low") {
                        label_txt = "Moderate-High";
                        exposure = "It is advisable to minimize prolonged outdoor exposure, especially for vulnerable groups like the elderly and children in this area. If outdoor activities are necessary, opt for cooler early morning or late evening hours"
                        mitigation = "Reducing heat here would be vital. You might want to consider adding green spaces, implementing cool roofs, and encouraging the use of reflective materials."
                        growing = "Consider growing plants in this area as a means to reduce the heat if you reside here."
                        verdict = "This area is at moderate-high risk of heat vulnerability."
                    } else if (props.label == "Very Low") {
                        label_txt = "High";
                        exposure = "It is advisable to minimize prolonged outdoor exposure, especially for vulnerable groups like the elderly and children in this area. If outdoor activities are necessary, opt for cooler early morning or late evening hours"
                        mitigation = "Reducing heat here would be vital. You might want to consider adding green spaces, implementing cool roofs, and encouraging the use of reflective materials."
                        growing = "Consider growing plants in this area as a means to reduce the heat if you reside here."
                        verdict = "This area is at high risk of heat vulnerability."
                    } else{
                        label_txt = "Very Low";
                        exposure = "It is typically safe outdoors during peak hot summer times, but remember to stay hydrated and take sun precautions"
                        mitigation = "While not urgent, planting trees for shade and using light-colored materials for buildings can enhance comfort in the area."
                        growing = "Additional vegetation is not truly necessary in this area, but you can still choose to do so."
                        verdict = "This area is at very low risk of heat vulnerability."
                    }
                }



                this._div.innerHTML = '<h4>Vegetation Coverage Map</h4>' + (props ?
                    "<h5>" + '<b>' + "<div id='elmnt'>" + "Suburb:  " + "</div>"+ props.SA2_NAME16 + '</b><br/>' + "<div id='elmnt'>" + 'Green Area coverage:  ' + "</div>" + props.perc + "%" + '</b><br/>' + "<div id='elmnt'>" + 'Verdict:  ' + "</div>" + verdict + '</b><br/>' + "</h5>"  + "<h4>Recommendations</h4>" + "<h5>" + "<div id='elmnt'>" +'Exposure:  ' + "</div>"+ exposure + '</b><br/>' + "<div id='elmnt'>" + 'Mitigation:  ' +"</div>"+ mitigation + '</b><br/>' + "<div id='elmnt'>" +'Growing:  ' +"</div>"+ growing + "</h5>"
                    : "<h5>" + 'Hover over a suburb' + "</h5>");
            };

            imf.addTo(this.map);

            var lgd = L.control({ position: 'bottomleft' });
            lgd.onAdd = function (map) {
                var div = L.DomUtil.create('div', 'imf lgd'),
                    grades = [0, 1, 2, 3, 4],
                    labels = ["Very Low", "Low", "Moderate", "High", "Very High"];
                div.innerHTML += '<h4>Green Area Coverage</h4>';

                // loop through our density intervals and generate a label with a colored square for each interval
                for (var i = 0; i < grades.length; i++) {
                    div.innerHTML +=
                        '<i style="background:' + getColorV(labels[i]) + '"></i> ' + "<h5>" +
                        labels[i] + ' ' ;
    
                }
                return div;
            };
            lgd.addTo(this.map);
            })
            .catch(error => {
                console.log('Error loading geojson data:', error);
            });
        },

        defaultMap(){
            this.map.remove();
            this.initMap();
        },





    }
};

</script>

<style src="./style.css"></style>
    
<style>
/* Add your CSS styles here */

#elmnt {
    font-size: 18px;
    font-family: 'Fredoka One', cursive;
}

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
    margin: 30px;
    position: relative;
    z-index: 0;

}

#instrcution {
    width: 50%;
    margin-right: auto;
    margin-left: auto;
    text-align: center;
    background-color: #11ad48;
    padding: 10px;
    border-radius: 10px;
    font-size: 23px;
    color: white;
}

.imf {
    /* font: 20px/30px Arial, Helvetica, sans-serif; */
    font-family: 'fredoka', cursive;
    background: white;
    background: rgba(255, 255, 255, 0.9);
    padding: 20px;
    border-radius: 5px;
    text-align: center;
    max-width: 500px;
    margin: 0 auto;
    border-radius: 20px;
    
}

.imf h4 {
    margin: 0 0 5px;
    background-color: #09B845;
    border-radius: 30px;
    padding: 20px;
    font-family: 'Fredoka One', cursive;
    font-size: 20px;
    color: white;
}

h2 {
    font-size: 40px;
}

h3 {
    font-size: 30px;
    text-align: center;

}

.lgd {
    line-height: 18px;
    /* color: #555; */
    background: white;
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
  background: #00a5cf;
  color: #fff;
  font-family: 'Fredoka One', cursive;
  font-size: 20px;
  font-weight: 400;
  border: none;
  outline: none;
  line-height: 66px;
  text-align: center;
  margin: 20px auto 0 auto;
  cursor: pointer;
  margin-right: 600px;

}

h5 {
    font-size: 18px;
    font-family: 'Fredoka', cursive;
    margin-top: 0px;
    margin-bottom: 0px;
}

#switch_view {
    width: 300px;
    height: 66px;
    border-radius: 30px;
    background: #008000;
    color: #fff;
    font-family: 'Fredoka One', cursive;
    font-size: 20px;
    font-weight: 400;
    border: none;
    outline: none;
    line-height: 66px;
    text-align: center;
    margin: 20px auto 0 auto;
    cursor: pointer;
    margin-left: 5px;
    margin-right: 5px;
}

#test {
    width: 300px;
    height: 66px;
    border-radius: 30px;
    background: #e68a00;
    color: #fff;
    font-family: 'Fredoka One', cursive;
    font-size: 20px;
    font-weight: 400;
    border: none;
    outline: none;
    line-height: 66px;
    text-align: center;
    margin: 20px auto 0 auto;
    cursor: pointer;
    margin-left: 5px;
}
</style>
    

