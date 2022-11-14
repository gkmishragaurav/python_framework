import unittest
import sys
sys.path.append("/Users/gaurav.mishra/framework/library")
sys.path.append("/Users/gaurav.mishra/framework/library/TestModules")

import Pet

class TestPet(unittest.TestCase):
  """
  Test case TestPet
  """
  def test_get_pet_available(self):
    res = Pet.get_pet()
    self.assertEqual(res.status_code, 200)
    for item in res.json():
      self.assertEqual(item['status'], 'available')

  def test_get_pet_pending(self):
    res = Pet.get_pet('pending')
    self.assertEqual(res.status_code, 200)
    for item in res.json():
      self.assertEqual(item['status'], 'pending')

  def test_get_pet_sold(self):
    res = Pet.get_pet('sold')
    self.assertEqual(res.status_code, 200)
    for item in res.json():
      self.assertEqual(item['status'], 'sold')

  def test_get_pet_unknown(self):
    res = Pet.get_pet('unknown')
    self.assertEqual(res.status_code, 200)

  def test_get_pet_empty(self):
    res = Pet.get_pet('')
    self.assertEqual(res.status_code, 200)

  def test_get_pet_none(self):
    res = Pet.get_pet(None)
    self.assertEqual(res.status_code, 200)

suite = unittest.TestLoader().loadTestsFromTestCase(TestPet)
unittest.TextTestRunner(verbosity=2).run(suite)