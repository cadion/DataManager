import unreal
import json
import unreal as ue
import os
#from converter import *

'''
설정 작업
1. setting
2. Project: DataSolution
3. Python Interpreter
4. Interpreter.Dropbox.ShowAll
5. FileTree Icon
6. Add %PythonStub%
7. in UE editor
    7-1. import unreal
    7-2. import unrealScript as us
    
리로드 방법 ( UE editor )
1. import imp
2. imp.reload(unrealScript)

api doc : https://docs.unrealengine.com/4.27/en-US/PythonAPI/
'''



unreal.log("Hello Unreal!")
def say_hi():
    unreal.log("Hello Unreal2!")

def get_selected_assets():
    return unreal.EditorUtilityLibrary.get_selected_assets()

def get_selected_asset():
    selected_asset_list = get_selected_assets()
    selected_asset = selected_asset_list[0]
    return selected_asset

def get_asset_path(asset):
    return unreal.AssetLibrary.get_asset_path(asset)

def get_asset_name(asset):
    return unreal.AssetLibrary.get_asset_name(asset)

def get_data_table_data(asset):
    dict_data = {}
    row_names = unreal.DataTableFunctionLibrary.get_data_table_row_names(dict_data)
    for col_name in unreal.DataTableFunctionLibrary.get_data_table_column_names(dict_data):
        positions = unreal.DataTableFunctionLibrary.get_data_table_column_as_string(dict_data, col_name)
        for idx, col in enumerate(positions):
            unreal.log(f"{row_names[idx]} - {col_name}: {col}")
    return False


def get_data_asset(asset):
    dict_data = {}




def print_selected_data_asset():
    asset = get_selected_asset()
    unreal.log(type(asset))
    data_asset = get_data_asset(asset)
    unreal.log(data_asset)

def get_selected_data():
    data = get_selected_asset()
    return get_data_table_data(data)
    if (type(data) == unreal.DataTable):
        return get_data_table_data(data)

    return False

def save_selected_data_as_json():
    with open(f'save_data.json', 'w') as f:
        json.dump(get_selected_data(), f, indent=4, ensure_ascii=False)


def dummy():
    data_table = 0 #data table ref
    column_name = 0 # column name in dt
    unreal.DataTableFunctionLibrary.get_data_table_row_names(data_table) #data_table 내 Row Names, 무조건 string으로
    unreal.DataTableFunctionLibrary.get_data_table_column_as_string(data_table, column_name) #data_table 내 Column Names, 무조건 string으로
