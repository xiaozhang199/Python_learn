#列表中元素的类型可以不相同
#列表索引值以0为开始值，-1为结束值
'''
namelist = []#定义一个空列表
namelist = ["小章","小王","小李"]
print(namelist[0])#小章
testlist = [1, "测试"]
print(type(testlist[0]))
print(type(testlist[1]))
for i in range(len(namelist)):
    print(namelist[i])
#等价于
for name in namelist:
    print(name)
'''
#增删改查
#增加：append
'''
namelist = ["小章","小王","小李"]
for name in namelist:
    print(name)
nametemp = input("请输入追加学生的姓名：")
namelist.append(nametemp)
for name in namelist:
    print(name)
'''
#extend
'''
a = [1,3]
b = [2,4]
a.append(b)#-->将列表b看作列表a的元素-->可以看作列表的嵌套
print(a)

a.extend(b)#将b的每个元素逐一追加到a中
print(a)
'''

#insert-->指定下标位置，插入元素
'''
a = [0,1,2]
a.insert(1,3) #第一个表示下标，第二个表示对象，将元素3插入下标为1的位置
print(a)
'''

#删：del -->del list[i]
'''
namelist = ["小章","小王","小李"]
for name in namelist:
    print(name)
del namelist[0] #在指定下标删除一个元素
for name in namelist:
    print(name)
'''
#pop():弹出末尾最后一个元素
'''
a = [1,2,3]
a.pop()
print(a)
'''
#remove -->直接删除指定元素-->如果元素重复，删除第一个出现的元素
'''
a = [1,2,3,2]
a.remove(2)
print(a)#[1,3,2]
'''
#改：-->直接按下标修改
'''
namelist = ["小章","小王","小李"]
for name in namelist:
    print(name)
namelist[1] = "直接"
for name in namelist:
    print(name)
'''

#查：in, not in
'''
namelist = ["小章","小王","小李"]
for name in namelist:
    print(name)
findname = input("请输入你要查找的学生姓名：")
if findname not in namelist:
    print("没有找到")
else:
    print("找到")
'''
#index-->可以查找指定下标范围的元素,并返回对应元素的下标-->范围区间左闭右开[) -->如果没有找到，就会报错

'''
a = ['a','b','c','d']
print(a.index('b',1,3))#1-->在下标1到3的范围内查找有没有'b'元素；[)-->返回下标
'''


#count-->计数元素出现过几次
'''
a = ['a','b','c','b']
print(a.count('b'));
'''
#排序和反转
'''
#reverse-->反转
a = [1,2,3,4]
print(a)
a.reverse()
print(a)
#sort-->从小到大排序
a.sort()
print(a)
#降序
a.sort(reverse=True)
print(a)
'''
#嵌套
'''
schoolnames = [[],[],[]] #有三个元素的空列表-->每个元素都是一个空列表
schoolnames = [["北京大学","清华大学"],["南开大学","天津师范大学"],["山东大学"]]#嵌套的列表中列表元素数目可以不一致
'''

'''
import  random
offices = [[],[],[]]
teachername = ["1","2","3","4","5","6","7","8"]
for teacher in teachername:
    index = random.randint(0,2)
    offices[index].append(teacher)
print(offices)

i = 1
for office in offices:
    print("办公室%d及其人数：%d"%(i,len(office)))
    i += 1
    for name in office:
        print("%s"%name,end="\t")
    print("\n")
    print("-"*20)
'''


#作业：
# products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",399]]
# print("-"*6,"商品列表","-"*6)
# i = 0
# for i in range(len(products)):
#     print(i,end="\t")
#     for detail in products[i]:
#         print(detail,end='\t')
#     print("")
#
# shopCart = []
# flag = True
# sum = 0
# while(flag):
#     index = input("请输入你要购买的商品编号：")
#     if (index == "q"):
#         flag = False
#         for i in range(len(shopCart)):
#             for detail in shopCart[i]:
#                 print(detail,end="\t")
#             print("")
#         print("您购买的商品总价为：%d"%sum)
#     else:
#         shopCart.append(products[int(index)])
#         sum += products[int(index)][1]

# first,*middles,last = sorted([1,531,66,7,2,16,17]);
# print(first);
# print(middles);
# print(last);
# 1
# [2, 7, 16, 17, 66]
# 531

shop = []
