import requests

DEFAULT_RETRY_COUNT=5
class RestHandler:

  def set_headers(self, added_fields=None):
    '''
    This will set the base header for rest req.
    :param added_fields: any fields to be added in header
    :return: header(dict)
    '''
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json'}
    if added_fields:
      headers.update(added_fields)
    return headers

  def get_request(self, final_url, header, retry=DEFAULT_RETRY_COUNT):
    '''
    To get responce of a req.
    :param final_url: url wants to get to
    :param header: header for req
    :param retry: if req need to retry
    :return: responce as pobject (dict)
    '''
    try:
      count = 0
      while count<retry:
        response = requests.get(final_url, headers=header)
        if response.status_code in [428, 429]: # rate limit touched
          count+=1
        else:
          break
      return response
    except Exception as e:
      print(e)
      return False

  def post_request(self, final_url, payload, header):
    try:
      response = requests.post(final_url, data=payload, headers=header)
      return response
    except Exception as e:
      print(e)
      return False

  def put_request(self, final_url, payload, header):
    try:
      response = requests.put(final_url, data=payload, headers=header)
      return response
    except Exception as e:
      print(e)
      return False

  def request(self, **kwargs):
    type = kwargs['type']
    url = kwargs['url']
    payload = kwargs['payload']
    header = self.set_headers()
    serializer = self.get_serializer(type)
    return serializer(url, payload, header)

  def get_serializer(self, req_type):
    if req_type.upper() == 'POST':
      return self.post_request
    elif req_type.upper() == 'GET':
      return self.get_request
    elif req_type.upper() == 'PUT':
      return self.put_request
    else:
      raise ValueError(req_type)

payload = {
  "id": 0,
  "username": "gaurav",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}
final_url = "https://petstore.swagger.io/v2/user"
rest_handle = RestHandler()
#
# res=rest_handle.post_request(final_url, json.dumps(payload), header=rest_handle.set_headers())
# print res
import json
res = rest_handle.request(type='post', url=final_url, payload=json.dumps(payload) )
# print res
# rest_handle = RestHandler()
# url = 'https://petstore.swagger.io/v2/user/{}'.format('string')
# print rest_handle.get_request(url, header=rest_handle.set_headers())

