def simplify_list(list_set_tuple, list_1d=None):
    """
    Распаковывает список с неопределенной глубиной вложенности (до 998 на самом деле).

    Заметка 1: пустые вложенные элементы никак не отражаются в возвращаемом списке
    Заметка 2: элементы множества при распаковке не сортируются, порядок будет случайным

    :param list_1d: Определение локального списка для правильной работы функции
    :type list_1d: list
    :param list_set_tuple: Распаковываемый список, множество или кортеж
    :type list_set_tuple: list, set, tuple
    :return: Развернутый список составленный из элементов полученного списка
    :rtype: list
    """

    # Объявление списка для заполнения.
    if list_1d is None:
        list_1d = []

    # Рекурсивный перебор всех элементов списка
    for element in list_set_tuple:
        if isinstance(element, (list, set, tuple)):
            simplify_list(element, list_1d)
        else:
            list_1d.append(element)
    return list_1d
