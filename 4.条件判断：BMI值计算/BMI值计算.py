user_weight = float(input("请输入你的体重(单位 kg)："))
# 错误写法：user_weight = intput(print(float"请输入你的体重")))
user_height = float(input("请输入你的身高(单位 m)："))
user_BMI = user_weight / user_height **2
print(f"你的BMI值为：{user_BMI}")

if user_BMI <= 18.5:
    print("你的身体偏瘦")
elif 18.5 < user_BMI <= 25:
    print("你的身体正常")
elif 25 < user_BMI <= 30:
    print("你的身体偏胖")
else:
    print("你的身体肥胖")