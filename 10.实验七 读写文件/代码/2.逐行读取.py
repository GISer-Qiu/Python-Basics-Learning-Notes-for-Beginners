#逐行读取
"""
上一节提到打开模式和读写方法要对应，
对于 "r" 的读方法，我们不只有一种，
还有 file.readline() 和 file.readlines()
    file.readline() 读取单行数据；
    file.readlines() 读取所有行，一次性将文件所有行读入内存，返回一个真正的列表，包含每行字符串
        file在此处同样代表自己命名和赋值的变量

关于读写方法的注意事项
假定现在有以下代码
with open(".../.../...", "r", encoding="utf-8") as example_1:
    print("逐行读取文件的内容：\n", example_1.readlines())
    print("读取文件单行的内容：", example_1.readline())      # 留意这一行特殊代码

运行代码之后，最后一行的代码只会返回“读取文件单行的内容：”，而不会返回打开文件后的内容。
这是因为代码会再文件内部“安置”一个“指针”，记录你读到了哪里，所以当运行了 file.readlines() 后，即“指针”已走到文件末尾，代码只会返回空字符串
"""

# 实战演示
with open("../第七章-实验数据/wrj03-004sd01.txt", "r", encoding="utf-8") as example_1:
   print("读取文件单行的内容：", example_1.readline())

with open("../第七章-实验数据/wrj03-004sd01.txt", "r", encoding="utf-8") as example_1:
    print("逐行读取文件的内容：\n", example_1.readlines())

"""
小技巧：如果不想要file.readlines()末尾的换行符，可以使用.strip()

.strip() 函数：
去除开头和结尾的空格、制表符 \t、换行符 \n，中间的空格不受影响
还可以在 括号() 中去掉的指定的字符，写法("要去除的字符")

变形：
.lstrip()  只去左边（开头）
.rstrip()  只去右边（结尾）
"""
# 实战演示
with open("../第七章-实验数据/wrj03-004sd01.txt", "r", encoding="utf-8") as example_1:
    contents = example_1.readlines()
    for line in contents:
        print(line.strip())
# 更简洁的写法：无需重复赋值
with open("../第七章-实验数据/wrj03-004sd01.txt", "r", encoding="utf-8") as example_1:
    for line in example_1:
        print(line.strip())
"""
原因：
文件对象本身就可以被 for 循环逐行读取。Python 内部会自动逐行读取，每一次循环产生一行（包含结尾的 \n），直到文件末尾自动停止

区别：
第一种写法占用内存更多，会产生中间列表 list，适合随机访问某一行或需要反复遍历的情况
第二种写法且更加高效，会直接拿到每一行的字符串 str，适合只需逐行处理一次的情况
"""
