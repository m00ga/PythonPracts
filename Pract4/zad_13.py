import random
import tkinter as tk
from functools import partial


class Pole:

    def __init__(self):

        self.__pole = [
            [],
            [],
            [],
            [],
        ]

        av = list(range(1, 16))
        rn1, rn2 = random.randint(0, 3), random.randint(0, 3)
        self.__pole[rn1].insert(rn2, None)

        for i in range(0, 4):
            for j in range(0, 4):
                try:
                    self.__pole[i][j]
                except IndexError:
                    rn = random.choice(av)
                    ind = av.index(rn)
                    self.__pole[i].append(av.pop(ind))

    @property
    def pole(self):
        return self.__pole

    def move(self, x1, y1, x2, y2) -> bool:
        try:
            if self.__pole[x2][y2] is not None:
                return False
            elif x2 - x1 != 0 and y2 - y1 != 0:
                return False
            else:
                self.__pole[x2][y2] = self.__pole[x1][y1]
                self.__pole[x1][y1] = None
                return True
        except IndexError:
            return False


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Пятнашки")
        self.resizable(0, 0)
        self.configure(bg="white")
        self.__pole = Pole()
        self.__picked = None
        self._draw()

    def _pickup(self, coords: tuple):
        if self.__picked is None:
            self.__picked = coords
            return
        elif self.__picked == coords:
            self.__picked = None
            return
        else:
            res = self.__pole.move(self.__picked[0], self.__picked[1], coords[0], coords[1])
            if res:
                self.__picked = None
            self._draw()

    def _draw(self):
        for i in range(0, 4):
            for j in range(0, 4):
                b = tk.Button(self,
                              text=self.__pole.pole[i][j],
                              height=4,
                              width=8,
                              borderwidth=1,
                              relief="solid",
                              activebackground="white",
                              command=partial(self._pickup, (i, j,))
                              )
                b.grid(row=i, column=j)


if __name__ == '__main__':
    app = App()
    app.mainloop()
