from math import cos

pattern = """
         ------------
        <      {}    >
         -----\\/-----
              /
      _______   
    /  |. .|  \\
    \\/ |   | \\/
     | .   . |
      -     -  
    """


# Задание 5

def zad_5():
    start = -100
    end = 100
    step = 5.5
    while end > start:
        print(f"x = {start} \t cos(2x+5) = {cos((2 * start) + 5)}")
        start += step


# Задание 6

def zad_6():
    n = int(input())
    sum = 0
    for i in range(1, n + 1):
        sum += i

    print(f"Сумма всех чисел до {n}: {sum}")


# Задание 7

def zad_7():
    n = int(input())
    s = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            s += i

    print(f"Сумма всех парних чисел до {n}: {s}")


# Задание 8

def zad_8():
    n = int(input())
    fac = 1
    for i in range(1, n + 1):
        fac = fac * i

    print(f"Факторіал всіх чисел: {fac}")


# Задание 9

def zad_9():
    n = int(input())
    d = 1
    for i in range(1, n + 1):
        if i > 0:
            d *= i

    print(f"Добуток всіх чисел: {d}")


# Задание 10

def zad_10():
    temp = 0.0
    for i in range(1, 8):
        temp += float(input(f"Среднедобова температура за {i} день: "))

    print(f"Середньотижнева температура: {temp / 7}")


# Задание 11

def zad_11():
    for i in range(1, 11):
        print(i)


# Задание 12

def zad_12():
    n = int(input())
    for i in range(1, n + 1):
        print(i)


# Задание 13

# Premium Deluxe Edition
def zad_13():
    n = int(input())
    for i in range(1, n + 1):
        print(pattern.format(i))


# Задание 14

# Elephant Counter v.3.0 Starter Edition
def zad_14():
    pass


if __name__ == '__main__':
    zad_13()
    exit(0)
