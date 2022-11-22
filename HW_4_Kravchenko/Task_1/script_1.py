import json
from HW_4_Kravchenko.Task_1.exceptions import NotFound


def get_company_city(company_id: str) -> str:
    """Возвращает город регистрации компании по её ID.

    Данные о компаниях содержатся в файле company_db.json. Каждому ID соответствует свой словарь с данными о компании.
    :param company_id: ID компании.
    :return: Название города.
    """

    with open("company_db.json") as f:
        comp_db = json.load(f)
    # print(type(comp_db), comp_db)
    if comp_db.get(company_id) is None:
        raise NotFound(f"Company with ID '{company_id}' is not found")
    else:
        # print(comp_db.get(company_id))
        # print(comp_db.get(company_id).get("city"))
        return comp_db.get(company_id).get("city")


if __name__ == "__main__":
    print(get_company_city("1"))
    # print(get_company_city("test"))
