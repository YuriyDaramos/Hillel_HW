AVAIL_MATH_OPER = ["+", "-", "*", "/"]    # Доступные математические операторы

n1 = None               # Число №1
n2 = None               # Число №2
math_oper = None        # Математический оператор

while True:
    print("Введите первое число")
    n1 = input()
    print("Введите второе число")
    n2 = input()
    try:
        n1 = float(n1)
        n2 = float(n2)
    except ValueError:
        print("Ошибка ввода, попробуйте снова")
        continue
    print("Введите математическй оператор из списка: +, -, *, /")
    math_oper = input()
    if math_oper not in AVAIL_MATH_OPER:
        print("Введен недопустимый оператор")
        continue
    else:
        if math_oper == "+":
            print("Результат операции: ", n1 + n2)
        elif math_oper == "-":
            print("Результат операции: ", n1 - n2)
        elif math_oper == "*":
            print("Результат операции: ", n1 * n2)
        elif math_oper == "/":
            try:
                print("Результат операции: ", n1 / n2)
            except ZeroDivisionError:
                print("Ошибка деления на ноль")
        break