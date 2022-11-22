import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://auto.ria.com/uk/car/used/"
# response = requests.get(URL)
#
# soup = BeautifulSoup(response.content, "html.parser")
# tittle = soup.find("section", class_="ticket-item").find("a", class_="address").text


def get_html(url):
    response = requests.get(url)
    if response.status_code != 200:
        return
    return response.content


def get_cars_list(soup):
    soup.find_all("section", class_="ticket-item")
    return soup


def save_to_excel(dict_):
    df = pd.DataFrame.from_dict(dict_)
    writer = pd.ExcelWriter("pandas.xlsx", engine="xlsxwriter")
    df.to_excel(writer, sheet_name="test")
    # writer.save
    pass


def main():
    html = get_html(URL)
    soup = BeautifulSoup(html, "html.parser")

    dict_ = {}

    for car_block in get_cars_list(soup):
        title_block = car_block.find("a", class_="address")
        title = title_block.text
        title = title.strip()
        link = title_block.get("href")

        price_block = car_block.find("div", class_="price-ticket").text
        price_usd = int(price_block.find("span", class_="bold size22 green").text.replace(" ", ""))
        price_uah = int(price_block.find("span", class_="i-block").text.replace(" ", "").replace("грн", "").rstrip())

        city = car_block.find("li", class_="item-char view-location js-location").text.replace("( від )", "").strip()

        dict_[title] = {"link": link,
                        "price_uah": price_uah,
                        "price_usd": price_usd,
                        "city": city}

    pass


if __name__ == "__main__":
    main()
