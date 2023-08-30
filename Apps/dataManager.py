import os
from converter import *

file_path = ""
file_name = ""

if True:
    path = input("Press Enter the path file path:")
    path = path_correction(path)
    #path = "C:/Users/dragon_kim/Desktop/Fork/design_data/table/src/ncpcostumeitem.xlsx" # 해제 예정

    file_path = os.path.dirname(path)
    file_path += "/"
    file_name = os.path.basename(path)
    file_name = file_name.split(".")[0]

    if (path[len(path)-4:len(path)] == "xlsx"):
        print("you select excel file")
        dict_data = read_xlsx(path)
    elif (path[len(path)-3:len(path)] == "csv"):
        print("you select csv file")
        dict_data = read_csv(path)
    elif (path[len(path)-4:len(path)] == "json"):
        print("you select json file")
        dict_data = read_json(path)
    else:
        print("unknown extension")
        exit()

    output_file(file_path, file_name, dict_data)


    # result = read_xlsx(path)
    # json_data = json.dumps(result, indent=4, ensure_ascii=False)
    # print(json_data)