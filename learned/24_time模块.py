"""
time 模块主要用来操作时间，还可以操作程序
常用函数：
    time()  # 获取从1970年1月1日 0时0分0秒距今经历的秒数
    strftime("%Y-%m-%d %H:%M:%S")   # 按照格式显示日期时间 这个使用方式还需要深入
    sleep(seconds)
"""
import time

print(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S", (2023, 12, 6, 12, 22, 50, 0, 0, 0)))
