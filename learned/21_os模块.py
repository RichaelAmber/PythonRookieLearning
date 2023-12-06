import os

"""
os模块主要用于获取系统的功能，操作文件或者文件夹
常见函数：
    os.curdir   表示当前目录
    os.getcwd()    获取当前路径
    os.mkdir()     创建文件夹（不能创建已经存在的文件）
    os.rmdir()     删除文件夹（只能删除空文件夹）
    os.rename(file1, file2) 重命名文件或文件夹
    os.path.join(path1, path2)  拼接路径
    os.path.getsize()   获取文件大小
    os.path.isfile()    判断是否是文件
    os.path.isdir()     判断是否是文件夹
"""
print(os.curdir)  # . 表示当前目录

# getcwd() 获取当前路径
print(os.getcwd())

# mkdir() 创建文件夹（不能创建已经存在的文件）
# os.mkdir("测试")

# 路径拼接
print(os.path.join(os.getcwd(), "测试.py"))

# 获取文件大小
print(os.path.getsize("20_math模块.py"))
