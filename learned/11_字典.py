# 字典的语法:{key:value,key1:value2......}
dict1 = {"name": "Selena Gomez", "age": 32, "height": 162, "sex": "female", "school": "MIT", "job": "singer"}

"""
1.获取字典中的元素
    通过索引方式：dict[key]
    通过get():dict.get(key)
"""
print(dict1["name"])
print(dict1.get("job"))

"""
2.删除字典中的元素
    pop()：dict.pop(key)
    popitem()：删除字典中最后一对key和value
    clear()：清空字典
"""
dict1.pop("name")
print(dict1)
dict1.popitem()
print(dict1)
# dict1.clear()
# print(dict1)

"""
3.获取字典中更多的元素
    获取字典的长度：len(dict)
    获取字典中所有的key：dict.keys()
    获取字典中所有的values：dict.values()
    获取字典中所有的key和value：dict.items()
"""
print(len(dict1))
print(dict1.keys())
print(dict1.items())

"""
4.遍历字典
    第一种方式： for in
    第二种方式：通过enumerate()函数
    第三种方式：通过dict.items()函数
"""
print("只遍历key==>")
for i in dict1:
    print(i)

print("只遍历value==>")
for v in dict1.values():
    print(v)

print("同时遍历key和value==>")
for k, v in enumerate(dict1):
    print(k, v)

print("同时遍历key和value 方式二==>")
for k, v in dict1.items():
    print(k, v)

"""
5.合并字典 dict1.update(dict2)
"""
dict2 = {'address': "Tokyo"}
dict1.update(dict2)
print(dict1)
