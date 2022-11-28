import requests
import uvicorn
from fastapi import FastAPI

app = FastAPI()


def get_main_info(term):
    url = f"https://en.wikipedia.org/w/api.php?action=opensearch&" \
          f"search={term}&limit=10&namespace=0&format=json"
    response = requests.get(url)
    return response.json()


def get_snippet(term):
    url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&" \
          f"srsearch={term}&format=json"
    response = requests.get(url)
    return response.json()


def get_content(term):
    url = f"https://en.wikipedia.org/w/api.php?action=query&" \
          f"prop=revisions&titles={term}&rvslots=*&rvprop=content&" \
          f"formatversion=2&format=json"
    response = requests.get(url)
    return response.json()


def get_random():
    url = f"https://en.wikipedia.org/w/api.php?action=query&" \
          f"list=random&format=json"
    response = requests.get(url)
    return response.json()


@app.get("/")
def root():
    return {
        "message": "Welcome to this MiniWiki API",
        "endpoints": [
            "/search/{term}",
            "/search1/{term}",
            "/search2/{term}",
            "/search3/{term}",
            "/random",
        ]
    }


@app.get("/search1/{term}")
def search(term: str):
    return get_main_info(term)


@app.get("/search2/{term}")
def search2(term: str):
    return get_snippet(term)


@app.get("/search3/{term}")
def search3(term: str):
    return get_content(term)


@app.get("/search/{term}")
def search(term: str):
    main_info = get_main_info(term)
    title, url = main_info[1][0], main_info[3][0]
    snippet_info = get_snippet(term)
    snippet = snippet_info['query']['search'][0]['snippet']
    related_pages = []
    for related_page in snippet_info['query']['search'][1:]:
        related_pages.append(related_page['title'])
    content = get_content(title)
    content = content['query']['pages'][0]['revisions'][0]['slots']['main'][
        'content']
    return {
        "title": title,
        "url": url,
        "snippet": snippet,
        "related_pages": related_pages,
        "content": content,
    }


@app.get("/random")
def random():
    return get_random()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.2", port=8000)
