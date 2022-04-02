import turtle


def changecolor(color: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            tur: turtle.Turtle = args[0].turtle
            stan = tur.fillcolor()
            tur.fillcolor(color)
            ret = func(*args, **kwargs)
            tur.fillcolor(stan)
            return ret

        return wrapper

    return decorator


class Pract5:

    def __init__(self):
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.picked = None
        self.funcs = [v for (k, v) in self.__class__.__dict__.items() if "zad" in k]

    def draw(self):
        self.picked(self)
        self.screen.mainloop()

    def pickup(self, num: int):
        self.picked = self.funcs[num]

    # Задание 1

    @changecolor("green")
    def zad_1_1(self):
        self.turtle.begin_fill()
        for _ in range(5):
            self.turtle.forward(100)
            self.turtle.right(144)
        self.turtle.end_fill()

    @changecolor("blue")
    def zad_1_2(self):
        angle = 144
        size = 5

        self.turtle.begin_fill()
        for _ in range(5):
            self.turtle.forward(size)
            self.turtle.right(angle)
            self.turtle.forward(size)
            self.turtle.right(72 - angle)
        self.turtle.end_fill()

    @changecolor("gold")
    def zad_1_3(self):
        size = 10
        angle = 140

        self.turtle.pencolor("gold")
        self.screen.bgcolor("navy")

        self.turtle.setheading(-15)
        for i in range(8):
            self.turtle.begin_fill()
            for _ in range(5):
                self.turtle.forward(size)
                self.turtle.right(angle)
                self.turtle.forward(size)
                self.turtle.right(72 - angle)
            self.turtle.end_fill()

            self.turtle.left(45)
            self.turtle.penup()
            self.turtle.forward(size * 10)
            self.turtle.pendown()

    @changecolor("lawn green")
    def zad_1_4(self):
        self.turtle.pencolor("green4")
        self.turtle.pensize(3)
        self.turtle.left(17.4)
        self.turtle.speed(0)

        self.turtle.begin_fill()
        i = -1530
        while i <= 1530:
            i += 2.5
            self.turtle.forward(3)
            self.turtle.right(abs(i) + 91.22)
            if i == 0:
                self.turtle.right(160)

        self.turtle.end_fill()

    def zad_2_1(self):
        i = 20

        while i <= 200:
            self.turtle.forward(i)
            self.turtle.right(90)
            self.turtle.forward(i - 10)
            self.turtle.right(90)
            i += 10

    def zad_2_2(self):
        pass


# in the pickup() method, the count starts from 0, for example 0 - zad_1_1
if __name__ == '__main__':
    pract = Pract5()
    pract.pickup(4)
    pract.draw()
    exit(0)
