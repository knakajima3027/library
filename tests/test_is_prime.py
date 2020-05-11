import unittest
from algorithms.is_prime import is_prime

class TestIsPrime(unittest.TestCase):

    def test_true_case1(self):
        for i in [2, 3, 5, 7, 11, 13, 17]:
            self.assertTrue(is_prime(i))

    def test_true_case2(self):
        for i in [8191,131071, 524287, 6700417]:
            self.assertTrue(is_prime(i))

    def test_false_case1(self):
        for i in [1, 4, 6, 8, 9, 12, 14, 15]:
            self.assertFalse(is_prime(i))

    def test_false_case2(self):
        for i in [6137, 83521, 161595]:
            self.assertFalse(is_prime(i))
