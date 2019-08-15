"""
使用海龟绘图画小猪佩奇
"""

import turtle as T

def nose(x,y):
    """画鼻子"""
    T.penup()
    # 将海龟移动到指定的坐标
    T.goto(x,y)
    T.pendown()
    # 设置海龟的方向（0-东、90-北、180-西、270-南）
    T.setheading(-30)
    # 画鼻头并上色
    T.begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            # 向左转3度
            T.left(3)
            # 向前走
            T.forward(a)
        else:
            a = a - 0.08
            T.left(3)
            T.forward(a)
    T.end_fill()
    # 移动画笔
    T.penup()
    T.setheading(90)
    T.forward(25)
    T.setheading(0)
    T.forward(10)
    T.pendown()
    # 设置新的画笔颜色（RGB）
    T.pencolor(255, 155, 192)
    T.setheading(10)
    T.begin_fill()
    T.circle(5)
    T.color(160, 82, 45)
    T.end_fill()
    T.penup()
    T.setheading(0)
    T.forward(20)
    T.pendown()
    T.pencolor(255, 155, 192)
    T.setheading(10)
    T.begin_fill()
    T.circle(5)
    T.color(160, 82, 45)
    T.end_fill()


def head(x,y):
    """画头"""
    T.color((255, 155, 192), "pink")
    T.penup()
    T.goto(x, y)
    T.setheading(0)
    T.pendown()
    T.begin_fill()
    T.setheading(180)
    T.circle(300, -30)
    T.circle(100, -60)
    T.circle(80, -100)
    T.circle(150, -20)
    T.circle(60, -95)
    T.setheading(161)
    T.circle(-300, 15)
    T.penup()
    T.goto(-100, 100)
    T.pendown()
    T.setheading(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            T.lt(3)  # 向左转3度
            T.fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            T.lt(3)
            T.fd(a)
    T.end_fill()


def ears(x,y):
    """画耳朵"""
    T.color((255, 155, 192), "pink")
    T.penup()
    T.goto(x, y)
    T.pendown()
    T.begin_fill()
    T.setheading(100)
    T.circle(-50, 50)
    T.circle(-10, 120)
    T.circle(-50, 54)
    T.end_fill()
    T.penup()
    T.setheading(90)
    T.forward(-12)
    T.setheading(0)
    T.forward(30)
    T.pendown()
    T.begin_fill()
    T.setheading(100)
    T.circle(-50, 50)
    T.circle(-10, 120)
    T.circle(-50, 56)
    T.end_fill()


def eyes(x,y):
    """画眼睛"""
    T.color((255, 155, 192), "white")
    T.penup()
    T.setheading(90)
    T.forward(-20)
    T.setheading(0)
    T.forward(-95)
    T.pendown()
    T.begin_fill()
    T.circle(15)
    T.end_fill()
    T.color("black")
    T.penup()
    T.setheading(90)
    T.forward(12)
    T.setheading(0)
    T.forward(-3)
    T.pendown()
    T.begin_fill()
    T.circle(3)
    T.end_fill()
    T.color((255, 155, 192), "white")
    T.penup()
    T.seth(90)
    T.forward(-25)
    T.seth(0)
    T.forward(40)
    T.pendown()
    T.begin_fill()
    T.circle(15)
    T.end_fill()
    T.color("black")
    T.penup()
    T.setheading(90)
    T.forward(12)
    T.setheading(0)
    T.forward(-3)
    T.pendown()
    T.begin_fill()
    T.circle(3)
    T.end_fill()


def cheek(x,y):
    """画脸颊"""
    T.color((255, 155, 192))
    T.penup()
    T.goto(x,y)
    T.pendown()
    T.setheading(0)
    T.begin_fill()
    T.circle(30)
    T.end_fill()


def mouth(x,y):
    """画嘴巴"""
    T.color(239, 69, 19)
    T.penup()
    T.goto(x, y)
    T.pendown()
    T.setheading(-80)
    T.circle(30, 40)
    T.circle(40, 80)


def setting():
    """设置参数"""
    T.pensize(4)
    # 隐藏海龟
    T.hideturtle()
    T.colormode(255)
    T.color((255, 155, 192), "pink")
    T.setup(840, 500)
    T.speed(10)


def main():
    """主函数"""
    setting() # 绘图前先设置参数
    # 将图形分成几个部分，每个部分提供作画起点即可
    # 图形参数可下载网络图像在画图软件中确定
    # 先完成主函数结构框架，再完善每个模块细节
    nose(-100, 100)
    head(-69, 167)
    ears(0, 160)
    eyes(0, 140)
    cheek(80, 10)
    mouth(-20, 30)
    T.done() # 绘图结束

if __name__ == '__main__':
    # 调用主函数
    main()