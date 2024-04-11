import re
import pandas as pd
#
# def get_decrease_index(dimensions):
#     reduce_UHI = (dimensions/dimensions+9,992 * 0.19)* 0.0385
#     return reduce_UHI
    


def get_plant(balcony_size,sunlight,watering):
    plant_data = pd.read_csv("./plant_deltail_clean.csv")
    def plant_recommender(plant_data, watering, sunlight, balcony_size_meters):
        # 检查balcony_size_meters是否为数字
        if not isinstance(balcony_size_meters, (int, float)) or balcony_size_meters <= 0:
            return ("balcony_size_meters must be a number greater than 0.")
        
        
        # 创建浇水和日照条件的映射
        watering_mapping = {
            'high': ['frequent'],
            'medium': ['average'],
            'low': ['minimum']
        }
        
        sunlight_mapping = {
            'high': ['full sun'],
            'medium': ['part shade', 'filtered shade'],
            'low': ['full shade', 'deep shade']
        }
        # 通过映射找到对应的浇水和日照条件列表
        watering_conditions = watering_mapping[watering]
        sunlight_conditions = sunlight_mapping[sunlight]
        
        # 定义一个函数来使用正则表达式解析size字符串并转换为米
        def parse_size_to_meters(size_str):
            match = re.search(r"'max_value': (\d+(\.\d+)?)", size_str)
            if match:
                max_value_feet = float(match.group(1))
                return max_value_feet * 0.3048
            else:
                return 0
        
        # 应用解析函数并筛选符合条件的植物
        suitable_plants = plant_data[
            plant_data['watering'].apply(lambda x: any(condition in x for condition in watering_conditions)) &
            plant_data['sunlight'].apply(lambda x: any(condition in x for condition in sunlight_conditions))
        ]
        
        suitable_plants['Size_meters'] = suitable_plants['dimensions'].apply(parse_size_to_meters)
        suitable_plants = suitable_plants[suitable_plants['Size_meters'] <= balcony_size_meters*0.3]
        
        # 检查是否找到了符合条件的植物
        if suitable_plants.empty:
            return "No plants match the given criteria."
    
        return suitable_plants.drop(columns=['dimensions'])[['original_url', 'watering_guide', 'common_name']]

    df = plant_recommender(plant_data,watering,sunlight,balcony_size)
    original_url = list(df['original_url'])[0]
    watering_guide = list(df['watering_guide'])[0]
    common_name = list(df['common_name'])[0]
    # print(type(original_url))
    # print(original_url[0])
    # print(common_name[0])
    # print(watering_guide[0])
    response_data = {
        'plantImageUrl': original_url,
        'plantName': common_name,
        'watering_guide': watering_guide
        # 'index': index
    }
    
    # print("=" * 10)
    # print(response_data)
    return response_data
    
# res = get_plant(3.3, "part_shade", "perennial", "frequent")
# res = get_plant(3.3, "sun-part_shade", "perennial", "frequent")
# print(res)