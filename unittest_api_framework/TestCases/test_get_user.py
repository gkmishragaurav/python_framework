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
  # positive negetive scanario for get_user api
  # status_code based
  def test_get_user(self):
    res = User.get_user('string')
    self.assertEqual(res.status_code, 200)

  def test_get_user_unknown(self):
    res = User.get_user('unknown_user')
    self.assertEqual(res.status_code, 404)

  def test_get_user_empty(self):
    res = User.get_user('')
    self.assertEqual(res.status_code, 405)

  def test_get_user_unicode(self):
    a = '''è'''
    res = User.get_user(a)
    self.assertEqual(res.status_code, 404)

suite = unittest.TestLoader().loadTestsFromTestCase(TestUser)
unittest.TextTestRunner(verbosity=2).run(suite)