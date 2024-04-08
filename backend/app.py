from flask import Flask, redirect, url_for, jsonify, request
import requests
import pandas as pd
from flask_dance.contrib.google import make_google_blueprint, google
from flask_cors import CORS
from get_plant import get_plant
app = Flask(__name__)
CORS(app) 



@app.route('/get_head_index', methods=['GET'])
def get_head_index():
    postcode = request.args.get('postcode')
    
    # 在这里根据 postcode 获取相应的地图信息和索引值
    # 假设这里直接返回一个固定的索引值进行示范
    index = 10
    return jsonify({'index': index})

@app.route('/plant_match', methods=['POST'])
def plant_match():
    # 从请求中获取前端发送过来的数据
    data = request.json
    
    # 在这里执行您的数据处理逻辑，比如根据收到的数据匹配植物信息
    balcony_size = data.get('apartmentSize')
    sunlight = data.get('sunlight')
    cycle = data.get('cycle')
    watering = data.get('watering')
    
    print(balcony_size, sunlight, cycle, watering)
    response_data = get_plant(balcony_size, sunlight, cycle, watering)
    # print(response_data)
    # 将结果以 JSON 格式返回给前端
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True, port=8000)