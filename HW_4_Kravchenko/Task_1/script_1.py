import json
from exceptions import NotFound, NoAccess


def user_id(get_company_city):
    def wrapper(user_id: str, company_id: str):
        with open("users_db.json") as f:
            users_db = json.load(f)
        # print(users_db.get(user_id))
        # print(int(company_id))
        # print(users_db.get(user_id).get('companies'))
        if users_db.get(user_id) is None:
            raise NotFound(f"User with ID '{user_id}' does not exist")
        elif int(company_id) in users_db.get(user_id).get('companies'):
            return get_company_city(company_id)
        else:
            raise NoAccess(f"User with ID '{user_id}' does not have enough permissions")
    return wrapper


@user_id
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
    print(get_company_city(user_id="1", company_id="1"))
    # print(get_company_city("test"))
