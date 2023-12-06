# Python3中主要有6种不同数据类型
"""
1、Number
2、String
3、List
4、Tuple
5、Dict
6、Set
"""

# 1.Number类型 主要包含 int（整型）float（浮点类型） bool（类型）
# int 类型
num = 32
print(num)

# float 类型
num1 = 3.21
print(num1)

# bool 类型 在python中归为int类型的一个子类
print(11 > 8)
print(4 < 3)

# String 类型 字符串类型主要有数字、字母、下划线、汉字组成的一串字符，一般使用单引号或者双引号包裹
str1 = "hello"
str2 = "world"
str3 = '''
这个世界会好吗？
谁知道呢
'''
print(str1, str2, str3)

# List 类型 列表使用[]来表示，[]里面可以存放字符\数字\字符串\甚至还可以嵌套列表
list1 = ['Selena Gomez', 'Tylor Swift', 12, 100.32, True]
print(list1)

# Tuple类型 元组使用（）来表示，它是一种特殊的列表，（）里面可以存放字符\数字\字符串\甚至还可以嵌套列表
tup = (12, 43, 9.87, True, False, "world")
print(tup)

# Dict 类型 字典使用{ }来表示 字典由索引和对应的值组成 {key1:value1, key2:value2 ......}
user = {"name": "Moore", "age": 29, "sex": "Female", "weight": 110}
print(user)

# Set 类型 集合 使用{ }来表示，{}里面直接存放值即可
# 和字典的区别是 大括号里只放值
set1 = {123, 87.56, True, False}
print(set1)
