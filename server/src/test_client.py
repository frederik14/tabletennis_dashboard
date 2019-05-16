# importing the requests library 
import requests
import json
from random import randint
  
# api-endpoint 
URL = "http://localhost:5000"

# r = requests.post(URL + '/players',json = {'name' : 'Frederik'})
# print(r)
# print(r.content)
# r = requests.post(URL + '/players',json = {'name' : 'Flore'})
# print(r)
# print(r.content)
r = requests.post(URL + '/games',json = {'home_player' : 'Frederik', 'out_player' : 'Flore'})
print(r)
print(r.content)
id = json.loads(r.content)['game']['id']
print('identifier:', id)

def rand_result():
    if randint(0,1) == 1:
        home = 2
        out = randint(0,1)
    else:
        home = randint(0,1)
        out = 2 
    return home, out

home_sets, out_sets = rand_result()

result = {
    'id' : id, 
    'home_sets' : home_sets,
    'out_sets' : out_sets 
}

r = requests.put(URL + '/games',json = result)
print(r)
print(r.content)