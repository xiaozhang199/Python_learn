#int 类型
# print(int('FF',16));#255
# print(int('100',4));#16

# import sys
# a = int(sys.argv[1]);
# b = int(sys.argv[2]);
# print(a + b);

#浮点数转换成分数
# print(1.25.as_integer_ratio());#(5,4)

#complex类型
# read:实部
# imag：虚部
# conjugate：共轭复数
# a = 1+2j;
# print(type(a));
# print(a.real);
# print(a.imag);
# print(a.conjugate());
# b = complex(5,2);
# print(b);
# print(a + b);
# <class 'complex'>
# 1.0
# 2.0
# (1-2j)
# (5+2j)
# (6+4j)

#bool型相关计算：
#短路计算
#Python任意表达式都可以评价为布尔逻辑值
# not True#false
# not False#True

#str:16位Unicode编码
print(ord('A')); #65 #将字符转换为Unicode编码
print(chr(65));#A #把十进制数转换为对应的字符
print(ord('张'));#24352
