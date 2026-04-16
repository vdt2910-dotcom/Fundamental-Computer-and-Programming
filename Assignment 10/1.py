import requests

def get_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = response.json()
    print(data["value"])  
get_joke()