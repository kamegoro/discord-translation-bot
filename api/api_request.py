import requests


def make_api_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
