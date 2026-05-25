"""
循环的基本语法与格式
1.for循环（以次数为界定）
for 【变量名】 in 【可迭代对象】：
    【对每个变量做一些事情】
    ……

    补充知识：
      temperature_dict.keys()  所有键
      temperature_dict.values()  所有值
      temperature_dict.items()  所有键、值对

2.while循环（以条件为界定，适合用在条件循环不知在何时结束的情况下使用）
while 【条件】:
    【行动】
"""

# while循环案例：加法计算器
# ——输入任意数量的数字，计算平均值
# 输入Q表示输入完成
# 平均值 = 总数 / 个数
total = 0
count = 0
user_input = input("输入任意数量的数字，计算平均值(输入Q表示计算结束)：")
while user_input != "Q":
    num = float(user_input)    #可写可不写，如果不写↓
    total = total +num             #这里的num就直接写成float(user_input)
    count = count + 1
    user_input = input("输入任意数量的数字，计算平均值(输入Q表示计算结束)：")
if count == 0:    #双等号是比较运算符
    result = 0       #这里的if写的是特殊情况
else:
    result = total / count
print(f"结果为：{result}")



#以下内容暂时作废

#情境导入
"""
print("不要98折，不要95折，清仓大甩卖，全场75折")
print('98折','95折','75折'in"不要98折，不要95折，清仓大甩卖，全场75折")     #无法输出'75折'？？

代码简化：
title = "不要98折，不要95折，清仓大甩卖，全场75折"
print(title)
print('98折','95折','75折' in title)      同样无法输出'75折'


#超市开门前的检查：检查货架
for shelf in range(1, 11):
    print(f"正在检查第 {shelf} 号货架")     #f可以写成F；f和{}配合使用，直接把变量和字符串接在一起；{}内可以放任何合法的 Python 表达式
print("检查完成！")
#复杂写法：print("正在检查第 "+ str(shelf)+ "号货架")

#顾客购物、扫描结账
total = 0
item_price = input("请输入商品价格（输入 '结束' 结账）：")
while item_price != '结束':          # 当输入不是“结束”时继续
    total = total + float(item_price)   # 累加价格
    item_price = input("请输入下一个商品价格（输入 '结束' 结账）：")
print(f"总计：{total} 元")

#discount  = input("你想优惠多少钱（输入 '结束' 结账）：")
#while last_price

"""

