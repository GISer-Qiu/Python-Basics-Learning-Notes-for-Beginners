# 读取csv文件
"""
前几节我们学的都是读取txt文件，这次我们来读取csv——使用 csv 模块
csv.reader(file)：一个迭代器，解析 CSV 文件，迭代时逐行解析（处理逗号、引号等），每次生成一个列表。这一特征体现在后续代码中（留意注释）
"""

# 实战演习
import csv   # 导入模块

with open("../第七章-实验数据/坐标 - 梅州加油站点数据.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for a in reader:   # 因为 reader 对应的是逐行解析，所以要用for循环
        print(a)

