# 1.遍历列表
list1 = ["Ariana Grande", 8964, 99.99, True, [1, 2, 3]]
# 遍历方式一：
for i in list1:
    print(i)
# 遍历方式二：
for index, value in enumerate(list1):
    print(index, value)

# 2.合并列表 通过+实现
list2 = [12, 445, 6, 4.53]
list3 = ["Miley Cyrus", "tylor swift", "SZA", "Doja Cat"]
print(list2 + list3)

# 3.判断元素是否在列表中 通过in 或 not in实现
print("SZA" in list3)

"""
4.列表添加元素
a.append() 向列表的尾部添加元素
a.extend() 可一次性添加多个元素，不改变原列表维度
           若追加一个元素，会将它做一次拆分
inset()  参数一：要追加的位置
         参数二：要追加的元素
若想一次追加多个元素，追加的元素以列表的形式追加
"""
list3.append("Sky")
print(list3)
list3.extend(list2)
print(list3)
list3.insert(0, "First Blood")
print(list3)

"""
5.列表删除元素
a.pop() 传入的参数是参数的下标,若不传参数，默认删除的是最后一个元素
a.remove() 传入的参数是要删除的元素
a.clear() 清空列表
"""
list3.pop(0)
print(list3)
list3.remove(12)
print(list3)
list3.clear()
print(list3)

"""
5.列表的排序
a.sort() 对原列表中的元素进行排序，默认是升序
sorted(list) 对列表元素进行排序，返回一个新列表
"""
list4 = [12, 34, 21, 35, 6, 24]
# 升序
list4.sort()
print(list4)
# 降序
list4.sort(reverse=True)
print(list4)

list5 = sorted(list4)
print(list5)
list5 = sorted(list4, reverse=True)
print(list5)
# 按列表元素的长度排序
list6 = ["abc", "hello", "e", "love", "mm"]
print(sorted(list6, key=len))

"""
6.翻转列表
reverse() 翻转列表元素
"""
list6.reverse()
print(list6)

"""
7.列表生成式
    range(start,end)
"""
# 原始人方式生成
list7 = []
for i in range(1, 11):
    list7.append(i ** 2)
print(list7)
# 列表生成式
list8 = [i ** 2 for i in range(1, 6)]
print(list8)
list9 = [i for i in range(1, 10) if i % 2 == 1]
print(list9)
