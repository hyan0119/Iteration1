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
        tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index (HVI):" + d.properties.HVI)
        .style("left", (event.pageX + 10) + "px")
        .style("top", (event.pageY - 10) + "px")
        .style("display", "block")
        .style("visibility", "visible");
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
        d3.select(this).style("fill", "green");
        // 選択されたパスを更新
        selectedPath = d3.select(this);
        



    });

    let isClicking = false; // マウスがクリックされているかどうかの状態

    canvas.on("mousedown", function() {
    isClicking = true;
    }).on("mouseup", function() {
    isClicking = false;
    });

    canvas.on("mousemove", function(event,d) {
    if (isClicking && selectedPath) {
        // マウスがクリックされており、選択されたパスがある場合のみ、情報を表示
        tooltip.html("Suburb: " + selectedPath.datum().properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index (HVI):" + selectedPath.datum().properties.HVI)
            .style("left", (d3.event.pageX + 10) + "px")
            .style("top", (d3.event.pageY - 10) + "px")
            .style("display", "block")
            .style("visibility", "visible");
    } else {
        // マウスがクリックされていない場合や、選択されたパスがない場合は情報を非表示
        // tooltip.style("display", "none");
    }
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