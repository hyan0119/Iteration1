from flask import Flask, redirect, url_for, jsonify, request
import requests
import pandas as pd
from flask_dance.contrib.google import make_google_blueprint, google
from flask_cors import CORS
from get_plant import get_plant
import pickle
app = Flask(__name__)
CORS(app) 
import os
from get_prediction import get_prediction, PREFIX
from search import search
print("Current working directory:", os.getcwd())


model = pickle.load(open( os.path.join(PREFIX, 'temp_reduction_estimate_model.pkl'), 'rb'))


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

@app.route('/predict', methods=['GET'])
def predict():
    street = request.args.get('street')
    postcode = request.args.get('postcode', '3000')  # Default to '3000' if not provided
    if street:
        rtn = get_prediction(street, postcode)
        return jsonify({"result": rtn})
    else:
        return jsonify({"error": "Street parameter is required"}), 400
# http://127.0.0.1:8000/predict?street=480-490%20Collins%20Street

@app.route("/get_green_area", methods=["GET"])
def get_green():
    street = request.args.get('street')
    from get_prediction import get_green_area
    return jsonify({"green_area": get_green_area(street)})

@app.route("/get_roof_type", methods=['GET'])
def get_roof():
    street = request.args.get('street')
    from get_prediction import get_root_type
    return jsonify({"roof_type": get_root_type(street)})
    
# df = pd.read_csv(os.path.join(PREFIX,"CBD.csv"))
# print(df)
@app.route('/search', methods=['GET'])
def search_by_word():
    key_word = request.args.get('key_word')
    # print(search(key_word))
    return jsonify(search(key_word))
# http://127.0.0.1:8000/search?key_word=Collins


if __name__ == "__main__":
    app.run(debug=True, port=8000)