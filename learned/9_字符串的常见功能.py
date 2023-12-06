# 1.获取字符串的长度和统计字符串出现的次数
str1 = "我的电脑有点卡了，你的电脑卡吗？"

# len() 统计字符串的长度
print(len(str1))
# count() 在整个字符串中统计子串出现的次数
print(str1.count("电脑"))

"""
2.大小写转换
    upper() 将小写字母全部转换为大写字母
    lower() 将大写字母全部转换为小写字母
    swapcase() 将字符串中的大写字母转换为小写，将小写转换为大写
    title() 将单词的每个首字母转换为大写
"""
str2 = 'i Miss You. I am So sCARed!'
print(str2.upper())
print(str2.lower())
print(str2.swapcase())
print(str2.title())

"""
3.查找字符串位置
    查找子串在字符串中第一次出现的位置
        find() 找到返回下标，没找到返回-1
        index() 功能和find()相似，没找到则直接报错
    查找子串在字符串中最后一次出现的位置
        rfind() 找到返回下标，没找到返回-1
        rindex() 功能和rfind()相似，没找到则直接报错
    在指定范围内查找
        find(substring,start,end)
        index(substring,start,end)
"""
str3 = "abcdqiohrfiqbhkcsbdjf"
print(str3.find('f'))
# print(str3.index('w'))
print(str3.rfind('j'))
print(str3.find('a', 2, 5))

"""
3.字符串的提取、分割与合并
    strip()     去除字符串两边的指定字符,默认去除的是空格
    lstrip()    只去除左边
    rstrip()    只去除右边
字符串的分割和合并
    split() 以指定字符对字符串进行分割（默认是空格）
    join()  合并字符串
"""
str1 = " I might, I might kill ex. I still love him though "
str2 = "+++--**&& I might, I might kill ex. I still love him though &&**--+++"
print(str1.strip())  # 默认去空格
print(str2.strip("+").strip("&"))  # 只会去除最外层的字符,有一定的局限性

# 分割
for arr in str1.split("i"):
    print(arr)
# 合并
str3 = '_'
tuple1 = ("I", "Love", "You")
print(str3.join(tuple1))
list1 = ["The", "City", "Is", "Raining"]
print(str3.join(list1))

"""
4.字符串的替换和判断
    替换：replace()    第一个参数要替换的内容，
    第二个参数替换后的内容,第三个参数表示替换次数
    判断：返回结果是布尔类型，True Or False
    isupper() 检测字符串中的字母是否全部是大写
    islower() 检测字符串中的字母是否全部是小写
    isdigit() 检测字符串中的字母是否全部是数字
    isTitle() 检测字符串中的首字母是否全部是大写
    isalpha() 检测字符串中的内容是否全部是由字母或者文字组成
"""
str4 = "Fuck you Man! Go Fuck yourself! Get the Fuck out!"
print(str4.replace("Fuck", "**", 2))

"""
5.字符串的编码和解码
    encode() 编码
    decode() 解码
    ASCII码的转换 
        chr() 将对应的ASCII值转换为对应的字符
        ord() 获取字符对应的ASCII值
"""
str5 = "我爱你"
print(str5.encode('utf-8'))
print(str5.encode('gbk'))

str6 = b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0'
str7 = b'\xce\xd2\xb0\xae\xc4\xe3'
print(str6.decode())
print(str7.decode("gbk"))

# ASCII码的转换
print(chr(97))
print(chr(65))
print(ord("c"))

"""
6.通过%占位符的方式实现字符串的格式化输出
    %   占位符
    %d  表示整数
    %f  表示小数
    %s  表示字符串
    %.2f    表示保留两位小数，保留的位数可自己控制
"""
name = "Moore"
age = 29
salary = 250000.34
print("我的名字是%s, 年龄是%d, 年收入是%.2f" % (name, age, salary))
