"""
datetime模块主要用来显示日期时间，其中的date类用来显示日期，time类用来显示时间
常用函数：
    date(2023,12,6) # 创建一个日期
    time(11,21,25)  # 创建一个时间
    datetime.now()  # 获取当前的日期时间
    datetime.now() +datetime.timedelta(5)   # 获取5天后的时间
"""

import datetime as dt
print(dt.datetime.now() + dt.timedelta(5))
