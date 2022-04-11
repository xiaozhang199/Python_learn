# f = open("123.txt",'r')#FileNotFoundError: [Errno 2] No such file or directory: '123.txt'
# f.close()

#捕获异常
#以下过程不会报错
# try:
#     f = open("123.txt",'r')
# except IOError:#如果捕获到的异常属于IOError
#     pass#捕获异常后执行的代码

# try:
#     print(num)#NameError: name 'num' is not defined. Did you mean: 'sum'?
# except IOError:#如果捕获到的异常属于IOError
#     print("产生错误了")#异常不统一


#异常类型捕获需要一致：
# try:
#     print(num)
# except NameError:#如果捕获到的异常属于NameError
#     print("产生错误了")
# 产生错误了

# try:
#     print(1)
#     f = open("123.txt",'r')
#     print(2)
#     print(num)
#     print(3)
# except (NameError,IOError):#-->到第一个错误的地方跳到此处，不再运行后面的代码
#     print("产生错误了")
# 1
# 产生错误了

#获取错误描述：
# try:
#     print(1)
#     f = open("123.txt",'r')
#     print(2)
#     print(num)
#     print(3)
# except (NameError,IOError) as result:
#     print("产生错误了")
#     print(result)
# #[Errno 2] No such file or directory: '123.txt'

#捕获所有的异常：
# try:
#     print(1)
#     f = open("123.txt",'r')
#     print(2)
#     print(num)
#     print(3)
# except Exception as result:
#     print("产生错误了")
#     print(result)
# [Errno 2] No such file or directory: '123.txt'

#try ... finally 和嵌套

# import time
# try:
#     f = open("text.txt",'r')
#     try:
#         while True:
#             content = f.readline()
#             if len(content) == 0:
#                 break
#             time.sleep(2)
#             print(content)
#     finally:
#         f.close()
# except Exception as result:
#     print(result)
# finally:#无论是否有异常，finally后面的内容都必须执行
#     print("文件关闭")

#课后作业
# f = open("gushi.txt",'w')
# f.write("""唤起一天明月
# 照我满怀冰雪
# 浩荡百川流
# """)
# f.close()
# try:
#     another = open("gushi.txt",'r')
#     temp = open("copy.txt",'w')
#     try:
#       try:
#         while True:
#             content = another.readline()
#             if len(content) == 0:
#                 break
#             temp.write(content)
#       except:
#             pass;
#       finally:
#           another.close()
#           temp.close()
# except Exception as result:
#     print(result)
# finally:
#     print("关闭文件")


def r(wenjian):
    f = open(wenjian,'r')
    content = str(f.readlines())
    f.close()
    return content

def w(wenjian,content):
    f = open(wenjian,'w')
    f.write(content)
    f.close()

try:
    content = """唤起一天明月
照我满怀冰雪
浩荡百川流
"""
    w("gushi.txt",content)
    temp = r("gushi.txt")
    w("copy.txt",temp)
except Exception as result:
    print(result)
finally:
    print("任务结束!")



