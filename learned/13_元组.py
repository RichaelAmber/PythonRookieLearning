"""
元组和列表
    相同点：本质上也是一种有序集合
    不同点： 1.元组() 列表[]
            2.元组中的元素不能修改
"""

# 1.创建元组
tup = (12, 34, 6, 7, True, "hello")
print(type(tup), tup)

# 若元组中的元素只有一个，需要在元素后面加上一个逗号
tup1 = (32,)
print(tup1)

# 2.可通过下标访问元组中的元素
print(tup[1], tup[-1])

# 3.元组元素不能修改
# tup[2] = 100
# print(tup)

# 4.合并元组 通过 +
tup2 = (223, 45, 9, 10)
print(tup1 + tup2)

# 5.判断元素是否在元组中，使用成员运算符 in或者not in
print(45 in tup2)
print(45 not in tup2)

# 6.其他类型转换为元组
list1 = [234, 54, 6, 7]
print(type(list1))
print(type(tuple(list1)))

# 7.遍历元组 还是 for in 和 enumerate()
for i in tup:
    print(i)

for k, v in enumerate(tup):
    print(k, v)
