EXIT_COMMAND = "/q"  # Команда выхода для пользователя

list_of_even = []   # Список для четных чисел

while True:
    print("Для остановки программы введите /q, для продолжения отправьте любое число")
    number = input()
    try:
        number = float(number)
        if number % 2:
            list_of_even.append(number)
    except ValueError:
        if number == EXIT_COMMAND:
            print(f"Введено чётных чисел: {len(list_of_even)}")
            break
        else:
            print("Введен неверный тип данных, введите число")
