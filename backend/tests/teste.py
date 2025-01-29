import requests

def teste_teste():
    r = requests.get('http://localhost:8000/products')
    response = r.json()
    print(response)

teste_teste()