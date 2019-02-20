# THIS IS A TEST FILE

import requests
from pprint import pprint
import json

# GET REQUEST
r = requests.get('https://hunter-todo-api.herokuapp.com/user')
r.json()

pprint(r.json())


# POST REQUEST- create new user
# url = 'https://hunter-todo-api.herokuapp.com/user'
# payload = {'username': 'john'}
# r = requests.post(url, json=payload)
#  pprint(r.json())

# AUTHENTICATE

# cookies = {'sillyauth': 'am9obg=='}

# r = requests.post(
#     'https://hunter-todo-api.herokuapp.com/auth', cookies=cookies)


# # ACCESS TODOS FOR USER
# url2 = 'https://hunter-todo-api.herokuapp.com/todo-item'
# r = requests.get(url2, cookies=cookies)
# pprint(r.json())

# # CREATE A TODOS(MADE 3)
# payload2 = {'content': 'finish app'}
# r = requests.post(url2, json=payload2, cookies=cookies)
# pprint(r.json())


# UPDATE A TODOS
# payload3 = {'completed': True}
# params = {'id': 60}
# r = requests.put('https://hunter-todo-api.herokuapp.com/todo-item/60',
#                  json=payload3, cookies=cookies)


# delete a todos
# payload4 = {'deleted': True}
# r = requests.delete('https://hunter-todo-api.herokuapp.com/todo-item/103',
#                     json=payload4, cookies=cookies)
