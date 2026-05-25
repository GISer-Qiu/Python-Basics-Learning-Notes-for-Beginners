# 读写json文件
"""
继续读写其他类型的文件，今天讲json文件——使用 json 模块

json.dump() 将 Python 字典写入 JSON 文件
json.load() 读取 JSON 文件并转换为 Python 对象
"""

# 实战演习
import json
data = {"name": "Alice", "age": 25, "city": "New York"}
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
with open("data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
    print("读取的 JSON 数据：", loaded_data)

