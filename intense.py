import requests
from bs4 import BeautifulSoup
import json


def download(url):
    response = requests.get(url)

    return response.text


def write(data_dict, filename):
    with open("data.json", "w") as outfile:
        json.dump(data_dict, outfile)

    with open("data.json", "r") as f:
        data = json.load(f)

    print(data)

    return filename


def parse(data):
    data_dict = {}

    soup = BeautifulSoup(data, 'html.parser')
    title = soup.find('h1').text
    Description = soup.find('span', class_="details_text").text
    price = soup.find('div', class_="article_right_price price").text
    area = soup.find('text').text
    published_date = soup.find('div', class_="add_date_block").text
    floors = soup.find('span', class_="all-floors").text
    id = soup.find('div', class_="article_item_id").text
    img = soup.find('div', {"class": "swiper-slide"}).find('img').attrs['src']

    data_dict['title'] = title
    data_dict['description'] = Description
    data_dict['price'] = price
    data_dict['area'] = area
    data_dict['published_date'] = published_date
    data_dict['floors'] = floors
    data_dict['id'] = id
    data_dict['image'] = img
    return data_dict


def main():
    url = 'https://ss.ge/ka/udzravi-qoneba/qiravdeba-3-otaxiani-bina-saburtaloze-6483528'
    filename = "data.json"

    data = download(url)
    result = parse(data)
    write(result, filename)


if __name__ == "__main__":
    main()
