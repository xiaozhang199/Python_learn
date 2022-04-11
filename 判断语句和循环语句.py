'''
if 0:
    print("true")#缩进必须有-->同一层次必须相同缩进
else:
    print("false")
print("end")
'''

'''
score = int(input("请输入该同学的考试成绩:"))
if score >= 90:
    print("本次考试成绩为A")
elif score >= 70 and score < 90:
    print("本次考试成绩为B")
elif score >= 60 and score < 70:
    print("本次考试成绩为C")
elif score >= 0 and score < 60:
    print("本次考试成绩为D")
else:
    print("数据为无效数据！")
'''

'''
xingbie = 1
danshen = 1
if(xingbie == 1):
    print("男生")
    if danshen == 1:
        print("介绍对象")
else:
    print("女生")
    
'''

'''
import  random #引入随即库
x = random.randint(0,2)#随机生成[0,2]之间的随机数-->整数
print(x)
print(type(x))#int
'''
#循环语句
'''
注意可迭代对象：
系列：例如字符串，列表，元组
字典
文件对象
迭代器对象
生成器函数
'''

'''
for i in range(5):
    print(i)
'''
'''
for i in range(0,11,3):
    print(i)
'''

'''
for i in range(-10,-100,-30):
    print(i)
'''
'''
name = "chengdu"
for x in name:
    print(x,end='\t')#c	h	e	n	g	d	u	
'''
'''
a = ["aa","bb","cc","dd"]
for i in range(len(a)):
    print(i,a[i])
'''

'''
i = 0
while i < 5:
    print("当前是第%d次循环"%(i+1))
    i += 1
'''
'''
3.
i = 1
res = 0
temp = 1
while i < 11:
    temp *= i
    res += temp
    i += 1
print(res)
'''
'''
count = 0
while count < 5:
    print(count)
    count += 1
print(count + 100)
'''

'''
#break-->结束整个循环;continue-->结束本次语句;pass-->占位符
i = 0
while i < 10:
    i += 1
    print("-"*30)
    if(i == 5):
        continue
    print(i)
'''

'''
season = [10,20,30,40]
for i,s in enumerate(season,start=1):
    print("{0}he{1}".format(i,s))
'''
'''
x = [1,2,3]
y = [4,5,6]
print(list(zip(x,y))#[(1, 4), (2, 5), (3, 6)]
'''


evens = [0,2,4]
odd = [1,3,5]
for e,o in zip(evens,odd):
    print("{0},{1},{2}".format(e,o,e*o))


