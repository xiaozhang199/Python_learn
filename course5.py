#元素下标的访问可以从前往后，也可以从后往前
# -4 -3 -2 -1 -->从后往前
# [1 2 3 4 5]
#  0 1 2 3 4 -->从前往后
# numlist = [1,2,3,4]
# print(numlist[-1])

# first,*middle,last = range(10) # *的位置不限
# print(middle) #[1, 2, 3, 4, 5, 6, 7, 8]
# print(type(middle)) #list
# *first,last3,last2,last1 = range(10) #[0, 1, 2, 3, 4, 5, 6]
# print(first)
# print(type(first))

#创建元组试例
# a = 1,2,3,4,5
# b = 1, #只有一个元素时，必须记得逗号
# c = 'a','b','c'
# print(a)
# print(b)
# print(c)
# d = tuple("abc")
# print(d) #('a', 'b', 'c')
# e = tuple([1,2,3])
# print(e) #(1, 2, 3)
# print(a[2:3]) #[2,3)之间的元素切片


#列表：单个元素等于空，元素直接变为空，切片等于空，切片直接被清除
# a = [0,1,2,3,4]
# a[2] = []
# print(a) #[0, 1, [], 3, 4]
# a[2:3] = []
# print(a) #[0, 1, 3, 4]
# del a[:] #将a清空为空列表
# print(a) #[]
# del a #删除列表a，a不再存在

# s = [1,4,3,2]
# res = sorted(s) #不改变s的值，将排序后的数组存在res中
# print(s)#[1, 4, 3, 2]
# s.sort()
# print(s)#[1, 2, 3, 4]

# a = {1,2,3,4,1}
# print(type(a)) #<class 'set'>
# b = {x ** 3 for x in[1,1,2,3]}
# print(b) #{8, 1, 27}
# c = {i for i in range(10)}
# print(c) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(type(b)) #<class 'set'>
# print(type(c)) #<class 'set'>
# item_one = 'avd'
# item_two = 'rgb'
# item_three = 'num' #str类型不允许改变
# total = item_one +\
#         item_two +\
#         item_three
# print(total) #avdrgbnum

