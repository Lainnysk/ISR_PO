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
