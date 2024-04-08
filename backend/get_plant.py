import requests
import pandas as pd

#       xxx index

# def get_decrease_index(dimensions):
#     reduce_UHI = (dimensions/dimensions+9,992 * 0.19)* 0.0385
#     return reduce_UHI
    


def get_plant(balcony_size,sunlight,cycle,watering):
    #
    #
    api_key = "sk-Gxoq6613e77d2ac0f4868"
    def fetch_plants_info(sunlight, cycle, watering):
        # Your API key and other parameters
        indoor = 1
        poisonous = 0
        page = 1

        # Constructing the URL with the given parameters
        url = f"https://perenual.com/api/species-list?key={api_key}&indoor={indoor}&poisonous={poisonous}" \
              f"&sunlight={sunlight}&cycle={cycle}&watering={watering}&page={page}"
        # print(url)
        # Sending a GET request to the API
        
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            # print("debug: ")
            # print(json_data)
            # print(json_data)
            # Extracting information from the response
            plants_data = {
                'id': [i['id'] for i in json_data['data']],
                'common_name': [i['common_name'] for i in json_data['data']],
                'scientific_name':
                    [i['scientific_name'] for i in json_data['data']],
                'cycle': [i['cycle'] for i in json_data['data']],
                'watering': [i['watering'] for i in json_data['data']],
                'sunlight': [i['sunlight'] for i in json_data['data']],
            }

            # convert to pandas format
            # delete the rows we dont need
            plants_df = pd.DataFrame(plants_data)
            plants_df = plants_df[~plants_df.apply(lambda row: row.astype(
                str).str.contains('Upgrade Plans To Premium/Supreme').any(),
                                                   axis=1)]

            return plants_df
        else:
            print("Failed to fetch data. Status code:", response.status_code)
            return {}

    def detail_plant_info(balcony_size_ft, plants_df):
        plants_data = []
        for ids in plants_df['id']:
            url = f"https://perenual.com/api/species/details/{ids}?key={api_key}"
            response = requests.get(url)
            if response.status_code == 200:
                json_data = response.json()
                # print('index: ', json_data.get('dimensions', {}).get('min value', float('inf')))
                # index = get_decrease_index(json_data.get('dimensions', {}).get('min value', float('inf')))
                # Assuming 'dimensions' is directly accessible and 'min_value' is directly comparable
                if json_data.get('dimensions', {}).get('min_value', float('inf')) <= (balcony_size_ft * 0.3):
                    plant_details = {
                        'id': ids,
                        'common_name': json_data.get('common_name'),
                        'scientific_name': json_data.get('scientific_name'),
                        'cycle': json_data.get('cycle'),
                        'watering': json_data.get('watering'),
                        'sunlight': json_data.get('sunlight'),
                        'flowers': json_data.get('flowers'),
                        'fruits': json_data.get('fruits'),
                        'growth_rate': json_data.get('growth_rate'),
                        'maintenance': json_data.get('maintenance'),
                        'care_level': json_data.get('care_level'),
                        'description': json_data.get('description'),
                        'image': json_data.get('default_image'),
                        # 'index': index
                    }
                    plants_data.append(plant_details)
                    break
            else:
                print(f"Failed to get data for plant id {ids}")
        # print("detail_plant_info")
        if plants_data:
            plants_data_detail_df = pd.DataFrame(plants_data)
            return plants_data_detail_df
        else:
            print("No plants meet the criteria or failed to fetch plant data.")
            return pd.DataFrame()

    # 假设这里是根据输入的数据进行植物匹配的逻辑
    # plant_name = 'Aloe Vera'
    # lifespan = 5
    # maintaining_guide = 'Water once a week'
    # temperature_contribution = 'High'
    # required_tools = 'Watering can'
    plant_image_url = None
    plant_name = None
    lifespan = None
    maintaining_guide = None
    index = 0
    try:
        plant_df = fetch_plants_info(sunlight, cycle, watering)
        # print(plant_df)
        # print('========')
        plants_data_detail_df = None
        if len(plant_df):
            plants_data_detail_df = detail_plant_info(float(balcony_size), plant_df)
        # print(plants_data_detail_df)
        # for i in plants_data_detail_df:
        #     print(i, plants_data_detail_df[i])
        try:
            plant_image_url = plants_data_detail_df['image'][0]['original_url']
        except Exception as e:
            plant_image_url = None
        # print('========')
            
        plant_name = plants_data_detail_df['common_name'][0]
        lifespan = plants_data_detail_df['cycle'][0]
        maintaining_guide = plants_data_detail_df['watering'][0]
        index = plants_data_detail_df[index]
    except Exception as e:
        print("errr")
    finally: 
        response_data = {
            'plantImageUrl': plant_image_url,
            'plantName': plant_name,
            'lifespan': lifespan,
            'maintainingGuide': maintaining_guide
            # 'index': index
        }
        # print("=" * 10)
        # print(response_data)
        return response_data
    
# res = get_plant(3.3, "part_shade", "perennial", "frequent")
# res = get_plant(3.3, "sun-part_shade", "perennial", "frequent")
# print(res)