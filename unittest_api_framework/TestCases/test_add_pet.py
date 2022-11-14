import unittest
import sys
sys.path.append("/Users/gaurav.mishra/framework/library")
sys.path.append("/Users/gaurav.mishra/framework/library/TestModules")

import Pet

class TestPet(unittest.TestCase):
  """
  Test case TestPet
  """
  def test_add_pet(self):
    payload = {
    "id": 0,
    "category": {
      "id": 0,
      "name": "abc"
    },
    "name": "doggie",
    "photoUrls": [
      "pic"
    ],
    "tags": [
      {
        "id": 0,
        "name": "tag_abc"
      }
    ],
    "status": "available"
    }
    res = Pet.add_pet(payload)
    self.assertEqual(res.status_code, 200)

  def test_add_pet_empty_payload(self):
    payload = {
    }
    res = Pet.add_pet(payload)
    self.assertEqual(res.status_code, 200)

  def test_add_pet_category(self):
    payload = {
    "category": {
      "id": 0,
      "name": "abc"
    }
    }
    res = Pet.add_pet(payload)
    self.assertEqual(res.status_code, 200)

  def test_add_pet_name(self):
    payload = {
    "name": "doggie123"
    }
    res = Pet.add_pet(payload)
    self.assertEqual(res.status_code, 200)

suite = unittest.TestLoader().loadTestsFromTestCase(TestPet)
unittest.TextTestRunner(verbosity=2).run(suite)