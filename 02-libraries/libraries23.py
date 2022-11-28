import requests

urls = [
    'http://marca.es/',
    'http://google.es/',
    'http://es.wikipedia.org/',
    'http://www.python.org/',
    'http://github.com/',
    'http://github.com/masdtraca'
]


def request(url):
    return requests.head(url, allow_redirects=True).ok


for url in urls:
    print(url, request(url))
