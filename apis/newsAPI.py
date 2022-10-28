import requests

def get_news_api():
    response = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=a50f180e554e4a98a049d6eca74783dd')
    return response.json()['articles']

# if __name__ == "__main__":
#     print(get_news_api())
    