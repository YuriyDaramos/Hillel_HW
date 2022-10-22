TASK_LIST = ["apple", "orange", 1, None, ["dog", "cat"], "book", "car", True, "False"]
list_not_str = []   # Список не включающий строки
list_only_str = []  # Список содержащий только строки

for i in TASK_LIST:
    if isinstance(i, str):
        list_only_str.append(i)
    else:
        list_not_str.append(i)

print(f"Оригинальный список:")
print(TASK_LIST)
print(f"Список без строк:")
print(list_not_str)
print(f"Список только из строк:")
print(list_only_str)
