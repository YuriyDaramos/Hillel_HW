def valcode_input_and_validate(valcode=None):
    """
    Инициирует ввод кода валюты с валидацией, возвращает код валюты; или проверяет валидность полученного аргумента.

    :param valcode: Код валюты (USD, EUR etc). Принимает только string.
    :return: Код валюты; если аргумент valcode передается, то производится только валидация аргумента
            с возвратом True при успехе и False при неудаче.
    """
    import requests
    import json

    VC_LIST_CALLER = "help"  # Команда для вызова списка возможных кодов валют

    vc_list = []  # Список возможных значений valcode
    req_current_date = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
    # Получение данных о курсе на сегодня, среди данных есть список возможных кодов валюты
    # Ниже пример получаемого словаря из json:
    # {"r030":840,
    # "txt":"Долар США",
    # "rate":36.5686,
    # "cc":"USD",
    # "exchangedate":"18.10.2022"}

    for i in json.loads(req_current_date.content):
        vc_list.append(i["cc"])  # Получение/актуализация списка возможных значений valcode

    # Блок для валидации кода валюты если аргумент был передан (не None)
    if valcode is not None:
        if valcode.upper() not in vc_list:
            return False
        else:
            return True

    # Блок ввода и валидации если аргумент не передан
    while True:
        print("Введите код валюты (USD, EUR etc):")
        valcode = input()
        if valcode.replace("\"", "") == VC_LIST_CALLER:
            for i in json.loads(req_current_date.content):
                print(i["cc"], i["txt"])  # Показ списка возможных значений valcode
            continue
        elif valcode.upper() not in vc_list:
            print("Вы ввели некорректный код валюты. "
                  f"Если хотите увидеть список возможных значений, введите \"{VC_LIST_CALLER}\"")
            continue
        break
    return valcode


def date_val(date, year="", month="", day="", future=False):
    """
    Проверяет существование даты по указанной маске и может сравнивать с текущей.

    :param date: Проверяемая дата, принимает строку в форматах YYYY, YYYYMM или YYYYMMDD (без разделителей).
                Если передаем год, месяц или день -- обязательно необходимо указывать и соответствующий
                параметр year, month или day как "%Y", "%m" или "%d".
                YYYY лежит в диапазоне от 1 до 9999.
    :param year: Маска для проверки года, принимает только "%Y" или "".
                Обязательно указывать "%Y" если в date передан год.
    :param month: Маска для проверки месяца, принимает только "%m" или "".
                Обязательно указывать "%m" если в date передан месяц.
    :param day: Маска для проверки дня, принимает только "%d" или "".
                Обязательно указывать "%d" если в date передан день.
    :param future: Принимает True и False. Если True, то инициирует сравнение с текущей датой.
    :return: True если дата существует, иначе False. Если future=True, а дата в будущем, то возвращает "future".
    """
    import datetime

    mask = year + month + day

    try:
        datetime.datetime.strptime(date, mask)
        # strptime преобразует date в строку по формату mask, при неудаче поднимается ValueError
    except ValueError:
        return False
    if future and datetime.datetime.now() <= datetime.datetime.strptime(date, mask):
        return "future"
    return True


def date_input_and_validate():
    """Запускает пользовательский ввод даты с валидацией, возвращает строку с датой в формате YYYYMMDD"""
    FUTURE_DATE_MESSAGE = "Нельзя выбрать еще не наступившую дату."
    INEXIST_DATE_MESSAGE = "Введена неверная или несуществующая дата."

    # Ввод и валидация года
    while True:
        print("Введите год:")
        year = input()
        for i in range(1, 4):  # Приведение к формату YYYY (если пользователь вводит "900" вместо "0900")
            if len(year) == i:
                year = "0" * (4 - i) + year
        if date_val(year, year="%Y", future=True) == "future":
            print(FUTURE_DATE_MESSAGE)
            continue
        elif date_val(year, year="%Y", future=True) is False:
            print(INEXIST_DATE_MESSAGE)
            continue
        elif int(year) < 1999:
            print("НБУ не предоставляет данные о курсе валют до 1999 года.")
            continue
        break

    # Ввод и валидация месяца на основе года
    while True:
        print("Введите месяц:")
        month = input()
        if len(month) == 1:  # Приведение к формату MM (если пользователь вводит "3" вместо "03")
            month = "0" + month
        if date_val(year + month, year="%Y", month="%m", future=True) == "future":
            print(FUTURE_DATE_MESSAGE)
            continue
        elif date_val(year + month, year="%Y", month="%m", future=True) is False:
            print(INEXIST_DATE_MESSAGE)
            continue
        break

    # Ввод и валидация дня на основе года и месяца
    while True:
        print("Введите день:")
        day = input()
        if len(day) == 1:  # Приведение к формату DD (если пользователь вводит "3" вместо "03")
            day = "0" + day
        if date_val(year + month + day, year="%Y", month="%m", day="%d", future=True) == "future":
            print(FUTURE_DATE_MESSAGE)
            continue
        elif date_val(year + month + day, year="%Y", month="%m", day="%d", future=True) is False:
            print(INEXIST_DATE_MESSAGE)
            continue
        break

    return year + month + day


def money_input_and_validation():
    """Запускает пользовательский ввод и валидацию конвертируемой валюты, возвращает строку"""
    INCORRECT_INPUT_MESSAGE = "Сумма ведена некорректно."

    while True:
        print("Введите конвертируемую сумму (UAH):")
        uah = input()
        try:
            float(uah)
        except ValueError:
            print(INCORRECT_INPUT_MESSAGE)
            continue
        break
    return uah


def currensy_calc(valcode=valcode_input_and_validate(),
                  date=date_input_and_validate(),
                  uah=money_input_and_validation()):
    """
    Вызов валютного калькулятора для UAH в любую другую валюту поддерживаемую НБУ.

    Любые из аргументов можно задать при вызове функции, иначе будет предложен ввод и последующая валидация значений.
    Тип параметров может быть только string.
    :param valcode: Код валюты (USD, EUR etc).
    :param date: Дата для парсинга курса валюты в формате YYYYMMDD.
    :param uah: Количество конвертируемых средств.
    :return: Форматированная строка с информацией о результатах конвертации.
    """
    import requests
    import json

    req = requests.get(
        f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&date={date}&json")
    if req.status_code == 200:
        req_dict = json.loads(req.content)[0]
        result = float(uah) / req_dict["rate"]
        return print(f"Если {uah} UAH обменяете по курсу НБУ на {req_dict['exchangedate']} "
                     f"вы получите {round(result, 2)} {req_dict['cc']}.")
    return print(f"Ошибка, status_code={req.status_code}")


currensy_calc()
