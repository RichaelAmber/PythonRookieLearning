# python中的集合和数学中的集合比较类似
# 特点：无序，无重复元素的集合

# 1.创建集合
set1 = {12, 34, 5, 67, True}
print(type(set1), set1)

# 2.集合中的元素不能通过下标访问或者修改
# print(set1[1])

# 3.获取集合的长度
print(len(set1))

# 4.一次添加一个元素 add()
set1.add(98)
set1.add(57)
print(set1)

# 5.一次添加多个数据 update()
set1.update([76, 2, 3])
print(set1)

"""
6.删除随机元素 pop() 测试发现似乎就是删除第一个元素
  删除指定元素 remove() 若元素不存在就报错
  删除指定元素 discard() 若元素不存在也不报错
  清空集合    clear()
"""
set1.pop()
print(set1)

set1.remove(98)
print(set1)

set1.discard(100)
print(set1)

# 7.遍历集合
for i in set1:
    print(i)