# importing the requests library 
import requests
import json
from random import randint
  
# api-endpoint 
URL = "http://localhost:5000"

r = requests.post(URL + '/players',data = {'name' : 'Frederik'})
print(r)
r = requests.post(URL + '/players',data = {'name' : 'Flore'})
print(r)

r = requests.post(URL + '/games',data = {'home_player' : 'Frederik', 'out_player' : 'Flore'})
print(r)
print(r.content)
identifier = json.loads(r.content)['identifier']
print('identifier:', identifier)

def set_result():
    if randint(0,1) == 1:
        home = 11
        out = randint(0,9)
    else:
        home = randint(0,9)
        out = 11 
    return home, out

def game_result():
    home1, out1 = set_result()
    home2, out2 = set_result()
    if home1 == home2 or out1 == out2:
        return home1, out1, home2, out2
    else:
        home3 , out3 = set_result()
        return home1, out1, home2, out2, home3, out3

g_result = [ game_result() ]
print(g_result)

result = {
    "identifier" : identifier,
    "result" : g_result
}

r = requests.put(URL + '/games',data = result)
print(r)
print(r.content)