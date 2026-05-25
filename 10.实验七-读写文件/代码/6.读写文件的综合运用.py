# 读取文件夹内的所有特定格式的文件目标
"""
os 和 glob 模块：批量读取某个文件夹下的所有 .txt 或其他特定格式的文件
os.listdir(folder_path)  获取文件夹内所有文件
filename.endswith(".txt")  筛选特定格式文件
os.path.join(folder_path, filename)  获取完整路径
"""

import os
# 指定文件夹路径
folder_path = "D:/2个人/学业和就业/大一下/Python/10.实验七-读写文件/Python代码"
file_extension = ".txt"  # 目标文件格式

# 遍历文件夹内所有指定格式的文件
for filename in os.listdir(folder_path):
    if filename.endswith(file_extension):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            print(f"文件: {filename} 内容:\n{content}\n")