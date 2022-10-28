import requests


def get_programming_quote():
    response = requests.get("https://programming-quotes-api.herokuapp.com/Quotes/random")
    return response.json()['en']

def get_motivational_quote():
    response = requests.get('https://api.goprogram.ai/inspiration')
    return response.json()['quote']


# if __name__ == '__main__' : 
#     print(get_motivational_quote())