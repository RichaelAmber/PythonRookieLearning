# input() 输入函数
'''
    1.参数是提示信息
    2.输入的内容使用变量接收
    3.input函数返回的是字符串类型
    4.input函数执行时，当输入完内容后，程序并没有执行完毕，一直处于等待状态，
只有当按下回车键时，才表示input()函数执行完毕，才会执行后续的代码
'''

age = input("Hi! Moore, how old are you?")
name = input("Could you tell me your real name?")
print(age, type(age))
print(name, type(name))
print("hello world")
