import os
import json
import pandas as pd


mgl_xlsx_format = {
    "first_col": 1,
    "first_row": 3,
    "ignore_colname": "#",
    "map_colname": "{",
    "list_colname": "[",
    "split_colname": "/"
}

def path_correction(path: str):
    result = path.replace("\\", "/")
    result = result.replace("\"", "")
    return result

def read_xlsx(file_ref: str):
    # with open(file_ref, "r") as f:
    data = pd.read_excel(file_ref, header=2)
    dict_data = data.to_dict(orient="records")
    #json_data = data.to_json("data.json", orient="columns", force_ascii=False)
    #csv_data = data.to_csv("data.csv", header=None, index=False, encoding="utf-8-sig")
    return dict_data

def read_json(file_ref: str):
    with open(file_ref, "r", encoding="utf-8-sig") as f:
        data = json.load(f)
    dict_data = data
    #data = pd.read_json(file_ref, orient="records")
    #dict_data = data.to_dict(orient="records")
    return dict_data

def read_csv(file_ref: str):
    data = pd.read_csv(file_ref, header=None)
    dict_data = data.to_dict(orient="records")
    return dict_data

def save_xlsx(file_ref: str, data: dict):
    df = pd.DataFrame(data)
    df.to_excel(file_ref, index=False)

def save_json(file_ref: str, data: dict):
    with open(file_ref, "w", encoding="utf-8-sig") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def save_csv(file_ref: str, data: dict):
    df = pd.DataFrame(data)
    df.to_csv(file_ref, header=None, index=False, encoding="utf-8-sig")


def output_file(file_path:str, file_name:str, dict_data):
    select_num = input(
        "Press Enter the number of the function you want to use:\n"
        "1. to json\n"
        "2. to csv\n"
        "3. to xlsx\n"
        "4. to exit\n"
        ": ")

    if select_num == "1":
        save_path = file_path + file_name + ".json"
        save_json(save_path, dict_data)
        print("save json file")
    elif select_num == "2":
        save_path = file_path + file_name + ".csv"
        save_csv(save_path, dict_data)
        print("save csv file")
    elif select_num == "3":
        save_path = file_path + file_name + ".xlsx"
        save_xlsx(save_path, dict_data)
        print("save xlsx file")
    elif select_num == "4":
        exit()
