# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append("/Users/gaurav.mishra/framework/library")
sys.path.append("/Users/gaurav.mishra/framework/library/TestModules")

import User

class TestUser(unittest.TestCase):
  """
  Test case TestUser
  """

  # positive negetive scanario for create_user_array api
  def test_create_user_array_one(self):
    payload = [{
      "id": 0,
      "username": 'abc1',
      "firstName": 'abc1',
      "lastName": 'abc1',
      "email": 'abc1',
      "password": 'abc1',
      "phone": 'abc1',
      "userStatus": 0
    }]
    res = User.create_user_array(payload)
    self.assertEqual(res.status_code, 200)
    res = User.get_user('abc1').json()
    self.assertEqual(res['username'], 'abc1')

  def test_create_user_array_empty_fields(self):
    payload = [{
    "id": 0,
    "username": '',
    "firstName": '',
    "lastName": '',
    "email": '',
    "password": '',
    "phone": '',
    "userStatus": 0
    }]
    res = User.create_user_array(payload)
    self.assertEqual(res.status_code, 200)

  def test_create_user_array_spl_char(self):
    payload = [{
      "id": 0,
      "username": '!@$%^&*(_)+=-{}[]><.,',
      "firstName": 'ab',
      "lastName": 'c',
      "email": 'a@b.com',
      "password": 'a',
      "phone": '987766',
      "userStatus": 0
    }]
    res = User.create_user_array(payload)
    self.assertEqual(res.status_code, 200)
    res = User.get_user('!@$%^&*(_)+=-{}[]><.,').json()
    self.assertEqual(res['username'], '!@$%^&*(_)+=-{}[]><.,')

  def test_create_user_array_unicode(self):
    payload = [{
    "id": 0,
    "username": 'Ï',
    "firstName": 'Ï',
    "lastName": 'Ï',
    "email": 'Ï',
    "password": 'Ï',
    "phone": 'Ï',
    "userStatus": 0
    }]
    res = User.create_user_array(payload)
    self.assertEqual(res.status_code, 200)

  def test_create_user_array_many(self):
    payload = []
    for i in range(10):
      temp = {"username": 'user_name_abc-{}'.format(i)}
      payload.append(temp)
    res = User.create_user_array(payload)
    self.assertEqual(res.status_code, 200)
    for i in range(10):
      res = User.get_user('user_name_abc-{}'.format(i)).json()
      self.assertEqual(res['username'], 'user_name_abc-{}'.format(i))

  def test_create_user_array_empty(self):
    payload = []
    res = User.create_user_array(payload)
    self.assertEqual(res.status_code, 200)

  def test_create_user_array_empty_elements(self):
    payload = [{},{},{},{}]
    res = User.create_user_array(payload)
    self.assertEqual(res.status_code, 200)

suite = unittest.TestLoader().loadTestsFromTestCase(TestUser)
unittest.TextTestRunner(verbosity=2).run(suite)