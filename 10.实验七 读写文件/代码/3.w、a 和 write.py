# "w"、"a" 模式和 file.write() 方法

# 实战演示
with open("../第七章-实验数据/example_0.txt", "w", encoding = "utf-8")as example_1:
    example_1.write("(This a new sentence.) Hello world!\n")   #需要自动换行
with open("../第七章-实验数据/example_0.txt", "a", encoding = "utf-8") as example_1:
        example_1.write("(This a new sentence.) Nice to meet you!\n")
print("Worked successfully!")   #顶格写！

# 第1节提到了../ 这个相对路径的写法，现在介绍一种更稳妥的写法
