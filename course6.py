# import sys
# print("hello" + sys.argv[0])
# a = dir(__builtins__)
# print(a)

# a,b = 1,2
# a,b = b,a
# print(a,b)

# print(list(map(lambda x,y:x+y,'abc','de')))

# first = [1,2,3]
# second = [4,5,6]
# total = list(zip(first,second))
# print(total) #[(1, 4), (2, 5), (3, 6)]

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--length',default=10,type=int,help='长度')
# parser.add_argument('--width',default=5,type=int,help='宽度')
# args = parser.parse_args()
# areas = args.length * args.width
# print(areas)

# import datetime
# birthyear = int(input("请输入你的出生年份"))
# age = datetime.date.today().year - birthyear
# print(age)

#文件操作
import sys
filename = sys.argv[0]
line_no = 0
with open(filename,'r',encoding='utf8') as f: #安全操作写法
    for line in f:
        line_no += 1
        print(line_no,":",line)