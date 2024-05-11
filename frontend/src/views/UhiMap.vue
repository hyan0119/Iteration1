<template>
    <div class="uhi-map">
        <div>
            <HeaderNavigation/>
        </div>
        <el-main class="main-content">
            <!-- <div id="map"></div> -->
            <h1>UHI Map</h1>
            <h2>Urban Heat Island Map</h2>
            <div id="map"></div>
        </el-main>
        <!-- <footer-column></footer-column> -->
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
            let hvi = '/hvi.json';

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
            this.map = L.map('map').setView([-37.8136, 144.9631], 13);

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
            maxZoom: 19,
        }).addTo(this.map);

            function style(feature) {
                        return {
                            fillColor: getColor(feature.properties.HVI),
                            fillOpacity: 0.7,
                            weight: 1.5,
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
                        weight: 1.5,
                        color: 'white'
                    };
                }
            L.geoJson(this.hviData, {style: style}).addTo(this.map);

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

                    info.update(layer.feature.properties);
                }

            function resetHighlight(e) {
                geojson.resetStyle(e.target);
                info.update();
            }

            function zoomToFeature(e){
                this.map.fitBounds(e.target.getBounds());
            }

            var geojson;
            // geojson = L.geoJson();

            function onEachFeature(feature, layer) {
                layer.on({
                    mouseover: highlightFeature,
                    mouseout: resetHighlight,
                    click: zoomToFeature.bind(this)
                });
            }

            geojson = L.geoJson(this.hviData, {
                    style: style,
                    onEachFeature: onEachFeature.bind(this)
                }).addTo(this.map);

            var info = L.control();

            info.onAdd = function (map) {
                this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
                this.update();
                return this._div;
            };

            // method that we will use to update the control based on feature properties passed
            info.update = function (props) {
                this._div.innerHTML = '<h4>Urban Heat Vulnerability Map</h4>' +  (props ?
                    '<b>' + props.SA2_NAME16 + '</b><br />' + props.HVI
                    : 'Hover over a suburb');
            };

            info.addTo(this.map);
        },

    }
};
</script>

<style scoped>
/* Add your CSS styles here */
.menu-item {
    font-size: 1.3rem !important;
}

#map {
            position: absolute;
            top: 0;
            bottom: 0;
            left: 0;
            right: 0;
            border: 2px solid white;
            margin: 150px;
        }
</style>

<style>
.info {
    padding: 6px 8px;
    font: 14px/16px Arial, Helvetica, sans-serif;
    background: white;
    background: rgba(255,255,255,0.8);
    box-shadow: 0 0 15px rgba(0,0,0,0.2);
    border-radius: 5px;
    text-align: center;
}
.info h4 {
    margin: 0 0 5px;
    color: #777;
}
</style>

<!-- <style src="./style.css"></style> -->
