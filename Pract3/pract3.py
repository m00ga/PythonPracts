from math import cos

donkey = """
           _\\       
            /`b  
       /####J   
       |\\ ||
"""

elephant = """
          _ __ _
         / |..| \\
         \/ || \/
          |_''_|
"""

universal = """
          ------------
         <      {}    >
          -----\\/-----
               /
            {anim}
"""

sec_pattern = """ 
          {prob}_ __ _
         {}/ |..| \\
         {}\/ || \/
          {}|_''_|
"""

menu = """
 _____ _            _                 _   _____                   _            
|  ___| |          | |               | | /  __ \                 | |           
| |__ | | ___ _ __ | |__   __ _ _ __ | |_| /  \/ ___  _   _ _ __ | |_ ___ _ __ 
|  __|| |/ _ \ '_ \| '_ \ / _` | '_ \| __| |    / _ \| | | | '_ \| __/ _ \ '__|
| |___| |  __/ |_) | | | | (_| | | | | |_| \__/\ (_) | |_| | | | | ||  __/ |   
\____/|_|\___| .__/|_| |_|\__,_|_| |_|\__|\____/\___/ \__,_|_| |_|\__\___|_|   
             | |                                               All-Products Edition                
             |_| 
             
-------------------------------= Головне меню =--------------------------------

1. ElephantCounter v1.0
2. ElephantCounter v2.0
3. ElephantCounter v3.0 Starter Edition
4. ElephantCounter v3.0 Premium Deluxe Edition
5. ElephantCounter v4.0 Premium Deluxe Edition
6. ElephantCounter v5.0 Ultimate International Premium Deluxe Edition

0. Вихід

-------------------------------= Головне меню =--------------------------------                                                                    
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
    n = int(input("До скількох рахувати: "))
    for i in range(1, n + 1):
        print(i)


# Задание 13

# Premium Deluxe Edition
def zad_13(animal=elephant):
    n = int(input("Скільки хочете бачити: "))
    for i in range(1, n + 1):
        print(universal.format(i, anim=animal))


# Задание 14

# Elephant Counter v.3.0 Starter Edition
def zad_14():
    pass


# Задание 15

# Elephant Counter v.4.0 Premium Deluxe Edition
def zad_15():
    n = int(input("Скільки слоників ви хочете побачити: "))
    print(sec_pattern.format("/" * n, "\\" * n, "|" * n, prob=" " * n))


# Задание 16

# Elephant Counter v.5.0 Ultimate International Premium Deluxe Edition
def zad_16():
    animals = [elephant, donkey]

    while True:
        choice = int(input("Виберіть тварину: \n 1 - Слоник \t 2 - Віслюк \n > "))
        if choice == 1 or choice == 2:
            break
        else:
            print("Неправильний вибір!\n")
            continue
    animal = animals[choice - 1]

    zad_13(animal)


# Задание 17

def zad_17():
    funcs = [zad_11, zad_12, zad_14, zad_13, zad_15, zad_16]

    while True:
        print(menu)
        choice = int(input("Виберіть бажану функцію: "))
        if choice == 0:
            break
        try:
            funcs[choice - 1]()
        except IndexError:
            print("Такої функції немає!")

    print("Дякуемо за користування")


# Задание 18

def zad_18():
    result = [
        [],
        [],
        []
    ]

    for i in range(10, 100):
        a = i // 10
        b = i % 10

        if i == (a ** 2 + b ** 2):
            result[0].append(i)

    for i in range(100, 1000):
        a = i // 100
        b = i % 100 // 10
        c = i % 10

        if i == (a ** 3 + b ** 3 + c ** 3):
            result[1].append(i)

    for i in range(1000, 10000):
        a = i // 1000
        b = i % 1000 // 100
        c = i % 100 // 10
        d = i % 10

        if i == (a ** 4 + b ** 4 + c ** 4 + d ** 4):
            result[2].append(i)

    print(f"n = 2\n{result[0]}\nn = 3\n{result[1]}\nn = 4\n{result[2]}")


# Задание 19

def zad_19():
    pass


if __name__ == '__main__':
    exit(0)
