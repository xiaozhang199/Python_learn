#Python语句分为简单语句和复合语句
#函数是可以重复调用的代码块
#函数可以有return返回值
#无返回值的情况：
'''
def sayhelllo():
    print("hello")
    print("it's so early")
sayhelllo()
'''
'''
hello
it's so early
'''
#有返回值的情况
'''
def ans(a, b):
    res = a * b
    return res
total = ans(4,5)
print(total)#20
'''
#自定义函数：type(),len()等
#模块函数：通过import语句，直接导入模块
'''
from math import sin
print(sin(2))
'''
#等效于：
'''
import math
print(math.sin(2))
'''

#类和对象
#创建类对象：
'''
class Person:#定义类
    def sayhello(self):#定义类的函数
        print("hello")
p = Person()#创建对象
p.sayhello()#调用对象的方法
'''

#模块和包
#.py文件就是模块
#多个模块可组建为包

#周五小球游戏作业
#Pygame Zero教程


