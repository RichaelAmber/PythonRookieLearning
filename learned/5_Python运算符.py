# time 2023-11-28 00:11
# 算数运算符 + - * / %(取余或者求模) //(取整)

a = 12
b = 3
c = 7
print("加法运算：", a + b)
print("减法运算：", a - b)
print("乘法运算：", a * b)
print("除法运算：", a / b)
print("取余运算：", a % c)
print("取整运算：", a // c)

# 复合的赋值运算符 += -= *= /= %= //= **=
num = 13
num += 21  # 等价于num = num + 21
print("赋值运算符+=：", num)

num1 = 21
num1 %= 8  # 等价于num = num % 8
print("赋值运算符%=：", num1)

num2 = 3
num2 **= 2  # 等价于num = num ** 2
print("赋值运算符**=：", num2)

num3 = 54
num3 //= 7  # 等价于num = num // 7
print("赋值运算符//=：", num3)

# 注意⚠️：python中没有 ++ -- 运算

# 成员运算符：in 和 not in
# 主要用于判定指定元素是否在序列中，若在返回True，若不在返回False
list1 = [12, 34, 56, 89, 32, True]
print(34 in list1)
print(8.87 in list1)
print(93 not in list1)
print("h" in "hello")
print("w" not in "hello")

# 逻辑运算符 and(逻辑与)   or(逻辑或)    not(逻辑非)
print("逻辑与 and 测试：", 23 > 11 and 19 > 14)
print("逻辑或 or 测试：", 23 < 12 or 98 < 65)
print("逻辑非 not 测试：", not 23 > 12)

# 逻辑运算符的结果和短路运算
print(200 and 19)  # 19
print(False and 0)  # False
print(12 or False)  # 12
print(0 or 87)  # 87
'''
注意⚠️：
    对于and运算符，如果左边值为假，无论右边是什么结果都是假，此时直接返回左边值作为最终结果
如果左边值为真，那么最终结果是不确定的，and会继续计算右边值并返回右边值作为最终结果
    对于or运算符，如果左边值为真，那么右边值不用计算了，直接返回左边值作为最终结果
如果左边值为假，那么最终结果是不确定的，or会继续计算右边值并返回右边值作为最终结果
'''
# 三元运算符的写法 简化的if else写法
max1 = a if a > b else b
print(max1)
