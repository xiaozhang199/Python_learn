#文件打开，关闭，修改，删除
# f = open("text.txt","w")#默认当前相同路径下，w:写模式，文件若不存在就创建了一个文件 r:只读模式，默认情况
# f.write("hello")
# f.close()#关闭文件

# read方法，读取指定的字符，开始时定位在头部，每执行一次，向后移动指定字符数
# f = open("text.txt","r")
# content  =f.read(3)#读前3个字符
# print(content)#hel
# content  =f.read(3)
# print(content)#lo
# f.close()

# f = open("text.txt","r")
# content = f.readlines()#全部读取#得到的是一个列表
# for temp in content:
#     print(temp)#分别输出每一行
# f.close()

# f = open("text.txt","r")
# content = f.readline()#读取一行
# print(content)
# f.close()

#文件相关操作 引入库os
import os
os.rename("test.txt","anothername.txt")