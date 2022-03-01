# Задание 1

def zad1():
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



if __name__ == '__main__':
    zad1()
    exit(0)
