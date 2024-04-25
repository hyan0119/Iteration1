import re
import pandas as pd
import requests
import datetime as dt

# make a call using openweather api
import requests

def get_weather_data():
    API_key = "5ddf500fc63209d20e002a8cd26adf96"
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Melbourne,AU&appid={API_key}"
    response = requests.get(url)
    response = response.json()
    # get elements from API response
    temp = response['main']['temp'] - 273.15
    humidity = response['main']['humidity']
    pressure = response['main']['pressure']
    wind_speed = response['wind']['speed']
    
    return temp,humidity,pressure,wind_speed

import datetime

def get_current_hour():
    now = datetime.datetime.now()

    # 初始化所有标志为0
    flags = {
        "Afternoon": 0,       # 正午
        "Early_afternoon": 0, # 早午
        "Early_evening": 0,   # 傍晚
        "Early_morning": 0,   # 早晨
        "Evening": 0,         # 晚上
        "Late_afternoon": 0,  # 晚午
        "Late_morning": 0,    # 上午
        "Night": 0            # 夜晚
    }

    # 定义每个时间段的小时
    if 5 <= now.hour < 8:
        flags["Early_morning"] = 1
    elif 8 <= now.hour < 11:
        flags["Late_morning"] = 1
    elif 11 <= now.hour < 13:
        flags["Afternoon"] = 1
    elif 13 <= now.hour < 15:
        flags["Early_afternoon"] = 1
    elif 15 <= now.hour < 17:
        flags["Late_afternoon"] = 1
    elif 17 <= now.hour < 19:
        flags["Early_evening"] = 1
    elif 19 <= now.hour < 21:
        flags["Evening"] = 1
    else:
        flags["Night"] = 1

    return flags

building_final= pd.read_csv('building_final.csv') 

building_final = building_final.drop_duplicates()


def get_green_area_by_input(df, user_input):
    # Check if user input is a postcode (all digits) or a suburb (includes letters)
    if user_input.isdigit():
        # User input is a postcode, so filter by postcode
        results = df[df['postcode'] == int(user_input)].sum()
    else:
        # User input is a suburb, so filter by suburb
        results = df[df['suburb'].str.lower() == user_input.lower()]

    # Check if any results were found
    if not results.empty:
        return results['green_area']
    else:
        return "Error: The postcode or suburb entered is incorrect or not found."


    
input_data = [
    get_weather_data()[0],
    get_weather_data()[1],
    get_weather_data()[2],
    get_weather_data()[3],
    get_green_area_by_input(building_final, '3000'),
    get_current_hour()['Afternoon'],
    get_current_hour()['Early_afternoon'],
    get_current_hour()['Early_evening'],
    get_current_hour()['Early_morning'],
    get_current_hour()['Evening'],
    get_current_hour()['Late_afternoon'],
    get_current_hour()['Late_morning'],
    get_current_hour()['Night']
]


import pickle
# Load the model from disk
with open('temp_reduction_estimate_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Define a new observation
new_observation = input_data

# get the columns from the model
feature_columns = ['temperature', 'humidity', 'air_pressure', 'wind_speed', 'green_area',
       'timing_Afternoon', 'timing_Early_afternoon', 'timing_Early_evening',
       'timing_Early_morning', 'timing_Evening', 'timing_Late_afternoon',
       'timing_Late_morning', 'timing_Night']

# add the columns to the new observation
new_observation = pd.DataFrame([new_observation])
# make a dummy dataframe with feature columns as columns
df = pd.DataFrame(columns=feature_columns)
# link the columns to the new observation
new_observation.columns = feature_columns


# Use the loaded model to make predictions
prediction = loaded_model.predict(new_observation)

print(f"Prediction: {prediction}")