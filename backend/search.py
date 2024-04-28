import pandas as pd
import os
from get_prediction import PREFIX
# word = "Collins"
# PREFIX = "backend"
# PREFIX = "./"

df = pd.read_csv(os.path.join(PREFIX,"CBD.csv"))
df["address"] = df["address"].astype(str)

def search(key_word:str):
    # print(word, key_word)
    # if word == key_word:
    #     print(True)
    result = df[df['address'].str.contains(key_word.strip(), case=False, na=False)]
    records = result.to_dict(orient='records')
    # for index, row in df.iterrows():
    #     # if row['address']
    #     if key_word in row["address"]:
    #         # print(True)
    #         records.append(row.to_dict())
    # # print(len(records))
    result_dict = {'data': records}
    return result_dict

# print(search(word))