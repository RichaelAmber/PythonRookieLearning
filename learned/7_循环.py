"""
1.初始条件
while 2.判断条件：
    循环体
    3.更新条件
注意⚠️：
    a.在while循环中，初始条件只会在第一次循环的时候执行，后续的循环会跳过
    b.在python中，不支持自增自减运算 ++ --
"""
num = 0
while num < 10:
    print("你爱我")
    num += 1
print("你不爱我")

"""
死循环：无法终止循环的循环条件
"""
while True:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "Moore" and password == "1234":
        print("恭喜你，账号密码正确，欢迎光临！！！")
        break
    else:
        print("账号密码错误，请重试")

"""
FOR语法：
    for 元素 in 可迭代对象
注意⚠️：
    1.python中的可迭代对象一般是指字符串｜列表｜元组｜集合等
    2.range是用来生成指定区间的整数数列 两个参数表示起点和终点
"""
# 输出1-10的所有数字
for i in range(1, 11):
    print(i)
# 使用for循环输出列表中的元素
for i in [12, 34, 5, 6, 86, 42]:
    print(i)
# 使用for循环遍历字符串
for i in "hello,欢迎来学习":
    print(i)

"""
break 和 continue 关键字
    break 是用来结束整个循环的
    continue 是跳出当前循环，开启下一轮循环
"""
# break举例：
#   当 num==3的时候，后续的num的值不输出
num = 0
while num < 5:
    if num == 3:
        num += 1
        break
    print(num)
    num += 1
# continue举例：
#   当 num==3的时候，不输出这个值，继续后面的输出
num = 0
while num < 5:
    if num == 3:
        num += 1
        continue
    print(num)
    num += 1
