import os
import sys
from converter import *

file_path = ""
file_name = ""


for arg in sys.argv[1:]:
    print(arg)

if True:
    print("---------------------------------")
    path = input("Press Enter the path file path:")
    path = path_correction(path)

    file_path = os.path.dirname(path)
    file_path += "/"
    file_name = os.path.basename(path)
    file_name = file_name.split(".")[0]

    while True:
        print("--------------------------")
        if (path[len(path)-4:len(path)] == "xlsx"):
            dict_data, file_name = read_xlsx(path)
        elif (path[len(path)-3:len(path)] == "csv"):
            dict_data = read_csv(path)
        elif (path[len(path)-4:len(path)] == "json"):
            dict_data = read_json(path)
        else:
            print("unknown extension")
            exit()


        output_file(file_path, file_name, dict_data)


    # result = read_xlsx(path)
    # json_data = json.dumps(result, indent=4, ensure_ascii=False)
    # print(json_data)