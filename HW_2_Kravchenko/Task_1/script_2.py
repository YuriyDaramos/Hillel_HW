EXIT_COMMAND = "/q" # Команда выхода для пользователя

number = None       # Содержит последнее значение введенное пользователем
number_sum = 0      # Ссума всех введенных чисел
number_counter = 0  # Счётчик введенных чисел

while True:
    print("Для остановки программы введите /q, для продолжения отправьте любое число")
    number = input()
    try:
        number = float(number)
        number_counter += 1
        number_sum += number
    except ValueError:
        if number == EXIT_COMMAND:
            if number_counter == 0:
                break
            else:
                print(f"Среднее арфиметическое: {number_sum / number_counter}") # Вычисление среднего арифметического
                break
        else:
            print("Введен неверный тип данных, введите число")
