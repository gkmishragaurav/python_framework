import unittest
import sys
sys.path.append("/Users/gaurav.mishra/framework/library")
sys.path.append("/Users/gaurav.mishra/framework/library/TestModules")

import Pet

class TestPet(unittest.TestCase):
  """
  Test case TestPet
  """
  def test_update_pet(self):
    payload = {
      "id": 0,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": "doggie",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }
    res = Pet.update_pet(payload)
    self.assertEqual(res.status_code, 200)

suite = unittest.TestLoader().loadTestsFromTestCase(TestPet)
unittest.TextTestRunner(verbosity=2).run(suite)