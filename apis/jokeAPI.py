import requests

def get_geek_jokes() :
    response = requests.get('https://geek-jokes.sameerkumar.website/api?format=json')
    return response.json()['joke']

def get_jokes() :
    response = requests.get('https://v2.jokeapi.dev/joke/Any?type=single')
    return response.json()['joke']

# if __name__=='__main__':
#     print(get_geek_jokes())
