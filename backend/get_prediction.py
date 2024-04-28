import re
import pandas as pd
import requests
import datetime as dt
import string
import os 
# make a call using openweather api
import requests

PREFIX = "backend/"
PREFIX = ""
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

building_final= pd.read_csv(os.path.join(PREFIX, 'CBD.csv')) 
building_final = building_final[building_final["postcode"] == 3000]
building_final = building_final.drop_duplicates(subset=["address"])
# building_final.to_csv("final.csv", index=False)

# def extract_range(info: str):
#     fields = info.split()
#     index = 0
#     find = False
#     for i, field in enumerate(fields):
#         for j in range(10):
#             if str(j) in field:
#                 index = i
#                 find = True
#                 break
#         if find:
#             break
#     field = str(fields[index])
#     lowercase_letters = string.ascii_lowercase

#     # 获取所有大写字母
#     uppercase_letters = string.ascii_uppercase

#     # 合并小写和大写字母
#     all_letters = lowercase_letters + uppercase_letters
#     field = field.strip(all_letters)
    
#     if '-' in field:
#         nums = field.split('-')
#         if (len(nums) != 2 or not nums[0].isdigit() or not nums[1].isdigit()):
#             return None
#         val1 = int(nums[0])
#         val2 = int(nums[1])
#         if val1 > val2:
#             return None
#         return val1, val2
#     elif field.isdigit():
#         val = int(field)
#         return val, val  
#     else:
#         return None
    
    

def get_green_area_by_input(df, street, postcode = "3000"):
    # Check if user input is a postcode (all digits) or a suburb (includes letters)
    if postcode.isdigit():
        # User input is a postcode, so filter by postcode
        tmp = df[df['postcode'] == int(postcode)]
        streets = tmp["address"].tolist()
        green_areas = tmp['green_area'].tolist()
        for i, loc in enumerate(streets):
            if loc.strip() == street.strip():
                return green_areas[i]
    return "error, no green_areas"

def get_root_type(street, postcode = '3000'):
    tmp = building_final[building_final['postcode'] == int(postcode)]
    streets = tmp["address"].tolist()
    roof_types = tmp['roof_type'].tolist()
    for i, loc in enumerate(streets):
        if loc.strip() == street.strip():
            return roof_types[i]
    return "error, no_root_type"

import pickle
# Load the model from disk
with open(os.path.join(PREFIX, 'temp_reduction_estimate_model.pkl'), 'rb') as file:
    loaded_model = pickle.load(file)


# get the columns from the model
feature_columns = ['temperature', 'humidity', 'air_pressure', 'wind_speed', 'green_area',
       'timing_Afternoon', 'timing_Early_afternoon', 'timing_Early_evening',
       'timing_Early_morning', 'timing_Evening', 'timing_Late_afternoon',
       'timing_Late_morning', 'timing_Night']



def get_green_area(street, postcode = '3000'):
    return get_green_area_by_input(building_final, street, postcode)

def get_prediction(street: str, postcode:str = "3000") :
    green_area = get_green_area_by_input(building_final, street, postcode)
    input_data = [
        get_weather_data()[0],
        get_weather_data()[1],
        get_weather_data()[2],
        get_weather_data()[3],
        green_area,
        get_current_hour()['Afternoon'],
        get_current_hour()['Early_afternoon'],
        get_current_hour()['Early_evening'],
        get_current_hour()['Early_morning'],
        get_current_hour()['Evening'],
        get_current_hour()['Late_afternoon'],
        get_current_hour()['Late_morning'],
        get_current_hour()['Night']
    ]
    # print(get_green_area_by_input(building_final, street, postcode))
    new_observation = input_data
    new_observation = pd.DataFrame([new_observation])
    df = pd.DataFrame(columns=feature_columns)
    # link the columns to the new observation
    new_observation.columns = feature_columns


    # Use the loaded model to make predictions
    prediction = loaded_model.predict(new_observation)
    # print(prediction)
    # print(f"Prediction: {prediction}")
    return prediction[0]
    
# get_prediction("13-15 Exploration Lane", "3000")