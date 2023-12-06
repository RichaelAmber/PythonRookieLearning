# 需求：给如下的函数添加功能，在函数中，多输出一句话：“我很好”
def test():
    print("你好吗？")


test()

print("开始实现====>")


# 第一种实现方式   对原函数进行覆盖
# def test():
#     print("你好吗？")
#     print("我很好")
#
#
# test()


# 第二种实现方式   函数嵌套
# def demo():
#     test()
#     print("我很好")
#
#
# demo()

# 第三种实现方式   闭包函数

def outer(fn):
    def inner():
        fn()
        print("我很好")  # 给原函数添加功能

    return inner


func = outer(test)
func()
"""
此处的outer就是一个装饰器函数
    fn表示形参，实际调用装饰器函数，传入的实际是原函数的名字
"""
print("简写形式开始实现====>")


# 装饰器的简写方式 @ + 装饰器的名称
# 原函数必须在@的下面

@outer  # 等价于 test = outer(test)
# 原函数
def test():
    print("你好吗？")


test()

"""
⚠️注意：
    1.在使用装饰器简写方式时，原函数必须在装饰器函数下面
    2.outer函数就是装饰器函数 @outer ===> test = outer(test)
"""


# 一个装饰器装饰多个函数

def outer1(fn):
    def inner(*args):
        print("数学运算的结果是：")
        fn(*args)

    return inner


@outer1
def add(a, b):
    print(a + b)


@outer1
def subtract(a, b):
    print(a - b)


@outer1
def multiply(a, b):
    print(a * b)


@outer1
def divide(a, b):
    print(a / b)


add(11, 22)
subtract(100, 25)
multiply(20, 7)
divide(17, 3)

"""
一个函数有多个装饰器函数修饰
"""


def outer2(fn):
    def inner(*args):
        fn(*args)
        print("想要唱给谁听！")

    return inner


def outer3(fn):
    def inner(*args):
        fn(*args)
        print("不唱给任何人听！")

    return inner


@outer2
@outer3
def say(*args):
    for name in args:
        print("唱歌给%s听，你能听到我的心声吗？" % name)


say("Selena Gomez", "Ariana Grande")

