def min_finder(*numbers):
    """Поиск наименьшего значения среди принятых аргументов"""
    min = numbers[0]
    [min = i for i in numbers: if i < min]
    return min


def max_finder(*numbers):
    """Поиск наибольшего значения среди принятых аргументов"""
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return max


def max_min_sum(*numbers):
    """Ссумирует наибольшее и наименьшее число среди принятых аргументов"""
    sum = min_finder(*numbers) + max_finder(*numbers)
    return sum


print(max_min_sum(100, 0.0, -25))