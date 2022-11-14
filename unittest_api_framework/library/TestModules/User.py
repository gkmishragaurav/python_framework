from library.rest_handler import RestHandler
import json

BASE_URL = "https://petstore.swagger.io/v2"
res_handle = RestHandler()

def create_user_from_csv():
  '''take a csv file as input and create all users'''
  pass

def create_random_user():
  '''random user will be created based on data'''
  pass

def create_user(payload):
  url = "{}/user".format(BASE_URL)
  response = res_handle.request(type='post', url=url, payload=json.dumps(payload))
  return response

def create_user_array(payload):
  url = "{}/user/createWithArray".format(BASE_URL)
  response = res_handle.request(type='post', url=url, payload=json.dumps(payload))
  return response

def update_user(user_name, updated_payload):
  url = "{}/user/{}".format(BASE_URL, user_name)
  response = res_handle.request(type='put', url=url, payload=json.dumps(updated_payload))
  return response

def get_user(user_name):
  url = '{}/user/{}'.format(BASE_URL, user_name)
  response = res_handle.request(type='get', url=url, payload=[])
  return response

