import json
from library.rest_handler import RestHandler

BASE_URL = "https://petstore.swagger.io/v2/pet"
res_handle = RestHandler()

def get_pet(status='available'):
  url = "{}/findByStatus?status={}".format(BASE_URL, status)
  response = res_handle.request(type='get', url=url, payload=[])
  return response

def add_pet(payload):
  url = BASE_URL
  response = res_handle.request(type='post', url=url, payload=json.dumps(payload))
  return response

def update_pet(payload):
  url = BASE_URL
  response = res_handle.request(type='put', url=url, payload=json.dumps(payload))
  return response

# print update_pet()