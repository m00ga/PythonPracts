import turtle


def changecolor(color: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            tur: turtle.Turtle = args[0]
            stan = tur.fillcolor()
            tur.fillcolor(color)
            ret = func(*args, **kwargs)
            tur.fillcolor(stan)
            return ret

        return wrapper

    return decorator


# Задание 1

@changecolor("green")
def zad_1_1(tur: turtle.Turtle):
    tur.begin_fill()
    for _ in range(5):
        tur.forward(100)
        tur.right(72)
    tur.end_fill()


@changecolor("blue")
def zad_1_2(tur: turtle.Turtle, size: int):
    angle = 144

    tur.begin_fill()
    for _ in range(5):
        tur.forward(size)
        tur.right(angle)
        tur.forward(size)
        tur.right(72 - angle)
    tur.end_fill()


@changecolor("gold")
def zad_1_3(tur: turtle.Turtle, scr: turtle.TurtleScreen):
    size = 10
    angle = 140

    tur.pencolor("gold")
    scr.bgcolor("navy")

    tur.setheading(-15)
    for i in range(8):
        tur.begin_fill()
        for _ in range(5):
            tur.forward(size)
            tur.right(angle)
            tur.forward(size)
            tur.right(72 - angle)
        tur.end_fill()

        tur.left(45)
        tur.penup()
        tur.forward(size * 10)
        tur.pendown()


if __name__ == '__main__':
    s = turtle.Screen()
    t = turtle.Turtle()

    s.mainloop()
    exit(0)
