#对齐方式：<>^-->左对齐，右对齐和居中对齐
#print("{0:<10}和{1:^4}和{2:>7}".format("asdf","as","sdfq"))

'''
while True:
    s = input("输入q终止")
    if s.upper() == 'Q':
        break
    print(s)
'''
#小球碰撞
import pgzrun
import random
WIDTH = 800
HEIGHT = 600
r = 20
y = HEIGHT/2
x = WIDTH/2
y_speed = 5
x_speed = 2
def draw():
    screen.fill('white')
    screen.draw.filled_circle((x,y),r,'red')
    screen.draw.filled_circle((x + 80, y + 40), r, 'yellow')
    screen.draw.filled_circle((x + 120, y + 60), r, 'black')

def update():
    global y,y_speed,x,x_speed
    y += y_speed
    x += x_speed
    if y >= HEIGHT - r or y <= r:
        y_speed = -y_speed
    if x <= r or x >= WIDTH - r:
        x_speed = -x_speed

pgzrun.go()