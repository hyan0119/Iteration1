let hvi = 'hvi.json'

let hviData
let selectedPath = null

let canvas = d3.select('#canvas')
let tooltip = d3.select('#tooltip')

let drawMap = () => {

    var projection = d3.geoMercator()
                               .fitSize([800, 800], hviData);
    
    var path = d3.geoPath()
                    .projection(projection);
    
    
 
    canvas.selectAll("path")
    .data(hviData.features)
    .enter().append("path")
    .attr("d", path)
    .attr('data-fips', (d) => d.properties.id) // FIPSコードをデータ属性として追加
    .style("fill", function(d) {
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
        } else {return "blue"}
    })
    .style("stroke", "white")
    .style("stroke-width", 0.5)
    .on("mouseover", function(event, d) {
                // マウスオーバー時の処理
        // tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI)
        // .style("left", (event.pageX + 10) + "px")
        // .style("top", (event.pageY - 10) + "px")
        // .style("display", "block")
        // .style("visibility", "visible")

        if (d.properties.HVI == 0) {
            tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb is not any warmer the countryside, so you would not notice any difference." + "<br>" + "It is as if this suburb is part of the natural landscape, with plenty of trees and parks that help keep it cool.")
            .style("left", (event.pageX + 10) + "px")
            .style("top", (event.pageY - 10) + "px")
            .style("display", "block")
            .style("visibility", "visible")
        } else if (d.properties.HVI == 1) {
            tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "You might feel that this suburb is a bit warmer here than in the countryside, but it is barely noticeable. This suburb might have some green spaces and buildings that do not get too hot during hot days, so it does not make much of a difference to your day or your electricity bill.")
            .style("left", (event.pageX + 10) + "px")
            .style("top", (event.pageY - 10) + "px")
            .style("display", "block")
            .style("visibility", "visible")
        } else if (d.properties.HVI == 2) {
            tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" +  "This suburb is warmer than the countryside. You might start turning on the air conditioning more often, and it could feel uncomfortably hot outside on some days. You might want to consider growing plants in your balcony, rooftop, or in rooms inside your house to add natural shades and help cooling down your area.")
            .style("left", (event.pageX + 10) + "px")
            .style("top", (event.pageY - 10) + "px")
            .style("display", "block")
            .style("visibility", "visible")
        } else if (d.properties.HVI == 3) {
            tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb experiences significantly higher temperatures than the countryside, especially during hot days, encouraging indoor stays with air conditioning and potentially impacting health. Installing cool or green roofs to reflect sunlight and heat, along with growing plants on balconies, rooftops, or indoors, can offer natural shade and cool the area.")
            .style("left", (event.pageX + 10) + "px")
            .style("top", (event.pageY - 10) + "px")
            .style("display", "block")
            .style("visibility", "visible")
        } else if (d.properties.HVI == 4) {
            tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb, hotter than the countryside, impacts comfort, increases electricity bills, and poses health risks in summer. To combat this, it needs more parks, green roofs, and cooling centers. Installing cool roofs and growing plants in your home can provide shade and cool your area, reducing the summer heat's adverse effects.")
            .style("left", (event.pageX + 10) + "px")
            .style("top", (event.pageY - 10) + "px")
            .style("display", "block")
            .style("visibility", "visible")
        } else if (d.properties.HVI == 5) { 
            tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb's extreme heat, beyond countryside levels, brings discomfort and health dangers. Mitigating it demands significant urban upgrades and cooling solutions. Installing cool or green roofs and growing plants indoors can shade and cool the area, easing summer and heatwave effects.")
            .style("left", (event.pageX + 10) + "px")
            .style("top", (event.pageY - 10) + "px")
            .style("display", "block")
            .style("visibility", "visible")
        } else {return "blue"}


    })
    .on("mouseout", function(d) {
                // マウスアウト時の処理
        tooltip.style("display", "none");
    })
    .on("click", function(event, d) {
        d3.select(this).style("fill", "orange");
    })
    .on("click", function(event, d) {
        // クリックされたパスの色を変更
        if (selectedPath) {
            // 以前に選択されたパスがある場合、その色を元に戻す
            selectedPath.style("fill", function(d) {
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
        d3.select(this).style("fill", "#33333e");
        // 選択されたパスを更新
        selectedPath = d3.select(this);
        



    });

    let isClicking = false; // マウスがクリックされているかどうかの状態

    canvas.on("mousedown", function() {
    isClicking = true;
    }).on("mouseup", function() {
    isClicking = false;
    });


}

d3.json(hvi).then(
    (data, error) => {
        if(error){
            console.log(log)
        }else{
            hviData = data
            console.log(hviData)
            drawMap()
        }
    }
)