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
    // .on("mouseover", function(event, d) {
    //             // マウスオーバー時の処理
    //     // tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI)
    //     // .style("left", (event.pageX + 10) + "px")
    //     // .style("top", (event.pageY - 10) + "px")
    //     // .style("display", "block")
    //     // .style("visibility", "visible")

    //     if (d.properties.HVI == 0) {
    //         tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb is not vulnerable to Urban Heat Island.")
    //         .style("left", (event.pageX + 10) + "px")
    //         .style("top", (event.pageY - 10) + "px")
    //         .style("display", "block")
    //         .style("visibility", "visible")
    //     } else if (d.properties.HVI == 1) {
    //         tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb is slightly vulnerable to Urban Heat Island.")
    //         .style("left", (event.pageX + 10) + "px")
    //         .style("top", (event.pageY - 10) + "px")
    //         .style("display", "block")
    //         .style("visibility", "visible")
    //     } else if (d.properties.HVI == 2) {
    //         tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" +  "This suburb is moderately vulnerable to Urban Heat Island.")
    //         .style("left", (event.pageX + 10) + "px")
    //         .style("top", (event.pageY - 10) + "px")
    //         .style("display", "block")
    //         .style("visibility", "visible")
    //     } else if (d.properties.HVI == 3) {
    //         tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb is highly vulnerable to Urban Heat Island.")
    //         .style("left", (event.pageX + 10) + "px")
    //         .style("top", (event.pageY - 10) + "px")
    //         .style("display", "block")
    //         .style("visibility", "visible")
    //     } else if (d.properties.HVI == 4) {
    //         tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb is extremely vulnerable to Urban Heat Island.")
    //         .style("left", (event.pageX + 10) + "px")
    //         .style("top", (event.pageY - 10) + "px")
    //         .style("display", "block")
    //         .style("visibility", "visible")
    //     } else if (d.properties.HVI == 5) { 
    //         tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb is severely vulnerable to Urban Heat Island.")
    //         .style("left", (event.pageX + 10) + "px")
    //         .style("top", (event.pageY - 10) + "px")
    //         .style("display", "block")
    //         .style("visibility", "visible")
    //     } else {return "blue"}


    // })
    .on("mouseout", function(d) {
                // マウスアウト時の処理
        tooltip.style("display", "none");
    })
    // .on("click", function(event, d) {
    //     d3.select(this).style("fill", "orange");
    // })
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

        if (selectedPath && selectedPath.node() === this) {
            // 以前に選択されたパスがクリックされた場合、選択を解除
            selectedPath = null;
            return;
        }
        // 新しいパスの色を変更
        d3.select(this).style("fill", "grey");
        
        // 選択されたパスを更新
        selectedPath = d3.select(this);
         
        // 選択されたパスのデータを取得
        const selectedData = d.properties;

        // tooltipの表示内容を作成
        const tooltipContent = "Suburb: " + selectedData.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + selectedData.HVI;

        if (selectedData.HVI == 0) {
            tooltipContent += "<br><br>This suburb is not vulnerable to Urban Heat Island.";
        } else if (selectedData.HVI == 1) {
            tooltipContent += "<br><br>This suburb is slightly vulnerable to Urban Heat Island.";
        } else if (selectedData.HVI == 2) {
            tooltipContent += "<br><br>This suburb is moderately vulnerable to Urban Heat Island.";
        } else if (selectedData.HVI == 3) {
            tooltipContent += "<br><br>This suburb is highly vulnerable to Urban Heat Island.";
        } else if (selectedData.HVI == 4) {
            tooltipContent += "<br><br>This suburb is extremely vulnerable to Urban Heat Island.";
        } else if (selectedData.HVI == 5) {
            tooltipContent += "<br><br>This suburb is severely vulnerable to Urban Heat Island.";
        } else {
            tooltipContent += "<br><br>Unknown vulnerability level.";
        }

        // tooltipを表示
        tooltip.html(tooltipContent)
            // .style("left", (event.pageX + 10) + "px")
            // .style("top", (event.pageY - 10) + "px")
            .style("display", "block")
            .style("visibility", "visible");
        
        // if (selectedPath.node() === this && isClicking){
        const c_path = this
        //     selectedPath = null
            

        // }
    
    })
    
    .on("mouseover", function(event, d) {
            // マウスオーバー時の処理
    // tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI)
    // .style("left", (event.pageX + 10) + "px")
    // .style("top", (event.pageY - 10) + "px")
    // .style("display", "block")
    // .style("visibility", "visible")

    if (d.properties.HVI == 0 && !selectedPath) {
        tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb is not vulnerable to Urban Heat Island.")
        .style("left", (event.pageX + 10) + "px")
        .style("top", (event.pageY - 10) + "px")
        .style("display", "block")
        .style("visibility", "visible")
    } else if (d.properties.HVI == 1 && !selectedPath) {
        tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb is slightly vulnerable to Urban Heat Island.")
        .style("left", (event.pageX + 10) + "px")
        .style("top", (event.pageY - 10) + "px")
        .style("display", "block")
        .style("visibility", "visible")
    } else if (d.properties.HVI == 2 && !selectedPath) {
        tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" +  "This suburb is moderately vulnerable to Urban Heat Island.")
        .style("left", (event.pageX + 10) + "px")
        .style("top", (event.pageY - 10) + "px")
        .style("display", "block")
        .style("visibility", "visible")
    } else if (d.properties.HVI == 3 && !selectedPath) {
        tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb is highly vulnerable to Urban Heat Island.")
        .style("left", (event.pageX + 10) + "px")
        .style("top", (event.pageY - 10) + "px")
        .style("display", "block")
        .style("visibility", "visible")
    } else if (d.properties.HVI == 4 && !selectedPath) {
        tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb is extremely vulnerable to Urban Heat Island.")
        .style("left", (event.pageX + 10) + "px")
        .style("top", (event.pageY - 10) + "px")
        .style("display", "block")
        .style("visibility", "visible")
    } else if (d.properties.HVI == 5 && !selectedPath) { 
        tooltip.html("Suburb: " + d.properties.SA2_NAME16 + "<br>" + "Urban Heat Island Vulnerability Index: " + d.properties.HVI + "<br>" + "<br>" + "This suburb is severely vulnerable to Urban Heat Island.")
        .style("left", (event.pageX + 10) + "px")
        .style("top", (event.pageY - 10) + "px")
        .style("display", "block")
        .style("visibility", "visible")
    } else {return "blue"}


    })
    .on("mouseout", function(event, d) {
        if (selectedPath) {
            tooltip.html(tooltipContent)
            .style("left", (event.pageX + 10) + "px")
            .style("top", (event.pageY - 10) + "px")
            .style("display", "block")
            .style("visibility", "visible");
        }

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