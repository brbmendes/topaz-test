import unittest
from unittest.mock import MagicMock

from src.entities.accountings import Accounting
from src.entities.servers import Server


class TestAccounting(unittest.TestCase):
    accounting = None
    def setUp(self):
        self.accounting = Accounting()

    def tearDown(self):
        self.accounting = None

    def test_start_accounting_without_servers(self):
        current = len(self.accounting.get_servers())
        expected = 0
        self.assertEqual(current,expected)

    def test_add_a_server(self):
        server = Server(1,1)
        self.accounting.add_server(server)
        current = len(self.accounting.get_servers())
        expected = 1
        self.assertEqual(current,expected)

    def test_get_set_cost_per_tick(self):
        self.accounting.set_cost_per_tick(3)
        current = self.accounting.get_cost_per_tick()
        expected = 3
        self.assertEqual(current,expected)

    def test_default_value_cost_per_tick(self):
        current = self.accounting.get_cost_per_tick()
        expected = 1
        self.assertEqual(current,expected)

    def test_calculate_cost_usage_without_add_server(self):
        current = self.accounting.calculate_cost_usage()
        expected = 0
        self.assertEqual(current,expected)

    def test_calculate_cost_usage_adding_a_server(self):
        server = Server(1,1)
        self.accounting.add_server(server)
        current = self.accounting.calculate_cost_usage()
        expected = 1
        self.assertEqual(current,expected)


if __name__ == '__name__':
    unittest.main()
