import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)


def main():
    turtle.setup(800, 600)
    turtle.pu()
    turtle.goto(-200, 100)
    turtle.pd()
    turtle.pencolor('blue')
    turtle.pensize(2)
    n = 3
    koch(400, n)
    turtle.right(120)
    koch(400, n)
    turtle.right(120)
    koch(400, n)
    turtle.hideturtle()
    turtle.done()


main()
