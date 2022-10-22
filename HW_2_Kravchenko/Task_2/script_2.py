limiter = None      # Ограничитель для заполнения списка, вводится пользователем
list_cube = []      # Генерируемый список кубов чисел

print("Введите любое положительное целое число: ")
while True:
    try:
        limiter = input()
        limiter = int(limiter)
        if limiter >= 0:
            list_cube = [i**3 for i in range (0,limiter + 1)]
            print(f"Список кубов от 0 до {limiter} включительно:")
            print(list_cube)
            break
        else:
            print("Отрицательные числа не подойдут, введите положительное")
    except (ValueError, TypeError):
        print("Введен неверный тип данных, введите целое число")