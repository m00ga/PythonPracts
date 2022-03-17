# Задание 1
import math


def zad_1():
    num = int(input())

    if num < 37:
        if num % 2 == 0:
            print("Ваше место в купе, верхняя койка")
        else:
            print("Ваше место в купе, нижняя койка")
    elif num >= 37:
        if num % 2 == 0:
            print("Ваше место боковое, верхняя койка")
        else:
            print("Ваше место боковое, нижняя койка")


# Задание 2


def zad_2():
    d = int(input())


# Задание 3

def zad_3():
    s = float(input("Площа зали: "))
    r = float(input("Радіус: "))
    k = float(input("Прохід: "))

    side = math.sqrt(s)
    s_r = side / 2
    r = r - k

    if s_r <= r:
        print("good")
    else:
        print("bad")


if __name__ == '__main__':
    exit(0)
