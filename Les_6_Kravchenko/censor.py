badword_text = "You motherfucker, come on, you little ass... fuck with me, eh?! You fucking little asshole, " \
               "dickhead, cocksucker... You fuckin’ — come on, come fuck with me! I’ll get your ass, you jerk! Oh, " \
               "you fuckhead, motherfucker! Fuck all you and your family! Come on, you cocksucker, slime bucket, " \
               "shitface, turdball! Come on, you scum sucker, you fucking with me?! Come on, you asshole! "

badword_blacklist = ["Motherfucker", "ass", "fuck", "fucking", "asshole", "dickhead", "cocksucker", "fuckin", "jerk",
                     "fuckhead", "shitface", "turdball", "Sucker"]


def censor_text(text, blacklist):
    """
    Цензурирует слова в тексте заменяя их на *, но оставляет первый символ чтобы все могли догадаться

    Также алгоритм восстанавливает некоторые знаки препинания
    :param text: Текст для цензурирования, регистр не важен
    :type text: str
    :param blacklist: Черный список слов, регистр не важен
    :type blacklist: list
    :return: Зацензуренный текст
    :rtype: str
    """

    word_list = text.split(" ")     # Список слов в тексте
    index = 0  # Счётчик слов, нужен для итерации слов

    lower_blacklist = list(map(str.lower, blacklist))

    # Поиск и обработка "плохих" слов
    for word in word_list:
        word_stripped = word.rstrip(",.!?'’")
        if word_stripped.lower() in lower_blacklist:
            if len(word_stripped) != len(word):
                # spm -- кол-во потерянных знаков препинания после "раздевания" слова
                spm = len(word_stripped) - len(word)  # spm -- Stripped Punctuation Marks
            else:
                spm = 0
            # замена определенных слов в тексте (по факту замена элементов списка)
            # слово в тексте = первый символ слова + кол-во "*" равное кол-ву оставшихся символов + знаки пунктуации
            word_list[index] = word[0] + ("*" * (len(word_stripped) - 1)) + (word[-1] * (spm * -1))
        index += 1
    return " ".join(word_list)


print("---------------------------------")
print(badword_text)
print("---------------------------------")
print(censor_text(badword_text, badword_blacklist))
print("---------------------------------")
