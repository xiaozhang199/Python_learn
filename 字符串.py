#字符串、列表、元组、字典

#字符串-->单引号、双引号、三引号
#python源代码默认UTF-8编码，默认unicode字符串
'''
word = '字符串'
sentence = "这是一个句子"
paragrath = """
这是一个段落
可以多行组成
 """
print(word)
print(sentence)
print(paragrath)
'''

'''
my_str = "it's good"
print(my_str)
my_str = 'it\'s good'#-->可能引发转义错误的时候要加斜杆
print(my_str)
print("hello","world",sep="\v")//纵向制表符
'''

'''

'''
# str = "chengdu"
# print(str)
# print(str[0:3])#che [起始位置：结束位置：步进值]
# print(str[0:7:2])#cegu
# print(str[4:])#gdu
# print(str[:4])#chen
#
# print(str + ", hello")#chengdu, hello-->字符串连接使用+
# print(str * 3)#字符串重复操作，使用*号
# print("hello\t,world")#hello	,world
# print(r"hello\t,world")#hello\t,world-->在字符串前加r后，转义字符失效

s = "asgfwer";
print(s.upper());#ASGFWER :s中的所有字符转换为大写，但是s不变
print(s);#asgfwer

s1 = "fas";
s2 = "qwr";
print(id(s1));
s1 += s2;
print(id(s1));
print()