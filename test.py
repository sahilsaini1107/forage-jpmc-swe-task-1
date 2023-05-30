import unittest

from client3 import getDataPoint, getRatio

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.quote = {
            'stock': 'ABC',
            'top_bid': {'price': '10.0'},
            'top_ask': {'price': '12.0'}
        }

    def test_getDataPoint(self):
        # Test the getDataPoint function
        expected_stock = 'ABC'
        expected_bid_price = 10.0
        expected_ask_price = 12.0
        expected_price = 11.0

        stock, bid_price, ask_price, price = getDataPoint(self.quote)

        self.assertEqual(stock, expected_stock)
        self.assertEqual(bid_price, expected_bid_price)
        self.assertEqual(ask_price, expected_ask_price)
        self.assertEqual(price, expected_price)

    def test_getRatio(self):
        # Test the getRatio function
        price_a = 10.0
        price_b = 5.0
        expected_ratio = 2.0

        ratio = getRatio(price_a, price_b)

        self.assertEqual(ratio, expected_ratio)

    def test_getRatio_with_zero_price_b(self):
        price_a = 10.0
        price_b = 0.0
        expected_ratio = None

        ratio = getRatio(price_a, price_b)

        self.assertIsNone(ratio)

if __name__ == '__main__':
    unittest.main()
