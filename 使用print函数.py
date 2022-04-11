#利用print函数进行输出-->单行注释
'''
print("90")
a = 100
b = 20
print(a)
print(a*b)
print('北京欢迎你')
print("北京欢迎你")
#不换行一次性输入多行数据：用,分割
print(a,b,"输出")
'''
#多行注释
'''
sadfwe
sadfds
wergew
'''
#标准化输出字符串
'''
变量可以是任意的类型
变量名必须是大小写英文，数字和下划线_组合，并且不能数字开头

标识符和关键字
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
#格式化输出
'''
age = 10;
print("我的年纪: %d岁"%age)
age += 1
print("我的年纪：%d岁"%age)
age += 1
print("我的年纪：%d岁"%age)
print("我的名字:%s，我的国籍:%s"%("张三", "中国"))
print("www","baidu","com",sep='.')
print("hello",end='\t')
print("hello",end='\n')
'''

#定义输出格式：
a = 1
b = 2
c = 3
print("输入{0}和{1}".format(a,b));
print("{:.3f}".format(3.1415926));
print("{:.0f}".format(3.1415926));
print("{:+.3f}".format(3.1415926));
print("{:+.3f}".format(-3.1415926));
#https://www.runoob.com/python/att-string-format.html -->format教程