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
