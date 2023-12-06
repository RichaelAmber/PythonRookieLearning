# 赋值 本质上就是引用
print("测试赋值")
list1 = [i for i in range(1, 11) if i % 2 == 0]
list2 = list1
list1[0] = 999
print(list1)
print(list2)

# 为了解决上述问题，可用浅拷贝 copy()
import copy
print("测试浅拷贝")
list3 = [i for i in range(1, 11) if i % 2 == 1]
list4 = list3.copy()
list3[0] = 999
print(list3)
print(list4)

# 当对象是多维数组时，浅拷贝也会失效，这时要用到深拷贝
print("浅拷贝不可用")
list5 = [1, 2, 3, 4, 5, [101, 102, 103, 104], 7, 8, 9, 10]
list6 = list5.copy()
list5[5][0] = 999
print(list5)
print(list6)

# 深拷贝 copy.deepcopy(list)
print("测试深拷贝")
list7 = [1, 2, 3, 4, 5, [101, 102, 103, 104], 7, 8, 9, 10]
list8 = copy.deepcopy(list7)
list7[5][3] = 999
print(list7)
print(list8)


