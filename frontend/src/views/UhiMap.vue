<template>
<div class="uhi-map">
<div>
<HeaderNavigation/>
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
<button @click="handleButtonClick">Reset View</button>
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
'<b>' + props.SA2_NAME16 + '</b><br />' + 'HVI:  ' + props.HVI
: 'Hover over a suburb');
};

info.addTo(this.map);

var legend = L.control({position: 'bottomright'});
legend.onAdd = function (map) {
    var div = L.DomUtil.create('div', 'info legend'),
        grades = [0, 1, 2, 3, 4, 5],
        labels = [];
    div.innerHTML += '<h4>Heat Vulnerability Index</h4>';
    
    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(grades[i]) + '"></i> ' +
            grades[i] + ' ' + (grades[i + 1] ? '&ndash;' + ' ' +grades[i + 1] + '<br>' : '+');
    }
    return div;
};
legend.addTo(this.map);









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
    this.map.setView([-37.8136, 144.9631], 10);

},

// switchMap() {
//     //load a new entire map
//     this.map.remove();
//     this.map = L.map('map').setView([-37.8136, 144.9631], 10);
//     L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
//     maxZoom: 19,
//     }).addTo(this.map);

//     let canopy = '/tree.geojson';
//     fetch(canopy)
//     .then(response => response.json())
//     .then(data => {
//     this.canopy = data;
//     this.initMap();
//     })
//     .catch(error => {
//     console.log('Error loading map data:', error);
//     });

    
// },





}
};

</script>

<style scoped>
/* Add your CSS styles here */
.menu-item {
font-size: 1.3rem !important;
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
}
</style>

<style>
.info {
padding: 6px 8px;
font: 20px/30px Arial, Helvetica, sans-serif;
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

h2 {
    font-size: 40px;
}

h3 {
    font-size: 30px;
    text-align: center;

}

.legend {
    line-height: 18px;
    color: #555;
}
.legend i {
    width: 18px;
    height: 18px;
    float: left;
    margin-right: 8px;
    opacity: 0.9;
}

/* #test {
    width: 1000px;
    height: 700px;
} */

</style>
<style src="./style.css"></style>
