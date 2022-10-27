def encode_caesar(text, key):
    """
    Шифрует текст по методу Цезаря

    :param text: Текс для шифрования
    :type text: str
    :param key: Ключ для шифра (значение сдвига)
    :type key: int
    :return: Зашифрованный текст
    :rtype: str
    """

    ord_list = []
    char_list = []

    [ord_list.append(ord(char)) for char in text]   # Перевод символов в коды Юникода
    new_ord_list = [ordn + key for ordn in ord_list]    # Шифрование кодов
    [char_list.append(chr(ordn)) for ordn in new_ord_list]  # Перевод кодов в символы Юникода
    return "".join(char_list)


def decode_caesar(text, key):
    """
    Дешифрует текст по методу Цезаря

    :param text: Текс для дешифровки
    :type text: str
    :param key: Ключ для шифра (значение сдвига)
    :type key: int
    :return: Расшифрованный текст
    :rtype: str
    """

    ord_list = []
    char_list = []
    [ord_list.append(ord(char)) for char in text]   # Перевод символов в коды Юникода
    new_ord_list = [ordn - key for ordn in ord_list]    # Дешифровкае кодов
    [char_list.append(chr(ordn)) for ordn in new_ord_list]  # Перевод кодов в символы Юникода
    return "".join(char_list)
