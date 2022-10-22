list_1 = ["apple", "orange", 1, None, ["dog", "cat"], "book", "car", True, "False"]     # Задан условием
list_not_str = []   # Список не включающий строки
list_only_str = []  # Список содержащий только строки

for i in list_1:
    if isinstance(i, str):
        list_only_str.append(i)
    else:
        list_not_str.append(i)

print(f"Оригинальный список:")
print(list_1)
print(f"Список без строк:")
print(list_not_str)
print(f"Список только из строк:")
print(list_only_str)

