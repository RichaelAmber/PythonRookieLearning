"""
1.字符串的声明：
    一对单引号或者一对双引号或者一对3个单引号或者一对3个双引号
"""
a = "hello"
b = 'world'
c = '''Best Kept Secret'''
d = """明天会好吗"""
print(a, b, c, d)

# 2.字符串外面若是单引号里面必须是双引号，外面是双引号里面必须是单引号
n = "I say, 'My name is sebastian'";
print(n)
"""
3.转义字符： \ 让符号失去原有的意义
\'：表示转义单引号
\"：表示转义双引号
\n：表示换行
\t：表示制表符
"""
e = "Are \"you OK ?"
print(e)
f = "Welcome to \nAmerica!"
print(f)
g = "1\t2\t3\t4\t5"
print(g)

# 4.字符串前面加r，表示原样输出
h = "i am a \teacher"
print(h)
h1 = r"i am a \teacher"
print(h1)

# 5.字符串前面加f，支持{}语法
name = "张三"
age = 27
print("我的名字是：{name}，年龄是：{age}")
print(f"我的名字是：{name}，年龄是：{age}")

"""
字符串的下标：也叫索引，表示第几个数据
在计算机程序中，下标一般从0开始 可以通过下标获取指定位置的数据
"""
str1 = "Moore,Hey! What do you think the experience of today? Did do something wrong?"
print(str1[20])
"""
字符串的切片：从字符串中复制一段指定的内容，生成一个新的字符串
    语法：字符串[start:end:step]
        start表示开始下标 截取的字符串包含开始下标的数据
        end表示结束下标   截取的字符串不包含结束下标的数据
        step表示步长     默认值是1
"""
print(str1[0:10])
print(str1[11:])
print(str1[:5])
print(str1[1:10:2])
print(str1[::])  # 表示复制
# 翻转字符串
print(str1[::-1])
# 负数表示从右边开始数
print(str1[-10:-1])
# 步长为负数表示从右往左获取元素
print(str1[9::-1])
