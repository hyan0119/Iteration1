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
    

    index = 10
    return jsonify({'index': index})

@app.route('/plant_match', methods=['POST'])
def plant_match():
    
    data = request.json
    
    
    balcony_size = data.get('apartmentSize')
    sunlight = data.get('sunlight')
    watering = data.get('watering')
    
    print(balcony_size, sunlight, watering)
    response_data = get_plant(float(balcony_size), sunlight, watering)
    # print(response_data)
    
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True, port=8000)