import os

import requests
from bs4 import BeautifulSoup

URL = 'http://www.xkcd.com/'
folder_name = 'images'


def create_folder():
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def get_last_comic_number():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    comic_url = soup.find('meta', property='og:url')['content']
    comic_number = comic_url.split('/')[-2]
    return comic_number


def download_comic(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image = soup.find(id='comic').find('img')
    comic_url = 'http:' + image['src']
    comic_name = os.path.basename(comic_url)
    print('Downloading', comic_name)

    with open(os.path.join(folder_name, os.path.basename(comic_url)),
              'wb') as f:
        f.write(requests.get(comic_url).content)


def download_comics(number):
    last_comic_number = get_last_comic_number()
    for i in range(int(last_comic_number), int(last_comic_number) - number, -1):
        download_comic(URL + str(i))


if __name__ == '__main__':
    create_folder()
    download_comics(10)
