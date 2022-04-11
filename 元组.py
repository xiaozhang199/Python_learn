#Tuple-->Tuple的元素不能修改，但可以包含可变对象，元组写在小括号内，用逗号分开
'''
tup1 = () #创建空的元组
tup2 = (50)#元组中如果只有一个元素，必须加逗号-->error
print(type(tup2))#<class 'int'>
tup3 = (50,)
print(type(tup3))#<class 'tuple'>
tup4 = (1,2,3)
print(type(tup4))#<class 'tuple'>
'''

'''
tup1 = ('abc','def',10,20)
print(tup1[1])#def
print(tup1[-1])#20
print(tup1[0:6])#('abc', 'def', 10, 20)-->从0开始，后面6个数，[)区间，如果大于元组元素数，直接显示后面的全部
'''

#增
'''
tup2 = (12,34,56)
tup3 = ('abc','def')
tup = tup2 + tup3
print(tup)#(12, 34, 56, 'abc', 'def')-->并不是在某一个元组上增加了，而是新建了一个元组
'''

#改
'''
tup3 = (12,34,56)
tup3[0] = 1000#直接报错，不支持修改
'''

#删
'''
tup1 = (12,34,56)
print(tup1)
del  tup1 #直接删除了整个元组变量，没有tup1了，并不是删除里面的元素
'''

#查
tup1 = ('abc','def',10,20)
print(tup1[1])#def
print(tup1[-1])#20
