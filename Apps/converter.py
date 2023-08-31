import os
import math
import json
from pandas.__init__ import pandas as pd
from enum import Enum
import warnings


mgl_xlsx_format = {
    "first_col": 1,
    "first_row": 3,
    "ignore_colname": "#",
    "map_colname": "{",
    "list_colname": "[",
    "split_colname": "/"
}

class mgl_ds(Enum):
    none = 0
    map = 1
    list = 2
    string_table = 3
def mgl_datastructure_formatting(data: dict):
    post_data = []
    for data_A in data:
        post_data_comp = {}
        state = mgl_ds.none
        state_name = ""
        remove_list = []
        for key in data_A.keys():
            if state == mgl_ds.map:
                if state_name + "/" in key:
                    post_data_comp[state_name][key.replace(state_name + "/", "")] = data_A[key]
                    continue
                else:
                    state = mgl_ds.none
                    state_name = ""
            elif state == mgl_ds.string_table:
                # Todo: string table 이름만드는거 추가해야 함
                if type(post_data_comp[state_name]) == float and math.isnan(post_data_comp[state_name]):
                    post_data_comp.pop(state_name)
                else:
                    post_data_comp[state_name] += "/" + str(data_A[key])
                remove_list.append(key)
                state = mgl_ds.none
                state_name = ""
                continue

            if "{}" in key:
                # Todo: 이거 임시구현임. 방법마련필요
                state = mgl_ds.map
                state_name = key.replace("{}", "")
                post_data_comp[state_name] = {}
                continue
            elif "[]" in key:
                if type(data_A[key]) == float and math.isnan(data_A[key]):
                    remove_list.append(key)
                elif type(data_A[key]) == str:
                    post_data_comp[key.replace("[]", "")] = data_A[key].split(",")
                else:
                    post_data_comp[key.replace("[]", "")] = [data_A[key]]
                continue
            elif key[0:2] == "ST":
                post_data_comp[key] = data_A[key]
                state = mgl_ds.string_table
                state_name = key
            else:
                post_data_comp[key] = data_A[key]
        for key in remove_list:
            data_A.pop(key)
        post_data.append(post_data_comp)
    return post_data




def path_correction(path: str):
    result = path.replace("\\", "/")
    result = result.replace("\"", "")
    return result

def select_sheet(data: dict):
    print("select sheet : ( 0 = quit )")
    i = 1
    temp_list = []
    for key in data.keys():
        print("\t" + str(i) + ". " + key)
        i += 1
    sheet_name = input("select sheet name:")
    if sheet_name == "0":
        exit()
    if sheet_name.isdecimal() and not(sheet_name in data.keys()):
        sheet_name = list(data.keys())[int(sheet_name) - 1]
    return data[sheet_name], sheet_name

def read_xlsx(file_ref: str):
    # with open(file_ref, "r") as f:
    warnings.simplefilter(action="ignore", category=UserWarning)
    data = pd.read_excel(file_ref, header=2, sheet_name=None)

    if len(data.keys()) > 1:
        data, sheet_name = select_sheet(data)
        print("------")
    else:
        sheet_name = list(data.keys())[0]
        data = data[sheet_name]
    dict_data = data.to_dict(orient="records")
    #json_data = data.to_json("data.json", orient="columns", force_ascii=False)
    #csv_data = data.to_csv("data.csv", header=None, index=False, encoding="utf-8-sig")
    dict_data = mgl_datastructure_formatting(dict_data)
    return dict_data, sheet_name

def read_json(file_ref: str):
    with open(file_ref, "r", encoding="utf-8-sig") as f:
        data = json.load(f)
    dict_data = data
    #data = pd.read_json(file_ref, orient="records")
    #dict_data = data.to_dict(orient="records")
    return dict_data

def read_csv(file_ref: str):
    data = pd.read_csv(file_ref, header=0)
    dict_data = data.to_dict(orient="records")
    return dict_data

def save_xlsx(file_ref: str, data: dict):
    df = pd.DataFrame(data)
    if os.path.isfile(file_ref):
        is_add = input("파일이 이미존재합니다. 내용을 추가하려면 y, 덮어쓰려면 n을 입력하세요.")
        if is_add == "y":
            dfA = pd.read_excel(file_ref, header=2)
            df = pd.merge(dfA, df, how="outer")
    df.to_excel(file_ref, index=False, startrow=2)

def save_json(file_ref: str, data: dict):

    for data_A in data:
        keyList = []
        for data_A_key in data_A.keys():
            if ((type(data_A[data_A_key]) == float or type(data_A[data_A_key]) == int) and math.isnan(data_A[data_A_key])):
                keyList.append(data_A_key)
        for key in keyList:
            data_A.pop(key)


    with open(file_ref, "w", encoding="utf-8-sig") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def save_csv(file_ref: str, data: dict):
    df = pd.DataFrame(data)
    df.to_csv(file_ref, header=True, index=False, encoding="utf-8-sig")


def output_file(file_path:str, file_name:str, dict_data):
    select_num = input(
        "Press Enter the number of the function you want to use:\n"
        "1. to json\t\t"
        "2. to csv\t\t"
        "3. to xlsx\t\t"
        "4. to exit"
        "\n: ")

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
