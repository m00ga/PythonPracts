import random
import tkinter as tk
from functools import partial


class Pole:

    def __init__(self):

        self.__pole = [[None] * 4 for _ in range(4)]
        av = list(range(1, 17))

        for i in range(0, 4):
            for j in range(0, 4):
                rn = random.choice(av)
                ind = av.index(rn)
                p = av.pop(ind)
                self.__pole[i][j] = p if p != 16 else None

    @property
    def pole(self):
        return self.__pole

    def get(self, coords: tuple):
        return self.__pole[coords[0]][coords[1]] if coords is not None else None

    def set(self, coords: tuple, value: int):
        self.__pole[coords[0]][coords[1]] = value

    def move(self, old_coords: tuple, new_coords: tuple) -> bool:
        try:
            old = self.get(old_coords)
            new = self.get(new_coords)
            if new is not None:
                return False
            elif new_coords[0] - old_coords[0] != 0 and new_coords[1] - old_coords[1] != 0:
                return False
            else:
                self.set(new_coords, old)
                self.set(old_coords, None)
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

    def _high(self, but: tk.Button):
        if not but.tag:
            but.configure(fg="gray")
            but.tag = True
        else:
            but.configure(fg="black")
            but.tag = False

    def _pickup(self, coords: tuple, but: tk.Button):
        if self.__picked is None:
            self.__picked = coords
            self._high(but)
            return
        elif self.__picked == coords:
            self.__picked = None
            self._high(but)
            return
        else:
            res = self.__pole.move(self.__picked, coords)
            if res:
                self.__picked = None
                self._high(but)
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
                              )
                b.configure(command=partial(self._pickup, coords=(i, j), but=b))
                b.tag = False
                b.grid(row=i, column=j)


if __name__ == '__main__':
    app = App()
    app.mainloop()