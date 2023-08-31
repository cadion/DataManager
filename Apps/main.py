import pandas as pd
import sys
import os
import os.path
import xlrd
import csv
import json
import re
import tkinter
from tkinter import filedialog
'''
need install library
- pandas
'''



if __name__ == '__main__':
    # chart_a = [{"name": "a", "value": 1}, {"name": "b", "value": 2}, {"name": "c", "value": 3}]
    # chart_b = [{"name": "a", "value": 1}, {"name": "c", "value": 2}, {"name": "d", "value": 3}]
    # chart_c = [{"name": "a", "value": 1}, {"name": "b", "value": 2}, {"name": "c", "value": 3}]
    # df_a = pd.DataFrame(chart_a)
    # df_b = pd.DataFrame(chart_b)
    # df_c = pd.DataFrame(chart_c)
    # print(pd.merge(df_a, df_b, how="outer"))
    with open(os.path.dirname(os.path.realpath(__file__))+r'\column_name_replace.csv', newline='', encoding='UTF8') as csvfile:
        pass
    print("hi")