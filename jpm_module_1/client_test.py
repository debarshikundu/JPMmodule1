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
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """

  def test_getRatio_lessthanone(self):
    price_a = 167.8
    price_b = 276.9
    self.assertLess(getRatio(price_a,price_b),1)
  
  def test_getRatio_greaterthanone(self):
    price_a = 276.9
    price_b = 100.3
    self.assertGreater(getRatio(price_a,price_b),1)
  
  def test_getRatio_equaltoone(self):
    price_a = 100.3
    price_b = 100.3
    self.assertEqual(getRatio(price_a,price_b),1)
  
  def test_getRatio_AZero(self):
    price_a = 0
    price_b = 276.9
    self.assertEqual(getRatio(price_a,price_b),0)

  #ZeroDivisionError 
  def test_getRatio_BZero(self):
    price_a = 167.8
    price_b = 0
    self.assertIsNone(getRatio(price_a,price_b))
    
  
if __name__ == '__main__':
    unittest.main()
