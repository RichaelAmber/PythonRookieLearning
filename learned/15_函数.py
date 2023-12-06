"""
一、函数的语法：
    def 函数名(参数1，参数2，参数3...):
        函数体
    1.使用def关键字声明函数
    2.函数由两部分组成：声明部分和实现部分
    3.函数名要遵循标识符的命名规则，尽量做到见名知意
    4.函数定义时的参数，叫做形参，可写可不写，取决于功能需求
    5.函数体要缩进
    6.函数要想使用必须调用
    7.函数调用必须在函数定义之后
"""


def test(n):
    print("接下来即将输入1-%d的数组，长度为%d" % (n, n))
    for i in range(1, n + 1):
        print(i)


test(10)
test(20)

"""
二、函数调用的注意事项：
    1.在同一个文件中，同名函数后面的会覆盖前面的
    2.若将函数名赋值给一个变量，那可通过该变量调用函数
    3.函数必须先定义，再调用
    4.一个项目中函数可多次调用
"""

"""
三、实参和形参：
    定义函数时传递的参数叫做形式参数
    调用函数时传递的参数叫做实际参数，调用的时候实参会替换形参
"""

"""
四、函数的参数类型
    a.必须参数  在调用时，必须顺序正确，参数数量保持一致
    b.关键字参数 使用关键字参数时，可自动匹配，允许实参和形参顺序不一致
    c.默认参数
"""


def student(name="Amber Shin", age=28):
    print("我的名字是%s,年纪%d，想哭，想笑，想变成天上那朵忽明忽暗的云" % (name, age))


student("田中", 28)
student(age=29, name="Moore")
student()

"""
五、函数的参数高级篇：不定长参数
    1. *args：用来接收多个位置参数，得到的是一个元组
        若有多个参数，*args一般在最后一个
    2. **kwargs:用来接收多个关键字参数，得到的时一个字典
        在传输参数时必须是key=value的形式
"""


def demo(*args):
    for i in range(0, len(args)):
        print(args[i])


demo("hello", 12, 34, 5, 65)
demo(1, 2, 3, 4, 5, 6)


def fn(**kwargs):
    for k, v in enumerate(kwargs):
        print(k, v)


fn(x=1, y=2, z=5)
fn(drink="coffee", location="the raining mountain", time="night")


