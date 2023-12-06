"""
filter是一个内置类
    filter() 第一个参数是一个函数，第二个参数是一个可迭代对象
    返回值是一个filter类型的对象
    可以发现 filter的函数不能改变值，而map可以
map也是一个内置类
    map()：第一个参数是一个函数，第二个参数是一个可迭代对象
    返回值是一个map类型的函数
"""
from random import random

ages = [12, 34, 56, 77, 89, 43, 25, 32]
print(ages)

ages1 = filter(lambda ele: ele > 30, ages)
print(list(ages1), type(ages1))

ages2 = map(lambda ele: ele + 30, ages)
print(list(ages2), type(ages2))
