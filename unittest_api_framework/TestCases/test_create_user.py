# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append("/Users/gaurav.mishra/framework/library")
sys.path.append("/Users/gaurav.mishra/framework/library/TestModules")
sys.path.append("/Users/gaurav.mishra/framework/library/utils")

import User
from log import testlog, fn_entry, fn_exit

class TestUser(unittest.TestCase):
  """
  Test case TestUser
  """
  # positive negetive scanario for create_user api

  # json based test cases
  def test_create_user(self):
    fn_entry("Entering test_create_user")
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
    testlog.info(payload)
    res = User.create_user(payload)
    testlog.info(res.status_code)
    testlog.info(res.json())
    self.assertEqual(res.status_code, 200)
    self.assertIsNotNone(res.json()['message'])
    res = User.get_user('xdfghjk123456').json()
    testlog.info(res)
    self.assertEqual(res['username'], 'xdfghjk123456')
    self.assertEqual(res['firstName'], 'ab')
    self.assertEqual(res['lastName'], 'c')
    self.assertEqual(res['email'], 'a@b.com')
    self.assertEqual(res['password'], 'a')
    self.assertEqual(res['phone'], '987766')
    self.assertEqual(res['userStatus'], 0)
    self.assertIsNotNone(res['id'])
    fn_exit("Exiting test_create_user")

  def test_create_user_spl_char(self):
    fn_entry("Entering test_create_user_spl_char")
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
    testlog.info(payload)
    res = User.create_user(payload)
    testlog.info(res.status_code)
    testlog.info(res.json())
    self.assertEqual(res.status_code, 200)
    self.assertIsNotNone(res.json()['message'])
    res = User.get_user('!@$%^&*(_)+=-{}[]><.,').json()
    testlog.info(res)
    self.assertEqual(res['username'], '!@$%^&*(_)+=-{}[]><.,')
    self.assertEqual(res['firstName'], 'ab')
    self.assertEqual(res['lastName'], 'c')
    self.assertEqual(res['email'], 'a@b.com')
    self.assertEqual(res['password'], 'a')
    self.assertEqual(res['phone'], '987766')
    self.assertEqual(res['userStatus'], 0)
    self.assertIsNotNone(res['id'])
    fn_exit("Exiting test_create_user_spl_char")

  def test_create_user_unicode(self):
    fn_entry("Entering test_create_user_unicode")
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
    testlog.info(payload)
    res = User.create_user(payload)
    testlog.info(res.status_code)
    testlog.info(res.json())
    self.assertEqual(res.status_code, 200)
    res = User.get_user('Ï')
    testlog.info(res.status_code)
    testlog.info(res.json())
    self.assertEqual(res.status_code, 200)
    fn_exit("Exiting test_create_user_unicode")

  def test_create_user_all_empty_fields(self):
    fn_entry("Entering test_create_user_all_empty_fields")
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
    testlog.info(payload)
    res = User.create_user(payload)
    testlog.info(res.status_code)
    testlog.info(res.json())
    self.assertEqual(res.status_code , 200)
    fn_exit("Exiting test_create_user_all_empty_fields")

  def test_create_user_no_id(self):
    fn_entry("Entering test_create_user_no_id")
    payload = {
    "username": 'abc',
    "firstName": 'abc',
    "lastName": 'abc',
    "email": 'abc',
    "password": 'abc',
    "phone": 'abc',
    "userStatus": 0
    }
    testlog.info(payload)
    res = User.create_user(payload)
    testlog.info(res.status_code)
    testlog.info(res.json())
    self.assertEqual(res.status_code , 200)
    fn_exit("Exiting test_create_user_no_id")

  def test_create_user_no_username(self):
    fn_entry("Entering test_create_user_no_username")
    payload = {
    "id": 1,
    "firstName": 'abc',
    "lastName": 'abc',
    "email": 'abc',
    "password": 'abc',
    "phone": 'abc',
    "userStatus": 0
    }
    testlog.info(payload)
    res = User.create_user(payload)
    testlog.info(res.status_code)
    testlog.info(res.json())
    self.assertEqual(res.status_code , 200)
    fn_exit("Exiting test_create_user_no_username")

  def test_create_user_only_username(self):
    fn_entry("Entering test_create_user_only_username")
    payload = {
    "username": 'fghjk',
    }
    testlog.info(payload)
    res = User.create_user(payload)
    testlog.info(res.status_code)
    testlog.info(res.json())
    self.assertEqual(res.status_code , 200)
    res = User.get_user('fghjk').json()
    testlog.info(res)
    self.assertEqual(res['username'], 'fghjk')
    fn_exit("Exiting test_create_user_only_username")

  def test_create_user_empty_payload(self):
    fn_entry("Entering test_create_user_empty_payload")
    payload = {}
    testlog.info(payload)
    res = User.create_user(payload)
    testlog.info(res.status_code)
    testlog.info(res.json())
    self.assertEqual(res.status_code , 200)
    fn_exit("Exiting test_create_user_empty_payload")

suite = unittest.TestLoader().loadTestsFromTestCase(TestUser)
unittest.TextTestRunner(verbosity=2).run(suite)
