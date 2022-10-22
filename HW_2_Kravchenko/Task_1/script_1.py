EXIT_COMMAND = "/q" # Команда выхода для пользователя

list_even = []      # Список для четных чисел
number = None       # Содержит последнее значение введенное пользователем

while True:
    print("Для остановки программы введите /q, для продолжения отправьте любое число")
    number = input()
    try:
        number = float(number)
        if number % 2 == 0:
            list_even.append(number)
    except ValueError:
        if number == EXIT_COMMAND:
            print(f"Введено чётных чисел: {len(list_even)}")
            break
        else:
            print("Введен неверный тип данных, введите число")
