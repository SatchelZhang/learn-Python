import turtle, time


# 绘制数码管间隔
def draw_gap():
    turtle.pu()
    turtle.fd(5)


# 绘制单段数码管
def draw_line(draw):
    draw_gap()
    turtle.pd() if draw else turtle.pu()
    turtle.fd(40)
    draw_gap()
    turtle.right(90)


# 根据数字绘制七段数码管
def draw_digit(digit):
    draw_line(True) if digit in [2, 3, 4, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 2, 3, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if digit in [2, 6, 8, 0] else draw_line(False)
    turtle.left(90)
    draw_line(True) if digit in [0, 4, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if digit in [2, 3, 0, 5, 6, 7, 8, 9] else draw_line(False)
    draw_line(True) if digit in [2, 3, 4, 0, 1, 7, 8, 9] else draw_line(False)
    turtle.left(180)
    turtle.pu()
    turtle.fd(20)


# 获得要输出的数字,data为日期，格式为‘%Y-%M=%D+'
def draw_date(date):
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('年', font=("Arial", 30, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月', font=("Arial", 30, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日', font=("Arial", 30, "normal"))
        else:
            draw_digit(eval(i))


def main():
    turtle.setup(800, 500, 300, 300)
    turtle.pu()
    turtle.bk(300)
    turtle.pensize(5)
    draw_date(time.strftime('%Y-%m=%d+', time.gmtime()))
    turtle.hideturtle()
    turtle.done()


main()
