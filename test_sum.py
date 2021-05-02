import unittest

class Tests(unittest.TestCase):
  def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")\

  def test_sum_with_negatives(self):
        self.assertEqual(sum([-4, -4, -4]), -12, "Should be -12")

  def test_sum_with_zeros(self):
        self.assertEqual(sum([0, 0, 0]), 0, "Should be zero")




# if __name__ == '__main__':
#   unittest.main()

