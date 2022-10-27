def encode_caesar(text, key):
    """
    Шифрует текст по методу Цезаря

    :param text: Текст для шифрования
    :type text: str
    :param key: Ключ для шифра (значение сдвига)
    :type key: int
    :return: Зашифрованный текст
    :rtype: str
    """

    new_text = []   # Список с зашифрованными символами
    for letter in text:
        # Перевод символа в код >> сдвиг кода на значение ключа >> перевод в символ >> добавление в список
        new_text.append(chr(ord(letter) + key))

    return "".join(new_text)


def decode_caesar(text, key):
    """
    Дешифрует текст по методу Цезаря

    :param text: Текст для дешифровки
    :type text: str
    :param key: Ключ для шифра (значение сдвига)
    :type key: int
    :return: Расшифрованный текст
    :rtype: str
    """

    new_text = []       # Список с дешифрованными символами
    for letter in text:
        # Перевод символа в код >> сдвиг кода на значение ключа >> перевод в символ >> добавление в список
        new_text.append(chr(ord(letter) - key))

    return "".join(new_text)
