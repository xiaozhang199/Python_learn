#dict 无序的对象集合，使用键值对存储，具有极快的查找速度
#key必须使用不可变类型，且在同一个字典中，键值唯一
#字典定义
#info = {"name":"张三","age":19}

'''
#字典访问
print(info["name"])#张三
#访问了不存在的键
#print(info["gender"])#KeyError-->程序报错
print(info.get("gender"))#None-->通过get不报错，没有找到对应的键，返回None
print(info.get("gerder","m"))#没找到，设定默认值m,找到了就显示原值
'''

#增
'''
info = {"name":"张三","age":19}
newID = input("请输入新的学号:")
info["id"] = newID
print(info)#{'name': '张三', 'age': 19, 'id': '23'}
'''

#删
#del
# info = {"name":"张三","age":19}
# print(info)#{'name': '张三', 'age': 19}
# del  info["name"]#删除指定键值对
# print(info)#{'age': 19}
# info = {"name":"张三","age":19}
# del info#删除字典后再访问报错，将字典变量从整个内存中删除

#clear
# info = {"name":"张三","age":19}
# print(info)
# info.clear()
# print(info)#{}

#修改-->直接通过键值修改
# info = {"name":"张三","age":19}
# info["age"] = 20
# print(info)#{'name': '张三', 'age': 20}

#查
# info = {'name': '张三', 'age': 20}
# print(info.keys())#dict_keys(['name', 'age'])
# print(info.values())#dict_values(['张三', 20])
# print(info.items())#dict_items([('name', '张三'), ('age', 20)]) 所有的项

#遍历
'''
info = {'name': '张三', 'age': 20}
#遍历键
for key in info.keys():
    print(key)
#遍历值
for value in info.values():
    print(value)
#遍历所有
for key,value in info.items():
    print("key = {0},value = {1}".format(key,value))
for item in info.items():
    print(item)
# key = name,value = 张三
# key = age,value = 20
# ('name', '张三')
# ('age', 20)
'''
#for循环扩展-->使用枚举函数，同时拿到列表中的下标和元素内容
# mylist = ['a','b','c']
# print(enumerate(mylist))#<enumerate object at 0x000001A8CBE58480>
# for i,x in enumerate(mylist):
#     print(i,x)
# 0 a
# 1 b
# 2 c

