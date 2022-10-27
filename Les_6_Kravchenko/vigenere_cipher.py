# В данный момент шифр работает неправильно. Функции шифровки и дешифровки работают корректно,
#  но сам закодированный текст некорректен, он не отвечает алгоритму Виженера

def encode_vigenere(text, keyword):
    """
    Шифрует текст по методу Виженера

    :param text: Текст для шифрования
    :type text: str
    :param keyword: Слово-ключ для шифра (значение сдвига)
    :type keyword: str
    :return: Зашифрованный текст
    :rtype: str
    """

    import string
    new_keyword = ""
    new_text = []

    # Увеличение ключевого слова до длины текста
    if len(text) - len(keyword) > 0:
        new_keyword = keyword * (len(text) // len(keyword))
        if len(text) % len(keyword) != 0:
            for i in range(len(text) % len(keyword)):
                new_keyword += keyword[i]
        keyword = new_keyword

    # Уменьшение ключевого слова до длины текста
    if len(text) - len(keyword) < 0:
        for i in range(len(text) % len(keyword)):
            new_keyword += keyword[i]
        keyword = new_keyword

    # Алгоритм шифра
    # Алфавит со значениями сдвига для каждого символа
    alphabet = {char: num for num, char in enumerate(string.ascii_letters)}

    for i in range(len(text)):
        # Перевод символа в код >> сдвиг кода на значение ключа >> перевод в символ >> добавление в список
        new_text.append(chr((ord(text[i]) + alphabet.get(keyword[i], 0))))

    return "".join(new_text)


def decode_vigenere(text, keyword):
    """
    Дешифрует текст по методу Виженера

    :param text: Текст для дешифрования
    :type text: str
    :param keyword: Слово-ключ для шифра (значение сдвига)
    :type keyword: str
    :return: Дешифрованный текст
    :rtype: str
    """

    import string
    new_keyword = ""
    new_text = []

    # Увеличение ключевого слова до длины текста
    if len(text) - len(keyword) > 0:
        new_keyword = keyword * (len(text) // len(keyword))
        if len(text) % len(keyword) != 0:
            for i in range(len(text) % len(keyword)):
                new_keyword += keyword[i]
        keyword = new_keyword

    # Уменьшение ключевого слова до длины текста
    if len(text) - len(keyword) < 0:
        for i in range(len(text) % len(keyword)):
            new_keyword += keyword[i]
        keyword = new_keyword

    # Алгоритм шифра
    # Алфавит со значениями сдвига для каждого символа
    alphabet = {char: num for num, char in enumerate(string.ascii_letters)}

    for i in range(len(text)):
        # Перевод символа в код >> сдвиг кода на значение ключа >> перевод в символ >> добавление в список
        new_text.append(chr((ord(text[i]) - alphabet.get(keyword[i], 0))))

    return "".join(new_text)
