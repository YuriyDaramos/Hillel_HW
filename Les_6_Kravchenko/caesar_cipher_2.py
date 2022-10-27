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


def test_encode_decode():      # Temp func only for testing
    import random

    t1 = "Шифр Цезаря, также известный как шифр сдвига, код Цезаря — один из самых простых и наиболее широко " \
         "известных методов шифрования. Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом " \
         "тексте заменяется символом, находящимся на некотором постоянном числе позиций левее или правее него в " \
         "алфавите. Например, в шифре со сдвигом вправо на 3, А была бы заменена на Г, Б станет Д, и так далее. "

    key1 = random.randint(1, 10)
    sep = ("\n" + "-" * 50)

    print("ORIGINAL TEXT:\n", t1, sep)

    t1_encode = encode_caesar(t1, key1)
    print(f"ENCODED TEXT (KEY = {key1}):\n", t1_encode, sep)

    t1_decode = decode_caesar(t1_encode, key1)
    print(f"DECODED TEXT (KEY = {key1}):\n", t1_decode, sep)

    t1_wrong_key_decode = decode_caesar(t1_encode, key1 + 1)
    print(f"DECODED TEXT (WRONG KEY = {key1 + 1}):\n", t1_wrong_key_decode, sep)


test_encode_decode()