import unittest

from warehouse.quantity import parse_quantity


class QuantityTests(unittest.TestCase):
    def test_valid_quantity(self):
        self.assertEqual(parse_quantity("5"), 5)
        self.assertEqual(parse_quantity("  12  "), 12)

    def test_zero_quantity(self):
        with self.assertRaises(ValueError):
            parse_quantity("0")

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            parse_quantity("-3")
