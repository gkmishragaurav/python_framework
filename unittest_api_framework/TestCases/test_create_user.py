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
  # positive negetive scanario for create_user api

  # json based test cases
  def test_create_user(self):
    payload = {
      "id": 0,
      "username": 'xdfghjk123456',
      "firstName": 'ab',
      "lastName": 'c',
      "email": 'a@b.com',
      "password": 'a',
      "phone": '987766',
      "userStatus": 0
    }
    res = User.create_user(payload)
    self.assertEqual(res.status_code, 200)
    self.assertIsNotNone(res.json()['message'])
    res = User.get_user('xdfghjk123456').json()
    self.assertEqual(res['username'], 'xdfghjk123456')
    self.assertEqual(res['firstName'], 'ab')
    self.assertEqual(res['lastName'], 'c')
    self.assertEqual(res['email'], 'a@b.com')
    self.assertEqual(res['password'], 'a')
    self.assertEqual(res['phone'], '987766')
    self.assertEqual(res['userStatus'], 0)
    self.assertIsNotNone(res['id'])

  def test_create_user_spl_char(self):
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
    res = User.create_user(payload)
    self.assertEqual(res.status_code, 200)
    self.assertIsNotNone(res.json()['message'])
    res = User.get_user('!@$%^&*(_)+=-{}[]><.,').json()
    self.assertEqual(res['username'], '!@$%^&*(_)+=-{}[]><.,')
    self.assertEqual(res['firstName'], 'ab')
    self.assertEqual(res['lastName'], 'c')
    self.assertEqual(res['email'], 'a@b.com')
    self.assertEqual(res['password'], 'a')
    self.assertEqual(res['phone'], '987766')
    self.assertEqual(res['userStatus'], 0)
    self.assertIsNotNone(res['id'])

  def test_create_user_unicode(self):
    payload = {
    "id": 0,
    "username": 'Ï',
    "firstName": 'Ï',
    "lastName": 'Ï',
    "email": 'Ï',
    "password": 'Ï',
    "phone": 'Ï',
    "userStatus": 0
    }
    res = User.create_user(payload)
    self.assertEqual(res.status_code, 200)
    res = User.get_user('Ï')
    self.assertEqual(res.status_code, 200)

  def test_create_user_all_empty_fields(self):
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
    res = User.create_user(payload)
    self.assertEqual(res.status_code , 200)

  def test_create_user_no_id(self):
    payload = {
    "username": 'abc',
    "firstName": 'abc',
    "lastName": 'abc',
    "email": 'abc',
    "password": 'abc',
    "phone": 'abc',
    "userStatus": 0
    }
    res = User.create_user(payload)
    self.assertEqual(res.status_code , 200)

  def test_create_user_no_username(self):
    payload = {
    "id": 1,
    "firstName": 'abc',
    "lastName": 'abc',
    "email": 'abc',
    "password": 'abc',
    "phone": 'abc',
    "userStatus": 0
    }
    res = User.create_user(payload)
    self.assertEqual(res.status_code , 200)

  def test_create_user_only_username(self):
    payload = {
    "username": 'fghjk',
    }
    res = User.create_user(payload)
    self.assertEqual(res.status_code , 200)
    res = User.get_user('fghjk').json()
    self.assertEqual(res['username'], 'fghjk')

  def test_create_user_empty_payload(self):
    payload = {}
    res = User.create_user(payload)
    self.assertEqual(res.status_code , 200)

suite = unittest.TestLoader().loadTestsFromTestCase(TestUser)
unittest.TextTestRunner(verbosity=2).run(suite)