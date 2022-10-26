t1 = "Шифр Цезаря, также известный как шифр сдвига, код Цезаря — один из самых простых и наиболее широко известных " \
     "методов шифрования. Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте " \
     "заменяется символом, находящимся на некотором постоянном числе позиций левее или правее него в алфавите. " \
     "Например, в шифре со сдвигом вправо на 3, А была бы заменена на Г, Б станет Д, и так далее. "


def encode_caesar(text, key):
    """Шифрует текст по методу Цезаря

    :param text: Текс для шифрования
    :type text: str
    :param key: Ключ для шифра (значение сдвига)
    :type key: int
    :return: Зашифрованный текст
    :rtype: str"""

    ord_list = []
    char_list = []
    [ord_list.append(ord(char)) for char in text]
    new_ord_list = [ordn + key for ordn in ord_list]
    [char_list.append(chr(ordn)) for ordn in new_ord_list]
    return "".join(char_list)


def decode_caesar(text, key):
    """Дешифрует текст по методу Цезаря

    :param text: Текс для дешифровки
    :type text: str
    :param key: Ключ для шифра (значение сдвига)
    :type key: int
    :return: Расшифрованный текст
    :rtype: str"""

    ord_list = []
    char_list = []
    [ord_list.append(ord(char)) for char in text]
    new_ord_list = [ordn - key for ordn in ord_list]
    [char_list.append(chr(ordn)) for ordn in new_ord_list]
    return "".join(char_list)


t2 = encode_caesar(t1, 50)
print(t2)
print("---------------------------------")
print(decode_caesar(t2, 50))
