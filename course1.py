#Python中一切皆是对象，变量名和对象直接绑定-->动态类型语言
'''
print(id(123))
a = 123#字面量表达式创建值为123的int型实例对象，并绑定到变量a-->值一般放在堆中，而变量一般在栈中，栈中变量指向堆中对象，变量引用对象
print(id(a))
1542051991600
1542051991600#值一样，数据是一个对象
'''

'''
#Python中的对象内存示意图：
#Python程序运行时，在内存中会创建各种对象（位于堆内存中），通过赋值语句，将对象绑定到变量（位于栈内存中），通过变量引用对象，进行各种操作
#多个变量可以引用同一个对象
#如果一个对象不再被任何有效作用域中的变量引用，则会通过自动垃圾回收机制，回收该对象占用的内存
i = 100#创建一个值为100的int对象，并绑定到变量i
i = i + 1#先计算表达式i + 1的值，然后创建一个值为101的int对象，并绑定到变量i
'''

'''
#对象的值比较（==）和引用判断（is）
a = "abc"
b = "abc"
c = "abcd"
print(a == b)#True-->判断两个变量指向的对象的值是否相同
print(a is b)#True-->判断两个变量是否指向同一对象
print(a == c)#False
print(a is c)#False
a = 25.0
b = 25
print(a == b)#True
print(a is b)#False
a = [1,2,3]
b = [1,2,3]
print(a == b)#True
print(a is b)#False
a = False
b = 0
print(a == b)#True
print(a is b)#False
'''

'''
#对象的可变性取决于其数据类型的设计，即是否允许改变其值
#不可变对象-->不可变对象一旦创建，其值就不能修改，例如：int, str, complex等
#可变对象--> 例如：list
x = y =[1,2,3]
x.append(4)
print(id(x))
print(id(y))
print(y)#[1,2,3,4]
z = [1,2,3,4]
print(x == z)#True
print(x is z)#False
'''
#命名规则
#模块/包名：全小写字母，简单有意义，如果需要可以使用下划线：math、sys
#函数名：全小写，可以使用下划线增加可读性
#变量名：全小写，可以使用下划线增加可读性
#类名：即多个单词组成名称，每个单词除了第一个字母大写外，其余的字母小写
#常量名：全大写字母，可以使用下划线增加可读性

#变量和赋值语句-->允许链式赋值
#系列解包赋值
'''
_,share,elem,_ = ['a',12,324,-1]
print(share,elem)#12,324
'''

#print(3**4)#81

'''
def do_nothing():
    pass#空语句
'''

'''
import turtle#默认朝右走

turtle.circle(100)#画圆
turtle.speed(100)#速度
turtle.color("red")#颜色

for i in range(50) :
    turtle.left(91)
    turtle.circle(100)
'''


'''
import turtle
#注意画笔的粗细需要改变
#注意画笔的位置需要移动-->默认坐标：0，0
turtle.speed(10)
turtle.pensize(8)#改变画笔粗细
turtle.circle(80)
turtle.penup()#抬笔
turtle.goto(-200,0)#goto(新坐标位置)
turtle.color("blue")
turtle.pendown()#落笔
turtle.circle(80)
turtle.penup()#抬笔
turtle.goto(200,0)#goto(新坐标位置)
turtle.color("red")
turtle.pendown()#落笔
turtle.circle(80)

turtle.penup()#抬笔
turtle.goto(100,-100)#goto(新坐标位置)
turtle.color("green")
turtle.pendown()#落笔
turtle.circle(80)

turtle.penup()#抬笔
turtle.goto(-100,-100)#goto(新坐标位置)
turtle.color("yellow")
turtle.pendown()#落笔
turtle.circle(80)

turtle.color("black")
turtle.penup()
turtle.goto(-100,180)
turtle.pendown()
turtle.write("北京 2022",font = ("kaiti", 43))
'''

#绘制美国队长的盾牌
'''
import turtle
turtle.pensize(10)
turtle.color("red")
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()

turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()

turtle.color("white")
turtle.penup()
turtle.goto(0,-150)
turtle.pendown()

turtle.begin_fill()
turtle.circle(150)
turtle.end_fill()

turtle.color("red")
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()

turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.color("blue")
turtle.penup()
turtle.goto(0,-50)
turtle.pendown()

turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.penup()
turtle.goto(-40,10)
turtle.pendown()

turtle.color("white")
turtle.begin_fill()

for i in range(5):
    turtle.forward(80)
    turtle.right(144)

turtle.end_fill()
turtle.hideturtle()
'''

'''
import turtle
turtle.color("red")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
turtle.color("black")
turtle.right(90)
turtle.forward(50)
'''

#随机数RGB red green blue
#彩旗飘飘
'''
import turtle
import random
turtle.speed(40)
turtle.colormode(255)
for i in range(20):
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)

    turtle.color(red,green,blue)

    x = random.randint(-300,300)
    y = random.randint(-100,200)

    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    turtle.color("black")
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
'''
#繁星漫天
import turtle
import random
turtle.colormode(255)
turtle.bgcolor("black")
turtle.pensize(100)
turtle.speed(50)
k = 20
h = 200
for i in range (7):
    turtle.color(k,k,k)
    turtle.penup()
    turtle.goto(-400,h)
    turtle.pendown()
    turtle.forward(1000)
    k += 20
    h -= 100
#画星星
for i in range(50):
    x = random.randint(-300,300)
    y = random.randint(0,300)
    size = random.randint(5,20)
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    turtle.color(red,green,blue)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pensize(3)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.left(30)
        turtle.forward(size)
        turtle.right(120)
    turtle.end_fill()
    turtle.left(20)



