AVAILABLE_MATH_OPERATORS = ["+", "-", "*", "/"]    # Доступные математические операторы

# Наглядная демонстрация возникающих сложностей со вложенными циклами
while True:         # Главный цикл

    print("Введите первое число:")
    try:
        num_1 = float(input())
    except ValueError:
        print("Ошибка ввода, попробуйте снова")
        continue

    while True:     # Ввод второго числа, повтор цикла при ошибке
        print("Введите второе число:")
        try:
            num_2 = float(input())
        except ValueError:
            print("Ошибка ввода, попробуйте снова")
            continue
        break

    while True:     # Перебор математических операторов
        print("Введите математический оператор из списка: +, -, *, /")
        math_operator = input()
        if math_operator not in AVAILABLE_MATH_OPERATORS:
            print("Введен недопустимый оператор")
            continue
        elif math_operator == "+":
            print(f"Результат операции {num_1} {math_operator} {num_2} = {num_1 + num_2}")
        elif math_operator == "-":
            print(f"Результат операции {num_1} {math_operator} {num_2} = {num_1 - num_2}")
        elif math_operator == "*":
            print(f"Результат операции {num_1} {math_operator} {num_2} = {num_1 * num_2}")
        elif math_operator == "/":
            try:
                print(f"Результат операции {num_1} {math_operator} {num_2} = {num_1 / num_2}")
            except ZeroDivisionError:
                print("Ошибка деления на ноль")
            break
    break
