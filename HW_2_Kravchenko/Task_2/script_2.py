while True:
    print("Введите любое положительное целое число: ")
    list_gen_limiter = input()  # Ограничитель для заполнения списка
    try:
        list_gen_limiter = int(list_gen_limiter)
    except ValueError:
        print("Введен неверный тип данных, введите целое число")
        continue

    if list_gen_limiter < 0:
        print("Отрицательные числа не подойдут, введите положительное")
        continue

    list_of_cubes = [i ** 3 for i in range(0, list_gen_limiter + 1) if list_gen_limiter >= 0]
    print(f"Список кубов от 0 до {list_gen_limiter} включительно:\n"
          f"{list_of_cubes}")
    break
