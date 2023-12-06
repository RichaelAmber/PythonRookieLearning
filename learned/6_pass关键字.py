# pass关键字在python中没有任何意义，只是单纯的实现占位，保证语句的完整性
age = int(input("请输入您的年龄："))

if age >= 18:
    print("欢迎光临鼠哥娱乐会所")
else:
    pass
# 使用pass进行占位，没有意义，仅仅是为了保证语句完整性，使程序不报错
print("hello world")
