from math import sqrt
# from time import time
import random


# Задание 1

def zad_1():
    pass


# Задание 2

def zad_2(a, b, c):
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Площа трикутника: {s}")


# Задание 3

def zad_3(a):
    pass


# Задание 4

def zad_4():
    pass


# Задание 5

def zad_5(n):
    if n == 0:
        return 1
    else:
        return n * zad_5(n - 1)


# Задание 6

# без рекурсии
def zad_6_1(k):
    f1 = 1
    f2 = 1
    for _ in range(2, k):
        f1, f2 = f2, f1 + f2

    print(f2)


# с рекурсией
def zad_6_2(k):
    if k == 0:
        return 0
    if k == 1:
        return 1

    return zad_6_2(k - 1) + zad_6_2(k - 2)


# Задание 7

def zad_7(n):
    s = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            s += zad_5(i)

    print(s)


# Задание 8

def zad_8(n):
    if n == 0:
        return 0

    return n % 10 + zad_8(n // 10)


# Задание 9

def zad_9(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False

    return True


# Задание 10

def zad_10(n):
    print([x for x in range(2, n+1) if zad_9(x)])


# Задание 11

# уже при n > 100000 лучше чем zad_10
# Решето Ератосфена
def zad_11(n):
    # all_nums = [x for x in range(2, n + 1)]
    # for j in all_nums:
    #     for n, i in enumerate(all_nums):
    #         if i == j:
    #             continue
    #         elif i % j == 0:
    #             all_nums.pop(n)
    # print(all_nums)

    numbers = [x for x in range(2, n + 1)]
    for num in numbers:
        if num != 0:
            for candidate in range(2 * num, n + 1, num):
                numbers[candidate - 2] = 0
    print([x for x in numbers if x != 0])


# Задание 12

def zad_12():
    pass


# Задание 13
# TODO: make working game, but later

# Пятнашки
def zad_13():
    pole = [
        [],
        [],
        [],
        [],
    ]

    for i in range(0, 4):
        for _ in range(0, 4):
            pole[i].append(random.randint(1, 15))

    print(pole)


if __name__ == '__main__':
    exit(0)
