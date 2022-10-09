import pandas as pd
import os

input_dir = fr"E:\PycharmProjects\pythonProject\pandas数据处理\merge"
output_path = fr"E:\PycharmProjects\pythonProject\pandas数据处理\output\result.csv"

df = None
flag = 0
for filename in os.listdir(input_dir):
    filepath = input_dir + os.sep + filename
    if flag == 0:
        df = pd.read_excel(filepath)
        flag = 1
    else:
        df = pd.concat([df, pd.read_excel(filepath)])
df.to_csv(output_path)
