"""
一、关于函数的返回值
1.有返回值的函数：
    需要return关键字返回
    return后面的代码不回执行
    return关键字一次性返回多个数据，多个数据用逗号隔开，结果以元组的形式返回
2.无返回值的函数
    函数中若没有return或没有数据返回，则默认返回是None
"""


def fn1():
    return 1, 2, 3


print(fn1())

"""
二、函数之间的嵌套
"""


def test():
    test1()
    print("Number 1: 顾城")


def test1():
    test2()
    print("Number 2：席慕容")


def test2():
    test3()
    print("Number 3：海子")


def test3():
    print("Number 4：泰戈尔")


test()

"""
三、匿名函数
    是一个表达式，比普通函数简单，使用lambada定义的表达式
    lambada表达式中包含了参数、实现体、返回值
"""


# 常规函数
def fn(num):
    return num ** 2


print(fn(3))
# lambada函数
num1 = lambda num: num ** 2
print(num1(5))

"""
四、回调函数
    把一个函数(a)作为一个参数传递到另一个函数(b)中去
"""


def add(a, b):
    print(a + b)


def subtract(a, b):
    print(a - b)


def multiply(a, b):
    print(a * b)


def divide(a, b):
    print(a / b)


# 需求：封装一个万能函数，传入两个参数，直接实现加减乘除
def demo(x, y, func):
    func(x, y)


# 测试
demo(1, 2, add)
demo(5, 1, subtract)
demo(2, 9, multiply)
demo(7, 4, divide)

"""
五、闭包函数（主要用于装饰器函数的实现）
    如果一个函数里嵌套了另一个函数，外部的叫外部函数，内部的叫内函数
    如果一个外部函数中定义了一个内部函数，并且外部函数的返回值是内部函数，就构成了一个闭包
"""


# 最简单的闭包函数
def outer():
    def inner():
        print("我是闭包函数！")

    return inner


fn = outer()  # fn ===> inner函数
fn()  # 感觉这个闭包函数有些无聊


# 闭包示例2
def outer1(x, *args):
    y = 100

    def inner1():
        print(x + y, args)

    return inner1


func1 = outer1(10, 1, 2, 3, 4)
func1()
# ⚠️注意：
# 闭包函数的内函数不能有形参
# 闭包函数调用前要先赋值
