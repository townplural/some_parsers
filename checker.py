import requests

def check_connection(url):
    response = requests.get(url)
    if response.status_code == 200:
        return True
    return False