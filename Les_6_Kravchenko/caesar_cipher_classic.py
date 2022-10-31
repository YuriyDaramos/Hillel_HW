def cipher_caesar(text, key, decode=False):
    """
    Шифрует и дешифрует посимвольно текст по методу Цезаря

    Классическое исполнение шифра. Преобразует только латинские буквы обеих регистров

    :param text: Текст для шифрования
    :type text: str
    :param key: Ключ для шифра (значение сдвига).
    :type key: int
    :param decode: Включения режима дешифровки, при значении True дешифрует текст по указанному ключу.
    :type decode: bool
    :return: Обработанный текст
    :rtype: str
    """

    ctext = ""  # cipher text -- обработанные символы текста

    if decode:
        key *= -1
    for char in text:
        if char.islower():
            ctext += (chr((ord(char) + key - 97) % 26 + 97))
        elif char.isupper():
            ctext += (chr((ord(char) + key - 65) % 26 + 65))
        else:
            ctext += char

    return ctext
