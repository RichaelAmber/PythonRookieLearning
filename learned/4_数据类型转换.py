# 数据类型转换： int==>str str==>int bool==>int
# 不同数据类型，运算规则不一样

# age = input("Hi,Moore.Please print your age:")
age = 29
# 在python中，字符串和整型不能直接进行数学运算
# print(age + 1)

# int() 将其他类型转换为整型
'''
    参数：
        1.要转换的数据类型
        2.base=10 表示禁止 默认是10进制
    返回值：
    返回的是一个整型的数据
'''
print(int(age) + 1)

str1 = "12"
print(int(str1))
print(int(str1, base=3))
# base其实表示的是 把该字符串从其他进制转化为10进制

# str()：将其他数据类型转换为字符串类型
num = 12
num1 = 87
print(num + num1)
print(type(num), type(num1))

str1 = str(num)
str2 = str(num1)
print(type(str1), type(str2))
print(str1 + str2)  # 字符串加号是一个拼接

# float()：将其他数据类型转换为浮点型
float1 = "12.34"
print(type(float1))
print(type(float(float1)))
float2 = "Hello"  # 不能转换为浮点型
# print(float(float2))

# bool()：将其他类型转换为布尔类型
print(bool(100))  # True
print(bool(3.14))  # True
print(bool(0))  # False
print(bool("hello"))
print(bool(''))
print(bool(""))
print(bool(' '))
print(bool([12, 34, 7]))
print(bool([]))
print(bool((32, 67, 98)))
print(bool({"name": "nigger", "age": 29}))
print(bool(()))
print(bool({}))
print(bool(None))
# 数字0，空字符串""或者''，空列表[]，空元组(),空字典{}，空集合set(),None
# 这些数据转换为bool类型时是False.

# list()：将其他数据类型转换为列表
tup = (12, 34, 678, 9)
print(tup, type(tup))
print(type(list(tup)))
list1 = list(tup)
print(list1)
str1 = "hello"
list2 = list(str1)
print(list2)
# 注意：一般情况下，是字符串和元组类型的数据转换为列表居多

# tuple()：将其他数据类型转化为元组
list1 = [12.45, 678, 9, True, False, 87]
print(type(list1), type(tuple(list1)),tuple(list1))
string1 = "123"
print(type(string1), type(tuple(string1)))
print(tuple(string1))
# 注意：一般情况下，是字符串和列表类型的数据转换为列表居多
