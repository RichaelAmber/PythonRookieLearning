"""
模块：一个py文件就可以简单的理解为是一个模块
    但是py文件要像模块一样导入使用，必须遵循命名规则
    常见的内置模块：os sys re math random datetime time
    calendar hashlib uuid hmac等模块
模块导入方式：
    1.直接使用import关键字倒入模块
    2.from 模块名 import 方法名或者变量名
    3.from 模块名 import * 表示导入该模块下面所有的方法和变量名
    4.import 模块名 as 别名
    5.from 模块名 import 方法名或者变量名 as 别名
"""
# 方法一
import time

print(time.time())

# 方法二
from random import randint

print(randint(1, 9))

# 方法四
import datetime as dt
print(dt.MAXYEAR)

# 方法五
from copy import deepcopy as dp

