# 
# Uzdevums: Izmantojot bibliotēku "requests" uzģenerēt Chuck Norris jokus
# https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content
# https://api.chucknorris.io/
# 
# 1. Izdrukā 3 nejaušus jokus no Chuck Norris
# 
# 2. Izdrukā 3 nejaušus jokus no Chuck Norris par programmēšanu
# 
import requests

for _ in range(3):
    request = requests.get('https://api.chucknorris.io/jokes/random')
    print(request.json()["value"])
print('')
for _ in range(3):
    requestCaregory = requests.get('https://api.chucknorris.io/jokes/random?category=dev')
    print(requestCaregory.json()["value"])