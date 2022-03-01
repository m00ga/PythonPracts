from math import inf, sqrt


# Задание 1

def zad_1():
    num = int(input())
    # 1)
    if num >= 0:
        print("Число додатне")
    else:
        print("Число від'ємне")
    # 2)
    if num > 0:
        print("Число додатне")
    elif num == 0:
        print("Дорівнює нулю")
    else:
        print("Число від'ємне")


# Задание 2

def zad_2():
    num = int(input())
    # 1)
    if num % 2 == 0:
        print("Число парне")
    # 2)
    if num % 2 != 0:
        print("Число непарне")
    # 3)
    if num % 3 == 0:
        print("Число кратне 3")
    # 4)
    if num % 5 != 0:
        print("Число некратне 5 ")
    # 5)
    if num % 2 == 0 and num % 7 == 0:
        print("Число парне i кратне 7")
    # 6)
    if num % 2 != 0 or num % 7 != 0:
        print("Число непарне або некратне 7")


def zad_2_7():
    num = int(input())
    a = int(input())
    b = int(input())
    if a <= num <= b:
        print("Належить")


def zad_2_8():
    num = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    if a < num < b and c <= num < inf:
        print("Належить")


def zad_2_9():
    x = int(input())
    a = int(input())
    # with abs
    if abs(x) < a:
        print("good")
    # without abs
    ab_v = x * -1 if x <= 0 else x
    if ab_v < a:
        print("good")


def zad_2_10():
    x = int(input())
    a = int(input())
    # with abs
    if abs(x) > a:
        print("good")
    # without abs
    ab_v = x * -1 if x <= 0 else x
    if ab_v > a:
        print("good")


# Задание 3

def zad_3():
    x = int(input())
    y = x + 5
    # 1)
    if y >= 0:
        print(f"sqrt(x+5) = {sqrt(y)}")
    # 2)
    if (a := x - 7) != 0:
        print(f"1/x-7 = {1 / a}")
    # 3)
    if (y >= 0) and sqrt(y) != 0:
        print(f"1/sqrt(x+5) = {1 / sqrt(y)}")
    # 4)
    if (a := abs(y)) != 0:
        print(f"1/abs(x+5) = {1 / a}")
    # 5)
    if (a := x ** 7) != 0:
        print(f"1/x^7 = {1 / a}")
    # 6)
    if (y >= 0) and (x - 7 >= 0):
        a, b = sqrt(x + 5), sqrt(x - 7)
        print(f"sqrt(x + 5) + sqrt(x - 7) = {a + b}")
    # 7)
    if y >= 0 and x - 7 != 0:
        print(f"sqrt(x+5) + 1/x-7 = {sqrt(y) + 1 / (x - 7)}")
    # 8)
    if y >= 0 and (a := sqrt(y)) != 0 and x - 7 != 0:
        print(f"1/sqrt(x+5) + 1/x-7 = {1 / a + 1 / (x - 7)}")


# Задание 4


def zad_4():
    x = int(input())
    x_2 = x ** 2
    # 1)
    print(x if x > 0 else x_2)
    # 2)
    print(x if -10 < x < 5 else x_2)
    # 3)
    print(x if (1 <= x <= 5 and 10 <= x < inf) else x_2)
    # 4)
    if x <= 0:
        print(x)
    elif 0 < x <= 5:
        print(x_2)
    else:
        print(25)


# Задание 5


def zad_5():
    a = int(input())
    b = int(input())

    # a)
    if a > b:
        print(b, a)
    else:
        print(a, b)
    # б)
    if a > b:
        print(a, b)
    else:
        print(b, a)


# Задание 6


def zad_6():
    a = int(input())
    b = int(input())
    c = int(input())
    m = a

    if b > m:
        m = b
    if c > m:
        m = c

    print(m)


# Задание 7


def zad_7():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())

    if ((x1, y1) > (0, 0) and (x2, y2) > (0, 0)) or ((x1, y1) < (0, 0) and (x2, y2) < (0, 0)):
        print("YES")
    else:
        print("NO")


# Задание 8


def zad_8():
    d = int(input())
    m = int(input())
    y = int(input())

    if m == 12 and d == 31:
        y += 1
        m = 1
        d = 1
    elif (m == 2 and d == 28) or (m == 8 and d == 31):
        m += 1
        d = 1
    elif (m % 2 == 0 and d == 30) or (m % 2 != 0 and d == 31):
        d = 1
        m += 1
    else:
        d += 1

    print(d, m, y, sep="\n")


if __name__ == "__main__":
    exit(0)
