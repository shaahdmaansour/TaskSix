#test if the calculator is working correctly
import unittest
from addCalculator import add

class TestAddFunction(unittest.TestCase):
  def test_add(self):
    #test using positive numbers only
    self.assertEqual(add(3, 5), 8)
    #test using negative numbers only
    self.assertEqual(add(-2, -4), -6)
    #test using both positive and negative numbers
    self.assertEqual(add(7, -3), 4)
    #test adding one zero number
    self.assertEqual(add(0, 5), 5)
    #test adding two zeroes
    self.assertEqual(add(0, 0), 0)    # Both zero

if __name__ == "__main__":
  unittest.main()
