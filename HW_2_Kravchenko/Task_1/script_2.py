EXIT_COMMAND = "/q"  # Команда выхода для пользователя

number = float()    # Содержит последнее значение введенное пользователем
number_sum = 0      # Сумма всех введенных чисел
number_counter = 0  # Счётчик введенных чисел

while True:
    print("Для остановки программы введите /q, для продолжения отправьте любое число")
    number = input()
    try:
        number = float(number)
    except ValueError:
        if number == EXIT_COMMAND:
            if number_counter == 0:
                break
            else:
                print(f"Среднее арифметическое: {number_sum / number_counter}")  # Вычисление среднего арифметического
                break
        else:
            print("Введен неверный тип данных, введите число")
            continue

    number_counter += 1
    number_sum += number
