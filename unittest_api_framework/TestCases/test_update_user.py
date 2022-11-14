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
  # positive negetive scanario for update_user api
  def test_update_user(self):
    payload = {
      "id": 0,
      "username": "string",
      "firstName": "string",
      "lastName": "string",
      "email": "string",
      "password": "string",
      "phone": "string",
      "userStatus": 0}
    res = User.update_user('abc', payload)
    self.assertEqual(res.status_code, 200)

  def test_update_user_to_unicode(self):
    payload = {
      "id": 0,
      "username": "ß",
      "firstName": "ß",
      "lastName": "ß",
      "email": "string",
      "password": "string",
      "phone": "string",
      "userStatus": 0}
    res = User.update_user('abc', payload)
    self.assertEqual(res.status_code, 200)

  def test_update_user_to_spl_char(self):
    payload = {
      "id": 0,
      "username": '!@$%^&*(_)+=-{}[]><.,',
      "firstName": 'ab',
      "lastName": 'c',
      "email": 'a@b.com',
      "password": 'a',
      "phone": '987766',
      "userStatus": 0
    }
    res = User.update_user('abc', payload)
    self.assertEqual(res.status_code, 200)

  def test_update_user_to_all_empty_fields(self):
    payload = {
    "id": 0,
    "username": '',
    "firstName": '',
    "lastName": '',
    "email": '',
    "password": '',
    "phone": '',
    "userStatus": 0
    }
    res = User.update_user('abc', payload)
    self.assertEqual(res.status_code, 200)

  def test_update_user_only_username(self):
    payload = {
    "username": 'fghjk',
    }
    res = User.update_user('abc', payload)
    self.assertEqual(res.status_code, 200)



suite = unittest.TestLoader().loadTestsFromTestCase(TestUser)
unittest.TextTestRunner(verbosity=2).run(suite)