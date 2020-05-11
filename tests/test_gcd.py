import unittest
from algorithms.gcd import gcd

class TestGcd(unittest.TestCase):

    def test_true_case1(self):
        self.assertEqual(gcd(36, 48), 12)

    def test_true_case2(self):
        self.assertEqual(gcd(360, 465), 15)


