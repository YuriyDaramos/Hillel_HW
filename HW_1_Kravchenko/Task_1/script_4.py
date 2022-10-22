list = [11,12,32,33,1,2,3]
match_list = []     # Список для совпадающих чисел
user_list = []      # Список для заполнения пользователем
user_list = [int(i) for i in input("Введите последовательность чисел через пробел: ").split()]
user_list_set = set(user_list)  # Используется множество для избавления от дубликатов в user_list
for i in user_list_set:
    for k in list:          # Добавление совпадающих чисел в список для совпадающих чисел
        if i == k:
            match_list.append(i)
            break
print("Заданный список", list)
print("Ваш список:", user_list)
print("Всего совпадений: ", len(match_list))
print("Совпадающие значения: ", match_list)
print("Это был вариант с использованием циклов и списков. Есть более простой вариант через множества")
match_set = set(list) & set (user_list)
print("Количество совпадений: ", len(match_set))
print("Множество совпадающих значений: ", match_set)