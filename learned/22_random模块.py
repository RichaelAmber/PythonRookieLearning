"""
random模块主要用于生成随机数或者从一个列表中随机获取数据
     random()   # 随机生成0-1之间的浮点数
     uniform(start,end) # 生成指定范围内的随机浮点数
     randint(start,end) # 生成指定范围内的随机整数
     randrange(start,end.step)  # 生成指定范围内的随机整数
     choice(str)    # 从指定内容中随机获取一个数据
     sample(str)    # 从指定内容中获取指定长度的数据
"""
import random
import random as rd

print(rd.randrange(10, 21, 5))

print(rd.choice("abcdefg"))
print(rd.choice(["Selena Gomez", "Ariana Grande", "Moon River"]))

print(rd.sample("Talking to the moon, try to get you", 4))
print(rd.sample(["Selena Gomez", "Ariana Grande", "Moon River"], 2))
