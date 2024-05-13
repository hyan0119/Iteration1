import re
import pandas as pd
import warnings

def get_plant(balcony_size, sunlight, watering, postcode):
    # Load plant data
    plant_data = pd.read_csv("./plant_deltail_guide_clean.csv")
    postcode_area = pd.read_csv("./city_postcode_area.csv")

    postcode_area_copy = postcode_area.copy()
    # Validate balcony size input
    if not isinstance(balcony_size, (int, float)) or balcony_size <= 0:
        return {"error": "Balcony size must be a number greater than 0."}
    # Check for empty inputs for sunlight, watering, and postcode
    if not sunlight:
        return {"error": "Sunlight cannot be empty. Please select one in the box"}
    if not watering:
        return {"error": "Watering cannot be empty. Please select one in the box"}
    if not postcode:
        return {"error": "Postcode cannot be empty. Please enter one in the box"}
    
    # Validate postcode: ensure it is a non-negative four-digit number not equal to zero
    if not isinstance(postcode, int) or postcode <= 0:
        return {"error": "Postcode must be a non-negative four-digit number and cannot be zero."}
    
    if len(str(postcode)) != 4:
        return {"error": "Postcode must be a four-digit number."}
    if postcode not in postcode_area['mccid_int'].values:
        return {"error": "Please enter the postcode in the city of Melbourne"}
    else:
        # Map watering and sunlight preferences to plant data terms
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

        # Filter plants based on watering and sunlight conditions
        filtered_plants = plant_data[
            plant_data['watering'].apply(lambda x: any(condition in x for condition in watering_mapping[watering])) &
            plant_data['sunlight'].apply(lambda x: any(condition in x for condition in sunlight_mapping[sunlight]))
        ]

        # Function to parse plant size from dimensions to meters
        def parse_size_to_meters(size_str):
            match = re.search(r"'max_value': (\d+(\.\d+)?)", size_str)
            if match:
                max_value_feet = float(match.group(1))
                return max_value_feet * 0.3048
            return 0
        
        # Apply size parsing and filter by balcony size
        filtered_plants['Size_meters'] = filtered_plants['dimensions'].apply(parse_size_to_meters)
        suitable_plants = filtered_plants[filtered_plants['Size_meters'] <= balcony_size * 0.3]

        # Return results or a no-match message
        if suitable_plants.empty:
            return {"error": "No plants match the given criteria."}
        
        random_plant = suitable_plants.sample(n=1).iloc[0]

        canopy_area = postcode_area_copy[postcode_area_copy['mccid_int'] == postcode]['canopy_area'].values[0]
        energy_save = (random_plant['Size_meters'] / (random_plant['Size_meters'] + canopy_area)) * 0.19 * 0.0385 * 12
        energy_save_str = f'The energy save for this is: {energy_save:.2f} AUD/MWh per year'

        response_data = {
            'plantImageUrl': random_plant['original_url'],
            'plantName': random_plant['common_name'],
            'watering_guide': random_plant['watering_guide'],
            'watering_guide_description': random_plant['watering_guide_description'],
            'sunlight_guide_description': random_plant['sunlight_guide_description'],
            'pruning_guide_description': random_plant['pruning_guide_description'],
            'energy_save': energy_save_str
        }

        return response_data

    
# res = get_plant(3.3, "high", "high", 3000)
# # # res = get_plant(3.3, "sun-part_shade", "perennial", "frequent")
# print(res)