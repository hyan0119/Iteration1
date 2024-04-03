from flask import Flask, redirect, url_for, jsonify, request, pandas as pd
from flask_dance.contrib.google import make_google_blueprint, google
from flask_cors import CORS
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
    apartment_size = data.get('apartmentSize')
    num_windows = data.get('numWindows')
    maintenance_availability = data.get('maintenanceAvailability')
    building_direction = data.get('buildingDirection')

# 在这里通过用户的选择进行植物筛选
def fetch_plants_info(sunlight, cycle, watering):
    # Your API key and other parameters
    api_key = "sk-rJHq66029a8017b004868"
    indoor = 1
    poisonous = 0
    page = 1

    # Constructing the URL with the given parameters
    url = f"https://perenual.com/api/species-list?key={api_key}&indoor={indoor}&poisonous={poisonous}" \
          f"&sunlight={sunlight}&cycle={cycle}&watering={watering}&page={page}"

    # Sending a GET request to the API
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()

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
        url = f"https://perenual.com/api/species/details/{ids}?key=sk-rJHq66029a8017b004868"
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
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
                    'original_url': json_data.get('original_url'),
                }
                plants_data.append(plant_details)
        else:
            print(f"Failed to get data for plant id {ids}")

    if plants_data:
        plants_data_detail_df = pd.DataFrame(plants_data)
        return plants_data_detail_df
    else:
        print("No plants meet the criteria or failed to fetch plant data.")
        return pd.DataFrame()

    # 假设这里是根据输入的数据进行植物匹配的逻辑
    # plant_image_url = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUTExIVFhUXGBgVGBgXGBUVFxYYGBUXFxcVFxcYHSggGBolGxUVITEhJSkrLi4uFx8zODMsNygtLisBCgoKDg0OGxAQGy0mICYtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIAKgBLAMBIgACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAAEBQMGAAECBwj/xAA/EAABAwIEAwYDBgQFBAMAAAABAAIRAyEEBRIxQVFhBhMicYGRMqGxFEJSwdHwI2Jy4QcVM1OCJLKz8YSSov/EABoBAAIDAQEAAAAAAAAAAAAAAAMEAQIFAAb/xAAvEQACAgICAQQAAwcFAAAAAAABAgARAyEEEjETIkFRBSNhFHGBkaGx0TJSwfDx/9oADAMBAAIRAxEAPwD2+Vjlpq04oQ8Tp0Vi5cVsFd8zptYVorSr2kzlwUNR8IgoTEoTA3qVbxIH1uqjOIQdYkFQHESuuBuMHVghqpCDfVIUbsSuuRckqlQPqLRrKKo9QTKGac5Nsqw2HqRuXi5B/TiEic9ap1S10tMEcQqMtipymjuXpwQxrtnTqE8RN/Zd4KsX02ucIJF0qb2fZ3hqFznX1QefXmsx8am+xjpY66iMKgBUUIhzQo3Ugs3Jj3qXkbmoStTcLt/9ot1M8Coy944A/JLOn3OMiZVkWSrPGamNHIz8k2cBvpg9Iv5pbjQ51mtNuNvkOKEAQdSj7EDwtbSFuvnen4SSelx77ILEYcwSRMc/02VYzXNXMJZH/rpCPh4xyNqAbJ11GmN7evY7SaYPkYPqYt6KOl/iI0EThrfeOuT6SLqj4klxJIQzmLXHBw1sbg/Vb7nt7M8od2yr3rWtqfCXENPlfrZVztPUBqj+KSyo3VpkFogxLSvM6hcQASSBsOU3Mcl03GVAGibNmBwEmTCAn4aENq0s2QsKM9Eysw8CjGrrt6q0YYVDIqBsHdu4PQzYpL2Ky3TRbWeP4lQTcfCOAurI5tljcnKVyEL8fMNiTVxecHUoAnDeJlyaDjEcT3Lz8P8AQ6RyLV3l2bMrSGy17fjpvBZVp/1MNx57Hmj3DigMyyqnXLXOllVk93VYYezyOzm/ymQeS4ZUy6y6P+4f8iFojxDDKzQUmq50/DAtxjZEEsrsEU6h4MeCf4TzyJ0ngeCrOYf4jPiKVEA83HVbyH6q6fh+Zz7dj7+JVnA8y355m1PC0jUqGeDWjdx5BUg9q8Q/xBtNoPDTPzKU5z2oqYqnorU2EgyxzZaWnjxMgjggKOKgQtXBwVxp7hbRd3JOp9NNUZN1ISoWlelZqoQpkj9ljHLHiyGpPUsdyLowlxXOpcVChjUOyo43ILwp9SENXMqMVOBXBqQuUypa4JXS+qITPEtlLq6hpQwUvQ9Zs7LuoVwSqSpg32mN1J3wK5qUpQzgWqCZSEOeuG1i0yDBUBrrjvJVQ06NP80rf7jvkp6Gb1RYOnzEoPCZVWfswgczYfqrNlOViiLu1E72EenFBy5MaiGRWM7y2tUdd4gcOHyRzlpzwuCZ2Wa7BjqNqKFTio5Qvkogs5rT4CVfHJgj2xfcoetuAiCJM8kNiGpN0Mrcic3eRISHNOx9CtJYDSfzb8J827e0KxFqqfarNcbQcAzS2m6Q10STzBnY8lbirkL1jNGDeq2Ilqdn6lEkObP8wuD68PVCYrLRGogIrCZrijd1V59VmLpuqTwm5iy1byKfcR/CKGviVOowSicrFJtQOrNc9rb6BHiPAE8kbWy0hL6tODsmuwYUDIuWDH9ucQ61NrKY4feIA6m3yV87OZl9ow7KpiSIP9QsV46Wq9dgc6o0qYoPcQ99QkfhFgBJ4TCzedxE9L8tdiMYn92zLy3Zaiy5qu0hzjsLny4qu4PtI4mXAFsnoQFiLiZhYjDOF8yx1KbXNLXNDmkQQRIIPAg7heddsuy3cM10abXUQ7USJ7ykD90n79Odju3ja6vWKzqhTY173+F3wwCZ52C5/wA9wxDYrs8cgXA8wZ29U5xMubCdAlfmQ/U6ueMU2KUU1Ys9yM06pDANR8TWiA2q3i6lwD+dP1bvADoEEWW+X12GxFiKn0HUNlFTK6rFRsN06+T31DmEOQk3RTigKz7o7NsSrwomQh67eK3TqWXFSpZSWlDIajlA564dU4KB1SFS5W5I6qha6jrVVA6uuuVuQVHLhbqulca1BlZIoqjZW2vXUKDIi3FUuSVVqpaVY6lAmyUY/AmNlUESIV2Zzyr37GBxcHGCDe3PovRXleWdmatGhVNas5wcyzWtaTMiCSVfqWeYdzQ7vmCRMEhp9QdlncwntoRrAQBsw9xWNPGFoPBALSCDsRcFKsXn7GvNNrS50WI21fhSa2TQhiwHmNKtQSBN91xUqILAUXNaS4y9x1OP5eQU25QsmSjQnA2J242Wi23mtC8oWtjA12l1tjPBUB7SDrzC6bRshcywTKjC2oAWcZtHIzzRbDsf2Uv7SNJoGCNwYJiY4DmrIgLASGNLcqdXLRT+Go146ET7LTaXNap3smVHC25pnKpXzExuKauC1IPE5MrI7DqRtAEJQ5WTxLhLnneNy0s4Jc6geC9Ix+Xg7hJH5PJTWLmAjcqVIneR56+phauGe/8Ai6CKRcYLx+CT97l5qvMzEi1wnVTIgLgJZjMIBwUocRJoedyGJPmCYnMXPa1h2bMf8iCfohmtW+5WaYTIoChIjChiXOYKbjLWnU2d2njpPAG1uiPe6m86qlJr3cXaqjC7q7Q4Bx/mN9kiZXvDQXHkL+/JSOq1fxBvQDV81XqwOjUsLn0BiMQJWYepJSTGVzqTHLymWP5ghQ9mNHuSvFG6YuKXYs3TGR6lnkTK8LKlZCYl2y251lZWBgbnOIqQha1WQsxD7Je6srCQTO6lZQ1Kshc1XIRz4UFpQmdfaYMKUVJQFYcVvD1V1zrjAPTDD05SumJNkzw7o3Qcr0JZYczDofFYaQj8O4FSvprLfIQ1xgKCJT6+WidkFicm4j9+auFShdQ16QXHlMYP0ojZmpo4VlBhhxLgTvpZOwPBayVhfUAgxufLzQuc0g24QmBzOoDDHEQZgfu6lkJXssH3o7npBsFywobBYjvKbXcxf813UqgW49Fll6O48CKhLYBSbHtLnk8yjW4nmog1R6tDUq24G/MqlNoDQCGjYzf1SXtPnbKtGkWmHBzg5nEGN/LqnuMpSFQ+0GFLXSNlocJldhfmL5SRr4huAxnVPMPiweKoFPEEbWTClincTZPZsNwINS697JsiqTVVMDj44qw4fFiFm58XWGRgYZUpSoO46LsVxzQeO7QUKR0lxc78LBqM8uhSfpO2lELYk1fDiFVM9aGySQI5mCfIcU5q1cZXHhYMOzm+9Qjo3h8lX8yyplMyXOqO/E8z8tvqmuNi6t7jv6EHkqIziJnS2Z2cZaB+qhfT/E4noLD14lG1gSbqA0SdgtQEDxB39RrlLGhuwCZjIw/xbSq7h8QWK2ZZmTTTErP5HqKeyyB+st2JqDUj8DWuq59qkphltQly0UX3WZIbctBegMU+6nDrIPEvuj5TCk6gtZqlpCy5JUtJJnP1epAWLsU2JSqobp9iaEoT/LS42j1MJtM4qUZTeopKgqYdx2CeYjKHNGojjHP1twWUqCjJmAGoPoSaimlgCd1M3JyAXaSQNzwCttPAs1B3y4TzRNSHAg7EEH1Sx5DGMLx/uUkN0rmpXhZmdN7dRDHAN3JsAOrjZJn4yUbGO43F21qWvLcRKbtfKqWV4iAm9PHDmk82M9ofG4rcY1ENUaoqWJ1FEOFks6VCBriLNMO0hJcPhw1yf5pa6qz8Z44G5MQmsAZkqK5NNLMzGHSGbAcuPmuxibqv0sUZI4gwRyI4Iyi8m6Szcatyy5Y9p1pRLHpRh3wiPtULNdSDqMq0NrPVV7RgFpTPE5gI3SbGDvNzZOcMFWswWVgRqVPTe+yY4dlpRlfCMptl7mtHNxgJJVzEOkUGlw/EfCz57rcDHINQHUwjGPi4sVmHz1wGkS88h+Z4JTXDj/qO1dBZo/M/JapGNrdAi+mtb3JoCP8A7bVq2qVNDfws3Pm5Pckq0afwNaDz3d/9jdUxtXmiaNUi4KWy4rFeP3Tg5nob8fIMXtNrqp5hU718NNkto53Upva9pu0g+fT1Xp3+T4eppqmlpLwHGCW3Im4HFJFRxtn5hQDknntfB6QpsPRlvhaTAkwJ23lOu1+C7loe0eA28jw91F2ExzZqNPxEAieIvqH0Vmyk4vUEr0pupiM5Q59KrVaD4HNHvM+3h91BQwdSNiF6qAIiBpMgiAAZSypkzp8MEcLwlxzr+IRsJECwtEzdWTLKABS/ugCmWCqLafEwMFjqMapSjHVEbia6R4ytJVlBJlsjSf7VZSYfEXVex1UhpcNgospzAl0FKcjBvsJRchGpesMWuMESu6+GsNAvPNLMNiogpyHg7FBxvHFoiYYc2CJ4FBDLoO8j5oxpuunFWLEyeoMicYiPJba5cgX+S61Abpa6MsJV+2euoAxpgNuerv7BUkgsMFem1cB3kySCZjz69Eiq5DRL3CrUNgbfBvs4EzKdwcnou/EUy4mZrlcw+JIR1El3NNuzWCpue9paSwAtBN4M7nrBnlKDdl9SlOsQGmASR4r2gfNGbKrePMD6ZAuMsC0BHvqWSvCyWktvpEkDeOYHEISvmPAFI9WZtwocKs3njXFhcJIBgx92dp6JX2Y7Pur1dZMMpuaSby686R7ekq0dlnk1Hg7ObtwsR+pViZRaxsMaGjeAABPNMnL6aFRLY8Yf3GVDOso0VXPA8NQlwPU3I85v6oJlG6veI+B3QEjzA4KnAy4N4kgBIu5Ml8QB1N93ZJ82xZYCnmbuFAE1HNazg5xABH5noqTndfEV6eulRLaE6e+eI1TMaGm5FjdRx+OXayNfcq6mtQJudCSarg1g4k/uVJVxtXFtNLDUQKbrGrV8I82N3niCkGDwTGP1P8Z/m4eis+CzK4AK0suNcRtBZ/pBKQsVZBlDHNdVrudVc176bQ4uLYY7TMHeSDYovHVGkRERtFoRvZ+kXUzawq1//PUU2LywE7boOXP+cQ3wZL2TKlVJC4Y6TZPsZlcCwUGEwI4hMjkLUqIvkjcImjhnuuAnbMrmE4weWgBKZeYqjU4KTKYcK9rgdiDIPEEbFeo5dmpq4ei53xl4a7hJHGPZLKeTtdvtx0iXegTDGYAhrHUmnwhumTeB+IeaR5HJGVQDDoGW4fneF77D1KW8tOno4Xb8wF5lk5fSxLGubDw9oLTbiLeq9Tpv1MaSQ0kbcjySjNskp4iC6Wvbs9u46dQg8blDFaP4MJkTtsRu6DIHA7cuMH0hbqOWYGm40/EfEPCT+KBZ3st6JSOUkNqGHiSVsE4XInqFulRhMsQ8taXNBMAmOaEwlB9RgL/C8mSdiByj9V6ZOW7ncCcQHiLcc8iyU1XJ/n2F0tBEnmT8tlXKq0EaxcVyLRqRsxRpPa/h94HYt4gq3BtFxALKZnxDwtvECfmPdUTMH2RWUYuf4b3ObVcIp1AQ2APE2XbxII8ndEpnxF20al8L1oy9sDQBDWx/LEeYS/GYh1KoHimQw2cRBBEmDA2IlZlFWGw4+ImdrcjEcZBmLSmOsBk7i+0unpCTGmjfkaktiAQd7ham0oDJXuIcSC1s+FpEQLm03j9EXUeAQOfrf9hWcSVNiSD9+age6CiA2UmzLGFrywG1tvIWlByKSLE4moYMTBnf5ouvTDocWgxcSJjynZA5O4Oa6YJmIkfMbgoXG5m6g7SYe0CeT29CdioxhgtGcWAFmIu2VEsqtqskahDot4h/b6KuYjGRAmTvP5J9nuZnEgNYwtDTMkySYVfZkNV5loJExa4B68k5x2CiniGUW3tjns3iHd+xwNg5rHcvHLY/fJXTEYCk50uptLh96BPnPFIqGQmjhXNB1PltR0fyGQ1p6CfdWTVraHDiAR6iUHPkB2kZwpQpoty3AGlULptcAXmDEFOHlLMyzKjQbrrVGsHU3PQDcnySluZYvEiMPT+z0v8AerDxkc6dL83IShmFnx9mGACihLBmOPpUWF1Wo1jb7mJ8hufRUZgxdZxdg6ehuwr1xpAHNlMySY4kRdWXK+zFGk81Xk1qpvrqw4g82jYJ1U4qxdE/07P6/wCJ3W/Mq2Wdj6TXitiXOxOI/HUuxvRjNgBw/JNe0tBzsK9rASbGBxAIkR+9kxg8ks7RZ2zC09TvE8/C3aSNyeQEhBGTI7j5Mlq6m54xmLQHGN+S3klKagPIonOc+r4lx1vJE/CLNHoPzlc5RLTcQtl7GLfmZxH1LN2Vb/CfcGK2IE//ACKiOxjgEqy3HBrajSIirVt51HEH1lC43NBO6RTAX5DE/ctkaG1jIQlOAgjjSdgoaldw3TTcQUYMEyzYGsCm9FwVMy3MQLJ9Qxtt1icrjsph0YRyyrpcCOCesrBwBFx9Oio1fMwOKaZFmZdGm/QfmlmwsFuFTILqPKzBe3keXmoatNwh7TwhzeB6jkUc4DioC0JQsVhiLnOX4qSGG0n9hGWFjw6IF1MbpVnfaalh3hjz4i0O9yR+SLiRs56J5kg15l4pDkpmiEPRJ5zysFO5xi0StnjgVcmQ5izUxwibG0get1SCwudAHFWHHYd7iQ95AJ2+4fLh7reEydrXBzn7EGAI6/F+i1MfsW7iuRS50JT8bRS7HRTbTdHim08WjeeY4L0jMsupVLuYJP3hY/Lf1SrF5VTD2vky1oaGmIbE3b5zJ6pLLyQpsyP2ciJuzOZRSDNFR7mkDwtJABO5PAcfVPu0uLfTpsAfBcTcG5ABkfNAmg6jq7mnqc82iAAeZNlWMzp4hunvnkgFxj8LnQTHn+RVMPXJkLDVzmYqtT0PIMwFSi0kjU3wkcbcfZSOeNcifX8kg7GH+C4kXLonnAG3uU6qPvPKFOVqYqIVCSouMGO5qq582tTJLvEyTBMOAB2mdv7ImvnDqe8Ovx/VJRnLRidYnRUhr2mDANj0IG/yVsKE3KZHUirjLs/jmV3aHgGoyHNcLOLRwJG8W9Cmv+W0zUNR2pzpk6jaeFo8kCzIKbKorU9THgyAD4CCILSIJAM8EQcfJDHtNOoduLXf0O4+RS2Z9+wyy6FNBMzyEPIdRqGk4EkAAFjuYLdiLfoQoqOafZAftFJzGkiarQalLlB0+Jn/ACEX3K6x3aShRDO8fL3QWsYNdQyNtAuPWAhMX9txO3/SUXbzD6zhxt8NP6qV7MPzPH2dfy+5YADYjPFdoMLSZrdiKel3wgEPLgfwtaZPokmUY/HViadBgo0TJFSq06g07FrDs473SnJMkw+DrVxqOpj2Bji1j3BrqbXEwRvJNxGyvH2l1Gk0vcN4L3H8TjDiIk2OyuSmLSC/1P8AiddmQ4Hs3SpO712qtW/3Kp1O/wCI2Z0hNS6375rQrAgEOBB2IIIUNasGmIueA49Um7ljuEFQzXa65LjI9jcWEG/VDl/EbrCSePsqjJUm4UXqsZ52XGJqmpUrvAsGtaBDWgC1+MyfVPR++C2B0VlzMptfMqwDaMrFLsPhmSQXl0HTrIgGLEhoE3SbFdkarAT3lLSLlxJaB1MhX/fgAqL237QkmphQwaWwC50ySLy29h9UzxcmbNk63++ByIgFmVDOcxaC1rSSWt0lw+F1yQWgiRud+eyCy5jqjuiDcwudCufZzKDpLgJ0xI4xzWpmyDCmvMWYljDMDlwgWUmKy0EbJlTeAEPisSIWH+05S3mW6KBKfjsH3bvD7BYMYQEfh8UPtdEbzUYI5hzoPyKC7U5ecNXfT+6fEw82nb229Fpoe9K3mUrVwOn2iq0XeAiDu1wDmnzBVnyTtwYh2Hpgce78F+cKgCmXOsnuAyt0WRORhw9KYSwYjxPRsP2lpvHwuHsiBmtPkfYKg4DC1CTPhAveYPkVYcC0EQHA+RBWHn4mMHUKuVpYHZnTi5i0xx/dl5N2yBxGLe78IayN4hoMf/pM8Xm5ZiSfutOgjeQDc/VMOzGXsrMq1iP9StUc2fwyGj/tK0OHgXh3lb5A/rJ9QmevUmKZpQOGzKm5xY14LhcgXhF6xBVcAoVGbEmMJYK2l5YQGgm0WHT3W8vx+slpabbHeeY8wh83x7GPaSwkhsi8cTuI4fmn8SkkqR8QbsK7XJMQQOY8kvqV5MOE/Lb6pZj+1lMWLHehB/RZmb21sGXsfDgO8BBLS1zSeO4sCPVZmbBkDDuNThkB8RnQrMJ06xI3Ew4dYN0B2kwRfScRdwgqkVM+qubpe4OuIJa0OFxs4CeCtmRVjUdoLntqaJNNwlhbYlw1XEyIvzRPQbDTQfqB/bM7P4oMYGapJaHkfhJJt6jSfVOO9kHzSzMMAWuPdtpgkTaW32hzYt7rvCVKgpzUYQRvpIcPMRf5I1DIey/PxIWwagOeB3BVp7id/I/v0Ks+IxPfAigx9UjfSIA8yVxiuydVtB5qVW7tqd2wcgQQXm5gE7RxTWLIEFNqCOIk3HtHOWmhSLpdWLAdFMa3nhMD4QYmTAulePweMrka3jC0pmGEPqnzf8NM+U+a6yrtA2g0MdQaxuxdTEepbx91YsQ9rmammQRIcLiOYWfn/LPZR/HzGlIYSu5Rl9HB6z3fhMu7673mb6ahN5nY7Jpgc1pV5a19xFjYkGLgHzVHzfNasuZLdOx0CAfdAZbQqVqjW0mlzgQbWAgiCXfd81PoHIvdzuB9b3UJf6OH/wCtruIb/p0nA/eHxsP/AGeyRdpDUfXklwpjZpJgkWLwOqc0MjdUf9pc9zXubo0tdbS02OpsEyZPkQuMbl4aTa/HifUoXqdDd3oCFYWIJljjYbfX+ydsH73KRUCWmE3p1LJPKbMhTCm7QttKjpuLhYSdvYSteKmx73gGBOkbjndD6EwlwynUQ2c4msyi51Foe8R4SCbTeADcxwUbcfS7vvNYDBxNo6Ec+iHHaLC79+3y8X0hGxBwb63U4kfcrz+3da4NGmCOB12PkSkGe54cSP4tJmv7r2S0joZJ1BNe1OGZiHmvQrNqWAczV4xHFoNyI4KsCnqW9gTHXZRRijs10TB8FTg3VryLMu7qsji4NjmCYhJ8LhOaZ5Jljn1mER4XNdvEAGSeqDySrXcoLvUu+Myam9+q7eJAMA/p6JBjsgeCdLgR1MEdCrdimnhdDkBwJ5rB9ZkMcbEplFxFBmF7iq+CWVtbyLwC0hvmAY90J2w7S0MQzRGpwu1w3BPXl0RPa/D6tNOSO8fE8GgXJPoqDi6Ya9waZAMStviYxlC5GJsXFzqwIZlEawDxXo+VYWQF5Zh3aHhw4L1LJM5w/dhxqtba4JgjpCr+KK9AqLnIAG3HLMAIuAvM+0+XfZa0NdZ0lsOBIE7GLhemZZmzcQ4tpCWN+J5sJOzWjifoq/2u7M4V7xoeyhWcQ50kNYWbF5bzmNkh+H5WxZimS9jx5/n9QrqCLE85qVLW34LvA5lUpsDO8e2JMBxi9+HmryzIMLQDKZexwdVAdWcGkuJa/RSbB8EFvi8xzsgxfZyjSOmvidD7wAzV4Q5zQ7fjEx1W6ufGwqv6QVVPXsMwS1wa1ukFpLQGzJBAMDhB913jaVR4LZDGnck3I3gAIPvTIA2F0wdVtJS+I+GfZluwOpX8dTFMeGo7UOGmPUEFBZpmhqBhPxBmlx5wTB9kTnVYSUgrv+i0BvcAT8Rdizre0c3Ae5hejsyxjAGsaQ0DSescTzNz7qpZLl9HvaVSpi6IDXB2gkhxIMgHUABeOa9EqCdh68wsj8SyeAIzgTVxTgMloU3Oc2iwOMXi9hwn4fRT1MM3ve+AmoWd10DdWqT7IPD5s1tV9CsdNRt2k2D2HYjrwjonDW7LOJcH3fP9ocVFmYtsHRB21OsT008R+7INznBhOlrnSNLTs5xIAFxb1THOX0zTd4m6mGJM+F28E8JHNJcsx41gn2+vqm8IIpjBuaaWHLsG2l8NhFxxDpl0x1RVVocCDsbFTh4mDfr+/oo6jQATIj2jhdXyKT7hv+8IBqpXmZJqOlwgcTv7KPNqn2cd3SMAieZZaLdTE+qeVTOzi3rAP1QlDLKYJcZed5cQfWEDvqjBsmqWUOjhX1KlR1iGsO8QXOsB5xJ9E/7M1xSwxaWaXFxaTaSDEuM8GifZF49lNpOiAOQEDbfrsl+EIcS87Gzf6eJ9f0UZMprY1BIvQy5U9MCCNIHC4gf2SzH1ab7SQecW9UkyvDdzr0vdDjOmbRyhNcOGuAImevBAbIBobh+1iK8c3QQ07xPT0RuVAOEm42QWfVXNeQ5jnsMTpBJafxMPA9NiiMveabGtN9TvCbjUCJkg3BA4LnX2BhKDzG2HaxuoNcSZAI5QtZh4qT28XCB6rQgGbSd4i/n5LUmZhDOQWCIT9Iow3Z2A4PfLXFpLRMEgyLqpZjlD2EksIvyMDkvSBK7fS1AgwQdwRP1RsfKZTco2EETxupRvK7FT3Vtz3GYekSKFFhf+MiWj+kHcqqdwXmTuTdbmLLa9mFRVlA1C8LWBEIptfTBBgi4IQ7cuPDdFYXCw9gfpkmBqEtmCbjkl8rIxldy65LmTa9OZ8Qs7z5+qlrS24Sbs81/2kzpgNMlrWtBvYwAJVjr0gVh8lADYjuMkruUXtZhX12lrLGZiSJ9t1Q35PWadLmET7Er2athmpdmD6bQdYBHPiE1xPxFsajGBcG6G7nj7qLmmHNIPVTmsALG6d9q8bSefAQSd1D2T7OVcTVY/SW0g4Oc87ENMw0H4iduS3RmHpepk1BVep6N2TwrqOFp04/iEa3k/c138XMxAj6KbtH2fZiqHdEw4O1teRqOqIJPmLe3IJvTphogfvqeZSXtpmZw+Ee9pAeSGNngXG5HUN1H0XlkzZMvJBx6JP/f/ACNdQFozx8giWzsT5TtI9lPjcQ6q7W/eAPQAAfRQUWEmACTyFz7BaJXsPmKT2vBVC6TCNe+BdYsSQA8SF8SuY6Xl0CYv6c0sqUCTbksWJsGhBxdicrcYU+Cw9eiXOp1XNc5ujVJJDZBgTsbC6xYkOTmYahFgWGxNSniKbqxdWLXA+Ml5Ik2E9ZhWvtL2goub/CrVKdW1gHtB6OB281ixR6QysrGWDkAyw5Nl4FAB7+9D/E4mfEXcTNzw9kFQp1MK4ubRbVpji0AVmjz2f8isWLPx5CHK/FxsqKuWPBYkVKYqAOAcJAcII8wF0WQOJ4/PosWIuSWHiR4h0jYaufPzj6rTqILbgEe48lixUX8y+06J83ysP0tpkNJ+KZMj8uXqkrcDWDw1zCGz8W7Y8wsWIIylgQYNkHmEuBbULYtYhHUHaYW1iUY+JAk+KxHhJcYHFJMNTrVa7axhrGfA133uEnksWIit0HYTjsxvRL9TnFx0nZpAt6hTmqtLEPI5JlpgeeBHlzS3M8dUgtBgERAH57rFiJiMhjqULGU3h9tkxy+gQOaxYtXNkb06iwAuNKY5tUrsubWLQTGlwfH4gNxPBYsSCsQ1iX6g6McYbDMoB2gkFwi8uA5QFBis7bSb4jt5wQsWIOFfWYBzLueo1KZnfbQkltH35eSqePzKrUu95PTh7LFi9Ng4uLCB1EDd+YCVccH/AIhVmMa3uKR0gC0tEDk0WC0sRcuDHlFOLk2R4l6ybtJRxDRpe3XALmSZaeIuBMcwjqmHpVSC9jXxtqAcBO5ANgeqxYvLc7jLxspGMmGRy3mF0cOxghjGt/paG/ReW9puyuI+01DSpPqMc7WHCN3XcOGxJWLFT8P5WTE5I3Y+ZbIoqf/Z'
    # plant_name = 'Aloe Vera'
    # lifespan = 5
    # maintaining_guide = 'Water once a week'
    # temperature_contribution = 'High'
    # required_tools = 'Watering can'

    plant_image_url = plants_data_detail_df['original_url']
    plant_name = plants_data_detail_df['common_name']
    lifespan = plants_data_detail_df['cycle']
    maintaining_guide = plants_data_detail_df['watering']
    temperature_contribution = 'High'
    required_tools = 'Watering can'

    # 构造响应数据
    response_data = {
        'plantImageUrl': plant_image_url,
        'plantName': plant_name,
        'lifespan': lifespan,
        'maintainingGuide': maintaining_guide,
        'temperatureContribution': temperature_contribution,
        'requiredTools': required_tools
    }

    # 将结果以 JSON 格式返回给前端
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True, port=8000)