import math
import time
import os

clear = lambda: os.system('cls')
Perimeter = lambda a, b, c: 4 * (a + b + c)
Square = lambda a, b, c: 2 * (a*b + a*c + b*c)

def n1():
    try:
        clear()
        print("\tКалькулятор")
        num1, num2 = (float(input("Введите число: ")) for i in range(2))
        ch = int(input('''(0) Ввести числа заново
(1) Сложение
(2) Вычитание
(3) Умножение
(4) Деление
(5) Целочисленное деление
(6) Остаток от деления
(7) Возведение в степень
(8) !int! Логарифм числа по основанию
(9) !int! Наибольший общий делитель 
(10) !int! Число сочетаний
(11) !int! Число размещений
(12) Расчет площади и периметра параллелепипеда
Выбор операции: '''))
        match ch:
            case 0:
                n1()
            case 1:
                print(f"\n{num1} + {num2} = {num1 + num2}\n")
            case 2:
                print(f"\n{num1} - {num2} = {num1 - num2}\n")
            case 3:
                print(f"\n{num1} * {num2} = {num1 * num2}\n")
            case 4:
                print(f"\n{num1} / {num2} = {num1 / num2}\n") 
            case 5:
                print(f"\n{num1} // {num2} = {num1 // num2}\n") 
            case 6:
                print(f"\n{num1} % {num2} = {num1 % num2}\n") 
            case 7:
                print(f"\n{num1} ^ {num2} = {num1 ** num2}\n")
            case 8:
                print(f"\n{num1}log({num2}) = {math.log(num1, num2)}\n")
            case 9:
                print(f"\nНаибольший общий делитель {int(num1)} и {int(num2)}: {math.gcd(num1, num2)}\n")
            case 10:
                print(f"\nЧисло сочетаний из {int(num1)} по {int(num2)}: {math.comb(int(num1), int(num2))}\n")
            case 11:
                print(f"\nЧисло размещений из {int(num1)} по {int(num2)}: {math.perm(int(num1), int(num2))}\n")
            case 12:
                num3 = float(input("Введите третий параметр - длину ребра: "))
                print(f"\nПериметр параллелепипеда с ребрами {num1}, {num2} и {num3} = {Perimeter(num1, num2, num3)}")
                print(f"Площадь поверхности параллелепипеда с ребрами {num1}, {num2} и {num3} = {Square(num1, num2, num3)}\n")
            case _:
                print("\nВведено неверное значение операции.")
                time.sleep(2)
                n1()
    except Exception :
        print("Некорректный ввод.")
        time.sleep(2)
        clear()
        n1()

def n2():
    try:
        clear()
        print("\tСчётчик")
        str = input("Введите строку: ")
        Spaces = str.count(" ")
        Coms = str.count(",")
        Chars = len(str) - (Spaces + Coms)
        print(f"\nКоличество символов в строке: {Chars}\nКоличество пробелов: {Spaces}\nКоличество запятых: {Coms}\n")
    except Exception:
        print("Некорректный ввод.")
        time.sleep(2)
        clear()
        n2()

def n3():
    try:
        clear()
        print("\tМатрица")
        matrix = []
        Column = int(input("Введите кол-во столбцов: "))
        Line = int(input("Введите кол-во строк: "))
        StartValue = int(input("Введите начальное значение: "))
        Step = int(input("Введите значение увеличения: "))
        for i in range(Line):
            matrix.append([])
            for j in range(Column):
                matrix[i].append(StartValue)
                StartValue += Step
        print()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], end = ' ')
            print()
        print()
    except Exception:
        print("\nНекорректный ввод.")
        time.sleep(2)
        clear()
        n3()

def main():
    while True:
        try: 
            choice = int(input("Введите номер функции: "))
            match choice:
                case 0:
                    break
                case 1:
                    n1()
                case 2:
                    n2()
                case 3:
                    n3()
                case _:
                    print("\nВведи значение 0-3!")
                    time.sleep(2)
                    clear()
                    main()
        except Exception:
            print("\nНекорректный ввод.")
            time.sleep(2)
            clear()
            main()

if __name__ == "__main__":
    main()