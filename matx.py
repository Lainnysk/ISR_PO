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