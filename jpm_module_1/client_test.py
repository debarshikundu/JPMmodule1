import unittest
import numpy as np
from client3 import *

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),[quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2])
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),[quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2])

  """ ------------ Add more unit tests ------------ """

  def test_getRatio(self):
    prices = [
      {'price_a':119.2, 'price_b': 121.68},
      {'price_a':122.3, 'price_b': 117.84}
    ]
    for price in prices:
      self.assertNotEqual(np.nan, price[0]/price[1])
      self.assertEqual(getRatio(price[0],price[1]), price[0]/price[1])
      
    
  
if __name__ == '__main__':
    unittest.main()
