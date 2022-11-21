import json

import tornado.testing

from addrservice.tornado.app import (
    ADDRESSBOOK_ENTRY_URI_FORMAT_STR
)

from tests.unit.tornado_app_handlers_test import (
    AddressServiceTornadoAppTestSetup
)


class TestAddressServiceApp(AddressServiceTornadoAppTestSetup):
  def test_address_book_endpoints1(self):
    # Get all addresses in the address book, must be ZERO
    r = self.fetch(
      ADDRESSBOOK_ENTRY_URI_FORMAT_STR.format(id=''),
      method='GET',
      headers=None,
    )
    all_addrs = json.loads(r.body.decode('utf-8'))
    self.assertEqual(r.code, 200, all_addrs)
    self.assertEqual(len(all_addrs), 0, all_addrs)
