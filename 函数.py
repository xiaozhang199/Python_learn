# def 函数名():
#     代码

# #函数的定义
# def printinfo():
#     print("----------")
#     print("嘤嘤嘤嘤嘤嘤嘤")
#     print("----------")
#
# #函数的调用
# printinfo()

# #带参数和返回值的
# def addNum(a,b):
#     c = a + b
#     return c
#
# print(addNum(10,33))

# #返回多个值的函数
# def divid(a,b):
#     ans = a // b
#     mod = a % b
#     return ans,mod
#
# ans1,ans2 = divid(10,3) #需要使用多个值来保存返回内容
# print(ans1,ans2)

# def ave(a,b,c):
#     res = (a+b+c) / 3
#     return res
#
# print(ave(10,24,8))

#全局变量和局部变量
# #局部变量是函数内部的变量，不同的函数可以有相同的局部变量
# def test1():
#     a = 300
#     print(a)
#
# def test2():
#     a = 500
#
# test1()
# test2()
# test1()

# a = 100#全局变量
# def test1():
#     a = 300
#     print(a)#输出的是局部变量-->变量名相同，优先使用局部变量
#
# def test2():
#     a = 500
#
# test1()
# test2()
# test1()
# 100
# 100

#想在函数中修改局部变量
# a = 100
# def test01():
#     global  a
#     a = 200
#     print(a)
#
# def test02():
#     print(a)
#
# test01()
# test02()
# 200
# 200