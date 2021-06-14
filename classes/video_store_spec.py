import unittest
from customer import Customer
from inventory import Inventory

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.test_customer = Customer()

    def test_new_id(self):
        self.test_customer.generate_id()
        self.assertTrue(self.test_customer.id, '7')

    def test_get_rentals(self):
        self.assertTrue(self.test_customer.get_rentals('2'),'Prometheus/Split/Sing' )


class TestInventory(unittest.TestCase):
    def setUp(self):
        self.test_inventory = Inventory()

    def test_flavor(self):
        self.assertTrue(type(self.test_inventory.list_inventory), list)

    def test_rent_movie(self):
        self.assertTrue(self.test_inventory.rent_movie('4'), 'Sing')

if __name__ == '__main__':
    unittest.main()